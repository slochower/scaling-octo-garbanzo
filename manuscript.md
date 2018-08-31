---
author-meta:
- David R. Slochower
date-meta: '2018-08-31'
lang: en-US
title: Membranes, motors, and molecular modeling
...



 In 1953 Stanley Miller mixed methane, ammonia, and hydrogen in glass tubes. 
 A flask with heated water and one with electrodes connected the tubes, and when a spark of electricity bolted across the electrodes, the apparatus produced amino acids, the building blocks of all proteins. 
 When I first heard about this experiment in high school, I was attracted to its simplicity and elegance. 
 Now, I recognize that it's explanatory power originates in the novelty of looking at a seemingly impenetrable question---the origin of life---from a new perspective. 
 I am looking for a research environment where disciplines are combined to tackle problems on the boundary of biological and medical science.

My research interests center on uncovering the physical principles that underlie biological and chemical phenomena. 
I try to create more accurate molecular simulations by improving physics-based force fields and combining new simulation procedures with nonequilibrium analytical tools.
I will extend my previous work on biological membranes to elucidate driving forces behind the formation of membrane domains featuring phosphoinositides.
I will also run simulations of synthetic molecular motors, such as those designed by Ben Feringa, to characterize their mechanical properties.
Finally, I will participate in a systematic overhaul of force field science, changing the way force fields are built and how they are distributed, by focusing on transparent and rigorous optimization criteria, in an open setting.
These investigations will provide a detailed accounting of the physical principles that are at work in biological systems.
My undergraduate degree in physics combined with my graduate work in biochemistry and biophysics, together with my postdoctoral training in computational chemistry, makes me well suited to this research plan.
Each aim of my detailed research plan focuses on a physical or chemical question at the heart of molecular motion.

# Summary of previous research

