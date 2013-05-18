Downsampling - what is going on?
################################
:date: 2011-02-11 04:19
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, pipeline
:slug: downsampling-what-is-going-on

The downsampling failure I `noted`_ `previously`_ appears to be
illusory. It may be that the offset noted only holds for single-frame
images, in which there may be many blank pixels. It is possible - though
not certain - that the ds1 images were significantly higher than ds5
because more noise-only pixels were included with higher outliers; i.e.,
ds1 high-outlier noise was being compared to ds5 noise that was lower
amplitude.
What led to these conclusions? First, I was getting inconsistent results
looking at Uranus in particular - ds5 appeared to have higher fluxes
than ds1. This was inconsistent with `earlier results`_ on OMC1. Partly,
this is because I switched from my `hacked-together plots`_ to the much
more refined `compare\_images`_ script, which demonstrated the effect of
changing the cutoff of the comparison.
Also, I added in a Pearson Correlation Coefficient computation. Given a
single data set with the only difference being downsampling, the data
should be perfectly correlated even if there is a flux offset
(correlation should be 1, but the best fit slope should not be). It was
an indication of a problem when I started seeing correlation
coefficients <0.90 for data that had already been sigma-cut; that means
that noise was being included in the correlation computations.
Therefore, the approach needed is to cut out the high pixels that are on
map edges. This I accomplished by adding an 'aperture' capability to the
compare\_images code (for Uranus) and cropping using montage and a
wcs-based box for Orion.
The results... are ambiguous. Wow. In some sub-fields - within the same
co-added map - the agreement is near-perfect.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_

.. raw:: html

   </div>

In others, ds1 is clearly > ds5 .

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image1|`_

.. raw:: html

   </div>

What's going on? ds1 does look uniformly more smooth.
Note that the *disagreement* is nearly scale-free:\ `|image2|`_
OK, so given the conclusion in Orion that ds1>=ds5, what's the deal with
Uranus?

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image3|`_

.. raw:: html

   </div>

The first two comparisons are for 1x1° observations; in both cases ds1 <
ds5, but by 6% and 24% respectively! The image of Uranus looks much
better (because of lack of parallel lines) in the second, more extreme
case. In both cases, the ds5 excess is nearly scale-free (not shown).

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

