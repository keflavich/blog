Cleaning ideas
##############
:date: 2008-08-11 15:20
:author: Adam (noreply@blogger.com)
:tags: googlepost
:slug: cleaning-ideas

It's proving very difficult to get rid of glitches, so here are some
more ideas:
 Median filter the whole timestream (downsampled) at a resolution that
will pull down the glitch peak. Subtract out the median-filtered
timestream from the original, and look for outliers in that
distribution: in principle, those should be glitches.
 Another option: subtract out the noise map AND the best-model map from
the original timestream before trying to pull out additional astro model
stuff. The map-to-timestream astro model can't include glitches because
they're averaged over, but the sky-subtracted timestream DOES include
glitches (no matter how many PCA components are removed) because
glitches are NOT correlated across detectors. The weird thing is that
this is effectively subtracting out exactly what was calculated from the
sky subtraction - the question is whether subtracting it out BEFORE sky
subtracting again gets you any benefit. If it was just noise,
subtracting noise from noise is fine, but the "noise" does include some
residual signal.
