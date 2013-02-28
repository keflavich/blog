Python 64 bit!
##############
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer

I got python 64 bit to compile, but it required a number of tricky
steps.
First, this guy has the instructions I followed:
`captnswing`_
However, it didn't work entirely as advertised. I ran the configure as
advertised:
``./configure --enable-framework=/Library/Frameworks \--enable-universalsdk=/ \MACOSX_DEPLOYMENT_TARGET=10.5 \--with-universal-archs=all \--with-readline-dir=/usr/local``
then the make install, but /usr/local/bin/python pointed to the wrong
place, so I replaced the symbolic link in my python path with the
correct one:
``sudo rm /Library/Frameworks/Python.framework/Versions/2.6/bin/python sudo ln -s /Library/Frameworks/Python.framework/Versions/2.6/bin/python-64 /Library/Frameworks/Python.framework/Versions/2.6/bin/python``
Now python is 64 bit:
``eta ~$ python -c "import sys; print sys.maxint"9223372036854775807``
I haven't checked whether it works yet though...
Update: Had to reinstall with gnu readline installed. Also have to
install PyQt4 and might have to recompile numpy...
numpy won't compile with python 2.6.2:
``C compiler: gcc -arch i386 -arch ppc -arch ppc64 -arch x86_64 -isysroot / -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypescompile options: '-Inumpy/core/include -Ibuild/src.macosx-10.5-universal-2.6/numpy/core/include/numpy -Inumpy/core/src -Inumpy/core/include -I/Library/Frameworks/Python.framework/Versions/2.6/include/python2.6 -c'gcc: build/src.macosx-10.5-universal-2.6/numpy/core/src/_sortmodule.cIn file included from numpy/core/include/numpy/ndarrayobject.h:26,                 from numpy/core/include/numpy/noprefix.h:7,                 from numpy/core/src/_sortmodule.c.src:29:numpy/core/include/numpy/npy_endian.h:33:10: error: #error Unknown CPU: can not set endiannesslipo: can't figure out the architecture type of: /var/folders/ni/ni+DtdqFGMeSMH13AvkNkU+++TI/-Tmp-//cceaWIvZ.outIn file included from numpy/core/include/numpy/ndarrayobject.h:26,                 from numpy/core/include/numpy/noprefix.h:7,                 from numpy/core/src/_sortmodule.c.src:29:numpy/core/include/numpy/npy_endian.h:33:10: error: #error Unknown CPU: can not set endiannesslipo: can't figure out the architecture type of: /var/folders/ni/ni+DtdqFGMeSMH13AvkNkU+++TI/-Tmp-//cceaWIvZ.outerror: Command "gcc -arch i386 -arch ppc -arch ppc64 -arch x86_64 -isysroot / -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Inumpy/core/include -Ibuild/src.macosx-10.5-universal-2.6/numpy/core/include/numpy -Inumpy/core/src -Inumpy/core/include -I/Library/Frameworks/Python.framework/Versions/2.6/include/python2.6 -c build/src.macosx-10.5-universal-2.6/numpy/core/src/_sortmodule.c -o build/temp.macosx-10.5-universal-2.6/build/src.macosx-10.5-universal-2.6/numpy/core/src/_sortmodule.o" failed with exit status 1``
That sucks.

.. _captnswing: http://blog.captnswing.net/2009/04/19/python-mod_wsgi-64bit-mac-os-x-105/
