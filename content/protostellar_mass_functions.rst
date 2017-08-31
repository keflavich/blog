Protostellar Mass Functions
###########################
:date: 2017-08-30 15:18
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: imf, pmf

The stellar `initial mass function
<https://en.wikipedia.org/wiki/Initial_mass_function>`_ is important for a wide
variety of astronomical topics, and I'm interested in studying its formation.
The `protostellar mass function`_, by contrast, is much
less well-studied, but understanding it can provide important insights into the
formation of the IMF.  In particular, we assume both for simplicity and because
of a lack of contrary evidence, that the IMF is uniform in time in space.  In
other words, given that a star is going to form at some point, it has a
likelihood to become a star of a given mass described exclusively by the IMF.
While this assertion is entirely absurd - if you are "about to form" a star in
a blob of gas that only has 0.1 Msun in a 1 pc radius, it certainly cannot form
a 100 Msun star - it remains consistent with nearly all observations and is
therefore used in this time- and space-invariant form.

It is likely that new studies of stellar populations, e.g., GAIA's observations
of a huge population of stars with well-determined distances (and therefore
luminosities), will reveal some variations in the IMF.  However, many studies
based on evolved stellar populations are subject to ambiguities in the initial
conditions.  So, it is still quite useful to study those initial conditions
directly.

There has not been a huge amount of work on protostellar mass functions.
`McKee and Offner`_ defined the PMF as the distribution of masses of
protostellar sources that would produce a given IMF.  Their PMFs are therefore
strongly dependent on the underlying IMF assumed.

I have implemented the mass functions they defined in `this code`_.  The code
is generalized such that you can input other mass functions.  McKee & Offner
only used the `Chabrier 2005`_ mass function; I include the `Kroupa 2001`_ mass
function as well for comparison

.. image:: |filename|/images/steadystate_pmf_chabrier.png
   :width: 600px

.. image:: |filename|/images/steadystate_pmf_kroupa.png
   :width: 600px

The comparison between the Chabrier and Kroupa mass functions is shown above.
Note that these are somewhat deceptive plots, since they show P(M) vs log(M).
The plot shows the most likely individual masses by number, but the plots are
actually quite squished to the left in linear space, such that the most common
range of stars (the integral of both functions) is closer to the same (~0.2-0.3
Msun).  The more commonly shown version of these plots is the integral form,
which has a positive power-law slope in the lowest bin in the Kroupa MF,
showing the usual peak at 0.3 Msun.  This version of the functions is
nontrivial to compute, especially for the modified PMFs.

The Chabrier version is a near-perfect match to Figure 3 of `McKee and Offner`_.


.. image:: |filename|/images/taperedaccretion_pmf_chabrier.png
   :width: 600px

.. image:: |filename|/images/taperedaccretion_pmf_kroupa.png
   :width: 600px
           

.. _McKee and Offner:
.. _protostellar mass function: http://adsabs.harvard.edu/abs/2010ApJ...716..167M
.. _this code: https://github.com/keflavich/imf/blob/master/imf/pmf.py
.. _Chabrier 2005: http://adsabs.harvard.edu/abs/2005ASSL..327...41C
.. _Kroupa 2001: http://adsabs.harvard.edu/abs/2001MNRAS.322..231K
