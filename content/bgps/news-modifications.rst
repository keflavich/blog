News, modifications
###################
:date: 2008-08-03 07:19
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, pointing
:slug: news-modifications

RA / Dec mapping did change centroid locations, but not really for the
better. A deeper analysis is probably necessary, but nevertheless I'm
not convinced mapping type is the problem. The list of possible answers
to the question of why my pointing models don't match Meredith's:

#. The new mapping is shifting the centroid
#. The centroiding method I'm using is different / incorrect
#. There is still something in the pointing we haven't caught

The lack of systematics suggests that the third option is not correct.
The first seems the most likely, but also the most difficult to track
down. I don't know where to go with #2.
I've updated the code so that the pointing model correction offsets in
RA/Dec are written to the FITS header. This will be the standard in all
future runs for individual observations. The calculation of this offset
post-mapping is straightforward but it's nice to have a redundant error
check.
The report for Monday will be kind of empty, sadly. However, I think I
can say that I'll now move on to testing the previous problems we faced,
in particular that we could not match the pointing across whole fields
(L111). If THAT is fixed, then at least we know that whatever my
pipeline is doing differently (e.g. PA at all times...) is useful if not
100% correct.
I'll need to be in the office to test the field mappings, though,
because ds9 display doesn't work well over wireless. I'll do a remote
run of the individual L111 and W5 maps to compare to previous ones.

