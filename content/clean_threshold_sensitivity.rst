CLEAN has extreme sensitivity to the threshold
##############################################
:date: 2016-03-10 10:12
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, clean


CLEAN diverges sometimes.  The point at which divergence begins is very
difficult to identify and unfortunately it looks like the images get mostly
better as you slowly approach the toxic threshold:

.. image:: |filename|/images/w51/tclean_threshold_sensitivity.png
   :width: 600px


The precise clean command used, with only threshold changing, is::

    2016-03-10 07:49:28     INFO    tclean::::      tclean(vis="w51_contvis_selfcal_4.ms",selectdata=True,field="",spw="",timerange="",
    2016-03-10 07:49:28     INFO    tclean::::+             uvrange="",antenna="",scan="",observation="",intent="",
    2016-03-10 07:49:28     INFO    tclean::::+             datacolumn="corrected",imagename="selfcal_allspw_selfcal_4ampphase_mfs_tclean_deeper_4mJy",imsize=[3072, 3072],cell="0.05arcsec",phasecenter="J2000 19:23:41.629000 +14.30.42.38000",
    2016-03-10 07:49:28     INFO    tclean::::+             stokes="I",projection="SIN",startmodel="",specmode="mfs",reffreq="",
    2016-03-10 07:49:28     INFO    tclean::::+             nchan=-1,start="",width="",outframe="LSRK",veltype="radio",
    2016-03-10 07:49:28     INFO    tclean::::+             restfreq=[],interpolation="linear",gridder="mosaic",facets=1,wprojplanes=1,
    2016-03-10 07:49:28     INFO    tclean::::+             aterm=True,psterm=False,wbawp=True,conjbeams=True,cfcache="",
    2016-03-10 07:49:28     INFO    tclean::::+             computepastep=360.0,rotatepastep=360.0,pblimit=0.4,normtype="flatnoise",deconvolver="clark",
    2016-03-10 07:49:28     INFO    tclean::::+             scales=[],nterms=2,restoringbeam=[],outlierfile="",weighting="briggs",
    2016-03-10 07:49:28     INFO    tclean::::+             robust=-2.0,npixels=0,uvtaper=[],niter=100000,gain=0.1,
    2016-03-10 07:49:28     INFO    tclean::::+             threshold="4mJy",cycleniter=-1,cyclefactor=1.0,minpsffraction=0.05,maxpsffraction=0.8,
    2016-03-10 07:49:28     INFO    tclean::::+             interactive=False,mask="",overwrite=True,savemodel="modelcolumn",calcres=True,
    2016-03-10 07:49:28     INFO    tclean::::+             calcpsf=True,parallel=False)


It looks like CLEAN needs a different type of threshold to finish on, perhaps
something requiring each subsequent component to be some value less than the
previous component.  If each component is forced to be less than the previous
one, the clean can never diverge, though clean would stop unexpectedly if
subtracting a component increased the amplitude of some other part of the map
(i.e., if the next brightest source is sitting in a negative bowl).  Still,
this might be a rarer occurrence than the divergence that I see all the time,
which may be related to gridding (given the sharp grid pattern seen in panel 4
of the linked image).
