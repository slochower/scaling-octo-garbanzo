---
author-meta:
- David R. Slochower
date-meta: '2018-09-11'
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
\color{CornflowerBlue}Each aim of my detailed research plan focuses on a physical or chemical question at the heart of molecular motion.\color{black}

\color{CornflowerBlue}At Carnegie Mellon, I look forward to extending my research on membranes using coarse-grained models,\color{black}


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


## What are the mechanical properties of synthetic molecular motors?
The ability of light-driven molecular motors to switch between two or more states makes them suitable for new forms of optical data storage [@18PGyWtWV], as "wheels" on nano-scale cars [@OAnfwOYX], trains [@10MPrT2Vf], worms [@Tels98bO], and walkers [@SfUEsk0e], or in new forms of responsive materials [@jCuccJLJ].
Unlike switches, whose work is reversed after every full cycle, molecular motors can be used to progressively move systems away from thermodynamic equilibrium [@1H5r7SBir].
The synthetic molecular motors of Ben Fergina operate by converting light and heat into directional rotary motion.
These motors belong to a class of molecules called overcrowded alkenes, with two stable enantiomers, and adopt a helical shape due to steric strain around the central double bond.
The two sets of conjugated rings rotate relative to each other, with the central bond acting as an axle, and for simplicity, one set of rings is designated the "stator" while the other set is called the "rotor."
The directional motion of these molecules can be analyzed in terms of two degrees of freedom: $E$ to $Z$ for the isomerization of the double bond (analogous to *cis* and *trans*) and $P$ and $M$ for the overall twist or helicity of the molecule (Figure @fig:motor-diagram). 


