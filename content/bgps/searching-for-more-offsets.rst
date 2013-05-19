Searching for more offsets
##########################
:date: 2008-08-12 21:35
:author: Adam (noreply@blogger.com)
:tags: googlepost, pointing
:slug: searching-for-more-offsets

The defining feature of my pointing calculations - and their
inconsistency - is that the spread for individual sources is bad, which
means that there's still something wrong in the way the bulk ra/dec are
being calculated.

I checked apply\_distortion\_map\_radec to see if it might have inserted
some bulk offset, but it only changes the average position by <2". That
might be an issue, but the boresight isn't necessarily aligned with the
mean location of the bolometers. It should be shifted by at least .3"
according to a simple average of sin/cos of the bolo\_params angles.
Comparing my pointing code to map\_ncdf\_reading directly:

readstruct=map\_ncdf\_reading(filename,/nopixoff)
offsets are small (e.g. -0.050665803 -0.0029540043 arcseconds ra/dec) if
I don't subtract fazo/fzao
offsets in ra/dec are remarkably close to fazo/fzao if I subtract them::

     92.830656 -126.12773
     95.000000 -120.00000

which is because ra/dec are pretty closely aligned to az/el.
So, any difference comes from at least one of the keyword parameters.
Therefore I AM missing something, and that something is one of the
keywords to map\_ncdf\_reading
