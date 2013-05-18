Examining bolocat
#################
:date: 2011-07-27 22:51
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, bolocat, analysis, simulation
:slug: examining-bolocat

Just in case we were wondering, the V1 bolocat is completely
inconsistent with a lognormal distribution, but is perfectly consistent
(or... at least reasonably consistent...) with a power law distribution.

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

These plots show power-law fits (red) and lognormal fits (blue) to the
data (black). It's pretty obvious that the lognormal is a bad fit, but
in case you're unconvinced, the ks test for the "source flux" has a
probability 1.6e-7, and it is the highest likelihood by 17 orders of
magnitude out of the 4 flux types.
By contrast, the simulations are on average (though not uniformly) more
consistent with lognormal than powerlaw distributions:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image4|`_

.. raw:: html

   </div>

Even in those examples where the KS test is slightly more favorable for
the powerlaw distribution, the lognormal is a pretty good fit, and the
failure points for the two distributions are in about the same place.
The smoothness of the lognormal distribution is required to reproduce
the observed distribution.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image5|`_

.. raw:: html

   </div>

Note that the first 4 plots are for the whole BGPS survey. What about an
individual field? For obvious reasons, I choose l30 again.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image6|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image7|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image8|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image9|`_

.. raw:: html

   </div>

This gets to be a little more interesting - apparently the "source flux"
has a tendency to pick up the power-law distributed background
structure, since it is consistent with a lognormal (but note that it is
also consistent with a powerlaw! The ks test doesn't really say
definitively which is better). Although the fits look bad at high flux,
note that this is a log-log plot and therefore the difference in
probability is rather small.
What does this all indicate? It's not entirely clear whether individual
fields are genuinely more lognormally-distributed or whether the number
statistics are just worse. However, even the source flux is consistent
with a power-law, while many realizations of the simulations are not.
Therefore, we should perform the next logical test - add point sources
drawn from a power-law distribution (and a log-normal distribution?) and
see what bolocat retrieves. We can at least say now that the point
source contribution cannot be ignored, since there is no power-law
distribution that can reproduce the observed bolocat flux distribution.

.. raw:: html

   </p>

.. _|image10|: http://2.bp.blogspot.com/-kKaOXdf9hW4/TjBRmgiNmqI/AAAAAAAAGUI/4H0KJk70F_o/s1600/bolocat_flux_cdf.png
.. _|image11|: http://1.bp.blogspot.com/-3T9mrt5U39E/TjBRm5p7inI/AAAAAAAAGUQ/ARP6EKQDYo0/s1600/bolocat_flux40_cdf.png
.. _|image12|: http://4.bp.blogspot.com/-ytrgQo5XYEg/TjBRndOQqOI/AAAAAAAAGUY/9g--hpa5X0Y/s1600/bolocat_flux80_cdf.png
.. _|image13|: http://3.bp.blogspot.com/-TqVY1B1uGLw/TjBRnt6uLEI/AAAAAAAAGUg/FhXct0wpEio/s1600/bolocat_flux120_cdf.png
.. _|image14|: http://2.bp.blogspot.com/-lpOaHHV3e3Q/TjCTzm9RwFI/AAAAAAAAGWI/o57oH5SfdqE/s1600/simulations_ksvalues_lognormvspowerlaw.png
.. _|image15|: http://1.bp.blogspot.com/-8_WCGM_8AjM/TjB2tW_JZeI/AAAAAAAAGU4/SDR1guNcNq0/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky07_seed00_peak100.00_smooth_bolocat_cdf.png
.. _|image16|: http://1.bp.blogspot.com/-vHQoJtAe-vU/TjCIiVcRHsI/AAAAAAAAGVo/04fA4WSCnlA/s1600/bolocat_flux40_L30_cdf.png
.. _|image17|: http://1.bp.blogspot.com/-kIpe2v9_YpQ/TjCIimC8K2I/AAAAAAAAGVw/-o5GZ7DoLOw/s1600/bolocat_flux80_L30_cdf.png
.. _|image18|: http://2.bp.blogspot.com/-Shg66Vp6sUI/TjCIi2HEe4I/AAAAAAAAGV4/na0n21atNsI/s1600/bolocat_flux120_L30_cdf.png
.. _|image19|: http://1.bp.blogspot.com/-R2zq58aXXyI/TjCIjeTdjHI/AAAAAAAAGWA/D3xEDRAgY7M/s1600/bolocat_flux_L30_cdf.png

.. |image0| image:: http://2.bp.blogspot.com/-kKaOXdf9hW4/TjBRmgiNmqI/AAAAAAAAGUI/4H0KJk70F_o/s320/bolocat_flux_cdf.png
.. |image1| image:: http://1.bp.blogspot.com/-3T9mrt5U39E/TjBRm5p7inI/AAAAAAAAGUQ/ARP6EKQDYo0/s320/bolocat_flux40_cdf.png
.. |image2| image:: http://4.bp.blogspot.com/-ytrgQo5XYEg/TjBRndOQqOI/AAAAAAAAGUY/9g--hpa5X0Y/s320/bolocat_flux80_cdf.png
.. |image3| image:: http://3.bp.blogspot.com/-TqVY1B1uGLw/TjBRnt6uLEI/AAAAAAAAGUg/FhXct0wpEio/s320/bolocat_flux120_cdf.png
.. |image4| image:: http://2.bp.blogspot.com/-lpOaHHV3e3Q/TjCTzm9RwFI/AAAAAAAAGWI/o57oH5SfdqE/s320/simulations_ksvalues_lognormvspowerlaw.png
.. |image5| image:: http://1.bp.blogspot.com/-8_WCGM_8AjM/TjB2tW_JZeI/AAAAAAAAGU4/SDR1guNcNq0/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky07_seed00_peak100.00_smooth_bolocat_cdf.png
.. |image6| image:: http://1.bp.blogspot.com/-vHQoJtAe-vU/TjCIiVcRHsI/AAAAAAAAGVo/04fA4WSCnlA/s320/bolocat_flux40_L30_cdf.png
.. |image7| image:: http://1.bp.blogspot.com/-kIpe2v9_YpQ/TjCIimC8K2I/AAAAAAAAGVw/-o5GZ7DoLOw/s320/bolocat_flux80_L30_cdf.png
.. |image8| image:: http://2.bp.blogspot.com/-Shg66Vp6sUI/TjCIi2HEe4I/AAAAAAAAGV4/na0n21atNsI/s320/bolocat_flux120_L30_cdf.png
.. |image9| image:: http://1.bp.blogspot.com/-R2zq58aXXyI/TjCIjeTdjHI/AAAAAAAAGWA/D3xEDRAgY7M/s320/bolocat_flux_L30_cdf.png
.. |image10| image:: http://2.bp.blogspot.com/-kKaOXdf9hW4/TjBRmgiNmqI/AAAAAAAAGUI/4H0KJk70F_o/s320/bolocat_flux_cdf.png
.. |image11| image:: http://1.bp.blogspot.com/-3T9mrt5U39E/TjBRm5p7inI/AAAAAAAAGUQ/ARP6EKQDYo0/s320/bolocat_flux40_cdf.png
.. |image12| image:: http://4.bp.blogspot.com/-ytrgQo5XYEg/TjBRndOQqOI/AAAAAAAAGUY/9g--hpa5X0Y/s320/bolocat_flux80_cdf.png
.. |image13| image:: http://3.bp.blogspot.com/-TqVY1B1uGLw/TjBRnt6uLEI/AAAAAAAAGUg/FhXct0wpEio/s320/bolocat_flux120_cdf.png
.. |image14| image:: http://2.bp.blogspot.com/-lpOaHHV3e3Q/TjCTzm9RwFI/AAAAAAAAGWI/o57oH5SfdqE/s320/simulations_ksvalues_lognormvspowerlaw.png
.. |image15| image:: http://1.bp.blogspot.com/-8_WCGM_8AjM/TjB2tW_JZeI/AAAAAAAAGU4/SDR1guNcNq0/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky07_seed00_peak100.00_smooth_bolocat_cdf.png
.. |image16| image:: http://1.bp.blogspot.com/-vHQoJtAe-vU/TjCIiVcRHsI/AAAAAAAAGVo/04fA4WSCnlA/s320/bolocat_flux40_L30_cdf.png
.. |image17| image:: http://1.bp.blogspot.com/-kIpe2v9_YpQ/TjCIimC8K2I/AAAAAAAAGVw/-o5GZ7DoLOw/s320/bolocat_flux80_L30_cdf.png
.. |image18| image:: http://2.bp.blogspot.com/-Shg66Vp6sUI/TjCIi2HEe4I/AAAAAAAAGV4/na0n21atNsI/s320/bolocat_flux120_L30_cdf.png
.. |image19| image:: http://1.bp.blogspot.com/-R2zq58aXXyI/TjCIjeTdjHI/AAAAAAAAGWA/D3xEDRAgY7M/s320/bolocat_flux_L30_cdf.png
