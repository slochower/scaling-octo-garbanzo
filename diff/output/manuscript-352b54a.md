---
author-meta:
- David R. Slochower
date-meta: '2018-09-20'
lang: en-US
title: Membranes, motors, and molecular modeling
...



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

- Our simulations to date have not only yielded an accurate characterization of PtdIns(4,5)*P*~2~ (at the native protonation state and bound to different ions) in a physiologically relevant bilayer environment, but also several important structural and energetic metrics – head group angle, molecular area, solvation in the immediate vicinity of PtdIns(4,5)*P*~2~, and spatial ion distribution functions for the entire bilayer.
- However, I have yet to study clusters of PtdIns(4,5)*P*~2~ and the interactions between PtdIns(4,5)*P*~2~ and proteins, two biologically-relevant components.

### Understand how divalent cations grow and stabilize clusters
The finite and well-defined size of PtdIns(4,5)*P*~2~ clusters suggests there is a balance between the mutual electrostatic and steric repulsion of the negatively charged lipids and the attraction mediated by Ca^2+^.
A key piece of evidence is the observation from molecular dynamics simulations that a single Ca^2+^ ion is able to bring together groupings of up to three lipids and lead to changes in membrane packing (as detailed in a publication currently under review).
In simulations, we find that only Ca^2+^ has the ability to nucleate clusters; in experiments, clusters are detected only at higher concentrations of Mg^2+^ and not at all with the monovalent ions Na^+^ or K^+^ [@JWXdIfNt]. 

Building upon an automated toolchain for constructing heterogeneous membrane compositions for molecular simulations [@14RTQvTQS; @aHkuGDrS], I will construct and run simulations of PtdIns(4,5)*P*~2~ clusters.
As in my previous work, I will test several variables independently by varying the counterion species, counterion concentration, and presence or absence of proteins.

- What is the critical concentration for PtdIns(4,5)*P*~2~ to spontaneously form clusters?
- PtdIns(4,5)*P*~2~ preferentially partitions into the liquid disordered phase.
- As the concentration of Ca2+ in the aqueous phase increases, the gel phase domains increase in size and irregularity; the gel phase domains have excess charge density and repel each other with such energy that they are capable of forming a Wigner lattice (the lowest energy spatial configuration of negatively charged particles in a positive electrostatic potential such that the Coulombic interactions dominate the kinetic energy) [47]. 
- Do PtdIns(4,5)*P*~2~ clusters grow in size over the course of the simulation?
- What happens on the boundary of the cluster? Are certain lipids more likely than others? Where is cholesterol?
- That the clusters so far visualized in experiments are round suggests the domains are fluid, rather than crystalline.
- I am going to test the hypothesis that PtdIns(4,5)*P*~2~ clusters increase the height of the membrane, are more laterally stiff, and display curvature.
- What is the diffusion coefficient inside the cluster?
- Quantify the Gaussian curvature.

### Determine how the ability of PtdIns(4,5)*P*~2~ to bind proteins changes inside a cluster
I am going to test the hypothesis that PtdIns(4,5)*P*~2~ clusters can form even in the absence of proteins, and that the clustered PtdIns(4,5)*P*~2~ has a greater affinity for many proteins.

- It is thought that the different physical properties inside clusters have significant biological effects.
- As many PtdIns(4,5)*P*~2~-binding proteins interact through an unstructured polybasic stretch, their interactions with the membrane depend on its surface potential and are therefore sensitive to the local density of PtdIns(4,5)*P*~2~, which is the most highly charged lipid in the bilayer.
- To stereospecifically bind PtdIns(4,5)*P*~2~, PH domains require a nearly extended form of PtdIns(4,5)*P*~2~ (this can be seen in some crystal structures).
- Actin regulatory proteins bind PtdIns(4,5)*P*~2~ and are likely to respond to changes in PtdIns(4,5)*P*~2~ packing.
- PtdIns(4,5)*P*~2~ clustering is not reduced when actin nucleation is disrupted, suggesting the clusters precede the proteins.
- We will build smaller (40×40 nm^2^) bilayer patches with varying levels of PtdIns(4,5)*P*~2~ concentration (including 0, 4, 10, and 30%) in the “inner” leaflet to study the effects of PtdIns(4,5)*P*~2~ on the protein binding mechanism.
- By studying the binding of polybasic protein domains under varying concentrations, we will characterize the interactions governing the protein binding affinity, and report the molecular mechanism of the PIP2-density dependence of polybasic protein binding.
- Many of the results of this aim can be compared directly to *in vitro* experiments of PtdIns(4,5)*P*~2~ in model membranes and *in vivo* imaging studies along the lines of van den Bogaart.

