Bolocam Mass Calculations
=========================
:date: 2013-03-25 11:14
:author: Adam (keflavich@gmail.com)
:tags: physics, bgps, dust

Adopt an effective Bolocam center frequency,  f = 271.1 GHz

Use Ossenkopf, V. & Henning, Th. 1994, A&A, 291, 943 Table 1. [http://adsabs.harvard.edu/abs/1994A%26A...291..943O]
Interpolate last two entries (lambda = 1.0 mm and 1.3 mm to f)

This gives kappa = 0.01166 cm^2 g^-1 (or round to 0.0117)
for gas-to-dust = 100.
But the slope between these 2 points is only 1.61!

The points in OH94 table 1 jump around and locally give a variety of
slopes around 1.8.  A fit to kappa longward of 100 microns
gives a slope of 1.8.

Interpolating kappa from 1.00 mm where OH5 gives kappa(1.00) = 0.0137
(for a gas-to-dust ratio = 100) to 271.1 GHz (= 1.1058 mm)
using a slope of 1.8 gives:

**:math:`\kappa = 0.01143 cm^{2} g^{-1}`**

This is the same as the value used by Enoch, so let's adopt it
(round to 0.0114), but note that this was calculated for 271.1 GHz.

For the v1.0 data, the BGPS has the following properties:

effective beam FWHM = 33"

gaussian beam sigma = 14.01"    (= FWHM / sqrt (8*ln(2))

effective beam radius = 19.82"    (= FWHM / sqrt (4*ln(2))

This is the radius of a circular top-hat function that has the
same solid angle as a gaussian.  At a distance of
D = 1 kpc, this radius corresponds to a length  = :math:`2.97 x 10^{17}` cm.
The effective beam solid angle is,

                :math:`\Omega = 2.902 x 10^{-8}` sr.

  Adopt a fiducial dust temperature for mass calculations,

                  :math:`T_d = 20K`

The total mass per Jy at :math:`D_{kpc}` = 1 kpc is given by

:math:`M = 1.0 x 10^{-23} * S(Jy) * D^2 / \kappa * B_nu(T)`

:math:`  =  14.30 * [e^(13.01/T(K) - 1] * S(Jy) * D^2_{kpc}`    (Solar masses)

 For T = 20 K
     :math:`M = 13.07 * S(Jy) * D^2_{kpc} M_{\odot}`      (Solar masses)

This corresponds to a beam-filling column density of H_2,
  N(H2) = 2.19e+22 * [e^(13.01/T(K) - 1] * S(Jy)             (cm^-2)

  For T = 20 K
  N(H2) = 2.01 x 10^{22} * S(Jy)    (cm^{-2})
  A_V = 21.1 magnitudes per Jy

where I used the Bohlin & Savage calibration,
  A_V = 1 mag. <=> N(H) = 1.9 x 10^{20} cm^{-2} and
  N(H_2) = N(H) / 2

