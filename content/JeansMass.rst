Some notes about the Jeans mass scale using astropy's units.

Simple approaches to determining mass scales:

.. math:: v_{esc} = \sqrt{\frac{G M}{R}}

Isothermal equation of state:

.. math::  P = \rho k T 

.. math::  c_s = \sqrt{2 k T / m}

Setting :math:`v_{esc} = c_s` yields the mass scale:

.. math:: M = \frac{R}{G}  \frac{2 k T}{m} = \frac{R c_s^2}{G}

Using :math:`\rho = \frac{M}{ 4/3 \pi R^{-3} }`,

.. math:: R = \left(\frac{M}{4/3 \pi \rho}\right)^{1/3}

 so

.. math:: M = M^{1/3} \frac{c_s^2}{G \rho^{1/3}}

which rearranges to

.. math:: M = \frac{c_s^{3}}{G^{3/2} \rho^{1/2}}

where :math:`M` is now :math:`M_J`, the Jeans mass. In terms of
temperature, this is:

.. math:: M_J = \frac{(2 k T)^{3/2}}{(m G)^{3/2} \rho^{1/2}}

where :math:`m` is the particle mass, usually assumed to be 2.8 amu.

In[1]:

.. code:: python

    # astropy imports
    import astropy.units as u
    import astropy.constants as c
    # turn off verbose but unnecessary information
    import warnings
    warnings.filterwarnings('ignore')
    warnings.filterwarnings('ignore', category=u.UnitsWarning, append=True)

.. parsed-literal::

    WARNING: ConfigurationDefaultMissingWarning: Requested default configuration file /Users/adam/repos/astropy/astropy/astropy.cfg is not a file. Cannot install default profile. If you are importing from source, this is expected. [astropy]


In[7]:

.. code:: python

    amu = c.m_p
    temperature = 10 * u.K
    m = (((2 * c.k_B * temperature)**1.5 / ((2.8*c.m_p*c.G)**1.5 * (2.8*1e4*amu / u.cm**3)**(1/2.)))).cgs

In[5]:

.. code:: python

    m.to(u.solMass)

Out[5]:

.. math::

    $1.92903 \; \mathrm{M_{\odot}}$

.. parsed-literal::

    <Quantity 1.92902547696 solMass>

