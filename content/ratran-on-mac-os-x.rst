RATRAN on Mac OS X
##################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, astronomy, computer

Mac OS X doesn't like the defaults built in to `RATRAN`_. It died
unhappily with errors like:
``ld_classic: can't locate file for: -lcrt0.o``
and
``ld: warning: in /usr/local/lib//libcfitsio.a, file is not of required architecture``
In order to get it to run, I had to do the following:

#. Install CFITSIO with ``CFLAGS="-arch x86_64 -arch i386 -g -O2"`` to
   /usr/local/lib
#. Edit the sky/Makefile OPT variable (line 23) to read:
   ``OPT = -I. -O2 -fno-automatic -arch x86_64``

Also, you need to set up system variables:

::

    export RATRAN=/path/to/Ratran export RATRANRUN=/path/to/Ratran/run 


.. _RATRAN: http://www.sron.rug.nl/~vdtak/ratran/frames.html
