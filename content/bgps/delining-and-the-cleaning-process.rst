Delining and the Cleaning process
#################################
:date: 2011-02-03 19:49
:author: Adam (noreply@blogger.com)
:tags: googlepost, cleaning, pipeline, deline
:slug: delining-and-the-cleaning-process

One item I forgot to mention last night was the effects of
lines/delining on
PCA subtraction. These should be the primary effects on the final map
for all
epochs except 2010, in which case the primary effect SHOULD be to reduce
substantial noise.
In the examples below, there are PSDs of whole timestreams (left) and
example timestreams from single scans (right). The first thing to note
is that
the delined timestreams still have correlated components in the line
region,
but they are suppressed - their amplitudes, and therefore their sort
order in
the PCA removal scheme, are changed. Since PCA cleaning is by its nature
adaptive
(the number of components remains fixed, but the order changes), these
effects
can be significant and dangerous. If the line noise is more correlated,
a PCA
component will be dedicated to removing it instead of atmospheric
signal.
Below are examples from l089 (epoch 0709) first. These have less
correlated
line noise and are more typical of BGPS observations. The first PCA
component,
the average, does not change much with PCA cleaning. However it is clear
that
the second component changes substantially, from large-amplitude
high-frequency
noise to small-amplitude variations that are very likely to describe
atmosphere.

--------------

.. raw:: html

   <table>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Example 1 - Zeroing out the lines:

.. raw:: html

   </tr>

.. raw:: html

   </td>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_

.. raw:: html

   </td>

.. raw:: html

   <td>

`|image1|`_

.. raw:: html

   </div>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td colspan="2">

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Example 2 - Fitting and removing the lines:

.. raw:: html

   </tr>

.. raw:: html

   </td>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image2|`_

.. raw:: html

   </td>

.. raw:: html

   <td>

`|image3|`_

.. raw:: html

   </div>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td colspan="2">

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Example 3 - Suppressing the lines with a non-fitted Gaussian:

.. raw:: html

   </tr>

.. raw:: html

   </td>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image4|`_

.. raw:: html

   </td>

.. raw:: html

   <td>

`|image5|`_

.. raw:: html

   </div>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td colspan="2">

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td colspan="2">

--------------

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td colspan="2">

The next examples are from December 2010 observations of Uranus. In this
case, the correlated noise component is clearly dominant.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td colspan="2">

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Zeroing lines:

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image6|`_

.. raw:: html

   </td>

.. raw:: html

   <td>

`|image7|`_

.. raw:: html

   </div>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Fitted lines:

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image8|`_

.. raw:: html

   </td>

.. raw:: html

   <td>

`|image9|`_

.. raw:: html

   </div>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Non-fitted gaussian suppression:

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image10|`_

.. raw:: html

   </td>

.. raw:: html

   <td>

`|image11|`_

.. raw:: html

   </div>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td colspan="2">

--------------

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

 Finally, these two are demonstrations of what you might expect to see
for a purely noiseless images of a planet (it was constructed from a
PSF). PCA is first:

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image12|`_

.. raw:: html

   </td>

.. raw:: html

   <td>

`|image13|`_

