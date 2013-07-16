PPVI Talk 3: Paul Clark
=======================
:date: 2013-07-15 11:45
:tags: ppvi

THE ORIGIN AND UNIVERSALITY OF THE INITIAL MASS FUNCTION
--------------------------------------------------------

Authors:

S. Offner (Yale University, United States),
P. Clark (Heidelberg University, ITA, Germany),
P. Hennebelle (Observatoire de Paris, LERMA, Paris, France),
N. Bastian (Liverpool John Moores University, United Kingdom),
M. Bate (University of Exeter, United Kingdom),
P. Hopkins (California Institute of Technology, Department of Astronomy, United States),
E. Moraux (Institut de Planetologie et d'Astrophysique de Grenoble (IPAG), France),
A. Whitworth (Cardiff University, Physics & Astronomy, United Kingdom)

Abstract
--------

We review current theories for the origin of the Stellar Initial Mass Function
(IMF) with particular focus on the extent to which the IMF can be considered
universal across various environments. To place the issue in an observational
context, we summarize the techniques used to determine the IMF for different
stellar populations, the uncertainties affecting the results, and the evidence
for systematic departures from universality under extreme circumstances. We
next consider theories for the formation of prestellar cores by turbulent
fragmentation and the possible impact of various thermal, hydrodynamic and
magneto-hydrodynamic instabilities. We address the conversion of prestellar
cores into stars, and evaluate the roles played by different processes:
competitive accretion, dynamical fragmentation, ejection and starvation,
filament fragmentation and filamentary accretion flows, disc formation and
fragmentation, critical scales imposed by thermodynamics, and magnetic braking.
We present explanations for the characteristic shapes of the Present-Day
Prestellar Core Mass Function and the IMF and consider what significance can be
attached to their apparent similarity. Substantial computational advances have
occurred in recent years, and we review the numerical simulations that have
been performed to predict the IMF directly and discuss the influence of
dynamics, time-dependent phenomena, and initial conditions. 


Last time, IMF discussion was very heated.
(technical difficulties)

Intro to IMF
------------
Salpeter, Kroupa, Chabrier, de Marchi ("Tapered" power law)
(aside) Thies & Kroupa: BDs not part of IMF

SFR indicators only see >10 Msun sources.  Must extrapolate downward.  This is
why extragalactic people care.

Are there variations in the IMF?
################################
Locally, no.

More evolved clusters, yes on the low-mass end:

 * Pleiades, NGC 2516, etc.  
 * Lose low-mass stars with age dynamically
 * fraction of BDs remaining drops to zero over time

Difficulties in measurement:

 * Patchy extinction
 * young clusters not done sampling IMF
 * don't understand hayashi tracks that well

Modal plot from van Dokkum

 * Hints at change in IMF

Extragalactic - big camps argue top, bottom heavy and universal

 * rely on mass to light ratios
 * M/L models depend on population synthesis models

What determines the IMF?
########################
Hoyle, Larson: the cloud fragmentation process.
Clouds fragment into cores, cores make stars.

Does supersonic turbulence regulate? (movie from Federrath)

Padoan: 

 * CMF driven only by turbulence. 
 * # of BDs controlled by Mach number.
 * Cloud-in-cloud problem: small cores may be in big cores

Press-Schechter & Excursion Set formalism

 * Gravitational decoupling sets "critical" scale
 * Hopkins: Density as a function of scale
    
    * large scale: shear support
    * intermediate: turbulence
    * small scale: hrm...
    * last-crossing => IMF

 * Hennebelle & Chabrier 2008 - account for non-thermal support
 * GMCs are a separate population

 * Useful: turbulence -> more BDs, so extragalactic maybe more turbulent?

Does the CMF map onto the IMF?
##############################

Cores must:

 * neither accrete nor merge (or you break the CMF my moving cores)
 * fragment self-similarly: same number of fragments per core
 * Same efficiency regardless of mass
 * formation must happen on similar timescale (can't have high-mass first)
 * Cores must be able to form stars, i.e. must be grav. bound

Can cores form stars?

 * Dust cores depend on column & temperature & line of sight effects
 * number of Jeans masses goes as T^-3
 * Velocity structure?  B-fields?

Fragmentation within cores

 * Used to think that everything fragmented...
 * strong B-fields reduce fragmentation
 * Still haven't studied parameter space well

SFE within cores

 * Binaries or triples form, requires 30%-50% efficiency
 * can work with outflows
 * but not clear... may depend on well-aligned B-field

Problems with CMF:

 * Pipe cores follow CMF shape, but are *pressure* bound
 * CMF in Aquila is too low
 * need CMF of Class 0 sources

Clusters
########
What effects have cluster simulations had on IMF studies...

 * Initial Conditions imprints thermal jeans mass in box, which imprints onto IMF
 * thermodynamics matter

Fraction of cloud doesn't matter

 * IMF is same in small periodic box and isolated cloud
 * colliding flows can build clouds, be more consistent
 * How we drive turbulence doesn't seem to affect IMF (solenoidal, compressive same)
 * power spectrum of turbulence doesn't affect IMF

Metallicity?

 * Myers 2011: 20x metallicity change -> same IMF
 * Multiplicity may change (Bate)
 * even 10^-5 Z_sun -> same IMF

Things that DO affect IMF:

 * radiative transfer: reduces fragmentation
 * need wind feedback, otherwise radiation -> flat IMF by preventing fragmentation but keeping gas
 * B-fields reduce characteristic mass by creating more filaments with different jeans masses

State of Simulations:

 * Top of IMF about right
 * bottom is wrong

Secondary Metrics
#################

Multiplicity

 * Krumholz & Bate both reproduce observations fairly well
 * Require radiative transfer

Summary
#######

 * IMF studies focused on low-mass end instead of high
 * Cores better understood

Future: Put simulations into observational plane

Questions
---------
 * Q: Properties of turbulence in simulations give same IMF... 
 * A: Outflows drive turbulence, but turbulence doesn't change IMF.  Outflows *remove* gas.

 * Q Zinnecker: Binaries.
 * A: Cathy will talk about this.  Fragmentation knobs are the issue
   Unclear that binary properties will stay constant (does field match cluster?)  N-body evolution matters

 * Q (Galactic center star studier...): not done with discussion of high-mass issues.  Radiatitve transfer still matters.  
 * A: Many effects are actually from mass segregation

 * Q: Alyssa Goodman:  Are the CMF and IMF both lognormals?
 * A: Sometimes fitting distributions they expect.  Maybe different processes in low mass clouds.
