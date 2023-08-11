Editing metadata in measurement sets
####################################
:date: 2023-08-11 15:34
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa



I needed to update the position of VLA phase calibrator `J1744-3116 <http://simbad.u-strasbg.fr/simbad/sim-id?Ident=%402384864&Name=QSO%20J1744-3116&submit=submit>`_ in my measurement sets.  The VLA coordinate is:

    ``17:33:02.705790 -13.04.49.54823 J2000``

while the ALMA coordinate is

    ``17:44:23.578227 -31.16.36.29204 ICRS``

and the SIMBAD coordinate is

    ``17 44 23.57824 -31 16 36.2943 ICRS``

These are separated by a significant amount:

.. code-block:: python

  from astropy import units as u, coordinates
  import numpy as np

  vla_coord = coordinates.SkyCoord("17:33:02.705790 -13:04:49.54823", unit=(u.h, u.deg), frame='fk5')
  alma_coord = coordinates.SkyCoord("17:44:23.578227 -31:16:36.29204", unit=(u.h, u.deg), frame='icrs')
  simbad_coord = coordinates.SkyCoord('17 44 23.57824 -31 16 36.2943', unit=(u.h, u.deg), frame='icrs')

  alma_coord.separation(vla_coord).to(u.arcsec)
  # <Angle 0.28848595 arcsec>

  simbad_coord.separation(vla_coord).to(u.arcsec)
  # <Angle 0.29071513 arcsec>

  simbad_coord.separation(alma_coord).to(u.arcsec)
  # <Angle 0.00226614 arcsec>


This is caused by a typo in the VLA calibrator catalog (Lorant Sjouwerman, private communication).

To fix it:

.. code-block:: python

  tb.open('22A-020.sb41257746.eb41788351.59700.31502699074/22A-020.sb41257746.eb41788351.59700.31502699074.ms/FIELD')

  # get the existing PHASE_DIR.  Shape is [coordinates, ?, sourceID]
  phasedir = tb.getcol('PHASE_DIR')
  # figure out which row contains the to-be-modified source
  rownr = np.argmax(tb.getcol('NAME') == 'J1744-3116')
  # modify the phasedir.  CASA expects coordinates to be wrapped at 180 deg
  phasedir[:, 0, rownr] = simbad_coord.fk5.ra.wrap_at(180*u.deg).rad, simbad_coord.fk5.dec.rad

  import shutil
  shutil.copytree('22A-020.sb41257746.eb41788351.59700.31502699074/22A-020.sb41257746.eb41788351.59700.31502699074.ms/FIELD', '22A-020.sb41257746.eb41788351.59700.31502699074/22A-020.sb41257746.eb41788351.59700.31502699074.ms/FIELD.backup')
  tb.open('22A-020.sb41257746.eb41788351.59700.31502699074/22A-020.sb41257746.eb41788351.59700.31502699074.ms/FIELD', nomodify=False)
  tb.putcol(columnname='PHASE_DIR', value=phasedir)
  tb.flush()
  tb.close()

Put all together:

.. code-block:: python

    from astropy import units as u, coordinates
    import numpy as np
  
    simbad_coord = coordinates.SkyCoord('17 44 23.57824 -31 16 36.2943', unit=(u.h, u.deg), frame='icrs')

    import glob, shutil
    for vis in glob.glob("*/*.ms"):
        shutil.copytree(vis+"/FIELD", vis+"/FIELD.backup")
        tb.open(vis+"/FIELD")
        phasedir = tb.getcol('PHASE_DIR')
        rownr = np.argmax(tb.getcol('NAME') == 'J1744-3116')
        assert rownr != 0
        phasedir[:, 0, rownr] = simbad_coord.fk5.ra.wrap_at(180*u.deg).rad, simbad_coord.fk5.dec.rad
        tb.open(vis+"/FIELD", nomodify=False)
        tb.putcol(columnname='PHASE_DIR', value=phasedir)
        tb.flush()
        tb.close()
    

