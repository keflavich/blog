4.3 Relative Alignment and Mosaicing
####################################
:date: 2009-03-04 02:57
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, methods paper
:slug: 43-relative-alignment-and-mosaicing

Relative alignment was performed by finding the peak of the
cross-correlation between images and a pointing master selected from the
epoch with the best-constrained pointing model for that field. Each
observation was initially mapped individually, then all observations of
a given field were cross-correlated with a selected master image of that
field. The cross-correlation peak was fit with a gaussian and the
difference between the gaussian peak and the image center was used as
the pixel offset. The offsets were recorded and written to the
timestreams. Finally, all observations of a field were merged into a
single timestream with pointing offsets applied to create the field
mosaic.
