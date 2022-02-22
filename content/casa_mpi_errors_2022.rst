CASA MPI Errors continued in early 2022
#######################################
:date: 2022-01-23 07:54 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA


Running 7m+12m combination, the following errors show up:


.. code::
    Exception: Error in making PSF : Invalid Table operation: Rows cannot be removed from table /blue/adamginsburg/adamginsburg/almaimf/workdir/G333.60_spw5_12M_B6/IMAGING_WEIGHT_1390794_230801956263_230804885819_bwtaper_0_interp_1; its storage managers do not support it

This turns up several times repeatedly:

.. code::
    G333.60_B6_fullcube_7M12M_5_15827045.log:2022-01-21 18:05:38  WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-25 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)      Exception for chan range [496, 499] ---   Error in making PSF : Interpolate1D::operator() data has repeated x values
    G333.60_B6_fullcube_7M12M_5_15868985.log:2022-01-22 00:01:20  WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-19 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)      Exception for chan range [496, 499] ---   Error in making PSF : Invalid Table operation: Rows cannot be removed from table /blue/adamginsburg/adamginsburg/almaimf/workdir/G333.60_spw5_12M_B6/IMAGING_WEIGHT_1390794_230801956263_230804885819_bwtaper_0_interp_1; its storage managers do not support it
    G333.60_B6_fullcube_7M12M_5_15891690.log:2022-01-22 14:37:39  WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-23 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)      Exception for chan range [496, 499] ---   Error in making PSF : Invalid Table operation: Rows cannot be removed from table /blue/adamginsburg/adamginsburg/almaimf/workdir/G333.60_spw5_12M_B6/IMAGING_WEIGHT_1390794_230801956263_230804885819_bwtaper_0_interp_1; its storage managers do not support it
    G333.60_B6_fullcube_7M12M_5_15914880.log:2022-01-23 02:21:24  WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-25 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)      Exception for chan range [496, 499] ---   Error in making PSF : Invalid Table operation: Rows cannot be removed from table /blue/adamginsburg/adamginsburg/almaimf/workdir/G333.60_spw5_12M_B6/IMAGING_WEIGHT_1390794_230801956263_230804885819_bwtaper_0_interp_1; its storage managers do not support it

Looks like it's always the same few channels failing.



Errors like this one:

.. code:: 
    WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-17 (file src/
    code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)        Exception for chan range [1152, 1153] ---   Programmer error: sumwt disk image is non existant

are probably cauased by deleting the .sumwt file in the middle of a tclean run
- so that is genuine "user error" (I was deleting the sumwt, psf, and weight
  files occasionally b/c they are the 'leftovers' when a tclean run fails for
  bad reasons)


There are some others that don't have obvious explanations:

.. code::
    casa_log_line_G010.62_B3_fullcube_7M12M_1_2022-01-21_08_17_16.log:2022-01-21 15:29:42   WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-15 (file src/ code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)        Exception for chan range [534, 535] ---   FilebufIO::readBlock - incorrect number of bytes read for file /blue/adamginsburg/adamgins burg/almaimf/workdir/G010.62_B3_spw1_7M12M_spw1.sumwt/table.f0
    casa_log_line_G010.62_B3_fullcube_7M12M_1_2022-01-21_08_17_16.log:2022-01-21 17:07:41   WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-31 (file src/ code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)        Exception for chan range [1596, 1597] ---   FilebufIO::readBlock - incorrect number of bytes read for file /blue/adamginsburg/adamgi nsburg/almaimf/workdir/G010.62_B3_spw1_7M12M_spw1.sumwt/table.f0

and this:

.. code::
    casa_log_line_G333.60_B6_fullcube_7M12M_5_2022-01-21_08_17_16.log:2022-01-21 18:05:38   WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-25 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)        Exception for chan range [496, 499] ---   Error in making PSF : Interpolate1D::operator() data has repeated x values


    
This is an old one that remains unsolved:

.. code::
   casa_log_line_G338.93_B3_fullcube_7M12M_1_2022-01-22_20_25_52.log:2022-01-23 04:59:57   WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-8 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336) Exception for chan range [2049, 2049] ---   Error in making PSF : A nasty Visbuffer2 error occured...wait


Got this real nice one after the .image was created:

.. code::
    *** Error in `/blue/adamginsburg/adamginsburg/casa/casa-6.4.3-4/lib/py/bin/python3': malloc(): smallbin double linked list corrupted: 0x00002af7a40d8000 ***
    ======= Backtrace: =========
    /lib64/libc.so.6(+0x7f804)[0x2af73aa03804]
    /lib64/libc.so.6(+0x82f40)[0x2af73aa06f40]
    /lib64/libc.so.6(__libc_malloc+0x4c)[0x2af73aa09b1c]
    /apps/compilers/gcc/9.3.0/lib64/libstdc++.so.6(_Znwm+0x15)[0x2af751076395]

That happened in the middle of major cycle 1, so the data were probably fine, but I'm just going to restart it
