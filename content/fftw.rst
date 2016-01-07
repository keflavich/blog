FFT comparisons in python
#########################
:date: 2015-12-07 11:24
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: fft, convolution

I'm trying to figure out which ffts are fastest, best, etc.

First, it is difficult to get fftw3 + pyfftw installed into python.

For pyfftw to install, you need to `enable floats and every specific type
<http://www.fftw.org/doc/Installation-on-Unix.html>`_ when compiling `fftw3
<http://www.fftw.org/>`_ (thanks to `linux toolkits blog
<http://linuxtoolkit.blogspot.de/2010/04/cant-find-fftw3f-library-when.html>`_).
Apparently you can't have ``--enable-long-double`` and ``--enable-float`` simultaneously,
but pyfftw requires both, so you have to install twice or thrice?  Nope, four
times!!  Also, `my own post
<https://github.com/hgomersall/pyFFTW/issues/16#issuecomment-19422752>`_
indicates that I should install to a different path to avoid weird conflicts
with other libraries.
::

    ./configure --enable-threads --enable-openmp --enable-mpi --enable-shared \
                --enable-fortran --enable-avx \
                CFLAGS="-O3 -fno-common -fomit-frame-pointer -fstrict-aliasing"
    make -j 4
    sudo make install

    ./configure --enable-float --enable-threads --enable-openmp --enable-mpi --enable-shared \
                --enable-fortran --enable-avx \
                CFLAGS="-O3 -fno-common -fomit-frame-pointer -fstrict-aliasing"
    make -j 4
    sudo make install

    # quad precision is not supported in mpi
    ./configure --enable-quad-precision --enable-threads --enable-openmp --enable-shared \
                --enable-fortran --enable-avx \
                 CFLAGS="-O3 -fno-common -fomit-frame-pointer -fstrict-aliasing"
    make -j 4
    sudo make install

    ./configure --enable-long-double --enable-threads --enable-openmp --enable-mpi --enable-shared \
                --enable-fortran --enable-avx \
                 CFLAGS="-O3 -fno-common -fomit-frame-pointer -fstrict-aliasing"
    make -j 4
    sudo make install


Onto speed test comparisons:

 * `Marshal Perrin's <https://gist.github.com/mperrin/5763120>`_
 * `my fork <https://gist.github.com/keflavich/5797994>`_
 * `speed tests on agpy <http://code.google.com/p/agpy/source/browse/trunk/tests/test_ffts.py>`_
 * `profiling convolve_fft with different parameters <https://github.com/astropy/astropy/pull/4374>`_

If you want to use ``fftw3`` with astropy's `convolve_fft
<http://docs.astropy.org/en/stable/api/astropy.convolution.convolve_fft.html#astropy.convolution.convolve_fft>`_,
use `this example
<https://code.google.com/p/agpy/source/browse/trunk/AG_fft_tools/convolve_nd.py?r=479#8>`_.


Onto some comparisons from `astropy issue 4374 <https://github.com/astropy/astropy/pull/4374>`_:

.. image:: |filename|/images/time_vs_mem.png
   :width: 600px

.. image:: |filename|/images/psfTfftT.png
   :width: 600px

.. image:: |filename|/images/psfTfftF.png
   :width: 600px

.. image:: |filename|/images/psfFfftT.png
   :width: 600px

.. image:: |filename|/images/psfFfftF.png
   :width: 600px


`Notebook containing comparisons between FFT and FFTW <https://gist.github.com/6a2d338830efdc02959a>`_
