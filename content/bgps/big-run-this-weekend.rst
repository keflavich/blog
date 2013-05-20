Big run this weekend...
#######################
:date: 2008-08-09 17:22
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, mapping
:slug: big-run-this-weekend

In case anyone is wondering why Milkyway is going really slowly, I'm
mapping a 69-observation set of Cygnus. It ought to prove to be an
interesting test of Milkyway's swap capacity, but other than that I
doubt it will be useful. While the pointing is reasonably good at this
point (30" still, but whatever), I haven't done ANY work on filtering
out bad observations / flagging stuff in Cyg. Data massaging is going to
be a long process, it would be great if I could do that instead of
pointing stuff. Argh.
One thing to note is that this file:
/scratch/sliced/l078/070702\_o33\_raw\_ds5.nc
is a "\_ds5.nc" but is NOT downsampled!
Update:
Mapped the individual files successfully, picked out noisy ones. The
overall map failed - just not enough memory to do a field that large. I
split it up in to two sets of 25 observations, plus I'll be mapping each
L 70-L 90 field separately (I didn't get ride of noisy observations for
this). I'm also remapping the individual observations with PSD flagging
enabled to see how that works.
For notes on the P Cyg observations, see the file
/scratch/adam\_work/texts/cygnus\_for\_pat.in
