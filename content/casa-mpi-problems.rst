CASA MPI problems
#################
:date: 2021-10-17 20:40 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: tags


There are several CASA MPI errors I encounter regularly.

.. code::

   2021-10-17 15:56:06     SEVERE  task_tclean::SynthesisImagerVi2::runCubeGridding (file src/code/synthesis/ImagerObjects/SynthesisImagerVi2.cc, line 1579)       remainder rank 7 failed
   master 1 init 1
   2021-10-17 15:59:21     SEVERE  tclean::::casa  Task tclean raised an exception of class RuntimeError with the following message: Error in making PSF : One or more  of the cube section failed in de/grid
   ding. Return values for the sections: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
   , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
   , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    Traceback (most recent call last):
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/site-packages/casashell/private/init_system.py", line 238, in __evprop__
        exec(stmt)
      File "<string>", line 1, in <module>
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/site-packages/casashell/private/init_system.py", line 175, in execfile
        newglob = run_path( filename, init_globals=globals )
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/runpy.py", line 263, in run_path
        pkg_name=pkg_name, script_name=fname)
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/runpy.py", line 96, in _run_module_code
        mod_name, mod_spec, pkg_name, script_name)
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/runpy.py", line 85, in _run_code
        exec(code, run_globals)
      File "/orange/adamginsburg/ALMA_IMF/reduction/reduction/line_imaging.py", line 935, in <module>
        **impars
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/site-packages/casatasks/tclean.py", line 1660, in __call__
        task_result = _tclean_t( _pc.document['vis'], _pc.document['selectdata'], _pc.document['field'], _pc.document['spw'], _pc.document['timerange'], _pc.document['uvrange'], _pc.document['antenna'], _pc.document['scan'], _pc.document['observation'], _pc.document['intent'], _pc.document['datacolumn'], _pc.document['imagename'], _pc.document['imsize'], _pc.document['cell'], _pc.document['phasecenter'], _pc.document['stokes'], _pc.document['projection'], _pc.document['startmodel'], _pc.document['specmode'], _pc.document['reffreq'], _pc.document['nchan'], _pc.document['start'], _pc.document['width'], _pc.document['outframe'], _pc.document['veltype'], _pc.document['restfreq'], _pc.document['interpolation'], _pc.document['perchanweightdensity'], _pc.document['gridder'], _pc.document['facets'], _pc.document['psfphasecenter'], _pc.document['wprojplanes'], _pc.document['vptable'], _pc.document['mosweight'], _pc.document['aterm'], _pc.document['psterm'], _pc.document['wbawp'], _pc.document['conjbeams'], _pc.document['cfcache'], _pc.document['usepointing'], _pc.document['computepastep'], _pc.document['rotatepastep'], _pc.document['pointingoffsetsigdev'], _pc.document['pblimit'], _pc.document['normtype'], _pc.document['deconvolver'], _pc.document['scales'], _pc.document['nterms'], _pc.document['smallscalebias'], _pc.document['restoration'], _pc.document['restoringbeam'], _pc.document['pbcor'], _pc.document['outlierfile'], _pc.document['weighting'], _pc.document['robust'], _pc.document['noise'], _pc.document['npixels'], _pc.document['uvtaper'], _pc.document['niter'], _pc.document['gain'], _pc.document['threshold'], _pc.document['nsigma'], _pc.document['cycleniter'], _pc.document['cyclefactor'], _pc.document['minpsffraction'], _pc.document['maxpsffraction'], _pc.document['interactive'], _pc.document['usemask'], _pc.document['mask'], _pc.document['pbmask'], _pc.document['sidelobethreshold'], _pc.document['noisethreshold'], _pc.document['lownoisethreshold'], _pc.document['negativethreshold'], _pc.document['smoothfactor'], _pc.document['minbeamfrac'], _pc.document['cutthreshold'], _pc.document['growiterations'], _pc.document['dogrowprune'], _pc.document['minpercentchange'], _pc.document['verbose'], _pc.document['fastnoise'], _pc.document['restart'], _pc.document['savemodel'], _pc.document['calcres'], _pc.document['calcpsf'], _pc.document['psfcutoff'], _pc.document['parallel'] )
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/site-packages/casatasks/private/task_tclean.py", line 364, in tclean
        imager.makePSF()
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/site-packages/casatasks/private/imagerhelpers/imager_base.py", line 344, in makePSF
        self.makePSFCore()
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/site-packages/casatasks/private/imagerhelpers/imager_base.py", line 496, in makePSFCore
        self.SItool.makepsf()
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/site-packages/casatools/synthesisimager.py", line 70, in makepsf
        return self._swigobj.makepsf()
      File "/blue/adamginsburg/adamginsburg/casa/casa-6.4.0-12/lib/py/lib/python3.6/site-packages/casatools/__casac__/synthesisimager.py", line 322, in makepsf
        return _synthesisimager.synthesisimager_makepsf(self)
    RuntimeError: Error in making PSF : One or more  of the cube section failed in de/gridding. Return values for the sections: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


That one appears to be caused by:

.. code::

    2021-10-17 15:53:34     WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-7 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line
     A) Exception for chan range [1921, 1924] ---   Error in making PSF : Interpolate1D::operator() data has repeated x values
    ##################################
    #############################
    Exception: Error in making PSF : Interpolate1D::operator() data has repeated x values


