Careful comparison of ds1 and ds5
#################################
:date: 2011-03-29 15:23
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, calibration, pipeline
:slug: careful-comparison-of-ds1-and-ds5

I looked very closely at the timestream and maps of 101208\_o11 and had
a pretty hard time figuring out why the data were different, but it
looked like the data really did differ on a point-by-point basis
(according to pyflagger). The only conclusion I was able to draw is that
the scaling must be off. I realized that the scaling was being done
before delining. I moved scaling from readall\_pc to premap, and it
brought at least this one source into agreement. Time to run ds1-ds5
comparisons again!
(this means that ds1 data MUST have deline run on it, but ds5 data
doesn't really need it)
Here are examples of ds1 and ds5 timestreams, with and without scaling,
and ds1 with and without delining:

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

   <div class="separator" style="clear: both; text-align: center;">

`|image4|`_

.. raw:: html

   </div>

.. raw:: html

   </p>

.. _|image5|: http://4.bp.blogspot.com/-KR_NYG31_O0/TZECtBAgqFI/AAAAAAAAGCg/1jC9Ys2r9Iw/s1600/101208_o11_ds5_uranus_indivtesttimestream011_plots_20_bolo02.png
.. _|image6|: http://3.bp.blogspot.com/-HbK-hAXjSDs/TZECtUNe8AI/AAAAAAAAGCo/i4fsH12Iw8Y/s1600/101208_o11_ds1_uranus_indivtest_delinetimestream011_plots_20_bolo02.png
.. _|image7|: http://3.bp.blogspot.com/-edXLnDrrt5o/TZECt0No8oI/AAAAAAAAGCw/QjHg1ScBHG0/s1600/101208_o11_ds1_uranus_indivtesttimestream011_plots_20_bolo02.png
.. _|image8|: http://1.bp.blogspot.com/-4NIxFxEQ1jU/TZECuDJ1fVI/AAAAAAAAGC4/tGE5tDH_168/s1600/101208_o11_ds1_uranus_indivtest_deline_noscaleacbtimestream011_plots_20_bolo02.png
.. _|image9|: http://2.bp.blogspot.com/-DfIepZXXCFc/TZECuhm8lwI/AAAAAAAAGDA/Awp60ZuPGps/s1600/101208_o11_ds5_uranus_indivtest_noscaleacbtimestream011_plots_20_bolo02.png

.. |image0| image:: http://4.bp.blogspot.com/-KR_NYG31_O0/TZECtBAgqFI/AAAAAAAAGCg/1jC9Ys2r9Iw/s200/101208_o11_ds5_uranus_indivtesttimestream011_plots_20_bolo02.png
.. |image1| image:: http://3.bp.blogspot.com/-HbK-hAXjSDs/TZECtUNe8AI/AAAAAAAAGCo/i4fsH12Iw8Y/s200/101208_o11_ds1_uranus_indivtest_delinetimestream011_plots_20_bolo02.png
.. |image2| image:: http://3.bp.blogspot.com/-edXLnDrrt5o/TZECt0No8oI/AAAAAAAAGCw/QjHg1ScBHG0/s200/101208_o11_ds1_uranus_indivtesttimestream011_plots_20_bolo02.png
.. |image3| image:: http://1.bp.blogspot.com/-4NIxFxEQ1jU/TZECuDJ1fVI/AAAAAAAAGC4/tGE5tDH_168/s200/101208_o11_ds1_uranus_indivtest_deline_noscaleacbtimestream011_plots_20_bolo02.png
.. |image4| image:: http://2.bp.blogspot.com/-DfIepZXXCFc/TZECuhm8lwI/AAAAAAAAGDA/Awp60ZuPGps/s200/101208_o11_ds5_uranus_indivtest_noscaleacbtimestream011_plots_20_bolo02.png
.. |image5| image:: http://4.bp.blogspot.com/-KR_NYG31_O0/TZECtBAgqFI/AAAAAAAAGCg/1jC9Ys2r9Iw/s200/101208_o11_ds5_uranus_indivtesttimestream011_plots_20_bolo02.png
.. |image6| image:: http://3.bp.blogspot.com/-HbK-hAXjSDs/TZECtUNe8AI/AAAAAAAAGCo/i4fsH12Iw8Y/s200/101208_o11_ds1_uranus_indivtest_delinetimestream011_plots_20_bolo02.png
.. |image7| image:: http://3.bp.blogspot.com/-edXLnDrrt5o/TZECt0No8oI/AAAAAAAAGCw/QjHg1ScBHG0/s200/101208_o11_ds1_uranus_indivtesttimestream011_plots_20_bolo02.png
.. |image8| image:: http://1.bp.blogspot.com/-4NIxFxEQ1jU/TZECuDJ1fVI/AAAAAAAAGC4/tGE5tDH_168/s200/101208_o11_ds1_uranus_indivtest_deline_noscaleacbtimestream011_plots_20_bolo02.png
.. |image9| image:: http://2.bp.blogspot.com/-DfIepZXXCFc/TZECuhm8lwI/AAAAAAAAGDA/Awp60ZuPGps/s200/101208_o11_ds5_uranus_indivtest_noscaleacbtimestream011_plots_20_bolo02.png
