CASA synthetic observations
###########################
:date: 2016-08-15 09:36
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, simulation, synthetic observation

To evaluate imaging robustness & quality, it is necessary to do some sort of
synthetic observation.  These synthetic observations can be done on real
images, e.g. Herschel data shifted to greater distances, or on simulated data.

Some examples:

 * https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/master/analysis/synth_imaging_perseus.py
 * https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/master/analysis/synth_imaging_perseus_2.py
 * https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/master/analysis/synth_imaging_aquila.py


General process:

 1. Import file into CASA .image form (e.g., ``importfits``)
 2. Load the .ms file and replace visibilities w/fourier transform of image
 3. Clean.

The hard part is setting up the files to be imported.

For example, you can import a FITS file, which to me seems to be the most
straightforward approach::


    importfits(fitsimage=perseus_rescaled,
               imagename=perseus_casa_image,
               overwrite=True,
               defaultaxes=True,#['RA---TAN','DEC--TAN','FREQUENCY','STOKES'],
               defaultaxesvalues=['2.909234541667E+02deg',
                                  '1.451177222222E+01deg',
                                  '233.9468GHz','I'],
               # 18" = 1.22 lambda/D
               beam=["{0}deg".format(18/3600.*distance_scaling),
                     "{0}deg".format(18/3600.*distance_scaling),
                     "0deg"],
              )

The beam probably matters for Jy->K, or Jy/beam->Jy conversion.  The
``defaultaxesvalues`` should correspond to the pointing center of the
interferometer pointing or mosaic.

Next is bringing this image - which we now pray is in the correct units - into UV space.::

    sm.openfromms("continuum_7m12m_noflag.ms")
    sm.setvp()
    success = sm.predict(perseus_casa_image)
    assert success
    # TODO: get these from ASDM_CALWVR and WEATHER
    success2 = sm.setnoise(mode='tsys-atm', relhum=60.0, pwv='2mm', tatmos=265.0, )
    success3 = sm.corrupt()
    sm.done()
    sm.close()

This snippet loads the .ms file (the visibilities), then overwrites them with
the fourier transform of the image using ``sm.predict``.  It's not clear whether
``setvp`` is necessary.  ``setnoise`` + ``corrupt`` just adds "appropriate"
atmospheric noise to the visibilities.

From there, you should just use the same ``clean`` parameters as for the
original data, or try to optimize ``clean`` here and use these parameters on
the real data.

The result will be the 'perfect' (no phase error, no amplitude error)
interferometric image.
