Update - Pointing Model
#######################
:date: 2008-08-01 16:43
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, pointing
:slug: update-pointing-model

Update - Pointing Model 7/31/08
The pointing model application "works" now, but I have a problem with
our model. We don't get down to the <10" RMS offset we're looking for.
The mean offsets are all zero, but the spread is more like 20".
Example plots on milkyway: [see attached PDFs too]

::
    /scratch/adam\_work/plots/models\_ptgmdl\_0506.ps
    /scratch/adam\_work/plots/models\_ptgmdl\_0707.ps
    /scratch/adam\_work/plots/models\_rawcsoptg\_0506.ps
    /scratch/adam\_work/plots/models\_rawcsoptg\_0707.ps

On the left side are plotted "all" of the data points, on the right I've
used a two-iteration 3-sigma rejection to eliminate outliers to a small
degree.

Top of these plots - as labeled - is altoff vs. alt, bottom is azoff vs.
alt.

The red lines are a 2nd order polynomial fit to the data.

The cyan lines are the pointing model corrections calculated by
Meredith.

The 'ptgmdl' files have had the pointing model corrections applied. Note
that they are centered around offsets of zero.

The 'rawcsoptg' files DO NOT have pointing model corrections applied,
and FZAO/FAZO have been REMOVED from the original pointing. Hence, these
are RAW CSO TELESCOPE POINTING plots.

Things to note:

 * In the 0707 'ptgmdl' set, the az is not quite centered at zero
 * the 0506 'ptgmdl' set still has bulk offsets
 * the ALTOFF and AZOFF are in delta-coordinate: this means that azoff

should be scaled by dividing by cos(alt) to put the y-axis in consistent
units. In most cases, this means that the already large spread at higher
altitudes is going to INCREASE. That means the problem is going to get
worse...
Questions:

 1. What is the main difference between my plots and Meredith's? i.e.  why is
    my RMS ~an order of magnitude larger?
 2. Does more outlier rejection make sense? Is there any reason not to trust
    certain observations if they visible turn out right?  PPSes are supposed to
    be "absolute references" for the 1x1, 3x1 maps OLD PROBLEM: PPS and large
    maps mapped with same 'pointing model' but ended up with different
    coordinates
