Python 64-bit on Mac OS X 10.6 Snow Leopard
###########################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, python


After `yesterday's disastrous attempt`_ to install various python
packages, I started from scratch. First, I got rid of all of my python
frameworks (backed up but removed from the path). Then, I compiled
python 2.7 from scratch:

I got some help from
`http://blog.mahmoudimus.com/2009/12/python-2-6-4-and-twisted-9-on-os-x-10-6-snow-leopard/`_
``./configure --enable-framework --enable-universalsdk=/Developer/SDKs/MacOSX10.6.sdk MACOSX_DEPLOYMENT_TARGET=10.6 --with-universal-archs=intel -with-readline-dir=/usr/localmake -j 17make -j 17 test``
``make`` results:

::

    Python build finished, but the necessary bits to build these modules were
    not found:
        _bsddb
        dl
        gdbm
        imageop
        linuxaudiodev
        ossaudiodev
        spwd
        sunaudiodev
    To find the necessary bits, look in setup.py in detect_modules() for the
    module's name.

I'm not concerned about these - I don't use any of them and I assume I
need to install some other packages to get them to work.
During make test, I had two failures that resulted in "python crash"
pop-up boxes:

::

    test_subprocess.    
    this bit of output is from a test of stdout in a different process ....    
    this bit of output is from a test of stdout in a different process ...
    test_sunaudiodev

Then, I got some malloc errors:

::

    test_ioTesting large file ops skipped on darwin.It requires 2147483648
    bytes and a long time.Use 'regrtest.py -u largefile test_io' to run
    it.Testing large file ops skipped on darwin.It requires 2147483648 bytes
    and a long time.Use 'regrtest.py -u largefile test_io' to run
    it.python.exe(22914,0x7fff70d3ebe0) malloc: ***
    mmap(size=9223372036854775808) failed (error code=12)*** error: can't
    allocate region*** set a breakpoint in malloc_error_break to
    debugpython.exe(22914,0x7fff70d3ebe0) malloc: ***
    mmap(size=9223372036854775808) failed (error code=12)*** error: can't
    allocate region*** set a breakpoint in malloc_error_break to
    debugpython.exe(22914,0x7fff70d3ebe0) malloc: ***
    mmap(size=9223372036854775808) failed (error code=12)*** error: can't
    allocate region*** set a breakpoint in malloc_error_break to
    debugtest_ioctl


.. _yesterday's disastrous attempt: http://buffalothedestroyer.blogspot.com/2010/02/installing-snow-leopard.html
.. _`http://blog.mahmoudimus.com/2009/12/python-2-6-4-and-twisted-9-on-os-x-10-6-snow-leopard/`: http://blog.mahmoudimus.com/2009/12/python-2-6-4-and-twisted-9-on-os-x-10-6-snow-leopard/
