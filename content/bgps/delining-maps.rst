Delining - Maps
###############
:date: 2011-02-03 22:16
:author: Adam (noreply@blogger.com)
:tags: googlepost, mapping, pipeline, deline
:slug: delining-maps

First comment - delining has **no effect** on downsampled data. At least
for the 0709 epoch, there were NO lines AT ALL in the data. From 0-5 Hz,
it was just empty. So we don't have to worry about that... the problem
only affects fully-sampled data.
Then, onto map comparisons. Curiously, the noise levels don't drop after
delining. They actually go up a bit. This may be because of the effects
on PCA cleaning.
However, flux levels in the sources go up by 0-10%. As usual, the change
in flux changes from field to field without any obvious reason.
Example 1: A pointing field. The source is ~2% brighter in the delined
version, but otherwise the match between the two is nearly perfect.

.. image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUskr5xAMSI/AAAAAAAAF_M/J65CutNg9hM/s320/101208_ob8_compare.png
.. image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUsksatOJSI/AAAAAAAAF_U/9X-rM6JQmCU/s320/101208_ob8_psd.png

Example 2: A bigger map, where the flux recovery is much greater when
delining, but the background levels are also higher.

.. image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUsoBrKcQyI/AAAAAAAAF_c/junIzma1zg4/s320/101208_o11_compare.png

.. image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUsoCFL1DiI/AAAAAAAAF_k/b1QrgajdlaE/s320/101208_o11_psd.png

.. _|image4|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUskr5xAMSI/AAAAAAAAF_M/J65CutNg9hM/s1600/101208_ob8_compare.png
.. _|image5|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUsksatOJSI/AAAAAAAAF_U/9X-rM6JQmCU/s1600/101208_ob8_psd.png
.. _|image6|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUsoBrKcQyI/AAAAAAAAF_c/junIzma1zg4/s1600/101208_o11_compare.png
.. _|image7|: http://3.bp.blogspot.com/_lsgW26mWZnU/TUsoCFL1DiI/AAAAAAAAF_k/b1QrgajdlaE/s1600/101208_o11_psd.png

