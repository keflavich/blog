What does feather do?
#####################
:date: 2016-05-26 08:29
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa


This is an examination of the 'feather' task in CASA.

First we have to track down what code is actually called.

On mac, this is:
/Applications/CASA.app/Contents/Resources/python/feather_cli.py -> feather_cli
/Applications/CASA.app/Contents/Resources/python/task_feather.py -> feather
/Applications/CASA.app/Contents/Resources/python/taskinit.py -> imtool->imager->casac.imager->/Applications/CASA.app/Contents/Resources/python/feather_cli.py
`https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Imager.cc#L2257`__

Within the imager, `setvp` is used to do something with the primary beam.  As
far as I can tell, this function spews a lot of text into the logger, sets
local variables, sets one larger-scope variable `BeamSquint::`, then does
`destroySkyEquation();`.  In short, I don't know what this does.  Probably my
reading of the C code is incorrect and these variables are *not* local, in
which case it is just setting a bunch of default beam parameters.

Then, `Imager.cc` calls `Feather.cc
<https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L1211>`__.

Feather sets parameters based on the effective dish diameter.  It uses
`1.22*(speed of light)/frequency/dish_diameter
<https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L244>`__,
so it is retrieving the FWHM
assuming a Gaussian beam by default.

A lovely aside: `Imager.cc` passes the local variable `lowPassFilterSD
<https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Imager.cc#L2320>`__
to `Feather.cc`, which is read in to the input boolean parameter
`doHiPassFilterOnSD
<https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L244>`__.
That seems like a potential place for confusion.

If `doHiPassFilterOnSD` is set *or* the effective beam diameter is set as a
parameter, the single dish image is deconvolved with its beam using the
GaussianDeconvolver.  This is actually disabled by default, though.

The low resolution image is `regridded <https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L142>`__
to match the high resolution image.

The `applyFeather <https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L375>`__
command seems to do the actual work.
It starts with `calcCWeightImage <https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L414>`__,
which sets the "weight" to one minus the peak-normalized fourier transform of
the low-resolution (single-dish) beam
`https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L427`__,
with the result stored in the variable `cwImage_p`.
`applyFeather <https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L408>`__ then just
multiplies the high-resolution image by this weight.

Back in the `saveFeatheredImage
<https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L695>`__
task, the single-dish data are fourier transformed, then a scaling factor, the ratio
between the low and high beam areas, is computed.  Finally, the single-dish
(scaled) and interferometer `fourier-transformed <https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L694>`__ images are `added
<https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L703>`__.

Is the single-dish image weighted by the beam at all?  The single-dish image will
be convolved with a kernel only if `doHighPassFilterOnSD <https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L1235>`__ is set
or if the effective dish diameter is set.  If the beam is the same size as the original
beam, nothing will happen.
In `setEffectiveDishDiam
<https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/synthesis/MeasurementEquations/Feather.cc#L256>`__
the low-resolution image is convolved with the `*deconvolved*
<https://github.com/radio-astro/casa/blob/160955adf4de4ee561cfc691904317953e08d7d6/code/components/ComponentModels/GaussianDeconvolver.cc#L34>`__
beam.

The most important note in this post is that the single-dish image is *not*
weighted unless `doHighPassFilterOnSD` is set, and even then nothing will be
done if the single-dish beam size passed as a parameter is the same as the beam
size specified in the header.  That means only the interferometer image is
weighted.  Maybe that is the correct behavior?  By weighting by (1-convolved
beam), which means setting the total flux in the interferometer image to zero,
the process is guaranteed to be flux conserving.

.. this is how you include images
.. .. image:: |filename|/images/psfFfftF.png
..    :width: 600px