![The two degrees of freedom in a synthetic molecular motor.](images/motor.png){#fig:motor-diagram .figure wwidth=2in wpos=L}


 "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
 "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


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

 ![On the left, the four ground state conformations of a second generation motor, adapted from Štacko et al[@mKSNFvW7]. On the right, the same four states placed on free energy profiles. The energy profiles are periodic, with two cycles shown for both isomerization state. A clone of the lower $E$ energy surface is shown above, for clarity, to demonstrate the progression from state 4 to state 1 requires energy.](images/offset-barriers.png){#fig:motors width=100%}
 
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

### Optimize the design of artificial molecular motors
As demonstrated by Richard Feynman in a lecture on Brownian ratchets, the challenge of designing molecular motors is not how to create motion, but how to control the directionality of the omnipresent motion on the molecular scale [@10FsKpWBI].
This is the so-called “gating" of stochastic motion[@qhUBHBOM].
In my previous work [@1BfYw0gk2], I showed that the gating can arise purely from the complementary shape of two potential energy surfaces, whereby an unpassable barrier on one surface can be bypassed through motion on the other surface (see Figure S6, in particular.)
In this section, I will explore the relationship between the shape of the potential energy surfaces the directionality of artificial molecular motors.

Using numerical methods such as gradient descent and COBYLA (where the derivative of the function is not known or expensive to compute), I will optimize the potential energy surfaces to yield the maximum directional flux and maximum torque generated. 
The surfaces will be modeled as splines with six to eight control points evenly spaced out along the periodic degree of freedom and the spline points will be allowed to move as the optimization procedure runs. 
Based on preliminary work using analytical functions as the potential energy surfaces, this procedure affords ample room to significantly change the properties of the surfaces. Indeed, some perturbations have reversed the flux on a given surface. 

I will begin using steepest descent and gradient based methods to optimize the potential energy surfaces to yield the maximal directional flux and maximum torque generated.
If those methods fail, I will use a method that does not rely on the gradient, such as constrained optimization by linear approximation (COBYLA).
The surfaces will be modeled as splines with six to eight control points evenly spaced out along the periodic degree of freedom and the spline points will be allowed to move as the optimization procedure runs. 
Based on preliminary work using analytical functions as the potential energy surfaces, this procedure affords ample room to significantly change the properties of the surfaces. 
Indeed, some perturbations have reversed the flux on a given surface. 

Next, I will couple my understanding of the surfaces with knowledge of how chemical constituents affect overall rotation rates to suggest new designs for synthetic motors.

## Building better force fields for drug discovery using open data and automated optimization

\color{CornflowerBlue}Designing ligands that bind their target with high affinity and specificity is the principle objective of small-molecule drug discovery, yet hit-to-lead and lead-optimization can take upwards of three years owing to the fact it is often necessary to synthesize hundreds or thousands of new compounds.\color{black}
\color{CornflowerBlue}In short, drug discovery is very expensive and often fails.\color{black}
\color{CornflowerBlue}In recent years, the pharmaceutical industry has begun to use absolute and relative binding free energy calculations to help narrow the number of compounds that must be synthesized [@1FiDpP1LR; @1BwXH3GFO].\color{black}
\color{CornflowerBlue}In particular, the advent of computational calorimetry has enabled quantitative and high-precision comparisons of binding free energies, enthalpies, and entropies (by subtraction) with experimental values determined by isothermal titration calorimetry or NMR [@1935a9V0d].\color{black}
\color{CornflowerBlue}The root mean squared error (RMSE) associated with such calculations is in the range of 1-4 kcal/mol [@LWd10vQy], yet even a modest improvement of the prediction accuracy of ~1 kcal/mol would lead to a substantial decrease in the number of compounds that must be manually screened by nearly an order of magnitude [@fC0t6Cy1].\color{black}
\color{CornflowerBlue}Although it has been suggested that changes in the force field functional form are required, it is clear that significant improvements can be made without introducing new physics [@LOjcxYqt].\color{black}
\color{CornflowerBlue}The first goal of this aim is to create better tools to guide early-stage drug discovery by reducing the number of compounds that must be synthesized to find a promising hit that can be carried over into clinical trials.\color{black}

 ![An example host-guest system, $\alpha$-cyclodextrin with cyclooctanol showing the pulling coordinate along the $z$ axis.](images/APR-annotated.png){#fig:apr .figure wwidth=3in wpos=R}

\color{CornflowerBlue}Host-guest systems are noncovalent complexes between a cavity-like host molecule and a small molecule guest.\color{black}
\color{CornflowerBlue}These systems retain many of the same chemical challenges of protein-ligand systems while being computationally tractable and reaching convergence on a shorter time scale. \color{black}
\color{CornflowerBlue}In the attach-pull-release (APR) method, the reversible work of transferring the guest from the binding site to solution, via a physical pathway, is computed using a series of umbrella sampling windows.\color{black}
\color{CornflowerBlue}In the “attach” phase, restraints are connected to the guest (and optionally, to the host for better conformational sampling) through a parameter $\lambda \in [0, 1]$ that controls the strength of the restraints.\color{black}
\color{CornflowerBlue}During the “pull” phase, the equilibrium length of a distance restraint joining the guest and host is increased until the guest is no longer interacting with the host molecule. \color{black}
\color{CornflowerBlue}The “release” phase reverses the work of attaching the restraints and also corrects the concentration of the guest molecule to standard state.\color{black}
\color{CornflowerBlue}Simulating each window and integrating over the partial derivative of the restraint energy with respect to the restraint target, we can generate a potential of mean force along the pulling coordinate that is used to compute the binding free energy at standard state, $\Delta G^\circ$.\color{black}

### Incorporate host-guest binding data into force field development
\color{CornflowerBlue}APR has consistently been ranked among the most accurate methods for predicting binding thermodynamics in blind challenges [@BGsUYQln; @GA1AFcUw]. I will continue the development of APR, through its Python interface, pAPRika, and turn it into a generalized tool that is capable of computing free energies along any physical pathway, using either AMBER or OpenMM as simulation packages.\color{black}
\color{CornflowerBlue}pAPRika is already being used by research groups across the country and in at least one group in China.\color{black}
\color{CornflowerBlue}Extending pAPRika would allow the same rigorous thermodynamic framework to be used in applications such as protein-protein interactions, dimerization of small molecules, or nucleotide flipping.\color{black}

\color{CornflowerBlue}Most established small molecule force fields (e.g., the general AMBER force field, GAFF) have been tuned using pure liquid state data, such as the average density, enthalpy of vaporization, or the self-diffusion coefficient.\color{black}
\color{CornflowerBlue}Over the past decade, it has become clear that reproducing those properties well does not guarantee binding thermodynamics at a level acceptable for guiding experiments.\color{black}
\color{CornflowerBlue}The open force field group aims to develop new, collaborative force fields using open access methods, open source software, and high-quality open data sets.\color{black}
\color{CornflowerBlue}One major difference is the creation of force fields using direct chemical perception and sampling phase space using Monte Carlo moves.\color{black}
\color{CornflowerBlue}The first prototype force field from this effort was recently realeased, although this was largely based on existing things.\color{black}
\color{CornflowerBlue}As part of the open force field effort, I will benchamrk new iteractions of SMIRNOFF99Frosst using pAPRika.\color{black}
\color{CornflowerBlue}A proximate goal is to allow an easy method for passing new parameter sets to pAPRika and receiving an estimate of the quality of the parameters, in a machine readable form, such as JSON or XML.\color{black}

\color{CornflowerBlue}Data is available for a variety of host molecules, encompassing the rigid (cucurbiturils) to highly flexible (cyclodextrins), which form complexes with a variety of guest molecules, from simple ions to drug-like molecules, in both polar and non-polar solvents. To begin, I will use a set of small molecules with β-cyclodextrin and cucurbiturl hosts from the “benchmark set” of Mobley et al. 45-46. Another benefit of these hosts is their relevance to drug design, as cyclodextrins have been used as drug carriers and are currently undergoing clinical trials. Another strength is that selective synthesis can be used to allow these host guest systems to specifically test functional groups, one by one 47. I will report metrics such as RMSE, R2, Kendall’s τ, and the slope of the correlation between the new force field and (a) a reference force field such as GAFF v1.7 or GAFF v2.1 and (b) the experimental data. \color{black}
\color{CornflowerBlue}Because enthalpies are only poorly correlated with free enrgies, these represent a nearly independent set of data.\color{black}

\color{CornflowerBlue}As part of the benchmarking effort, I will also investigate the accuracy of non-pathway, end-point methods, such as the interaction entropy and hybrid solvent approaches (Niel’s research plan) to elucidate – and make public -- the strengths of weaknesses of the different approaches, and to which systems they may be applicable. Compare them on an equal footing.\color{black}


### Integrate automated optimization techniques, such as ForceBalance, with host-guest binding data

\color{CornflowerBlue}As part of the open force field effort, we need to be able to rapidly and efficiently evaluate force field parameters.\color{black}
\color{CornflowerBlue}ForceBalance, is a tool that uses thermodynamic fluctuation formulas and reference data (e.g., *ab initio* quantum mechanical calculations and experimental values) to etermine the gradient of the parameters.\color{black}
\color{CornflowerBlue}We will extend our collaboration with Dr. Lee-Ping Wang, to interface ForceBalance with pAPRika.\color{black}

\color{CornflowerBlue}The experimental data will be taken from ThermoML.\color{black}

\color{CornflowerBlue}Because binding $\Delta H$ values are not highly correlated with $\Delta G^\circ$, they represent a nearly independent set of observations for the optimization.\color{black}

- We need to rapidly and efficiently test force field parameters.
- ForceBalance is an existing tool that can be used for parameter refinement (and is already in the process of being integrated into the open force field group).
- We will allow ForceBalance to call pAPRika with candidate sets of parameters.
- Given that time will be limited for the APR calculations, we will improve the ability to detect convergence of simulations, dynamically running individual windows.
- The "return on investment" tells us how the standard error of the mean for the overall binding free energy changes as more frames are run in a particular window.
- Together, these methodological improvements will help create a transparent and robust metric for evaluating force field performance and help predict the performance of candidate force fields in drug development.

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
</font>

\pagebreak
\setlength{\parskip}{0.1mm}

<!--- 
\setlength{\parindent}{-0.2in}
\setlength{\leftskip}{0.2in}
\setlength{\parskip}{8pt}
\color{CornflowerBlue}https://groups.google.com/forum/#!topic/pandoc-discuss/SUZ08-Kc6Og --->\color{black}
# References {.page_break_before .unnumbered}
\setstretch{1}

<!-- Explicitly insert bibliography here -->
<div id="refs", custom-style="References"></div>
