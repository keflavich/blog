Deconvolve and Epochs
#####################
:date: 2011-04-05 18:12
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, distortion mapping, weighting, pipeline
:slug: deconvolve-and-epochs

I've spent a large portion of the last week working on the deconvolver.
I found `previously`_ that a reconvolved map does a better job of
restoring flux than the straight-up deconvolved map for point sources /
pointing observations.
However, the same update broke the regular mapping modes, leading to
horrible instability in the mapping routines for large maps such as W5.
Curiously, it seems that the aspect that breaks is the weighting;
somehow the noise drops precipitously in certain bolometers, leading to
extremely high weights. Perhaps they somehow dominate the PCA
subtraction and therefore have all their noise removed?
Either way, there are a few large-scale changes that need to be made:

#. Since Scaling and Weighting are now done on a whole-timestream basis,
   we should only map single epochs at once and coadd them after the
   fact. This approach will also help relieve RAM strain. Since it
   appears that individual observations are now reasonably convergent
   with the proper treatment of NANs in the deconvolution scheme, it
   should be possible to take any individual map and coadd it in a
   reasonable way.
#. Bolometers with bad weights need to be thrown out. Alternatively, and
   more appropriately, I need to discover WHY their weights are going
   bad.

We also need to explore different weighting schemes.

#. 1/Variance over whole timestream (current default)
#. 1/Variance on a per-scan basis (previous default) [based on PSDs]
#. Minimum Chi\ :sup:`2` with Astrophysical Model (??)
#. Min Chi\ :sup:`2` on a per-scan basis?

Because of the extensive testing this will require, it is really
becoming essential that we develop an arbitrary map creation & testing
routine.

.. raw:: html

   </p>

.. _previously: http://bolocam.blogspot.com/2011/03/workaround-for-individual-maps.html
