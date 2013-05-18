Aperture Photometry
###################
:date: 2011-08-13 02:50
:author: Jared (noreply@blogger.com)
:tags: googlepost, aperture photometry, point source
:slug: aperture-photometry

So the code to add point sources to the maps and perform basic aperture
photometry has started working to the point where I can share some
results.

.. raw:: html

   <div>

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   <div>

For maps with no underlying sky structure, only point sources, recovery
is very nearly perfect, with PearsonR coefficients essentially equal to
1 until the peak amplitude of the point sources drops below 2.0 (and
even then they only drop to ~0.997)

.. raw:: html

   </div>

.. raw:: html

   <div>

Below is a sample of the difference residual of output-input flux vs
input flux for 40", 80" and 120" apertures

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </div>

`|image0|`_\ This may look relatively scattered, but this plot of output
flux vs input flux will show just how correlated these are:

.. raw:: html

   <div>

`|image1|`_

.. raw:: html

   </p>

.. raw:: html

   <div>

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   <div>

Note that for the blank maps, these are taken from simulations using a
power law distribution of point sources from 0.1 to 2.0 Jy in magnitude
(if we allow the range to extend above 2.0 Jy, the recoveries become
even more closely correlated.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   <div>

As for simulations with background sky structure we see similar patterns
for the most part, however a few interesting pieces appear:

.. raw:: html

   </div>

.. raw:: html

   <div>

For the 4 different source ranges I ran, the 80" aperture had the
highest pearson r coefficient across all simulations. Generally sitting
around 0.95 with the 40" and 120" apertures floating from 0.75-0.9. This
may be a fluke, however, I need to run more simulations to see if this
is reproducible with other seeds.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   <div>

Also, in the difference residuals we can clearly see an underrecovery of
flux as input flux increases, which we should probably work to quantify,
as seen by this example:

.. raw:: html

   </div>

`|image2|`_

.. raw:: html

   <div>

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   </p>

.. _|image3|: http://2.bp.blogspot.com/-j5k--Oz92T0/TkXiYHLWjQI/AAAAAAAAABc/MnRtjz6hAMo/s1600/exp13_ds2_astrosky_arrang45_srcpeakalpha002.00source_range_00.1_02.0ptsrc_brightness_diffresid.png
.. _|image4|: http://3.bp.blogspot.com/-zL6VyzobtkU/TkXix_KEExI/AAAAAAAAABk/6vYph5jtyM4/s1600/exp13_ds2_astrosky_arrang45_srcpeakalpha002.00source_range_00.1_02.0ptsrc_brightness_lin.png
.. _|image5|: http://1.bp.blogspot.com/-X4lP1Pl4PLg/TkXka4eio7I/AAAAAAAAABs/RCKTuX14PD8/s1600/exp13_ds2_astrosky_arrang45_atmotest_amp2.0E%252B01_sky00_seed00_peak001.00_smooth_srcpeakalpha002.00source_range_00.1_02.0_wptsrcptsrc_brightness_diffresid.png

.. |image0| image:: http://2.bp.blogspot.com/-j5k--Oz92T0/TkXiYHLWjQI/AAAAAAAAABc/MnRtjz6hAMo/s320/exp13_ds2_astrosky_arrang45_srcpeakalpha002.00source_range_00.1_02.0ptsrc_brightness_diffresid.png
.. |image1| image:: http://3.bp.blogspot.com/-zL6VyzobtkU/TkXix_KEExI/AAAAAAAAABk/6vYph5jtyM4/s320/exp13_ds2_astrosky_arrang45_srcpeakalpha002.00source_range_00.1_02.0ptsrc_brightness_lin.png
.. |image2| image:: http://1.bp.blogspot.com/-X4lP1Pl4PLg/TkXka4eio7I/AAAAAAAAABs/RCKTuX14PD8/s320/exp13_ds2_astrosky_arrang45_atmotest_amp2.0E%252B01_sky00_seed00_peak001.00_smooth_srcpeakalpha002.00source_range_00.1_02.0_wptsrcptsrc_brightness_diffresid.png
.. |image3| image:: http://2.bp.blogspot.com/-j5k--Oz92T0/TkXiYHLWjQI/AAAAAAAAABc/MnRtjz6hAMo/s320/exp13_ds2_astrosky_arrang45_srcpeakalpha002.00source_range_00.1_02.0ptsrc_brightness_diffresid.png
.. |image4| image:: http://3.bp.blogspot.com/-zL6VyzobtkU/TkXix_KEExI/AAAAAAAAABk/6vYph5jtyM4/s320/exp13_ds2_astrosky_arrang45_srcpeakalpha002.00source_range_00.1_02.0ptsrc_brightness_lin.png
.. |image5| image:: http://1.bp.blogspot.com/-X4lP1Pl4PLg/TkXka4eio7I/AAAAAAAAABs/RCKTuX14PD8/s320/exp13_ds2_astrosky_arrang45_atmotest_amp2.0E%252B01_sky00_seed00_peak001.00_smooth_srcpeakalpha002.00source_range_00.1_02.0_wptsrcptsrc_brightness_diffresid.png
