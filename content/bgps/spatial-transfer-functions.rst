Spatial Transfer Functions
##########################
:date: 2011-07-13 18:54
:author: Adam (noreply@blogger.com)
:tags: googlepost, simulation
:slug: spatial-transfer-functions

The majority of the past week has been dedicated to debugging; it looks
like cross-scanned simulations finally work.
The plot below is a derivation of the spatial transfer function for a
number of different intrinsic sky power-law power spectra.


.. image:: http://2.bp.blogspot.com/-JyAPg0u9uQ8/Th3kuQh1fpI/AAAAAAAAGRs/pP7o3n9_wds/s320/Experiment10_AverageRecoveryFunction.png


Justifying the above plot is essential.
First, the very steep power-laws [-3 in the example below] show a
recovery fraction >1. This is simply because their S/N was inadequate -
the output power spectrum is nearly flat, but at a level higher than the
sky.


.. image:: http://4.bp.blogspot.com/-JPBjsLDfP5M/Th3lw5n1xTI/AAAAAAAAGR0/aDeOmMv5s8w/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky00_seed00_peak010.00_nosmooth_compare.png



.. image:: http://3.bp.blogspot.com/-LOCDmoLCcZs/Th3lxfnKVzI/AAAAAAAAGR8/9NCM3OroGoM/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky00_seed00_peak010.00_nosmooth_psds.png


Second, the most plausible power-laws [-1.5 in the example below] show
pretty good recovery (90-95% over the relevant range):


.. image:: http://1.bp.blogspot.com/-MTZ8WGl3ZRc/Th3mMkvv2II/AAAAAAAAGSE/0OO4Te39fPI/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky03_seed00_peak010.00_nosmooth_compare.png



.. image:: http://2.bp.blogspot.com/-5IeTZW-ZTAw/Th3mNHPC8gI/AAAAAAAAGSM/WhIWClGWqbo/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky03_seed00_peak010.00_nosmooth_psds.png



.. image:: http://4.bp.blogspot.com/-O6ofm7GaxUI/Th3mNgf29AI/AAAAAAAAGSU/VzQ7aL-yd_E/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky03_seed00_peak010.00_nosmooth_stf.png


There are some "white" power losses, particularly in the flatter
power-spectra. My best guess is that this has something to do with the
relative scales being offset from a mean of 1, but so far all tests to
show that that is the cause have in fact shown no problems at all. What
else could cause a scale-independent power loss?
Also, the flat power spectrum (and inverted) aren't quite flat because I
impose a "galactic scale height" on them. Should I stop doing that?


.. _|image6|: http://2.bp.blogspot.com/-JyAPg0u9uQ8/Th3kuQh1fpI/AAAAAAAAGRs/pP7o3n9_wds/s1600/Experiment10_AverageRecoveryFunction.png
.. _|image7|: http://4.bp.blogspot.com/-JPBjsLDfP5M/Th3lw5n1xTI/AAAAAAAAGR0/aDeOmMv5s8w/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky00_seed00_peak010.00_nosmooth_compare.png
.. _|image8|: http://3.bp.blogspot.com/-LOCDmoLCcZs/Th3lxfnKVzI/AAAAAAAAGR8/9NCM3OroGoM/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky00_seed00_peak010.00_nosmooth_psds.png
.. _|image9|: http://1.bp.blogspot.com/-MTZ8WGl3ZRc/Th3mMkvv2II/AAAAAAAAGSE/0OO4Te39fPI/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky03_seed00_peak010.00_nosmooth_compare.png
.. _|image10|: http://2.bp.blogspot.com/-5IeTZW-ZTAw/Th3mNHPC8gI/AAAAAAAAGSM/WhIWClGWqbo/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky03_seed00_peak010.00_nosmooth_psds.png
.. _|image11|: http://4.bp.blogspot.com/-O6ofm7GaxUI/Th3mNgf29AI/AAAAAAAAGSU/VzQ7aL-yd_E/s1600/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky03_seed00_peak010.00_nosmooth_stf.png

.. |image6| image:: http://2.bp.blogspot.com/-JyAPg0u9uQ8/Th3kuQh1fpI/AAAAAAAAGRs/pP7o3n9_wds/s320/Experiment10_AverageRecoveryFunction.png
.. |image7| image:: http://4.bp.blogspot.com/-JPBjsLDfP5M/Th3lw5n1xTI/AAAAAAAAGR0/aDeOmMv5s8w/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky00_seed00_peak010.00_nosmooth_compare.png
.. |image8| image:: http://3.bp.blogspot.com/-LOCDmoLCcZs/Th3lxfnKVzI/AAAAAAAAGR8/9NCM3OroGoM/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky00_seed00_peak010.00_nosmooth_psds.png
.. |image9| image:: http://1.bp.blogspot.com/-MTZ8WGl3ZRc/Th3mMkvv2II/AAAAAAAAGSE/0OO4Te39fPI/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky03_seed00_peak010.00_nosmooth_compare.png
.. |image10| image:: http://2.bp.blogspot.com/-5IeTZW-ZTAw/Th3mNHPC8gI/AAAAAAAAGSM/WhIWClGWqbo/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky03_seed00_peak010.00_nosmooth_psds.png
.. |image11| image:: http://4.bp.blogspot.com/-O6ofm7GaxUI/Th3mNgf29AI/AAAAAAAAGSU/VzQ7aL-yd_E/s320/exp10_ds2_astrosky_arrang45_atmotest_amp1.0E%252B01_sky03_seed00_peak010.00_nosmooth_stf.png
