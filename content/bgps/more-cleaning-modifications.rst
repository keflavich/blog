More cleaning modifications
###########################
:date: 2008-08-12 17:01
:author: Adam (noreply@blogger.com)
:tags: googlepost, pipeline
:slug: more-cleaning-modifications

I had removed sigmadeglitch from deline, now it's permanently gone. I
think it might be worth exploring re-inserting sigmadeglitch somewhere.
My higher-order polynomial fit is creating deeper bowls around sources,
so that's a big problem, but if I use a lower order I get the bad
streaks. What's the best way to deal with this? I'm thinking perhaps
only doing the polysub on the second iteration (i.e. after a source
model has been subtracted).
Delining runs into some issues now, though, because not all frequencies
are sampled (?).
