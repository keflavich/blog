Deconvolution vs. Not
#####################
:date: 2008-11-28 19:39
:author: Adam (noreply@blogger.com)
:tags: googlepost, mapping
:slug: deconvolution-vs-not

I've done some by-eye comparisons of deconvolutions vs no deconvolution.
The no-deconvolution clearly does better on the bright sources: probably
the deconvolved beam size is a little bit different from (larger?
smaller?) the actual source size. Deconvolution does better in putting
noise from noisy regions into the noisemap and keeping it out of the
astromap.
Both might be useful - the deconvolved maps may end up being prettier,
but the no-deconvolve maps will probably have more reliable fluxes.
This all probably relies on testing / simulation.
