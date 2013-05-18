Installing Snow Leopard
#######################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, mac, computer

I'm going to attempt to install snow leopard today. This post will serve
as a record of the difficulties I run into.
Things to install (and ensure they are 64-bit):

-  ipython
-  numpy
-  scipy
-  matplotlib
-  stsci-python
-  starlink
-  gfortran
-  latex
-  idl (check)

Things that have happened:

#. Had to restart again (twice) to install additional updates
#. My bash command line looked funny - something about bash changed, but
   I don't know what. The fix was easy: commented out some code from
   `http://pseudogreen.org/blog/set\_tab\_names\_in\_leopard\_terminal.html`_
   that I had been using to set the tab title
#. My locate db broke. Needed repair: ``sudo /usr/libexec/locate.updatedb``
#. numpy svn failed to build:
   `` python setup.py buildRunning from numpy source directory.non-existing path in 'numpy/distutils': 'site.cfg'F2PY Version 2_8111numpy/core/setup_common.py:86: MismatchCAPIWarning: API mismatch detected, the C API version numbers have to be updated. Current C api version is 4, with checksum 59750b518272c8987f02d66445afd3f1, but recorded checksum for C API version 4 in codegen_dir/cversions.txt is 3d8940bf7b0d2a4e25be4338c14c3c85. If functions were added in the C API, you have to update C_API_VERSION  in numpy/core/setup_common.pyc.  MismatchCAPIWarning)blas_opt_info:  FOUND:    extra_link_args = ['-Wl,-framework', '-Wl,Accelerate']    define_macros = [('NO_ATLAS_INFO', 3)]    extra_compile_args = ['-faltivec', '-I/System/Library/Frameworks/vecLib.framework/Headers']lapack_opt_info:  FOUND:    extra_link_args = ['-Wl,-framework', '-Wl,Accelerate']    define_macros = [('NO_ATLAS_INFO', 3)]    extra_compile_args = ['-faltivec']running buildrunning config_ccunifing config_cc, config, build_clib, build_ext, build commands --compiler optionsrunning config_fcunifing config_fc, config, build_clib, build_ext, build commands --fcompiler optionsrunning build_srcbuild_srcbuilding py_modules sourcesbuilding library "npymath" sourcescustomize NAGFCompilerFound executable /usr/local/bin/f95customize AbsoftFCompilerCould not locate executable f90Found executable /usr/bin/f77absoft: no Fortran 90 compiler foundabsoft: no Fortran 90 compiler foundcustomize IBMFCompilerCould not locate executable xlf90Could not locate executable xlfcustomize IntelFCompilerCould not locate executable ifortCould not locate executable ifccustomize GnuFCompilerFound executable /usr/local/bin/g77gnu: no Fortran 90 compiler foundgnu: no Fortran 90 compiler foundcustomize Gnu95FCompilerFound executable /usr/local/bin/gfortrancustomize Gnu95FCompilercustomize Gnu95FCompiler using configC compiler: gcc -arch i386 -arch ppc -arch ppc64 -arch x86_64 -isysroot /Developer/SDKs/MacOSX10.5.sdk -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypescompile options: '-Inumpy/core/src/private -Inumpy/core/src -Inumpy/core -Inumpy/core/src/npymath -Inumpy/core/src/multiarray -Inumpy/core/src/umath -Inumpy/core/include -I/Library/Frameworks/Python.framework/Versions/2.6/include/python2.6 -c'gcc: _configtest.cgcc _configtest.o -o _configtestld: library not found for -lcrt1.10.5.ocollect2: ld returned 1 exit statusld: library not found for -lcrt1.10.5.ocollect2: ld returned 1 exit statusfailure.removing: _configtest.c _configtest.oTraceback (most recent call last):  File "setup.py", line 210, in     setup_package()  File "setup.py", line 203, in setup_package    configuration=configuration )  File "/Users/adam/repos/numpy-svn/numpy/distutils/core.py", line 186, in setup    return old_setup(**new_attr)  File "/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/distutils/core.py", line 152, in setup    dist.run_commands()  File "/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/distutils/dist.py", line 975, in run_commands    self.run_command(cmd)  File "/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/distutils/dist.py", line 995, in run_command    cmd_obj.run()  File "/Users/adam/repos/numpy-svn/numpy/distutils/command/build.py", line 37, in run    old_build.run(self)  File "/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/distutils/command/build.py", line 134, in run    self.run_command(cmd_name)  File "/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/distutils/cmd.py", line 333, in run_command    self.distribution.run_command(command)  File "/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/distutils/dist.py", line 995, in run_command    cmd_obj.run()  File "/Users/adam/repos/numpy-svn/numpy/distutils/command/build_src.py", line 152, in run    self.build_sources()  File "/Users/adam/repos/numpy-svn/numpy/distutils/command/build_src.py", line 163, in build_sources    self.build_library_sources(*libname_info)  File "/Users/adam/repos/numpy-svn/numpy/distutils/command/build_src.py", line 298, in build_library_sources    sources = self.generate_sources(sources, (lib_name, build_info))  File "/Users/adam/repos/numpy-svn/numpy/distutils/command/build_src.py", line 385, in generate_sources    source = func(extension, build_dir)  File "numpy/core/setup.py", line 670, in get_mathlib_info    raise RuntimeError("Broken toolchain: cannot link a simple C program")RuntimeError: Broken toolchain: cannot link a simple C program``
   **SOLUTION:** Use the Mac OS X 10.6 python (/usr/bin/python). I will do this
   until I run into another problem. Numpy build successfully
#. Build/install matplotlib - failed! Completely!
#. Acquired gcc/gfortran from `hpc`_
#. Followed instructions from `hyperjeff`_ on fortran install...
#. Get rid of numpy 1.2.1:
   `` mv /System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/numpy /System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/.not_numpy.bak``
#. Try to install scipy. Fail on missing umfpack, follow `hyperjeff`_'s
   instructions (but make sure to edit the site.cfg in scipy, not just the one in
   numpy). 
   Had to add the following code:
   ``sudo cp AMD/Lib/libamd.a /System/Library/Frameworks/Python.framework/Versions/2.6/libsudo cp UMFPACK/Lib/libumfpack.a /System/Library/Frameworks/Python.framework/Versions/2.6/libsudo cp AMD/Include/amd.h /System/Library/Frameworks/Python.framework/Versions/2.6/includesudo cp UFconfig/UFconfig.h /System/Library/Frameworks/Python.framework/Versions/2.6/includesudo cp UMFPACK/Include/*.h /System/Library/Frameworks/Python.framework/Versions/2.6/include``
#. Installed fftw from `fftw.org`_ with simple ./configure, make, sudo
   make install - no compiler opts as they killed the install
#. Get SoundSource from `rogueamoeba`_
#. Updated `istatmenus`_


.. _`http://pseudogreen.org/blog/set\_tab\_names\_in\_leopard\_terminal.html`: http://pseudogreen.org/blog/set_tab_names_in_leopard_terminal.html
.. _hpc: http://hpc.sourceforge.net/
.. _hyperjeff: http://blog.hyperjeff.net/?p=160
.. _fftw.org: http://www.fftw.org/
.. _rogueamoeba: http://www.rogueamoeba.com/freebies/
.. _istatmenus: http://www.islayer.com/apps/istatmenus/
