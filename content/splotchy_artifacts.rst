CASA clean: "splotchy" artifacts
################################
:date: 2016-06-14 09:31
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, clean, artifacts


This image shows artifacts that look "splotchy".  They are locations clean has
placed a negative model component where none belongs, so the residual is highly
positive and the resulting image is negative.

.. image:: |static|/images/casa/splotchy.png
   :width: 600px

Discussing with others, it appears that this artifact may be unique to
multiscale clean and therefore may be a result of a too-strong component being
added on a large scale.  It is not yet clear how to suppress these artifacts,
but I'm attempting to change the scales included.  Other ideas would be welcome
in the comments.
