Inconsistent
############
:date: 2008-08-17 18:56
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, pointing
:slug: inconsistent

James: "I think it's fair to say, though, that there is some problem
with the simultaneous assumption that CSO coords are geo and that we are
applying the ab/nut correction correctly."
Yep. The relevant files are in /scratch/adam\_work/plots/:
models\_noabnut\_radec\_0707.ps
models\_noabnut\_rawcsoptg\_radec\_0707.ps
models\_oppositeabnut\_radec\_0707.ps
models\_oppositeabnut\_rawcso\_radec\_0707.ps
I'm afraid they're pretty confusing.
'noabnut' means no aberration/nutation correction was applied during the
mapping process.
'oppositeabnut' means that an aberration/nutation correction that,
according to the eq2hor and hor2eq texts, should actually convert
heliocentric to geocentric, is being used on data that we believe is
starting in a geocentric frame. There are two possibilities: 1. We are
wrong 2. eq2hor/hor2eq are wrong.
The 'rawcso' files have FAZO/FZAO "subtracted out" (removed) in pages 1
and 3, and FAZO/FZAO added back in on pages 2 and 4. 'rawcso' means that
we're looking at the ra/dec the CSO gave without the users' FAZO/FZAO
corrections.
The non-rawcso have the NCDF ra/dec vectors, with precession correction
applied (and some form of ab/nut correction), but the FAZO/FZAO are
still present. THESE should be equivalent to Meredith's plots, e.g.
where FAZO\_SET/FZAO\_SET are on the y axis. However, that's only true
for pages 1 and 3. Pages 2 and 4 have FAZO/FZAO essentially
double-subtracted, so they should be ignored. Pages 1 and 3 of the
non-rawcso files should be equivalent to pages 2 and 4 of the rawcso
files with the exception that the sigma-rejection used to choose the
yellow points is different.
So what's in each page? On pages 1 and 2, the red lines are my best fit
to the yellow data, which is the black data with an iterative sigma
rejection applied (i.e. reject at 1 sigma, recalculate sigma from good
data, reject at 2 sigma). The blue lines are Meredith's models. The
right side includes only the yellow data points with the red line
subtracted. On pages 3 and 4, the same is pretty much true except that
ONLY the altitude-dependent line has been subtracted: there is no fit to
azimuth.
Also, the 'sourcecompare' files are similar. I'd check those out too.
I still don't have the extremely low RMS that Meredith saw. I'm going to
go through and try to reject bad data points by hand to see if I can get
to that level. We'll see.
