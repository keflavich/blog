Testing out analytic filter functions
#####################################
:date: 2011-07-15 03:03
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, analysis, simulation
:slug: testing-out-analytic-filter-functions

I've attempted to model the spatial filter function as a gaussian (or
PSF) plus an inverse gaussian. i.e., the high-spatial-frequency
components are smoothed with the PSF, and the low spatial frequency
components are convolved with a (1-gaussian) high-pass filter.
First, the mildly good news: With a 300" FWHM large-scale cutoff, the
filter PSD reasonably resembles the iterative map PSD:

.. image:: http://3.bp.blogspot.com/-udANxY5rM98/Th-i7hx3qnI/AAAAAAAAGS0/kwoR30ZO5OI/s320/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_map20filterpsds.png

Luckily, the double-filter goes a very long way in explaining the
scale-free flux loss. In the following diagram, I show the effect of the
filter compared to the input map.

.. image:: http://3.bp.blogspot.com/-iZtSoQjlzJY/Th-jf6oatlI/AAAAAAAAGS8/p8ZcznsKGpI/s320/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_filterpsds.png

The filter only recovers about 75% of the flux at ANY wavenumber. The
map does slightly worse at high frequencies, which I can't explain yet.
These show the recovery fraction of the iterative maps, a gaussian
smoothing function with FWHM=33", and the mid-pass-filter. Map20 (no
smooth) has a lot of additional "noise power" at high spatial
frequencies; if it wasn't for the telescope filter function, we would
apparently have pretty good high-frequency recovery. Hmph.
Note that map20 is higher than the filter at some intermediate
frequencies, but quite a bit lower at higher frequencies. Also note the
moderately poor agreement between the 'smoothed' and 'smoothed (theory)'
lines.

.. image:: http://4.bp.blogspot.com/-zhxfyI_XDNY/Th-qZmsMZaI/AAAAAAAAGTE/550ocw2kFx8/s320/filterfunctions_smoothedx2.png

Finally, look at the comparison between map20 and fiiltered. The
agreement is not bad for positive points; filtered is apparently
slightly higher but that can be adjusted. The problem: the filter forces
some structures that are negative or zero to be positive. For example,
look at the feature at 210,300 that is negative in Map20 but positive in
Filtered. In the real (input) map, this feature is lower than its
surroundings - it is legitimately negative.

.. image:: http://4.bp.blogspot.com/-zH98yuBL7lo/Th-tQIoKYCI/AAAAAAAAGTM/QNqslST6b2c/s320/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_map20filtercompare.png

.. image:: http://2.bp.blogspot.com/-bvlju06_ySU/Th-ttpCOuhI/AAAAAAAAGTU/3zoCyl5gCIY/s320/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_filtercompare.png

.. _|image5|: http://3.bp.blogspot.com/-udANxY5rM98/Th-i7hx3qnI/AAAAAAAAGS0/kwoR30ZO5OI/s1600/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_map20filterpsds.png
.. _|image6|: http://3.bp.blogspot.com/-iZtSoQjlzJY/Th-jf6oatlI/AAAAAAAAGS8/p8ZcznsKGpI/s1600/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_filterpsds.png
.. _|image7|: http://4.bp.blogspot.com/-zhxfyI_XDNY/Th-qZmsMZaI/AAAAAAAAGTE/550ocw2kFx8/s1600/filterfunctions_smoothedx2.png
.. _|image8|: http://4.bp.blogspot.com/-zH98yuBL7lo/Th-tQIoKYCI/AAAAAAAAGTM/QNqslST6b2c/s1600/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_map20filtercompare.png
.. _|image9|: http://2.bp.blogspot.com/-bvlju06_ySU/Th-ttpCOuhI/AAAAAAAAGTU/3zoCyl5gCIY/s1600/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_filtercompare.png

