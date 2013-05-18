Using Guider images to achieve ~arcsecond pointing accuracy
###########################################################
:date: 2012-10-05 14:46
:author: Adam (keflavich@gmail.com)
:tags: googlepost, research ideas, astronomy, observing

.. raw:: html

   <div dir="ltr" style="text-align: left;">

One of the challenges of observing in the near-IR / optical is field
identification. In the case of the Apache Point Observatory 3.5m, the
"raw" pointing - i.e., if you enter a coordinate and press "slew" - is
usually good to within ~1 arcminute. However, once you're on the target
field, it's up to you as the observer to identify the exact location
within the 5x5' field to observe.
This proves quite challenging in crowded fields, especially with
rotation. It is far more difficult, though, in sparse fields when your
target is a faint emission line feature - there will be no corresponding
light in your guider image. But you still want ~arcsecond pointing
accuracy.
I think this can be achieved by using the astrometry.net source
recognition and field identification tools, but highly constrained to be
within ~10' of the target field. The WCS coordinates would then be
applied to the guider image, and the target location identified and
translated into a telescope pointing offset.
This technique is probably not needed for most spectroscopic
observations (e.g., of bright point sources). However, for
slit-scan-mapping or observations of faint point sources, this approach
provides the opportunity to do fast-switching with a bright calibration
star so that telluric correction can be provided on a short (~5-10
minute) timescale, as is needed for truly accurate calibration.

.. raw:: html

   </div>

.. raw:: html

   </p>

