Weighting - next steps
######################
:date: 2008-11-15 01:04
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post
:slug: weighting-next-steps

Idea: 'edge taper' for scans. The scan start/end usually has higher
noise, so it would be good to downweight those regions slightly.
Probably only the first/last 5% of each scan should be linearly
downweighted.
I'm running a lot of tests on l001 with/without deconvolution, lots of
iterations, different pca components. They'll be done sometime tomorrow.
