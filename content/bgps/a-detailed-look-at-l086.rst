A detailed look at l086
#######################
:date: 2009-03-04 21:35
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, mapping
:slug: a-detailed-look-at-l086

Despite a slew of alignment errors, it appears that the alignment for
MOST fields turns out OK using Method 3 of the pixel-shift code; the
signal to noise is VERY low in a lot of fields.
070724\_o38 does not come up with a good fit, for very good reason -
there appears to be no signal at all.
070907\_o20 is a problem. The offset was 27 pixels, which is too large,
but nonetheless correct. I had to institute the plane fitter at an
earlier stage to get it to work.
However, the biggest problem: the SCUBA source aligns with 070907\_o20
but not the rest of the maps. So I needed to re-fit everything. That was
a BIG mistake, we need to check carefully for it in other fields.