## Improving free energy calculations
Accurate binding thermodynamics calculations remain one of the central goals of biomolecular simulations. 
While in the Gilson group, I contributed to an overall evaluation of more than ten different methods, from research groups around the world, used to compute host-guest binding free energies and enthalpies [@BGsUYQln]. 
As part of that work, I extended our own method (attach-pull-release [@uzHaEv9Z]) by completely rewriting the code in Python and adding several advanced features enabling larger and more challenging systems to be used (this code is available on [GitHub](https://www.github.com/slochower/pAPRika)). 
More recently, I have also worked on assessing the efficiency and reproducibility of how different algorithms converge toward free energy estimates (forthcoming publication).

## The evolution of molecular motors
Biological motors are enzymes that use chemical energy to drive directional motion. 
Although motor proteins must have arisen through random mutation and natural selection, it is not clear how the evolutionary leap from non-motor enzymes to molecular motors could have occurred. 
I showed that any chiral molecule driven out of equilibrium should undergo cycles of conformational change [@1BfYw0gk2]. 
This work was highlighted by [UCSD](http://ucsdhealthsciences.tumblr.com/post/173707350285/its-not-intelligent-design-so-how-did) and ["New and Notable"](https://www.cell.com/biophysj/fulltext/S0006-3495(18)30444-2) in Biophysical Journal.

## The design of new force fields
As part of the open force field consortium---a collaboration with Dr. David Mobley, Dr. John Chodera, Dr. Michael Shirts, Dr. Lee-Ping Wang, and Dr. Chris Bayly--- I participated in the effort to build new molecular mechanics force fields based on direct chemical perception instead of indirect, atom-type based approaches (forthcoming publication). 
I have also contributed to the design, coding, and implementation of a new force field format---SMIRKS Native Open Force Field (SMIRNOFF)---based on a hierarchical structure that supports customized combining rules, partial bond orders, polarizability, and other advanced features. 
The tools and data are open source and available on [GitHub](https://github.com/openforcefield).

## Simulations of complex membranes
Continuing the work that I started during graduate school at the University of Pennsylvania [@1G0A01ZNq; @SdO7fVnR; @Ag1rh6TA; @1E1rz4J4o; @1AHXI1BtY], I'm interested in simulating increasingly complex, and thus more physiologically relevant, models of biological membranes. 
We recently reported (forthcoming publication) how the interplay between lipid species, cholesterol, counterions, and water near the membrane interface can lead to the formation of nano-scale lipid clusters. 
A natural next step is to understand the role proteins play in stabilizing these clusters, as discussed below.

# Detailed research plan

## How are highly enriched clusters of negatively charged phospholipids stabilized?

Phosphoinositides are a minor class of lipids located on the inner leaflet of the plasma membrane, found at about 0.5 mole percent of all phospholipids in mammalian cells (10-100 μM), that have an outsized biological role.
This class of lipids participates in myriad cell processes including attachment of the cytoskeleton, membrane fusion, vesiculation, and both activation and inhibition of enzymes [@GGlssBvj].
Disruption in signaling pathways associated with the phosphoinositides have been implicated in several cancers as well as Charcot-Marie-Tooth disease along with other neurodegenerative disorders [@8Xw2kuUO; @12CAxA8dE; @l2gqdgv; @izLqFTEH; @1HRoQaadQ; @1DCzqvykg].
Among all phospholipids, PtdIns(4,5)*P*~2~ may be the most common regulatory lipid: hundreds of cytosolic proteins have been found to bind PtdIns(4,5)*P*~2~ in vitro [@uyKE7bWV] including proteins that cause or sense membrane curvature [@3EmJ4esY; @5PUA7pLD].

PtdIns(4,5)*P*~2~ is one of the most highly charged molecules in the cell, carrying a net charge from -3 to -5 at physiological pH, owing to a phosphodinoester and two phosphomonoester groups [@8pFCG7HG].
Despite their high charge, through the use of super-resolution microscopy, there is mounting evidence for nano-scale clusters of PtdIns(4,5)*P*~2~ within cells. 
In neuronal cells, clusters of PtdIns(4,5)*P*~2~ have been visualized using fluorescent phosphoinositide-binding domains and phosphoinositide-specific antibodies [@U2YHSNKE.; @Gw4f4Ayu].
These clusters are circular, roughly 70--90 nm in diameter, and composed of greater than 80% PtdIns(4,5)*P*~2~. 
A separate study found clusters of around 60 nm for PtdIns(4,5)*P*~2~, and larger clusters for PtdIns(3,4,5)*P*~3~, in the plasma membrane [@rvpDeSHJ]. 
Even in the absence of proteins, *in vitro* assays in the Janmey group have demonstrated PtdIns(4,5)*P*~2~ clusters of 40--50 nm, by AFM and TEM imaging, after the addition of as little as ~1  μM Ca^2+^[@LhOwGz4k].
Another study using fluorescence self-quenching and Förster resonance energy transfer assays noted PtdIns(4,5)*P*~2~ self association at concentrations as low as 0.05 mole percent, with divalent and trivalent metal ions, in model membranes and liposomes [@ior8wlwH].

### How do divalent cations grow and stabilize clusters?
The finite and well-defined size of PtdIns(4,5)*P*~2~ clusters suggests there is a balance between the mutual electrostatic and steric repulsion of the negatively charged lipids and the attraction mediated by Ca^2+^.
A key piece of evidence is the observation from molecular dynamics simulations that a single Ca^2+^ ion is able to bring together groupings of up to three lipids and lead to changes in membrane packing (as detailed in a publication currently under review).
In simulations, we find that only Ca^2+^ has the ability to nucleate clusters; in experiments, clusters are detected only at higher concentrations of Mg^2+^ and not at all with the monovalent ions Na^+^ or K^+^ [@JWXdIfNt]. 

Building upon an automated toolchain for constructing heterogeneous membrane compositions for molecular simulations [@14RTQvTQS; @aHkuGDrS], I will construct and run simulations of PtdIns(4,5)*P*~2~ clusters.
As in my previous work, I will test several variables independently by varying the counterion species, counterion concentration, and presence or absence of proteins.

### What are the physical properties of the clusters?
That the clusters so far visualized in experiments are round suggests the domains are fluid, rather than crystalline.
I am going to test the hypothesis that PtdIns(4,5)*P*~2~ clusters increase the height of the membrane, are more laterally stiff, and display curvature.

### How does the ability of PtdIns(4,5)*P*~2~ to bind proteins change when it is present in a cluster?
I am going to test the hypothesis that PtdIns(4,5)*P*~2~ clusters can form even in the absence of proteins.


## What are the mechanical properties of synthetic molecular motors?
The ability of light-driven molecular motors to switch between two or more states makes them suitable for new forms of optical data storage [@18PGyWtWV], as "wheels" on nano-scale cars [@OAnfwOYX], trains [@10MPrT2Vf], worms [@Tels98bO], and walkers [@SfUEsk0e], or in new forms of responsive materials [@jCuccJLJ].
Unlike switches, whose work is reversed after every full cycle, molecular motors can be used to progressively move systems away from thermodynamic equilibrium [@1H5r7SBir].
The synthetic molecular motors of Ben Fergina operate by converting light and heat into directional rotary motion.
These motors belong to a class of molecules called overcrowded alkenes, with two stable enantiomers, and adopt a helical shape due to steric strain around the central double bond.
The two sets of conjugated rings rotate relative to each other, with the central bond acting as an axle, and for simplicity, one set of rings is designated the "stator" while the other set is called the "rotor."
The directional motion of these molecules can be analyzed in terms of two degrees of freedom: $E$ to $Z$ for the isomerization of the double bond (analogous to *cis* and *trans*) and $P$ and $M$ for the overall twist or helicity of the molecule (Figure @fig:motor-diagram). 

![The two degrees of freedom in a synthetic molecular motor.](images/motor.png){#fig:motor-diagram}

### Calculate the speed, torque, and efficiency of motors
In 2006, it was shown that light driven molecular motors can rotate a glass rod that is more than 10,000 times their size upon irradiation with light and when included as a dopant in a liquid crystal film [@thFGBz32].
While it is clear that artificial motors, when aligned appropriately so their individual effects are magnified, can produce macroscopic effects, it is not known how much force an individual molecular motor can generate. 
I will use the nonequilibrium model I developed to quantify directional motion in biological motors with these artificial molecular motors.
 I will focus on the “second generation” class of motors from Ben Feringa and colleagues, which possess symmetric stators that enable easier functionalization, and a lower energy cost for the thermal helix inversion step.
 I will study the four ground states that comprise the 360 degree cycle depicted in Figure @fig:motors.
 On the left, the four structural states of the motor demonstrate movement of the upper rotor relative to the fixed stator through two photochemical and two thermal steps.
 On the right, the free energy profiles along a given surface $E$ or $Z$ represent the pattern of energy troughs and barriers for changing the helicity of the structure while maintaining the same orientation of the double bond, essentially sliding the bulky biaryl rings connected to the rotor past the stator.
 This barrier can be considerable, on the order of tens to hundreds of kcal/mol, depending on the chemical groups attached to the rotor.
 Each ground state can have a half life of months to years at room temperature [@1H5r7SBir].
 The excited state structures and dynamics are considerably more complex and, based on preliminary work in the Gilson group, are difficult to converge.

 ![On the left, the four ground state conformations of a second generation motor, adapted from Štacko et al[@mKSNFvW7]. On the right, the same four states placed on free energy profiles. The energy profiles are periodic, with two cycles shown for both isomerization state. A clone of the lower $E$ energy surface is shown above, for clarity, to demonstrate the progression from state 4 to state 1 requires energy.](images/offset-barriers.pdf){#fig:motors width=970px height=321.34px}
 
 To run the nonequilibrium model, we need to know the shape of the energy surfaces and the rate constants for moving between and along each surface. 
 The free energy profiles along a given surface represent the energy barrier for the changing the helicity of the structure while maintaining the same orientation of the double bond. 
 Previously we used microsecond-scale molecular dynamics simulations to determine the energy landscapes based on equilibrium population distributions.
 However, because the barriers here are expected to be much larger, I will directly probe the potential surfaces by evaluating the energy of conformations for different values of the central dihedral angle.
 I will perform this dihedral scan using a quantum chemistry package, such as [Psi4](http://psicode.org/) using density functional theory and semi-empirical methods.
 B3LYP calculations with the 6-31G* basis set were used to optimize the geometry of a related motor and then subjected to surface scanning using PM3 semi-empirical methods [@N6pRFM85].
 I will begin using those methods and move to higher level basis sets and higher levels of theory if necessary.
 I will test the sensitivity of these results to different quantum methods.

I expect there to be a small but nonzero energy gap between the surfaces due to the chirality of the molecule.
Although the motion from $3 \rightarrow 4$ is the reverse of $1 \rightarrow 2$, there are small differences in the maximum wavelength used to achieve the transformations.
A difference in the relative stability of each isomer has also been detected through proton NMR.
The quantum calculations will reveal the difference between the two conformers for a specific helicity, and this will be used to offset the surfaces in the nonequilibrium model.

### How can we design better molecular motors?
As demonstrated by Richard Feynman in a lecture on Brownian ratchets, the challenge of designing molecular motors is not how to create motion, but how to control the directionality of the omnipresent motion on the molecular scale [@10FsKpWBI].
This is the so-called “gating" of stochastic motion[@qhUBHBOM].
In my previous work [@1BfYw0gk2], I showed that the gating can arise purely from the complementary shape of two potential energy surfaces, whereby an unpassable barrier on one surface can be bypassed through motion on the other surface (see Figure S6, in particular.)
In this section, I will explore the relationship between the shape of the potential energy surfaces the directionality of artificial molecular motors.

I will begin using steepest descent and gradient based methods to optimize the potential energy surfaces to yield the maximal directional flux and maximum torque generated.
If those methods fail, I will use a method that does not rely on the gradient, such as constrained optimization by linear approximation (COBYLA).
The surfaces will be modeled as splines with six to eight control points evenly spaced out along the periodic degree of freedom and the spline points will be allowed to move as the optimization procedure runs. 
Based on preliminary work using analytical functions as the potential energy surfaces, this procedure affords ample room to significantly change the properties of the surfaces. 
Indeed, some perturbations have reversed the flux on a given surface. 

I will combine this information with knowledge of how different chemical constituents affect overall rotation rates to suggest new designs for synthetic motors.

## Can we build a truly open force field?
In this aim, I test the hypothesis that all-atom molecular dynamics force fields for small molecules (e.g., the general AMBER force field, GAFF[@YmRgHfeU]) can be improved by incorporating host-guest binding data in their parameterization. 
Many small molecule force fields have been parameterized against the properties of pure liquids, such as heats of vaporization and density.
Although force fields such as GAFF are able to reproduce some equilibrium thermodynamic properties well, they have notable failures [@HlBr7NrU] and perform only moderately well for predicting binding free energies and enthalpies [@HVgz5rZq].

### Incorporate host-guest binding data into force field development

- APR diagram with workflow.

We will also investigate end-state methods, such as interaction entropy

The partial derivatives can be used to linearly extrapolate.

Cyclodextrins only have three functional groups, but through selective syntehsis, we can test more.

$$
\text{ROI} = \frac{\partial (\partial G_\text{SEM})}{\partial (dU/d\lambda_\text{SEM})} \frac{\partial (dU/d\lambda_\text{SEM})}{\partial N_\text{frames}}
$$ {#eq:roi}

Equation @eq:roi is the return on investment.

### Integrate automated optimization techniques, such as ForceBalance, with host-guest binding data

ForceBalance [@8Q2gLatV; @JFWYe0Pp]. 


# Notes
<font color="red">
- Do we have to explain the nonequilibrium model completely?
Concerns

Too much from Mudong?
Too much from Niel and/or Mobley?
Introduction okay? Too mawkish?

I know there's something wrong the diagram, but I'm not sure what I want to show or how to fix it. I need to somehow show that the vertical axis is some "pseudo" energy -- the heights along $x$ axis are supposed to barriers, but the isomer states themselves don't increase in energy.

- Diffusion is very slow.
- Induction of pores or local regions of high curvature.
- What is the Gaussian curvature?
- What is the modulus of elasticity?
- What is the equivalent radius of curvature?
- Match AFM or scattering experiments.
- Saffron-Delbruk model of diffusion.

The results can be compared to AFM, IR, neutron scattering, or other biophysical experiments on membranes.
As I reported previously, the angle between the head group and the surface of the membrane affects the lipid's ability to bind proteins.

The thermodynamic and kinetic properties of molecular motors depend on the chemical substituents of the rotor and the stator.
Chemical modification of the two rings connected by a double bond affects the racemization barrier of several kcal/mol, by changing the interatomic distance between the rings and therefore, also increasing or decreasing the steric hindrance [@2eTPSj9q].
The rotation rate of molecular motors can vary from seconds to milliseconds [@Sjg8ym5x].
Gravity and inertia are irrelevant, but viscosity and Brownian motion are dominant.

AJDLFK;JASL;KDFJ;ASLFJL;KSADJFLJ
</font>

# References {.page_break_before .unnumbered}

<!-- Explicitly insert bibliography here -->
<div id="refs", custom-style="References"></div>
