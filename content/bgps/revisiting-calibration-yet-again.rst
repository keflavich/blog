Revisiting calibration yet again
################################
:date: 2011-03-23 00:22
:author: Adam (noreply@blogger.com)
:tags: googlepost, planning, calibration, pipeline
:slug: revisiting-calibration-yet-again

The recent hiatus for paper revisions has, unfortunately, come to an
end.
Re-examining my work, I did quite a lot but encountered many dead-ends.
First, we would very much like to use an \*identical\* reduction process
on both the calibration data and the science data. That way, we could
feel very confident that the reduction process isn't introducing any
weird artifacts.
Unfortunately, I discovered early on that using ds5 data, 13 pca
components, and n>1 iterations resulted in strange shape and flux
conservation failures. These errors do NOT occur in co-added maps; they
are unique to single-observation scans (though I don't recollect whether
2 scans is enough or if you need more).
I spent many hours banging my head against this problem and have never
gotten a satisfactory solution. But perhaps it's time to approach it
again. The map00 images look MUCH rounder and generally better than the
map10 images.
So, the problem I need to examine is the iterative process. Why does it
fail for single images? Is it something about the noise properties?
model00 looks fine... what gets put into the timestream? Examining
timestreams is a terrible and horrendous process... but what else can I
do?
The next step will be to examine the timestreams of a particular
observation. I think a good choice is 101208\_ob7; the next observation,
101208\_ob8 was a large-area map and it looks fine (i.e., it improves
with iteration). So I can start looking at the effects of polysub,
iteration, etc. on this particular source.
Of course, the stupid trick with the pipeline - every time - is that
"fixing" a problem for one source has a nasty tendency to break it for
all other sources. That's why there are so many flags that can be passed
around. Still, this is the approach I have to take...
