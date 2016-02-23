A tclean vs clean comparison
############################
:date: 2016-02-22 11:23
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, ALMA


Comparing tclean to clean with the following parameters::

    clean(vis=vis0, imagename=myimagebase, field="", spw='',
          mode='mfs', outframe='LSRK', interpolation='linear',
          imagermode='mosaic', multiscale=multiscale, interactive=False,
          niter=1000, threshold='100mJy', imsize=imsize, minpb=0.5, cell=cell,
          phasecenter=phasecenter, weighting='briggs', usescratch=True,
          pbcor=True, robust=-2.0)

    tclean(vis=vis0, imagename=myimagebase, field="", spw='',
           outframe='LSRK', interpolation='linear', gridder='mosaic',
           scales=multiscale, interactive=False, niter=1000,
           threshold='100mJy', imsize=imsize, mask='auto-pb', specmode='mfs',
           cell=cell, phasecenter=phasecenter, weighting='briggs', robust=-2.0)


Note the very bad cleaning instability creeping in in the clean image:

.. image:: |filename|/images/tclean_vs_clean_7m12m.png
   :width: 600px
