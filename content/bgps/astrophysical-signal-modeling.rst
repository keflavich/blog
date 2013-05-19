Astrophysical Signal Modeling
#############################
:date: 2011-05-24 17:39
:author: Adam (noreply@blogger.com)
:tags: googlepost, simulation, pipeline
:slug: astrophysical-signal-modeling

Here we finally get into the meat of the simulations. The goal is to
develop realistic - but arbitrary - astrophysical models to run through
simulations.
The first step is to figure out what a realistic sky looks like. To this
end, I use the HiGal SDP fields, looking only at their power spectra.
They are well represented by a power law with α = 3 (shown in the dashed
black line below).

.. image:: http://2.bp.blogspot.com/-50R2lfaIGrY/TdvZi5tl5VI/AAAAAAAAGLQ/w45OC9dk3Rg/s320/sdp_psds_powerlaw.png

Therefore, I've attempted to randomly sample from a similar power law
distribution using the following IDL code:

``dimsize = 512    realpower = realpowers[ii]    imagpower = imagpowers[ii]    imagscale = imagscales[ii]    peakamp = 1.0    noise = 0.03    smoothscale = 2.0    smoothkernel = psf_gaussian(npix=512,ndim=2,fwhm=31.2/7.2/2.0,/normalize)    sigma_gp = 128.0 ; sigma-width of the Galactic Plane (can get more accurate value from Cara's paper)    xx = findgen(dimsize) #  replicate(1.0,dimsize)    yy = findgen(dimsize) ## replicate(1.0,dimsize)    rr = sqrt( (xx-255.5)^2 + (yy-255.5)^2 )    realpart = (rr^realpower) * randomn(seed1,[dimsize,dimsize])    imagpart = ((rr*imagscale)^imagpower) * randomn(seed2,[dimsize,dimsize])*complex(0,1)     fakesky = abs(fft(shift(realpart + imagpart,0,0),1))    expweight = exp(-(yy-255.5)^2/(2.0*sigma_gp^2)) ; most power is in the inner plane    fakesky *= peakamp/max(fakesky)    fakesky_sm = convolve(fakesky,smoothkernel)    fakesky_sm = fakesky_sm*expweight    fakesky_sm += randomn(seed3,[dimsize,dimsize]) * noise``

Since Power is the fourier-transform squared, I'm using a power-law of
α=1.5 for the "real" part of the sampling. The imaginary part follows a
shallower slope to reduce the amount of power in large structures, which
didn't look quite right (but maybe I should leave both slopes the
same?). With both the same, and without the imaginary part down-scaled,
the structure appears too "cloudy" and not "clumpy" enough. But back to
that later...

The peak amplitude is set by re-scaling the map. Ideally, we'd like to
see this set by a point source, since that is true in most fields.
The noise level should not be included in simulations, but should be
used to show the difference between pipeline-leftover noise and gaussian
noise on the sky. i.e., what structures disappear when you just add
noise, and what structures are removed by the pipeline.

The PSF is simply to smooth out signals that are removed by the
telescope beam. We can replace this with a "real" PSF if and when we've
come up with a believable one.

The noise is added after the smoothing because it should be on a pixel
scale rather than a beam scale.

Here are some example realizations with different power laws:

.. image:: http://3.bp.blogspot.com/-vCy9Lx2RjWw/Tdvs_PO1u6I/AAAAAAAAGLw/cc7cIupQu0U/s320/exp7_fakesky_sm_realP-1.0_imagP-1.0_imagS01.0_seednum02.png

.. image:: http://4.bp.blogspot.com/-qpgg2U41r6U/Tdvs_RPxARI/AAAAAAAAGL4/v5exzhhqDew/s320/exp7_fakesky_sm_realP-1.5_imagP-1.5_imagS01.0_seednum02.png

.. image:: http://3.bp.blogspot.com/-2kUqO9aE8zM/Tdvs_maHaCI/AAAAAAAAGMA/u5bDCfiVuH0/s320/exp7_fakesky_sm_realP-2.0_imagP-2.0_imagS01.0_seednum02.png

.. _|image4|: http://2.bp.blogspot.com/-50R2lfaIGrY/TdvZi5tl5VI/AAAAAAAAGLQ/w45OC9dk3Rg/s1600/sdp_psds_powerlaw.png
.. _|image5|: http://3.bp.blogspot.com/-vCy9Lx2RjWw/Tdvs_PO1u6I/AAAAAAAAGLw/cc7cIupQu0U/s1600/exp7_fakesky_sm_realP-1.0_imagP-1.0_imagS01.0_seednum02.png
.. _|image6|: http://4.bp.blogspot.com/-qpgg2U41r6U/Tdvs_RPxARI/AAAAAAAAGL4/v5exzhhqDew/s1600/exp7_fakesky_sm_realP-1.5_imagP-1.5_imagS01.0_seednum02.png
.. _|image7|: http://3.bp.blogspot.com/-2kUqO9aE8zM/Tdvs_maHaCI/AAAAAAAAGMA/u5bDCfiVuH0/s1600/exp7_fakesky_sm_realP-2.0_imagP-2.0_imagS01.0_seednum02.png

