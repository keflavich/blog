Fourier transforms are not commutative or distributive
######################################################
:date: 2011-07-15 20:09
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, analysis
:slug: fourier-transforms-are-not-commutative-or-distributive

Problem with yesterday's work:

::

    A*B = IFT(FT(A)*FT(B))A*B - A*C != IFT(FT(A)*(FT(B)-FT(C)))

If instead of yesterday's "bandpass filter" you use the convolution -
convolution 'filter', the agreement in real space and most of fourier
space is much better:

.. image:: http://1.bp.blogspot.com/-dXT8RIHG6iI/TiCeMHu2bBI/AAAAAAAAGTc/NjQaTyJb4cc/s320/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_map20filtercompare.png

.. image:: http://1.bp.blogspot.com/-m0DeYyvE0Xg/TiCeM6b_LOI/AAAAAAAAGTk/MwwIbLjhY4Q/s320/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_map20filterpsds.png

though map20 clearly reproduces some structures better (higher) but is
overall less powerful than the filtered map.

.. _|image2|: http://1.bp.blogspot.com/-dXT8RIHG6iI/TiCeMHu2bBI/AAAAAAAAGTc/NjQaTyJb4cc/s1600/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_map20filtercompare.png
.. _|image3|: http://1.bp.blogspot.com/-m0DeYyvE0Xg/TiCeM6b_LOI/AAAAAAAAGTk/MwwIbLjhY4Q/s1600/exp12_ds2_astrosky_arrang45_atmotest_amp5.0E%252B02_sky00_seed00_peak050.00_nosmooth_map20filterpsds.png

