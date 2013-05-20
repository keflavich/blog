PPS analysis
############
:date: 2010-06-16 18:06
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, calibration
:slug: pps-analysis

I've started looking at PPS fields to see if I can glean any additional
information about the "flux discrepancy" from them.  However, the
results are, as usual, unenlightening.
There is no consistent increase in flux when 3 PCA components are used
instead of 13 PCA components - very plausibly an indication that 13 PCA
is not too much to subtract because it's only atmosphere.  Similarly,
there is no obvious benefit to using a quadratic sky estimator instead
of a PCA estimator.
I'm using aperture photometry (without background subtraction) on
identical fields to perform these comparisons.  I've selected
(arbitrarily) the l357pps source as my comparison source.  The next step
(ongoing) is to compare to the co-added maps and crosshatched
large-scale maps of the same field.
(next step) PPS < single cross-hatched large-scale observation pair <
13PCA full combined map < 3PCA full combined map.
Unfortunately, this result implies that the small maps under-recover
flux, which suggests that the large maps are too bright, which is the
opposite of what we expect.  Additionally, lower noise -> more flux
recovered?
When background subtraction is included, the 3PCA and 13PCA fluxes match
nearly perfectly.
Despite the failure of this test (PPS < full field), I will do a
systematic comparison of PPS sources with 0PCA + masking to the large
fields in the hopes that doing so can provide a legitimate estimate of
the "scale factor" from treating small and large fields differently.
