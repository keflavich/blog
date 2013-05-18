flagger
#######
:date: 2008-11-22 01:37
:author: Adam (noreply@blogger.com)
:tags: googlepost, flagging
:slug: flagger

Discovered that the flagger causes some pretty serious problems if you
try to run it on a non-coadd for obvious reasons: there's practically no
coverage! Individual maps should NOT go through the flagger, so I have
added a piece of code that turns off the flagger if only one observation
is being used. That code is in map\_iter where the flagger is called.