The 3x1s are also highly discrepant. #12 shows nearly perfect agreement,
albeit with high dispersion (low correlation) because of pixel-to-pixel
variations around the peak. #13 is the only observation with a huge DS1
excess. It also demonstrates very poor correlation. It looks like the
telescope got bumped for the ds5 data (which is not actually possible;
recall they're the same data set). What happened here? Maybe a glitch
that went unflagged (mad\_flagger is off by default for individual
scans)?

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image6|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image7|`_

.. raw:: html

   </div>

In observations 4 and 5, we're looking at a 40-50% excess in ds5! What
the heck? There really is no clear explanation for this.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image8|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image9|`_

.. raw:: html

   </div>

But... what? Magically, they come into perfect agreement when the scan
axis nearly lines up with the coordinate axis! Or, is this just an
effect of the worse weather on night 2?

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image10|`_

.. raw:: html

   </div>

Next thing to try: masked source map comparison. Unfortunately, masking
royally screwed up the long scans - probably because the initial polysub
didn't work. And masking in the individual point source maps did
nothing... so that pretty much rules out atmospheric oversubtraction,
doesn't it?
What else could be causing this offset? 0pca looks the same as 13pca,
give or take, so it's not the atmospheric subtraction. Could the
downsampling result in an offset in the bolo-scaling? Where else in the
process could things go wrong? Tomorrow, need to investigate .sav files
with pyflagger...

.. raw:: html

   </p>

.. _noted: http://bolocam.blogspot.com/2011/01/downsampling-has-serious-negative.html
.. _previously: http://bolocam.blogspot.com/2011/01/more-evidence-that-downsampling-causes.html
.. _earlier results: http://bolocam.blogspot.com/2011/01/downsampling-has-serious-negative.html
.. _hacked-together plots: http://4.bp.blogspot.com/_lsgW26mWZnU/TTiWWl3j3dI/AAAAAAAAF3I/Ef3WHEv5oXU/s1600/omc1_dstest_pixel-pixel.png
.. _compare\_images: http://code.google.com/p/bgpspipeline/source/browse/bgps_pipeline/plotting/compare_images.py
.. _|image11|: http://1.bp.blogspot.com/-i20j3FEx758/TVR-PbQl7lI/AAAAAAAAGAY/imgMqceS9n8/s1600/v2.0_dl_omc_b_OMC4_ds1ds5_compare.png
.. _|image12|: http://4.bp.blogspot.com/-JsRH_ZQilWM/TVR-Os6vBSI/AAAAAAAAGAQ/JRR6Trm-weo/s1600/v2.0_dl_omc_b_OMC2_ds1ds5_compare.png
.. _|image13|: http://2.bp.blogspot.com/-J1XXZki2sxU/TVSXhlmGZKI/AAAAAAAAGAg/aDyQ7Sz2CfM/s1600/v2.0_dl_omc_b_OMC2_ds1ds5_psd_compare.png
.. _|image14|: http://3.bp.blogspot.com/-AosJ1vzcYSs/TVSZjIZ81fI/AAAAAAAAGAk/qVGeaJtkbPA/s1600/101208_o10_ds1ds5_compare.png
.. _|image15|: http://1.bp.blogspot.com/_lsgW26mWZnU/TVSZki9k9OI/AAAAAAAAGA0/t9LOGHOAL7Q/s1600/101208_o10_ds1ds5_compare.png
.. _|image16|: http://2.bp.blogspot.com/_lsgW26mWZnU/TVSZj1pglLI/AAAAAAAAGAs/-4153NoAQQ0/s1600/101208_o11_ds1ds5_compare.png
.. _|image17|: http://3.bp.blogspot.com/-9gwzGfDBCEk/TVSZllWeBxI/AAAAAAAAGA8/x3mg5RbMScs/s1600/101208_o12_ds1ds5_compare.png
.. _|image18|: http://3.bp.blogspot.com/-9gwzGfDBCEk/TVSZllWeBxI/AAAAAAAAGA8/x3mg5RbMScs/s1600/101208_o13_ds1ds5_compare.png
.. _|image19|: http://1.bp.blogspot.com/_lsgW26mWZnU/TVSaYfZx0WI/AAAAAAAAGBE/cWbbBQCJOvk/s1600/101208_ob4_ds1ds5_compare.png
.. _|image20|: http://2.bp.blogspot.com/_lsgW26mWZnU/TVSaZM27sqI/AAAAAAAAGBM/XR-6pttUcBo/s1600/101208_ob5_ds1ds5_compare.png
.. _|image21|: http://3.bp.blogspot.com/_lsgW26mWZnU/TVSaaP6ISNI/AAAAAAAAGBU/PvN5aFOxBAQ/s1600/101209_ob5_ds1ds5_compare.png

.. |image0| image:: http://1.bp.blogspot.com/-i20j3FEx758/TVR-PbQl7lI/AAAAAAAAGAY/imgMqceS9n8/s1600/v2.0_dl_omc_b_OMC4_ds1ds5_compare.png
.. |image1| image:: http://4.bp.blogspot.com/-JsRH_ZQilWM/TVR-Os6vBSI/AAAAAAAAGAQ/JRR6Trm-weo/s1600/v2.0_dl_omc_b_OMC2_ds1ds5_compare.png
.. |image2| image:: http://2.bp.blogspot.com/-J1XXZki2sxU/TVSXhlmGZKI/AAAAAAAAGAg/aDyQ7Sz2CfM/s320/v2.0_dl_omc_b_OMC2_ds1ds5_psd_compare.png
.. |image3| image:: http://3.bp.blogspot.com/-AosJ1vzcYSs/TVSZjIZ81fI/AAAAAAAAGAk/qVGeaJtkbPA/s320/101208_o10_ds1ds5_compare.png
.. |image4| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TVSZki9k9OI/AAAAAAAAGA0/t9LOGHOAL7Q/s320/101208_o10_ds1ds5_compare.png
.. |image5| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TVSZj1pglLI/AAAAAAAAGAs/-4153NoAQQ0/s320/101208_o11_ds1ds5_compare.png
.. |image6| image:: http://3.bp.blogspot.com/-9gwzGfDBCEk/TVSZllWeBxI/AAAAAAAAGA8/x3mg5RbMScs/s320/101208_o12_ds1ds5_compare.png
.. |image7| image:: http://3.bp.blogspot.com/-9gwzGfDBCEk/TVSZllWeBxI/AAAAAAAAGA8/x3mg5RbMScs/s320/101208_o13_ds1ds5_compare.png
.. |image8| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TVSaYfZx0WI/AAAAAAAAGBE/cWbbBQCJOvk/s320/101208_ob4_ds1ds5_compare.png
.. |image9| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TVSaZM27sqI/AAAAAAAAGBM/XR-6pttUcBo/s320/101208_ob5_ds1ds5_compare.png
.. |image10| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TVSaaP6ISNI/AAAAAAAAGBU/PvN5aFOxBAQ/s320/101209_ob5_ds1ds5_compare.png
.. |image11| image:: http://1.bp.blogspot.com/-i20j3FEx758/TVR-PbQl7lI/AAAAAAAAGAY/imgMqceS9n8/s1600/v2.0_dl_omc_b_OMC4_ds1ds5_compare.png
.. |image12| image:: http://4.bp.blogspot.com/-JsRH_ZQilWM/TVR-Os6vBSI/AAAAAAAAGAQ/JRR6Trm-weo/s1600/v2.0_dl_omc_b_OMC2_ds1ds5_compare.png
.. |image13| image:: http://2.bp.blogspot.com/-J1XXZki2sxU/TVSXhlmGZKI/AAAAAAAAGAg/aDyQ7Sz2CfM/s320/v2.0_dl_omc_b_OMC2_ds1ds5_psd_compare.png
.. |image14| image:: http://3.bp.blogspot.com/-AosJ1vzcYSs/TVSZjIZ81fI/AAAAAAAAGAk/qVGeaJtkbPA/s320/101208_o10_ds1ds5_compare.png
.. |image15| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TVSZki9k9OI/AAAAAAAAGA0/t9LOGHOAL7Q/s320/101208_o10_ds1ds5_compare.png
.. |image16| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TVSZj1pglLI/AAAAAAAAGAs/-4153NoAQQ0/s320/101208_o11_ds1ds5_compare.png
.. |image17| image:: http://3.bp.blogspot.com/-9gwzGfDBCEk/TVSZllWeBxI/AAAAAAAAGA8/x3mg5RbMScs/s320/101208_o12_ds1ds5_compare.png
.. |image18| image:: http://3.bp.blogspot.com/-9gwzGfDBCEk/TVSZllWeBxI/AAAAAAAAGA8/x3mg5RbMScs/s320/101208_o13_ds1ds5_compare.png
.. |image19| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TVSaYfZx0WI/AAAAAAAAGBE/cWbbBQCJOvk/s320/101208_ob4_ds1ds5_compare.png
.. |image20| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TVSaZM27sqI/AAAAAAAAGBM/XR-6pttUcBo/s320/101208_ob5_ds1ds5_compare.png
.. |image21| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TVSaaP6ISNI/AAAAAAAAGBU/PvN5aFOxBAQ/s320/101209_ob5_ds1ds5_compare.png
