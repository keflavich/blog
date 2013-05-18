ds1-ds5 comparisons
###################
:date: 2011-04-26 21:54
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, downsampling, pipeline
:slug: ds1-ds5-comparisons

I'm comparing simulated ds1-ds5 to real ds1-ds5 comparison tests.
In the simulated tests, I compare the recovered map after 20 iterations
with 13 pca components subtracted to the input map. There are figures
showing this comparison for ds1 and ds5 images in addition to one
showing the comparison between ds1 and ds5. The agreement is pretty much
as good as you could ask for.
These simulations are the most realistic run yet. They include a
simulated atmosphere that is perfectly correlated between all bolometers
excepting gaussian noise, but the relative sensitivity of the bolometers
is varied.

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

This is what a 'real' ds1-ds5 comparison looks like. The image shown is
a "cross-linked" observation of Uranus with downsampling off and on.
Note that downsampling clearly and blatantly smears the source flux.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image3|`_

.. raw:: html

   </div>

The same image with "beam location correction" looks no better.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image4|`_

.. raw:: html

   </div>

The problem is essentially the same with the individual scan directions:

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

What is causing this difference?

-  higher-order corrections to the atmosphere calculation?
-  inadequate sampling of the model?
-  "pointing" offsets between the model and the data (note that these
   are NOT pointing offsets, but they may be "distortion map" offsets)?
-  Other?

Examining the weights and scales for two individual (real) observations,
ds1 followed by ds5, is not particularly telling; there is one
additional outlier bolometer flagged out in the ds1 observation, but
there is nothing obviously wrong with that bolometer (it may have much
lower high-frequency noise than others).

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image7|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image8|`_

.. raw:: html

   </div>

The simulations actually have more discrepant weights, but that doesn't
seem to cause any problems:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image9|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image10|`_

.. raw:: html

   </div>

The timestreams both have similar artifacts:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image11|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image12|`_

.. raw:: html

   </div>

while the simulated versions really don't:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image13|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image14|`_

.. raw:: html

   </div>

