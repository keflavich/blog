FFTs and unlucky primes
#######################
:date: 2008-08-12 17:04
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, mapping
:slug: ffts-and-unlucky-primes

I've encountered a lot (!) of unlucky prime numbers that I'm trying to
FFT in too many places, and it basically stops the code.
211151 was impossibly bad, 5827 is pretty bad too.
I solved the first by splitting into by-scan delining, which is better
anyway. But the second is a map, in which I KNOW zero padding is OK.
So... are there any functions that find the nearest reasonably efficient
map size?
