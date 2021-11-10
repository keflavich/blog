CASA doesn't like VaryingResolutionSpectralCubes
################################################
:date: 2021-11-09 19:53 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa, bug


I get this from trying to run ``makemask``:


.. code-block::

    makemask(mode='copy',
            inpimage=lineimagename+".image",
            inpmask=lineimagename+".image:mask0",
            output=lineimagename+".mask")

    2021-11-09 02:27:10     INFO    makemask::::casa        ##########################################
    2021-11-09 02:27:10     INFO    makemask::::casa        ##### Begin Task: makemask           #####
    2021-11-09 02:27:10     INFO    makemask::::casa        makemask( mode='copy', inpimage='/blue/adamginsburg/adamginsburg/almaimf/workdir/G353.41_B6_spw5_12M_spw5.image', inpmask='/blue/adamginsburg/adamginsburg/almaimf/workdir/G353.41_B6_spw5_12M_spw5.image:mask0', output='/blue/adamginsburg/adamginsburg/almaimf/workdir/G353.41_B6_spw5_12M_spw5.mask', overwrite=False, inpfreqs=[], outfreqs=[] )
    2021-11-09 02:27:11     INFO    makemask::ImageFactory::createImage     Created Paged image '__tmp_outputmask_22199' of shape [1080, 900, 1, 480] with float valued pixels.
    2021-11-09 02:27:11     INFO    makemask::::casa        Summing all T/F mask in inpmask and normalized to 1 for mask
    2021-11-09 02:27:51     SEVERE  image::regrid   Exception Reported: Exception: An image with multiple beams cannot be regridded along the spectral axis. You may wish to convolve all channels to a common resolution and retry.
    2021-11-09 02:27:51     SEVERE  image::regrid+  ... thrown by std::shared_ptr<casa6core::ImageInterface<T> > casa::ImageRegridder<T>::regrid() const [with T = float] at File: src/code/imageanalysis/ImageAnalysis/ImageRegridder.tcc, line: 102
    2021-11-09 02:27:52     INFO            deleted table /blue/adamginsburg/adamginsburg/almaimf/workdir/G353.41_spw5_12M_B6/_tmp_copy___tmp_frominmask_22199
    2021-11-09 02:27:56     SEVERE  image::calc (file src/tools/image/image_cmpt.cc, line 553)      Exception Reported: ImageExprParse: '__tmp_fromTFmask_22199' is an unknown lattice or image or it is an unqualified region
    2021-11-09 02:27:56     SEVERE  image::calc (file src/tools/image/image_cmpt.cc, line 553)+     Scanned so far: iif ("__tmp_fromTFmask_22199"
    2021-11-09 02:27:56     SEVERE  makemask::::casa        Task makemask raised an exception of class RuntimeError with the following message: *** Error (2), in mode copy: *** ImageExprParse: '__tmp_fromTFmask_22199' is an unknown lattice or image or it is an unqualified region
    2021-11-09 02:27:56     SEVERE  makemask::::casa+       Scanned so far: iif ("__tmp_fromTFmask_22199"
    2021-11-09 02:27:56     INFO    makemask::::casa        Task makemask complete. Start time: 2021-11-08 21:27:09.614534 End time: 2021-11-08 21:27:56.399654
    2021-11-09 02:27:56     INFO    makemask::::casa        ##### End Task: makemask             #####
    2021-11-09 02:27:56     INFO    makemask::::casa        ##########################################


   2021-11-09 02:27:51     SEVERE  image::regrid   Exception Reported: Exception: An image with multiple beams cannot be regridded along the spectral axis. You may wish to convolve all channels to a common
    resolution and retry.
   2021-11-09 02:27:51     SEVERE  image::regrid+  ... thrown by std::shared_ptr<casa6core::ImageInterface<T> > casa::ImageRegridder<T>::regrid() const [with T = float] at File: src/code/imageanalysis/Imag
   eAnalysis/ImageRegridder.tcc, line: 102
   2021-11-09 02:27:56     SEVERE  image::calc (file src/tools/image/image_cmpt.cc, line 553)      Exception Reported: ImageExprParse: '__tmp_fromTFmask_22199' is an unknown lattice or image or it is an un
   qualified region
   2021-11-09 02:27:56     SEVERE  image::calc (file src/tools/image/image_cmpt.cc, line 553)+     Scanned so far: iif ("__tmp_fromTFmask_22199"
   2021-11-09 02:27:56     SEVERE  makemask::::casa        Task makemask raised an exception of class RuntimeError with the following message: *** Error (2), in mode copy: *** ImageExprParse: '__tmp_fromTF
   mask_22199' is an unknown lattice or image or it is an unqualified region
   2021-11-09 02:27:56     SEVERE  makemask::::casa+       Scanned so far: iif ("__tmp_fromTFmask_22199"


I'm pretty sure the complaint is caused by the top line: there are multiple
beams in the image.  This is _absurd_, though, because the `makemask` command
should not care at all about beams, there is no spectral regridding happening.

This might be new to CASA 6.4, not sure.



