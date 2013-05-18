Pointing update
###############
:date: 2008-08-01 22:30
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, pointing
:slug: pointing-update

I believe I've completely dealt with the projection issues. There are a
lot of new plots available now, pretty much everything for Jun/Jul 05
and July 07. Low on my to-do list is the rest of the pointing model
tests.
My conclusion now is that I can't match the 3-4" RMS in dAlt and dAz.
Even with aggressive sigma-rejection of outliers, I only get down to
~10" RMS (which adds to ~15" RMS). My calculated pointing models differ
significantly from Meredith's, but not extremely so for 0707.
The code I've used to generate the plots is centroid\_plots.pro under
plotting/. Using that code, I am able to essentially reproduce each
change made in do\_the\_pointing besides the distortion mapping. Because
of the weak dependence of the pointing model on altitude, even errors on
the scale of precession won't really hurt the pointing model
calculations. The only unanswered question I think may be responsible
for some errors - but not enough, I think - is whether eq2hor/hor2eq
could be double-correcting for aberration and nutation, but this
wouldn't affect the actual data reduction. It WOULD affect my plotting!
I think my next test is to try to coadd different epochal data for
particular fields, e.g. l001, l033. Not l000 because of the galactic
coordinate issue.
