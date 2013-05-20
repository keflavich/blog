Bolocat v1-v2 comparison with new calibration
#############################################
:date: 2011-08-30 21:04
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, bolocat, version comparison
:slug: bolocat-v1-v2-comparison-with-new-calibration

.. image:: http://2.bp.blogspot.com/-c3_0Rlbv2qM/Tl1P5FhWC8I/AAAAAAAAGdc/oiFxmO7vrUU/s320/total_v1v2_40arcsec_ratio_compare.png

.. image:: http://4.bp.blogspot.com/-Gk60vlSPkWk/Tl1P5c4THoI/AAAAAAAAGdk/E7zdIwtyD3w/s320/total_v1v2_40arcsec_fit_compare.png

I re-examined the Bolocat data on l351 after re-running the pipeline
with the new calibration curve. The change wasn't all that great. See
`this post`_ for a brief description of the procedure.
In the data below, I've fit the residuals as a function of v1.0.2 flux
density in an aperture (source mask) with a line. The slope of the line
should ideally be zero - that would indicate a multiplicative offset is
an acceptable correction.
Nicely, in the 40" aperture case, I see no reason to exclude the m=0
case. For the most reliable data - the 13pca - the slope is rather small
and the "correction factor" is disturbingly close to what we recommended
(1.5). We have no right to be that lucky...

.. image:: http://2.bp.blogspot.com/-W08ZvMS3M90/TlwhPW62NQI/AAAAAAAAGc8/8YRm6iyDPO8/s320/l351_40arcsec_residualfit.png

...and so perhaps wer are not. The source mask includes more area and
therefore is more sensitive to extended flux recovery. The slopes are
not consistent with 0 - just look at the data above and below 2 Jy to
see that there is a difference. The multiplicative correction of 1.5 is
decent for a pretty wide range of flux densities, but is inadequate for
the brightest sources. This is somewhat interesting... it implies that
the brightest sources also lie on the highest backgrounds.

.. image:: http://3.bp.blogspot.com/-GQBE_MjAxt8/TlwhPveClUI/AAAAAAAAGdE/lohBYlJuHwM/s320/l351_sourcemask_residualfit.png

You might note that the brightest source has a smaller correction factor
in both apertures. It's not clear why that is the case, but I don't
think it's enough to call it a trend yet - wait for the full 8000-source
comparison first.
Why is there so much scatter? Not entirely clear, but the scatter is
primarily at low S/N.

.. image:: http://3.bp.blogspot.com/-GPKbsfs9Y8k/Tl1OJE43J3I/AAAAAAAAGdM/pVUx9SClgtc/s320/l351_40arcsec_fit_compare_monochrome.png

.. image:: http://3.bp.blogspot.com/-snhh3Bamwc4/Tl1OJXzOYNI/AAAAAAAAGdU/n-rPxs-ZCtI/s320/l351_40arcsec_ratio_compare_monochrome.png

Here are the same for all of the data reduced up to this point:

.. image:: http://2.bp.blogspot.com/-oUewyjZc9wU/Tl1QaGPeURI/AAAAAAAAGds/CHx3BtnT9sA/s320/total_v1v2_sourcemask_fit_compare.png

.. image:: http://1.bp.blogspot.com/-n27ucFd82VI/Tl1Qab1kbUI/AAAAAAAAGd0/kwWAceGqo5c/s320/total_v1v2_sourcemask_ratio_compare.png

.. _|image8|: http://2.bp.blogspot.com/-c3_0Rlbv2qM/Tl1P5FhWC8I/AAAAAAAAGdc/oiFxmO7vrUU/s1600/total_v1v2_40arcsec_ratio_compare.png
.. _|image9|: http://4.bp.blogspot.com/-Gk60vlSPkWk/Tl1P5c4THoI/AAAAAAAAGdk/E7zdIwtyD3w/s1600/total_v1v2_40arcsec_fit_compare.png
.. _this post: http://bolocam.blogspot.com/2011/08/bolocat-v1-v2-comparison.html
.. _|image10|: http://2.bp.blogspot.com/-W08ZvMS3M90/TlwhPW62NQI/AAAAAAAAGc8/8YRm6iyDPO8/s1600/l351_40arcsec_residualfit.png
.. _|image11|: http://3.bp.blogspot.com/-GQBE_MjAxt8/TlwhPveClUI/AAAAAAAAGdE/lohBYlJuHwM/s1600/l351_sourcemask_residualfit.png
.. _|image12|: http://3.bp.blogspot.com/-GPKbsfs9Y8k/Tl1OJE43J3I/AAAAAAAAGdM/pVUx9SClgtc/s1600/l351_40arcsec_fit_compare_monochrome.png
.. _|image13|: http://3.bp.blogspot.com/-snhh3Bamwc4/Tl1OJXzOYNI/AAAAAAAAGdU/n-rPxs-ZCtI/s1600/l351_40arcsec_ratio_compare_monochrome.png
.. _|image14|: http://2.bp.blogspot.com/-oUewyjZc9wU/Tl1QaGPeURI/AAAAAAAAGds/CHx3BtnT9sA/s1600/total_v1v2_sourcemask_fit_compare.png
.. _|image15|: http://1.bp.blogspot.com/-n27ucFd82VI/Tl1Qab1kbUI/AAAAAAAAGd0/kwWAceGqo5c/s1600/total_v1v2_sourcemask_ratio_compare.png

