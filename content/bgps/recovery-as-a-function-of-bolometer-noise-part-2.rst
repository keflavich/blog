Recovery as a function of bolometer noise part 2
################################################
:date: 2011-05-27 23:49
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, simulation
:slug: recovery-as-a-function-of-bolometer-noise-part-2

In the Experiment 7 simulations I was running, I observed greater noise
than expected, causing me to question the results of the `previous
post`_. I therefore ran Experiment 8, which is the same as Experiment 6
from that post with a larger (320x320) map with a larger step size. The
noise recovery remains linear, but the scaling is quite different - a
factor of ~4 instead of ~12. The step size is the most likely culprit,
since an 8x larger step size should result in sqrt(8)~2.8 worse noise
per pixel.

.. image:: http://1.bp.blogspot.com/-ubZ-9LXWmXQ/TeAdFoOUcZI/AAAAAAAAGMY/bSSwM2JuLyA/s320/exp8_measurednoise_vs_bolonoiseRMS.png

There are some curious / worrisome artifacts that turn up and are
evident in the recovery fraction plot. For the low-noise cases, the
middle bolometers get totally flagged out because they are over-weighted
(by orders of magnitude).

.. image:: http://3.bp.blogspot.com/-0KKwo1wB6aI/TeAdFz6pTiI/AAAAAAAAGMg/yHGsx8j7WMM/s320/exp8_recovery_vs_bolonoiseRMS.png

So I'm forced to explore via pyflagger. I will almost certainly need to
re-run all experiments after making a change to how weights are
computed.
Well, it turns out the problem is that those 28 bolos are scaled to
zero, even though there is nothing obvious (or even suggestive) in their
timestream plots. This is only true when varyrelscale is off. Apparently
varying the relative scales leads to a different problem.
AHA! The noise is so low that the relative scales are SO well correlated
that the signal is enough to cause problems! A plausible solution is
therefore no change to the pipeline, but to add minimal (nominal) noise
to the relative scales to increase the MAD so that the others don't get
flagged out.
So I added a 1% variation, which prevented flagging at the scale stage,
but there are still some disturbing artifacts in the map:

.. image:: http://4.bp.blogspot.com/-TX2_8PsUgdM/TeA4Iu9T5FI/AAAAAAAAGMo/vfEjTGcSBp0/s320/psf_ds1_reconv_arrang45_atmotest_noise%252B1.0E-03_amp1.0E%252B00_compare.png

Unfortunately, this problem requires further examination in detail. Exp
9/10 should probably be gaussians and airys on larger step-size maps,
but the solution will require something else, possibly even a change in
the pipeline. On the plus side, I think I can re-run experiment 7 with a
factor of 4 instead of 12 scaling for the noise and expect it to work.

.. _previous post: http://bolocam.blogspot.com/2011/05/recovery-as-function-of-bolometer-noise.html
.. _|image3|: http://1.bp.blogspot.com/-ubZ-9LXWmXQ/TeAdFoOUcZI/AAAAAAAAGMY/bSSwM2JuLyA/s1600/exp8_measurednoise_vs_bolonoiseRMS.png
.. _|image4|: http://3.bp.blogspot.com/-0KKwo1wB6aI/TeAdFz6pTiI/AAAAAAAAGMg/yHGsx8j7WMM/s1600/exp8_recovery_vs_bolonoiseRMS.png
.. _|image5|: http://4.bp.blogspot.com/-TX2_8PsUgdM/TeA4Iu9T5FI/AAAAAAAAGMo/vfEjTGcSBp0/s1600/psf_ds1_reconv_arrang45_atmotest_noise%252B1.0E-03_amp1.0E%252B00_compare.png

