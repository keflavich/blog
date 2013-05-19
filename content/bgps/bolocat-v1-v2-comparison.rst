Bolocat v1-v2 comparison
########################
:date: 2011-08-23 04:39
:author: Adam (noreply@blogger.com)
:tags: googlepost, bolocat, version comparison
:slug: bolocat-v1-v2-comparison

For this experiment, I ran Bolocat on all of the v1 and v2 images using
the source masks Erik derived for v1. I then compared the derived fluxes
using both aperture photometry (as defined in bolocat) and the mask
sums.

First, note that the object\_photometry code Erik wrote does NOT do
background subtraction - this is important for understanding
non-multiplicative offsets between v1 and v2.

I fit a 2-parameter model (a line) to the v2 vs v1 plots using two
methods. The simple linear-least-squares method is one we're all
familiar with, and it gives semi-reasonable results, but is NOT
statistically robust when there are errors on both axes. The other fit
method used was Total Least Squares, which is approximately equivalent
to Principle Component Analysis with 2 vectors. It uses components of
the singular-value-decomposition to determine the best fit. The fits
returned by TLS should be more robust, though the additive offsets need
not be.

Conclusion: Our factor of 1.5 looks like it was pretty accurate. For 40"
apertures, the best fit is ~1.56, which is easily within the error bars.
Luckily, for 40" apertures, there is no apparent need for an additive
offset (I'm pretty sure the uncertainty on the measured offset is larger
than the offset, though statistically that is not the case), which would
complicate things.

However, for the source mask, there is a greater scaling factor and a
very substantial offset. This implies that the peaks in v2 are brighter
by a large factor, but the backgrounds in v2 are actually lower than in
v1 (though please do check my reasoning here). I'm really not sure what
to make of the difference between source mask and aperture yet,
though... there's probably something significant in the source mask
being forced to pick positive pixels. (and peppered pickles)

.. image:: http://2.bp.blogspot.com/-9a-O_TQx3Ek/TlMr1f-nmKI/AAAAAAAAGbs/Tp6UY_vwl_s/s320/total_v1v2_40arcsec_fit_compare.png

.. image:: http://2.bp.blogspot.com/-zhLxvflZ-30/TlMr1mWy6kI/AAAAAAAAGb0/GH7xSizIjnk/s320/total_v1v2_sourcemask_fit_compare.png

.. _|image2|: http://2.bp.blogspot.com/-9a-O_TQx3Ek/TlMr1f-nmKI/AAAAAAAAGbs/Tp6UY_vwl_s/s1600/total_v1v2_40arcsec_fit_compare.png
.. _|image3|: http://2.bp.blogspot.com/-zhLxvflZ-30/TlMr1mWy6kI/AAAAAAAAGb0/GH7xSizIjnk/s1600/total_v1v2_sourcemask_fit_compare.png

