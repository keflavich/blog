Progress on alignment, ideas for the next few steps
###################################################
:date: 2008-09-15 02:19
:author: Adam (noreply@blogger.com)
:tags: googlepost, pipeline
:slug: progress-on-alignment-ideas-for-the-next-few-steps

Alignment: I did a more thorough test of the aligner, and found an error
that was getting me the wrong results. I'm still getting distinctly
different results than I got with imalign, but I'm not convinced they're
wrong. One problem I have to deal with is the ambiguity between pointing
model applied / no pointing model applied. In retrospect, I should have
done ALL of the maps with no pointing model: it would be simpler to
maintain a self-consistent set of alignment corrections.
However, since that isn't what I did - and there isn't enough memory to
host both data sets at the moment - I've dealt with the problem by
adding all of the offsets to the header. Hopefully now it will be
obvious if and what offsets have been applied, both pointing model and
'manual', from header keywords. Sadly, it was a pain to get that to work
- IDL's \_extra does not work the same way as normal keyword passing,
which is disappointing and frustrating because it made me rename a lot
of variables that should not have been renamed.
IF this alignment fails to produce perfect results (which I don't really
expect to happen - it will just take time to debug), it is still a good
first step, and all we'd really need to do is use bolocat to pull out
sources from the reference image and then match those in the others,
doing the same thing imalign does. It wouldn't be difficult but it would
be time consuming to program.
Had a bunch of ideas during my insomnia last night, but I'm afraid I
forgot most of them...
One idea was related to the use of MAD as opposed to STDDEV: it may
allow for a more robust sigma-rejection for automated flagging. But
that's difficult.
Another thought was using the maps to auto-identify glitches. To do
this, I'd make a combined map and an individual map, hastrom them, and
subtract the combined from the individual. We could then probably pretty
easily spot any glitches; they should be the only outliers left, in
principle. I'll test that idea, but it actually looks less promising
than I'd hoped. Things are not coming out right in preliminary tests -
huge residuals.
