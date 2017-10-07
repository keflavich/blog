Understanding Millimeter Source Counts
######################################
:date: 2017-10-07 14:48
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: plf, pmf, cmf

A few recent projects (`ALMA W51
<https://github.com/keflavich/W51_ALMA_2013.1.00308.S>`_ and `ALMA Sgr B2
<https://github.com/keflavich/SgrB2_ALMA_3mm_Mosaic/>`_) have raised
the question: How do we interpret unresolved millimeter sources?

In the two linked works, I concluded that most of the 1mm and 3mm point sources
we detected with ALMA at D>5 kpc are protostars with dust envelopes - i.e.,
they are "Class 0/I"-like sources, but they are generally more luminous (and
therefore more massive) than their local analogs.

One of the appeals of the dust continuum, the wavelength range from about 0.5
to 2 mm, for studying star formation is that we usually assume that the source
brightness is proportional to the source mass.  For optically thin dust, this
assumption is pretty good.  The (systematic, unmeasurable) uncertainty is, to
first order, just the uncertainty in the dust temperature.

However, protostellar cores - dust cores that contain a YSO or any luminous
object (whether the luminosity is nuclear or gravitational in nature doesn't
matter) - violate those assumptions.  First, the dust is not isothermal, so the
emission is weighted toward the hotter dust that represents less of the total
mass.  Second, the dust is not necessarily optically thin - a centrally
concentrated source is likely to have a significant optical depth, particularly
at the shorter wavelengths.  Third, once the optically thin assumption is
broken, the source geometry matters; there may be some axes along which the
source is substantially brighter.

The `ALMA-IMF program
<https://almascience.nrao.edu/observing/highest-priority-projects#flyout_2017.1.01355.L>`_,
which I am co-leading with Frederique Motte, has the broad goal of
understanding the formation of the IMF in the Galaxy.  In practice, we will
measure some form of 1 mm luminosity function.  In the long term, we may be
able to obtain some additional constraints on the internal temperature
structures of the sources.  The imminence of this large data set motivates the
development of a general systematic analysis tool for assessing the
implications of the mm luminosity function on the underlying mass function.

In the related `Protostellar Mass Functions`_ post, I implemented the
protostellar mass functions described by `McKee and Offner`_.  These functions
provide the mapping between a stellar mass function and a protostellar mass
function given some assumed accretion history.  The assumed accretion histories
for the stars are very simple (in reality, accretion is probably quite
stochastic), but that's fine since it provides something testable.

I've then tried to follow up by implementing the next step toward producing
something comparable to observables as defined in `Offner and McKee`_, but
unfortunately this is a good deal more challenging.  We need a means to map a
protostellar mass to a luminosity, and there is no simple one-to-one function
to do this.

Protostellar Evolution Models
-----------------------------
Several authors have described protostellar evolution models.  They mostly
refer back to `Palla & Stahler I`_ and `II <Palla & Stahler II>`_.  The `Offner
& McKee model <Offner+ 2009>`_ is based on `Tan & McKee 2004`_.  There is a
similar model by `Hosokawa & Omukai`_, who have shown that high-mass stars can
have substantially varying structures (radii -> luminosities) depending on
their accretion rates.  Mikhail Klassen implemented the `Offner+ 2009`_
protostellar evolution models `in fortran <MikhailKlassen>`_ in `this paper
<Klassen+ 2012>`_, with only slight differences assumed in the polytropic
parameters and the accretion luminosity (`Offner+ <Offner+ 2009>`_ assumed 25%
of the accretion energy is lost to wind and treated the disk and star accretion
luminosity separately, according to `Klassen+ 2012`_).

The Klassen implementation is the best immediately available to me.  Both they
and `Offner and McKee` compared their results to `Hosokawa & Omukai`_,
considering the latter to be more accurate, and found "good" agreement (<2x
disagreement) in the radius as a function of mass.  The same comparison is
shown below; these figures match `Klassen+ 2012`_ Figures 1 and 2 (though I
don't plot exactly the same things).

.. image:: |filename|/images/Klassen_vs_Hosokawa_model_comparison.png
   :width: 600px

At least in priniple, these tools give us a mechanism to determine L(M, M_f),
the luminosity as a function of the current mass and the final mass of a star.
Alternatively, that can be written as L(t, M_f), the luminosity as a function
of time and final mass.  However, there is at least one major practical concern:
the protostellar evolution models have the free variable mdot, not M_f, so
in order to use these models, we need to populate a 'fully sampled' L(M, M_f) table.
Offner et al computed such a table, but then used an approximation for
R(M) - the stellar radius as a function of its mass - for their calculations.

TODO: compute function that obtains R, T given M, t

Protostellar SED Models
-----------------------
The next step in computing a millimeter luminosity distribution is to convert
from stellar luminosity to the reprocessed flux at a given wavelength.  This
step has an enormous number of free parameters, since the surrounding structure
may include both a disk and a core whose shapes will both vary.

There are two large grids of radiative transfer models that have been computed
for this purpose.  The `Robitaille grid`_ is complete and open, and it should
cover all stellar masses.  The `Zhang+ 2017`_ grid is not yet available, but it
may be more self-consistent.


.. _McKee and Offner:
.. _protostellar mass function: http://adsabs.harvard.edu/abs/2010ApJ...716..167M
.. _Offner and McKee: http://adsabs.harvard.edu/abs/2011ApJ...736...53O
.. _Palla & Stahler I: http://adsabs.harvard.edu/abs/1991ApJ...375..288P
.. _Palla & Stahler II: http://adsabs.harvard.edu/abs/1992ApJ...392..667P
.. _MikhailKlassen: https://github.com/mikhailklassen/protostellar_evolution
.. _Klassen+ 2012: http://adsabs.harvard.edu/abs/2012MNRAS.421.2861K
.. _Tan & McKee 2004: http://adsabs.harvard.edu/abs/2004ApJ...603..383T
.. _Hosokawa & Omukai: http://adsabs.harvard.edu/abs/2009ApJ...691..823H
.. _Offner+ 2009: http://adsabs.harvard.edu/abs/2009ApJ...703..131O
.. _Protostellar Mass Functions: protostellar_mass_functions.rst
.. _robitaille sedfitter: github.com/astrofrog/sedfitter
.. _Robitaille grid: https://zenodo.org/record/166732#.WdlXwmK3xcw
.. _Zhang+ 2017: http://adsabs.harvard.edu/abs/2017arXiv170808853Z
