Rant: calc_beam_locations
#########################
:date: 2009-02-06 18:24
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post
:slug: rant-calc_beam_locations

It took me a few days to figure this out, but "calc\_beam\_locations" is
about 800 lines of wasted space. It does nothing substantive until line
335. Everything to that point is parameter parsing. But there doesn't
need to be any of that crap, really, and it should have been outsourced
to functions to begin with.
NCDF files are read to get the rotation angle - JUST as an error check!
There is no a priori reason to include it.
All that the code does is read in a centroid file (a list of x,y
offsets), rotate them, and output them as r,theta,error. Sure, there's a
bunch of automated outlier rejection etc, but... seriously?! We don't
have enough observations to hold up the statistics necessary for that to
begin with! NO ONE would if each observation takes an hour. It's absurd.
Odd as it is coming from me, manual rejection makes a lot more sense in
this case.
Now, I still have to understand WHY the beam locations are rotated by
the fiducial array angle.
