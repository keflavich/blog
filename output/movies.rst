MOVIES!
#######
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, animation, computer

Making movies is surprisingly difficult. No matter what language you
use, apparently true movie files can only be made by stringing together
images, i.e. there is no native movie-producing feature. Gnuplot can do
some simple animations but to do anything sophisticated you need to
start delving into variables, and for that I switch to a real language.
So, I returned to python. As usual, it took no more than a few hours of
coding and learning to come up with something. But it bothers me that it
took that long: I still think python is most deficient in its failure to
create a default column-text reader like 'readcol' in IDL. I can't
complain that much, though: I wrote `my own`_ in about 5 minutes.
Anyway, the key is to use the ``.set_xdata`` and ``.set_ydata``
functions of a plot to update a canvas. I still don't have nearly as
high a plotting speed as I'd like, but it works alright if I don't
display to screen. Probably a different backend would be more effective
but I don't like to mess with backends.
I use `` savefig(filename,dpi=50) `` to reduce the image quality so that
it's easier for the animator to handle.
ImageMagick's convert can be used to stitch any kind of image into a
movie given that you've installed an mpeg2 encoder (fink gave me
``mpeg2vidcodec      ``). The command is very simple:
``convert -size 300x300 *.png movie.mpg``
I had to use a smaller image size because a series of 1000x12kb files
somehow chomped ~6-8 GB of RAM and swap space.

.. _my own: http://casa.colorado.edu/~ginsbura/pyreadcol.htm
