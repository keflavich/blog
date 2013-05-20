Trying to bootstrap
###################
:date: 2011-03-28 02:01
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, downsampling, discrepancy, calibration, pipeline
:slug: trying-to-bootstrap

I've concluded, based on previous posts
http://bolocam.blogspot.com/2011/02/downsampling-why-is-dec-2010-different.html,
http://bolocam.blogspot.com/2011/03/revisiting-calibration-yet-again.html,
and
http://bolocam.blogspot.com/2011/03/workaround-for-individual-maps.html,
that ds5 is a problem primarily for undersampled images, i.e. those
taken in the normal mapping mode. This makes bootstrapping a bit tricky.

There are two options:

    1. Map Uranus and AFGL 4029 both in Volts and figure out what flux density
       AFGL 4029 must have to lie on that curve
    2. Map Uranus and compute a calibration curve, apply that calibration curve
       to AFGL 4029, and then compare derived flux densities.

Both have the major problem that the individual AFGL 4029 maps will
forcibly be undersampled if I use ds5 data (which is normally OK,
according to the first paragraph). In the second case, it is possible to
co-add the images and get around the under-sampling issue, while in the
first case it is not because of the dependence on total loading
(MEANDC).

The real problem is that the whole goal of these observations was to
compare the different observing methods and see if they agree (1x1, 3x1,
pointing, etc.) since the pointing-style observations were used to
calibrate the others. But if the 1x1s are just straight-up unreliable,
how can we do the comparison? I think the co-added AFGL 4029 is the only
option, but then how do I test if it's correct? It would be really nice
to have AFGL 4029 observed with both scan types...

Alright, onto the data. After last week's fix of the bad bolos, I really
hope ds1 and ds5 agree. However, first glance at the cal curves says
they don't. ds1 and ds2 agree, but ds5 is different.

After checking them out with
``ds9 *ds[15]*13pca*_map10.fits -scale limits -1 1000 -log -cmap hsv -match colorbars -match scales -match frames wcs &``,
it appears that the _mask_ data is all... wrong, somehow. That's OK, I
want to discard the mask data anyway, so I'm happy to NOT spend time
debugging it.

Even after careful examination showing that the fits look good - and
noting that the fluxes look pretty much the same - the calibration
curves still look rather different. Unfortunately I had to spend 3 hours
debugging IDL plotting commands; I want to show the fits each time and
save them as postscripts. What does "xyouts" with "/device,/normal" do?
I thought that should plot x,y text at the coordinates specified in the
plot window... but no, that is JUST /normalize.

Anyway, realized that centroid\_map treated NANs as zero. Added ERR
keyword (with a reasonable estimate of the error) in centroid\_map to
ignore NANs. It looks like improper treatment of NANs is responsible for
a lot of the scatter seen in the calibration plots.

There is a substantial difference between the "fitted" peak and the
"measured" peak (the latter computed by taking the sum of the pixels
divided by the area of the fitted gaussian). It looks like the
"measured" version is more robust, at first glance. However,
unfortunately, for 101208\_o11, the difference between ds1 and ds5
exists in both quantities. I will have to examine timestreams now...
ARGH.

Well, the timestreams show... that indeed the model is lower in ds1, but
not why. The "remainder" (new\_astro; the stuff that never gets
incorporated into the model but DOES get incorporated into the map)
appears to be the same in both. Similarly, there is little to no flux in
the PCA atmosphere, so it's not simply being cleaned out. Where is the
flux going or coming from?

.. image:: http://3.bp.blogspot.com/-6lqGwWn650Q/TY_rgZKA9QI/AAAAAAAAGCI/Iq9O5mnmhl8/s320/101208_o11_ds1_uranus_indivtest_delinetimestream011_plots_20_bolo02.png

.. image:: http://1.bp.blogspot.com/-7uBbEU1tAqM/TY_rgg6Jq9I/AAAAAAAAGCQ/iaGhOSb6gtQ/s320/101208_o11_ds5_uranus_indivtesttimestream011_plots_20_bolo02.png

.. image:: http://1.bp.blogspot.com/-YKdZcNOjm7Q/TY_rg6tcvhI/AAAAAAAAGCY/fr4l8j-v4xI/s320/101208_o11_ds1_uranus_indivtesttimestream011_plots_20_bolo02.png

.. _|image3|: http://3.bp.blogspot.com/-6lqGwWn650Q/TY_rgZKA9QI/AAAAAAAAGCI/Iq9O5mnmhl8/s1600/101208_o11_ds1_uranus_indivtest_delinetimestream011_plots_20_bolo02.png
.. _|image4|: http://1.bp.blogspot.com/-7uBbEU1tAqM/TY_rgg6Jq9I/AAAAAAAAGCQ/iaGhOSb6gtQ/s1600/101208_o11_ds5_uranus_indivtesttimestream011_plots_20_bolo02.png
.. _|image5|: http://1.bp.blogspot.com/-YKdZcNOjm7Q/TY_rg6tcvhI/AAAAAAAAGCY/fr4l8j-v4xI/s1600/101208_o11_ds1_uranus_indivtesttimestream011_plots_20_bolo02.png

