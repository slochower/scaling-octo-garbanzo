---
author-meta:
- David R. Slochower
date-meta: '2018-09-28'
lang: en-US
title: Membranes, Motors, and Molecular Modeling
...



The interface between physics and biology is an active, growing area of science with many opportunities and unanswered questions.
I plan to focus on three areas that bridge theory, modeling, and simulations.
My research program will investigate the physical principles that underlie biological and chemical phenomena, providing new insight into the complex behavior of cell membranes and the operation and design of molecular motors.
In parallel, I will develop advanced simulation technologies to compute binding free energies and improve force fields, continuing my commitment to open source software and open access science.

\textcolor{blue}{\textbf{Insert university-specific paragraph here.}}

## Use simulations to understand lipid dynamics in cell membranes
*The goal of this aim is to characterize
lipid-lipid interactions and the physical mechanisms that drive and stabilize lateral segregation of lipid species.*

The primary function of a membrane is to separate what is outside from what is inside, yet cell membranes are extremely dynamic: they act as scaffolds for the generation of second messengers, as the attachment point for the cytoskeleton, and form highly curved geometries during vesicle fusion and fission, among myriad other functions.
Mammalian plasma membranes are a rich mixture of hundreds of types of phospholipids intermingled with other types of lipids, sterols, and proteins.
Continuum models have shed light on membrane topology and geometry, but they are not well suited to capture the intracacies of lipid-lipid interactions [@w5pYOl69], and until recently [@1Dvbhukpz], most simulations have incorporated only a few lipid types, notwithstanding the tremendous diversity present in cell membranes.

