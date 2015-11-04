Separating Line from Continuum in CASA data
###########################################
:date: 2015-11-04 15:57
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA

I'm continuing to try to separate the line forest from the continuum data in my
W51 cube.  Some approaches 'kinda work', some don't.

The iterative approach suggested in the `previous post
<|filename|cvel_w51_fail.rst>`_ `works reasonably well
<https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/630c60e7e57ea7b57877d66b15860b26419a5552/script_12m/uvcontsub_test.py>`_,
but results in oversubtraction of the continuum, even with
a few iterations.  Note that this approach requires `copying columns between ms
files using the table toolkit
<https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/630c60e7e57ea7b57877d66b15860b26419a5552/script_12m/uvcontsub_test.py#L17>`_.

.. image:: |filename|/images/w51/oversubtracted_spectrum.png
   :width: 400px

Another approach I wanted to try was to image the whole cube, take the minimum
value along the spectral axis, and subtract that.  This would avoid the
oversubtraction issue by force.  However, `this
<https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/c58e4fdf755f85b163d1684cc7383ef31d6a1669/script_12m/mincontsub.py>`_
leads to failures in the `ft` task::

    CASA <85>: ft(vis='w51_test_small_imcont.ms', model='test_continuum_min.image', usescratch=True, nterms=1)
    2015-11-04 15:01:29	WARN	ft::FTMachine::initMaps	No overlap in frequency between image channels and selected data found for this FTMachine
    2015-11-04 15:01:29	WARN	ft::FTMachine::initMaps+	 Check your data selection and image parameters if you end up with a blank image

which I don't understand.  I had to `hack the header
<https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/c58e4fdf755f85b163d1684cc7383ef31d6a1669/script_12m/mincontsub.py#L22>`_
just to get ft to load the file at all, and apparently my hack wasn't good enough.
It's really unclear to me now how to load a model from a FITS file.

The next approach is to load the whole continuum-subtracted cube into a model,
subtract THAT, then make a continuum image, then subtract that, then maybe
we have line and continuum?  Maybe?  I suspect this approach will require
some sort of cube masking.

Unfortunately, ft is again the problem::

    2015-11-04 15:09:08	SEVERE	ft::imager::ft() (file /Users/rpmbuild/gradle/workdir/casaautobuild/release-4_5/code/synthesis/MeasurementEquations/Imager.cc, line 4488)	Exception: (/Users/rpmbuild/gradle/workdir/casaautobuild/release-4_5/darwin/include/casacore/lattices/Lattices/Lattice.tcc : 299) Failed AlwaysAssert shapeIn.isEqual (shapeOut)
