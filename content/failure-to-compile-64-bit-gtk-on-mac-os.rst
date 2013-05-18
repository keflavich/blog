Failure to compile 64 bit gtk on mac os
#######################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, computer

Attempted to install gtk+-2.17.2 on my mac. Had to install:
``glib-2.21.2``
which would not let me compile with multiple architectures, and
``pkgconfig-0.9.0,``
which won't configure because:
``configure: configuring in glib-1.2.8configure: running /bin/sh './configure' --prefix=/usr/local  CC= CFLAGS= LDFLAGS= --cache-file=/dev/null --srcdir=.configure: warning: CC=: invalid host typeconfigure: warning: CFLAGS=: invalid host typeconfigure: error: can only configure for one host and one target at a timeconfigure: error: /bin/sh './configure' failed for glib-1.2.8``
which is bs because I don't have any compiler flags set.

So, gtk+ seems hopeless.
UPDATE: 0.9.0 is not the latest version, 0.23.0 is. Dumb version
numbering.

GTK is absurd to install. You need:

 * pkg-config
 * glib
 * cairo
 *  pixman
 * pango (MUST be installed AFTER cairo)
 * `atk`_
 * `libtiff`_
 * `libjpg`_
 * `jpeg2000`_ - but I just passed a flag to not do this because it didn't install right. ``--without-libjasper``
 * `fontconfig`_ I mean, really? at this point it's just ridiculous....

and finally, it died with this:
checking Pango flags... configure: error:

::
    \*\*\* Pango not found. Pango built with Cairo support is required
    \*\*\* to build GTK+. See http://www.pango.org for Pango information.

which meant that I had to reinstall Pango because I had installed it
before Cairo.

I believe this is where the term `dependency hell`_ comes from.

Also, I don't think any of these are x86-64 compatible.

Then I'm STILL not done.
PyGTK dies with an import error on dsextras, which a painful google
search traces to pygobject. pygobject makes and installs fine.... but
then I find out it installed to
/usr/local/lib/python2.6/site-packages/gtk-2.0/, which is obviously not
on my python path since I installed a framework.

So:
``./configure --prefix=/Library/Frameworks/Python.framework/Versions/2.6/``
in both pygobject and pygtk.

Oh, guess what? Need pycairo too. What happens there? What you'd guess::

    ld warning: in /Developer/SDKs/MacOSX10.5.sdk/usr/local/lib/libcairo.dylib, file is not of required architecture

so when I configure pygtk:

The following modules will be built:
 * atk
 * pango

The following modules will NOT be built:
 * pangocairo
 * gtk
 * gtk.glade
 * gtk.unixprint

Damn. That blows.

::

    python-64 -c "import gtk"
    ImportError:
    dlopen(/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/gtk-2.0/glib/\_glib.so,
    2): no suitable image found. Did find:

    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/gtk-2.0/glib/\_glib.so:
    mach-o, but wrong architecture

FAIL.

.. _atk: http://ftp.gnome.org/pub/gnome/sources/atk/
.. _libtiff: ftp://ftp.remotesensing.org/pub/libtiff/
.. _libjpg: http://www.ijg.org/
.. _jpeg2000: http://www.openjpeg.org/index.php
.. _fontconfig: http://fontconfig.org/wiki/
.. _dependency hell: http://en.wikipedia.org/wiki/Dependency_hell
