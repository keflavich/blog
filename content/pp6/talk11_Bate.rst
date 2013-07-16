PPVI Talk 11: Matthew Bate
==========================
:date: 2013-07-15 14:30
:tags: ppvi

STAR CLUSTER FORMATION AND FEEDBACK
-----------------------------------


M. Krumholz (University of California, Santa Cruz, Astronomy, Santa Cruz, United States),
M. Bate (Exeter University, Astrophysics, United Kingdom),
H. Arce (Yale University, Astronomy, United States),
J. Dale (Czech Academy of Sciences, Mathematics, Physics, and Earth Sciences, Czech Republic),
R. Gutermuth (University of Massachusetts, Department of Astronomy, United States),
R. Klein (University of California, Berkeley, Astronomy, United States),
Z.-Y. Li (University of Virginia, Astronomy, United States),
F. Nakamura (National Astronomical Observatory of Japan, Japan),
Q. Zhang (Harvard-Smithsonian Center for Astrophysics, United States)

Stars do not generally form in isolation. Instead, they form in clusters, and in these clustered environments newborn stars can have profound effects on one another and on their parent gas clouds. Feedback from clustered stars is almost certainly responsible for a number of otherwise puzzling facts about star formation: that it is an inefficient process that proceeds slowly when averaged over galactic scales; that it produces mostly unbound field stars rather than bound clusters; and that it produces an IMF with a distinct peak in the range 0.1 - 1 Msun, rather than an IMF dominated by brown dwarfs. In this review we summarize current observational constraints and theoretical models for the complex interplay between clustered star formation and feedback. 

Intro
-----
 * 30 Dor - need for feedback treatment
 * Wrong results without feedback
   * SFR too high
   * IMF has too many small stars
 * clusters stay bound unless feedback included. Too bound?

3 Categories of feedback:
 * momentum: Jets, outflows, radiation pressure.  Efficient cooling
 * hot gas feedback: winds from hot stars, high velocity shocks, ionized regions
 * Thermal feedback: heating, thermal pressure

Momentum Feedback
`````````````````
Protostellar outflows
 * outflow momentum / cloud mass = velocity; compare to velocity dispersion
 * If all simultaneous, could unbind cloud
 * if gradual, stir turbulence
 * Low coupling could just punch holes

NGC 1333 "prototypical protocluster"
 * most observations: can drive turbulence
 * outflow power vs turbulence dissipation: often comparable
 * insufficient in GMCs / large scales

Simulations:
 * outflows can maintain virial equilibrium
 * collimated flows more efficient than spherical flows at driving turbulence
 * jet into smooth medium bad at exciting supersonic turbulence
 * Wang 2010: outflows, turbulence, b-fields all reduce SFR

Radiation Pressure
##################
Direct transfer of momentum via photons
 * dominated by massive stars
 * drive winds on galactic scales
 * less important than outflows for clusters with M<10^4 msun

Feedback significant if :math:`\dot{p} * t_{ff} \gtrsim M v_{virial}`.  
 * :math:`\dot{p} = f_{trap} L/c`.
 * what is f_trap?
 * Murray says f > 1, others say 1
 * Shane Davis VET vs FLD radiation
 * Efficiency still uncertain

Hot Gas Feedback
````````````````
Hot stars: T>40,000 K
 * M > 40 msun
 * wind momentum flux less than radiation
 * winds create shocks, very hot gas.  Cooling is slow
 * But, wind-shocked gas can "leak" 
 * HII regions are also important

Wind observations:
 * Chandra 30 Dor & others
 * Partially leaky
 * HII regions dominate in general
 * ?x-ray dominates in 30 dor? (inconsistent with slide)

Wind theory:
 * spherically symmetric models
 * leakage parameters
 * simulations: Rogers & Pittard
 * very leaky

Photoionization / Hot Gas
#########################
Spitzer standard treatment

Hundreds of HII regions known...

Theory:
 * limit growth of OB stars
 * Walmsley: accretion flows stall HII region, crush it
 * Keto: gravitational trapping

HII expansion into clouds
 * disrupts low-mass clouds
 * Dale: GMC survives if escape velocity exceeds 10 km/s

Triggering
----------
 * weak triggering: same # of stars, but faster
 * strong triggering: increase in overall SFE
 * Top-heavy IMF?  No

RDI: Bisbas, Haworth

Evidence is weak
 * age gradients: questionable
 * higher sfe: questionable
 * causal links in ages
 * young stars near bubbles
 * 10-20% (Kendrew)
 * negative feedback wins

SNe feedback
------------
hot gas feedback
 * not important because delayed by 4 years
 * only 1 sne in 30 Dor, but lots of ejection by other forms
 * very important on large / galactic scales

Thermal Feedback
----------------
Direct stellar luminosity
 * some nuclear, some accretion
 * <3 msun, accretion luminosity dominates
 * if accretion energy goes into outflows, not thermal
 * accretion bursty would reduce thermal feedback
 * substantial heating in inner portions of clusters
 * thermal feedback inhibits fragmentation: changes IMF
 * reduce dependence on initial conditions for IMF
 * can reproduce IMF

Cooperative accretion
 * thermal feedback prevents additional fragmentation -> top-heavy IMF
 * everything accretes onto current stars

more physics in more simulations
 * outflows reduce accretion, which reduces thermal feedback
 * reduces "overheating" problem

B-fields
 * may increase accretion rates
 * on large scales, inhibit fragmentation
 * overall make star formation efficiency lower


Questions
---------
 * Q: Chris McKee: Possible role of supernovae.  Photoionization occurs first.
   Supernova goes off in low density cavity, no effect on cloud.
 * A: Potential problem, we just don't know at the moment.  In the 10^5+ Msun
   clouds, the cloud stays intact - HII region doesn't kill it.  In those
   cases, they hit lots of mol. gas
 * Q: Peter ?: Question about methods.  Are the sink particles magic?  Is this
   magic?
 * A: Well, we need them in order for the simulations to work.  Try to make
   them as small as possible.  Go to first hydrostatic core phase.  I think
   they're not the dominant uncertainties
 * Q: Diederich Kruijssen - How does feedback affect cluster formation?  If you
   end with a bound cluster, feedback didn't matter.
   Do we understand the degeneracies well enough to make "perfect" simulations.
 * A: No conclusions.  This is about where we are now.  How does feedback
   affect the *cluster*?  We still don't know.
 * A2: No, we don't understand the degeneracies between the types of feedback
   at all.
 * Q: Mike Myer - Global collapse vs driven turbulence.  Modest age spreads.
   SFR too fast & too efficient; I would think either or.  Which solves too
   fast, which solves too efficient?
 * A: Too fast - solved by Wang et al.  All feedback & mechanisms, SFR drops a
   lot.  But, none stop star formation in the end.  Need some way to disperse
   cloud still.  Need HII regions and other feedback in more massive clusters.
 * Q: Hans Zinnecker - SN feedback.  Some evidence in ScoCen for SN triggering
   because low-mass stars are coeval with other stars.  Coeval = must be
   triggered.  Also have to think about starburst galaxies - maybe different
   mode.  Maybe positive triggering in starbursts
