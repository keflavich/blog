CASA reading incorrect number of bytes w/MPI
############################################
:date: 2021-12-02 08:15 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa



Running big MPI runs again, I encounter errors like these one::

    2021-12-02 07:02:26      WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-25 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)        Exception for chan range [1434, 1445] ---   FilebufIO::readBlock - incorr
    ect number of bytes read for file /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw7_12M_spw7.sumwt/table.f0
    ##################################
    #############################
    Exception: FilebufIO::readBlock - incorrect number of bytes read for file /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw7_12M_spw7.sumwt/table.f0


    2021-12-02 06:03:53        WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-13 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)        Exception for chan range [550, 560] ---   FilebufIO::readBlock - incorrect number
     of bytes read for file /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw4_12M_spw4.sumwt/table.f0
    ##################################
    #############################
    Exception: FilebufIO::readBlock - incorrect number of bytes read for file /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw4_12M_spw4.sumwt/table.f0

    2021-12-02 04:57:21 WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-9 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336) Exception for chan range [1563, 1574] ---   FilebufIO::readBlock
    - incorrect number of bytes read for file /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw0_12M_spw0.sumwt/table.f0
    ##################################
    #############################
    Exception: FilebufIO::readBlock - incorrect number of bytes read for file /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw0_12M_spw0.sumwt/table.f0


This is only quasi-repeatable.  For spw4, it happened after the 8th Major Cycle
the first time, then the 6th Major Cycle the second time.  By repeating the
cleans over and over, I was able to eventually get the results to converge.
It looks like these crashes are sporadic but don't affect the data.