This is true even when the relative strength of the atmosphere is
higher:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image15|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image16|`_

.. raw:: html

   </div>

I think the most viable candidate is the 'pointing offset' idea, which
will take a little work to simulate properly...

.. raw:: html

   </p>

.. _|image17|: http://4.bp.blogspot.com/-xZqAo2n84iE/TbcsrsLkkaI/AAAAAAAAGIM/J_4xWIOGoCQ/s1600/exp2_varyrelscale_amp1.0E-01_map20_ds1ds5compare.png
.. _|image18|: http://4.bp.blogspot.com/-G7ks6aygM8w/TbcssORKmqI/AAAAAAAAGIU/aFrSrgTEhc4/s1600/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01_compare.png
.. _|image19|: http://4.bp.blogspot.com/-MemhZbvFgYw/Tbcssv4s06I/AAAAAAAAGIc/8aSHBsnKHuU/s1600/airy_test_ds5_reconv_arrang45_atmotest_amp1.0E-01_compare.png
.. _|image20|: http://2.bp.blogspot.com/-UvoCV4PvBcM/TbcstPbA_5I/AAAAAAAAGIk/S1cPsnCGmvc/s1600/091219_o15-6_ds5_uranus_indivtest_reconv_ds1ds5compare.png
.. _|image21|: http://2.bp.blogspot.com/-ab27Av_tJB4/Tbcu3Jp0x6I/AAAAAAAAGIs/xUjzxFEVYXI/s1600/091219_o15-6_ds5_uranus_indivtest_reconvBL_ds1ds5compare.png
.. _|image22|: http://4.bp.blogspot.com/-WwNjh1U-xu0/TbcyTyab16I/AAAAAAAAGI0/oO1fOiY4Bow/s1600/091219_o16_ds1_uranus_indivtest_reconv_ds1ds5compare.png
.. _|image23|: http://3.bp.blogspot.com/-k2U0rWMtcH8/TbcyUxfGrfI/AAAAAAAAGI8/ErLepYPyYJE/s1600/091219_o15_ds1_uranus_indivtest_reconv_ds1ds5compare.png
.. _|image24|: http://2.bp.blogspot.com/-FQGo3OPClLw/Tbc5gVqn-1I/AAAAAAAAGJE/RSmGgDcDSK0/s1600/091219_o15-6_ds1_uranus_indivtest_reconv091219_o15_raw_ds1.nc_indiv13pca_weights_iter10.png
.. _|image25|: http://1.bp.blogspot.com/-M0u4dlKj5IM/Tbc5g7PQ5YI/AAAAAAAAGJM/njdiKaENlzI/s1600/091219_o15-6_ds5_uranus_indivtest_reconv091219_o15_raw_ds5.nc_indiv13pca_weights_iter10.png
.. _|image26|: http://1.bp.blogspot.com/-pL-VkELw7g4/Tbc7OrD5d6I/AAAAAAAAGJU/zCB9wyF09_g/s1600/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01_weights_iter20.png
.. _|image27|: http://4.bp.blogspot.com/-D0GDZ-wq0ZY/Tbc7PIM2pQI/AAAAAAAAGJc/38Edm0ufAs4/s1600/airy_test_ds5_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01_weights_iter20.png
.. _|image28|: http://4.bp.blogspot.com/-S_3X_HkqzF4/Tbc7v7rrs4I/AAAAAAAAGJk/y0Wkwo3JYhg/s1600/091219_o15-6_ds1_uranus_indivtest_reconv091219_o15_raw_ds1.nc_indiv13pcatimestream004_plots_10_bolo12.png
.. _|image29|: http://4.bp.blogspot.com/-lg_Z50_vocc/Tbc7wZXRUlI/AAAAAAAAGJs/fcuf9u241QE/s1600/091219_o15-6_ds5_uranus_indivtest_reconv091219_o15_raw_ds5.nc_indiv13pcatimestream004_plots_10_bolo12.png
.. _|image30|: http://1.bp.blogspot.com/-cG1uUEY_N9M/Tbc-ZJtPVzI/AAAAAAAAGJ0/VGcWV0JYtxQ/s1600/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01timestream011_plots_20_bolo07.png
.. _|image31|: http://3.bp.blogspot.com/-4KA5jSCQgsY/Tbc-ZhvL_lI/AAAAAAAAGJ8/brh-nGwSses/s1600/airy_test_ds5_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01timestream011_plots_20_bolo07.png
.. _|image32|: http://1.bp.blogspot.com/-2MZXbARZeWo/Tbc-xHG3bOI/AAAAAAAAGKE/yEiYQ8YqqkU/s1600/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E%252B00timestream011_plots_20_bolo07.png
.. _|image33|: http://2.bp.blogspot.com/-Lr1QqlLNc20/Tbc-xhLCH3I/AAAAAAAAGKM/N1GKh-hZZ-Q/s1600/airy_test_ds5_reconv_arrang45_atmotest_varyrelscale_amp1.0E%252B00timestream011_plots_20_bolo07.png

.. |image0| image:: http://4.bp.blogspot.com/-xZqAo2n84iE/TbcsrsLkkaI/AAAAAAAAGIM/J_4xWIOGoCQ/s320/exp2_varyrelscale_amp1.0E-01_map20_ds1ds5compare.png
.. |image1| image:: http://4.bp.blogspot.com/-G7ks6aygM8w/TbcssORKmqI/AAAAAAAAGIU/aFrSrgTEhc4/s320/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01_compare.png
.. |image2| image:: http://4.bp.blogspot.com/-MemhZbvFgYw/Tbcssv4s06I/AAAAAAAAGIc/8aSHBsnKHuU/s320/airy_test_ds5_reconv_arrang45_atmotest_amp1.0E-01_compare.png
.. |image3| image:: http://2.bp.blogspot.com/-UvoCV4PvBcM/TbcstPbA_5I/AAAAAAAAGIk/S1cPsnCGmvc/s320/091219_o15-6_ds5_uranus_indivtest_reconv_ds1ds5compare.png
.. |image4| image:: http://2.bp.blogspot.com/-ab27Av_tJB4/Tbcu3Jp0x6I/AAAAAAAAGIs/xUjzxFEVYXI/s320/091219_o15-6_ds5_uranus_indivtest_reconvBL_ds1ds5compare.png
.. |image5| image:: http://4.bp.blogspot.com/-WwNjh1U-xu0/TbcyTyab16I/AAAAAAAAGI0/oO1fOiY4Bow/s320/091219_o16_ds1_uranus_indivtest_reconv_ds1ds5compare.png
.. |image6| image:: http://3.bp.blogspot.com/-k2U0rWMtcH8/TbcyUxfGrfI/AAAAAAAAGI8/ErLepYPyYJE/s320/091219_o15_ds1_uranus_indivtest_reconv_ds1ds5compare.png
.. |image7| image:: http://2.bp.blogspot.com/-FQGo3OPClLw/Tbc5gVqn-1I/AAAAAAAAGJE/RSmGgDcDSK0/s320/091219_o15-6_ds1_uranus_indivtest_reconv091219_o15_raw_ds1.nc_indiv13pca_weights_iter10.png
.. |image8| image:: http://1.bp.blogspot.com/-M0u4dlKj5IM/Tbc5g7PQ5YI/AAAAAAAAGJM/njdiKaENlzI/s320/091219_o15-6_ds5_uranus_indivtest_reconv091219_o15_raw_ds5.nc_indiv13pca_weights_iter10.png
.. |image9| image:: http://1.bp.blogspot.com/-pL-VkELw7g4/Tbc7OrD5d6I/AAAAAAAAGJU/zCB9wyF09_g/s320/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01_weights_iter20.png
.. |image10| image:: http://4.bp.blogspot.com/-D0GDZ-wq0ZY/Tbc7PIM2pQI/AAAAAAAAGJc/38Edm0ufAs4/s320/airy_test_ds5_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01_weights_iter20.png
.. |image11| image:: http://4.bp.blogspot.com/-S_3X_HkqzF4/Tbc7v7rrs4I/AAAAAAAAGJk/y0Wkwo3JYhg/s320/091219_o15-6_ds1_uranus_indivtest_reconv091219_o15_raw_ds1.nc_indiv13pcatimestream004_plots_10_bolo12.png
.. |image12| image:: http://4.bp.blogspot.com/-lg_Z50_vocc/Tbc7wZXRUlI/AAAAAAAAGJs/fcuf9u241QE/s320/091219_o15-6_ds5_uranus_indivtest_reconv091219_o15_raw_ds5.nc_indiv13pcatimestream004_plots_10_bolo12.png
.. |image13| image:: http://1.bp.blogspot.com/-cG1uUEY_N9M/Tbc-ZJtPVzI/AAAAAAAAGJ0/VGcWV0JYtxQ/s320/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01timestream011_plots_20_bolo07.png
.. |image14| image:: http://3.bp.blogspot.com/-4KA5jSCQgsY/Tbc-ZhvL_lI/AAAAAAAAGJ8/brh-nGwSses/s320/airy_test_ds5_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01timestream011_plots_20_bolo07.png
.. |image15| image:: http://1.bp.blogspot.com/-2MZXbARZeWo/Tbc-xHG3bOI/AAAAAAAAGKE/yEiYQ8YqqkU/s320/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E%252B00timestream011_plots_20_bolo07.png
.. |image16| image:: http://2.bp.blogspot.com/-Lr1QqlLNc20/Tbc-xhLCH3I/AAAAAAAAGKM/N1GKh-hZZ-Q/s320/airy_test_ds5_reconv_arrang45_atmotest_varyrelscale_amp1.0E%252B00timestream011_plots_20_bolo07.png
.. |image17| image:: http://4.bp.blogspot.com/-xZqAo2n84iE/TbcsrsLkkaI/AAAAAAAAGIM/J_4xWIOGoCQ/s320/exp2_varyrelscale_amp1.0E-01_map20_ds1ds5compare.png
.. |image18| image:: http://4.bp.blogspot.com/-G7ks6aygM8w/TbcssORKmqI/AAAAAAAAGIU/aFrSrgTEhc4/s320/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01_compare.png
.. |image19| image:: http://4.bp.blogspot.com/-MemhZbvFgYw/Tbcssv4s06I/AAAAAAAAGIc/8aSHBsnKHuU/s320/airy_test_ds5_reconv_arrang45_atmotest_amp1.0E-01_compare.png
.. |image20| image:: http://2.bp.blogspot.com/-UvoCV4PvBcM/TbcstPbA_5I/AAAAAAAAGIk/S1cPsnCGmvc/s320/091219_o15-6_ds5_uranus_indivtest_reconv_ds1ds5compare.png
.. |image21| image:: http://2.bp.blogspot.com/-ab27Av_tJB4/Tbcu3Jp0x6I/AAAAAAAAGIs/xUjzxFEVYXI/s320/091219_o15-6_ds5_uranus_indivtest_reconvBL_ds1ds5compare.png
.. |image22| image:: http://4.bp.blogspot.com/-WwNjh1U-xu0/TbcyTyab16I/AAAAAAAAGI0/oO1fOiY4Bow/s320/091219_o16_ds1_uranus_indivtest_reconv_ds1ds5compare.png
.. |image23| image:: http://3.bp.blogspot.com/-k2U0rWMtcH8/TbcyUxfGrfI/AAAAAAAAGI8/ErLepYPyYJE/s320/091219_o15_ds1_uranus_indivtest_reconv_ds1ds5compare.png
.. |image24| image:: http://2.bp.blogspot.com/-FQGo3OPClLw/Tbc5gVqn-1I/AAAAAAAAGJE/RSmGgDcDSK0/s320/091219_o15-6_ds1_uranus_indivtest_reconv091219_o15_raw_ds1.nc_indiv13pca_weights_iter10.png
.. |image25| image:: http://1.bp.blogspot.com/-M0u4dlKj5IM/Tbc5g7PQ5YI/AAAAAAAAGJM/njdiKaENlzI/s320/091219_o15-6_ds5_uranus_indivtest_reconv091219_o15_raw_ds5.nc_indiv13pca_weights_iter10.png
.. |image26| image:: http://1.bp.blogspot.com/-pL-VkELw7g4/Tbc7OrD5d6I/AAAAAAAAGJU/zCB9wyF09_g/s320/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01_weights_iter20.png
.. |image27| image:: http://4.bp.blogspot.com/-D0GDZ-wq0ZY/Tbc7PIM2pQI/AAAAAAAAGJc/38Edm0ufAs4/s320/airy_test_ds5_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01_weights_iter20.png
.. |image28| image:: http://4.bp.blogspot.com/-S_3X_HkqzF4/Tbc7v7rrs4I/AAAAAAAAGJk/y0Wkwo3JYhg/s320/091219_o15-6_ds1_uranus_indivtest_reconv091219_o15_raw_ds1.nc_indiv13pcatimestream004_plots_10_bolo12.png
.. |image29| image:: http://4.bp.blogspot.com/-lg_Z50_vocc/Tbc7wZXRUlI/AAAAAAAAGJs/fcuf9u241QE/s320/091219_o15-6_ds5_uranus_indivtest_reconv091219_o15_raw_ds5.nc_indiv13pcatimestream004_plots_10_bolo12.png
.. |image30| image:: http://1.bp.blogspot.com/-cG1uUEY_N9M/Tbc-ZJtPVzI/AAAAAAAAGJ0/VGcWV0JYtxQ/s320/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01timestream011_plots_20_bolo07.png
.. |image31| image:: http://3.bp.blogspot.com/-4KA5jSCQgsY/Tbc-ZhvL_lI/AAAAAAAAGJ8/brh-nGwSses/s320/airy_test_ds5_reconv_arrang45_atmotest_varyrelscale_amp1.0E-01timestream011_plots_20_bolo07.png
.. |image32| image:: http://1.bp.blogspot.com/-2MZXbARZeWo/Tbc-xHG3bOI/AAAAAAAAGKE/yEiYQ8YqqkU/s320/airy_test_ds1_reconv_arrang45_atmotest_varyrelscale_amp1.0E%252B00timestream011_plots_20_bolo07.png
.. |image33| image:: http://2.bp.blogspot.com/-Lr1QqlLNc20/Tbc-xhLCH3I/AAAAAAAAGKM/N1GKh-hZZ-Q/s320/airy_test_ds5_reconv_arrang45_atmotest_varyrelscale_amp1.0E%252B00timestream011_plots_20_bolo07.png