- Diffusion is very slow.
- Induction of pores or local regions of high curvature.
- What is the Gaussian curvature?
- What is the modulus of elasticity?
- What is the equivalent radius of curvature?
- Match AFM or scattering experiments.
- Saffron-Delbruk model of diffusion.
- The results can be compared to AFM, IR, neutron scattering, or other biophysical experiments on membranes.
- As I reported previously, the angle between the head group and the surface of the membrane affects the lipid's ability to bind proteins.

## What are the mechanical properties of synthetic molecular motors?

![The two degrees of freedom in a synthetic molecular motor.](images/motor.png){#fig:motor-diagram .figure wwidth=2in wpos=L}

The ability of light-driven molecular motors to switch between two or more states makes them suitable for new forms of optical data storage [@18PGyWtWV], as "wheels" on nano-scale cars [@OAnfwOYX], trains [@10MPrT2Vf], worms [@Tels98bO], and walkers [@SfUEsk0e], or in new forms of responsive materials [@jCuccJLJ].
Unlike switches, whose work is reversed after every full cycle, molecular motors can be used to progressively move systems away from thermodynamic equilibrium [@1H5r7SBir].
The synthetic molecular motors of Ben Fergina operate by converting light and heat into directional rotary motion.
These motors belong to a class of molecules called overcrowded alkenes, with two stable enantiomers, and adopt a helical shape due to steric strain around the central double bond.
The two sets of conjugated rings rotate relative to each other, with the central bond acting as an axle, and for simplicity, one set of rings is designated the "stator" while the other set is called the "rotor."
The directional motion of these molecules can be analyzed in terms of two degrees of freedom: $E$ to $Z$ for the isomerization of the double bond (analogous to *cis* and *trans*) and $P$ and $M$ for the overall twist or helicity of the molecule (Figure @fig:motor-diagram). 

### Calculate the speed, torque, and efficiency of motors
In 2006, it was shown that light driven molecular motors can rotate a glass rod that is more than 10,000 times their size upon irradiation with light and when included as a dopant in a liquid crystal film [@thFGBz32].
While it is clear that artificial motors, when aligned appropriately so their individual effects are magnified, can produce macroscopic effects, it is not known how much force an individual molecular motor can generate. 
I will take the nonequilibrium model I developed to quantify directional motion in biological motors to these artificial molecular motors, in a new direction, focusing on the "second generation" class of motors from Ben Feringa and colleagues, which possess chemically symmetric stators and a lower energy for the thermal step.
 I will study the four ground states that comprise the 360$^\circ$ cycle depicted in Figure @fig:motors.
 On the left, the four structural states of the motor demonstrate movement of the upper rotor relative to the fixed stator through two photochemical ($1 \rightarrow 2, 3 \rightarrow 4$) and two thermal steps ($2 \rightarrow 3, 4 \rightarrow 1$).
 On the right, I've sketched illustrative free energy profiles along a given surface $E$ or $Z$; these represent the pattern of energy troughs and barriers for changing the helicity of the structure while maintaining the same orientation of the double bond, essentially sliding the bulky biaryl rings connected to the rotor past the stator.

 ![On the left, the four ground state conformations of a second generation motor, adapted from Štacko et al[@mKSNFvW7]. On the right, the same four states placed on free energy profiles. The energy profiles are periodic, with two cycles shown for both isomerization state. A clone of the lower $E$ energy surface is shown above, for clarity, to demonstrate the progression from state 4 to state 1 requires energy.](images/offset-barriers.png){#fig:motors width=100%}
 
Previously we used microsecond-scale molecular dynamics simulations to determine the energy landscapes based on equilibrium population distributions. 
However, because the barriers here are expected to be much larger, I will directly probe the potential surfaces by evaluating the energy of motor conformations for different values of the central dihedral angle.
I will perform this dihedral scan using a quantum chemistry package, such as [Psi4](http://psicode.org/) with density functional theory and semi-empirical methods.
I will begin with the semi-empirical methods PM3 or AM1 and test the sensitivity of the results to different quantum approaches (e.g., other types of DFT and Hartree-Fock) and basis sets (e.g., 6-31G*).
From the discrete free energy profiles, the rate of bin-to-bin transitions can be deduced, and these are gathered, together with the surface-to-surface transition rates, in a Markov matrix.
Solving for the eigenvectors of the matrix yields the nonequilibrium steady state (NESS) population in each photochemical state of the motor. 
From the NESS, I will calculate the net probability flux for the complete cycle ($1 \rightarrow 1$), as illustrated by the series of purple and orange arrows in Figure @fig:motors, for a given input level of light irradiation. 

### Optimize the design of artificial molecular motors
As demonstrated by Richard Feynman in a lecture on Brownian ratchets, the challenge of designing molecular motors is not how to create movement, but how to control the directionality of the omnipresent -- and random -- motion on the molecular scale [@10FsKpWBI].
This has been referred to as the “gating" of stochastic motion[@qhUBHBOM].
In my previous work [@1BfYw0gk2], I showed that the gating can arise purely from the complementary shape of two potential energy surfaces, whereby an unpassable barrier on one surface can be circumnavigated by motion on the other surface (see Figure S6, in particular.)
In this section, I will explore the relationship between the shape of the potential energy surfaces and the directionality of artificial molecular motors. 
This sub-aim will test the current understanding of motor mechanisms, most of which has been inferred through static structural snapshots and chemical intuition, using design proofs and will open the field of rational design to molecular rotors, pumps, transporters, and other nanorobotics.

It has been empirically determined that adding electron donating and electron withdrawing moieties has the potential to affect the rotation rate of the motor [@1AzLiBVkC].
Polarizing the molecule by placing electron withdrawing and electron donating groups on either end of the central double bond, has the potential to lengthen the effective axle, significantly reducing the barrier for rotation. 
I will numerically optimize the potential energy surfaces that I determine in the previous sub-aim, to yield the maximum directional flux and maximum torque (see Figure @fig:COBYLA for an example). 
The surfaces will be modeled as splines with six to eight control points evenly spaced along the periodic degree of freedom and the spline points will be allowed to move as the optimization procedure runs. 
Based on preliminary work, this procedure affords ample room to significantly change the properties of the surfaces. 
I will couple the understanding that arises from this study with the knowledge of how chemical constituents affect overall rotation rates to suggest new avenues for synthetic motor design.

 ![Example optimization (using the constrained optimization by linear approximation algorithm, COBYLA) of motor surfaces for maximum flux. Later iterations are darker  colors. On the left, the $Z$ surface; in the middle, the $E$ surface; on the right, the net probability flux corresponding to each optimization iteration.](images/COBYLA.png){#fig:COBYLA width=100%}

## Building better force fields for drug discovery using open data and automated optimization

Designing ligands that bind their target with high affinity and specificity is the principal objective of small-molecule drug discovery, yet hit-to-lead and lead-optimization can take upwards of three years owing to the fact it is often necessary to synthesize hundreds or thousands of new compounds.
In short, drug discovery is very expensive and often fails.
In recent years, the pharmaceutical industry has begun to use absolute and relative binding free energy calculations to help narrow the number of compounds that must be synthesized [@1FiDpP1LR; @1BwXH3GFO].
In particular, the advent of computational calorimetry has enabled quantitative and high-precision comparisons of binding free energies, enthalpies, and entropies (by subtraction) with experimental values determined by isothermal titration calorimetry or NMR [@1935a9V0d].
The root mean squared error (RMSE) associated with such calculations is in the range of 1-4 kcal/mol [@LWd10vQy], yet even a modest improvement of the prediction accuracy of ~1 kcal/mol would lead to a substantial decrease in the number of compounds that must be manually screened by nearly an order of magnitude [@fC0t6Cy1].
Although it has been suggested by some that changes in the force field functional form are required, it is clear that there is ample room to improve the accuracy of existing parameters through careful analysis [@LOjcxYqt].
The first goal of this aim is to create better tools to guide early-stage drug discovery by reducing the number of compounds that must be synthesized to find a promising hit that can be carried over into clinical trials.

 ![An example host-guest system, $\alpha$-cyclodextrin with cyclooctanol (unbound) showing the pulling coordinate along the $z$ axis.](images/APR-annotated.png){#fig:apr .figure wwidth=3in wpos=L}

Host-guest systems are noncovalent complexes between a cavity-like host molecule and a small molecule guest.
These systems retain many of the same, strong functional group interactions of protein-ligand systems while being computationally tractable and reaching convergence on a shorter time scale. 
In the attach-pull-release (APR) method, the reversible work of transferring the guest from the binding site to solution, via a physical pathway, is computed using a series of umbrella sampling windows (Figure @fig:apr).
In the “attach” phase, restraints are connected to the guest (and optionally, to the host for better conformational sampling) through a parameter $\lambda \in [0, 1]$ that controls the strength of the restraints.
During the “pull” phase, the equilibrium length of a distance restraint joining the guest and host is increased until the guest is no longer interacting with the host molecule. 
The “release” phase reverses the work of attaching the restraints and also corrects the concentration of the guest molecule to standard state.
Simulating each window and integrating over the partial derivative of the restraint energy with respect to the restraint target, we can generate a potential of mean force along the pulling coordinate that is used to compute the binding free energy at standard state, $\Delta G^\circ$.

### Incorporate host-guest binding data into force field development
APR has consistently been ranked among the most accurate methods for predicting binding thermodynamics in blind challenges [@BGsUYQln; @GA1AFcUw]. 
I will independently continue the development of APR, through its Python interface, pAPRika, and transform it into a generalized tool that is capable of computing free energies along any physical pathway, using either AMBER or OpenMM as simulation packages.
The core functionality of pAPRika is already being used by research groups across the country and in at least one group in China.
Extending pAPRika would allow the same rigorous thermodynamic framework to be used in applications such as protein-protein interactions, dimerization of small molecules, or nucleotide flipping.
As part of the development, I will also investigate the accuracy of non-pathway, end-point methods, such as the direct calculation of interaction entropy [@gRfhPG7N].

Most established small molecule force fields (e.g., the general AMBER force field, GAFF) have been tuned using pure liquid state data, such as the average density, enthalpy of vaporization, or the self-diffusion coefficient.
Over the past decade, it has become clear that reproducing those properties well does not guarantee binding thermodynamics at a level acceptable for guiding experiments.
The open force field group (OpenFF) aims to develop new, collaborative force fields using open access methods, open source software, and high-quality open data sets.
One central difference with the OpenFF group is the use of direct chemical perception to apply force field parameters based on a molecular graph instead of atom types[@HlBr7NrU], and the desire to avoid over-fitting parameters by making Monte Carlo moves in parameter space to find the fewest number of parameters required to describe a set of chemistries [@13lTSBgHy].
The first prototype force field from this effort was release in June 2018, called SMIRNOFF99Frosst v0.1, based on a predecessor of GAFF.
SMIRNOFF99Frosst is able to perform as well as GAFF, and in some cases, alleviate conformational problems caused by GAFF's atom types, in only 335 parameter lines compared to the 6794 lines in GAFF version 2.1. 
Beyond this initial release, multiple generations of SMIRNOFF99Frosst are planned, incorporating new forms of Lennard-Jones interactions, the addition of atom polarizabilities, and Bayesian estimates to quantify systematic errors in the force field.

![A comparison of binding free energies between SMIRNOFF99Frosst and GAFF v1.7 for a series of cyclodextrin hosts and guests (unpublished results). Points are colored according to guest functional group.](images/SMIRNOFF-vs-GAFF-deltaG.png){#fig:smirnoff .figure wwidth=3in wpos=R}

As part of the OpenFF consortium, I will benchmark new iterations of SMIRNOFF99Frosst using host-guest thermodynamics computed by pAPRika.
Figure @fig:smirnoff shows the very first comparison of SMIRNOFF99Frosst v0.1 and GAFF v1.7 on host-guest systems.
GAFF v1.7 is known to overestimate binding affinities by >1 kcal/mol[@HVgz5rZq], and it appears that SMIRNOFF99Frosst reduces this tendency.
To begin, I will use the "[benchmark set](https://escholarship.org/uc/item/9p37m6bq)" of Mobley et al.[@12BD3oHp4].
There, experimental data are available for rigid curcurbituril and highly flexible cyclodextrin hosts with a variety of drug-like guest molecules. 
When available, I will also incorporate the binding data resulting from selective derivatization of cyclodextrins designed to evaluate specific functional group interactions [@13gqBX78S].
Enthalpies are poorly correlated with free energies, and thus, they represent a nearly independent set of data to compare. 
I will match the simulations to the experimental conditions, including host and guest concentration, stoichiometry, ion concentration, and buffer conditions.
I will report metrics such as RMSE, R^2^, Kendall’s τ, and the slope of the correlation between candidate parameter sets and (a) a reference force field such as GAFF, CGenFF, or OPLS3 and (b) the experimental thermodynamic data determined using ITC and NMR. 
The results of my analysis will be reported through [continuous integration](https://travis-ci.org/openforcefield/openforcefield?branch=master), whereby each candidate update to the force field is automatically tested through a clear and well-defined set of tests. 

### Integrate automated optimization techniques, such as ForceBalance, with host-guest binding data

As part of the open force field effort, we need to be able to rapidly and efficiently optimize force field parameters given functional forms and input data. 
ForceBalance is a tool, written by Dr. Lee-Ping Wang, that uses thermodynamic fluctuation formulas and reference data (e.g., *ab initio* quantum mechanical calculations and experimentally known molecular or bulk properties) to optimize an objective function, such as the sum of squared differences between the calculated and reference values
ForceBalance has already been used to optimize water models[@50lAQZra] and protein force fields [@1E3wArY0j]. 
As a member of the OpenFF consortium, Dr. Wang has begun to add support for the SMIRNOFF force field format. 
I will extend my collaboration with Dr. Wang to include pAPRika in the optimization loop of ForceBalance. 
I have experience working with the analytic derivatives of the binding free energy with respect to Lennard-Jones parameters [@xRauI5mb], and using these derivatives to tune parameters was recently used by a colleague to optimize the TIP3P water model for binding calculations by post-processing existing MD trajectories for small parameter perturbation [@NeqIQDLp].

A proximate goal is to create a method for passing a candidate set of parameters from ForceBalance to pAPRika and for pAPRika to return an estimate of the quality of the parameters in machine-readable format, such as JSON or XML. 
The experimental data for ForceBalance will be taken from the free and open [ThermoML](https://www.nist.gov/mml/acmd/trc/thermoml) database curated by NIST. 
I will focus on including data that represent intermolecular interactions, such as enthalpies of mixing and partition coefficients, that will broaden the data used for force field development beyond single species properties. 
Host-guest calculations are computationally expensive, sometimes requiring >1 GPU-day to reach the desired level of convergence, and this has the potential to significantly slow down ForceBalance. 
I will add the ability to automatically allocate resources in the APR calculation, by calculating the return on investment (ROI) in each window. 
The ROI is the partial derivative of the overall standard error of the mean binding affinity with respect to the number of frames in window $i$, $\partial G^\circ_\text{SEM} / \partial N^i_\text{frames}$ . 
This will allow us to simulate each window long enough such that the overall estimate of the binding free energy reaches below a certain threshold. 

Together, these methodological improvements will help create a transparent and robust set of metrics to evaluate the performance of candidate force fields on an equal footing.
By incorporating host-guest binding data, the degeneracy in parameter space will be broken, avoiding force fields that agree excellently with experiment for liquid properties and yet agree poorly on binding.
I believe the ideas in this aim could be turned into an NIH proposal by demonstrating the need to systematically evaluate force field accuracy for protein-ligand binding, perhaps the most important application of this work for human health.

\pagebreak
\setlength{\parskip}{0.1mm}

<!--- 
\setlength{\parindent}{-0.2in}
\setlength{\leftskip}{0.2in}
\setlength{\parskip}{8pt}
https://groups.google.com/forum/#!topic/pandoc-discuss/SUZ08-Kc6Og --->
# References {.page_break_before .unnumbered}
\setstretch{1}

<!-- Explicitly insert bibliography here -->
<div id="refs", custom-style="References"></div>
