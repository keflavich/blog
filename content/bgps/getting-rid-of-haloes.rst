Getting rid of haloes
#####################
:date: 2012-03-31 00:28
:author: Adam (noreply@blogger.com)
:tags: googlepost, artifacts, deconvolution, mapping
:slug: getting-rid-of-haloes

Haloes are when images look like this:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_

.. raw:: html

   </div>

instead of this, as they should:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image1|`_

.. raw:: html

   </div>

Things to try:

#. Pass ``/return_deconv`` to deconv\_map
#. Pass ``/linear`` to deconv\_map
#. Disable deconvolve - deconvolve=0

In l123 & l169, at least, ``/return_deconv`` worked

.. raw:: html

   </p>

.. _|image2|: http://1.bp.blogspot.com/-Hwwiewo9FyU/T3Yhs6TpYcI/AAAAAAAAG0k/uKSTBCn95FY/s1600/Screen%2Bshot%2B2012-03-30%2Bat%2B3.09.54%2BPM.png
.. _|image3|: http://4.bp.blogspot.com/-t5jVccq9Dtc/T3Yhs-hcY5I/AAAAAAAAG0s/EZ4x0zdSgxw/s1600/Screen%2Bshot%2B2012-03-30%2Bat%2B3.09.58%2BPM.png

.. |image0| image:: http://1.bp.blogspot.com/-Hwwiewo9FyU/T3Yhs6TpYcI/AAAAAAAAG0k/uKSTBCn95FY/s320/Screen%2Bshot%2B2012-03-30%2Bat%2B3.09.54%2BPM.png
.. |image1| image:: http://4.bp.blogspot.com/-t5jVccq9Dtc/T3Yhs-hcY5I/AAAAAAAAG0s/EZ4x0zdSgxw/s320/Screen%2Bshot%2B2012-03-30%2Bat%2B3.09.58%2BPM.png
.. |image2| image:: http://1.bp.blogspot.com/-Hwwiewo9FyU/T3Yhs6TpYcI/AAAAAAAAG0k/uKSTBCn95FY/s320/Screen%2Bshot%2B2012-03-30%2Bat%2B3.09.54%2BPM.png
.. |image3| image:: http://4.bp.blogspot.com/-t5jVccq9Dtc/T3Yhs-hcY5I/AAAAAAAAG0s/EZ4x0zdSgxw/s320/Screen%2Bshot%2B2012-03-30%2Bat%2B3.09.58%2BPM.png
