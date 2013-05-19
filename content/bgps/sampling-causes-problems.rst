Sampling causes problems
########################
:date: 2011-04-18 23:39
:author: Adam (noreply@blogger.com)
:tags: googlepost, downsampling, pipeline
:slug: sampling-causes-problems

One of the simplest experiments that can be run is a point-source
observed in point-scan mode, i.e. with smaller step-sizes. I've done
this for an Airy disk with noise added in the image plan but not
atmosphere (some noise is necessary to avoid bizarre artifacts with
weighting when you have truly zero signal and zero noise). At a S/N of
500, the noise is pretty minimal, though.
It turns out for the 'noiseless' images, the PCA cleaning is the
issue... curiously, it varies significantly with iteration. Is it worth
trying to debug the PCA cleaning for noiseless timestreams? I mean...
they really shouldn't have any correlated information anyway.
There is still an outstanding issue where one bolometer gets scaled to
be higher than the rest without any apparent reason for doing so.
It is also clear that we do not nyquist-sample the pixels with the
timestream. However, that doesn't explain a deficiency observed in the
ds1 images. Also note that the sidelobes are not picked up at this S/N,
but that's not too surprising.
And here is the explanation: The peak is missed by about 10% because of
finite sampling? Somehow the sampled gaussian nearly uniformly
underestimates the gaussian... I think this violates theory a bit.....

.. image:: http://3.bp.blogspot.com/-L2CMkehyV2g/TazJvpj2jjI/AAAAAAAAGGg/_BM0_GgC_x4/s320/airy_test_ds1_reconv_arrang45_atmotest_amp1.0E-01timestream011_plots_20_bolo07.png

Here's the problem shown again:

.. image:: http://2.bp.blogspot.com/-vvY-1uleKmk/TazKE4Osm_I/AAAAAAAAGGo/n6Nadxi8UM4/s320/airy_test_ds1_reconv_arrang45_atmotest_amp1.0E-01_compare.png

This is a comparison between the input image and a ds1-sampled image
with perfectly correlated atmospheric noise. So there is something in
the pipeline that is preventing the peaks from achieving the necessary
heights.... I wonder if resampling the deconvolved image onto a
higher-resolution grid, then downsampling afterwards, would fix this?
Also note that the flux loss increases from 7% to 20% from ds1 to ds5:

.. image:: http://4.bp.blogspot.com/-hHQBTMME8Ow/TazKuf0gkuI/AAAAAAAAGGw/uQdJw4kc2U8/s320/airy_test_ds5_reconv_arrang45_atmotest_amp1.0E-01_compare.png

.. _|image3|: http://3.bp.blogspot.com/-L2CMkehyV2g/TazJvpj2jjI/AAAAAAAAGGg/_BM0_GgC_x4/s1600/airy_test_ds1_reconv_arrang45_atmotest_amp1.0E-01timestream011_plots_20_bolo07.png
.. _|image4|: http://2.bp.blogspot.com/-vvY-1uleKmk/TazKE4Osm_I/AAAAAAAAGGo/n6Nadxi8UM4/s1600/airy_test_ds1_reconv_arrang45_atmotest_amp1.0E-01_compare.png
.. _|image5|: http://4.bp.blogspot.com/-hHQBTMME8Ow/TazKuf0gkuI/AAAAAAAAGGw/uQdJw4kc2U8/s1600/airy_test_ds5_reconv_arrang45_atmotest_amp1.0E-01_compare.png

