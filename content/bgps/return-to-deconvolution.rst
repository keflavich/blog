Return to Deconvolution
#######################
:date: 2009-02-23 18:55
:author: Adam (noreply@blogger.com)
:tags: googlepost, mapping
:slug: return-to-deconvolution

I ran the v0.7 reductions with deconvolution on for 50 iterations. I had
cut out deconvolution originally because of the funky noise maps, but
that was partly an error on my part. There is also an issue with bright
sources being largely left over in the noise maps.
The deconvolver does MUCH better at filtering out the fuzzy atmospheric
emission, so I want to use it. It leaves some flux from bright point
sources behind, though, so I decided to try to make the deconvolution
kernel smaller to see if that recovers more of the pointlike flux.
