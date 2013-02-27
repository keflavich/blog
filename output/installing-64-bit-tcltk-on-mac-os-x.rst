Installing 64 bit tcl/tk on Mac OS X
####################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, python, computer

Everything is described in this post:
http://www.nabble.com/Error-compiling-tk-8.5.7-on-Mac-OS-X-10.5-td23790967.html
But here's a script too:
``curl -O 'http://osdn.dl.sourceforge.net/sourceforge/tcl/t{cl,k}8.5.7-src.tar.gz'for f in t*8.5.7*.gz; do tar zxf $f; done cd tcl8.5.7/unix/./configure --enable-framework --enable-64-bitcd tk8.5.7/unix/./configure --enable-framework --enable-64-bitmake -j 4 -C tcl8.5.7/unix make -j 4 -C tk8.5.7/unixsudo make install -C tcl8.5.7/unix sudo make install -C tk8.5.7/unix ``
Concerns:
-might be necessary to do this in the macosx directory for some reason,
though Aqua doesn't support 64 bits
-have to recompile python to get \_tkinter to work (see `a later post`_)

.. _a later post: http://buffalothedestroyer.blogspot.com/2009/07/success-64-bit-python-with-64-bit-tcltk.html