This happened after a lot of apparently successful cleaning, as an .image was created.  However, the failure caused
CASA to exit.


This tclean command:

.. code::

   2021-10-17 15:19:43     INFO    tclean::::casa  tclean( vis='/blue/adamginsburg/adamginsburg/almaimf/workdir/G008.67_B3_spw2_12M.concat.ms', selectdata=True, field='G008.67', spw='', timerange='', uvrange='', antenna='', scan='', observation='', intent='', datacolumn='corrected', imagename='/blue/adamginsburg/adamginsburg/almaimf/workdir/G008.67_B3_spw2_12M_spw2', imsize=[2880, 2250], cell=['0.08arcsec', '0.08arcsec'], phasecenter='ICRS 271.5877979623041deg -21.620789662367244deg', stokes='I', projection='SIN', startmodel='', specmode='cube', reffreq='', nchan=-1, start='', width='', outframe='LSRK', veltype='radio', restfreq=[], interpolation='linear', perchanweightdensity=True, gridder='mosaic', facets=1, psfphasecenter='', wprojplanes=1, vptable='', mosweight=True, aterm=True, psterm=False, wbawp=True, conjbeams=False, cfcache='', usepointing=False, computepastep=360.0, rotatepastep=360.0, pointingoffsetsigdev=[], pblimit=0.05, normtype='flatnoise', deconvolver='multiscale', scales=[0, 4, 8, 16, 32], nterms=2, smallscalebias=0.5, restoration=True, restoringbeam='', pbcor=False, outlierfile='', weighting='briggsbwtaper', robust=0.0, noise='1.0Jy', npixels=0, uvtaper=[''], niter=5000000, gain=0.1, threshold='0.0168Jy', nsigma=0.0, cycleniter=-1, cyclefactor=2.0, minpsffraction=0.05, maxpsffraction=0.8, interactive=0, usemask='user', mask='', pbmask=0.1, sidelobethreshold=3.0, noisethreshold=5.0, lownoisethreshold=1.5, negativethreshold=0.0, smoothfactor=1.0, minbeamfrac=0.3, cutthreshold=0.01, growiterations=75, dogrowprune=True, minpercentchange=-1.0, verbose=False, fastnoise=True, restart=True, savemodel='none', calcres=False, calcpsf=True, psfcutoff=0.35, parallel=True )

using concatenated data caused the failure.  It was run as an MPI job with 32 cores and 128 GB RAM.
The same issue recurred for the next MS (spw3), but not for spw0 or spw1 - yet, they're still running.


This: "Exception for chan range [1921, 1924] ---   Error in making PSF : Interpolate1D::operator() data has repeated x values" suggests to me that there's
a problem with the gridder thinking there are more channels than there actually are; ``tclean``'s behavior is not consistent between operating on concatenated
data sets and on lists of data sets.  This issue may be a manifestation of tclean misunderstanding the grid when operating with MPI enabled.
This could also prove not to be an MPI error, but one that is only encountered if MPI is enabled b/c MPI gets to channel 1921 while non-MPI never gets
there before the job is canceled for time.





W51 spw2 had similar:

.. code::

    WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-21 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336)        Exception for chan range [1269, 1277] ---   FilebufIO::readBlock - incorrect number of bytes read for file /blue/adamginsburg/adamginsburg/almaimf/workdir/W51-E_B3_spw2_12M_spw2.sumwt/table.f0
    Exception: FilebufIO::readBlock - incorrect number of bytes read for file /blue/adamginsburg/adamginsburg/almaimf/workdir/W51-E_B3_spw2_12M_spw2.sumwt/table.f0
    WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-9 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336) Exception for chan range [1314, 1322] ---   FilebufIO::readBlock - incorrect number of bytes read for file /blue/adamginsburg/adamginsburg/almaimf/workdir/W51-E_B3_spw2_12M_spw2.sumwt/table.f0
    Exception: FilebufIO::readBlock - incorrect number of bytes read for file /blue/adamginsburg/adamginsburg/almaimf/workdir/W51-E_B3_spw2_12M_spw2.sumwt/table.f0


I have not found solutions to any of these; the workaround appears to be just to not use MPI.


EDIT: here's another one


.. code::

    2021-10-22 22:36:53     WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-2 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336) Exception for chan range [55, 109] ---   Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw1_12M_sio.contcube.model/table.lock
    ##################################
    #############################
    Exception: Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw1_12M_sio.contcube.model/table.lock
    2021-10-22 22:36:54     WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-4 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336) Exception for chan range [165, 219] ---   Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw1_12M_sio.contcube.model/table.lock
    ##################################
    #############################
    Exception: Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw1_12M_sio.contcube.model/table.lock
    2021-10-22 22:36:57     WARN    MPICommandServer::command_request_handler_service::SynthesisImagerVi2::CubeMajorCycle::MPIServer-1 (file src/code/synthesis/ImagerObjects/CubeMajorCycleAlgorithm.cc, line 336) Exception for chan range [0, 54] ---   Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw1_12M_sio.contcube.model/table.lock
    ##################################
    #############################
    Exception: Setting masked pixels to zero for input startmodel : Error (Resource deadlock avoided) when acquiring lock on /blue/adamginsburg/adamginsburg/almaimf/workdir/G327.29_B6_spw1_12M_sio.contcube.model/table.lock
