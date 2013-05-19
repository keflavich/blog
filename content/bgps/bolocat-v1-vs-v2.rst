Bolocat V1 vs V2
################
:date: 2012-05-24 17:59
:author: Adam (noreply@blogger.com)
:tags: googlepost
:slug: bolocat-v1-vs-v2

I've done some very extensive comparison of v1 and v2. The plots below
are included in the current BGPS draft, but I'll go into more excessive
detail here. ALL plots below show Version 1 fluxes versus Version 2
fluxes using Bolocat V1 apertures. This means there are only two
possible effects in play:

#. Different fluxes in the v1 and v2 maps
#. Pointing (spatial) offsets between the v1 and v2 maps
   [see http://bolocam.blogspot.com/2012/05/bgps-v2-pointing.html]

Therefore, the plots below are just different ways of visualizing the
same information. This holds true despite the fact that different
"correction factors" appear in different plots.

.. image:: http://3.bp.blogspot.com/-gGL8rEcNr20/T75tzRC4dJI/AAAAAAAAHHM/A8KeWkBtfmc/s320/total_ratiohistograms.png

Ratios of v2 fluxes to v1 fluxes in the listed apertures. The curves
represent best-fit gaussian distributions to the data after excluding
outliers using a `minimum covariance determinant`_ method

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `|image2|`_                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1 vs v2 with a background subtracted around the source equal to the source area (this was not reported in Bolocat v1, but is a tool Erik implemented so I used it)   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `|image4|`_                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1 vs v2 in 40" apertures, as stated.  There are y=x and y=1.5x lines plotted: these are NOT fits to the data!  The green line is a Total Least Squares linear fit to the data weighted by the measured errors.     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Source Mask "aperture":

.. image:: http://1.bp.blogspot.com/-YS2Jtvz4Yy0/T75pixKkYsI/AAAAAAAAHFs/iEJHrsKsBk0/s320/total_v1v2_sourcemask_bg_fit_compare.png

.. image:: http://1.bp.blogspot.com/-g-ZbEUUWEpY/T75pjj26FeI/AAAAAAAAHGE/rtdSRgoMQpo/s320/total_v1v2_sourcemask_fit_compare.png

Same as above, but the best fit slope is steeper. The best explanation
for the steeper slope (i.e., v2 > 1.5(v1)) is that more extended flux is
recovered in v2 around bright sources, therefore in the larger source
masks, there is greater flux than would be recovered if a simple 1.5x
corrective factor was applied.
80" apertures

.. image:: http://2.bp.blogspot.com/-WKtlvnFbUF4/T75piyh8tVI/AAAAAAAAHF4/FROq508X6pU/s320/total_v1v2_80arcsec_fit_compare.png

.. image:: http://1.bp.blogspot.com/-EHGNHIarslc/T75yqG_AmFI/AAAAAAAAHJg/ToAicG9ynmk/s320/total_v1v2_80_nobgarcsec_fit_compare.png

Same for 120" apertures:

.. image:: http://1.bp.blogspot.com/-ymBFW1Y5OhY/T75piwFYrJI/AAAAAAAAHFw/07ujRFCd_Ts/s320/total_v1v2_120arcsec_fit_compare.png

.. image:: http://3.bp.blogspot.com/-PMkvtoJKNVs/T75yqPe16PI/AAAAAAAAHJk/QF041ok8yQ0/s320/total_v1v2_120_nobgarcsec_fit_compare.png

For all 3 of the 40, 80 and 120" apertures both, the 1.5x correction
factor is nearly perfect (agrees to <5%).  The background subtraction
seems to have different effects depending on aperture size.  I welcome
Erik to comment on this, but I do not think it is particularly
important.
The figures below require some explanation.  NONE of the circular
apertures use background subtraction in this comparison (i.e., compare
to the RIGHT column above).
These figures are histograms of the flux ratio within a given aperture
as a function of flux in the v1 aperture.  From bottom to top, the flux
in the v1 aperture goes from 0.1 to 10 Jy.  The X-axis shows the ratio
of the v2 flux to the v1 flux.  The black dots with error bars represent
the best-fit gaussian distribution to each flux bin.  The colorbar shows
the log of the number of sources; the most in any bin is about
10\ :sup:`2.5` ~ 300.
In short, there is some sign that the ratio of v2/v1 flux varies with v1
flux.  This effect could be seen in the figures above since a linear fit
is imperfect.  The effect is not very strong.  Again, I believe the
explanation here is the changed spatial transfer function in v2.

.. image:: http://3.bp.blogspot.com/-bfrjMd2veR0/T75pzxm5_xI/AAAAAAAAHGs/SQ1LDR8_EoM/s320/ratio_twodhist_40.png

.. image:: http://4.bp.blogspot.com/-unXyfhsIL1g/T75pkN6kWkI/AAAAAAAAHGQ/axiiWsEMO0M/s320/ratio_twodhist_80.png

.. image:: http://2.bp.blogspot.com/-kJEMLqkaQak/T75pkNu78XI/AAAAAAAAHGM/Dh2T4m0cD-8/s320/ratio_twodhist_120.png
.. image:: http://4.bp.blogspot.com/-ExDpIxfHO74/T75pkjjeKAI/AAAAAAAAHGk/pU3mE5uzcgM/s320/ratio_twodhist_sourcemask_nobg.png

.. image:: http://3.bp.blogspot.com/-Pru74WRl-Hg/T75pkOL1YWI/AAAAAAAAHGU/qtrMl-w59SA/s320/ratio_twodhist_sourcemask.png

.. _|image16|: http://3.bp.blogspot.com/-gGL8rEcNr20/T75tzRC4dJI/AAAAAAAAHHM/A8KeWkBtfmc/s1600/total_ratiohistograms.png
.. _minimum covariance determinant: http://scikit-learn.org/dev/modules/generated/sklearn.covariance.MinCovDet.html
.. _|image17|: http://3.bp.blogspot.com/-n_NxdUplC5s/T75t2udmpqI/AAAAAAAAHIQ/yRM1PQjXEV0/s1600/total_v1v2_40arcsec_fit_compare.png
.. _|image18|: http://3.bp.blogspot.com/-EJs6vHAzoM8/T75t2hH3u0I/AAAAAAAAHII/GbdXYj10Z8k/s1600/total_v1v2_40_nobgarcsec_fit_compare.png
.. _|image19|: http://1.bp.blogspot.com/-YS2Jtvz4Yy0/T75pixKkYsI/AAAAAAAAHFs/iEJHrsKsBk0/s1600/total_v1v2_sourcemask_bg_fit_compare.png
.. _|image20|: http://1.bp.blogspot.com/-g-ZbEUUWEpY/T75pjj26FeI/AAAAAAAAHGE/rtdSRgoMQpo/s1600/total_v1v2_sourcemask_fit_compare.png
.. _|image21|: http://2.bp.blogspot.com/-WKtlvnFbUF4/T75piyh8tVI/AAAAAAAAHF4/FROq508X6pU/s1600/total_v1v2_80arcsec_fit_compare.png
.. _|image22|: http://1.bp.blogspot.com/-EHGNHIarslc/T75yqG_AmFI/AAAAAAAAHJg/ToAicG9ynmk/s1600/total_v1v2_80_nobgarcsec_fit_compare.png
.. _|image23|: http://1.bp.blogspot.com/-ymBFW1Y5OhY/T75piwFYrJI/AAAAAAAAHFw/07ujRFCd_Ts/s1600/total_v1v2_120arcsec_fit_compare.png
.. _|image24|: http://3.bp.blogspot.com/-PMkvtoJKNVs/T75yqPe16PI/AAAAAAAAHJk/QF041ok8yQ0/s1600/total_v1v2_120_nobgarcsec_fit_compare.png
.. _|image25|: http://3.bp.blogspot.com/-bfrjMd2veR0/T75pzxm5_xI/AAAAAAAAHGs/SQ1LDR8_EoM/s1600/ratio_twodhist_40.png
.. _|image26|: http://4.bp.blogspot.com/-unXyfhsIL1g/T75pkN6kWkI/AAAAAAAAHGQ/axiiWsEMO0M/s1600/ratio_twodhist_80.png
.. _|image27|: http://2.bp.blogspot.com/-kJEMLqkaQak/T75pkNu78XI/AAAAAAAAHGM/Dh2T4m0cD-8/s1600/ratio_twodhist_120.png
.. _|image28|: http://4.bp.blogspot.com/-ExDpIxfHO74/T75pkjjeKAI/AAAAAAAAHGk/pU3mE5uzcgM/s1600/ratio_twodhist_sourcemask_nobg.png
.. _|image29|: http://3.bp.blogspot.com/-Pru74WRl-Hg/T75pkOL1YWI/AAAAAAAAHGU/qtrMl-w59SA/s1600/ratio_twodhist_sourcemask.png

