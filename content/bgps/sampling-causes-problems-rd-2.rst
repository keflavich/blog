Sampling Causes Problems: Rd 2
##############################
:date: 2011-04-19 17:39
:author: Adam (noreply@blogger.com)
:tags: googlepost, downsampling, simulation, pipeline
:slug: sampling-causes-problems-rd-2

Proof that a well-sampled timestream / gaussian is recovered better than
a poorly sampled one:

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

These aren't really the most convincing, since the flux loss is only
1-8% depending on how you count. The atmosphere-included ones have
larger flux loss, which is important to understand... WHY does the added
noise INCREASE the flux loss?
Ugh, unfortunately, there is a perfect counter-example. The first image
shows a timestream in which the input map is sampled by 7.2" pixels,
which is just shy of nyquist sampling the 1-sigma width of the gaussian
(but is fine for the FWHM of the gaussian). The second shows 3.6"
sampling of the same. No improvement. The third, very surprisingly,
shows significant improvement - but this was an experiment in which the
relative scales were allowed to vary.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image4|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image5|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image6|`_

.. raw:: html

   </div>

The first two each had one high-weight bolometer rejected, the last had
12 high-weight bolos rejected. So that's problably the problem....

.. raw:: html

   </p>

.. _|image7|: http://3.bp.blogspot.com/-PVt1suBQt3s/Ta3EQqypzAI/AAAAAAAAGG4/ap-3_SKjigI/s1600/airy_test_superres_ds1_smallpix_sn100timestream012_plots_16_bolo12.png
.. _|image8|: http://1.bp.blogspot.com/-HMr4DXKBVMY/Ta3GE49GmcI/AAAAAAAAGHA/ULLRUq_IWn8/s1600/airy_test_superres_ds1_sn100timestream012_plots_20_bolo12.png
.. _|image9|: http://3.bp.blogspot.com/-ujL_h0j-Gms/Ta3GWwcEttI/AAAAAAAAGHI/4uVLXXXhtqc/s1600/airy_test_superres_ds1_smallpix_sn100_compare.png
.. _|image10|: http://4.bp.blogspot.com/-r98h73qcMKY/Ta3GXBKAT3I/AAAAAAAAGHQ/k3y8j427TC0/s1600/airy_test_superres_ds1_sn100_compare.png
.. _|image11|: http://4.bp.blogspot.com/-NIwHLJT2SOw/Ta3IAGQA4HI/AAAAAAAAGHY/N3Oju7RHhRE/s1600/airy_test_ds1_reconv_arrang45_atmotest_amp1.0E-01timestream011_plots_20_bolo07.png
.. _|image12|: http://4.bp.blogspot.com/-Qo8-kSCFMCc/Ta3IATO7P1I/AAAAAAAAGHg/Jx9ufNhabiE/s1600/airy_test_ds1_reconv_arrang45_atmotest_smallpix_amp1.0E-01timestream011_plots_20_bolo07.png
.. _|image13|: http://3.bp.blogspot.com/-6PlqmOsDRFY/Ta3IA00cfBI/AAAAAAAAGHo/t5b2jddw5Lw/s1600/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01timestream011_plots_20_bolo07.png

.. |image0| image:: http://3.bp.blogspot.com/-PVt1suBQt3s/Ta3EQqypzAI/AAAAAAAAGG4/ap-3_SKjigI/s320/airy_test_superres_ds1_smallpix_sn100timestream012_plots_16_bolo12.png
.. |image1| image:: http://1.bp.blogspot.com/-HMr4DXKBVMY/Ta3GE49GmcI/AAAAAAAAGHA/ULLRUq_IWn8/s320/airy_test_superres_ds1_sn100timestream012_plots_20_bolo12.png
.. |image2| image:: http://3.bp.blogspot.com/-ujL_h0j-Gms/Ta3GWwcEttI/AAAAAAAAGHI/4uVLXXXhtqc/s320/airy_test_superres_ds1_smallpix_sn100_compare.png
.. |image3| image:: http://4.bp.blogspot.com/-r98h73qcMKY/Ta3GXBKAT3I/AAAAAAAAGHQ/k3y8j427TC0/s320/airy_test_superres_ds1_sn100_compare.png
.. |image4| image:: http://4.bp.blogspot.com/-NIwHLJT2SOw/Ta3IAGQA4HI/AAAAAAAAGHY/N3Oju7RHhRE/s320/airy_test_ds1_reconv_arrang45_atmotest_amp1.0E-01timestream011_plots_20_bolo07.png
.. |image5| image:: http://4.bp.blogspot.com/-Qo8-kSCFMCc/Ta3IATO7P1I/AAAAAAAAGHg/Jx9ufNhabiE/s320/airy_test_ds1_reconv_arrang45_atmotest_smallpix_amp1.0E-01timestream011_plots_20_bolo07.png
.. |image6| image:: http://3.bp.blogspot.com/-6PlqmOsDRFY/Ta3IA00cfBI/AAAAAAAAGHo/t5b2jddw5Lw/s320/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01timestream011_plots_20_bolo07.png
.. |image7| image:: http://3.bp.blogspot.com/-PVt1suBQt3s/Ta3EQqypzAI/AAAAAAAAGG4/ap-3_SKjigI/s320/airy_test_superres_ds1_smallpix_sn100timestream012_plots_16_bolo12.png
.. |image8| image:: http://1.bp.blogspot.com/-HMr4DXKBVMY/Ta3GE49GmcI/AAAAAAAAGHA/ULLRUq_IWn8/s320/airy_test_superres_ds1_sn100timestream012_plots_20_bolo12.png
.. |image9| image:: http://3.bp.blogspot.com/-ujL_h0j-Gms/Ta3GWwcEttI/AAAAAAAAGHI/4uVLXXXhtqc/s320/airy_test_superres_ds1_smallpix_sn100_compare.png
.. |image10| image:: http://4.bp.blogspot.com/-r98h73qcMKY/Ta3GXBKAT3I/AAAAAAAAGHQ/k3y8j427TC0/s320/airy_test_superres_ds1_sn100_compare.png
.. |image11| image:: http://4.bp.blogspot.com/-NIwHLJT2SOw/Ta3IAGQA4HI/AAAAAAAAGHY/N3Oju7RHhRE/s320/airy_test_ds1_reconv_arrang45_atmotest_amp1.0E-01timestream011_plots_20_bolo07.png
.. |image12| image:: http://4.bp.blogspot.com/-Qo8-kSCFMCc/Ta3IATO7P1I/AAAAAAAAGHg/Jx9ufNhabiE/s320/airy_test_ds1_reconv_arrang45_atmotest_smallpix_amp1.0E-01timestream011_plots_20_bolo07.png
.. |image13| image:: http://3.bp.blogspot.com/-6PlqmOsDRFY/Ta3IA00cfBI/AAAAAAAAGHo/t5b2jddw5Lw/s320/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01timestream011_plots_20_bolo07.png
