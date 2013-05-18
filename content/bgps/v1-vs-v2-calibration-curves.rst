V1 vs V2: Calibration Curves
############################
:date: 2011-08-25 17:09
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, calibration, version comparison
:slug: v1-vs-v2-calibration-curves

Why did we find a factor ~1.8 in `the previous post`_? Well, for
starters we used a calibration curve that was based off of 'masking' and
other tricky techniques.
The calibration curves below are the first ever produced
self-consistently, i.e. using the EXACT same pipeline with the EXACT
same parameters as the science data. No hacks were needed to produce
these\ `\*`_. The recovered Volts/Jy are substantially higher than
BGPSv1 and ALSO higher than the curve used about a year ago in an
attempt to explain the v1 flux discrepancy.
Remember that a higher calibration curve means a LOWER recovered flux. I
haven't finished the check, but odds are pretty good that applying these
self-consistent cal curves will reduce the v2 data to be about 1.5.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image1|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image2|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image3|`_

.. raw:: html

   </div>

.. raw:: html

   <div name="&quot;asterisk">

While no hacks were needed to produce these plots, there were abundant
problems. There are far fewer data points than there should be. The
problems are manifold, but mostly have to do with the PCA scaling (I
think).
In some cases, the first scan in an observation was wildly variable.
There looked to be an exponential or similar decay (as has been observed
in scan turnarounds) at the observation start that took ~3 scans to
decay to bring all of the bolometers onto a scaleable curve. This is a
HUGE problem, because the assumption that the dominant signal is
atmosphere is badly violated in this situation - the signal becomes
electronics-dominated. The first PCA component is then an ugly
step-function. With these first scans flagged out, the whole problem
goes away, but that's a painful manual process. Automating it MAY be
possible, but also risky.
In other cases, particularly September 4th 2007, the atmosphere appeared
to be negligible! While the atmospheric optical depth probably was not,
if it was extraordinarily stable over the course of ~10 minutes, again
we experience severe problems. A stable atmosphere means no atmospheric
variation, which means that ACBOLOS is just noise (plus Uranus signal).
Ironically, this is very bad for calibration - it means there is no
common signal on which we can calibrate the bolos' relative
sensitivities. This problem doesn't seem to affect science data,
probably because there's no such thing as 45-minute stable atmosphere
(especially when you're following rising/setting sources). If I REALLY
need that data, I could snag the relative scalings from a science field
and apply them to the cal data... honestly that's not a bad idea in
general... hmm... Well, we'll explore that later if I have time, that
will take days to implement.

.. raw:: html

   </p>

.. _the previous post: http://bolocam.blogspot.com/2011/08/bolocat-v1-v2-comparison.html
.. _\*: #asterisk"
.. _|image4|: http://4.bp.blogspot.com/-PRU4LQ5f-C4/TlZ9wpeFBeI/AAAAAAAAGb8/jKdJHtIqV40/s1600/planet_dcfluxes_05_defaults_ds2_v2.0_13pca_map20.png
.. _|image5|: http://3.bp.blogspot.com/-AIzsETyl69g/TlZ9w50DjBI/AAAAAAAAGcE/h5ggKhH3dO4/s1600/planet_dcfluxes_06_defaults_ds2_v2.0_13pca_map20.png
.. _|image6|: http://4.bp.blogspot.com/-BNWD4QQ21Ac/TlZ9xZ5eTkI/AAAAAAAAGcM/QOVbum2jXIo/s1600/planet_dcfluxes_07_defaults_ds2_v2.0_13pca_map20.png
.. _|image7|: http://2.bp.blogspot.com/-OucWo74b8VY/TlZ9yFIJYQI/AAAAAAAAGcU/IBMs5YLMlYU/s1600/planet_dcfluxes_09_defaults_ds2_v2.0_13pca_map20.png

.. |image0| image:: http://4.bp.blogspot.com/-PRU4LQ5f-C4/TlZ9wpeFBeI/AAAAAAAAGb8/jKdJHtIqV40/s320/planet_dcfluxes_05_defaults_ds2_v2.0_13pca_map20.png
.. |image1| image:: http://3.bp.blogspot.com/-AIzsETyl69g/TlZ9w50DjBI/AAAAAAAAGcE/h5ggKhH3dO4/s320/planet_dcfluxes_06_defaults_ds2_v2.0_13pca_map20.png
.. |image2| image:: http://4.bp.blogspot.com/-BNWD4QQ21Ac/TlZ9xZ5eTkI/AAAAAAAAGcM/QOVbum2jXIo/s320/planet_dcfluxes_07_defaults_ds2_v2.0_13pca_map20.png
.. |image3| image:: http://2.bp.blogspot.com/-OucWo74b8VY/TlZ9yFIJYQI/AAAAAAAAGcU/IBMs5YLMlYU/s320/planet_dcfluxes_09_defaults_ds2_v2.0_13pca_map20.png
.. |image4| image:: http://4.bp.blogspot.com/-PRU4LQ5f-C4/TlZ9wpeFBeI/AAAAAAAAGb8/jKdJHtIqV40/s320/planet_dcfluxes_05_defaults_ds2_v2.0_13pca_map20.png
.. |image5| image:: http://3.bp.blogspot.com/-AIzsETyl69g/TlZ9w50DjBI/AAAAAAAAGcE/h5ggKhH3dO4/s320/planet_dcfluxes_06_defaults_ds2_v2.0_13pca_map20.png
.. |image6| image:: http://4.bp.blogspot.com/-BNWD4QQ21Ac/TlZ9xZ5eTkI/AAAAAAAAGcM/QOVbum2jXIo/s320/planet_dcfluxes_07_defaults_ds2_v2.0_13pca_map20.png
.. |image7| image:: http://2.bp.blogspot.com/-OucWo74b8VY/TlZ9yFIJYQI/AAAAAAAAGcU/IBMs5YLMlYU/s320/planet_dcfluxes_09_defaults_ds2_v2.0_13pca_map20.png
