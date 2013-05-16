BGPS Point Source Recovery
##########################
:date: 2013-05-16 12:21
:author: Adam (keflavich@gmail.com)
:tags: bgps, simulations, pointsource, bolocat


In the last couple drafts of the BGPS paper (e.g. `the May 15, 2013 draft
<https://github.com/keflavich/bgpsv2/blob/master/v2_draft0515.pdf?raw=true>`_),
we've included a single simulation demonstrating the flux recovery of the
Bolocat:

.. image:: https://raw.github.com/keflavich/bgpsv2/master/figures/in_vs_out_bolocat_FLUX_40.png?login=keflavich&token=8ff3096beef7bf15627a7a6b7363cb49
    :width: 800
.. image:: https://raw.github.com/keflavich/bgpsv2/master/figures/in_vs_out_bolocat_FLUX_120.png?login=keflavich&token=2c6e9896c5df6824e9881c94d6af542f
    :width: 800

These figures are regarded as very important, as they demonstrate the
capability of recovering accurate flux density measurements from a realistic
sky using bolocat.

However, the above figures show a simulation only for one set of parameters,
with :math:`\alpha=1` in the power-law flux distribution, which unfortunately
is not realistic according to "Figure 8":

.. image:: https://github.com/keflavich/bgpsv2/raw/master/figures/l030_higal_bgps_powerspec_compare.png
    :width: 800


So I've started up a new experiment, experiment #23, to examine this problem. 

The problem has a few layers:

1. The reason I used :math:`\alpha=1` is that it looks much like a realistic
   BGPS map after processing, in the sense that most of the field is empty
   but there are a few hundred sources in the map.  However, :math:`\alpha=1`
   is not a realistic representation of the measured power spectra.
2. :math:`\alpha=2` maps with the previous normalization had a peak value of
   18 Jy, which resulted in heavily signal-dominated output maps that did not
   resemble BGPS maps.
3. The normalization is tricky.  One of the key goals of the simulations was to
   test the effect of different atmospheric to astrophysical signal ratios on
   the angular transfer function; in order to accomplish this, it was necessary
   to scale the atmospheric power based on the astrophysical power at its peak
   in fourier space.  i.e., in real timestreams, we can measure the astrophysical
   to atmospheric power ratio, but we have to perform that measurement somewhere
   that the angular transfer function is known to be reliable.  This is done at
   about 1 Hz.  
4. The normalization is important because of the noise level.  In the
   simulations, we use a fixed noise level of about 30 mJy in the timestreams
   to match our best observations (though it is not difficult to scale this to
   other levels).  This fixed noise level means that, for some normalizations,
   all pixels are statistically significant.  Also, even though the noise level
   is fixed, it will be higher because of intrinsic noise in a power-law
   distributed map.
5. The normalizations used in experiment #21, the angular transfer function
   measurement, were selected such that there would be high signal-to-noise at
   all angular scales.  This means that white noise would not be dominant on
   any angular scale, since white noise is equivalent to :math:`\alpha=0`.  So
   it wasn't crazy to use these ridiculously high-flux maps, but it is not
   feasible to use the same maps for analysis of point sources.  In maps for
   which we're interested in small-angular-scale features (<100"), we want the
   maps to be primarily noise-dominated with a handful of bright features
   either caused by adding point sources directly or from the local peaks in
   the power-law distributed flux.


