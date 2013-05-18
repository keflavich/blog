Weighting and Scaling
#####################
:date: 2011-04-19 23:08
:author: Adam (noreply@blogger.com)
:tags: googlepost
:slug: weighting-and-scaling

The "simple" relative sensitivity calibration was causing serious
problems.
The assumed model for a "gain" $G$, timestream $S$, and reference
timestream $R$ is:
$S = G R$
Naively, one would assume that something like
$G = median(S/R)$
would work. However, it doesn't. The distribution of $G$ values looks
like:
