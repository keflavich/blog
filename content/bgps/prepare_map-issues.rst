prepare_map issues
##################
:date: 2008-09-01 16:31
:author: Adam (noreply@blogger.com)
:tags: googlepost, mapping
:slug: prepare_map-issues

The problem: There is a bulk offset that can range from small to ~22'
(largest observed so far) in the combined maps that is not present in
the individual maps.
Observations: I THINK the offset between ra/dec and l/b is most
pronounced when the map boundaries are most different.
We have been putting CRPIX in the middle of the map (i.e. number of x/y
elements divided by 2), which is not the same position as the median
ra/dec or l/b. I figured this might be a problem, but there's not really
a way around it - if you just set CRPIX to be 0,0, it doesn't change
anything. xy2ad and ad2xy produce self-consistent results, but that
doesn't mean anything either.
I think the problem is that AD2XY is largely ignorant of CRPIX: it
calculates x/y offsets from the CRVAL assuming that the CRVAL is at
CRPIX.... but I don't know why that should be wrong. Ideas? More to come
if I figure anything out.
Update: from doing the individual maps in l/b vs ra/dec, I don't think
the offset is between l/b and ra/dec.... something less fundamental.
Update 2: still no clues after reading ad2xy and trying to plow through
parts of wcssph2xy. gotta be rect\_pix\_tstream, but I think it's
right....
Update 3: I think I have figured out the problem, currently testing. My
idea has to do with the fact that all x,y positions in
rect\_pix\_tstream are positive, but ad2xy is not constrained to return
positive values. In principle, the two-iteration ad2xy should take care
of this, but in the case where the middle of the map in pixels is not
the middle of the map in the WCS coordinate system, it is still possible
to get negative pixel mappings out of the 2nd iteration. I'm still
confused about whether this is really possible - makes my head fuzzy -
but I tried implementing a solution where I simply shift the crpix
rather than recalculating with AD2XY.
Update 4: Based on L111, my test in update 3 fixed the problem. Scuba
contours are correct, and reasonably consistent across the field - still
need to do the more complete test, e.g. Cygnus
Update 5: Cygnus tests still await completion, but a very close
inspection of single L111 maps reveals a ~2 pixel difference that could
go a long way to explaining my high-RMS pointing calculations. Still
doesn't explain the sine curve, but anything helps...
Update 6: My correction definitely fixed the problem, EXCEPT there's
still an ambiguity at the .5 pixel level. Specifically, is AD2XY
treating the pixel center as .5,.5 or 0,0? Ditto IDL. I believe (from my
simulated data) that this ambiguity is still causing a problem.
Update 7: New correction fixed problem to better than 1" (checked by
making a simulated map with 1" pixels) - probably 'perfect' now. Read
prepare\_map.pro for details. The issue was a difference in pixel
centers.
