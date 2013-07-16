PPVI Talk 4: Christoph Federrath
================================
:date: 2013-07-15 14:30
:tags: ppvi

THE STAR FORMATION RATE OF MOLECULAR CLOUDS
-------------------------------------------

Authors:

P. Padoan (ICREA & Institute of Cosmos Sciences, University of Barcelona, Spain),
C. Federrath (School of Mathematical Sciences, Monash University, Australia),
G. Chabrier (Ecole Normale Superieure de Lyon, France),
N. Evans (The University of Texas at Austin, United States),
D. Johnstone (Herzberg Institute of Astrophysics, National Research Council of Canada),
J. Jorgensen (Star and Planet Formation Center, University of Copenhagen, Denmark),
C. McKee (University of California, Berkeley, United States),
A. Nordlund (Niels Bohr Institute & Star and Planet Formation Center, University of Copenhagen)

We review recent advances in the analytical and numerical modeling of the star
formation rate in molecular clouds and discuss the available observational
constraints. We focus on molecular clouds as the fundamental star formation
sites, rather than on the larger-scale processes that form the clouds and set
their properties. Molecular clouds are shaped into a complex filamentary
structure by supersonic turbulence, with only a small fraction of the cloud
mass channeled into collapsing protostars over a free-fall time of the system.
In recent years, the physics of supersonic turbulence has been widely explored
with computer simulations, leading to statistical models of this fragmentation
process, and to the prediction of the star formation rate as a function of
fundamental physical parameters of molecular clouds, such as the virial
parameter, the rms Mach number, the compressive fraction of the turbulence
forcing, and the ratio of magnetic to gas pressure. Infrared space telescopes,
as well as ground-based observatories have provided unprecedented probes of the
filamentary structure of molecular clouds and the location of forming stars
within them. We may thus be on the verge of a breakthrough in our understanding
of star formation, and particularly of the star formation rate of molecular
clouds. 

Content
-------
Star Formation Rate from statistics of turbulence

Drastic differences in SFR, not just because of column density.  (Lada 2010:
Pipe vs Rho Oph, Rho = 15 Pipe)

Intro slides:

 * KS relation with local clouds
 * CMF -> IMF (30-70% SFE)
 * Radiation feedback: 

    * only affects small scales
    * affects > 10^8 cm^-3

 * B-fields 
   
   * reduce fragmentation *more effectively* than radiation
   * drive outflows

 * Outflows & Jets

   * direct: reduce star mass
   * indirect - drive turbulence
   * triggering SF

What drives turbulence?
-----------------------

 * Jets contribute to turbulence on small scales, but don't feed back effectively on large scales
 * Ionization fronts, bubbles?
 * SN explosions
 * MRI / shear?

Turbulence
``````````

 * Reynolds > 1000
 * cites da Vinci
 * Supersonic "cascades" to sonic scale

    * Kolmogorov -5/3 turbulence is incompressible (subsonic)
    * Larson -2 supersonic, shock-dominated

Turbulence in a Box
###################

 * Mach numbers 2-50
 * "Forcing term" f

   * divergence free vs. compressive turbulence
   * compressive -> bigger voids, higher overdensity

 * Density PDF: lognormal
 * Perseus observations: similar Mach numbers, different dispersions: requires changed *b*
 * Column vs. Volume density: Brunt 
 * Kainulainen, starless -> taurus -> IRDCs

   * starless: b=0
   * starry: b=0.5
   * IRDCs: higher

Density PDF -> SFR
------------------

All recent theories of SF, SFR are based on an integral over the density PDF.

 * Hennebelle & Chabrier theory: Different free-fall times at different densities, so must be in an integral
 * Cricitical density :math:`s_{crit}\propto \ln \left(\alpha_{vir}\mathcal{M}^2\right)`
 * SFR depends on alpha_vir, b, and M
 * Dependence on alpha_vir: inversely proportional to SFR, SFR \propto alpha_vir^-1/2
 * Dependence on Mach number

    * stronger when you consider non-constant t_ff
    * SFR larger as gas compressed more

 * Dependence on *b*: Compressive is much more star forming

   * compressive drives gas to self-gravitating densities far more rapidly

 * What about magnetic fields?  Add \beta

   * B-fields "wash out" structures
   * Reduce fragmentation

 * Direct measurement of line-of-sight star counts and gas density

   * 1%, 10% SFE examples
   * makes a distribution similar to Heiderman plot
   * agreement assumes total core-to-star efficiency = 100%

Conclusions
-----------

 * supersonic, magnetized turbulence is important for driving SFR

Questions
---------

 * Q: Adam Frank - Abstract vs realistic forcing from, e.g., outflows.  Driving
   sources makes turbulence look different.
 * A: These experiments are essential.  Need to find out.

 * Q: Fabian Heitsch - How does non-isothermality affect theory?
 * A: We are looking only at density ranges where gas is isothermal.  SFR is
   not very dependent on T, but IMF *is*.

 * Q: How do you explain that solenoidal is a better fit, when all drivers are
   compressive?
 * A: Don't know. BUT, compression *drives* solenoidal modes
   [this is possibly interesting - does a single compression event drive a lot of solenoids?]

 * Q: What are the effects of field-slippage (non-ideal MHD, ambipolar diffusion)
 * A: Not that important....

 * Q: Tan - Filaments have ordered B-fields on large scales.  Do you see that in the simulations
 * A: Fields are very intermittent, bouncing all over the place. Large scale
   "input" B-fields may be more important for mol. clds

 * Q: Solenoidal -> toroidal fields, which squeeze gas.  Do you see squeezing
   (compression) from solenoidal?
 * A: "simple" version of B-fields only works for magnetic pressure, not
   magnetic tension.  For subsonic, SFR doesn't work.  Need disordered fields

 * Q: Clark? - How do these results compare with Lada's?  
 * A: Don't know, didn't want the complexity
