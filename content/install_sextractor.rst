Installing sextractor on a mac?
####################################
:date: 2013-02-27 18:02
:author: Adam (keflavich@gmail.com)

Attempting to install sextractor.

First, tried following these instructions:

http://henrysmac.org/blog/2012/8/17/install-sextractor-on-os-x-lion.html


Then found out that mac's tar doesn't work properly (see this note: http://math-atlas.sourceforge.net/atlas_install/node60.html)


Fixed that with:

.. code-block:: bash

    wget ftp://gnu.mirror.iweb.com/gnu/tar/tar-latest.tar.gz
    cd ~/repos/
    tar -xzvf ~/Downloads/tar-latest.tar.gz # ironically
    cd tar-1.26/
    ./configure
    make
    make install # fails
    sudo make install
    hash -r


OK, try the instructions again:

.. code-block:: bash

    # first command may not work... visit that link if so
    wget https://sourceforge.net/projects/math-atlas/files/latest/download?source=files
    mkdir ~/repos/ATLAS3.10
    cd ~/repos/ATLAS3.10
    tar -xf ~/Downloads/atlas3.10.1.tar -C ./ --strip-components 1
    mkdir build/
    cd build/
    ../configure -b 64 --shared --prefix=/usr/local/lib/atlas --with-netlib-lapack-tarfile=/Users/adam/Downloads/lapack-3.4.2.tar 
    make build


Died with errors::

    ar r /Users/adam/repos/ATLAS3.10/build/lib/libatlas.a ATL_dMBJBmm.o ATL_dIBNBmm.o ATL_dIBJBmm.o ATL_dgemm.o ATL_dGetNB.o ATL_dGetNCNB.o ATL_dgemmNN.o ATL_dgemmNT.o ATL_dgemmTN.o ATL_dgemmTT.o ATL_dNCmmIJK.o ATL_dNCmmJIK.o ATL_dNCmmIJK_c.o ATL_dNCmmJIK_c.o ATL_daliased_gemm.o ATL_dAgemmNN.o ATL_dAgemmNT.o ATL_dAgemmTN.o ATL_dAgemmTT.o ATL_dmmJIK.o ATL_dmmIJK.o ATL_dmmJKI.o ATL_dmmK.o ATL_dmmBPP.o ATL_dmmJITcp.o ATL_dcol2blk_aX.o ATL_drow2blkT_aX.o ATL_dcol2blk_a1.o ATL_drow2blkT_a1.o ATL_dputblk_bX.o ATL_dputblk_b1.o ATL_dputblk_bn1.o ATL_dputblk_b0.o
    ar: fatal error in /usr/bin/ranlib
    make[4]: *** [dlib.grd] Error 1
    make[3]: *** [dlib] Error 2
    make[2]: *** [IBuildPtlibs] Error 2
       DONE  STAGE 4-2-1 at 23:09


       BEGIN STAGE 4-3-0: LAPACK TUNING at 23:09


          BEGIN STAGE 4-3-1: dLAPACK TUNING at 23:09
    make -f Makefile IBuildPtlibs 2>&1 | ./xatlas_tee INSTALL_LOG/LIBPTBUILD.LOG
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_dGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip tuning" ; \
            else \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_dGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_dGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_dGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip tuning
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_dtGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip threaded tuning" ; \
            elif [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_pthreads.h" ]; then \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_dtGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_dtGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_dtGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip threaded tuning
          DONE  STAGE 4-3-1 at 23:09


          BEGIN STAGE 4-3-2: sLAPACK TUNING at 23:09
    make -f Makefile ILATune pre=d 2>&1 | ./xatlas_tee INSTALL_LOG/dLATUNE.LOG
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_sGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip tuning" ; \
            else \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_sGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_sGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_sGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip tuning
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_stGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip threaded tuning" ; \
            elif [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_pthreads.h" ]; then \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_stGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_stGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_stGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip threaded tuning
          DONE  STAGE 4-3-2 at 23:09


          BEGIN STAGE 4-3-3: zLAPACK TUNING at 23:09
    make -f Makefile ILATune pre=s 2>&1 | ./xatlas_tee INSTALL_LOG/sLATUNE.LOG
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_zGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip tuning" ; \
            else \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_zGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_zGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_zGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip tuning
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_ztGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip threaded tuning" ; \
            elif [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_pthreads.h" ]; then \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_ztGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_ztGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_ztGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip threaded tuning
          DONE  STAGE 4-3-3 at 23:09


          BEGIN STAGE 4-3-4: cLAPACK TUNING at 23:09
    make -f Makefile ILATune pre=z 2>&1 | ./xatlas_tee INSTALL_LOG/zLATUNE.LOG
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_cGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip tuning" ; \
            else \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_cGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_cGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_cGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip tuning
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_ctGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip threaded tuning" ; \
            elif [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_pthreads.h" ]; then \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_ctGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_ctGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_ctGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip threaded tuning
          DONE  STAGE 4-3-4 at 23:09
       DONE  STAGE 4-3-0 at 23:09
    DONE  STAGE 4-0-0 at 23:09


    BEGIN STAGE 5-0-0: FINAL LIBRARY UPDATE at 23:09


       BEGIN STAGE 5-1-0: FINAL STATIC LIBRARY UPDATE at 23:09
    make -f Makefile IBuildLibs IBuildPtlibs0 2>&1 | ./xatlas_tee INSTALL_LOG/LIBUPDATE.LOG
    cd /Users/adam/repos/ATLAS3.10/build/src/auxil ; make lib
    make[3]: Nothing to be done for `lib'.
    cd /Users/adam/repos/ATLAS3.10/build/src/blas/gemm ; make lib
    make auxillib dcleanuplib dusergemm
    cd /Users/adam/repos/ATLAS3.10/build/src/auxil ; make lib
    make[5]: Nothing to be done for `lib'.
    cd KERNEL ; make -f dMakefile dlib
    make[5]: Nothing to be done for `dlib'.
    make[4]: Nothing to be done for `dusergemm'.
    make -j 4 dlib.grd
    ar r /Users/adam/repos/ATLAS3.10/build/lib/libatlas.a ATL_dMBJBmm.o ATL_dIBNBmm.o ATL_dIBJBmm.o ATL_dgemm.o ATL_dGetNB.o ATL_dGetNCNB.o ATL_dgemmNN.o ATL_dgemmNT.o ATL_dgemmTN.o ATL_dgemmTT.o ATL_dNCmmIJK.o ATL_dNCmmJIK.o ATL_dNCmmIJK_c.o ATL_dNCmmJIK_c.o ATL_daliased_gemm.o ATL_dAgemmNN.o ATL_dAgemmNT.o ATL_dAgemmTN.o ATL_dAgemmTT.o ATL_dmmJIK.o ATL_dmmIJK.o ATL_dmmJKI.o ATL_dmmK.o ATL_dmmBPP.o ATL_dmmJITcp.o ATL_dcol2blk_aX.o ATL_drow2blkT_aX.o ATL_dcol2blk_a1.o ATL_drow2blkT_a1.o ATL_dputblk_bX.o ATL_dputblk_b1.o ATL_dputblk_bn1.o ATL_dputblk_b0.o
    ar: fatal error in /usr/bin/ranlib
    make[4]: *** [dlib.grd] Error 1
    make[3]: *** [dlib] Error 2
    make[2]: *** [IBuildLibs] Error 2
       DONE  STAGE 5-1-0 at 23:09


       BEGIN STAGE 5-2-0: DYNAMIC/SHARED LIBRARY UPDATE at 23:09
    make -f Makefile IBuildDyLibs 2>&1 | ./xatlas_tee INSTALL_LOG/LIBDYBUILD.LOG
    cd /Users/adam/repos/ATLAS3.10/build ; make dylibs
    cd lib ; make shared_all
    make dylib
    rm -rf RCW_tMp ; mkdir RCW_tMp
    cd RCW_tMp ; ar x ../liblapack.a 
    ar: ../liblapack.a: No such file or directory
    make[5]: *** [dylib] Error 1
    make[4]: *** [shared_all] Error 2
    make[3]: *** [dylibs] Error 2
    make[2]: *** [IBuildDyLibs] Error 2
       DONE  STAGE 5-2-0 at 23:09




    ATLAS install complete.  Examine 
    ATLAS/bin/<arch>/INSTALL_LOG/SUMMARY.LOG for details.
    make clean
    rm -rf *.dSYM
    rm -f *.o x* config?.out *core*



    make check 

    Died with errors:

    ar r /Users/adam/repos/ATLAS3.10/build/lib/libatlas.a ATL_sMBJBmm.o ATL_sIBNBmm.o ATL_sIBJBmm.o ATL_sgemm.o ATL_sGetNB.o ATL_sGetNCNB.o ATL_sgemmNN.o ATL_sgemmNT.o ATL_sgemmTN.o ATL_sgemmTT.o ATL_sNCmmIJK.o ATL_sNCmmJIK.o ATL_sNCmmIJK_c.o ATL_sNCmmJIK_c.o ATL_saliased_gemm.o ATL_sAgemmNN.o ATL_sAgemmNT.o ATL_sAgemmTN.o ATL_sAgemmTT.o ATL_smmJIK.o ATL_smmIJK.o ATL_smmJKI.o ATL_smmK.o ATL_smmBPP.o ATL_smmJITcp.o ATL_scol2blk_aX.o ATL_srow2blkT_aX.o ATL_scol2blk_a1.o ATL_srow2blkT_a1.o ATL_sputblk_bX.o ATL_sputblk_b1.o ATL_sputblk_bn1.o ATL_sputblk_b0.o
    ranlib /Users/adam/repos/ATLAS3.10/build/lib/libatlas.a
    touch slib.grd
    cd /Users/adam/repos/ATLAS3.10/build/src/blas/level3 ; make slib
    ( cd kernel; make slib )
    make -j 4 slib.grd
    make[6]: `slib.grd' is up to date.
    make sl3ref
    cd /Users/adam/repos/ATLAS3.10/build/src/blas/reference/level3 ; make slib
    make[7]: Nothing to be done for `slib'.
    ( cd rblas;  make slib )
    make[5]: Nothing to be done for `slib'.
    cd ../pklevel3 ; make slib
    cd gpmm ; make slib
    make -j 4 slib.grd
    make[7]: `slib.grd' is up to date.
    cd sprk ; make slib
    make -j 4 slib.grd
    make[7]: `slib.grd' is up to date.
    make -j 4 sblas3.grd
    ar r /Users/adam/repos/ATLAS3.10/build/lib/libatlas.a ATL_ssymm.o ATL_ssyr2k.o ATL_ssyrk.o ATL_strmm.o ATL_strsm.o
    ar: fatal error in /usr/bin/ranlib
    make[5]: *** [sblas3.grd] Error 1
    make[4]: *** [sblas3] Error 2
    make[3]: *** [sl3lib] Error 2
    make[2]: *** [sanity_test] Error 2
    make[1]: *** [sanity_test] Error 2
    make: *** [test] Error 2



Gave up after discovering this is an unsolved (and probably intrinsically unsolveable) problem:
http://fink.9193.n7.nabble.com/Atlas-STAGE-2-3-2-CacheEdge-DETECTION-error-td26004.html



maybe try this:
http://okomestudio.net/biboroku/?p=824

nope, same thing


Tried switching from gcc-4.6 to gcc-4.2 (the latter should have been the default anyway).
Even when I renamed gcc-4.6 to dontuse_gcc-4.6, specified CC=/usr/bin/gcc, still found gcc-4.6! 

So I moved /usr/local/bin/gcc-4.6 to /usr/local/bin/dontuse/.gcc-4.6
Ridiculous.


Then tried what the site actually said, and used the hpc binaries::

    wget http://prdownloads.sourceforge.net/hpc/gfortran-lion.tar.gz?download
    wget http://prdownloads.sourceforge.net/hpc/gcc-lion.tar.gz?download
    mkdir ~/repos/hpc
    tar -xzf ~/Downloads/gcc-lion.tar.gz -C ~/repos/hpc/ --strip-components 2
    tar -xzf ~/Downloads/gfortran-lion.tar.gz -C ~/repos/hpc/ --strip-components 2

    CC=/Users/adam/repos/hpc/bin/gcc PATH=/Users/adam/repos/hpc/bin:$PATH ../configure -b 64 --shared --prefix=/usr/local/lib/atlas --with-netlib-lapack-tarfile=/Users/adam/Downloads/lapack-3.4.2.tar 


    ar r /Users/adam/repos/ATLAS3.10/build/lib/libatlas.a ATL_dMBJBmm.o ATL_dIBNBmm.o ATL_dIBJBmm.o ATL_dgemm.o ATL_dGetNB.o ATL_dGetNCNB.o ATL_dgemmNN.o ATL_dgemmNT.o ATL_dgemmTN.o ATL_dgemmTT.o ATL_dNCmmIJK.o ATL_dNCmmJIK.o ATL_dNCmmIJK_c.o ATL_dNCmmJIK_c.o ATL_daliased_gemm.o ATL_dAgemmNN.o ATL_dAgemmNT.o ATL_dAgemmTN.o ATL_dAgemmTT.o ATL_dmmJIK.o ATL_dmmIJK.o ATL_dmmJKI.o ATL_dmmK.o ATL_dmmBPP.o ATL_dmmJITcp.o ATL_dcol2blk_aX.o ATL_drow2blkT_aX.o ATL_dcol2blk_a1.o ATL_drow2blkT_a1.o ATL_dputblk_bX.o ATL_dputblk_b1.o ATL_dputblk_bn1.o ATL_dputblk_b0.o
    ar: fatal error in /usr/bin/ranlib
    make[4]: *** [dlib.grd] Error 1
    make[3]: *** [dlib] Error 2
    make[2]: *** [IBuildPtlibs] Error 2
       DONE  STAGE 4-2-1 at 18:09


       BEGIN STAGE 4-3-0: LAPACK TUNING at 18:09


          BEGIN STAGE 4-3-1: dLAPACK TUNING at 18:09
    make -f Makefile IBuildPtlibs 2>&1 | ./xatlas_tee INSTALL_LOG/LIBPTBUILD.LOG
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_dGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip tuning" ; \
            else \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_dGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_dGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_dGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip tuning
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_dtGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip threaded tuning" ; \
            elif [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_pthreads.h" ]; then \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_dtGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_dtGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_dtGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip threaded tuning
          DONE  STAGE 4-3-1 at 18:09


          BEGIN STAGE 4-3-2: sLAPACK TUNING at 18:09
    make -f Makefile ILATune pre=d 2>&1 | ./xatlas_tee INSTALL_LOG/dLATUNE.LOG
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_sGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip tuning" ; \
            else \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_sGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_sGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_sGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip tuning
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_stGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip threaded tuning" ; \
            elif [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_pthreads.h" ]; then \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_stGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_stGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_stGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip threaded tuning
          DONE  STAGE 4-3-2 at 18:09


          BEGIN STAGE 4-3-3: zLAPACK TUNING at 18:09
    make -f Makefile ILATune pre=s 2>&1 | ./xatlas_tee INSTALL_LOG/sLATUNE.LOG
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_zGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip tuning" ; \
            else \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_zGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_zGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_zGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip tuning
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_ztGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip threaded tuning" ; \
            elif [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_pthreads.h" ]; then \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_ztGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_ztGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_ztGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip threaded tuning
          DONE  STAGE 4-3-3 at 18:09


          BEGIN STAGE 4-3-4: cLAPACK TUNING at 18:09
    make -f Makefile ILATune pre=z 2>&1 | ./xatlas_tee INSTALL_LOG/zLATUNE.LOG
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_cGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip tuning" ; \
            else \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_cGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_cGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_cGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip tuning
    if [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_ctGetNB_geqrf.h" ]; then \
               echo "Arch Defaults allow us to skip threaded tuning" ; \
            elif [ -s "/Users/adam/repos/ATLAS3.10/build/include/atlas_pthreads.h" ]; then \
            cd /Users/adam/repos/ATLAS3.10/build/tune/lapack ; make res/ATL_ctGetNB_geqrf.h ; \
            cp /Users/adam/repos/ATLAS3.10/build/tune/lapack/res/ATL_ctGetNB_geqrf.h \
                   /Users/adam/repos/ATLAS3.10/build/include/atlas_ctGetNB_geqrf.h ; \
            fi
    Arch Defaults allow us to skip threaded tuning
          DONE  STAGE 4-3-4 at 18:09
       DONE  STAGE 4-3-0 at 18:09
    DONE  STAGE 4-0-0 at 18:09


    BEGIN STAGE 5-0-0: FINAL LIBRARY UPDATE at 18:09


       BEGIN STAGE 5-1-0: FINAL STATIC LIBRARY UPDATE at 18:09
    make -f Makefile IBuildLibs IBuildPtlibs0 2>&1 | ./xatlas_tee INSTALL_LOG/LIBUPDATE.LOG
    cd /Users/adam/repos/ATLAS3.10/build/src/auxil ; make lib
    make[3]: Nothing to be done for `lib'.
    cd /Users/adam/repos/ATLAS3.10/build/src/blas/gemm ; make lib
    make auxillib dcleanuplib dusergemm
    cd /Users/adam/repos/ATLAS3.10/build/src/auxil ; make lib
    make[5]: Nothing to be done for `lib'.
    cd KERNEL ; make -f dMakefile dlib
    make[5]: Nothing to be done for `dlib'.
    make[4]: Nothing to be done for `dusergemm'.
    make -j 4 dlib.grd
    ar r /Users/adam/repos/ATLAS3.10/build/lib/libatlas.a ATL_dMBJBmm.o ATL_dIBNBmm.o ATL_dIBJBmm.o ATL_dgemm.o ATL_dGetNB.o ATL_dGetNCNB.o ATL_dgemmNN.o ATL_dgemmNT.o ATL_dgemmTN.o ATL_dgemmTT.o ATL_dNCmmIJK.o ATL_dNCmmJIK.o ATL_dNCmmIJK_c.o ATL_dNCmmJIK_c.o ATL_daliased_gemm.o ATL_dAgemmNN.o ATL_dAgemmNT.o ATL_dAgemmTN.o ATL_dAgemmTT.o ATL_dmmJIK.o ATL_dmmIJK.o ATL_dmmJKI.o ATL_dmmK.o ATL_dmmBPP.o ATL_dmmJITcp.o ATL_dcol2blk_aX.o ATL_drow2blkT_aX.o ATL_dcol2blk_a1.o ATL_drow2blkT_a1.o ATL_dputblk_bX.o ATL_dputblk_b1.o ATL_dputblk_bn1.o ATL_dputblk_b0.o
    ar: fatal error in /usr/bin/ranlib
    make[4]: *** [dlib.grd] Error 1
    make[3]: *** [dlib] Error 2
    make[2]: *** [IBuildLibs] Error 2
       DONE  STAGE 5-1-0 at 18:09


       BEGIN STAGE 5-2-0: DYNAMIC/SHARED LIBRARY UPDATE at 18:09
    make -f Makefile IBuildDyLibs 2>&1 | ./xatlas_tee INSTALL_LOG/LIBDYBUILD.LOG
    cd /Users/adam/repos/ATLAS3.10/build ; make dylibs
    cd lib ; make shared_all
    make dylib
    rm -rf RCW_tMp ; mkdir RCW_tMp
    cd RCW_tMp ; ar x ../liblapack.a 
    ar: ../liblapack.a: No such file or directory
    make[5]: *** [dylib] Error 1
    make[4]: *** [shared_all] Error 2
    make[3]: *** [dylibs] Error 2
    make[2]: *** [IBuildDyLibs] Error 2
       DONE  STAGE 5-2-0 at 18:09




    ATLAS install complete.  Examine 
    ATLAS/bin/<arch>/INSTALL_LOG/SUMMARY.LOG for details.
    make clean
    rm -rf *.dSYM
    rm -f *.o x* config?.out *core*


This is the next step, if I ever get there::

    wget http://www.astromatic.net/download/sextractor/sextractor-2.8.6.tar.gz
    tar -xzvf ~/Downloads/sextractor-2.8.6.tar.gz 
