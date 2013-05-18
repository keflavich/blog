Spatial Transfer Function vs. nPCA
##################################
:date: 2011-08-10 16:29
:author: Adam (noreply@blogger.com)
:tags: googlepost, simulation
:slug: spatial-transfer-function-vs-npca

A demonstration that the spatial transfer function can be improved to
~80% at ~300 arcseconds by reducing the number of PCA components
subtracted. However, image fidelity and noise backgrounds suffer, so
these sorts of maps are probably less ideal for point source extraction.
Below:
 0 PCA
 3 PCA
 10 PCA
 15 PCA

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

.. raw:: html

   </p>

.. _|image4|: http://1.bp.blogspot.com/-CPZck7lZils/TkKxcMIgsoI/AAAAAAAAGZg/HeZJfzaSewk/s1600/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_00pca_median_psds.png
.. _|image5|: http://1.bp.blogspot.com/-ew7CSdNfc3M/TkKxcZb3qDI/AAAAAAAAGZo/_mSPtt6TgG4/s1600/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_03pca_psds.png
.. _|image6|: http://4.bp.blogspot.com/-NG2yqqzPucM/TkKxcxoM6pI/AAAAAAAAGZw/zocHKlKAO3Q/s1600/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_10pca_psds.png
.. _|image7|: http://1.bp.blogspot.com/-Y_rIZ33S8QE/TkKxdOlcTAI/AAAAAAAAGZ4/J6kkz5PDasA/s1600/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_15pca_psds.png

.. |image0| image:: http://1.bp.blogspot.com/-CPZck7lZils/TkKxcMIgsoI/AAAAAAAAGZg/HeZJfzaSewk/s320/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_00pca_median_psds.png
.. |image1| image:: http://1.bp.blogspot.com/-ew7CSdNfc3M/TkKxcZb3qDI/AAAAAAAAGZo/_mSPtt6TgG4/s320/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_03pca_psds.png
.. |image2| image:: http://4.bp.blogspot.com/-NG2yqqzPucM/TkKxcxoM6pI/AAAAAAAAGZw/zocHKlKAO3Q/s320/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_10pca_psds.png
.. |image3| image:: http://1.bp.blogspot.com/-Y_rIZ33S8QE/TkKxdOlcTAI/AAAAAAAAGZ4/J6kkz5PDasA/s320/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_15pca_psds.png
.. |image4| image:: http://1.bp.blogspot.com/-CPZck7lZils/TkKxcMIgsoI/AAAAAAAAGZg/HeZJfzaSewk/s320/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_00pca_median_psds.png
.. |image5| image:: http://1.bp.blogspot.com/-ew7CSdNfc3M/TkKxcZb3qDI/AAAAAAAAGZo/_mSPtt6TgG4/s320/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_03pca_psds.png
.. |image6| image:: http://4.bp.blogspot.com/-NG2yqqzPucM/TkKxcxoM6pI/AAAAAAAAGZw/zocHKlKAO3Q/s320/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_10pca_psds.png
.. |image7| image:: http://1.bp.blogspot.com/-Y_rIZ33S8QE/TkKxdOlcTAI/AAAAAAAAGZ4/J6kkz5PDasA/s320/exp15_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_smooth_15pca_psds.png
