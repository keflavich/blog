New to-do list, updated things....
##################################
:date: 2008-10-15 12:57
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, mapping, pipeline
:slug: new-to-do-list-updated-things

``do_maptests.pro`` is running a bunch of different mapping parameters
(pca components, deconvolution, etc.) on l000, l002, l003, l033, l083.
We'll then run bolocat on it and look for the following:
-number of sources found
-flux in sources found as a function of n\_pca
-size of sources as function of n\_pca
-BADNESS, e.g. blurring / unremoved atmosphere / oversubtracted sources
``bolocat2reg`` makes a region file out of a bolocat catalog. I'd like
to make a separate ds9 region file that includes the actual pointing
error + the centroiding error rather than just the elliptical fit to a
given source; that will be more useful for finder charts.
My current goal is to get a nice set of images I can combine to release
as a poster to Jason Glenn's student who is making pretty posters for
publicity purposes; probably to promote CCAT. Umm.... I blame the late
hour for the alliteration.
That goal also means I've been using an IRAF task to do some mosaicing
(easier than writing the IDL code AGAIN):
``mscstack l001_5pca_map09.fits,l002_5pca_map09.fits,l000_5pca_map09.fits,l359_5pca_map09.fits,l003_5pca_map09.fits  GCCOMBINE_5pca.fits lthresh=-1l001_13pca_map09_scuba_aligned.fits,l002_13pca_map09_scuba_aligned.fits,l000_13pca_map09_scuba_aligned.fits,l359_13pca_map09_scuba_aligned.fits,l003_13pca_map09_scuba_aligned.fits  GCCOMBINE.fits lthresh=-1mscstack l029_13pca_map09_scuba_aligned.fits,l030_13pca_map09_scuba_aligned.fits,l031_13pca_map09_scuba_aligned.fits,l032_13pca_map09_scuba_aligned.fits,l033_13pca_map09_scuba_aligned.fits,l034_13pca_map09_scuba_aligned.fits L33COMBINE.fits lthresh=-1 hsig=5 lsig=5``
