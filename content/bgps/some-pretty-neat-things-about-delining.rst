Some pretty neat things about delining....
##########################################
:date: 2011-02-03 04:50
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, pipeline, deline
:slug: some-pretty-neat-things-about-delining

Well, I did the work, so might as well come up with some plots...
I created a gaussian-fitting based delining code that saves all of the
fits in a text file! That's a lot of data to play with, and allows me to
draw some conclusions:

#. For the narrow lines, the linewidth (gaussian sigma) is 0.03 Hz. For
   the wide lines, it is 0.05.

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

#. The amplitudes from December 2010 are ENORMOUS compared to others!

   .. raw:: html

      <div class="separator" style="clear: both; text-align: center;">

   `|image2|`_

   .. raw:: html

      </div>

#. The width distributions of the two are similar, though the lines
   appear to be significantly wider in July 2009

   .. raw:: html

      <div class="separator" style="clear: both; text-align: center;">

   `|image3|`_

   .. raw:: html

      </div>

I've also gotten to the point that I'm satisfied with how delining with
wing suppression works. Wing suppression is 0.4-2x quicker than fitting
directly, depending on... not clear what exactly; it depends on epoch,
but that could either be because there are more lines found or because
of relative data size. Does delining have to be done on whole
timestreams, or can it be done on a scan-by-scan basis? This is not
entirely clear... the peaks are less suppressed when done on a
scan-by-scan basis (presumably because the S/N is low and peaks are
therefore not detected), but incorrect suppression (removing a line
that's not there) is reduced. For short scans, the scan-by-scan approach
is 10x faster; for longer scans it's ~20% faster. I think the
scan-by-scan approach is going to be ideal.

--------------

Examples from l089 (0709):
Top row: non-fitted line suppression

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image4|`_\ `|image5|`_

.. raw:: html

   </div>

Bottom row: fitted line suppression

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image6|`_\ `|image7|`_

.. raw:: html

   </div>

--------------

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

Examples from Uranus (1012, really really liney):

.. raw:: html

   </div>

Top row: non-fitted line suppression

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image8|`_\ `|image9|`_

.. raw:: html

   </div>

Bottom row: fitted line suppression

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image10|`_\ `|image11|`_

.. raw:: html

   </div>

.. raw:: html

   </p>

.. _|image12|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUorHEcJO0I/AAAAAAAAF7k/TaWEWrbczZ0/s1600/histogram_fit_deline_linewidths.png
.. _|image13|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUorHusiIdI/AAAAAAAAF7s/NX67lE3OgaQ/s1600/histogram_fit_deline_linewidths_wide.png
.. _|image14|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUosLpxdcdI/AAAAAAAAF70/QTgqsu4uQrg/s1600/histogram_fit_deline_amplitudes_epochcompare.png
.. _|image15|: http://3.bp.blogspot.com/_lsgW26mWZnU/TUotc81_ztI/AAAAAAAAF78/8nxzuv8Apc8/s1600/histogram_fit_deline_width_epochcompare.png
.. _|image16|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUowz4zgpsI/AAAAAAAAF8E/iJd0tAbVj0U/s1600/deline_10hz_wingsuppress_psds_003.png
.. _|image17|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUow1IQ_Y9I/AAAAAAAAF8c/1OkISODwwPM/s1600/deline_fitline_10hz_noscan_nsig0_preservephase_timestreams_003.png
.. _|image18|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUow0sTBKsI/AAAAAAAAF8U/GtL0nyvlNBw/s1600/deline_fitline_10hz_noscan_nsig0_preservephase_psds_003.png
.. _|image19|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUow0d-vEcI/AAAAAAAAF8M/or2gkvGxW4o/s1600/deline_10hz_wingsuppress_timestreams_003.png
.. _|image20|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUoxEvWqRwI/AAAAAAAAF8k/J6ImhPN9ZS0/s1600/deline_10hz_wingsuppress_psds_003.png
.. _|image21|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUoxFMLdujI/AAAAAAAAF8s/DrzWxFCdBu0/s1600/deline_10hz_wingsuppress_timestreams_003.png
.. _|image22|: http://3.bp.blogspot.com/_lsgW26mWZnU/TUoxFXYN_tI/AAAAAAAAF80/BQwv6ROSOJ4/s1600/deline_fitline_10hz_noscan_nsig0_preservephase_psds_003.png
.. _|image23|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUoxF_c0URI/AAAAAAAAF88/JU9_F-8HC2k/s1600/deline_fitline_10hz_noscan_nsig0_preservephase_timestreams_003.png

.. |image0| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUorHEcJO0I/AAAAAAAAF7k/TaWEWrbczZ0/s320/histogram_fit_deline_linewidths.png
.. |image1| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUorHusiIdI/AAAAAAAAF7s/NX67lE3OgaQ/s320/histogram_fit_deline_linewidths_wide.png
.. |image2| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUosLpxdcdI/AAAAAAAAF70/QTgqsu4uQrg/s320/histogram_fit_deline_amplitudes_epochcompare.png
.. |image3| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUotc81_ztI/AAAAAAAAF78/8nxzuv8Apc8/s320/histogram_fit_deline_width_epochcompare.png
.. |image4| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUowz4zgpsI/AAAAAAAAF8E/iJd0tAbVj0U/s320/deline_10hz_wingsuppress_psds_003.png
.. |image5| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUow1IQ_Y9I/AAAAAAAAF8c/1OkISODwwPM/s320/deline_fitline_10hz_noscan_nsig0_preservephase_timestreams_003.png
.. |image6| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUow0sTBKsI/AAAAAAAAF8U/GtL0nyvlNBw/s320/deline_fitline_10hz_noscan_nsig0_preservephase_psds_003.png
.. |image7| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUow0d-vEcI/AAAAAAAAF8M/or2gkvGxW4o/s320/deline_10hz_wingsuppress_timestreams_003.png
.. |image8| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUoxEvWqRwI/AAAAAAAAF8k/J6ImhPN9ZS0/s320/deline_10hz_wingsuppress_psds_003.png
.. |image9| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUoxFMLdujI/AAAAAAAAF8s/DrzWxFCdBu0/s320/deline_10hz_wingsuppress_timestreams_003.png
.. |image10| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUoxFXYN_tI/AAAAAAAAF80/BQwv6ROSOJ4/s320/deline_fitline_10hz_noscan_nsig0_preservephase_psds_003.png
.. |image11| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUoxF_c0URI/AAAAAAAAF88/JU9_F-8HC2k/s320/deline_fitline_10hz_noscan_nsig0_preservephase_timestreams_003.png
.. |image12| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUorHEcJO0I/AAAAAAAAF7k/TaWEWrbczZ0/s320/histogram_fit_deline_linewidths.png
.. |image13| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUorHusiIdI/AAAAAAAAF7s/NX67lE3OgaQ/s320/histogram_fit_deline_linewidths_wide.png
.. |image14| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUosLpxdcdI/AAAAAAAAF70/QTgqsu4uQrg/s320/histogram_fit_deline_amplitudes_epochcompare.png
.. |image15| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUotc81_ztI/AAAAAAAAF78/8nxzuv8Apc8/s320/histogram_fit_deline_width_epochcompare.png
.. |image16| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUowz4zgpsI/AAAAAAAAF8E/iJd0tAbVj0U/s320/deline_10hz_wingsuppress_psds_003.png
.. |image17| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUow1IQ_Y9I/AAAAAAAAF8c/1OkISODwwPM/s320/deline_fitline_10hz_noscan_nsig0_preservephase_timestreams_003.png
.. |image18| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUow0sTBKsI/AAAAAAAAF8U/GtL0nyvlNBw/s320/deline_fitline_10hz_noscan_nsig0_preservephase_psds_003.png
.. |image19| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUow0d-vEcI/AAAAAAAAF8M/or2gkvGxW4o/s320/deline_10hz_wingsuppress_timestreams_003.png
.. |image20| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUoxEvWqRwI/AAAAAAAAF8k/J6ImhPN9ZS0/s320/deline_10hz_wingsuppress_psds_003.png
.. |image21| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUoxFMLdujI/AAAAAAAAF8s/DrzWxFCdBu0/s320/deline_10hz_wingsuppress_timestreams_003.png
.. |image22| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUoxFXYN_tI/AAAAAAAAF80/BQwv6ROSOJ4/s320/deline_fitline_10hz_noscan_nsig0_preservephase_psds_003.png
.. |image23| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUoxF_c0URI/AAAAAAAAF88/JU9_F-8HC2k/s320/deline_fitline_10hz_noscan_nsig0_preservephase_timestreams_003.png
