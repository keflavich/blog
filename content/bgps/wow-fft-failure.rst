Wow - FFT failure
#################
:date: 2008-08-12 15:11
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, pipeline
:slug: wow-fft-failure

On my huge Cygnus run, the fft keeps failing in the deline code. It's
actually pretty impressive, but there are 844604 points in the
timestream. The prime factorization of 844604 is 2^2 \* 211151. This is
just damned bad luck, because I think an FFT is extremely inefficient
when it can't factorize. What's the best workaround? ....
9 AM update: I've rewritten the deliner to work on a scan-by-scan basis.
It's possible that the delining failed in the past because it was
essentially removing a constant amplitude at the line frequencies across
the observation (or combined observations!) which is not likely to be
true.