![An example of a curved membrane with many different lipid species, colored separately, representative of the systems I will simulate.](images/membrane-vmd.png){#fig:membrane-setup .figure wwidth=2.5in wpos=R}
 
Despite advances in super-resolution microscopy, such as PALM [@mNNsAL8U] and STORM [@12fkuxySq], *in vivo* characterization of membrane heterogeneity remains challenging due to the high spatiotemporal resolution required to study fluctuating nanoscale assemblies of lipids and proteins in living cells and the need to chemically modify the lipids or bind them to ligands in order to visualize them or detect their motions and conformations by spectroscopy. 
However, a variety of indirect experimental techniques, often using fluorescently labeled lipid analogs, have characterized the existence of sub-micron sized domains in living cells and plasma membrane extracts [@GGtK2c0N; @1Eg1Hzju1; @oBaB5Z87; @BzP79Vj9; @aiu6Tmil].
Even in the absence of proteins or chemical modifications, *in vitro* assays in the Janmey group have demonstrated clusters of negatively charged phospholipids of on the order of 50 nm after the addition of as little as 1 μM Ca^2+^ [@LhOwGz4k].

My approach is to understand what conditions promote cluster formation and how the behavior of lipids in clusters differs from bulk. 
I will initially focus on delineating the nucleation of cation-induced clusters of anionic phospholipids. 
This work will involve extending the methods I developed to investigate single molecule QM/MM and all-atom nanoscale simulations. 
In those simulations, I found that Ca^2+^ can act as "molecular glue," forming aggregates of three lipids that remain together for at least 100 ns, much longer than other ion-lipid bond lifetimes. 
Extending beyond the all-atom simulations, I will use the [methods](https://github.com/biophyscode) we created to construct and equilibrate multi-component membrane systems to build models containing rich mixtures of phospholipids (Figure @fig:membrane-setup), going past typical two or three-component systems that are frequently used.

The finite and well-defined size of the experimentally-characterized domains suggests there is a balance between the mutual electrostatic and steric repulsion of negatively charged lipids and attraction mediated by counterions. 
I will monitor the extent of phase separation and demixing in simulations containing combinations of physiological divalent and monovalent ions with varying fractions of charged and uncharged lipids. 
The calculated diffusion coefficient inside the clusters can be compared with values obtained using fluorescence correlation spectroscopy (FCS) and spot variant FCS [@oBaB5Z87].
Simple, physical models based primarily on electrostatics [@10CqL9t0a] predict continual growth of clusters in the presence of excess counterions, yet *in vivo* clusters plateau at a stable size.
Taking advantage of multiscale techniques, including all-atom and coarse-grained simulations using GPU-accelerated molecular dynamics, I will be able to study the growth and merging of clusters on the biologically-relevant microsecond to millisecond timescale. 
The size and shape of the simulated clusters will be contrasted with those seen with AFM imaging and electron microscopy [@LhOwGz4k].

Experiments pulling thin membrane tethers have shown that phase-separated phospholipid domains form precisely at the junction of highly curved regions [@XIltXoGI], implying a relationship between membrane morphology and lipid sorting.
Free energy methods, such as those detailed in the [third aim](#build-advanced-technologies-to-perform-free-energy-calculations-for-drug-design) of this proposal, can be impose a given curvature on a region and measure the energy required to do so.
The bending modulus and mean curvature of simulated clusters will be compared with data from pipette aspiration of membrane tubules [@XIltXoGI; @oBaB5Z87; @aiu6Tmil], and the order parameter of lipids inside the cluster can be contrasted with complementary non-fluorescent methods, such as  EPR, NMR, and neutron scattering. 

![An illustration of stereospecific recognition of phospholipids by proteins.](images/stereospecific.png){#fig:stereospecific .figure wwidth=2in wpos=L}

In the second phase of this project, I will study whether being in a cluster alters the ability of certain lipids to perform their biological roles. 
Many of the lipids implicated in cluster formation, such as PtdIns(4,5)*P*~2~, have been shown to bind hundreds of proteins [@uyKE7bWV], and several integral membrane proteins have been shown to partition into lipid raft-like domains [@2TfZ4zWV].
In some cases, PtdIns(4,5)*P*~2~ binds protein pockets in a highly stereospecific manner (e.g., PtdIns(4,5)*P*~2~ may bind tightly but the closely related isomers PtdIns(3,4)*P*~2~ and PtdIns(3,5)*P*~2~ may not bind at all) requiring a fully extended and accessible head group (Figure @fig:stereospecific). 
In order to evaluate the biological consequences of clustering, I will run simulations containing proteins that bind through either non-specific, electrostatic attraction (e.g., N-WASP and gelsolin) or through tight coordination (e.g., the PH domain of PLCδ). 
Whether these proteins bind “free” lipid molecules as well as they bind clustered ones will be tested using enhanced sampling methods.

I expect the outcome of studying lipid sorting and segregation to be especially helpful for understanding how the accumulation of membrane comopnents is coupled to the many dynamic biological roles of the plasma membrane.
Furthermore, I anticipate the results in the second phase could provide quantitative insights for pore-formation in cell membranes by toxins and cationic surfactants, the activation of integral ion channels and GPCRs by certain lipids, and the energetics of membrane fusion, fission and other buckling geometries.

## Develop design principles for synthetic molecular motors
*The proposed research will investigate current molecular motors and suggest new scaffolds for future nanomachines.*

![The two degrees of freedom in a synthetic molecular motor.](images/motor.png){#fig:motor-diagram .figure wwidth=2in wpos=L}

As demonstrated by Richard Feynman in a lecture on Brownian ratchets, the challenge of designing molecular motors is not how to create movement, but how to control the directionality of the omnipresent -- and random -- motion on the molecular scale [@10FsKpWBI].
Non-protein synthetic molecules can be used to drive molecular motion and have been employed as "wheels" on nano-scale cars [@OAnfwOYX], trains [@10MPrT2Vf], worms [@Tels98bO], and walkers [@SfUEsk0e], or in new forms of responsive materials [@jCuccJLJ].
Yet, the design of these machines has mostly consisted of trial and error and it is not clear *a priori* how chemically modifying their scaffolds affects their functioning  [@1H5r7SBir].

One the most well-studied groups of molecular machines is the “second generation” rotary motors from Ben Feringa and colleagues [@FwAqK1Dt].
These overcrowded alkenes have two stable enantiomers, and adopt a helical shape due to the steric strain around the central double bond (Figure @fig:motor-diagram).
Upon irradiation with light and the application of heat, the two sets of conjugated rings rotate relative to each other, with the central bond acting as an axle, and for simplicity, one set of rings is designated the "stator" while the other set is called the "rotor."
The directional motion of these molecules can be analyzed in terms of two degrees of freedom: $E$ to $Z$ for the isomerization of the double bond (analogous to *cis* and *trans*) and $P$ and $M$ for the overall twist or helicity of the molecule.

Considerable effort has been spent using advanced quantum mechanical modeling to investigate the photochemical excitation and the dynamics of the excited state [@so4s7d25; @N6pRFM85].
However, those insights have not been combined with the statistical mechanics of the four ground states that comprise the 360$^\circ$ cycle of the motor (Figure @fig:motors, left side).
My approach to modeling involves adapting the nonequilibrium method I developed to analyze directional motion in biological motors. 
The ground state structures can be mapped onto discretized potential energy surfaces (PES) for each isomerization state, that will be determined evaluating the ground state energy of the motor as a function of the central dihedral angle (Figure @fig:motors, right side).
A Markov matrix encodes the rates of moving between and along bins on each PES, and the eigenvectors of this matrix characterize the steady state probability flux that quantifies the extent of directional motion.
From this, I can determine the maximum speed and the maximum power that can be produced by individual motors.

![On the left, the four ground state conformations of a second generation motor, adapted from Štacko et al[@mKSNFvW7]. On the right, the same four states placed on free energy profiles. The energy profiles are periodic, with two cycles shown for either isomerization state. A clone of the lower $E$ energy surface is shown above, for clarity, to demonstrate the progression from state 4 to state 1 requires energy.](images/offset-barriers.png){#fig:motors width=100%}

 ![Functional group additions can have a large effect on overall rotation rates (redrawn from [@gimGEnwq]).](images/Feringa-R-with-table.png){#fig:feringa-r .figure wwidth=2in wpos=R}

This group of molecules is perhaps the most well-studied and well-characterized class of motors.
Over the past decade, there have been many designs for rotary motors (reviewed by Kassem et al.[@1H5r7SBir]), and it has become clear that the chemical constituents on both the rotor and the stator affect motor operation [@MVPWALSk] (Figure @fig:feringa-r).
Reducing the bulkiness of the rotor can speed up the overall rotation rate of the motor, but can also lead to the loss of directionality [@1F5wsgY82].
It is also possible to alter the quantum yield of the photochemical step by adding electron withdrawing or electron donating groups, polarizing the molecule and lengthening the central double bond [@Ewc7FKL8; @122TltEto].
Yet, to date there is no underlying theory that can be leveraged to aid the creation of new motors.

By systematically studying how the addition of chemical moieties affects the $E$ and $Z$ PES of the motors, the relationship between the chemical makeup of the rotor and stator and the strength of directional motion will become clear.
The understanding gained from this analysis can be used to suggest new avenues in chemical space to create rotors geared for a particular purpose.
For example, in some instances it may be desirable to have motors that rotate slowly but provide a tremendous amount of torque (e.g., for using nanoscale motors to transport macroscopic objects) while in other circumstances, it may be more beneficial to have motors that rotate as quickly as possible (e.g., for using motors to rapidly switch the surface properties of a particular material). 
The results of this research will provide a fundamental understanding of the principles underlying motor operation and open up rational design for molecular rotors, pumps, transporters, and other nanorobotics.

## Build advanced technologies to perform free energy calculations for drug design
*The proposed research in this aim will advance quantitative methods for free energy calculations and incorporate binding thermodynamics into a community-driven open access force field effort.*

Designing ligands that bind their target with high affinity and specificity is one objective of small-molecule drug discovery, yet hit-to-lead and lead-optimization can take upwards of three years owing to the fact it is often necessary to synthesize hundreds or thousands of new compounds.
Drug discovery is very expensive and often fails.
In recent years, the pharmaceutical industry has begun to use absolute and relative binding free energy calculations to help narrow the number of compounds that must be synthesized [@1FiDpP1LR; @1BwXH3GFO].
In particular, the advent of computational calorimetry has enabled quantitative and high-precision comparisons of binding free energies, enthalpies, and entropies (by subtraction) with experimental values determined by isothermal titration calorimetry or NMR [@1935a9V0d].
The root mean squared error associated with such calculations is several kcal/mol [@LWd10vQy], and even a modest improvement of the prediction accuracy by 1 kcal/mol would lead to a substantial decrease in the number of compounds that must be manually synthesized and tested [@fC0t6Cy1].
The first goal of this aim is to create better tools for estimating protein-ligand binding constants.

 ![An example host-guest system, $\alpha$-cyclodextrin with cyclooctanol (unbound) showing the pulling coordinate along the $z$ axis.](images/APR-annotated.png){#fig:apr .figure wwidth=3in wpos=L}

Host-guest systems, nonconvalent complexes between a cavity-containing host and a small molecule guest, have emerged as a powerful tool for evaluating free energy algorithms.
The attach-pull-release (APR) method has consistently been ranked among the most accurate techniques for predicting binding thermodynamics host-guest complexes in blind challenges [@BGsUYQln; @GA1AFcUw]. 
In APR, the reversible work of transferring the guest from the binding site to solution, via a physical pathway, is computed using a series of umbrella sampling windows (Figure @fig:apr).
In the “attach” phase, restraints are connected to the guest (and optionally, to the host for better conformational sampling) through a parameter $\lambda \in [0, 1]$ that controls the strength of the restraints.
During the “pull” phase, the equilibrium length of a distance restraint joining the guest and host is increased until the guest is no longer interacting with the host molecule. 
The “release” phase reverses the work of attaching the restraints and also corrects the concentration of the guest molecule to standard state.
Simulating each window and integrating over the partial derivative of the restraint energy with respect to the restraint target, we can generate a potential of mean force along the pulling coordinate that is used to compute the binding free energy at standard state, $\Delta G^\circ$.

I will independently continue the development of APR, and its Python interface that I created -- called pAPRika -- by transforming it into a generalized tool that is capable of computing free energies along any physical pathway, using either AMBER or the open source OpenMM as simulation packages.
The core functionality of pAPRika is already being used by research groups across the country and in at least one group in China.
An important milestone is adapting pAPRika for the efficient computation of protein-ligand binding free energies.
One advantage of APR is a complete thermodynamic description of binding ($\Delta G^\circ$, $\Delta H$, and $-T \Delta S$) that are all absolute quantities for any protein-ligand pair instead of relative $\Delta G$ values along some chosen route of successive alchemical modifications that would be obtained through free energy perturbation methods.
Due to the much larger size of proteins compared to host-guest complexes, the increased fluctuations in potential energy make $\Delta G^\circ$ much harder to converge.
A key step will be adding the ability to automatically allocate resources, by calculating the "return on investment" (ROI) in each window that reports how extra sampling in any $\lambda$ state affects the standard error of the mean binding affinity.
Efficient APR calculations are well suited to predict which ligands, among a series of potentially unrelated scaffolds and structures, will bind most tightly to a protein target, such as during virtual screening.

Even when results are well-converged, the accuracy of a free energy simulations is necessarily limited by the accuracy of the force field it uses. 
Most established small molecule force fields (e.g., the general AMBER force field, GAFF) have been tuned using pure liquid state data, such as the average density, enthalpy of vaporization, or the self-diffusion coefficient.
Over the past decade, it has become clear that reproducing those properties well does not guarantee binding thermodynamics at a level acceptable for guiding experiments.
The open force field group (OpenFF) is an academic collaboration that aims to develop new force fields using open access methods, open source software, and high-quality open data sets.
One central difference with the OpenFF group is the use of direct chemical perception to apply force field parameters based on a molecular graph instead of atom types[@HlBr7NrU], and the desire to avoid over-fitting parameters by making Monte Carlo moves in parameter space to find the fewest number of parameters required to describe a set of chemistries [@13lTSBgHy].
The first prototype force field from this effort was release in June 2018, called SMIRNOFF99Frosst v0.1, based on a predecessor of GAFF.
SMIRNOFF99Frosst is able to perform as well as GAFF, and in some cases, alleviate conformational problems caused by GAFF's atom types, in only 335 parameter lines compared to the 6794 lines in GAFF version 2.1. 
Beyond this initial release, multiple generations of SMIRNOFF-based force fields are planned, incorporating new forms of Lennard-Jones interactions, the addition of atom polarizabilities, and Bayesian estimates to quantify systematic errors in the force field.

![A comparison of binding free energies between SMIRNOFF99Frosst and GAFF v1.7 for a series of cyclodextrin hosts and guests (unpublished results). Points are colored according to guest functional group.](images/SMIRNOFF-vs-GAFF-deltaG.png){#fig:smirnoff .figure wwidth=3in wpos=R}

As a member of the OpenFF consortium, I am responsible for benchmarking new iterations of SMIRNOFF-family force fields using host-guest thermodynamics computed by pAPRika.
Figure @fig:smirnoff shows the very first comparison of SMIRNOFF99Frosst v0.1 and GAFF v1.7 on host-guest systems.
GAFF v1.7 is known to overestimate binding affinities by >1 kcal/mol[@HVgz5rZq], and it appears that SMIRNOFF99Frosst reduces this tendency.
To begin, I will use the "[benchmark set](https://escholarship.org/uc/item/9p37m6bq)" of Mobley et al.[@12BD3oHp4].
There, experimental data are available for rigid curcurbituril and highly flexible cyclodextrin hosts with a variety of drug-like guest molecules. 
When available, I plan to incorporate the binding data resulting from selective derivatization of cyclodextrins designed to evaluate specific functional group interactions [@13gqBX78S].
pAPRika makes it easy to match the simulations to the experimental conditions, including host and guest concentration, stoichiometry, ion concentration, and buffer conditions.

To include pAPRika calculations in the creation of new force fields, I will leverage the ForceBalance framework of Wang et al.[@JFWYe0Pp]
ForceBalance uses thermodynamic fluctuation formulas and reference data (e.g., *ab initio* quantum mechanical calculations and experimentally known molecular or bulk properties) to optimize an objective function, such as the sum of squared differences between the calculated and reference values.
I will extend my collaboration with Dr. Lee-Ping Wang and integrate pAPRika binding free energy calculations into the optimization loop of ForceBalance. 
Enthalpies are poorly correlated with free energies, and thus, they represent a nearly independent set of data to compare. 
I have experience working with the analytic derivatives of the binding free energy with respect to Lennard-Jones parameters [@xRauI5mb], and using these derivatives to tune parameters was recently used by a colleague to optimize the TIP3P water model for binding calculations by post-processing existing MD trajectories for small parameter perturbation [@NeqIQDLp].

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