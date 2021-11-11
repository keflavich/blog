CASA table locking with MPI
###########################
:date: 2021-11-11 15:53 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa

A bunch of CASA MPI runs have race conditioned themselves into a corner, apparently:       

.. code-block:: python

    2021-11-07 23:33:10     WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-5 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336) Exception for chan range [104, 129] ---   Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.contcube.model/table.lock
    ##################################
    #############################
    Exception: Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.contcube.model/table.lock
    2021-11-07 23:33:10     WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-10 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)        Exception for chan range [234, 258] ---   Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.contcube.model/table.lock
    ##################################
    #############################
    Exception: Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.contcube.model/table.lock
    2021-11-07 23:33:10     WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-9 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336) Exception for chan range [208, 233] ---   Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.contcube.model/table.lock
    ##################################
    #############################
    Exception: Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.contcube.model/table.lock
    2021-11-07 23:33:10     WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-2 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336) Exception for chan range [26, 51] ---   Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.contcube.model/table.lock
    ##################################
    #############################
    Exception: Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.contcube.model/table.lock
    2021-11-07 23:33:10     WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-15 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)        Exception for chan range [359, 383] ---   Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.contcube.model/table.lock
    ##################################
    #############################
    Exception: Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.contcube.model/table.lock


This shows up in ~10 runs that I started around the same time, but I don't usually see it.

This looks like a serious bug having to do with using a startmodel: there is a line earlier copying the startmodel to the model::

    2021-11-07 23:27:44     INFO    SIImageStore::setModelImageOne  Copying input model /blue/adamginsburg/adamginsburg/almaimf/workdir//G351.77_B6_spw1_12M_sio.contcube.model to /blue/adamginsburg/adamginsburg/almaimf/workdir/G351.77_B6_spw1_12M_sio.model

but MPI seems to have gotten mixed up and is sill trying to write to the contcube.model
