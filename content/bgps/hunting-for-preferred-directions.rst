Hunting for preferred directions
################################
:date: 2011-06-06 03:58
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, simulation
:slug: hunting-for-preferred-directions

In our last group meeting, we discussed simulations using filamentary
structures. I've been trying to determine how best to generate
random/artificial filamentary structures in images. The first step in
that direction is coming up with a way to measure asymmetries and
therefore preferred directions within a real map. In order to do this,
I've had to develop a number of new tools in agpy for azimuthally binned
radial profiles and radially-averaged azimuthal profiles
(`radialprofile.py`_).
Examining real maps is necessary because a simple sinusoidal dependence
of the power introduces filamentation along the same directions at ALL
scales, which is not obviously (or in some cases, obviously not) the
correct solution. Filaments are observed on large scales, but sometimes
there can be 'kinks' in opposite directions on small scales.
So, the map I picked to examine was one with the most flagrantly obvious
filamentary structure in it: the Motte DR 21 MAMBO map. It was also a
choice of convenience because I already had the data on my laptop....

.. image:: http://3.bp.blogspot.com/-ULjqyt_ofEI/TexIAK9ohhI/AAAAAAAAGM0/eCEys_tFOTA/s320/MAMBOmap.png

The preferred direction is quite obvious in this map: there is a long
filament going up and down the map. Therefore, the DC component should
be substantially higher in one direction than the other.

.. image:: http://1.bp.blogspot.com/-X7TY9wPUL7Y/TexIAZ7hH_I/AAAAAAAAGM8/IEkgX500_Os/s320/MAMBOpsd.png

In the power-spectral-density image, it is quite clear that there is a
preferred direction, though it is not obvious that the fourier transform
is rotated 90 degrees from the image. My fourier intuition somewhat
fails me here.... I realize that a broad, smooth profile in real space
should be narrow and highly peaked in fourier space, but I don't fully
understand why it effectively spreads out in the perpendicular
direction, which I have confirmed that it does with a simple experiment.
I also don't know what the Shah function is, but it implies a periodic
dip in the image at every 1/5th of the image, or every 50 pixels.

.. image:: http://2.bp.blogspot.com/-l4qWlj1G42k/TexIAufhjSI/AAAAAAAAGNE/UqagczdWzwA/s320/MAMBOpowerspectra.png

These are the power spectra averaged over different angles as labeled.
-15 corresponds to -15 to +15, 15 corresponds to 15 to 45, etc. The
highly peaked 75-105 power spectrum shows the large-scale filamentary
profile. I think the difference in the DC component is actually an
artifact of the azimuthal binning process: each pixel can only be
assigned one angle, so the DC value isn't included in all of them...
I'll need to find a workaround for that because it's quite deceptive.

.. image:: http://4.bp.blogspot.com/-qEWk2rRrwNI/TexIBKn59FI/AAAAAAAAGNM/MXdsiKagpW4/s320/MAMBOazspectra.png

The more interesting way to view the data - and perhaps to analyze maps
- is to take *radial* averages in some range of spatial scales and plot
the azimuthal dependence. There is a clear sinusoid at large scales. The
legend shows "spatial frequency" in 1/pixel units. The distribution
becomes more even with angle and even changes preferred direction at
smaller scales (higher frequencies).
Next step is testing different approaches. I think an added,
steeper-power-law component would probably be the best way to start.
Another suggestion, courtesy Bruce Elmegreen, is to attempt this sort of
asymmetric power law sampling in 3 dimensions (with only 1 or 2
dimensions asymmetric) and then projecting down onto two dimensions.

.. _radialprofile.py: http://code.google.com/p/agpy/source/browse/trunk/agpy/radialprofile.py
.. _|image4|: http://3.bp.blogspot.com/-ULjqyt_ofEI/TexIAK9ohhI/AAAAAAAAGM0/eCEys_tFOTA/s1600/MAMBOmap.png
.. _|image5|: http://1.bp.blogspot.com/-X7TY9wPUL7Y/TexIAZ7hH_I/AAAAAAAAGM8/IEkgX500_Os/s1600/MAMBOpsd.png
.. _|image6|: http://2.bp.blogspot.com/-l4qWlj1G42k/TexIAufhjSI/AAAAAAAAGNE/UqagczdWzwA/s1600/MAMBOpowerspectra.png
.. _|image7|: http://4.bp.blogspot.com/-qEWk2rRrwNI/TexIBKn59FI/AAAAAAAAGNM/MXdsiKagpW4/s1600/MAMBOazspectra.png

