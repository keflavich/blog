pstopng
#######
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, postscript

Following `this thread`_ and my need to convert IDL .ps files to .pngs
so that I can view them in Mac Preview without having to go through an
(often failed) conversion process led to a few discoveries.
First, it is challenging to get ImageMagick's convert to make an opaque
background for the .ps file without seriously degrading the resolution.
This can be accomplished by passing *both* the ``-alpha Off`` and the
`` -density 300`` simultaneously. This is slow, though, and
recommendations to speed it up using the
``-limit area 4096 -limit memory 4096`` tags actually made it slower!
However, the thread pointed out that ghostscript can do the conversion
directly:
``gs -dBATCH -sDEVICE=png16m -r300 -dEPSCrop -dNOPAUSE -sOutputFile=XXX.png XXX.ps``
``-sDEVICE`` sets the output to png, ``-r300`` tag sets the density to
be 300 pixels/inch, ``-dEPSCrop`` is necessary to get the right sized
image out (otherwise it defaults to a portrait 8.5x11), and
`` -dBATCH `` prevents the gs command line from activating after the
command is executed. I'm not sure if ``-dNOPAUSE`` is necessary, but
apparently if you don't activate it you have to do something after every
page is processed.
My code to do batch ps-to-png conversion is available at
`http://code.google.com/p/agpy/source/browse/trunk/agpy/pstopng`_.
Timing demonstrations (units are seconds, R is 'real' or clock time, 'U'
is user time, and 'S' is system time):
``/usr/local/bin/convert -density 300 -alpha Off deline_zero_10hz_timestreams_003.ps deline_zero_10hz_timestreams_003.png TIMING: R: 3.126  U: 2.948  S: 0.084/usr/local/bin/convert -limit area 4096 -limit memory 4096 -density 300 -alpha Off deline_zero_10hz_timestreams_003.ps deline_zero_10hz_timestreams_003.png TIMING: R: 3.800  U: 2.970  S: 0.161gs -dBATCH -sDEVICE=png16m -r300 -dEPSCrop -dNOPAUSE -sOutputFile=deline_zero_10hz_timestreams_003.png deline_zero_10hz_timestreams_003.psTIMING: R: 0.801  U: 0.781  S: 0.017``

.. _this thread: http://studio.imagemagick.org/discourse-server/viewtopic.php?f=1&t=8545&start=0
.. _`http://code.google.com/p/agpy/source/browse/trunk/agpy/pstopng`: http://code.google.com/p/agpy/source/browse/trunk/agpy/pstopng
