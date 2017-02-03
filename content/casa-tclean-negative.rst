CASA tclean adds negative components
####################################
:date: 2016-05-01 10:21 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa, tclean

I'm trying to examine some of my 7m+12m combined data and have run into yet another
mysterious behavior of CASA.  ``tclean`` is adding negative components in regions with
exclusively positive emission.

In this image, the *left* is the clean image, which doesn't make any sense; it
looks like it should be a residual image but it is not.  2nd image is the clean
components (negative!!), 3rd is the residual, 4th is the dirty map.

.. image:: |filename|/images/casa/bad_cleancomps.png
   :width: 600px

One tricky thing for this particular image is that the emission is real, BUT it
is also directly on top of a major sidelobe of the brightest source in the
region.  Nonetheless, I cannot imagine any way to explain the negative
component.  I don't really understand when a negative component is added, but
presumably it ought to happen when the residual has a negative value but also
the highest amplitude in the map; this obviously never happens here since the
residual in fact has one of the highest *positive* amplitudes in the map.

The imaging parameters seem not to affect this problem. I attempted reducing the
gain to 0.05 to no avail.  Changing from natural to robust weighting actually
removed most of the negative components.

Failed combination of 7m and 12m data
-------------------------------------
The above was a tangent.  The real reason I was working on this data set was to
combine the 7m and 12m spectral data.  The problem I keep seeing is very large,
smooth blobs that are spatially distinct from the more compact emission.  It's
as if someone took the two independent cubes (12m and 7m) and just added them
together; it looks like flux is not being conserved.

The UV plots, especially weight vs uvdist, look fine.  The 7m antenna are
downweighted relative to the 7m antennae by a factor ~2.

One of the bigger problems is that I have a vague - possibly not justified - 
sense that there is a velocity offset of ~1 km/s between the 7m and 12m data.
If this is the case, there's no wonder the combination isn't working.
However, it's nearly inconceivable.

Followup Feb 2017
-----------------
That vague fear turned out to be entirely justified.  It turned out that the 7m
and 12m array data sets were not in a common frame, and they were therefore
offset by something like the Earth's change in velocity between the observation
dates.  The solution was to cvel the data sets to the LSRK frame prior to
concatenating them.  While I know I made these changes, I unfortunately can't
find the specific commit where I made them.
