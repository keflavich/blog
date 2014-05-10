Python stack on Mavericks
=========================
:date: 2014-02-19 12:02
:author: napattack (adam.g.ginsburg@gmail.com)
:tags: mac, install, python, scipy, fortran


As you might expect from numerous blog posts and the general difficulty people
have always experienced upgrading mac OS versions, Mavericks caused some truly
hideous issues.

The only really "new" issues specifically for Mavericks relate to app nap.  The
main solution is minrk's appnope_.  Otherwise, command line options like
`defaults write <app domain name> NSAppSleepDisabled -bool YES` are required
`if the button is missing`_ from Mac's Get Info pane.

I tried installing the conda_ stack to get python running quickly.  This
worked to an extremely limited degree: the TkAgg shipped with anaconda links to
`XQuartz`_, which is highly undesirable for a number of reasons.  This meant
that matplotlib plots showed up as X11 plots.  With the Mac OS X backend, the
windows failed to show up in the Dock and therefore were totally unusable (though
they did look OK).

I am still using conda_ to maintain multiple parallel versions of python for
testing.  However, I went back to my typical install-from-source approach.

To get the matplotlib backends to interact nicely with apple, you need to install
them using the `/Library` version of python

.. code-block:: bash

    # this had to happen sometime early:
    $ xcode-select --install

    $ wget https://pypi.python.org/pypi/pip#downloads
    $ tar -xzvf ~/Downloads/pip-1.5.2.tar.gz 
    $ cd pip-1.5.2
    $ /Library/Frameworks/Python.framework/Versions/2.7/bin/python setup.py install
    $ /Library/Frameworks/Python.framework/Versions/2.7/bin/pip install virtualenv
    $ cd 
    $ /Library/Frameworks/Python.framework/Versions/2.7/bin/virtualenv virtual-python

After this, I was surprisingly able to install everything in the python stack
with no hitches.  Obviously, that could not possibly last. 

While matplotlib and numpy worked fine, scipy had problems.

::

    ImportError: dlopen(/Users/adam/virtual-python/lib/python2.7/site-packages/scipy/integrate/_odepack.so, 2): Symbol not found: __gfortran_internal_free
    Referenced from: /Users/adam/virtual-python/lib/python2.7/site-packages/scipy/integrate/_odepack.so
    Expected in: flat namespace
       in /Users/adam/virtual-python/lib/python2.7/site-packages/scipy/integrate/_odepack.so

This terrible error led me back to re-compiling scipy.  I tried installing with
hpc_ gfortran, but that didn't work at all, first apparently because of linking
errors in numpy.  When I investigated numpy, I found that the compilers
apparently don't work at all:

:: 

    C compiler: /usr/local/bin/gcc -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -arch i386 -arch x86_64
    ...
    RuntimeError: Broken toolchain: cannot link a simple C program


I had to give up on that, and then googling returned no results at all, which I
thought was a bit weird.  Scipy seems to want gcc and g++ 4.2, even though
they're years old.  I had to find those and gfortran-4.2 somehow, but the `old
site`_ that used to serve them seems to have lost the files!  They had an
`older version`_, though, which appears to work.  Scipy is a scary install.

Problems with XQuartz
---------------------

XQuartz is not well-behaved on Mac OS X 10.9.  First, `on retina machines, it
does not display well`_.  Second, and much more important, it `does not work on
external monitors`_.  Apparently this can be worked around by turning off
"Displays have different spaces"  in Mission Control, but so far that has had
no effect for me.


.. _if the button is missing: http://apple.stackexchange.com/questions/121386/missing-prevent-app-nap-button-on-app
.. _appnope: https://github.com/minrk/appnope
.. _conda: https://store.continuum.io/cshop/anaconda/
.. _XQuartz: xquartz.macosforge.org
.. _hpc: hpc.sourceforge.net
.. _old site: r.research.att.com/tools/
.. _older version: http://r.research.att.com/tools/gcc-42-5666.3-darwin11.pkg
.. _on retina machines, it does not display well: https://xquartz.macosforge.org/trac/ticket/661
.. _does not work on external monitors: http://xquartz.macosforge.org/trac/ticket/797
