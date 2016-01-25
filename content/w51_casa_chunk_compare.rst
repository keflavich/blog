CASA imaging of huge cube
#########################
:date: 2016-01-25 10:09
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, imaging, cubes

Imaging full cubes, i.e. every channel and every pixel, from ALMA data proved
too much for the first few machines I tried it on, so I then tried splitting
the cubes into chunks (`source
<https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/master/script_12m/scriptForImaging_fullcube.py>`_).

For the most part, this works well, but there are some serious problems:

.. image:: |filename|/images/casa/spectrum_with_badchunk.png
   :width: 600px

Note the range from 233.8-234 GHz.  It has a continuum level way above the
rest.  This is utter nonsense, and turns out to be due to some imaging error.
The first image below shows a "good" chunk of the cube, the second image shows
a "bad" chunk.

.. image:: |filename|/images/casa/w51_cube_chunk_compare_good.png
   :width: 600px

.. image:: |filename|/images/casa/w51_cube_chunk_compare_bad.png
   :width: 600px

It is clear that the second image was restore using a too-large beam, and this is verified by examining the header:

.. code-block:: python

    In [8]: badcube.beam
    Out[8]: Beam: BMAJ=1.15963029861 arcsec BMIN=0.96223282814 arcsec BPA=-71.0310058594 deg
    
    In [9]: goodcube.beam
    Out[9]: Beam: BMAJ=0.408393889665 arcsec BMIN=0.229679107666 arcsec BPA=45.966835022 deg



I don't yet know what is causing this error.  When I try re-doing the clean
with ``tclean``, I get the following message, which is a hint:

::

    2016-01-25 09:13:04     WARN    task_tclean::SIImageStore::getPSFGaussian (file
    /var/rpmbuild/BUILD/casa-prerelease/casa-prerelease-4.5.0/code/synthesis/ImagerObjects/SIImageStore.cc,
    line 1262)      PSF is blank for[C139:P0] [C140:P0] [C141:P0] [C142:P0]
    [C143:P0] [C144:P0] [C145:P0] [C146:P0] [C147:P0] [C148:P0] [C149:P0] [C150:P0]
    [C151:P0] [C152:P0] [C153:P0] [C154:P0] [C155:P0] [C156:P0] [C157:P0] [C158:P0]
    [C159:P0] [C160:P0] [C161:P0] [C162:P0] [C163:P0] [C164:P0] [C165:P0] [C166:P0]
    [C167:P0] [C168:P0] [C169:P0] [C170:P0] [C171:P0] [C172:P0] [C173:P0] [C174:P0]
    [C175:P0] [C176:P0] [C177:P0] [C178:P0] [C179:P0] [C180:P0] [C181:P0] [C182:P0]
    [C183:P0] [C184:P0] [C185:P0] [C186:P0]
    

Apparently tclean solves this problem!  Instead of using a single beam for all
channels, it creates a CASAMBM table in the FITS output and uses different
beams at each channel.  There must be genuinely bad data (probably an
atmospheric absorption line) at the specified frequencies.  At least now, that
will come up more naturally, rather than spiking the data.  
