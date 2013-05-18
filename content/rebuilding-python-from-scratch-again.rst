Rebuilding python from scratch again
####################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, python, mac

I got scipy working a week or two ago, but doing so killed matplotib's
tkagg. So, I switched to the MacOSX backend, which worked ok until I
realized that the interactive (connect) features of macosx failed
miserably. This led me to try to get matplotlib working.... which broke
with those awful "symbol not found" errors in ft2font.so and \_path.so,
which I've determined all have to do with linking to the wrong library
files.
The most worrisome part of this process was discovering that a full Time
Machine recovery of /usr and /Library/Frameworks and /Library/Python did
\*not\* restore python - it stayed dead with IDENTICAL errors. So there
are probably additional layers of hidden links.
The process below is based on `hyperjeff's blog post`_ but differs
substantially based on `Sam Skillman's recommendations`_ and the very
big issue I ran into that my /usr/local files appeared to be corrupted.
After this install, my path no longer includes /usr/local/bin and /sw
has been moved to /\_sw... hopefully one of these days I'll be ballsy
enough to delete it.

#. Install python 2.6.4

   #. Needed a clean terminal with no flags set at all. Don't know why -
      all I had set were a bunch of -arch x86\_64 flags.
      ``export LD_LIBRARY_PATH="/usr/local/lib:/usr/X11/lib"./configure --enable-framework=/Library/Frameworks MACOSX_DEPLOYMENT_TARGET=10.6 make -j 17sudo make install``
   #. Reset PYTHONPATH to blank
   #. `` alias clearflags='export CFLAGS=""; export CCFLAGS=""; export CXXFLAGS=""; export LDFLAGS=""; export FFLAGS="";'``
      to make sure

#. Install FFTW
   ``cd ~/tmpcurl -O http://www.fftw.org/fftw-3.2.2.tar.gztar xf fftw-3.2.2.tar.gzcd fftw-3.2.2clearflags./configure CC="gcc -arch x86_64" CXX="g++ -arch x86_64" CPP="gcc -E" CXXCPP="g++ -E"make -j 17sudo make install``
#. Install UMFPACK
   ``cd ~/tmpcurl -O http://www.cise.ufl.edu/research/sparse/umfpack/current/UMFPACK.tar.gzcurl -O http://www.cise.ufl.edu/research/sparse/UFconfig/current/UFconfig.tar.gzcurl -O http://www.cise.ufl.edu/research/sparse/amd/current/AMD.tar.gztar xf AMD.tar.gztar xf UFconfig.tar.gztar xf UMFPACK.tar.gzsed -ibck 's/F77 = f77/F77 = gfortran/' UFconfig/UFconfig.mk sed -ibck '299,303s/# //' UFconfig/UFconfig.mkcp UFconfig/UFconfig.h AMD/Include/cp UFconfig/UFconfig.h UMFPACK/Include/cd UMFPACKmake -j 17make hbmake clean``
#. Install numpy

   #. Set environment variables
      ``export MACOSX_DEPLOYMENT_TARGET=10.6export CFLAGS="-arch x86_64"export FFLAGS="-m64"export LDFLAGS="-Wall -undefined dynamic_lookup -bundle -arch x86_64"export PYTHONPATH="/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/"echo "[amd]library_dirs = /Users/adam/tmp/AMD/Libinclude_dirs = /Users/adam/tmp/AMD/Includeamd_libs = amd[umfpack]library_dirs = /Users/adam/tmp/UMFPACK/Libinclude_dirs = /Users/adam/tmp/UMFPACK/Includeumfpack_libs = umfpack" > site.cfg``
   #. Setup & Install
      ``python setup.py build --fcompiler=gnu95sudo python setup.py install``
   #. Test: python -c "import numpy"

#. Install scipy. The important thing is to use g++-4.2 because g++-4.5
   doesn't accept the -arch flag. Also, get rid of /sw if it's on your
   computer at all.
   ``sudo mv /System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/numpy /System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/numpyXcd ~/repos/scipy-0.7.1python setup.py cleanrm -rf buildclearflagsFFLAGS="-m64" CFLAGS="-arch x86_64 -I/usr/local/include/freetype2 -I/usr/X11/include -L/usr/X11/lib"  LDFLAGS="-Wall -undefined dynamic_lookup -bundle  -lpng -arch x86_64" CXX="/usr/bin/g++-4.2" CC="/usr/bin/gcc-4.2" python setup.py buildpython setup.py install``
   Test the install:
   ``python -c "import scipy, scipy.fftpack, scipy.interpolate"``
#. 

   #. Install matplotlib. MAKE SURE /usr/bin/texbin is in front of
      /usr/local/bin and /sw/bin so that dvipng comes from MacTEX. I
      also ended up having to remove /usr/local/bin from my path
      completely
      ``sudo mv /System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/numpy /System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/numpyXcd ~/repos/matplotlib-svnpython setup.py cleanrm -rf buildclearflags``
   #. Do hyperjeff's recommended edits except don't use /usr/local
      because it's f'd:
      make.osx:
      ``MACOSX_DEPLOYMENT_TARGET=10.6PREFIX=/usrPYTHON=/Library/Frameworks/Python.framework/Versions/Current/bin/python## You shouldn't need to configure past this point (and yet…)PKG_CONFIG_PATH="${PREFIX}/lib/pkgconfig"CFLAGS="-arch i386 -arch x86_64 -I${PREFIX}/include -I${PREFIX}/include/freetype2 -isysroot /Developer/SDKs/MacOSX10.6.sdk"LDFLAGS="-arch i386 -arch x86_64 -L${PREFIX}/lib -syslibroot,/Developer/SDKs/MacOSX10.6.sdk"FFLAGS="-arch i386 -arch x86_64"``
      setup.cfg:
      ``wxagg = False``
   #. Do the install (different from hyperjeff b/c I don't want root)
      `` sudo make -f make.osx fetch deps make -f mpl_build mpl_installpython setup.py install``

#. Install setuptools
#. easy\_install ipython
#. install everything else pythonically

.. raw:: html

   </p>

.. _hyperjeff's blog post: http://blog.hyperjeff.net/?p=160
.. _Sam Skillman's recommendations: http://casa.colorado.edu/~skillman/research_and_codes/files/649710e82f85745eb65a90535f0f3098-5.html
