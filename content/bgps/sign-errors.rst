sign errors
###########
:date: 2009-02-01 19:50
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, calibration
:slug: sign-errors

pinned down the problem. Was a minor sign error in the offsets. Why is
it that simple sign errors are ALWAYS the hardest things to track down?
Now, open question: should x,y scaling be free parameters or not? What I
mean is, when I measure the positions of bolometers on the array using
the planet map, should I allow the X and Y stretch (the bolometer
spacing) to change? Should it be a uniform stretch in X and Y or should
it be allowed to 'distort' too? My opinion is, none of the above: I'm
measuring their actual positions (in terms of a fixed spacing) and
therefore stretching or distorting to match the nominal positions is not
necessary.
