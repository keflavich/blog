Single Dish - Interferometer Combination Experiments
####################################################
:date: 2016-06-01 11:17
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, uv combination


I spent 3 days in Köln with Alvaro Sanchez-Mongé, Peter Schilke, Fanyi Meng,
and Anika Schmiedeke working on Sgr B2 data and specifically on trying to
combine the single dish (total power) data with my merged ACA+12m data from
ALMA program 2013.1.00269.S.

tl;dr: feathering appears to work fine, and many other methods work equally
well (assuming they can be implemented, which is uniformly harder).  Negative
bowls persisting after feathering are an indication of a problem with the input
data.


Feathering
----------
Fourier space combination of the single-dish and interferometric data is by
far the most straightforward to implement and the fastest.  However, in the HC3N
data, it left strong negative bowls, which should not be possible.

On the Einstein image, the image quality from feathering was not great, but
there were no negative bowls left.  The dynamic range is lower in the Einstein
data, but this still hints that there is a problem with the HC3N images.  We're
investigating the possibility that the 7m data are improperly calibrated or
weighted.


Miriad
------
We never managed to create UV data from the single dish data because of complaints about
the pointing information.


Cleaning with a single dish image as an input model
---------------------------------------------------
We attempted to clean the data using the single dish image as an input model.

On the real data, this failed with both tclean and clean.  With ``tclean``, there
was no error message, it just hung indefinitely.
With ``clean``, the error message is::

    *** Error ***  LatticeExprNode - coordinates of operands mismatch
    Scanned so far: modelos_0 + __temp_model2

    2016-06-01 10:35:05     SEVERE  clean::::       An error occurred running task clean.

Changing CDELT to 1 GHz, which solved a previous issue, had no effect here.


It turns out ``tclean`` will fail silently if it doesn't find the
``startmodel``, which has to be specified as an image *prefix* for version
<=4.6, and the image has to exist as a ``.model`` file.  For higher versions, 4.6+,
the model can be directly referenced (as in clean).  Eventually, tclean seems to have
completed, though the results indicate that it does not treat the units as I expected;
the total power data seems to be over-weighted by a factor of 10^3+, probably by the ratio
of the beam areas:

.. image:: http://i.imgur.com/8dW7t8I.png
   :width: 600px

For the simulated images (einstein), we get the error::

    2016-06-01 10:55:11	SEVERE	SynthesisImager::defineImage (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/ImagerObjects/SynthesisImager.cc, line 668)	Error in adding Mapper : Error in createImStore : ::operator!= (const IPosition&, const IPosition&) - left and right operand do not conform
    2016-06-01 10:55:11	SEVERE	tclean::task_tclean::	Exception from task_tclean : 2016-06-01 10:55:11	SEVERE	SynthesisImager::defineImage (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/ImagerObjects/SynthesisImager.cc, line 668)	Error in adding Mapper : Error in createImStore : ::operator!= (const IPosition&, const IPosition&) - left and right operand do not conform

This is probably an issue with regridding.  ``imregrid`` doesn't like our data::

    2016-06-01 11:00:41	SEVERE	imregrid::image::regrid	Exception Reported: Exception: The number of pixel axes in the output shape and Coordinate System must be the same. Shape has size 4. Output coordinate system has 3 axes.
    2016-06-01 11:00:41	SEVERE	imregrid::image::regrid+	... thrown by SPIIF casa::ImageRegridder::_regrid() const at File: /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/imageanalysis/ImageAnalysis/ImageRegridder.cc, line: 138

Adding a frequency axis to the FITS data (which was missing before...) seems to
have fixed this error for the Einstein data, but not for the real HC3N data.

.. (this is now incorporated in an above paragraph)
.. tclean appears to use the wrong units for the input model, treating that model
.. very differently than ``clean`` does.  This error may be limited to CASA <=
.. 4.5, since the tclean documentation regarding models changed substantially from
.. 4.5 to 4.6.

Linear Combination in Image Space
---------------------------------
Linear combination of the single dish and interferometer data in image space,
followed by image-space deconvolution, has been used successfully on HI data.
In principle, this is very straightforward, except for the need for
deconvolution.  CASA now has an image-space deconvolution program
(``deconvolve``), so I was able to implement this approach.  However, the
deconvolver seems to only work on the inner 1/4 of the image in each dimension,
which left incomplete images that were difficult to compare.  Additionally,
CASA does not (obviously) carry the appropriate machinery for computing the
residual image and adding the convolved model back to the residual image.
Still, this is a promising route forward as it is computationally relatively
cheap and mostly easy to implement.

Linear combination is partly implemented now using the CASA ``deconvolve`` task;
it hasn't been generalized but you can see the outline / single working case at
`this link
<https://github.com/radio-astro-tools/uvcombine/blob/master/uvcombine/realspace_combine.py>`__.

.. this is how you include images
.. .. image:: |static|/images/psfFfftF.png
..    :width: 600px
