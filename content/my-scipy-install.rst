my scipy install...
###################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, python

As far as I was able to reconstruct, my scipy install looked like this
when it went well:
``mkdir scipy-bincp ../scipy-svn/site.cfg .export PATH=/Users/adam/repos/scipy.git/scipy-bin:$PATHln -s /usr/bin/g++-4.0 scipy-bin/g++-4.0ln -s /usr/bin/g++-4.0 scipy-bin/c++export CC=/usr/bin/gcc-4.0 ln -s /usr/bin/gcc-4.0 scipy-bin/ln -s /usr/bin/gcc-4.0 scipy-bin/gccln -s /usr/local/bin/gfortran-4.0 scipy-bin/gfortran-4.0ln -s /usr/local/bin/gfortran-4.0 scipy-bin/gfortranln -s /usr/local/bin/g95 scipy-bin/g95ln -s /usr/local/bin/i686-apple-darwin8-gfortran-4.2 scipy-bin/python2.7 setup.py buildpython2.7 setup.py install``
However, site.cfg included pointers to AMD and UMFPACK that were
installed via the incredibly complicated series of steps listed here:
`http://blog.hyperjeff.net/?p=160`_
`AG`_

.. _`http://blog.hyperjeff.net/?p=160`: http://blog.hyperjeff.net/?p=160
.. _AG: http://casa.colorado.edu/~ginsbura/index.htm
