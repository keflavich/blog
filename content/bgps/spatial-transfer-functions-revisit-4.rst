Spatial Transfer Functions, revisit 4
#####################################
:date: 2011-08-05 18:56
:author: Adam (noreply@blogger.com)
:tags: googlepost, analysis, testing, simulation, pipeline
:slug: spatial-transfer-functions-revisit-4

Last report was a bit of a fiasco. There were problems all over the
place I didn't understand. I still don't but I've fixed them. My best
guess at this point is that a pass-by-reference led to an unacceptable
modification of an image. That doesn't even make sense - there was no
place it could have happened - but, there you have it.
So, going through the process step by step.
This is the effect of smoothing an image:


.. image:: http://1.bp.blogspot.com/-3TabjiWVKm4/Tjs03gqxkxI/AAAAAAAAGXk/BQOH5FvG3CM/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky02_seed00_peak010.00_SMvsNOSM_input_psds.png



.. image:: http://1.bp.blogspot.com/-AWglr2CHB-0/Tjs04fniKDI/AAAAAAAAGXs/MM3RCNu6x10/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky02_seed00_peak010.00_SMvsNOSM_input_compare.png



.. image:: http://2.bp.blogspot.com/-5yFhvF1iOeY/Tjs1ES7HeuI/AAAAAAAAGX0/T44kJArWn2o/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky02_seed00_peak010.00_SMvsNOSM_input_stf.png


Note from the 3rd figure that 100% recovery isn't reached until ~700
arcseconds.
Next question: What is happening at large spatial scales in the
flat-spectrum simulations?


.. image:: http://1.bp.blogspot.com/-Fi2EBFsPFK4/TjtLzkxRxRI/AAAAAAAAGX8/4GoYEwSaaKc/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky07_seed00_peak100.00_smooth_compare.png



.. image:: http://2.bp.blogspot.com/-P3TEAHevkEY/TjtL0BG8BbI/AAAAAAAAGYE/oC71ZTFTz3k/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky06_seed00_peak100.00_smooth_compare.png



.. image:: http://4.bp.blogspot.com/-g0m5hEHx8QY/TjtL00D3USI/AAAAAAAAGYM/687cgIORovk/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky05_seed00_peak100.00_smooth_compare.png


No obvious problems there.


.. image:: http://3.bp.blogspot.com/-DwXSkiyw2kE/TjtNt7XadiI/AAAAAAAAGYU/trzLma37DgM/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky05_seed00_peak100.00_smooth_psds.png



.. image:: http://1.bp.blogspot.com/-Q9ItTP7uQDs/TjtNuILPfLI/AAAAAAAAGYc/w67japCoUpo/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky06_seed00_peak100.00_smooth_psds.png



.. image:: http://3.bp.blogspot.com/-mgWHY8CT3tQ/TjtNuv1jZ-I/AAAAAAAAGYk/Iddg_I2UKjo/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky07_seed00_peak100.00_smooth_psds.png


Hmm, no apparent problem here either, though one might ask why the two
curves approach each other in sky05 (alpha=-0.5).
So it appears that the reason for the bump up at low frequencies (long
wavelengths) must be because of edge effects. After much hassle, I've
addressed that by cropping images.
Finally, the averaged results:


.. image:: http://3.bp.blogspot.com/-26KmVHKU_QY/Tjw8VVYnkkI/AAAAAAAAGY4/-R-e3mwVwZc/s320/stfs_bestmodel_fits.png



.. image:: http://2.bp.blogspot.com/-lPtvV465aLg/Tjw8VhQZXXI/AAAAAAAAGZA/Rib4AX6z75E/s320/stfs_bestmodels.png


So we've got an Official Spatial Transfer Function.
However, of course, we must note that there is a dependence on the
atmosphere amplitude to source amplitude ratio: it appears that
large-scale structure is \*easier\* to recover when the atmosphere is at
higher amplitude. This makes sense: it is easier to distinguish faint
astrophysical signal from bright atmosphere in this case. The reason I
didn't run simulations to test this more is that the S/N ratio on small
scales becomes poor for the low astrophysical amplitudes.


