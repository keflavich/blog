New code
########
:date: 2008-09-05 21:00
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, pipeline
:slug: new-code

Done for the day after this (observing tonight)
two new procedures::

 alignment_offsets_to_ncdf.pro
 calcoeffs_to_ncdf.pro

they're really easy, very nearly one-liners. Once they've been used
once, you can just use ncdf\_varput\_scale
Modified keyword parameters in do\_the\_pointing: offsets will always be
applied unless the keyword 'no\_offsets' is passed into the code (or the
top-level wrapper). Since offsets default to zero, this should be OK.
