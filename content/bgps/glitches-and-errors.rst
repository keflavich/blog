Glitches and errors
###################
:date: 2008-08-11 04:24
:author: Adam (noreply@blogger.com)
:tags: googlepost
:slug: glitches-and-errors

It's definitely important to get rid of the spikes and, more
importantly, the exponential decay. The current function is pretty good,
but possibly not good enough because there are some situations in which
the turnaround decay is obviously not well-enough dealt with and results
in high/low streaks.
The glitches can be ~20 Jy. The problem is that they sometimes show up
in the middle of sources (e.g. in 060609\_o26). That will badly distort
fluxes.
My ideal is still to use a median instead of mean combination of data
points into image points, but that seems to be impractical to implement.
Other ideas...