.. _|image11|: http://1.bp.blogspot.com/-3TabjiWVKm4/Tjs03gqxkxI/AAAAAAAAGXk/BQOH5FvG3CM/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky02_seed00_peak010.00_SMvsNOSM_input_psds.png
.. _|image12|: http://1.bp.blogspot.com/-AWglr2CHB-0/Tjs04fniKDI/AAAAAAAAGXs/MM3RCNu6x10/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky02_seed00_peak010.00_SMvsNOSM_input_compare.png
.. _|image13|: http://2.bp.blogspot.com/-5yFhvF1iOeY/Tjs1ES7HeuI/AAAAAAAAGX0/T44kJArWn2o/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky02_seed00_peak010.00_SMvsNOSM_input_stf.png
.. _|image14|: http://1.bp.blogspot.com/-Fi2EBFsPFK4/TjtLzkxRxRI/AAAAAAAAGX8/4GoYEwSaaKc/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky07_seed00_peak100.00_smooth_compare.png
.. _|image15|: http://2.bp.blogspot.com/-P3TEAHevkEY/TjtL0BG8BbI/AAAAAAAAGYE/oC71ZTFTz3k/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky06_seed00_peak100.00_smooth_compare.png
.. _|image16|: http://4.bp.blogspot.com/-g0m5hEHx8QY/TjtL00D3USI/AAAAAAAAGYM/687cgIORovk/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky05_seed00_peak100.00_smooth_compare.png
.. _|image17|: http://3.bp.blogspot.com/-DwXSkiyw2kE/TjtNt7XadiI/AAAAAAAAGYU/trzLma37DgM/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky05_seed00_peak100.00_smooth_psds.png
.. _|image18|: http://1.bp.blogspot.com/-Q9ItTP7uQDs/TjtNuILPfLI/AAAAAAAAGYc/w67japCoUpo/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky06_seed00_peak100.00_smooth_psds.png
.. _|image19|: http://3.bp.blogspot.com/-mgWHY8CT3tQ/TjtNuv1jZ-I/AAAAAAAAGYk/Iddg_I2UKjo/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky07_seed00_peak100.00_smooth_psds.png
.. _|image20|: http://3.bp.blogspot.com/-26KmVHKU_QY/Tjw8VVYnkkI/AAAAAAAAGY4/-R-e3mwVwZc/s1600/stfs_bestmodel_fits.png
.. _|image21|: http://2.bp.blogspot.com/-lPtvV465aLg/Tjw8VhQZXXI/AAAAAAAAGZA/Rib4AX6z75E/s1600/stfs_bestmodels.png

.. |image11| image:: http://1.bp.blogspot.com/-3TabjiWVKm4/Tjs03gqxkxI/AAAAAAAAGXk/BQOH5FvG3CM/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky02_seed00_peak010.00_SMvsNOSM_input_psds.png
.. |image12| image:: http://1.bp.blogspot.com/-AWglr2CHB-0/Tjs04fniKDI/AAAAAAAAGXs/MM3RCNu6x10/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky02_seed00_peak010.00_SMvsNOSM_input_compare.png
.. |image13| image:: http://2.bp.blogspot.com/-5yFhvF1iOeY/Tjs1ES7HeuI/AAAAAAAAGX0/T44kJArWn2o/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky02_seed00_peak010.00_SMvsNOSM_input_stf.png
.. |image14| image:: http://1.bp.blogspot.com/-Fi2EBFsPFK4/TjtLzkxRxRI/AAAAAAAAGX8/4GoYEwSaaKc/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky07_seed00_peak100.00_smooth_compare.png
.. |image15| image:: http://2.bp.blogspot.com/-P3TEAHevkEY/TjtL0BG8BbI/AAAAAAAAGYE/oC71ZTFTz3k/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky06_seed00_peak100.00_smooth_compare.png
.. |image16| image:: http://4.bp.blogspot.com/-g0m5hEHx8QY/TjtL00D3USI/AAAAAAAAGYM/687cgIORovk/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky05_seed00_peak100.00_smooth_compare.png
.. |image17| image:: http://3.bp.blogspot.com/-DwXSkiyw2kE/TjtNt7XadiI/AAAAAAAAGYU/trzLma37DgM/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky05_seed00_peak100.00_smooth_psds.png
.. |image18| image:: http://1.bp.blogspot.com/-Q9ItTP7uQDs/TjtNuILPfLI/AAAAAAAAGYc/w67japCoUpo/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky06_seed00_peak100.00_smooth_psds.png
.. |image19| image:: http://3.bp.blogspot.com/-mgWHY8CT3tQ/TjtNuv1jZ-I/AAAAAAAAGYk/Iddg_I2UKjo/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky07_seed00_peak100.00_smooth_psds.png
.. |image20| image:: http://3.bp.blogspot.com/-26KmVHKU_QY/Tjw8VVYnkkI/AAAAAAAAGY4/-R-e3mwVwZc/s320/stfs_bestmodel_fits.png
.. |image21| image:: http://2.bp.blogspot.com/-lPtvV465aLg/Tjw8VhQZXXI/AAAAAAAAGZA/Rib4AX6z75E/s320/stfs_bestmodels.png
