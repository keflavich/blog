CASA MPI debugging cont'd
#########################
:date: 2022-05-06 09:08
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA

I continue to try to get MPI to run to completion.


Using casa-6.5.0-9-py3.8, the latest error on the W51 B3 mosaic (biggest in ALMA-IMF, approximately):
2022-05-03 06:36:06     SEVERE  MPICommandServer::command_request_handler_service::CubeMajorCycleAlgorithm::task::MPIServer-2 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 137)      Exception (std): ArrayBase::validateConformance shape [3] differs from [4]

This leads to a lot of frozen nodes:
2022-05-03 19:29:17     SEVERE  MPIMonitorClient::monitor_status_service::MPIMonitorClient::monitor_status_service::casa        Ping status response from server 1 not received in the last 420s. Setting its status to 'timeout'

This happens during the MakePSF stage.


On G333.60 B6, which is smaller, the first exception I see is:
2022-05-05 17:31:47     SEVERE  MPIMonitorClient::monitor_status_service::MPIMonitorClient::monitor_status_service::casa        Ping status response from server 4 not received in the last 85s. Setting its status to 'timeout'
but... it looks like the clean actually finished!


This is an odd one that happened during a major cycle, I think:

2022-05-13 17:47:25     WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-19 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)        Exception for chan range [144, 151] ---   Setting masked pixels to zero for input startmodel : Er
ror (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G328.25_B6_spw4_12M_spw4.contcube.model/table.lock


This one resulted in the residual and image being identical past some point in the spectrum, i.e., it gave up partway through writing to disk.  There was NO CASA error!  Just a miserable segfault

[c0711a-s25:60411] *** Process received signal ***
[c0711a-s25:60411] Signal: Segmentation fault (11)
[c0711a-s25:60411] Signal code: Address not mapped (1)
[c0711a-s25:60411] Failing at address: 0x2d867e04f000


