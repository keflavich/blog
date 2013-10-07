Installing MultiNest on Mac OS X 10.7
=====================================
:date: 2013-10-06 15:25
:tag: install, stats, python

Installing multinest & pymultinest has proved non-trivial.

First, you probably can't build using the default mac gcc; a gcc version >4.5
is probably needed.  The error I got installing MultiNest only turned up one
useful result on google... it was a `question I had asked
<https://github.com/hyperion-rt/hyperion/issues/23>`_ on the `hyperion github
page <https://github.com/hyperion-rt>`_.

To get around that, I installed the `hpc compilers
<http://hpc.sourceforge.net/>`_ (4.7 since I'm on OS X 10.7) into
`/usr/local/hpc/` to keep them distinct from the system gcc, which is needed
for many other things.

I then installed the `openMPI compilers <http://www.open-mpi.org/>`_ to `/usr/local/openmpi`::

    ./configure --prefix=/usr/local/openmpi
    make
    sudo make install

Then I tried installing pymultinest

:: 


    dor ~/repos/MultiNest cmake/master$ mkdir build
    dor ~/repos/MultiNest cmake/master$ cd build/
    dor ~/repos/MultiNest/build cmake/master$ which mpif90
    /usr/local/openmpi/bin/mpif90
    dor ~/repos/MultiNest/build cmake/master$ which gfortran
    /usr/local/hpc/bin//gfortran
    dor ~/repos/MultiNest/build cmake/master$ which gcc
    /usr/local/hpc/bin//gcc
    dor ~/repos/MultiNest/build cmake/master$ cmake -DCMAKE_{C,CXX}_FLAGS="-arch x86_64" -DCMAKE_Fortran_FLAGS="-m64" ..
    -- The Fortran compiler identification is GNU
    -- The C compiler identification is GNU 4.7.1
    -- The CXX compiler identification is GNU 4.7.1
    -- Check for working Fortran compiler: /usr/local/hpc/bin/gfortran
    -- Check for working Fortran compiler: /usr/local/hpc/bin/gfortran  -- works
    -- Detecting Fortran compiler ABI info
    -- Detecting Fortran compiler ABI info - done
    -- Checking whether /usr/local/hpc/bin/gfortran supports Fortran 90
    -- Checking whether /usr/local/hpc/bin/gfortran supports Fortran 90 -- yes
    -- Checking whether C compiler has -isysroot
    -- Checking whether C compiler has -isysroot - yes
    -- Checking whether C compiler supports OSX deployment target flag
    -- Checking whether C compiler supports OSX deployment target flag - yes
    -- Check for working C compiler: /usr/local/hpc/bin/gcc
    -- Check for working C compiler: /usr/local/hpc/bin/gcc -- works
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Checking whether CXX compiler has -isysroot
    -- Checking whether CXX compiler has -isysroot - yes
    -- Checking whether CXX compiler supports OSX deployment target flag
    -- Checking whether CXX compiler supports OSX deployment target flag - yes
    -- Check for working CXX compiler: /usr/local/hpc/bin/g++
    -- Check for working CXX compiler: /usr/local/hpc/bin/g++ -- works
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Looking for Fortran dgemm
    -- Looking for Fortran dgemm - found
    -- Looking for include file pthread.h
    -- Looking for include file pthread.h - found
    -- Looking for pthread_create
    -- Looking for pthread_create - found
    -- Found Threads: TRUE
    -- A library with BLAS API found.
    -- Looking for Fortran cheev
    -- Looking for Fortran cheev - found
    -- A library with LAPACK API found.
    -- Detected gfortran, adding -ffree-line-length-none compiler option.
    -- Found MPI_C: /usr/local/openmpi/lib/libmpi.dylib;/usr/lib/libm.dylib
    -- Found MPI_CXX: /usr/local/openmpi/lib/libmpi_cxx.dylib;/usr/local/openmpi/lib/libmpi.dylib;/usr/lib/libm.dylib
    -- Found MPI_Fortran: /usr/local/openmpi/lib/libmpi_f90.a;/usr/local/openmpi/lib/libmpi_f77.dylib;/usr/local/openmpi/lib/libmpi.dylib;/usr/lib/libm.dylib
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /Users/adam/repos/MultiNest/build
    dor ~/repos/MultiNest/build cmake/master$ make
    Scanning dependencies of target multinest_mpi_shared
    [  1%] Building Fortran object src/CMakeFiles/multinest_mpi_shared.dir/utils.f90.o
    [  3%] Building Fortran object src/CMakeFiles/multinest_mpi_shared.dir/utils1.f90.o
    [  5%] Building Fortran object src/CMakeFiles/multinest_mpi_shared.dir/kmeans_clstr.f90.o
    [  6%] Building Fortran object src/CMakeFiles/multinest_mpi_shared.dir/xmeans_clstr.f90.o
    [  8%] Building Fortran object src/CMakeFiles/multinest_mpi_shared.dir/posterior.F90.o
    [ 10%] Building Fortran object src/CMakeFiles/multinest_mpi_shared.dir/priors.f90.o
    [ 12%] Building Fortran object src/CMakeFiles/multinest_mpi_shared.dir/nested.F90.o
    [ 13%] Building Fortran object src/CMakeFiles/multinest_mpi_shared.dir/cwrapper.f90.o
    Linking Fortran shared library ../../lib/libmultinest_mpi.dylib
    [ 13%] Built target multinest_mpi_shared
    Scanning dependencies of target multinest_mpi_static
    [ 15%] Building Fortran object src/CMakeFiles/multinest_mpi_static.dir/utils.f90.o
    [ 17%] Building Fortran object src/CMakeFiles/multinest_mpi_static.dir/utils1.f90.o
    [ 18%] Building Fortran object src/CMakeFiles/multinest_mpi_static.dir/kmeans_clstr.f90.o
    [ 20%] Building Fortran object src/CMakeFiles/multinest_mpi_static.dir/xmeans_clstr.f90.o
    [ 22%] Building Fortran object src/CMakeFiles/multinest_mpi_static.dir/posterior.F90.o
    [ 24%] Building Fortran object src/CMakeFiles/multinest_mpi_static.dir/priors.f90.o
    [ 25%] Building Fortran object src/CMakeFiles/multinest_mpi_static.dir/nested.F90.o
    [ 27%] Building Fortran object src/CMakeFiles/multinest_mpi_static.dir/cwrapper.f90.o
    Linking Fortran static library ../../lib/libmultinest_mpi.a
    [ 27%] Built target multinest_mpi_static
    Scanning dependencies of target multinest_shared
    [ 29%] Building Fortran object src/CMakeFiles/multinest_shared.dir/utils.f90.o
    [ 31%] Building Fortran object src/CMakeFiles/multinest_shared.dir/utils1.f90.o
    [ 32%] Building Fortran object src/CMakeFiles/multinest_shared.dir/kmeans_clstr.f90.o
    [ 34%] Building Fortran object src/CMakeFiles/multinest_shared.dir/xmeans_clstr.f90.o
    [ 36%] Building Fortran object src/CMakeFiles/multinest_shared.dir/posterior.F90.o
    [ 37%] Building Fortran object src/CMakeFiles/multinest_shared.dir/priors.f90.o
    [ 39%] Building Fortran object src/CMakeFiles/multinest_shared.dir/nested.F90.o
    [ 41%] Building Fortran object src/CMakeFiles/multinest_shared.dir/cwrapper.f90.o
    Linking Fortran shared library ../../lib/libmultinest.dylib
    [ 41%] Built target multinest_shared
    Scanning dependencies of target multinest_static
    [ 43%] Building Fortran object src/CMakeFiles/multinest_static.dir/utils.f90.o
    [ 44%] Building Fortran object src/CMakeFiles/multinest_static.dir/utils1.f90.o
    [ 46%] Building Fortran object src/CMakeFiles/multinest_static.dir/kmeans_clstr.f90.o
    [ 48%] Building Fortran object src/CMakeFiles/multinest_static.dir/xmeans_clstr.f90.o
    [ 50%] Building Fortran object src/CMakeFiles/multinest_static.dir/posterior.F90.o
    [ 51%] Building Fortran object src/CMakeFiles/multinest_static.dir/priors.f90.o
    [ 53%] Building Fortran object src/CMakeFiles/multinest_static.dir/nested.F90.o
    [ 55%] Building Fortran object src/CMakeFiles/multinest_static.dir/cwrapper.f90.o
    Linking Fortran static library ../../lib/libmultinest.a
    Error copying file "/Users/adam/repos/MultiNest/build/src/kmeans_clstr.mod" to "/Users/adam/repos/MultiNest/modules/".
    make[2]: *** [../lib/libmultinest.a] Error 1
    make[1]: *** [src/CMakeFiles/multinest_static.dir/all] Error 2
    make: *** [all] Error 2
    
The approach that worked::

    mkdir -p build lib modules bin/chains
    cd build
    cmake -DCMAKE_{C,CXX}_FLAGS="-arch x86_64" -DCMAKE_Fortran_FLAGS="-m64" ..
    make
    sudo make install
    cd ../lib
    ln -s libmultinest.dylib libmultinest.so
    export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/usr/local/hpc/lib:/usr/local/openmpi/lib/
    export LD_LIBRARY_PATH=/Users/adam/repos/MultiNest/lib

At this point, multinest imports but doesn't run the tests...
