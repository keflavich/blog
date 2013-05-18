Paragraph for the methods paper
###############################
:date: 2008-11-15 00:25
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, methods paper
:slug: paragraph-for-the-methods-paper

The raw data from Bolocam contains noise components from the atmosphere
and instrument in addition to the astrophysical signal. To remove the
atmospheric noise, an iterative approach was required.

#. The median across all bolometers is subtracted
#. A set number of principle components are subtracted. The principle
   components are the most correlated components between bolometers. In
   this process both the atmosphere above the telescope - which is
   assumed to be constant across the field of view - and any large-scale
   astrophysical structure are removed.
#. The timestream data is mapped into the plane of the sky. Data points
   are mapped to the nearest pixel. 7.2" pixels are used so that
   sampling is better than Nyquist.
#. The map is deconvolved using a maximum entropy deconvolution
   algorithm ( Based on paper by Hollis, Dorband, Yusef-Zadeh, Ap.J.
   Feb.1992, written by Frank Varosi at NASA/GSFC 1992)
#. The deconvolved map is returned to a timestream and subtracted from
   the original to yield a noise-only timestream.
#. Power spectral densities are calculated for each scan in the noise
   timestream, and weights are calculated from these. [At the moment,
   the weights are actually inverse-variance]
#. The deconvolved map timestream is subtracted from the raw timestream,
   and then steps 1-6 are repeated on that timestream to recover flux
   that was oversubtracted in the first iteration.

Convergence takes ???? iterations....
??? PCA components are subtracted [default 13]...

.. raw:: html

   </p>

