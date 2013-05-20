STF measurement attempts, round 3?
##################################
:date: 2011-08-03 02:51
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, discrepancy, simulation
:slug: stf-measurement-attempts-round-3

Below are plots of the spatial transfer function for a variety of
simulation parameters. Each line represents the median (i.e., mean of
the center 2 of 4) spatial transfer function of 4 realizations of the
listed parameters.

.. image:: http://3.bp.blogspot.com/-qAq4e3xotf8/TjJCwJb6knI/AAAAAAAAGXA/mv7hs-uKudI/s320/stfs_atmo01_peak010_smooth.png

.. image:: http://2.bp.blogspot.com/-lTKFbV1Zxno/TjJCwluvOXI/AAAAAAAAGXI/fK7qPWDF0Qw/s320/stfs_atmo10_peak010_smooth.png

.. image:: http://1.bp.blogspot.com/-HNLrsuXSrvA/TjJCwx9xEBI/AAAAAAAAGXQ/a0l3Qljyp04/s320/stfs_atmo10_peak100_smooth.png

A few unfortunate details are apparent:

#. The STF is background dependent, though not strongly
#. The STF appears to never exceed 85%, and be more typically 75%. If
   this is not matched by point-source PSDs, an explanation for the flux
   discrepancy becomes possible
#. The 50% recovery point is much closer in than previously stated, at
   closer to 150" than 300".

Note for comparison that the recovery fraction for point sources is much
more nearly 1, at least in the calibrator type maps. We need to wait for
Jared's simulations with point sources in a full size map to confirm
this, but it seems pretty likely that the STF is different for point
sources and extended structures.

.. image:: http://4.bp.blogspot.com/-n0mH8DTSc80/Tji3c0tOffI/AAAAAAAAGXc/_Xd-AQMo4QU/s320/psf_ds1_reconv_arrang45_atmotest_noise%252B6.3E-04varyrelscale_amp1.0E%252B00_psds.png

.. _|image4|: http://3.bp.blogspot.com/-qAq4e3xotf8/TjJCwJb6knI/AAAAAAAAGXA/mv7hs-uKudI/s1600/stfs_atmo01_peak010_smooth.png
.. _|image5|: http://2.bp.blogspot.com/-lTKFbV1Zxno/TjJCwluvOXI/AAAAAAAAGXI/fK7qPWDF0Qw/s1600/stfs_atmo10_peak010_smooth.png
.. _|image6|: http://1.bp.blogspot.com/-HNLrsuXSrvA/TjJCwx9xEBI/AAAAAAAAGXQ/a0l3Qljyp04/s1600/stfs_atmo10_peak100_smooth.png
.. _|image7|: http://4.bp.blogspot.com/-n0mH8DTSc80/Tji3c0tOffI/AAAAAAAAGXc/_Xd-AQMo4QU/s1600/psf_ds1_reconv_arrang45_atmotest_noise%252B6.3E-04varyrelscale_amp1.0E%252B00_psds.png