.. raw:: html

   </div>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

 A single bolometer's timestream and PSD:

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image14|`_

.. raw:: html

   </td>

.. raw:: html

   <td>

`|image15|`_

.. raw:: html

   </div>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

.. raw:: html

   </p>

.. _|image16|: http://3.bp.blogspot.com/_lsgW26mWZnU/TUrs_QRBBHI/AAAAAAAAF9Y/BH4XEdrFdt0/s1600/zero_pca_psds.png
.. _|image17|: http://3.bp.blogspot.com/_lsgW26mWZnU/TUrs_nWI6YI/AAAAAAAAF9g/1Dcr0zyMBvM/s1600/zero_pca_timestreams.png
.. _|image18|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUrs-f7qfqI/AAAAAAAAF9I/Dt3Kk9roeW8/s1600/fitline_pca_psds.png
.. _|image19|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUrs-_it9CI/AAAAAAAAF9Q/06KgQOS2vNA/s1600/fitline_pca_timestreams.png
.. _|image20|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUr_QHkPADI/AAAAAAAAF9o/n5ylgDCLKPw/s1600/wingsupp_pca_psds.png
.. _|image21|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUr_QnuPZfI/AAAAAAAAF9w/lt4rEB1Qlq0/s1600/wingsupp_pca_timestreams.png
.. _|image22|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCBUeD67I/AAAAAAAAF94/CCj9gbJOgk8/s1600/zero_pca_psds.png
.. _|image23|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCB4wFnSI/AAAAAAAAF-A/YgbjYlybcOc/s1600/zero_pca_timestreams.png
.. _|image24|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCCQNHurI/AAAAAAAAF-I/a5_FQ7bqUjI/s1600/fitline_pca_psds.png
.. _|image25|: http://3.bp.blogspot.com/_lsgW26mWZnU/TUsCCtO7DTI/AAAAAAAAF-Q/wKBz0UhDruE/s1600/fitline_pca_timestreams.png
.. _|image26|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUsCLgCRbmI/AAAAAAAAF-Y/WzHcr1E5q4s/s1600/wingsupp_pca_psds.png
.. _|image27|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCL5e9eGI/AAAAAAAAF-g/TgmNWbiJzbs/s1600/wingsupp_pca_timestreams.png
.. _|image28|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCyELAZ1I/AAAAAAAAF-o/65L-rwGFscM/s1600/noiselesssim_pca_psds.png
.. _|image29|: http://3.bp.blogspot.com/_lsgW26mWZnU/TUsCyRaYY7I/AAAAAAAAF-w/ZaRL4CPWw2E/s1600/noiselesssim_pca_timestreams.png
.. _|image30|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUsDgR4xcEI/AAAAAAAAF-4/udxMkuH6kio/s1600/noiselesssim_deline_wingsupp_10hz_noscan_nsig0_psds_000.png
.. _|image31|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUsDgtnBPNI/AAAAAAAAF_A/weQNMCgtrtc/s1600/noiselesssim_deline_wingsupp_10hz_noscan_nsig0_timestreams_000.png

.. |image0| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUrs_QRBBHI/AAAAAAAAF9Y/BH4XEdrFdt0/s320/zero_pca_psds.png
.. |image1| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUrs_nWI6YI/AAAAAAAAF9g/1Dcr0zyMBvM/s320/zero_pca_timestreams.png
.. |image2| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUrs-f7qfqI/AAAAAAAAF9I/Dt3Kk9roeW8/s320/fitline_pca_psds.png
.. |image3| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUrs-_it9CI/AAAAAAAAF9Q/06KgQOS2vNA/s320/fitline_pca_timestreams.png
.. |image4| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUr_QHkPADI/AAAAAAAAF9o/n5ylgDCLKPw/s320/wingsupp_pca_psds.png
.. |image5| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUr_QnuPZfI/AAAAAAAAF9w/lt4rEB1Qlq0/s320/wingsupp_pca_timestreams.png
.. |image6| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCBUeD67I/AAAAAAAAF94/CCj9gbJOgk8/s320/zero_pca_psds.png
.. |image7| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCB4wFnSI/AAAAAAAAF-A/YgbjYlybcOc/s320/zero_pca_timestreams.png
.. |image8| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCCQNHurI/AAAAAAAAF-I/a5_FQ7bqUjI/s320/fitline_pca_psds.png
.. |image9| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUsCCtO7DTI/AAAAAAAAF-Q/wKBz0UhDruE/s320/fitline_pca_timestreams.png
.. |image10| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUsCLgCRbmI/AAAAAAAAF-Y/WzHcr1E5q4s/s320/wingsupp_pca_psds.png
.. |image11| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCL5e9eGI/AAAAAAAAF-g/TgmNWbiJzbs/s320/wingsupp_pca_timestreams.png
.. |image12| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCyELAZ1I/AAAAAAAAF-o/65L-rwGFscM/s320/noiselesssim_pca_psds.png
.. |image13| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUsCyRaYY7I/AAAAAAAAF-w/ZaRL4CPWw2E/s320/noiselesssim_pca_timestreams.png
.. |image14| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUsDgR4xcEI/AAAAAAAAF-4/udxMkuH6kio/s320/noiselesssim_deline_wingsupp_10hz_noscan_nsig0_psds_000.png
.. |image15| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUsDgtnBPNI/AAAAAAAAF_A/weQNMCgtrtc/s320/noiselesssim_deline_wingsupp_10hz_noscan_nsig0_timestreams_000.png
.. |image16| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUrs_QRBBHI/AAAAAAAAF9Y/BH4XEdrFdt0/s320/zero_pca_psds.png
.. |image17| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUrs_nWI6YI/AAAAAAAAF9g/1Dcr0zyMBvM/s320/zero_pca_timestreams.png
.. |image18| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUrs-f7qfqI/AAAAAAAAF9I/Dt3Kk9roeW8/s320/fitline_pca_psds.png
.. |image19| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUrs-_it9CI/AAAAAAAAF9Q/06KgQOS2vNA/s320/fitline_pca_timestreams.png
.. |image20| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUr_QHkPADI/AAAAAAAAF9o/n5ylgDCLKPw/s320/wingsupp_pca_psds.png
.. |image21| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUr_QnuPZfI/AAAAAAAAF9w/lt4rEB1Qlq0/s320/wingsupp_pca_timestreams.png
.. |image22| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCBUeD67I/AAAAAAAAF94/CCj9gbJOgk8/s320/zero_pca_psds.png
.. |image23| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCB4wFnSI/AAAAAAAAF-A/YgbjYlybcOc/s320/zero_pca_timestreams.png
.. |image24| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCCQNHurI/AAAAAAAAF-I/a5_FQ7bqUjI/s320/fitline_pca_psds.png
.. |image25| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUsCCtO7DTI/AAAAAAAAF-Q/wKBz0UhDruE/s320/fitline_pca_timestreams.png
.. |image26| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUsCLgCRbmI/AAAAAAAAF-Y/WzHcr1E5q4s/s320/wingsupp_pca_psds.png
.. |image27| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCL5e9eGI/AAAAAAAAF-g/TgmNWbiJzbs/s320/wingsupp_pca_timestreams.png
.. |image28| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUsCyELAZ1I/AAAAAAAAF-o/65L-rwGFscM/s320/noiselesssim_pca_psds.png
.. |image29| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUsCyRaYY7I/AAAAAAAAF-w/ZaRL4CPWw2E/s320/noiselesssim_pca_timestreams.png
.. |image30| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUsDgR4xcEI/AAAAAAAAF-4/udxMkuH6kio/s320/noiselesssim_deline_wingsupp_10hz_noscan_nsig0_psds_000.png
.. |image31| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUsDgtnBPNI/AAAAAAAAF_A/weQNMCgtrtc/s320/noiselesssim_deline_wingsupp_10hz_noscan_nsig0_timestreams_000.png
