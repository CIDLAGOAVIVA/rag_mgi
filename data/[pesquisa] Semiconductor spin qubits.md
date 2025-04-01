## Semiconductor spin qubits

Guido Burkard

Department of Physics, University of Konstanz, D-78457 Konstanz, Germany

Thaddeus D. Ladd and Andrew Pan

HRL Laboratories, LLC, 3011 Malibu Canyon Road, Malibu, California 90265, USA

## John M. Nichol

Department of Physics and Astronomy, University of Rochester, Rochester, New York 14627, USA

## Jason R. Petta

Department of Physics, Princeton University, Princeton, New Jersey 08544, USA, Department of Physics and Astronomy, University of California -Los Angeles, Los Angeles, California 90095, USA,

Center for Quantum Science and Engineering, University of California -Los Angeles, Los Angeles, California 90095, USA, and HRL Laboratories, LLC, 3011 Malibu Canyon Road, Malibu, California 90265, USA

<!-- image -->

(published 14 June 2023; corrected 15 September 2023)

The spin degree of freedom of an electron or a nucleus is one of the most basic properties of nature and functions as an excellent qubit, as it provides a natural two-level system that is insensitive to electric fields, leading to long quantum coherence times. This coherence survives when the spin is isolated and controlled within nanometer-scale, lithographically fabricated semiconductor devices, enabling the existing microelectronics industry to help advance spin qubits into a scalable technology. Driven by the burgeoning field of quantum information science, worldwide efforts have developed semiconductor spin qubits to the point where quantum state preparation, multiqubit coherent control, and single-shot quantum measurement are now routine. The small size, high density, long coherence times, and available industrial infrastructure of these qubits provide a highly competitive candidate for scalable solid-state quantum information processing. Here the physics of semiconductor spin qubits is reviewed, with a focus not only on the early achievements of spin initialization, control, and readout in GaAs quantum dots but also on recent advances in Si and Ge spin qubits, including improved charge control and readout, coupling to other quantum degrees of freedom, and scaling to larger system sizes. First introduced are the four major types of spin qubits: single spin qubits, donor spin qubits, singlet triplet spin qubits, and exchange-only spin qubits. The mesoscopic physics of quantum dots, including single-electron charging, valleys, and spin-orbit coupling, are then reviewed. Next a comprehensive overview of the physics of exchange interactions is given, a crucial resource for singleand two-qubit control in spin qubits. The bulk of the review is centered on the presentation of results from each major spin-qubit type, the present limits of fidelity, and an overview of alternative spin-qubit platforms. A physical description of the impact of noise on semiconductor spin qubits, aided in large part by an introduction to the filter-function formalism, is then given. Last, recent efforts to hybridize spin qubits with superconducting systems, including charge-photon coupling, spin-photon coupling, and long-range cavity-mediated spin-spin interactions, are reviewed. Cavity-based readout approaches are also discussed. The review is intended to give an appreciation for the future prospects of semiconductor spin qubits while highlighting the key advances in mesoscopic physics over the past two decades that underlie the operation of modern quantum-dot and donor spin qubits.

DOI: 10.1103/RevModPhys.95.025003

## CONTENTS

| I. Introduction                                         |   2 |
|---------------------------------------------------------|-----|
| II. Basics of Spin Qubits                               |   4 |
| A. Loss-DiVincenzo (LD) spin qubit                      |   5 |
| B. Donor spin qubits and Kane s proposal '              |   6 |
| C. Singlet triplet (ST 0 and ST /C6 ) qubits            |   6 |
| D. Exchange-only (EO) and resonant-exchange (RX) qubits |   8 |

|                                            |   E. Spin qubits with additional charge degrees of freedom 9 |
|--------------------------------------------|--------------------------------------------------------------|
| III. Mesoscopic Physics of Dots and Donors |                                                            9 |
| A. Quantum confinement                     |                                                            9 |
| 1. Bulk band structure                     |                                                           10 |
| 2. Band structure engineering              |                                                           11 |
| 3. Electrostatic gating                    |                                                           11 |
| B. Electron-electron interactions in QDs   |                                                           12 |
| C. Isolating and detecting single charges  |                                                           13 |

| 14   | C. Applications for readout        |   46 |
|------|------------------------------------|------|
| 16   | D. New avenues of research in cQED |   47 |
| 17   | VIII. Outlook                      |   48 |
| 18   | Acknowledgments                    |   48 |
|      | Appendix: Spin Rotation Gates      |   49 |
| 18   | References                         |   49 |

## I. INTRODUCTION

Quantum computers are fundamentally capable of vastly outperforming all classical computers for a growing list of problems (Feynman, 1982; DiVincenzo, 1995; Ekert and Jozsa, 1996; Shor, 1997; Nielsen and Chuang, 2000; Childs and van Dam, 2010; Montanaro, 2016; Jordan, 2021). To perform a quantum computation, the information to be processed must be represented in a suitable physical form (Landauer, 1991). Semiconductor spin qubits are one platform that has fulfilled the main criteria for the implementation of quantum computation.

The requirements for quantum computation can be stated as follows (DiVincenzo, 1998; DiVincenzo, 2000):

- (1) The elementary units of information need to be stored in a scalable quantum register. In analogy with binary logic where bits take on the value of 0 or 1, quantum information is typically stored in the form of quantum bits (qubits). A qubit is a quantum twolevel system with orthogonal, i.e., distinguishable, basis states j 0 i and j 1 i . Systems with spin 1 = 2 are perhaps the simplest example of this encoding, although other spin-based possibilities exist, as we discuss.
- (2) A further requirement is that the qubits can be prepared in a fiducial state, for example, j 00 … 0 i .
- (3) The quantum system must remain coherent for times much longer than the duration of elementary logic gates since decoherence causes computational errors.
- (4) Along with maintaining coherence, a high-fidelity gate set (single-qubit and two-qubit gates) must be attainable.
- (5) Finally, it is required that a sufficiently large part of the quantum register can be read out at the end of a computation.

37 38 38 38 39 39 40 40 40 41 42 43 44 44 44 45 46 The spin degree of freedom naturally defines a qubit, as spin-up or spin-down in the case of one electron (Loss and DiVincenzo, 1998), or as two distinct nuclear spin states (Kane, 1998). As we show, spin qubits have satisfied the DiVincenzo criteria. Electron spins can be electrically initialized and read out with high fidelity using energy-dependent tunneling or the Pauli exclusion principle (Elzerman et al. , 2004; Petta et al. , 2005). While coupling of the charge to electric fields allows for electrical control of spin states, the small magnetic moment of the electron spin is weakly coupled to the environment, leading to long spin coherence times. Semiconductors may be ideal hosts for solid-state qubits, as materials such as Si can be chemically and isotopically purified to extremely high levels. As Kane (1998) pointed out, ' Because of the advanced state of Si materials technology and the tremendous effort currently underway in Si nanofabrication, Si is the obvious choice for the semiconductor

| D. Zeeman interactions and spin-orbit coupling                                                 | 14    |
|------------------------------------------------------------------------------------------------|-------|
| E. Valleys                                                                                     | 16    |
| F. Hyperfine interactions                                                                      | 17    |
| IV. Spin-Spin Interactions                                                                     | 18    |
| A. Kinetic exchange in the Fermi-Hubbard hopping model                                         | 18    |
| B. Heitler-London and Hund-Mulliken models                                                     | 19    |
| C. Full configuration interaction (FCI) calculations of exchange                               | 20    |
| D. Discussion of theoretical approaches for calculating exchange                               | 20    |
| E. Pauli spin blockade                                                                         | 21    |
| F. Long-range couplers                                                                         | 22    |
| 1. Spin transport, spin swaps, and spin CTAP                                                   | 22    |
| 2. Superexchange                                                                               | 23    |
| 3. Capacitive and electric dipole-dipole couplings                                             | 23    |
| 4. Cavity QED                                                                                  | 24    |
| V. Quantum Gates and Quantum Circuits                                                          | 24    |
| A. Loss-DiVincenzo single-spin qubits                                                          | 24    |
| 1. Initialization and readout                                                                  | 24    |
| 2. Single-qubit gates                                                                          | 25    |
| 3. Two-qubit gates                                                                             | 26    |
| 4. Limits of fidelity: Randomized benchmarking                                                 | 27    |
| B. Donor spin qubits                                                                           | 28    |
| 1. Donor electron spin initialization and readout                                              | 28    |
| 2. Donor electron spin single-qubit gates 3. Donor nuclear spin control and readout            | 28 29 |
| 4. Two-qubit gates                                                                             | 29    |
| 5. Limits of fidelity: Randomized benchmarking                                                 | 30    |
| C. Singlet triplet qubits                                                                      | 30    |
| 1. Initialization and readout                                                                  | 30 31 |
| 2. Single-qubit gates                                                                          | 32    |
| 3. Two-qubit gates                                                                             | 32    |
| 4. Limits of fidelity: Randomized benchmarking D. Exchange-only qubits                         | 33    |
| 1. Initialization and readout                                                                  | 33    |
| 2. Exchange-only single-qubit gates                                                            | 33    |
| 3. Resonant-exchange single-qubit gates                                                        | 34 34 |
| 4. Two-qubit gates                                                                             | 35    |
| 5. Limits of fidelity: Randomized benchmarking E. Alternative material platforms               | 35    |
|                                                                                                | 35    |
| 1. Carbon nanotubes 2. Spin-orbit qubits                                                       | 35    |
| F. Discussion VI. Dephasing and Decoherence                                                    | 36    |
| 3. Holes in Si and Ge = GeSi                                                                   | 36    |
| A. Filter-function formalism 1. T                                                              |       |
| 1 via noise-correlation function 2. Filter-function derivation                                 |       |
| 3. Dephasing time T /C3 2                                                                      |       |
| 4. Decoherence time T 2 and rotating-frame timescales                                          |       |
| 5. Filters for multispin qubits                                                                |       |
| 6. Non-Markovian and contextual noise                                                          |       |
| B. Spin dephasing due to hyperfine interactions                                                |       |
| C. Phonon-mediated spin relaxation D. Charge noise                                             |       |
| VII. Hybrid Systems                                                                            |       |
| A. Overview of superconducting circuit QED B. Coherent interactions in quantum-dot circuit QED |       |
| 1. Charge-photon coupling                                                                      |       |
| 2. Spin-photon coupling                                                                        |       |
| 3. Cavity-mediated spin-spin interactions                                                      |       |

FIG. 1. The four major qubit types covered in this review, with images depicting the original proposals, early devices, and modern devices. (a) Loss-Divincenzo (LD) single spin qubits (Loss and DiVincenzo, 1998; Elzerman et al. , 2004; Mills, Guinn, Gullans et al. , 2022). (b) Donor spin qubits (Kane, 1998; Morello et al. , 2010; He et al. , 2019). (c) Singlet triplet (ST) spin qubits (Levy, 2002; Petta et al. , 2005; Fedele et al. , 2021). (d) Exchange-only (EO) spin qubits (DiVincenzo et al. , 2000; Medford, Beil, Taylor, Bartlett et al. , 2013; Ha et al. , 2022).

<!-- image -->

host. ' Experiments on large spin ensembles demonstrating seconds-long electron spin coherence times and hours-long nuclear spin coherence times in isotopically enriched silicon give credence to Kane s statement (Tyryshkin ' et al. , 2012; Saeedi et al. , 2013).

Single spins have been controlled with electron spin resonance (Koppens et al. , 2006) and two-electron spin states with exchange coupling (Petta et al. , 2005). Silicon quantum devices have achieved high-fidelity single-qubit (Yoneda et al. , 2018) and two-qubit gates (Veldhorst et al. , 2015; Watson et al. , 2018; Zajac et al. , 2018), and recent advances have pushed the fidelity beyond the thresholds required to enter a regime for fault-tolerant operation (Mills, Guinn, Gullans et al. , 2022; Noiri et al. , 2022; Xue et al. , 2022).

Another motivation for harnessing the spin degree of freedom is scale. Given that a fully error corrected quantum computer is likely to require at least one million physical qubits (Fowler et al. , 2012), the small ∼ 100 nm intrinsic scale of quantum dots (QDs) lends itself to the creation of a dense quantum computing architecture that could be mass produced by the semiconductor microelectronics industry (Vandersypen et al. , 2017). At the same time, the small size scale of a spin qubit can lead to engineering challenges associated with addressing each qubit and achieving sufficient connectivity for quantum error correction. Indeed, many interesting recent physics results from the QD community have shown that spins can be coherently coupled to microwave photons (Landig et al. , 2018; Mi et al. , 2018; Samkharadze et al. , 2018), providing opportunities for longrange coupling of spin qubits and readout (Petersson et al. , 2012; Mi et al. , 2018; Zheng et al. , 2019; Borjans et al. , 2020; Borjans, Mi, and Petta, 2021).

The scope of this review is limited to semiconductor spin qubits in shallow donors and gate-defined QDs. Electronic and nuclear spins of point defects in wide-band-gap semiconductors such as diamond or SiC are beyond the scope of this review; see Childress and Hanson (2013), Doherty et al. (2013), and Awschalom et al. (2018). Optically addressable and self-assembled QDs have provided seminal studies toward semiconductor spin qubits, including early measures of semiconductor spin decoherence rates, but are more relevant for photonic implementations of quantum information systems that are not the focus of this review (Imamoglu et al. , 1999; Kroutvar et al. , 2004; Bracker et al. , 2005; De Greve et al. , 2011; Warburton, 2013). Topological quantum computation is not covered here, either with anyons in quantum Hall systems (Das Sarma, Freedman, and Nayak, 2006) or with Majorana fermions in superconductor-semiconductor hybrid systems (Mourik et al. , 2012; Das Sarma, Freedman, and Nayak, 2015).

Section II introduces the four major types of spin qubits, namely, the single spin qubit, donor spin qubit, singlet triplet spin qubit, and exchange-only spin qubit. Figure 1 gives an overview of the four qubit types, with images illustrating theoretical proposals, early devices, and modern devices. Readers familiar with the basic spin-qubit types can proceed to Sec. III, which covers the mesoscopic physics underpinning the operation of semiconductor spin qubits. Details regarding the control of spin-spin interactions, in particular, exchange, are given in Sec. IV. The implementation of quantum gates and circuits for the various spin-qubit flavors is discussed in Sec. V. Dephasing and decoherence of spin qubits due to uncontrolled interactions with their environment is covered in Sec. VI. Hybrid systems consisting of semiconductor spin

FIG. 2. (a) Spin configurations, (b) Bloch spheres, and (c) energy-level diagrams associated with LD single spin qubits, two-spin singlet triplet (ST 0 ) qubits, and three-spin EO spin qubits. Donor spin qubits also rely on single spins, in a manner similar to the LD case. We conventionally identify the north pole of the Bloch sphere with the qubit j 0 i state and the south pole with j 1 i , irrespective of which state is lower in energy. For the LD qubit, a static magnetic field B z eff defines the quantization axis of the single spin, while a transverse (and smaller) ac magnetic field B x eff ð Þ t drives coherent spin rotations between spin-up and spin-down. We identify j 0 i ¼ j ↓ i and j 1 i ¼ j ↑ i and note that the level ordering in (c) holds for g &gt; 0 , as in Si. For the ST 0 qubit, exchange coupling J and a longitudinal magnetic-field gradient Δ B z provide two orthogonal control axes. For the EO spin qubit, nearest-neighbor exchange couplings J 12 and J 23 provide two control axes that are separated by 120° on the Bloch sphere.

<!-- image -->

qubits embedded in superconducting circuits can be found in Sec. VII. We conclude by commenting on future directions for the field in Sec. VIII.

and control methods, all of which we elaborate on in this section.

## II. BASICS OF SPIN QUBITS

In this section, we introduce the various kinds of spin qubits. At the most basic level, we can classify spin-qubit types based on the number of spins used to encode the qubit. Figure 2 shows the Bloch spheres and control axes for single spin qubits, two-spin singlet triplet qubits, and threespin exchange-only qubits. For example, the single spin Loss-DiVincenzo qubit encodes quantum information in the spin state of a single electron. A static magnetic field lifts the degeneracy between the spin-up and spin-down states of the electron, while a transverse ac magnetic field drives coherent rotations between spin up and spin down (Loss and DiVincenzo, 1998).

At a more detailed level (see Fig. 3), the different types of spin qubits are distinguished by how they encode spins into qubits; by the number and species of particles that carry the spin (atomic nucleus, electron, hole, etc.); by their placement in a single-site or multisite arrangement, where a site can be a QD or a donor atom; and by their initialization, measurement,

Common to all semiconductor spin qubits is the confinement of spin to isolated sites. In semiconductors, in contrast to metals, the density of conduction electrons can be depleted to be arbitrarily low. The density may in fact be engineered, starting at zero in an intrinsic semiconductor at a low temperature. This allows for the restriction of electron motion to two dimensions in quantum wells (QWs) or at interfaces between two materials (Ando, Fowler, and Stern, 1982), and further to one or even zero dimensions with electrostatic tailoring of the potential landscape (Kouwenhoven, Austing, and Tarucha, 2001; van der Wiel et al. , 2002). Confinement in all spatial dimensions is achieved in QDs that localize electrons and act as artificial atoms (Kastner, 1992). A collection of electrons, each of which is confined to one such QD, provides a nearly ideal arena for the realization of spin-based quantum information processing (Loss and DiVincenzo, 1998).

Another commonality to all flavors of semiconductor spin qubits is some use of the exchange interaction. The physics of exchange is discussed in Secs. III.B and IV, but essentially this interaction arises from the requirement that two-electron states be antisymmetric, allowing for spin configurations that are either singlets (spin antisymmetric) or triplets (spin

FIG. 3. Spin-qubit configurations grouped by the number of spin1 = 2 particles per qubit and number of sites (usually QDs). Spins are indicated by the small gray dots (electrons or holes) or small white dots (nuclei), which are numbered to adhere to the basis description of Fig. 4. Sites are indicated by the large (pink) circles; their overlap indicates ' always-on exchange, ' meaning that the spins contained are somewhat delocalized across the site even for the idle qubit.

<!-- image -->

symmetric). When the electrons overlap spatially, the energy of the spin-singlet state is lowered relative to the three spintriplet states by an amount called the exchange coupling J . This effect (sometimes referred to as pseudoexchange or kinetic exchange) occurs due to the ability of electrons in the singlet state to move to and from the same location (while maintaining a totally antisymmetric wave function), while such motion is forbidden for the spin-symmetric (and hence spatially antisymmetric) triplets. This effect for spins i and j is captured by the Heisenberg exchange Hamiltonian H ¼ Jij S i · S j , where S i denotes the quantum operator for the spin of the electron residing in the i th site. From a quantum control perspective, an appeal of spin qubits is that Jij can typically be tuned over many orders of magnitude by adjusting gate voltages (Petta et al. , 2005). Depending on the type of spin qubit, the exchange interaction may be used for either single-qubit (Levy, 2002; Petta et al. , 2005; Eng et al. , 2015) or two-qubit (Nowack et al. , 2011; Veldhorst et al. , 2015; Watson et al. , 2018; Zajac et al. , 2018) gates.

## A. Loss-DiVincenzo (LD) spin qubit

The spin 1 = 2 of an electron represents a natural realization of a qubit. The encoding for a single-electron-spin LossDiVincenzo qubit is a direct mapping S i ¼ -σ i = 2 between spin operators and encoded Pauli operators. In the limit of tight electronic confinement, with one electron per dot, the electron spin dynamics are governed by the Heisenberg exchange Hamiltonian (as previously discussed) and the single-electron Zeeman Hamiltonian, leading to a total Hamiltonian of the form

<!-- formula-not-decoded -->

where B i and gi are the effective magnetic field and g factor at site i .

The Loss-DiVincenzo qubit requires a method of initialization and measurement of single-electron spin states. The original proposal (Loss and DiVincenzo, 1998) suggested spin-selective ferromagnetic elements in the device; however, actual practice has employed spin-selective tunneling to a fermionic bath of electrons (Elzerman et al. , 2004) in which a large static magnetic field B ≫ kBTe=g μ B enables tunneling of the higher-energy QD spin state to the Fermi sea, while tunneling from the lower-energy spin state is energetically forbidden. Here kB is Boltzmann s ' constant and Te is the electron temperature. The presence or absence of a tunneling event, as measured using sensitive charge detectors (see Sec. III.C), is then used to infer the orientation of the electron spin. This spin readout protocol is commonly referred to as Elzerman readout and requires relatively large magnetic fields, which in turn sets the Larmor frequency for spins in the tens of gigahertz range.

For this qubit type, the single spin B -dependent (Zeeman) terms provide single-qubit control. Time-dependent control of B i or gi is required for the implementation of single-qubit gates. This has been realized using a combination of static and oscillatory magnetic fields within the framework of electron spin resonance (ESR) (Koppens et al. , 2006; Pla et al. , 2012; Veldhorst et al. , 2015) or using oscillatory electric fields in combination with spin-orbit coupling (Nowack et al. , 2007; Nadj-Perge et al. , 2010) or magnetic-field gradients (PioroLadriere et al. , 2008; Brunner et al. , 2011; Yoneda et al. , 2018; Zajac et al. , 2018) by applying electric-dipole spin resonance (EDSR).

The exchange coupling, which can be adjusted with gate voltages (Petta et al. , 2005), allows for time-dependent twoqubit control, and hence the realization of entangling twoqubit gates between nearest-neighbor spins (Nowack et al. ,

2011; Veldhorst et al. , 2015). Recent implementations of Loss-DiVincenzo qubits use static field gradients for B , pulsed or ac-driven exchange for Jij ð Þ t , and oscillatory electric fields (Watson et al. , 2018; Zajac et al. , 2018) to achieve full control of a two-qubit system.

## B. Donor spin qubits and Kane s proposal '

Shortly after the publication of the Loss-DiVincenzo proposal on quantum computation with QDs, Kane (1998) published a proposal to use the nuclear spins of 31 P donor atoms in silicon to construct a quantum computer. Nuclear spins are highly coherent since the nuclear gyromagnetic ratio γ n = 2 π ¼ 17 2 . MHz T for = 31 P is nearly 2000 times smaller than the electron gyromagnetic ratio γ e = 2 π ≈ 28 GHz T, and = their lack of mobility in a solid-state host inhibits chargehybridizing or spin-orbit-related decoherence mechanisms (which are discussed in Sec. VI).

Kane proposed using the I ¼ 1 = 2 nuclear spin of a 31 P donor in Si as a quantum bit. 31 P is a shallow donor in Si with a 45 meV ionization energy (Feher, 1959; Wilson and Feher, 1961). The donor electron has a hydrogenic s -like ground state with an effective Bohr radius of 1.8 nm (Smith et al. , 2017). To maintain a high degree of nuclear spin coherence, the donor nuclear spins would ideally be embedded in a host material composed of I ¼ 0 isotopes, as background nuclear spins can lead to decoherence. Despite their small effective mass and widespread use in mesoscopic physics, common III-V semiconductors such as GaAs and InAs have stable isotopes only with I ≠ 0 . In contrast, Si is composed primarily of I ¼ 0 nuclear spin isotopes 28 Si and 30 Si. The remaining 5% of I ¼ 1 = 2 29 Si can be removed through isotopic enrichment.

Gate-voltage control of the donor-bound electronic wave function is an important aspect of the Kane quantum computer. Kane proposed using an array of 31 P donor atoms placed ∼ 200 Å beneath the Si surface as the register of qubits. By adjusting the voltage Vg on an A gate placed above each donor, the donor electron can be pulled away from the donor toward the Si = SiO 2 interface to reduce the hyperfine interaction A Vg ð Þ and control the nuclear spin resonance frequency. Nuclear spin exchange is mediated by electrons using gates called J gates, which are located between adjacent donor sites. The J -gate voltage influences the overlap between adjacent donor electron wave functions and, through the hyperfine interaction, the nuclear spin exchange coupling. Measurements of the nuclear spin state are performed by again leveraging the tunability of the electronic wave function using gates. Nuclear spin initialization can be achieved using the same steps for nuclear spin state readout, with an additional radio-frequency-driven rotation to the desired starting spin state if required.

Since Kane s proposal, many elements of this qubit type ' have been demonstrated, and in doing so, many critical variations on the donor-qubit concept have emerged. 31 P nuclei have been placed in natural-abundance (Morello et al. , 2010) and isotopically enhanced silicon substrates (Muhonen et al. , 2014) using a masked ion-implantation method. Scanning tunneling microscope lithography has been used to incorporate 31 P nuclei into natural-abundance silicon

(Fuechsle et al. , 2012). Control of the exchange interaction between 31 P donor-bound electrons has been demonstrated using both fabrication methods (He et al. , 2019; Madzik et al. , 2021). The initialization and readout of a single 31 P nuclear spin has been performed with over 99% fidelity (Pla et al. , 2013), the A -gate-modulated hyperfine interaction has been used as envisioned by Kane to tune electron and nuclear Larmor resonances (Laucht et al. , 2015), and multiqubit electron and nuclear processes have been characterized with gate-set tomography for total singleand two-qubit gate fidelities exceeding 99% (Nielsen et al. , 2021; Madzik et al. , 2022). A key challenge of the Kane proposal is that the required exchange interaction is highly sensitive to the 31 P donor placement (Koiller, Hu, and Das Sarma, 2001), thus requiring either impeccable fabrication tolerance or more tolerant forms of two-qubit gates, several of which have been proposed (Tosi et al. , 2017; Broome et al. , 2018).

## C. Singlet triplet ( ST 0 and ST /C6 ) qubits

Both the Loss-DiVincenzo (Loss and DiVincenzo, 1998) and Kane (Kane, 1998) proposals for quantum computing involve single spin qubits manipulated with a combination of static and oscillating electric and magnetic fields. The oscillating fields can be difficult to localize in nanoscale devices, and the power dissipated by those fields can be problematic at cryogenic temperatures. In addition, the primary source of dephasing for single spin qubits is the magnetic noise associated with the semiconductor environment, which can be large in materials such as GaAs that have spinful nuclei; see Sec. VI. In part to overcome these control and dephasing challenges, spin qubits can be realized through different sets of multispin states associated with groups of electrons (Fig. 3).

Conceptually, the simplest extension of the single spin qubit is a qubit formed from two electrons in a double quantum dot (DQD), utilizing the controlled singlet triplet splitting offered by the exchange interaction (Sec. IV) to define the singlet triplet (ST 0 ) qubit (Levy, 2002; Petta et al. , 2005). The j S i and j T 0 i basis states are defined in Fig. 4. The ST 0 qubit Hamiltonian in the presence of exchange and magnetic-field gradients is

<!-- formula-not-decoded -->

In Eq. (2) the encoded Pauli operators σ z and σ x are in the singlet triplet basis, the exchange coupling J 12 can be experimentally controlled by adjusting the QD gate voltages (Petta et al. , 2005), and Δ ð gB z Þ is the effective difference in magnetic field between the two dots along an applied global field direction ( z direction).

Figure 4 provides a useful framework for understanding the ST 0 qubit and others discussed later. We note that the basis states and the encoded qubit Pauli operators σ x , σ y , and σ z are defined such that the /C6 1 eigenstates of σ z are the encoded (basis) states and the 0 eigenstates are leakage states (polarized triplet states T /C6 in this case). Additionally, all of the encoded Pauli operators have the correct commutation relations. To understand how physical interactions map to encoded qubit operations, consider that any spin operator X

FIG. 4. Spin-qubit encodings. The first column N is the number of spin1 2 = particles per qubit, followed by a named ' type ' of qubit discussed in this review. The two-qubit states j 0 i and j 1 i are then specified in terms of both a conserved and a qubit-dependent ' q number ' describing the total angular momentum; here m always refers to the total spin projection, whereas Sjk /C1/C1/C1 refers to the combined total spin angular momentum of spins j; k; … . Clebsch-Gordan coefficients translate these spin angular momentum combinations into ' states. ' For the three-spin case, m may take either value /C6 1 = 2 in the encoded subspace. The final column shows the encoded Pauli operators σ of the qubit in terms of the spin operators S j of each spin1 = 2 particle j . The qubit states are the /C6 1 eigenstates of σ z . Degeneracies in these eigenstates indicate gauge freedom, and the null spaces of these operators are leakage states. For the LD qubit, the constant relating the logical qubit to the spin changes with the g factor. The minus value shown here is consistent with the Si g &gt; 0 choice used in Fig. 2.

can be decomposed into encoded Pauli operators as X ¼ j c j σ j , with c j ¼ Tr f X σ j g = 2 .

## (Petta et al. , 2005; Barthel et al. , 2010; Borjans, Mi, and Petta, 2021).

Since the initial demonstration (Petta et al. , 2005), ST 0 qubits and variants thereof, including ' resonantly driven ST 0 ' or ' flip-flop ' qubits, have been the focus of intense research. Single-qubit gates have been studied in GaAs QDs (Bluhm et al. , 2011; Shulman et al. , 2014) and in Si QDs (Maune et al. , 2012; Wu et al. , 2014; Fogarty et al. , 2018; Jock et al. , 2018). Capacitive coupling of ST 0 qubits can yield an entangling operation (Taylor et al. , 2007; Shulman et al. , 2012; Nichol et al. , 2017). Early results on ST 0 qubits coupled via a superconducting resonator or exchange coupling have also been encouraging (Bøttcher et al. , 2022).

In the presence of a global magnetic field, the Zeeman energy can compensate for exchange, and the polarized triplet ( T j þi in GaAs or j T -i in Si) can become degenerate with the singlet state. This degeneracy can be lifted via transverse magnetic-field gradients (Taylor et al. , 2007), spin-orbit coupling (Stepanenko et al. , 2012; Nichol et al. , 2015), or spin-valley coupling (Cai et al. , 2023), and an effective ST þ

P As a result of the tunable exchange coupling J 12 , ST 0 qubits feature full electrical control with baseband voltage pulses (Petta et al. , 2005). The ST 0 qubit also exists in a decoherence-free subspace (DFS) with respect to global magnetic fields that couple to the spin of the electron since m ¼ 0 for both j S i and j T 0 i (Lidar, Chuang, and Whaley, 1998). However, the ST 0 qubit remains sensitive to local magnetic-field fluctuations as a result of the Δ ð gB z Þ term in the Hamiltonian. This σ x term may result from quasistatic hyperfine fields (Taylor et al. , 2007; Petta et al. , 2008), g -factor variations (Jock et al. , 2018; Liu et al. , 2021), or micromagnet field gradients.

Pauli spin blockade, a manifestation of exchange coupling (Sec. IV.E), enables straightforward, rapid, and high-fidelity measurements of joint spin states. A spin blockade measurement converts singlets and triplets to different spatial configurations of the two electrons in the DQD, which can easily be distinguished using a nearby charge sensor

qubit can be formed in GaAs (or a ST -qubit in Si; we loosely refer to both types as ST /C6 qubits, with the understanding that the relevant triplet state is dependent on the sign of the g factor). In the fj S i ; j T þig basis the encoded Hamiltonian is H ST þ ¼ E ST þ σ z = 2 þ Δ ST σ x = 2 , where the electrically tunable qubit splitting E ST þ ¼ EZ -J , for the average Zeeman energy EZ . Universal control of ST /C6 qubits can be achieved through baseband voltage pulses (Cai et al. , 2023) and Landau-ZenerSt¨ckelberg u interferometry (Petta, Lu, and Gossard, 2010; Gaudreau et al. , 2012). To date ac-driven ST /C6 Rabi oscillations have not been observed. Two-qubit gates for the ST /C6 qubit based on capacitive coupling have been proposed (Ribeiro, Petta, and Burkard, 2010).

## D. Exchange-only (EO) and resonant-exchange (RX) qubits

The spin-qubit encodings discussed thus far use both magnetic splittings and kinetic exchange to complete singleand two-qubit gate sets. However, Bacon et al. (2000), DiVincenzo et al. (2000), and Kempe et al. (2001) showed that universal quantum computation is possible using only the exchange interaction.

To understand how this is possible, we may ask how multiple spins can encode a single qubit beyond the singlet triplet example already presented. The key principle results from the addition of angular momentum: in particular, the total angular momentum of N spin1 = 2 electrons add, via angular momentum rules, into subsystems with total angular momentum numbers varying from 1 2 = (for odd N ) or 0 (for even N ) to N= 2 , with readily calculable degeneracies. For two electrons, the singlet and triplet states correspond to the S 12 ¼ 0 singlet and the S 12 ¼ 1 triplet, with no additional degeneracies; the m ¼ 0 subsystem of these two spaces is the singlet triplet qubit. For three electrons, there are two ways to combine into S 123 ¼ 1 = 2 , and these two states, at constant m ¼ /C6 1 = 2 , may be considered to form a qubit. For four electrons, there are again two ways to combine into S 1234 ¼ 0 , which was the original exchange-only qubit presented by Bacon et al. (2000). The pairwise exchange interactions among a set of N spins conserves their total angular momentum and their total m quantum numbers but gives full control within the copies of total angular momentum subspaces.

The smallest encoding to allow exchange-only control is therefore three spins in their S 123 ¼ 1 2 = manifold. Here there are two copies corresponding to total spin projection m ¼ /C6 1 = 2 . Any exchange operation within a single, threespin qubit behaves the same way regardless of m . Exchange interactions occurring between pairs of encoded qubits, however, do depend on m , and as such two-qubit operation requires that either m is polarized (typically at high magnetic field), in which case the exchange-only two-qubit gates presented by DiVincenzo et al. (2000) may be employed and the system is generally called a decoherence-free subspace (DFS), or m may be left unpolarized, in which case the m -independent two-qubit gates presented by Fong and Wandzura (2011) may be employed and the system is generally called a decoherence-free subsystem (also abbreviated DFS). As the four-spin S 1234 ¼ 0 encoding has only m ¼ 0 , this is also considered a decoherence-free subspace. The nomenclature decoherence free refers to the original motivation for these encodings before exchange-only control was discovered (Zanardi and Rasetti, 1997), which was to eliminate the particular source of decoherence that arises from fluctuations in the global magnetic field.

The states and Pauli operators of the three-spin S 123 ¼ 1 = 2 and four-spin S 1234 ¼ 0 DFS qubits are shown in Fig. 4. We note in this table that for DFS qubits, unlike the single-spin or two-spin cases, the decomposition of encoded Pauli operators into spin operators feature no notion of direction. The qubit is controlled via the controlled fractional permutations of spins via exchange, rather than physical rotations about any preferred axis, which is reflective of their designed insensitivity to the global applied field.

In Fig. 4, we see that, for three spins in the S 123 ¼ 1 = 2 subsystem, exchange coupling between spins 1 and 2, as for singlet triplet qubits, appears as a σ z . Exchange coupling between spins 2 and 3 appears in both σ x and σ z , combining to the ˆ n axis shown in Fig. 2. Composite gates enabling arbitrary single-qubit operations may be composed of alternating combinations of these exchange operations.

Both one- and two-qubit quantum gates for the EO qubit proceed by sequentially pulsing on and off the exchange coupling Jij ð Þ t for pairs of spins i and j ; this is done via dc voltages on the gates. In the idle state, when quantum gates are not being executed, the exchange coupling is set to zero everywhere [ Jij ð Þ ¼ t 0 ], in which case, even in a magnetic field, all qubit states are degenerate, and ideally there is no phase evolution between superposed states in the laboratory frame. This contrasts with the LD qubit, which has a rotating frame at the electron Larmor frequency that must be tracked by a local oscillator. The EO qubit requires no such oscillator.

An alternative mode of operation for EO qubits is called the RX qubit. The RX qubit differs from the dc-mode EO qubit in that the nearest-neighbor exchange couplings are constantly set to the same nonzero value J ¼ J 12 ¼ J 23 , opening an energy gap between the qubit states j 0 i and j 1 i . There is now a rotating frame at frequency J , and singlequbit gates can correspondingly be executed with ac exchange pulses Δ J t ð Þ ¼ J 12 -J 23 ∝ cos ð ω t Þ , where /uni210F ω ¼ J (Medford, Beil, Taylor, Bartlett et al. , 2013; Medford, Beil, Taylor, Rashba et al. , 2013; Taylor, Srinivasa, and Medford, 2013). Two-qubit gates can be obtained using dc pulses for the exchange coupling between pairs of spins belonging to different qubits (Doherty and Wardrop, 2013), or via capacitive couplings, as demonstrated for the case of the ST 0 qubit (Shulman et al. , 2012; Feng, Zaw, and Koh, 2021).

While allowing for narrowband ac operation, always-on exchange coupling also (to some extent) exposes the qubit to electric noise. The discussion of possible ways to protect RX qubits from electric noise at suitable operating points where the qubit is insensitive to noise (sweet spots) has led to the asymmetric resonant-exchange qubit (Russ and Burkard, 2015a) and always-on exchange-only (AEON) qubit concepts (Shim and Tahan, 2016). The AEON qubit allows for onequbit and two-qubit operations while always remaining at a charge-insensitive region of potential bias space.

Magnetic-field gradients are also a source of unwanted noise for exchange-only qubits. For any of these three-spin encodings, matrix elements due to local gradients will in

general cause leakage from the total S subspace in which the qubit is encoded in another S subspace. Such ' spin leakage ' is a key error type to manage, unlike in the LD qubit case.

## E. Spin qubits with additional charge degrees of freedom

The previously discussed spin qubits operate in the regime of half filling, with one particle per site, as represented by the diagonal entries in Fig. 3, with spin being the remaining degree of freedom, while particle hopping occurs only virtually. In this section, we describe qubit variants that deviate from single-charge filling, and thus allow for correlations between charge and spin, to exploit spin-charge hybridization for qubit initialization and readout, electricfield control, and electric-dipole coupling to other qubits or cavity electric fields.

An instructive example is the flopping-mode qubit, which consists of a single electron that can occupy either the left or right site of a DQD (Benito et al. , 2019; Croot et al. , 2020; Mutter and Burkard, 2021). The charge can be coupled to the spin by spin-orbit coupling or an external magnetic-field gradient, and delocalization of the charge across the DQD near zero-level detuning enhances the electric-dipole moment compared to a single QD (Cottet and Kontos, 2010; Hu, Liu, and Nori, 2012). Judicious control of the energy-level detuning and tunneling strength between the two sites permits a tunability of the electric dipole. Therefore, strong coupling to the electric field or other qubits can be obtained when needed, while there is a small susceptibility to charge noise at small coupling or sweet spots when the qubit is idle. Increasing the number of sites available to a single particle to three allows for the formation of a charge quadrupole qubit (Friesen et al. , 2017; Koski et al. , 2020).

Rather than extending the number of sites for a single particle, one can instead decrease the number of sites for the three-particle EO qubit. Reduction from three to two sites leads to the QD hybrid qubit (Koh et al. , 2012; Shi et al. , 2012, 2014; Kim et al. , 2014). While this design essentially fixes the intrasite exchange coupling to a nonzero value, it still allows for fast electrical control of a qubit via the energy detuning and tunnel coupling. Although charge noise is a concern for the hybrid qubit, its impact is reduced due to the similarity of the orbital wave functions of the intrasite singlet and triplet states. Reducing the number of sites further to a single site, one obtains the spin-charge qubit (Kyriakidis and Burkard, 2007); see Fig. 3. Four electrons in four dots can define a pulsed EO qubit with total spin S ¼ 0 that is initialized via two spin singlets (Bacon et al. , 2000). RXlike operation is possible using at least three always-on exchange interactions between four dots (Sala and Danon, 2017). Alternatively, a hybrid quadrupolar exchange-only (QUEX) mode of operation is possible with four electrons in three dots, using a valley or orbital splitting in the central dot as an effective always-on exchange coupling (Russ, Petta, and Burkard, 2018).

## III. MESOSCOPIC PHYSICS OF DOTS AND DONORS

In this section, we review the basic principles behind the operation of QDs and donors, which form the basis for semiconductor spin qubits. In Sec. III.A we discuss how electrons, which exist in bulk semiconductors as delocalized Bloch states, can be confined in QDs by the heterostructure and externally applied potentials. The essential role of Coulomb interactions in defining QD states and the exchange interaction is covered in Sec. III.B. Section III.C summarizes the development of QD device designs and charge sensing technology. We conclude by covering interactions with other microscopic degrees of freedom in semiconductor QDs, such as spin-orbit coupling (SOC) and its relation to the Zeeman Hamiltonian (Sec. III.D), valley states in silicon (Sec. III.E), and lattice nuclei (Sec. III.F). Several of these topics have also been reviewed elsewhere (van der Wiel et al. , 2002; Hanson et al. , 2007; Zwanenburg et al. , 2013), and we emphasize recent developments where applicable.

## A. Quantum confinement

Semiconductor spin qubits rely on the full three-dimensional (3D) confinement of electrons. Figure 5 illustrates some of the most commonly employed spin-qubit designs and the resulting electronic confinement potentials. In donor-based devices, donors can be placed in the semiconductor using ' bottom-up ' scanning tunneling microscopy (STM) lithography or ' top-down ' ion implantation. 3D confinement of the donor electron is then generated using the Coulomb potential of the dopant atom in the semiconductor. Figure 5(a) depicts a device in which donor sites and gates are both fabricated using STM lithography (He et al. , 2019). Alternatively, P ions can be implanted into Si metal-oxide-semiconductor (MOS) devices that incorporate microwave striplines and singleelectron transistor charge detectors (Morello et al. , 2010).

In most planar QD systems, a layered semiconductor heterostructure generates confinement in the z direction (generally the growth direction), while electrostatic gates confine electrons within the x y -plane; see Figs. 5(b) -5(e). Many early experiments were performed using depletionmode GaAs devices, as illustrated in Fig. 5(b). In these devices an AlGaAs spacer layer is doped with Si to provide the free electrons that populate the two-dimensional electron gas (2DEG) formed at the AlGaAs/GaAs interface. The 2DEG is depleted by applying negative voltages to top gates. In this example the top gates are designed to form a DQD (Elzerman et al. , 2003).

Many modern devices utilize undoped semiconductors to reduce charge noise and gate leakage. In undoped devices, electrons are accumulated at the Si = SiO 2 interface [Fig. 5(c)] or the Si QW [Fig. 5(d)] by applying positive voltages to overlapping accumulation gates (Angus et al. , 2007; Borselli et al. , 2011a). In both of these designs, the barrier gates (cyan) set the height of tunnel barriers and the darker (orange) gates define the locations of the QDs. The gate layers are separated by a thin dielectric, often Al O . In inactive regions of the 2 3 device, the gates are elevated off of the substrate using a layer of screening gates or a spacer layer.

A recent development is the fabrication of QDs using a single-layer etch-defined gate electrode (SLEDGE) process; see Fig. 5(d). In these devices the electronically active region of the device is patterned in a single step (Ha et al. , 2022). Subsequent fabrication steps make electrical contact to the

FIG. 5. Device designs commonly used to confine electron spins. Vertical confinement is illustrated in the plots of E z ð Þ and lateral confinement is illustrated in the x y -plane. (a) Donor electrons are confined by the positive potential of the donor atom and manipulated with gates defined through conventional or STM lithography. (b) Depletion-mode device design commonly used in early GaAs experiments. Modern Si MOS and Si = SiGe devices utilize overlapping gate architectures to achieve tight control of QD electrons. (c) In Si MOS, electrons are localized at the SiO /Si interface. (d) In Si 2 = SiGe, the electrons reside in a buried QW. (e) Single-layer etchdefined gate electrode (SLEDGE) devices utilize a single layer of gates patterned on the top surface of a Si = SiGe heterostructure. The gates are contacted from above using vias, which allows gate wiring to fan out away from the active area of the device in multiple planes. (f) FinFETs use a combination of dry etching and electrostatic gating to confine QD electrons. (c) -(f) Quantum-dot electrons are accumulated beneath the dark (orange) plunger gates, while the tunnel barrier gates are indicated with lighter shading (cyan). Gates are electrically isolated from one another using a thin dielectric. In (c) and (d), the plunger and barrier gate layers are isolated from the semiconductor in inactive regions of the device using screening gates.

<!-- image -->

gate electrodes from the top using vias. SLEDGE designs may be more amenable to the development of large 2D QD arrays, as the electrical connections to the gates can be fanned out in multiple layers.

Last, fin field-effect transistor (FinFET) and silicon-oninsulator (SOI) nanowire approaches [Fig. 5(f)] use a combination of etching and electrostatic gating to define QDs (Voisin et al. , 2016; Zwerver et al. , 2022). The etching process defines a quasi-1D channel (or pair of parallel channels). ' Wraparound ' electrostatic gates generate the electric confinement potential along the length of the channel. The FinFETapproach is currently being investigated by a number of industrial labs due to its similarity to conventional CMOS transistors. Additionally, the wrap-around gate design strongly couples to the QD electrons, giving rise to a robust charge sensing signal; see Sec. III.C (Ciriano-Tejel et al. , 2021).

## 1. Bulk band structure

We begin our discussion of confinement by considering the bulk band structure of the most common materials used to fabricate spin qubits, namely, GaAs and Si. Figure 6 shows the first Brillouin zone and electronic band structure of GaAs and Si (Yu and Cardona, 2010), which arise due to the crystalline potential of each material. While the full band structure is complex, much of its practical impact on the properties of QDs is captured by the effective-mass approximation (EMA) describing the conduction band minima and valence band maxima. In this approach, the crystal potential effects are encapsulated by a renormalized kinetic energy operator in the Schrödinger equation, yielding the following single-particle Hamiltonian (Yu and Cardona, 2010):

<!-- formula-not-decoded -->

with effective masses m i and the position vector r ¼ ð r x ; r y ; r z Þ ¼ ð x; y; z Þ . In Eq. (3) we have also included the slowly varying potential U ð r Þ , which includes the electrostatic potential generated by the gate electrodes as well as the Zeeman term with the effective g tensor ˆ g , which is further discussed in Sec. III.D.

The effective mass may be either isotropic or anisotropic, depending on the material; in the former case, we can define a single effective mass m /C3 ¼ m x;y;z . For instance, free electrons in GaAs [Fig. 6(a)] occupy the isotropic Γ point ( k ¼ 0 ) conduction band minimum and are described by m /C3 ¼ 0 067 . m , where m is the bare-electron mass. Bulk silicon [Fig. 6(b)], by contrast, has a sixfold degenerate

FIG. 6. Bulk Brillouin zone (upper panels) and band structure (lower panels) as a function of k along the h 100 i and h 111 i directions for (a) GaAs and (b) Si. The nondegenerate conduction band minimum in GaAs is centered at the Γ point ( k ¼ 0 ), while Si has six equivalent conduction band minima along the highsymmetry h 100 i ( Δ ) directions and an anisotropic effective mass. The heavy-hole (HH) and light-hole (LH) valence bands for both materials are separated in energy from the split-off (SO) band by the spin-orbit splitting.

<!-- image -->

conduction band minimum along the h 100 i ( Δ ) directions in k space. Each valley has an anisotropic effective mass of 0 92 . m and 0 19 . m in its longitudinal and transverse directions, respectively. The sixfold valley degeneracy is broken in Si devices by heterostructure and electrostatic confinement. This induces a valley splitting, a concept that is further discussed in Sec. III.E.

The effective-mass approximation is sufficient for understanding many QD properties. However, microscopic details of important phenomena such as spin-orbit and valley splitting are sensitive to band mixing and atomistic effects beyond the effective-mass approximation. Microscopic descriptions of such effects can be obtained from more complicated band structure models, for instance, using k · p or tight-binding Hamiltonians (Yu and Cardona, 2010). Such models are also useful, particularly for describing valence band holes, where multiple bands are relevant due to Γ point degeneracies and SOC. As shown in Fig. 6, this leads to heavy-hole (HH) and light-hole (LH) bands that are degenerate at Γ , as well as a split-off (SO) band that is lowered in energy by the bulk spinorbit splitting. The structure of the valence band near the Γ point originates from the p -type atomic orbitals (rather than the s type in the conduction band) related to the orbital angular momentum l ¼ 1 . Combined with the spin s ¼ 1 = 2 , this allows for total angular momentum j ¼ 3 = 2 (LH and HH) or j ¼ 1 = 2 (SO), with the two split by the SOC. The HH and LH bands are distinguished by j z ¼ /C6 1 = 2 (LH) and j z ¼ /C6 3 = 2 (HH) (Yu and Cardona, 2010).

## 2. Band structure engineering

To trap single spins, quantum confinement is necessary and is typically provided by a combination of material-defined and electrostatically defined spatial barriers. For donors in bulk silicon, 3D confinement is provided by the impurity potential itself, as depicted in Fig. 5(a). This potential decays as 1 =r away from the impurity but has localized corrections in the immediate vicinity of the donor site; the latter short-range effects are called central-cell corrections (Pantelides, 1978). In epitaxial Si = SiGe, Ge = SiGe, and GaAs = AlGaAs heterostructures, by contrast, charge carriers (i.e., electrons or holes) are confined in the out-of-plane (growth) direction by the conduction band offsets occurring at semiconductor interfaces (Ando, Fowler, and Stern, 1982; Abram and Jaros, 1989; Bastard, 1991).

For instance, many seminal results in mesoscopic physics were obtained with 2DEG devices fabricated on Schottky-gated GaAs AlGaAs heterostructures = [Fig. 5(b)]. Sandwiching a thin GaAs layer between two Al Ga x 1 -x As layers creates a 2DEG in the GaAs layer due to its lower conduction band edge. A 2DEG can also be formed at a single heterointerface, such as GaAs = AlGaAs, which confines electrons inside GaAs in a nearly triangular confinement potential. In most cases, the electrons are provided by doping the adjacent Al Ga x 1 -x As layer with Si atoms (Manfra, 2014). Undoped enhancement-mode devices, where electrons are electrostatically forced into the QW with a top gate, are also being investigated (Mak et al. , 2013; Tracy, Hargett, and Reno, 2014).

In Si MOS devices, the 2DEG is formed at the Si-oxide interface. The large band gaps of most oxides allow for large band offsets, in turn enabling high out-of-plane electric fields to be applied by metal gates without inducing leakage. As a result, MOS electrons are confined in an approximately triangular potential formed by the Si-oxide conduction band offset on one side and the gate-induced electric field on the other, which is illustrated by the potential cut in Fig. 5(c).

2DEGs can be similarly formed in Si = SiGe heterostructures, where strain is appreciable due to the 4% larger lattice constant of Ge than of Si (Sch¨ affler, 1997). For spin-qubit applications, a thin tensile-strained Si layer is typically sandwiched between lattice-relaxed Si Ge x 1 -x alloy layers, which induces a conduction band offset that traps electrons in the Si QW. Undoped heterostructures are now the norm for Si = SiGe QWs, as electron accumulation can be totally gate modulated (Deelman, Edge, and Jackson, 2016). The induced out-of-plane electric fields in these structures are therefore comparatively modest, as shown in Figs. 5(d) and 5(e). Finally, FinFETs extend MOS architectures utilizing etching and electrostatic gating to confine QD electrons [Fig. 5(f)].

## 3. Electrostatic gating

Once a QW has been formed in a planar heterostructure, confinement in the in-plane dimensions can further reduce the effective dimensionality of the electronic states. In-plane confinement is achieved through the electrostatic potential U ð r Þ in Eq. (3), which is typically induced by metal gate electrodes above the heterostructure. A confining potential along a single direction creates a quasi-1D channel, which can form a quantum point contact (QPC) [Fig. 7(a)]. Finer-grained electrostatic confinement along both in-plane directions can form effectively 0D QDs. The potential minima define QD locations where electrons can be trapped [Fig. 7(b)].

FIG. 7. Electrostatic confinement. (a) 1D states can be formed in a QPC due to the potential constriction from a split gate. (b) Electrostatic confinement in both in-plane directions of a QW lead to 0D QD states. (c) Two QDs placed in series form a DQD. Depletion-mode devices are shown.

<!-- image -->

Gate-voltage changes alter both the QD electrochemical potential and the shape of the confining potential. QDs can be connected in series to make larger structures, such as the DQD depicted in Fig. 7(c). In a DQD, the interdot barrier height can be voltage controlled to modulate the interdot tunnel coupling t c [Fig. 8(c)]. Typical devices use separate plunger and barrier gates to control the dot electrochemical potentials and interdot barriers, respectively. In practice, geometrical cross capacitances influence the potential under neighboring gates (van der Wiel et al. , 2002), and voltage compensation of multiple gates is required to independently control each dot potential, a procedure sometimes referred to as defining ' virtual gates ' (Keller et al. , 1996; Hensgens et al. , 2017; van Diepen et al. , 2018; Mills, Zajac et al. , 2019).

## B. Electron-electron interactions in QDs

Band structure and electrostatic confinement allow the formation of 0D QD states and the trapping of individual

FIG. 8. (a) DQD confinement potential. (b) DQD charge stability diagram. From Zajac et al. , 2018. (c) DQD energy levels near the ð 1 0 ; Þ ð -0 1 ; Þ interdot charge transition. (d) DQD energy levels in the two-electron regime showing the crossover from the ð 2 0 ; Þ → ð 1 1 ; Þ → ð 0 2 ; Þ charge state.

<!-- image -->

electrons (and hence spins). As more electrons are added to a QD, the electron-electron Coulomb interaction becomes critical to the properties of the entire system. Trapped electrons in a QD electrostatically repel any other electron attempting to join that dot. This classical effect defines the charging energy EC ¼ e =C 2 , where C is the total dot capacitance. Coulomb repulsion is drastically illustrated by the phenomenon of a Coulomb blockade in electron transport through QDs. Biasing a QD in Coulomb blockade fixes its electron occupation, which is a prerequisite for defining any spin qubit (Kouwenhoven, Austing, and Tarucha, 2001; Hanson et al. , 2007).

While Coulomb blockade can be understood conceptually through classical considerations, quantum effects further modify and enrich the physics. The full energy penalty for changing electron occupation is called the addition energy E add , which can be qualitatively understood with a simple constant interaction model in which E add ¼ EC þ E orb . Here E orb is the change in single-particle energy that appears when an extra electron must occupy a new orbital level to enter the QD (due to the Pauli exclusion principle prohibiting more than two electrons from occupying a single energy level).

Transport through multiple QDs connected in series proceeds when the electrochemical potentials of the individual QDs lie within the source-drain bias window and tunneling from one dot to the next is downhill in energy (van der Wiel et al. , 2002). We consider the level structure of a DQD in Fig. 8(a), as it illustrates several key QD control principles. Figure 8(b) shows a DQD charge stability diagram, with charge states denoted ð N ; N 1 2 Þ , where Ni is the number of electrons in dot i . For a single-electron DQD ( N 1 þ N 2 ¼ 1 ), there are two relevant charge states, ð 1 0 ; Þ and ð 0 1 ; Þ , and we can approximate the DQD in that basis as a two-level system with the Hamiltonian

<!-- formula-not-decoded -->

where the detuning ε ¼ μ 1 -μ 2 is the difference between the electrochemical potentials of the two dots. Hopping between different charge states is described by the tunnel coupling t c , which is generally an exponential function of the interdot barrier height. As illustrated in Fig. 8(c), the ground-state charge occupancy changes from ð 1 0 ; Þ to ð 0 1 ; Þ as ε changes sign, while around zero detuning the eigenstates are hybridized by t c into antibonding and bonding combinations of the charge states.

For a two-electron DQD (where N 1 þ N 2 ¼ 2 ), the ð 2 0 ; Þ , ð 1 1 ; Þ , and ð 0 2 ; Þ charge states are possible. However, the DQD detuning must be highly biased for the doubly occupied ð 2 0 ; Þ or ð 0 2 ; Þ charge state to become the ground state due to Coulomb repulsion. As a result, the DQD ground state changes from ð 2 0 ; Þ to ð 1 1 ; Þ to ð 0 2 ; Þ as ε increases, as illustrated in Fig. 8(d). In practice, voltage modulation of detuning and tunnel coupling is critical for nearly all spinqubit control modalities.

Spin-spin Heisenberg exchange interactions are a key resource for spin qubits. Microscopically these interactions

FIG. 9. Low-energy orbital spectrum of a one- and two-electron QD in the limit of an infinitesimal magnetic field. (a) A oneelectron QD with a parabolic potential has excited orbital states equally spaced by E orb (only excitations along one dimension are shown for simplicity, and a small Zeeman splitting illustrates the spin degeneracy). (b) For two electrons, the total energy is increased by E add and the lowest spin-singlet and spin-triplet eigenstates are shown with the combinations of the orbital wave functions j g; e i that dominate each state. Note that antisymmetric spin singlets have spatially symmetric orbital wave functions, and vice versa, to satisfy the Pauli exclusion principle. The singlet triplet splitting J is due to the triplet occupation of the excited orbital, though the energy of the latter is lowered from the oneelectron orbital splitting by direct exchange 2 J .

<!-- image -->

arise from the interplay of the Pauli exclusion principle, the external potential, and Coulomb interactions; given its complexity and importance, we refer the interested reader to Sec. IV for a detailed discussion of this topic. Here we illustrate these principles by discussing the energy spectrum of two electrons in a single QD, which is also practically important for spin manipulation and measurement.

As illustrated in Fig. 9, the one-electron states of a single QD include an orbital ground and first excited state, separated in energy by E orb . When a second electron is added to the dot, the spatial wave functions must be either symmetric or antisymmetric under particle exchange, corresponding to spin-singlet and spin-triplet states, respectively. Singlets can have both electrons occupy the same or different spindegenerate orbitals, while spatial antisymmetry requires that triplets must have electrons in separate orbitals. Restricting ourselves to the two lowest orbital states for simplicity, we find that the ground-state spin singlet comes from double occupation of the ground orbital, while the triplet states are higher in energy, as they must place one electron each in the ground and first excited orbitals, as shown in Fig. 9. In the absence of a magnetic field these triplet states are degenerate with energy ET , and the singlet triplet splitting J ¼ ET -ES is positive. This example illustrates the general principle that any two-electron system (even spanning multiple QDs) has a singlet ground state in the absence of magnetic fields (Lieb and Mattis, 1962).

Note that in general, for a two-electron QD, J &lt; E orb , the single-particle orbital splitting, because the triplet state is lowered in energy by the direct Coulomb exchange interaction 2 J . 1 In practice, contributions from other orbitals are also quantitatively important, but they do not substantially change the qualitative physical picture. These arguments can also be extended to include excited valley states, which are often the lowest energy excitations in Si QDs; in such cases, the lowest excited triplet may occupy the excited valley rather than the orbital state, giving rise to a even richer two-electron spectrum (Hada and Eto, 2003; Ercan, Coppersmith, and Friesen, 2021).

## C. Isolating and detecting single charges

In this section we more closely examine spin-qubit designs and the various approaches for detecting the number of charges trapped in a QD. Figure 10 gives an overview of the various single-electron QD designs that have been utilized by the spin-qubit community. Common ' stadiumstyle ' depletion-mode GaAs gate electrode designs are shown in Figs. 10(a) -10(e). The use of undoped Si = SiGe wafers and overlapping gate stacks that gate the dots from the top has been a paradigm shift for the community; one that has arguably propelled the field of Si spin qubits forward in recent years. Top gates allow for tighter confinement, yield larger capacitive coupling to QD electrons, and can be fabricated in multiple layers. Figures 10(f) and 10(g) show examples of Si MOS single-QD and DQD designs (Angus et al. , 2007; Lai et al. , 2011). A device fabricated using STM-based hydrogen passivation lithography is shown in Fig. 10(h) (He et al. , 2019). Figures 10(i) and 10(j) illustrate dual-rail designs, where linear QD arrays are partnered with a parallel channel of charge detectors. The device in Fig. 10(i) is a 1 × 6 Si = SiGe QD array with opposing charge sensors (Ha et al. , 2022). A linear nine-dot array with three charge sensors is shown in Fig. 10(j) (Zajac et al. , 2016). These overlapping gate designs have been successfully extended to small 2D arrays in other material systems, as illustrated by the 2 × 2 Ge QD array in Fig. 10(k) (Hendrickx et al. , 2021). QD fabrication methods are rapidly transitioning from academic-scale lift-off processes to industrycompatible subtractive processes that are more amenable to the development of multilayer devices (Geyer et al. , 2021; Ha et al. , 2022). Si MOS or CMOS nanowire devices fabricated in industrial-grade research foundries are similar to FinFETs, show single-electron-single-qubit operation, and have highlighted the promise of pathways to qubits that may scale in a manner comparable to conventional silicon transistor technologies (Ansaloni et al. , 2020; Zwerver et al. , 2022).

Charge sensing techniques can be adapted for highly sensitive single-shot spin readout by utilizing Pauli spin blockade, as presented for different types of spin qubits in Sec. V (Elzerman et al. , 2004; Barthel et al. , 2009;

FIG. 10. (a) -(c) Few electron single, double, and triple QDs (Ciorga et al. , 2000; Elzerman et al. , 2003; Schröer et al. , 2007). (d) Eightsite 1D QD array (Volk et al. , 2019). (e) 3 × 3 QD array (Mortemousque et al. , 2021). (f),(g) Si MOS single and DQD devices (Angus et al. , 2007; Lai et al. , 2011). (h) Donor device fabricated using STM lithography (He et al. , 2019). (i) Single-layer etch-defined 1 × 6 QD array in Si = SiGe (Ha et al. , 2022). (j) 1 × 9 QD array fabricated using overlapping Al gates on Si = SiGe (Zajac et al. , 2016). (k) Enhancement-mode Ge = GeSi structure (Hendrickx et al. , 2021). Holes are confined in (k), while the remaining devices isolate electrons. Images are sized to share common dimensional scales.

<!-- image -->

Pakkiam et al. , 2018; West et al. , 2019). The QPC charge sensors in the devices shown in Figs. 10(b), 10(c), and 10(e) and QD charge sensors shown in Figs. 10(d) and 10(h) -10(j) are used to measure changes in the charge occupation of QD devices (Field et al. , 1993; DiCarlo et al. , 2004). The measurement bandwidth can be greatly increased using radio-frequency (rf) reflectometry (Schoelkopf et al. , 1998), as later demonstrated with rf QPCs [Fig. 11(b)] and rf sensor dots [Fig. 11(c)] (Reilly et al. , 2007; Barthel et al. , 2010).

fields due to hyperfine or spin-orbit effects. Time-dependent modulation of this Hamiltonian enables coherent single-spin rotations, as detailed in Sec. V.A.2. As SOC is a crucial ingredient to both ˆ g and B eff , we discuss it further here

A recent development is dispersive gate sensing, where microwave reflection off of a QD gate is used to infer the QD charge occupation (Colless et al. , 2013; Urdampilleta et al. , 2019; West et al. , 2019; Zheng et al. , 2019). Dispersive sensing has the potential to scale to larger system sizes, as additional QD or QPC sensors are not needed. Finally, as discussed in Sec. VII, dispersive chargeand spin-state readout can be achieved in the circuit quantum electrodynamics (cQED) architecture [Fig. 11(e)]. Baseband and microwave charge detection approaches have also greatly benefited from the development of cryogenic amplifiers (Vink et al. , 2007; Macklin et al. , 2015).

## D. Zeeman interactions and spin-orbit coupling

Direct magnetic manipulation of the electron spin S in solids is generally described by the Zeeman Hamiltonian

<!-- formula-not-decoded -->

where μ B is the Bohr magneton ( 58 μ eV T). In contrast to = free electrons where the coupling is described by a scalar g factor g ≈ 2 , the crystal field in solids can lead to an anisotropic magnetic response captured by an effective g tensor ˆ g (Slichter, 2010). The effective magnetic field B eff can include externally applied fields as well as internal

FIG. 11. (a) QPC charge detector to probe the charge occupation of a single QD (Field et al. , 1993). (b) rf QPC for fast sensing of a DQD(Reilly et al. , 2007). (c) Fast charge sensing of a DQD using a rf-QD charge sensor (Barthel et al. , 2010). (d) Donor device fabricated using STM lithography and probed using rf reflectometry (Keith, House et al. , 2019). (e) cQED device for detecting charge and spin states in a cavity-coupled InAs nanowire DQD (Petersson et al. , 2012). (f) Dispersive gate sensing of charge states in a FinFET device (Gonzalez-Zalba et al. , 2015).

<!-- image -->

along with the ways that it can be utilized to manipulate individual spins.

SOC arises from the relativistic coupling of spin to electric fields and is described by the Hamiltonian H SO ¼ ð g μ B= /uni210F mc 2 Þð ∇ V × p Þ · S , where V is the electric potential and p is the electron momentum (Zutic, Fabian, and Das Sarma, 2004). In essence, an electron spin moving in a potential experiences an effective momentum-dependent magnetic field B eff SO ; . For spherically symmetric potentials such as the hydrogen atom, this coupling takes the commonly cited isotropic form L S · . In semiconductor heterostructures, the ∇ V term arises from internal crystal fields and potential discontinuities at material interfaces (Zutic, Fabian, and Das Sarma, 2004; Hanson et al. , 2007).

The spin-orbit interaction in bulk solids increases with atomic number; thus, the spin-orbit splitting (equal to the valence band splitting in Fig. 6) is 44 meV in Si but about 300 and 340 meV in Ge and GaAs, respectively. In bulk semiconductors, the p -like valence bands are particularly strongly coupled by SOC, while the effects on s -like conduction band electrons, such as those in GaAs, are weaker but significant for spin-qubit control, for example, by altering the g factor, as described by the Roth formula (Roth, 1960; Zwanenburg et al. , 2013),

<!-- formula-not-decoded -->

where Δ SO and Eg denote the SO splitting in the valence band between the LH or HH and SO bands and the band gap. In bulk silicon, the electron g factor remains close to 2 and is only weakly anisotropic (Roth, 1960), while electrons in bulk GaAs have an isotropic g factor of -0 44 . , which can be further (and anisotropically) modified in QWs (Kogan et al. , 2004; van Beveren et al. , 2005; Yugova et al. , 2007).

Additional SOC effects arise in 2D QWs due to confinement and lowered symmetries, which for electrons are largely described by the effective Hamiltonian 2

<!-- formula-not-decoded -->

where γ R and γ D are the so-called Rashba and Dresselhaus SOCcoefficients. These interactions fundamentally arise from inversion symmetry breaking at different scales. Structural inversion asymmetries (SIAs) due to confining electric fields lead to Rashba couplings, while Dresselhaus interactions relate to the bulk inversion asymmetry (BIA) of the zincblende lattice in GaAs and to heterostructure interface inversion asymmetry (IIA) in Si QWs (Golub and Ivchenko, 2004; Nestoklon et al. , 2008; Prada, Klimeck, and Joynt, 2011). Figure 12(a) illustrates these different sources of microscopic asymmetries and their connection to spin-orbit coupling. Intuitively, a QD electron undergoes cyclotron motion due to an applied magnetic field, leading to SOC effects as its local momentum samples these asymmetries (Jock et al. , 2018). Additional spin-orbit couplings

FIG. 12. (a) Spin-orbit interactions in QDs arise microscopically from the inversion asymmetries due to the bulk crystal structure (BIA), structural effects (SIA) like external fields, and interfaces (IIA). Under an applied magnetic field into the page, the local momentum of the electron wave function rotates (as depicted by arrows), causing local couplings to the atomic-scale gradients induced by these asymmetries that sum to the effective couplings in Eq. (7). (b) Effective spin-orbit field direction for Dresselhausand Rashba-type interactions as a function of in-plane momentum at the Fermi surface k ¼ kF ; see Eq. (8).

<!-- image -->

beyond the linear terms in Eq. (7), such as terms cubic in momentum p , can also be relevant for quantum-confined holes.

The Hamiltonian of Eq. (7) introduces additional g -tensor modulations by coupling the vector potential A of an external magnetic field to spin via the momentum: p → p -e A . For example, choosing the Coulomb gauge for an in-plane magnetic field B ¼ B x ˆ x , one obtains B -dependent terms eB x z ð γ RS x -γ DS y Þ in H SO. If the SO couplings γ R;D contain interfacial contributions, this introduces spin-dependent level shifts that contribute both diagonal and off-diagonal g -tensor terms gxx and gxy . Further g -tensor corrections arise from the admixture of excited orbital states (de Sousa and Das Sarma, 2003; Stano and Fabian, 2005) or valley states in Si QDs (Nestoklon et al. , 2008; Prada, Klimeck, and Joynt, 2011; Veldhorst, Ruskov et al. , 2015; Ruskov et al. , 2018; HarveyCollard et al. , 2019). These couplings can be sensitive to local device disorder, causing interdot g -factor gradients in Si = SiGe (Ferdous et al. , 2018) and in MOS dots for electrons and holes (Voisin et al. , 2016; Jock et al. , 2018; Tanttu et al. , 2019). The effects of SOC on electronic g factors have also been investigated in metallic nanoparticles (Petta and Ralph, 2001, 2002), InAs (Schroer et al. , 2011) and InSb nanowire DQDs (Nadj-Perge et al. , 2012), and self-assembled QDs (Nakaoka, Tarucha, and Arakawa, 2007), among other systems.

The Hamiltonian in Eq. (7) can also be interpreted as the action of a momentum-dependent spin-orbit field,

<!-- formula-not-decoded -->

where θ denotes the angle between p and the ½ 110 /C138 direction (Kavokin, 2001). Figure 12(b) shows the different orientation dependencies of Rashba and Dresselhaus SOC fields. This effective field imparts a directional dependence to matrix

elements involving momentum, including interdot tunneling and intradot orbital spin-flip transitions (Stepanenko et al. , 2012; Hofmann et al. , 2017). This also enables control of electron spins with orbital motion, or EDSR, as first described by Rashba and Efros (2003). For example, if we apply a static magnetic field B 0 ¼ B 0 ˆ z and take ˆ g t ð Þ ¼ g 1 , the orbital motion of the electron with py ð Þ ¼ t p 0 cos ð ω t Þ yields HR ¼ 2 γ Rp 0 cos ð ω t Þ S x , which can be used to drive Rabi oscillations in a rotating frame.

Golovach, Borhani, and Loss (2006) developed the theory for EDSR in 2DEG-based QD systems, while Flindt, Sørensen, and Flensberg (2006) considered EDSR in nanowire devices with strong SOC. Following the argument given by Golovach, Borhani, and Loss (2006), a harmonic QD subject to an oscillating electric field can be described by an effective Hamiltonian H eff ¼ ð 1 = /uni210F Þ½ g μ B B S · þ h ð Þ t · S /C138 , with h ð Þ ¼ t 2 g μ B B × Ω ð Þ t , where Ω ð Þ t is a dimensionless driving field. The coupling strength (and hence the effective Rabi frequency) scales linearly with the amplitude of the oscillating electric field, and the drive is maximal when Ω ð Þ t and B are orthogonal. The driving strength is Ω ð Þ t ∼ r 0 ð Þ t = λ SO, where λ SO ∼ λ /C6 ¼ /uni210F =m /C3 ð γ D /C6 γ R Þ is the spin-orbit length and r 0 ð Þ ¼ t -e E ð Þ t =m /C3 ω 2 0 denotes the shift of the QD due to the electric field, where E ð Þ t and /uni210F ω 0 are the electric field and the confinement energy of the QD.

As an alternative to the ac-driven displacement of the entire electronic wave function in a spin-orbit field, driving ac electric fields can also distort the confining potential, and hence the wave function, which manifests as an effective time modulation of the anisotropic g tensor that can also cause spin rotations (Vrijen et al. , 2000). In general, ˆ g ¼ ˆ g V t ( ð Þ ) , where V t ð Þ is a time-dependent gate voltage on the device (Venitucci et al. , 2018). The first demonstration of spin control using g -tensor resonance was in a 2D GaAs = AlGaAs heterostructure, where the Al concentration was purposely graded to achieve a spatially varying ˆ g (Kato et al. , 2003). Driving the system with an electric field yielded spin rotations that were optically detected using time-resolved Kerr rotations. Recent progress utilizing g -tensor modulation has occurred in hole spin qubits by taking advantage of the natural anisotropies of the valence band, as discussed in Sec. V.E.3.

' Synthetic ' spin-orbit fields can also be induced by translating a spin along an extrinsic magnetic-field gradient, typically generated in QDs by a nearby micromagnet. As proposed by Tokura et al. (2006), this enables ' slanting Zeeman field ' spin resonance or EDSR in a magnetic-field gradient, as external driving electric fields E ac displace the electron within the QD, allowing it to experience the spatially varying transverse magnetic field. The effective ac magneticfield strength can be calculated from perturbation theory as

<!-- formula-not-decoded -->

where E orb is the QD orbital splitting, l orb is the orbital length scale, and b SL ¼ ∂ B z = x ∂ is the transverse magnetic-field gradient. The resulting Rabi frequency f Rabi ¼ g μ BB ac = 2 h is linearly proportional to E ac and b SL (Pioro-Ladriere et al. , 2008).

FIG. 13. (a) The valley splitting of donors in bulk Si from the admixture of the sixfold degenerate valleys (depicted in the Brillouin zone) leads to three sets of states. (b) In Si QDs, the electric fields in MOS and strain in Si = SiGe raises the energy of the four in-plane valleys, and the relevant valley splitting is between the two out-of-plane valleys. (c) The admixture of valley states leads to rapidly varying modulations in the donor ground state, taken from an effective-mass calculation presented by Gamble et al. (2015). (d) The full groundand excited-state wave functions in Si QDs oscillate rapidly due to the intervalley phase. Interference of the valley Bloch functions minimizes the interface overlap for the ground state.

<!-- image -->

Finally, while typical EDSR operation displaces the spin within a single QD, which limits the interaction strength in tightly confined QDs (Hu, Liu, and Nori, 2012), low-power electrical spin control can be achieved by increasing the displacement of the electron through the use of DQDs [Fig. 19(d)]. Benito et al. (2019) considered this ' floppingmode ' spin qubit, which consists of a single electron confined in a semiconductor DQD in the presence of both a homogeneous external magnetic field Bz ˆ and a transverse field gradient created with a micromagnet Δ B x ≈ b SL Δ z= 2 , where 2 Δ B x is the difference in the x component of the magnetic field from the left side to the right side of the DQD separated by Δ z (Benito et al. , 2017). When Δ B x is appreciable, ac driving of the electron across the DQD can lead to low-power single-spin rotations (Croot et al. , 2020).

## E. Valleys

A modification of the simple picture of electron confinement presented in Sec. III.A occurs in Si, where the conduction band features six equivalent minima, referred to as valleys, as shown in Fig. 6(b). The valley degree of freedom can complicate the level structure of quantum-confined states (Sch¨ affler, 1997; Zwanenburg et al. , 2013; Gyure et al. , 2021). For donors in bulk silicon, each valley contributes a degenerate state in the EMA. This degeneracy is lifted by valleyorbit coupling with the tetrahedral donor central-cell potential, leading to a nondegenerate ground state composed of a symmetric linear combination of the six valleys, as shown in Fig. 13(a). By contrast, the four in-plane ð x; y Þ valleys are raised in energy by the strain in Si = SiGe QWs (Sch¨ affler, 1997) and higher subband quantization energy in MOS devices (Ando, Fowler, and Stern, 1982). This leaves two longitudinal kz valleys whose degeneracy is lifted by the heterointerfaces, giving rise to valley splitting, as illustrated in

Fig. 13(b). Controlling and maximizing this splitting is critical for Si-based spin qubits, as it is typically the lowest energy excitation in a single-electron QD.

Valley splitting arises from atomic-scale interactions of the electron with the heterostructure potential, where the EMA is most questionable (Saraiva et al. , 2009; Friesen and Coppersmith, 2010) and numerical full-band calculations using tight binding or pseudopotentials can offer atomistic insight (Boykin et al. , 2004; Zhang et al. , 2013). Nonetheless, many key features can be described within an augmented effective-mass framework, where the full wave function is expanded in terms of envelope and Bloch functions for each relevant valley as

<!-- formula-not-decoded -->

In Eq. (10) k j and uj ð r Þ are the wave vector and periodic parts of the Bloch function, respectively, for the j th valley, and Fj is the envelope function for that valley. For donors in bulk silicon, the Nv sum runs over all six valleys, whereas only the two k /C6 z valleys matter for QDs. Each valley envelope function is the solution of

<!-- formula-not-decoded -->

where Ti is the effective-mass kinetic operator for the i th valley, U ð r Þ is the external potential, and V ij VO is the valleyorbit coupling matrix element, which can be fit to data or estimated from a model potential (Gamble et al. , 2015). For donors, the magnitude of the valley-orbit splitting is mostly set by the central-cell correction, though it is sensitive to local strain. However, the superposition of valley states introduces a complicated interference pattern in the full donor wave function ψ ð r Þ ; see Fig. 13(c). As a result, the interdonor tunnel coupling and exchange coupling are sensitive to the placement of donors in the Si crystal lattice (Koiller, Hu, and Das Sarma, 2002; Gamble et al. , 2015; Salfi et al. , 2018).

If we consider a QW with a sharp heterointerface at z ¼ zi , we can estimate the interfacial intervalley coupling as V VO þ z; -z ¼ v 0 δ ð z -zi Þ (Friesen et al. , 2007; Saraiva et al. , 2009). Taking the valley-free envelope function F z ð Þ as the solution of the intravalley part of Eq. (11), we can evaluate the intervalley matrix element of V VO þ z; -z to obtain the valley mixing Δ VO ¼ v 0 j F zi ð Þj 2 e 2 ik z z i . As this is a complex-valued matrix element, the valley splitting is equal to twice its norm (VS ¼ 2 j Δ VO j ). This simple example illustrates that the valley splitting is dependent on the electron overlap with the interface, which can be increased using vertical electric fields or reducing the QW width.

Experiments show that the tunable out-of-plane electric fields in MOS structures allow for a wide range of valley splittings between 50 and 500 μ eV (Yang et al. , 2013; Gamble et al. , 2016; Petit et al. , 2018). Electric-field tuning is weaker in Si = SiGe QWs due to the smaller conduction band offset, and the valley splitting is most strongly influenced by interface quality and QW width, with values up to 200 -300 μ eV

reported in high-quality interfaces and narrow wells (Borselli et al. , 2011b; Hollmann et al. , 2020; Chen et al. , 2021). Beyond improving the epitaxial quality, other methods have been proposed for achieving uniformly high valley splitting by modulating the Ge content of the barrier or QW regions (Zhang et al. , 2013; McJunkin et al. , 2021).

The valley mixing phase ϕ V ¼ arg ð Δ VO Þ is also significant, as it characterizes the superposition of valleys in the ground state. In general this phase minimizes the ground-state overlap with the interface, lowering its energy, as shown in Fig. 13(d). Changes in this phase due to disorder modify the valley character of the ground and excited states of different QDs, enabling intervalley tunneling (Culcer, Hu, and Sarma, 2010; Burkard and Petta, 2016; Mi, Peterfalvi et al. , 2017; Borjans et al. , 2021).

## F. Hyperfine interactions

Nuclear spins in semiconductors act as both a nuisance and a potential resource for spin qubits. For example, fluctuating hyperfine fields limit T /C3 2 to about 10 ns (Petta et al. , 2005) in GaAs spin qubits, leading to strongly damped Rabi oscillations (Koppens et al. , 2006). On the other hand, electric-field control of the hyperfine coupling constant A featured prominently in Kane s ' proposal (Kane, 1998). As discussed in Sec. II.B, Kane suggested using a gate voltage to adjust the overlap between the donor electron wave function and the 31 P nuclear spin, thereby tuning A . The hyperfine interaction between one electron (carrying spin operator S and orbital angular momentum operator L ) and many nuclei at positions R k carrying spin I k is described by the following Hamiltonian (Abragam, 1961):

<!-- formula-not-decoded -->

In Eq. (12) g 0 is the bare-electron g factor, γ n is the nuclear gyromagnetic ratio, and Ψ ð r Þ is the full electron wave function [not the effective-mass envelope function Fj ð r Þ ]. The last term with δ ð r Þ is the Fermi contact term and is dominant for conduction electrons in both GaAs and Si; it is isotropic, and as such its effects are immune to the orientation of an applied magnetic field relative to the crystalline axes. The magnetic dipole-dipole terms are usually smaller, but they can contribute to the dephasing of electron spin resonance of donors and QDs in Si at low magnetic field (Witzel, Hu, and Das Sarma, 2007; Zhao et al. , 2019).

For the Fermi contact hyperfine interaction, we obtain

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

In Eq. (14) ψ ð R k Þ is the effective-mass envelope wave function at each nucleus location and η is the bunching factor, which captures the microscopic overlap of the Bloch wave function with the nucleus. The envelope wave function is normalized as P k j ψ ð R k Þj 2 ¼ 1 , where the sum is over all nuclear sites in the crystal. For 31 P in Si, as well as 29 Si in Si and all Ga and Al nuclei in GaAs, η has been both measured (Feher, 1959; Paget et al. , 1977) and calculated (Assali et al. , 2011; Philippopoulos, Chesi, and Coish, 2020); however, for some species, such as 73 Ge in SiGe, only estimates are available, typically from spin-qubit experiments (Kerckhoff et al. , 2021).

The dynamics of the nuclei themselves, in particular, the magnetic nuclear dipole-dipole interactions, is also of critical importance in determining how the nuclear spin bath evolves. In the frequent case that one QD electron overlaps with many nuclear spins, the hyperfine interaction behaves as an effective ' Overhauser ' magnetic field that the electron spin experiences, which fluctuates in time due to nuclear dynamics (Taylor et al. , 2007). These effects are central to spin-qubit dephasing and decoherence and are further discussed in Sec. VI.

## IV. SPIN-SPIN INTERACTIONS

The most important physical mechanism leading to interactions between spin qubits is the exchange interaction. Exchange results from a combination of Fermi statistics, electron tunneling, and Coulomb repulsion; a common notation is required to combine these aspects. We must first define a many-particle basis, which is generally done in terms of single-particle basis functions ϕ m ð r Þ χ σ , for spatial orbitals enumerated by m , spin σ ¼ ↑ ↓ ; , and position r . The spinor obeys χσχ † σ 0 ¼ δ σσ 0 . Exchange depends on the Pauli exclusion principle, which means that the multiparticle wave function Ψ m 1 σ 1 m 2 σ 2 … ð r 1 ; r 2 ; … Þ must be fully antisymmetric for arbitrarily labeled electrons 1 2 ; ; … . This may be formally assured via the use of a Slater determinant, i.e.,

<!-- formula-not-decoded -->

Equivalently, this wave function may be described by anticommuting annihilation operators cm σ . The operator cm † σ creates a conduction electron in orbital state ϕ m ð r Þ and spin state σ , and we write

<!-- formula-not-decoded -->

where j vac i is the vacuum containing no electrons. Using this notation, the general many-body Hamiltonian within the EMA approximation [Eq. (3)] reduces to

<!-- formula-not-decoded -->

with the single-particle kinetic and potential energy integral

<!-- formula-not-decoded -->

The diagonal matrix β ¼ diag ð mx -1 ; m y -1 ; m z -1 Þ gives the inverse effective masses and U ð r Þ is the externally applied potential due to gate biasing and built-in electric fields. The general Coulomb integral is

<!-- formula-not-decoded -->

where ε r is the semiconductor relative permittivity (which may in general depend on position); any image effects due to metal gates are ignored for simplicity. Note that both of these integrals are independent of spin.

This notation allows us to distinguish two flavors of the exchange interaction, direct and kinetic. Direct exchange is simply illustrated for two orbitals, labeled 1 and 2, with high spatial overlap, such as orbital states in a common dot or donor. If we ask how the Coulomb interaction impacts the energy of a doubly occupied orbital state, the dominant terms of the Coulomb integral in our single-particle basis can then be broken up into the direct Coulomb term K , corresponding to the case m ≠ n , m ¼ p , and n ¼ l , such as V 1221 , and the direct exchange term J , corresponding to m ¼ n and l ¼ p , such as V 1122 . These two terms separate a pair of two-electron energy levels by the energy K -J = 2 for triplet spin states (spatially antisymmetric, spin symmetric), and by K þ 3 J = 2 for singlet spin states (spatially symmetric, spin antisymmetric). Hence, the combination of Coulomb repulsion and Pauli exclusion raises the energy of the singlet relative to the triplet state by the amount 2 J . Although this direct exchange term is important, leading, in particular, to Hund s rule when orbitals ' are filled, spin-qubit control mostly leverages the distinct and more highly controllable kinetic exchange interaction, which is due to the effect of the Pauli exclusion principle on the spinindependent Tmn and K terms. We address this interaction in Sec. IV.A.

## A. Kinetic exchange in the Fermi-Hubbard hopping model

Kinetic exchange is most easily introduced using the simplified Fermi-Hubbard hopping model, where we presume that electrons are tightly bound into their single-electron orbitals ϕ j ð r Þ . Here ϕ j ð r Þ describes ground-state occupation in dot j , with negligible dot-to-dot Coulomb interactions ( K ) and dot-to-dot direct exchange interactions ( J jk ), as previously discussed. In this approximation, the only relevant Coulomb interaction is the on-site Coulomb interaction with magnitude U ¼ Vjjjj , and the kinetic energy transition matrix Tjk is described in terms of a constant tunnel coupling

t c ¼ T 12 between sites 1 and 2 and voltage-controlled chemical potentials μ j for the diagonal elements Tjj . Constraining the discussion to two electrically charged spin1 = 2 particles (such as electrons) filling two sites and neglecting any magnetic field at first for simplicity, one obtains the Fermi-Hubbard Hamiltonian

<!-- formula-not-decoded -->

The possible linearly independent quantum states described by Eq. (20) can be characterized by their charge and spin configurations. For two charges in two sites, the possible charge configurations are ð 2 0 ; Þ , ð 1 1 ; Þ , and ð 0 2 ; Þ , where ð ni ; n j Þ indicates the numbers of particles on sites 1 and 2. The exclusion principle allows only one spin configuration for ð 2 0 ; Þ and ð 0 2 ; Þ with one spin-up and one spin-down particle, and hence total spin zero (spin singlet). For ð 1 1 ; Þ there are four possibilities, one spin-singlet state and three spin-triplet states. We may choose our energy zero such that μ 1 þ μ 2 ¼ 0 and define the detuning μ 1 -μ 2 ¼ ε . We therefore arrive at

<!-- formula-not-decoded -->

where S indicates that all three states occurring in this Hamiltonian are spin singlets, while the three spin-triplet states are at zero energy. Diagonalizing this Hamiltonian for j t c j ≪ U /C6 ε and j ε j &lt; U , one finds a low-energy hybridized singlet state

<!-- formula-not-decoded -->

up to terms of order t 2 c = U ð /C6 ε Þ 2 with energy -J , where

<!-- formula-not-decoded -->

represents the exchange coupling. Virtual hopping between the two sites lowers the energy of the lowest spin singlet by J relative to the spin-triplet energy (Fig. 14); this is the kinetic exchange interaction.

The other singlet states are at higher energies, separated by roughly U /C6 ε . Excited ð 2 0 ; Þ and ð 0 2 ; Þ triplets (discussed in Sec. III.B) are at similarly high energies. Neglecting those higher states, one finds as the effective Hamiltonian for the ð 1 1 ; Þ charge configuration

<!-- formula-not-decoded -->

where S ¼ S i þ S j denotes the total spin of sites i and j and the constant can be omitted to yield Eq. (1).

FIG. 14. Energy levels, exchange coupling J , and wave functions in a DQD with two particles. (a) Two-particle energy levels as a function of level detuning ε . Tunnel coupling t c leads to level repulsion between the singlet states (blue curves) where the on-site Coulomb energy U equals /C6 ε . J is the energy difference between the low-energy spin singlet and the spin triplets (red curves). Wave functions for (b) the symmetric (i.e., ε ¼ 0 ) and (c) detuned DQDs.

<!-- image -->

## B. Heitler-London and Hund-Mulliken models

To gain a more microscopic understanding of the exchange J in Eq. (1) as well as the parameters of the Fermi-Hubbard model (20), the localization of electrons to a single site realized by a QD in a 2D electron system can be modeled with high accuracy with a harmonic potential V ð r Þ ¼ m ω 2 0 ð x 2 þ y 2 Þ = 2 . Here /uni210F ω 0 is the orbital level spacing of the QD and r ¼ ð x; y Þ . The exchange coupling between spins of electrons residing in two adjacent QDs i and j can then be modeled using a quartic potential V ð r Þ that is locally harmonic in its two minima, with d the interdot spacing. The exchange energy can be obtained as the energy difference of spin-singlet and spin-triplet states for the two-electron orbital Hamiltonian including the Coulomb interaction,

<!-- formula-not-decoded -->

where E B , , and A denote the electric and magnetic fields and the vector potential.

The Heitler-London (HL) method evaluates the energies of the spin-singlet (spin-triplet) trial wave functions with antisymmetric (symmetric) spin state j S i ( T j α i ) and corresponding symmetric (antisymmetric) orbital wave functions in the ð 1 1 ; Þ charge configuration,

<!-- formula-not-decoded -->

in order to guarantee an overall antisymmetric wave function under particle exchange, as required for fermions. Here Σ ¼ h j i j i denotes the overlap between the single-particle groundstate wave functions of the electron localized on adjacent sites i and j ≠ i . The exchange energy J ¼ h Ψ -j H j Ψ -i -h Ψ þj H j Ψ þi decays exponentially with increasing interdot spacing d and magnetic field B for large B . The sign of J can correspond to antiferromagnetic ( J &gt; 0 ) or ferromagnetic ( J &lt; 0 ) coupling. While J &gt; 0 is obligatory for B ¼ 0 in a two-electron system, J can display a sign change from positive to negative at finite B &gt; 0 (Burkard, Loss, and DiVincenzo, 1999; Zumb¨ uhl et al. , 2004) or in multielectron QDs (Martins et al. , 2017; Deng et al. , 2018; Malinowski et al. , 2019).

The main shortcomings of the HL method are that it does not take into account doubly occupied sites and that, while it provides the exchange energy for the Heisenberg Hamiltonian (1), it cannot deliver the parameters of the Hubbard model (20).

The Hund-Mulliken (HM) or molecular-orbital model extends the HL model to include doubly occupied sites by expanding the Hilbert space with two spin-singlet states with orbital wave functions j ii i and j jj i corresponding to the ð 2 0 ; Þ and ð 0 2 ; Þ charge states (Burkard, Loss, and DiVincenzo, 1999). The single-particle states j i i and j j i are first orthonormalized to form a convenient basis. The exchange energy is found as

<!-- formula-not-decoded -->

where Ui ¼ Uj ¼ U &gt; 0 and t ij ¼ t c correspond to the effective on-site Coulomb and tunneling matrix elements in Eq. (20) and J is the direct exchange contribution due to the long-range Coulomb interaction. The approximation holds in the Hubbard limit t c ≪ U . If direct exchange effects can be neglected, we recover the result [Eq. (23)] for ε ¼ 0 .

Extensions of the HL approach include the effect of an inhomogeneous field (de Sousa, Hu, and Das Sarma, 2001), s p -hybridization of single-dot orbitals (Burkard, Loss, and DiVincenzo, 1999), and a symmetry-breaking variational approach (Yannouleas and Landman, 2002). The HM model has been extended to include on-site triplet states (White and Ramon, 2018). Spin-orbit coupling in the presence of a magnetic field can render the exchange coupling anisotropic by contributing a Dzyaloshinskii-Moriya interaction D · ð S i × S j Þ to the Hamiltonian (Kavokin, 2001, 2004; Chutia, Friesen, and Joynt, 2006; Baruffa, Stano, and Fabian, 2010a, 2010b; Liu et al. , 2018).

## C. Full configuration interaction (FCI) calculations of exchange

The previously described approximate analytic models give important insights into the exchange interaction but do not completely capture the impact of band structure and electrostatic confinement. These can be fully accounted for by solving the complete Hamiltonian of Eq. (17), which in general must be done numerically (Reimann and Manninen, 2002). The FCI method is an efficient and systematic way to solve multielectron Hamiltonians and is thus an invaluable tool for understanding exchange interactions in realistic spin-qubit devices.

In the FCI approach, which was first developed for quantum chemistry (Szabo and Ostlund, 1996), a set of 2 K singleparticle spin orbital basis states f ϕ m ð r Þ χ σ g is chosen; these are product states of real-space basis functions and spinors. The former may be convenient analytic functions or eigenstates of the single-particle operator T in Eq. (17) (Rontani, 2006; Joecker et al. , 2021; Anderson et al. , 2022). Often K ≈ 20 -40 orbitals are needed to obtain fully converged dot or donor states. From this single-particle basis, the set of all possible N -particle Slater determinants is constructed and is used as the multielectron basis in which Eq. (17) is diagonalized. All matrix elements of the Hamiltonian in this basis can be expressed solely with single-electron terms and two-electron Coulomb integrals in Eq. (19), which can be computed using the single-particle states ϕ m . This ensures that all exchange and correlation effects are included, provided that a large enough single-particle basis is used.

The resulting N -electron eigenstates are linear combinations of Slater determinants and in the absence of spin-orbit or magnetic gradients can be classified by their spin properties, including total spin S 2 and spin projection S z . For instance, exchange J can be computed from the energy splitting between the lowest two-electron singlet and triplet eigenstates. As the total number of Slater determinants scales as ð 2 K N Þ , FCI calculations become intractable for large N ; however, realistic two- and three-electron systems are well within the capabilities of modern computers.

## D. Discussion of theoretical approaches for calculating exchange

The most basic model for describing controlled exchange is the Fermi-Hubbard hopping model [Eq. (20)], with constant U , detuning ε taken as a linear function of the gate voltage, and the tunnel coupling t c taken as an exponential function of the gate voltage. The model makes predictions for exchange as a function of voltage that are not well replicated by experiments, with the largest deviations at high values of exchange (Reed et al. , 2016). This is unsurprising given the change in character of tunneling barriers as dots combine shown in Fig. 15. Nonetheless, this model is of high value for providing a qualitative understanding in exchange-based experiment design.

The HL model is more quantitative but has some limitations on its validity (Calderón, Koiller, and Das Sarma, 2006; Saraiva, Calderón, and Koiller, 2007); in the weak interdot coupling limit the HL results agree qualitatively with exact diagonalization results, with some quantitative modifications (Melnikov and Leburton, 2006). Experimental results in laterally coupled vertical DQDs show that the HeitlerLondon model forms a good approximation of the twoelectron wave function (van der Wiel et al. , 2006).

Since the HM method takes into account double occupation of sites, its range of validity in charge configuration space is greater than that in the HL approach. The HM predictions were experimentally verified by Hatano et al. (2008). The

FIG. 15. (a) -(d) Simulation of the change in the gray DQD potential (light shading) and pink electron density (dark shading) as the interdot barrier is lowered to increase exchange from approximately 10 kHz to 1 GHz. The potential is generated by solving the Poisson equation for a representative Si = SiGe DQD, which is then used in FCI calculations to obtain the wave functions and J ( K ¼ 30 single-particle eigenstates are used to construct the basis). At practically useful multimegahertz levels of exchange, the electrostatic barrier vanishes and the electrons shift closer together, separated primarily by their Coulomb repulsion.

<!-- image -->

validity of the single-particle description even for multielectron QDs was discussed by Hu and Das Sarma (2001) and Bakker et al. (2015). A comparison of the Hartree-Fock, HM, Heisenberg, and Hubbard models using a double-well potential consisting of a linear combination of Gaussians was made by Hu and Das Sarma (2000).

The determination of J with high accuracy and predictive power is possible with FCI calculations (Hu and Das Sarma, 2001). Since the magnitude and sensitivity of J depend on both material properties (such as the effective mass and permittivity) and device electrostatics, the accuracy depends in turn on accurate modeling of the device structure. The sensitivity of FCIcalculations to material parameters reveals phenomena that may not be obvious using site-based methods, such as the specific charge configurations for ' sweet spots ' where a qubit is resilient against charge noise (Vion et al. , 2002).

In Fig. 15 we compare the numerically computed electrostatic potential and electron density in a typical Si DQD as J increases. Qualitatively we expect to modulate exchange by lowering the tunnel barrier between well-separated electrons; however, in practice the reduced confinement displaces the electrons significantly toward each other as exchange is activated. Indeed, at large J no external potential barrier between the electrons exists, and the Coulomb repulsion itself acts as the effective barrier; hence, the notion of a separable dot basis does not hold, as the electron states transition smoothly between a doubleand a single-dot limit. Such effects are particularly important when one considers simultaneous exchange between multiple pairs of electrons (Pan et al. , 2020; Qiao et al. , 2020; van Diepen et al. , 2021), which requires coordinated spatial displacements. Describing such effects accurately within site-based approaches like the

FIG. 16. PSB in a DQD. (a) Starting with a ð 1 0 ; Þ charge state, ð 2 0 ; Þ singlet initialization occurs by biasing the left QD such that μ S ð 2 0 ; Þ &lt; EF &lt; μ T ð 2 0 ; Þ . Qubit operations and readout are then performed by changing bias positions along the ð 2 0 ; Þ ð -1 1 ; Þ detuning axis. Readout is implemented by detuning such that the singlet ground state is ð 2 0 ; Þ . Interdot tunneling is prohibited by PSB for the spin-triplet state (lower right panel), keeping it in the ð 1 1 ; Þ charge state and allowing spin-to-charge conversion. (b) Charge stability diagram in the vicinity of the ð 2 0 ; Þ ð -1 1 ; Þ anticrossing.

<!-- image -->

previously discussed Fermi-Hubbard, Heitler-London, and Hund-Milliken models requires major modifications.

More generally, numerical FCI calculations are important for describing the effects of electron-electron interactions on the QD level structure, such as Wigner molecule behavior (Ercan, Coppersmith, and Friesen, 2021). Similarly, such calculations can capture the impact on J of locally sensitive parameters such as valley splitting and spin-orbit coupling. FCI calculations have revealed the complex dependency of exchange couplings in donors (Gamble et al. , 2015; Tankasala et al. , 2018; Joecker et al. , 2021) and QDs (Hu and Das Sarma, 2001; Nielsen, Rahman, and Muller, 2012; Gyure et al. , 2021) and have been used to study charge-noise sensitivity (Shim and Tahan, 2018) and mediated exchange in multielectron dots (Nielsen et al. , 2013; Deng and Barnes, 2020).

## E. Pauli spin blockade

An important manifestation of exchange, well understood in the Fermi-Hubbard model discussed in Sec. IV.A, is Pauli spin blockade (PSB). As illustrated in Fig. 16, the ground state of a two-electron DQD can be either the ð 1 1 ; Þ or ð 2 0 ; Þ charge configuration, 3 depending on the DQD level detuning ε ¼ μ 1 -μ 2 . As discussed in Sec. III.B, the ð 2 0 ; Þ ground state is a spin singlet. Thus, when the detuning ε satisfies -U -J max &lt; ε &lt; -U , singlets occupy the ð 2 0 ; Þ charge state,

but the triplet spin states remain in the ð 1 1 ; Þ configuration (Fig. 14). The maximum value of the exchange coupling J max depends on the energy separation between the ground and first excited states in the left QD. In GaAs QDs, this separation typically depends on the orbital energy spacing, which can be of the order of meV. In Si QDs, this energy spacing can depend on the valley splitting, which can be tens to hundreds of μ eV, or the orbital energy spacing, depending on the number of electrons. This phenomenon, wherein spin states map onto distinct charge configurations, constitutes PSB.

The experimental realization and confirmation of PSB first occurred in vertical GaAs DQDs, which are fabricated by etching semiconductor heterostructures (Kouwenhoven and Marcus, 1998). Electrical transport measurements in the first experiments provided evidence for current rectification via PSB (Ono et al. , 2002). Even at that early stage, these experiments were motivated by the possibility of using electron spins as quantum bits. Following the initial demonstration of PSB, pulsed-gate measurements showed that the triplet-singlet relaxation time was much longer than charge relaxation times, thereby confirming the suitability of singlet and triplet states for quantum information purposes (Fujisawa et al. , 2002). PSB was later observed in planar GaAs DQDs with higher electron occupations (Johnson, Petta, and Marcus, 2005) and used in pulsed-gate experiments to measure tripletsinglet relaxation as a function of magnetic field (Johnson et al. , 2005).

PSB is an essential tool for the initialization and readout of many types of spin qubits. Pairs of electrons in the same QD can easily be initialized as spin singlets by enabling electron tunneling between that dot and a nearby electron reservoir (Petta et al. , 2005; Maune et al. , 2012; Botzem et al. , 2018). After initialization, spin singlets can be separated via interdot tunneling into separate dots. If the two electrons are separated adiabatically in the presence of a magnetic gradient, the singlet transitions to a spin-zero product state, thus enabling the straightforward creation of product states (Petta et al. , 2005; Foletti et al. , 2009).

Following evolution of the spin states, these steps can be reversed to project a pair of electrons onto the singlet triplet basis. A simple readout method involves rapidly pulsing the detuning to -U -J max &lt; ε &lt; -U after manipulation. In this state, the singlet triplet energy splitting is extremely sensitive to environmental charge noise. The joint spin state dephases rapidly, and an external charge detector such as a QPC (Petta et al. , 2005) or QD (Barthel et al. , 2009) can extract information about the charge state of the DQD using one of the techniques discussed in Sec. III.C, thus projecting its spin state. If the detuning is pulsed adiabatically with respect to any magnetic gradients, one spin-zero product state maps to the singlet and all other spin states map to the triplet. Generally, PSB readout is straightforward to implement and can enable rapid (microsecond scale or shorter) and highfidelity ( &gt; 98% ) readout fidelity of different qubit types (Reilly et al. , 2007; Barthel et al. , 2009, 2010; Connors, Nelson, and Nichol, 2020; Noiri et al. , 2020; Borjans, Mi, and Petta, 2021). The extension to triple QDs leads to bipolar PSB and state transfer across the system (Busl et al. , 2013).

## F. Long-range couplers

Despite its simplicity and speed, Heisenberg exchange directly couples only nearest-neighbor spins, as it relies on wave function overlap. The requirement for close proximity of the spins (see Fig. 15) poses challenges for the design, fabrication, and operation of large-scale spin-based quantum information processors. This section reviews the various approaches for creating an effective long-range coupling between distant spins. Many of these approaches are in the early stages of development. As such, the experimental characterization of quantum state transfer fidelities using protocols such as randomized benchmarking and gate-set tomography is one important future avenue of research in this area.

## 1. Spin transport, spin swaps, and spin CTAP

Perhaps one of the most conceptually straightforward ways to achieve long-range connectivity is to physically transport qubits across a device. The two main approaches that have been investigated include the use of a surface acoustic wave (SAW) as a conveyor belt for electrons and so-called bucketbrigade-style single-electron shuttling. SAWs are traveling acoustic waves that are typically generated in piezoelectric materials such as GaAs using interdigitated transducers (Datta, 1986). Early experiments in GaAs AlGaAs hetero-= structures demonstrated single-charge (McNeil et al. , 2011) and single-spin transport (Bertrand et al. , 2016) between two QDs [Fig. 17(a)]. Spin-state transport using SAWs was recently demonstrated with high fidelity (Jadot et al. , 2021). SAW implementations of spin-state transport may have long-term limitations due to power dissipation, SAW directionality, and the relatively large size requirements of SAW transducers. Some of these scaling challenges may be alleviated using charge and spin shuttling.

Charge shuttling involves moving an electron through an array of QDs by periodically modulating the confinement potential. Early experimental implementations of charge shuttling in superconducting devices were motivated by the metrological desire to have a high-speed current standard (Keller et al. , 1999). A theoretical proposal by Taylor et al. (2005) suggested using a bucket-brigade charge shuttle to transfer quantum information between semiconductor spin qubits. To achieve charge transfer, the detuning between adjacent QDs is ramped across the interdot charge transition. Early experiments in GaAs demonstrated spin shuttling [Fig. 17(b)] (Baart et al. , 2016; Fujita et al. , 2017). In Si, charge shuttling has been achieved in a linear array of nine QDs (Mills, Zajac et al. , 2019), and spin shuttling has been quantitatively characterized in a Si MOS DQD (Yoneda et al. , 2021). Such combined spin-charge transport in silicon is affected by magnetic-field gradients, valley physics, and spinorbit coupling (Ginzel et al. , 2020). Conveyor-mode charge shuttling through a 400 nm long open channel defined by a series of electrodes was demonstrated by Seidler et al. (2022).

Another approach for achieving spin-state transfer without the physical transfer of charges is to use a sequence of pairwise spin swaps to couple spatially separated spin qubits [Fig. 17(d)]. Spin swaps can be achieved using exchange

FIG. 17. Various approaches for achieving long-range spin coupling. (a) Surface acoustic waves (Bertrand et al. , 2016). (b) Charge transport (Fujita et al. , 2017). (c) Superexchange (Baart et al. , 2017). (d) Spin swaps (Kandel et al. , 2019). (e) Spin CTAP (Gullans and Petta, 2020). (f) Capacitive coupling (Shulman et al. , 2012). (g) Coupling through a spin chain (Bose, 2003).

<!-- image -->

pulses, as proposed in the original Loss-DiVincenzo proposal (Loss and DiVincenzo, 1998; Petta et al. , 2005; Kandel et al. , 2021). Spin swaps can also be implemented in systems with a magnetic-field gradient by periodically modulating the exchange coupling (Nichol et al. , 2017). The first demonstrations were achieved in GaAs, with more recent high-fidelity demonstrations achieved in Si = SiGe QDs (Nichol et al. , 2017; Sigillito, Gullans et al. , 2019; Weinstein et al. , 2023).

Greentree et al. (2004) proposed using coherent transport via adiabatic passage (CTAP), in analogy with stimulated Raman adiabatic passage (STIRAP), which is commonly used in atomic physics (Vitanov et al. , 2017), to achieve charge transfer in QD arrays (Cole et al. , 2008; Ban, Chen, and Platero, 2018). Theoretically, the idea has been extended to spin in a number of ways and is closely related to adiabatic quantum teleportation (Bacon and Flammia, 2009). In exchange-coupled spin chains, adiabatic modulation of the interdot exchange couplings transfer spin states between distant dots without the motion of the electrons themselves (Petrosyan, Nikolopoulos, and Lambropoulos, 2010; Chancellor and Haas, 2012; Oh et al. , 2013). These ideas have been applied to multispin states (Srinivasa, Levy, and Hellberg, 2007; Farooq et al. , 2015; Ban et al. , 2019) and single-spin states in the presence of magnetic gradients (PicóCort´ es, Gallego-Marcos, and Platero, 2019; Gullans and Petta, 2020) [Fig. 17(e)]. Experimental results by Kandel et al. (2021) in GaAs QD arrays give a proof of concept that such adiabatic protocols are viable.

## 2. Superexchange

To create an effective long-range exchange coupling between distant spins, sometimes referred to as superexchange, an additional QD-based mediator (typically a single QD or a chain of occupied QDs) is physically interposed between the two spins of interest. Through a process involving a virtual occupation or excitation of the mediator, the spins coupled to the mediator experience an effective, indirect exchange interaction (Bose, 2003; Friesen et al. , 2007).

When two electrons are coupled to a single-QD mediator [Fig. 17(c)], they can experience an effective tunnel coupling, which depends on the electrochemical potential of the mediator levels, through a virtual tunneling process (Loss and DiVincenzo, 1998). This virtual tunneling process for electrons also creates a virtual exchange interaction for spin states. Although the occupation of the inner QD never physically changes, this scenario creates an indirect coupling between the outer QDs, which preserves the coherence of both charge (Braakman et al. , 2013; Busl et al. , 2013) and spin states (Sánchez, Gallego-Marcos, and Platero, 2014; Sánchez et al. , 2014; Baart et al. , 2017; Malinowski et al. , 2019; Chan et al. , 2021). Direct, coherent spin exchange with mediator electrons is also possible in a multiply occupied QD mediator (Malinowski et al. , 2019).

Superexchange can also occur with a multi-QD mediator (Qiao, Kandel, Fallahi et al. , 2021). One of the most commonly studied systems that is predicted to exhibit superexchange is an extended, strongly coupled spin chain (Wójcik et al. , 2005; Campos Venuti, Degli Esposti Boschi, and Roncaglia, 2006; Oh, Friesen, and Hu, 2010) to which two end spins are weakly coupled. The use of a spin chain as a long-range coupler of spins, also referred to as the spin bus, was examined by Bose (2003, 2007), and extensively by Friesen et al. (2007). They showed that a series chain of N QDs with nearest-neighbor exchange coupling J may provide an effective end-to-end exchange coupling of J= ffiffiffi ffi N p [Fig. 17(g)]. Spin chains have also been considered in the context of donor systems (Mohiyaddin et al. , 2016).

## 3. Capacitive and electric dipole-dipole couplings

Spin-qubit encodings with a charge-qubit character offer a natural coupling scheme with more reach than exchange: the electric field created by charge displacement in one qubit can be used to control the state by displacing the charge of another qubit [Fig. 17(f)]. At short range, this is effectively a quantum cross-capacitance effect; at larger distances, it has the character of an electrically mediated effective dipole-dipole coupling. This translates to a spin coupling due to exchange, field gradients, or spin orbit (Taylor et al. , 2005; Stepanenko and Burkard, 2007; Shulman et al. , 2012; Cayao, Benito, and Burkard, 2020), or due to the hyperfine splitting between electrons and nuclei. The latter effect may benefit the scaling of donor systems since the electric dipole of a donor impurity

may be ' stretched ' by the action of a gate above the device, enabling electric control of a long-distance dipole-dipole coupling. Since this long-range coupling has a weak spatial dependence in comparison to exchange, it may allow donor devices to be fabricated through a controlled ionimplantation process, with the inevitable placement straggle compensated for by gate calibration (Tosi et al. , 2017). Coupling a donor to a dot may offer similar advantages (Harvey-Collard et al. , 2017a). Such spin-relevant capacitive interactions are most effective when coupled to microwave excitations in a resonator, which we address in Secs. IV.F.4 and VII.

## 4. Cavity QED

Three sets of experiments in 2004 demonstrated coherent coupling of solid-state qubits to photons, opening the door to long-range qubit coupling approaches employing photons in the microwave (Wallraff et al. , 2004) and optical regimes (Reithmaier et al. , 2004; Yoshie et al. , 2004). Long-range coupling of two superconducting qubits using a microwave cavity was achieved shortly thereafter (Majer et al. , 2007; Sillanpaa, Park, and Simmonds, 2007). The concept of a cavity bus for coupling superconducting qubits is now widespread (Blais et al. , 2021). Concepts for coupling spin qubits to cavities date back as far as 1999 (Imamoglu et al. , 1999), with a resurgence of theoretical activity taking place again in 2004 -2007 (Childress, Sorensen, and Lukin, 2004; Burkard and Imamoglu, 2006; Trif, Golovach, and Loss, 2008; Jin et al. , 2012). Given the explosive growth of this area of quantum information science, we devote Sec. VII to a review of progress in QD cQED and its potential for providing long-range spin-spin couplings for qubits. We also note for completeness various proposals and experiments demonstrating coupling of superconducting qubits to phonons, an area that is ripe for exploration using QDs (Gustafsson et al. , 2014).

## V. QUANTUM GATES AND QUANTUM CIRCUITS

Over the last two decades, there has been substantial progress developing spin-qubit technologies using the previously discussed interactions and building blocks. In this section, we delve into the theoretical and experimental status of the qubit types introduced in Sec. II. For each qubit type, we discuss how initialization and readout have been physically implemented, strategies followed for performing singleand two-qubit gate operations, and the current status of gate fidelity.

To make quantitative comparisons of gate fidelities in this review, we put particular emphasis on randomized benchmarking (RB). The RB experiment consists of random sequences of quantum gates CRCN … C C 2 1 applied to an initial state where the ð N þ Þ 1 th ' recovery ' gate CR is chosen such that each sequence would, in the absence of error, have the logical action of identity (Magesan, Gambetta, and Emerson, 2011). The Cj ' s are drawn from the Clifford group, the group of gates that transform any multiqubit Pauli operator P (as Cj PCj † ) into another Pauli operator (i.e., the Clifford group is the normalizer of the n -qubit Pauli group). Besides forming a discrete group for computational ease of composing to identity, this choice of operations ' twirls ' generic errors on the gates Cj into a uniform, incoherent, depolarization-like error, enabling a potentially complex error structure to collapse into a singleexponential decay when one averages over the results of the initial-state-probability measurements after many random sequences. The exponential decay constant resulting from simple least-squares fitting of repeated measurements over random circuits provides the single benchmark number, interpreted as an average gate infidelity. The infidelity of a particular Clifford gate, such as the CZ or CNOT entangling gate, can be extracted by measuring the decay while interleaving this gate among all the Clifford gates, and subtracting off the measured decay rate without interleaving. For a review of RB and its variants, see Helsen et al. (2022).

Example randomized benchmarking data from a number of semiconductor spin qubits are shown in Fig. 26; these results are further discussed later. One-qubit (1Q) RB and two-qubit (2Q) RB are important accomplishments, in part because the ability to perform RB, which requires the application of many (preferably thousands) of programmed, calibrated operations on a qubit, shows that the entire system, including cryogenics, control hardware, wiring, and qubits, are coperforming in a way necessary for operation as a future quantum computer. Quantum state, process, and gate-set tomography (GST) (Mohseni, Rezakhani, and Lidar, 2008) use repeated state estimation to identify specific errors and may give complementary information to a qubit s computational utility. Hence, ' these methods provide additional fidelity metrics in Secs. V.A -V.D.

## A. Loss-DiVincenzo single-spin qubits

The control of a single LD qubit follows the same principles as the coherent control of large spin ensembles, a subject with a long history in ESR and nuclear magnetic resonance (NMR) (Abragam, 1961; Slichter, 2010). However, single-spin control faces additional challenges that are absent in ensemble experiments. In bulk ESR and NMR, initialization is typically performed by waiting for the ensemble to thermalize; at typical magnetic fields and temperatures, the resulting polarization is small, but this is compensated for in the measurement signal-to-noise ratio by the large size of the spin ensemble. For single-spin qubits, an initialization routine giving nearly 100% polarization is required, and waiting for thermalization is prohibitively time consuming. Hence, coherent single-spin control requires fast, highfidelity initialization and measurement procedures, and this is where the review of LD qubits begins.

## 1. Initialization and readout

The first experimental demonstration of single-spin readout was achieved by Elzerman et al. (2004) in a GaAs QD. In the same issue of Nature , electrical detection of single-spin resonance in a Si transistor was also reported (Xiao et al. , 2004). Elzerman et al. (2004), and many researchers since, used energy-dependent tunneling, providing a high-enough magnetic field for the Zeeman splitting EZ ¼ g μ BB to greatly

FIG. 18. Energy-dependent tunneling for single-spin initialization and readout of LD qubits. Note that the ground state in GaAs is j ↑ i due to its negative electron g factor. (a) j ↑ i can be initialized by emptying the dot (top panel) and then applying a positive voltage pulse, such that E ↓ &gt; EF &gt; E ↑ (bottom panel). With E ↓ &gt; EF &gt; E ↑ an electron can tunnel only into the spin ground state. (b) After spin manipulations, spin readout is performed by pulsing back to the initialization bias condition. In this example, the presence (absence) of a tunneling event during the measurement period indicates j ↓ i ( j ↑ i ).

<!-- image -->

exceed the thermal energy kBTe for electron temperature Te . 4 Initialization and readout are then achieved through singleelectron tunneling between the QD and an electron reservoir; see Fig. 18. Tunneling is controlled by adjusting the QD energy level relative to the Fermi level of the reservoir EF using time-dependent gate-voltage pulses Vg ð Þ t . These gate voltage pulses can be short ( ∼ 100 ps), as previously demonstrated for charge qubits (Fujisawa et al. , 2002; Hayashi et al. , 2003; Petta et al. , 2004; Petersson et al. , 2010).

The modest g factor in GaAs required Elzerman et al. (2004) to operate with B ¼ 10 T. The gate-voltage pulse sequence for readout, illustrated in Fig. 18, first emptied the QDand then pulled the energy of both spin states below EF to randomly load the QD in j ↓ i or j ↑ i . After waiting for a time t wait , the QD was biased to set E ↓ &gt; EF &gt; E ↑ . Through the process of spin-to-charge conversion, an increase in the QPC current corresponds to a j ↓ i -spin measurement outcome, while no change in current is detected for an j ↑ i spin. Similarly, initialization is achieved by pulling only the spin ground state beneath EF . Single-spin control is then generally implemented deep in Coulomb blockade (see Sec. III.B) to prevent loss of the electron to the reservoir when microwave fields are applied to drive the spin.

Elzerman spin-dependent tunneling imposes several experimental constraints and must be carefully optimized to achieve high-fidelity readout. First, by necessity Elzerman readout is implemented on QDs that are adjacent to charge reservoirs. In contrast, readout of central dots in a large array would require transport of the spin to an end site of the array; see Sec. IV .F. Second, there is a competition in timescales. Since spin readout is achieved using charge detection, the electron must have sufficient time to tunnel off the QD during the readout pulse. If the tunnel rate is too fast compared to the measurement

bandwidth, the charge signal can be missed, while if the rate is too slow, the spin can relax before measurement. Third, Ez ≫ kBTe is required to initialize into the ground state, which implies operation at high field and low temperature. In practice, the spin relaxation rate Γ 1 ¼ 1 =T 1 ∝ B 5 in GaAs, which limits the practical field range (in addition to technical challenges associated with microwave control above 20 GHz). Finally, spin readout is destructive since the j ↓ i spin is lost to the Fermi sea during tunneling. An overview of the conditions required to achieve a readout fidelity F &gt; 99% was given by Keith, Gorman et al. (2019). Mills, Guinn, Feldman et al. (2022) recently achieved F &gt; 99% in Si = SiGe quantum devices.

Another route to achieving high measurement fidelity involves quantum nondemolition (QND) measurements, in which the measurement does not alter the qubit state after its initial projection. In contrast, spin-dependent tunneling always resets the qubit to the ground state and is thus not a QND measurement. QND measurements of a single-spin qubit may be performed by conditionally rotating an ancilla and then measuring the ancilla with spin-dependent tunneling. This process may be repeated many times because resetting the ancilla and performing the conditional rotation do not disturb the qubit state, provided the rotation has a high-enough fidelity. Xue et al. (2019) and Yoneda et al. (2020) demonstrated QND measurements of a single spin, boosting the measurement fidelity from around 80% after a single measurement to around 95% after repeated QND measurements. The circuit quantum electrodynamics device architecture may provide another avenue for QND measurements of single spins (Mi et al. , 2018); see Sec. VII.

## 2. Single-qubit gates

Coherent single-spin control was first demonstrated by Koppens et al. (2006) using ESR in a GaAs DQD. By applying a source-drain bias V SD across the DQD, a ð 1 1 ; Þ polarized spin-triplet state ( T þ or T -) was initialized via transport in the PSB regime. Spin detection in this case occurred by measuring the DQD leakage current I dot as a function of B 0 and the frequency f ac ¼ ω = 2 π of an applied microwave magnetic field B ac generated by driving an ac current through a stripline fabricated adjacent to the DQD. On resonance, when B 0 ¼ /C6 hf ac =g μ B for one of the spins, singlespin ESR drives transitions from the triplet to singlet, lifting PSB and increasing I dot . Measurements revealed a peak in I dot around B ¼ 0 due to hyperfine mixing of the spin states (Johnson et al. , 2005; Jouravlev and Nazarov, 2006; Koppens et al. , 2006), as well as two satellite peaks following the resonance condition B ¼ /C6 hf ac =g μ B [Fig. 19(a)].

The physics of how applied transverse ac magnetic fields drive coherent spin rotations follows conventional ESR. The transverse ac field may be assumed to point along ˆ x , i.e., B 1 ð Þ t ˆ x ¼ B ac cos ð ω t þ ϕ Þ ˆ x , where ϕ is a phase relative to a local oscillator. The effective Hamiltonian in the rotating frame (see the Appendix) is then ˜ H ¼ ð g μ BB 0 -/uni210F ω Þ S z þ g μ B ð B ac = 2 Þ S x . The first term vanishes when the electron spin is driven on resonance (with /uni210F ω ¼ g μ BB 0 ), and the electron spin coherently rotates between j ↑ i and j ↓ i at the Rabi frequency f Rabi ¼ g μ B B ac = h 2 . In the Bloch sphere representation of the LD qubit (see Fig. 2), the static B 0 field points along

FIG. 19. Single-spin rotations driven with (a) an ac magnetic field generated by a coplanar waveguide (Koppens et al. , 2006), (b) an ac electric field in the presence of intrinsic SOC (Nowack et al. , 2007), and (c) an ac electric field in the presence of synthetic SOC (a magnetic-field gradient) (Tokura et al. , 2006; Pioro-Ladriere et al. , 2008). (d) Low-power EDSR in a field gradient can be achieved in the flopping-mode regime of a DQD (Benito et al. , 2019; Croot et al. , 2020).

<!-- image -->

the z axis and leads to Larmor precession of the spin, while the transverse field B 1 ð Þ t points along the x axis for ϕ ¼ 0 and yields a σ x rotation.

For Koppens et al. (2006) and Koppens, Nowack, and Vandersypen (2008), Rabi oscillations at frequencies up to ∼ 10 MHzwere achieved but were highly damped in this first experiment due to hyperfine interactions [lower image in Fig. 19(a)], which move the spin out of resonance and lead to imperfect rotations on the Bloch sphere. Hyperfine coupling is further discussed in Sec. VI. Later silicon-based ESR devices (Pla et al. , 2012; Veldhorst et al. , 2014) achieved comparable Rabi frequencies in a system with reduced hyperfine coupling.

Pioro-Ladriere et al. (2008) demonstrated the feasibility of electrically driving spin rotations using a magnetic-field gradient resulting from a fabricated Co micromagnet. A time-dependent gate voltage V ac periodically moved the electron in the inhomogeneous field of the micromagnet and spin rotations were detected in the PSB leakage current [Fig. 19(c)]. The longitudinal magnetic-field gradient from the magnet allowed the EDSR transitions of both spins to be spectrally resolved. Yoneda et al. (2014) built upon these results by demonstrating &gt; 100 MHz Rabi frequencies, measuring Rabi chevrons in the time domain, and achieving Z gates in the field gradient.

Single-spin control based on ESR raises questions on how to selectively control one qubit in an array. In some LD-based architectures, only global single-spin control is possible (Jones et al. , 2018), but these require high dot-to-dot uniformity. Tunable and selective single-qubit rotations require a unique Larmor resonance for each qubit, for example, by engineering magnetic-field gradients across the device (PioroLadriere et al. , 2008) or through voltage-tunable g factors (Veldhorst et al. , 2014). A key concern of any ESR approach is power dissipation, as device heating often limits the maximum Rabi frequency that can be obtained, thereby encouraging new designs for resonators and approaches for local control with global fields (Vahapoglu et al. , 2021).

One year after ESR control of a single spin in a GaAs QD was shown, Nowack et al. (2007) achieved electrically driven single-spin rotations using EDSR with the intrinsic SOC of GaAs. An ac voltage excitation applied to a gate electrode shifted the orbital wave function, and coherent Rabi oscillations were again detected by measuring I dot in the PSB regime [Fig. 19(b)]. The highest Rabi frequency achieved was 4.7 MHz; nevertheless, this important demonstration spurred the investigation of electrical control in strong spin-orbit systems (see Sec. V.E.2) and added weight to the development of EDSR in the ' artificial SOC ' created by magnetic-field gradients (Tokura et al. , 2006). The transition from ESR to gradient-enabled EDSR not only affords more speed but also provides a clear mechanism for selectivity, since the ac driving field can be applied directly to a QD gate electrode.

A larger displacement of the electron spin in the magneticfield gradient can be achieved in a DQD at ε ¼ 0 , which is known as the flopping mode (Croot et al. , 2020). As illustrated by the measurements in Fig. 19(d), the power required to achieve an EDSR Rabi frequency f Rabi ¼ 6 MHz is reduced by a factor of ∼ 250 at ε ¼ 0 compared to the fardetuned single-dot regime. Flopping-mode operation may greatly reduce power requirements in larger QD device architectures.

## 3. Two-qubit gates

LD qubits use voltage-controlled exchange for two-qubit gates (see Sec. IV), which was first shown to coherently couple two single spins by Petta et al. (2005) [Fig. 20(a)]. In

FIG. 20. Coherent exchange oscillations as first observed in a DQD using PSB readout for (a) GaAs (Petta et al. , 2005) and (b) SiGe (Maune et al. , 2012).

<!-- image -->

this experiment fast ( ∼ 200 ps) exchange oscillations were observed in a GaAs DQD. Time-domain control of J t ð Þ was also used to measure the inhomogeneous spin dephasing time T /C3 2 ∼ 10 ns and the spin-echo decay time T 2 ∼ 1 μ s. Many aspects of the work of Petta et al. (2005) were later repeated with Si = SiGe by Maune et al. (2012) [Fig. 20(b)] with longer coherence times and improved exchange coherence. The limiters of coherence for exchange oscillations are discussed in Sec. VI. These early results featured singlet triplet readout only by PSB; Nowack et al. (2011) extended these results to a GaAs DQD that allowed for independent single-shot readout of each spin with a fidelity of 86%.

True LD operation requires the ability to do both singlespin rotations for single-qubit gates and exchange operations for two-qubit gates, thus completing a universal control set. The exchange Hamiltonian of Eq. (1) couples j ↑↓ i to j ↓↑ i ; an exchange π pulse (activating exchange for a time τ ¼ π /uni210F =J ) realizes a SWAP gate, while an exchange π = 2 pulse generates the entangling square root of the SWAP gate, ffiffiffiffiffiffiffiffiffi ffi SWAP. The effect p of the exchange coupling can be seen by writing Eq. (1) as the projection operator on the spin-singlet state H ¼ -J j S ih S , j with the resulting unitary U ð ϕ Þ ¼ exp ð i ϕ j S ih S jÞ ¼ 1 þð e i ϕ -1 Þj S ih S . j For ϕ ¼ J = τ /uni210F π we find that U ð π Þ ¼ 1 2 -j S ih S j ¼ SWAP, while for ϕ ¼ π = 2 we have U ð π = 2 Þ ¼ ð 1 þ Þ i 1 = 2 þð 1 -i Þ SWAP = 2 ¼ ffiffiffiffiffiffiffiffiffi ffi SWAP. Using this interaction p and single-qubit rotations separately, the CNOT gate (up to a global phase) could then be obtained using the sequence CNOT ¼ e -i π S = y 2 2 e i π S z 1 = 2 e -i π S z 2 = 2 ffiffiffiffiffiffiffiffiffi ffi SWAP p e i π S z 1 ffiffiffiffiffiffiffiffiffi ffi SWAP p e i π S = y 2 2 (Loss and DiVincenzo, 1998).

In practice, however, exchange coupling and local magnetic fields typically act on a register of spin qubits simultaneously, such as in devices with magnetic-field gradients or g -factor variations (Brunner et al. , 2011). Considering two exchangecoupled spins, we can investigate this situation with the Heisenberg Hamiltonian (1), where i; j ¼ 1 2 ; , such that H ¼ J S 1 · S 2 þ g μ B ð B 1 · S 1 þ B 2 · S 2 Þ ; for simplicity we have assumed that the g factor is the same for both sites, although similar principles may be applied with dot-varying g factors (Jock et al. , 2018; Tanttu et al. , 2019). Taking the magnetic-field direction to be the same on both sites (i.e., ˆ z ), H ¼ J S 1 · S 2 þ B S z ð 1 þ S z 2 Þ þ Δ B S z ð 1 -S z 2 Þ = 2 , with B ¼ g μ B ð B 1 þ B 2 Þ = 2 ¼ g μ BB z and Δ B ¼ g μ B ð B 1 -B 2 Þ ¼ g μ B Δ B z . As this Hamiltonian includes two potentially independently controllable noncommuting terms, a variety of adiabatic and diabatic control options exist for achieving entangling twoqubit gates. For example, the direct time evolution of this Hamiltonian with all terms held constant generates the CZ (or CPHASE) gate U CZ ¼ diag ð 1 1 1 ; ; ; -1 Þ ¼ i exp ð -i τ H= /uni210F Þ for a gate time τ ¼ 2 π k= Ω , where /uni210F Ω ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi ffi J 2 þ Δ B 2 p with k ¼ 1 2 ; ; … and J ¼ ð k -n -2 m -1 = 2 Þ /uni210F Ω =k with n; m integers, and B ¼ ð n þ 1 = 2 Þ /uni210F Ω = k 2 (Burkard et al. , 1999). A simple case is k ¼ 1 and n ¼ m ¼ 0 , where CZ can be realized for an arbitrary Δ B ≠ 0 , with B ¼ Δ B= 2 ffiffi ffi 3 p , J ¼ 2 Δ B= ffiffi ffi 3 p , and τ ¼ π /uni210F =J . When combined with single-qubit rotations, this gate lends itself to the implementation of the CNOT gate. An equivalent version of a CZ gate can also be derived from a two-site hopping model (Meunier, Calado, and Vandersypen, 2011).

Watson et al. (2018) utilized a dc exchange pulse to implement a CZ gate in the large magnetic-field gradient regime. Veldhorst et al. (2015) demonstrated full two-qubit control in Si MOS, achieving selective spin control by voltage shifting the g factors, and therefore also the ESR resonance frequencies of the two qubits. Fast CZ gates were implemented by pulsing on exchange (Petit et al. , 2020). Zajac et al. (2018) demonstrated a resonantly driven CNOT gate by lowering the energy of antiparallel spin states ( j ↑↓ i , j ↓↑ i ) relative to the parallel spin states ( j ↑↑ i , j ↓↓ i ) with exchange while applying a single microwave pulse (Russ et al. , 2018). As each of these experiments also included site-selective single-spin initialization, control, and readout, full gate sets for LD qubits were demonstrated in all cases.

## 4. Limits of fidelity: Randomized benchmarking

The transition to Si = SiGe spin qubits from GaAs has resulted in higher overall operation fidelities for LD qubit control. Kawakami et al. (2014) demonstrated spin control in a Si = SiGe DQD with a Co micromagnet, observing f Rabi ∼ 5 MHzand measuring T 2 and T /C3 2 using spin-echo and Ramsey pulse sequences, and later single-qubit randomized benchmarking with 98.1% fidelity (Kawakami et al. , 2016). Using ESR for RB, Veldhorst et al. (2014) showed a single-qubit control fidelity of 99.6% in a 28 Si MOS device (included in Fig. 26). Similarly, Takeda et al. (2016) reported fidelities of 99.6% using EDSR in a field gradient in natural Si = SiGe devices. Veldhorst et al. (2015) extended these results to a Si MOS DQD, where selective ESR control of two spins was achieved. Zajac et al. (2018) used RB to demonstrate singlequbit fidelities of 99.3% and 99.7% in a two-qubit Si = SiGe device. Isotopic enrichment has led to continued increases in single-qubit gate fidelity, as discussed in Sec. V.A.4. Using isotopically enriched Si = SiGe, Yoneda et al. (2018) achieved single-qubit fidelities exceeding 99.9%. Characterization of the electrical noise in this device indicates that coherence is limited by charge motion in the presence of the micromagnet field gradient. Yang et al. (2019) achieved single-qubit Clifford fidelities of 99.96% in a Si MOS device using improved pulse engineering. Recently Xue et al. (2021) reported single-gate fidelities of 99.69% in a Si = SiGe QD that was notable for being operated by a cryogenic control chip.

Early attempts to characterize two-qubit gate fidelities employed quantum state tomography. Zajac et al. (2018) used the resonant CNOT gate to generate a Bell state with fidelity F ¼ 78% . Watson et al. (2018) achieved Bell-state fidelities up to 90% using decoupled CZ gates and demonstrated a resonant CNOT gate. Both of these experiments had to correct the tomography for significant state preparation and measurement (SPAM) errors. Huang et al. (2019) more rigorously characterized two-qubit gate fidelities using RB in a Si MOS DQD, with an average Clifford (CROT) gate fidelity of 94.7% (98%) achieved in a regime with always-on exchange. Xue et al. (2019) implemented a variation on RB called character RB, enabling the interleaving of a two-qubit gate among single-qubit Clifford gates, and obtained twoqubit gate fidelity estimates of 92%. Xue et al. (2022) recently achieved a two-qubit gate fidelity of 99.65% using pulsed exchange. In the regime of always-on exchange, Noiri et al.

(2022) also achieved RB with &gt; 99% two-qubit gates. Highfidelity overall operation of two qubits in a six QD device was obtained by Mills, Guinn, Gullans et al. (2022), with sequential single-spin rotation F &gt; 99 9% . , simultaneous single-spin rotation F &gt; 99% , and a two-qubit CZ F &gt; 99 8% . . SPAM errors in this demonstration were &lt; 3% . Fidelities are expected to further increase with reduced charge noise and higher levels of isotopic enrichment.

Efforts to control hole spins in Ge = GeSi heterostructures have advanced significantly in a short period of time. Owing to strong SOC, hole spins can be manipulated electrically without the need for a separate ESR drive line or micromagnet. The smaller effective mass of holes in Ge also relaxes nanofabrication requirements, as the QDs are larger than in Si. Hendrickx, Franke et al. (2020) achieved short ( ∼ 20 ns) single-hole-spin rotations with F &gt; 99 3% . and a two-qubit exchange gate. Multiqubit operations have been implemented in a 2 × 2 Ge QD array, culminating in the generation of a four-qubit Greenberger-Horne-Zeilinger state (Hendrickx et al. , 2021).

## B. Donor spin qubits

When Kane (1998) was published, it was different from contemporary proposals based on QDs since basic GaAs QD devices had already been fabricated (Kouwenhoven and Marcus, 1998). While doped Si is common, the isolation of single donors near gated nanostructures for single-electron control and measurement presented novel fabrication challenges. A number of groups have faced this challenge using bottom-up STM lithography on hydrogen passivated silicon surfaces, enabling the placement of atoms nearly one at a time into designated locations as both qubits and gates (Lyding et al. , 1994; Schofield et al. , 2003; Bussmann et al. , 2015). Alternatively, Morello et al. (2010) showed that the approach of detected ion implantation of P into MOS-style devices allows single-donor-spin measurements and subsequent control. Electrostatically gated dot-donor devices are also being explored (Harvey-Collard et al. , 2017a) and may provide unique opportunities for nuclear spin readout and coupling to microwave photons (Mielke, Petta, and Burkard, 2021). The ion-implantation and STM lithography approaches have both shown steady progress in controlling single-electron spin states, the nuclear spin of the donor, and the exchange coupling between donors, as we discuss in this section, concluding with a discussion of gate fidelities.

## 1. Donor electron spin initialization and readout

Morello et al. (2010) used the Elzerman energy-dependent tunneling approach to spin initialization and readout discussed in Sec. V.A.1, borrowing heavily from developments in QDs [Fig. 21(a)]. A single-electron transistor (SET) was fabricated next to a 90 × 90 nm 2 region that was implanted with P donors, and voltage control of a nearby plunger gate was used to control the electronic state of the donor. Single-shot measurements allowed mapping of the electron spin lifetime as a function of magnetic field, with T 1 ¼ 6 s obtained at B ¼ 1 5 . T, and the spin readout visibility was estimated to be

FIG. 21. (a) Single-shot readout of a donor-bound electron spin (Morello et al. , 2010). (b) Rabi oscillations of a donor-bound electron spin (Pla et al. , 2012). (c) Exchange oscillations from a two-donor device. (He et al. , 2019). (d) Coherence of three-qubit Greenberger-Horne-Zeilinger states (Madzik et al. , 2022).

<!-- image -->

around 92%. The use of cryogenic amplifiers near donor qubits has enabled high-fidelity electron spin readout in these systems (Tracy et al. , 2016).

Spin readout has also been achieved in donor devices fabricated with STM lithography. Broome et al. (2017) placed a small cluster of donor atoms next to a SET and demonstrated F ¼ 98 4% . single-shot readout of a donor singlet triplet qubit. Koch et al. (2019) later achieved an average measurement fidelity of F ¼ 97 9% . for single-spin Elzerman readout using a SET, and Keith, House et al. (2019) showed F ¼ 97% measurement fidelity with a 1 5 . μ s SET measurement time. Dispersive gate-based sensing has also been explored, but, as with QD systems, dispersive sensing yields lower fidelities and measurement bandwidths. Pakkiam et al. (2018) dispersively probed a donor singlet triplet qubit with a moderate fidelity F ¼ 82 9% . and 3 kHz bandwidth.

## 2. Donor electron spin single-qubit gates

Coherent control of a donor electron spin was achieved by Pla et al. (2012) using a natural Si substrate. The electron spin Rabi oscillations [see Fig. 21(b)] were highly damped due to hyperfine interactions, which is reminiscent of the first GaAs QD single-spin Rabi oscillations (Koppens et al. , 2006). Isotopically enriched samples were next investigated using devices where 31 P ions were implanted in an isotopically

enriched layer of 28 Si with an 800 ppm residual concentration of 29 Si (Muhonen et al. , 2014). The use of a Hahn echo pulse sequence extended the coherence time out to ∼ 1 ms. More complex dynamical decoupling pulse sequences were shown to extend the coherence time out to nearly 1 s (Muhonen et al. , 2014). Later experiments demonstrated a factor of ∼ 10 enhancement of the coherence time for dressed electronic spin states (Laucht et al. , 2017).

Tettamanzi et al. (2017) took a first step toward donor quantum control by demonstrating pulse spectroscopy of a single P atom at frequencies up to 13 GHz. These experiments demonstrated that microwave signals could be transmitted down heavily doped P leads in silicon. Hile et al. (2018) later probed ESR spectra of a single P donor and 2P molecule, and Koch et al. (2019) then extended these results to single-shot measurements of a single P donor qubit using a SET.

Fricke et al. (2021) used STM lithography to pattern a P donor molecule in natural-abundance silicon. Coherent electron spin control was achieved with Rabi frequencies of the order of 1 MHz. The Ramsey T /C3 2 ∼ 300 ns was extended out to T 2 ∼ 300 μ s using a Hahn echo pulse sequence.

## 3. Donor nuclear spin control and readout

Kane (1998) had envisioned the qubit as the 31 P nuclear spin, not the electron; the electron was used for readout and control leveraging the 31 P hyperfine coupling of A ≈ 114 MHz (Sec. III.F). Pla et al. (2013) accessed the nuclear spin using an ESR measurement time much less than the nuclear spin-flip time. This device was able to resolve ESR transition frequencies that jumped between f ⇑ ¼ g μ BB=h þ A= 2 and f ⇓ ¼ g μ BB=h -A= 2 . These jumps were interpreted as being due to flips of the nuclear spin state (denoted by ⇑ and ⇓ ). A broadband antenna on the device allowed for direct driving of the donor atom nuclear spin, with dephasing times 10 4 times longer than for the donor electron spin. Since the readout of the donor nuclear spin is QND, nuclear spin readout fidelities &gt; 99 8% . have been achieved (Pla et al. , 2013).

In a follow-up experiment in 28 Si, nuclear spin control with a fidelity exceeding 99.99% was demonstrated. Muhonen et al. (2014) showed Carr-Purcell-MeiboomGill (commonly referred to as CPMG) dynamic decoupling pulse sequences extended the nuclear spin coherence time beyond 30 s. Wolfowicz et al. (2014) and Laucht et al. (2015) showed that the Larmor resonances of each donor site could be selectively controlled by pushing the electron closer to its 31 P donor using a gate, as proposed by Kane, enabling a global ESR field to selectively control one site at a time.

The 31 P donor is a nuclear spin I ¼ 1 = 2 system, but nuclei with spin I &gt; 1 = 2 such as I ¼ 7 2 = 123 Sb allow for richer and more complicated control possibilities. The uniform Zeeman splitting between adjacent states of different m is shifted by the electric quadrupole interaction due to local strain, allowing individual addressability of all 2 I þ 1 ¼ 8 nuclear spin transitions (Franke et al. , 2016). Modulation of these quadrupole splittings by an ac electric field drives Rabi oscillations between transitions. Sigillito et al. (2017) reported evidence for electric quadrupole transitions in 75 As nuclei. Recently Asaad et al. (2020) demonstrated coherent control of the 123 Sb donor and a dephasing time T /C3 2 ≈ 92 ms. Wolfowicz et al. (2013) also demonstrated the use of clock transitions in highspin nuclei, achieving second-scale coherence times. Another interesting area of research involves the development of acceptor-based devices, which may benefit from enhanced SOC (Salfi et al. , 2016).

## 4. Two-qubit gates

Kane (1998) proposed coupling between donor nuclear spin qubits mediated via exchange between the electron spins on each donor. However, it was soon noted that atomic-scale oscillations in exchange due to multivalley interference would render this interaction highly sensitive to atomic placement (Koiller, Hu, and Das Sarma, 2001; Wellard et al. , 2003; Gamble et al. , 2015; Joecker et al. , 2021), requiring an architecture tolerant of such variation, extremely careful donor placement, or the use of asymmetric donor clusters with more than one phosphorous atom (Wang et al. , 2016). A variety of demonstrations of exchange on various donor devices have helped show a range of possibilities beyond Kane s original ' proposal. Weber et al. (2014) used donor devices fabricated with STM-based lithography to show exchange and PSB of two electrons on the same donor site, Gorman et al. (2016) demonstrated methods to calibrate tunnel couplings, and Broome et al. (2017) performed high-fidelity singlet triplet (PSB) readout. With sufficient control over the donor positions and of tunnel couplings, Broome et al. (2018) were able to observe two-electron correlations and He et al. (2019) showed fast coherent exchange oscillations between donor clusters [Fig. 21(c)]. As with the first exchange oscillations in GaAs and Si = SiGe DQDs, the oscillations were heavily damped due to charge noise (Petta et al. , 2005; Maune et al. , 2012).

Experiments on implanted donor devices have also demonstrated two-qubit operations. Madzik et al. (2021) demonstrated conditional operation of exchange-coupled donor qubits building on the theoretical proposal by Kalra et al. (2014). Madzik et al. (2022) exploited the hyperfine coupling between two donor nuclear spins coupled to the same electron to implement a two-qubit gate between nuclear spins based on geometric phases with a fidelity above 99%; see Fig. 21(d).

Tosi et al. (2017) proposed using electric-dipole coupling to couple electron spin-nuclear spin flip-flop qubits, an approach that could be extended to enable coupling via superconducting cavities; see Sec. VII. Basic operation of the flip-flop qubit was demonstrated by Savytskyy et al. (2023).

An alternative coupling relevant to donors is the magnetic dipole-dipole coupling between electrons, as its long-range, magnetic nature avoids the atomic precision fabrication requirement for exchange. Proposals to exploit this interaction through isotopic engineering and implanted donors employ a variety of methods to manage the interaction, including selective ionization and mechanical motion (Ladd et al. , 2002; de Sousa, Delgado, and Das Sarma, 2004; Hill et al. , 2015; O Gorman ' et al. , 2016); however, execution of

any such proposal will require devices with exquisite coherence.

## 5. Limits of fidelity: Randomized benchmarking

The demanding nanoscale fabrication requirements of donor devices have impeded their progress relative to gatedefined QDs. RB and GST have thus far been limited to ion-implanted devices, which are capable of supporting noteworthy quantum control fidelities. Muhonen et al. (2015) performed comprehensive measurements of the electron and nuclear spin-qubit gate fidelities using 1Q RB (included in Fig. 26). Average electron spin gate fidelities exceeded 99.95%, while the nuclear spin fidelity was 99.99%. The dependence of the fidelity on pulse power and shape in these early experiments suggests that the overall fidelities are limited by quantum control hardware constraints, not the intrinsic performance of the qubit.

Recent characterization of two P ion-implanted donors coupled by a single electron using GST have demonstrated single-qubit fidelities of up to 99.93% and two-qubit fidelities of 99.2% (Madzik et al. , 2022). GST allows for the distinction of coherent (stochastic) errors that transfer amplitude (probability) to erroneous states, as well as relational errors, where the errors incurred are dependent on the history of prior gate operations. Madzik et al. (2022) found evidence for coherent ZZ errors that were attributed to off-resonant leakage of microwave power near ESR frequencies. While an exchange gate has been demonstrated with a STM fabricated device (He et al. , 2019), the quantitative characterization of the exchange gate through RB remains an important goal for the donor spinqubit platform.

## C. Singlet triplet qubits

The early demonstration of coherent exchange in a GaAs DQD (Petta et al. , 2005) showed not only the potential for two-qubit operations of LD qubits but also basic single-axis control of the ST 0 qubit. The data in Fig. 20 show that the DQD level detuning ε enables control over the exchange coupling J , which is the energy separation between the S and T 0 qubit states, as discussed in Sec. IV. In these early demonstrations, the longitudinal magnetic-field gradient experienced by the two spins Δ B z , which lifts the degeneracy between the flip-flop states j ↑↓ i ¼ ðj S i þ j T 0 iÞ = ffiffi ffi 2 p and j ↓↑ i ¼ ðj T 0 i -j S iÞ = ffiffi ffi 2 p , was provided by the random hyperfine fields of nuclear spins in the device.

Figure 22 also shows that, at a particular value of ε , the j S i and j T þi states become degenerate where J compensates the Zeeman splitting between triplet states EZ . Near this detuning, the ST þ qubit is formed. Here again we have the controllable qubit energy splitting E ST þ ¼ Ez -J and the transverse coupling Δ ST can be introduced by various mechanisms, such as microscopic hyperfine or spin-orbit interactions (Taylor et al. , 2007; Petta, Lu, and Gossard, 2010; Stepanenko et al. , 2012; Nichol et al. , 2015). For the ST þ qubit we are assuming that we have a device made with a negative g -factor material, such as GaAs, where j T þi is lower in energy than j T -i . For a positive g -factor material such as Si, the natural choice is a ST -qubit.

FIG. 22. (a) Energy-level diagram for two electrons in a DQD. ε is the energy-level detuning, and ð 1 1 ; Þ and ð 2 0 ; Þ indicate the DQD charge configurations. The Zeeman and exchange splittings are g μ BB and J ð ε Þ , where B denotes the magnetic field. The spin states are j S i¼ðj ↑↓ i -j ↓↑ iÞ = ffiffi ffi 2 p , j T 0 i¼ðj ↑↓ iþ j ↓↑ iÞ = ffiffi ffi 2 p , j T þi ¼ j ↑↑ i , and j T -i ¼ j ↓↓ i . Singlet triplet oscillations driven by (b) g -factor differences between dots (Liu et al. , 2021), (c) micromagnets (Wu et al. , 2014), and (d) dynamic nuclear polarization (Foletti et al. , 2009).

<!-- image -->

## 1. Initialization and readout

ST 0 and ST þ qubit demonstrations (Petta et al. , 2005; Foletti et al. , 2009; Maune et al. , 2012; Botzem et al. , 2018) use PSB for initialization and readout (Sec. IV.E). The high fidelity of PSB initialization and readout in DQDs is enabled by the large exchange coupling in the ð 2 0 ; Þ charge configuration. The energy splitting from the singlet ground state to the excited ð 2 0 ; Þ triplet states was shown to be a meVor higher in energy in GaAs and tens to hundreds of μ eV higher in energy in Si QDs, as discussed in Sec. IV.A. These energy scales are larger than kBTe at typical electron temperatures. Following initialization, the electrons are usually separated via tunneling to the ð 1 1 ; Þ charge state.

Experiments have leveraged adiabatic and nonadiabatic separation to complete qubit control; see the energy-level diagram in Fig. 22(a). When electron separation occurs rapidly with respect to any magnetic gradients, tunneling preserves the spin state, so an initialized singlet remains a singlet (Petta et al. , 2005; Foletti et al. , 2009; Maune et al. , 2012; Botzem et al. , 2018). If the separation occurs slowly with respect to magnetic gradients, the singlet state transitions to the lower-energy spin-zero product state (Petta et al. , 2005; Foletti et al. , 2009). Hence, two orthogonal ST -qubit basis 0 initializations are available, and pulsing detuning ε or tunnel coupling t c enables characterization of the exchange coupling. The spin-to-charge conversion offered by PSB reduces spin readout to dot-selective charge readout. A significant number of optimizations have been explored to increase readout speed and fidelity (Reilly et al. , 2007; Barthel et al. , 2009, 2010; Connors, Nelson, and Nichol, 2020; Noiri et al. ,

2020; Borjans, Mi, and Petta, 2021). A key trade-off is that while larger gradient B fields can drive faster singlequbit operations, these persistent gradients reduce the fidelity of PSB readout due to enhanced spin relaxation (Barthel et al. , 2012). Latched readout protocols first demonstrated with charge qubits (Petersson et al. , 2010) have been extended to singlet triplet qubits and can overcome this limitation (Studenikin et al. , 2012; Harvey-Collard et al. , 2018; Orona et al. , 2018).

## 2. Single-qubit gates

As described in Sec. II.C, the Hamiltonian [Eq. (2)] governing the control of ST 0 qubits includes an exchangedriven σ z term and a σ x term that is set by an effective magnetic-field gradient. Full two-axis control of the ST 0 -qubit Bloch vector therefore requires control of exchange, which can be achieved by adjusting interdot barrier heights or DQD level detunings and magnetic-field gradients. Approaches to generate the required magnetic-field gradients are varied and include dynamic nuclear polarization (DNP) (Foletti et al. , 2009; Bluhm et al. , 2010), the use of permanent micromagnets (Wu et al. , 2014; Fogarty et al. , 2018), g -factor differences (Harvey-Collard et al. , 2017b; Jock et al. , 2018; Liu et al. , 2021), and spin-valley coupling (Jock et al. , 2022). Data acquired using some of these approaches are shown in Figs. 22(b) -22(d). We elaborate on these approaches later.

For gate-defined spin qubits, typical exchange couplings are in the megahertz to gigahertz range. Coherent exchange rotations are achieved by applying fast gate-voltage pulses ( &lt; 1 ns to tens of ns). Voltage pulses of the opposite sign applied to the DQD plunger gates can rapidly change the detuning to configurations with large J , as first demonstrated by Petta et al. (2005). This control at fixed tunnel coupling is capable of generating arbitrary single-qubit gates (Hanson and Burkard, 2007). However, detuning-controlled exchange oscillations are vulnerable to charge noise, and the number of coherent oscillations is typically around ten (Petta et al. , 2005; Maune et al. , 2012; Dial et al. , 2013; Fogarty et al. , 2018; He et al. , 2019). Exchange oscillations can also be observed with larger numbers of electrons in the QDs in configurations where the inner electrons form a ' frozen core ' (Barnes et al. , 2011; Higginbotham, Kuemmeth et al. , 2014). Bertrand et al. (2015) and Martins et al. (2016), working in GaAs DQDs, and Reed et al. (2016), working in isotopically enhanced Si triple quantum dots (TQDs), showed that improved qubit control results when the barrier height between electrons is pulsed to smaller values, as simulated in Fig. 15. The improvement occurs because the Coulombdominated exchange coupling is first-order insensitive to potential fluctuations in this ' symmetric ' mode. As a result, the quality factor of exchange oscillations is higher than that for detuning-controlled oscillations, although the magnitude of the required voltage pulses is also significantly higher. Both of these methods of creating exchange coupling suffice to generate σ z rotations on the ST 0 Bloch sphere. In principle, both methods can also be used to control ST þ qubits, though detuning sweeps have been used more frequently in these systems (Petta, Lu, and Gossard, 2010; Ribeiro, Petta, and Burkard, 2010).

Full control of the ST 0 -qubit Bloch vector also requires an effective magnetic-field gradient for σ x rotations. The use of hyperfine fields is particularly convenient for GaAs QDs due to the many spinful nuclei. A challenge with using hyperfine as a basis of control is that, as discussed in Sec. VI.B, the nuclear hyperfine field fluctuates randomly because the nuclear Zeeman energy is so small, typically less than 1 mK for fields of the order of 1 T, and magnetic dipoledipole interactions lead to nuclear spin diffusion. However, various mechanisms can be employed to enhance and stabilize the nuclear polarization via the electron spins (Petta et al. , 2008; Foletti et al. , 2009; Bluhm et al. , 2010; Shulman et al. , 2012; Nichol et al. , 2017). These processes are collectively called DNP (Abragam and Goldman, 1978).

In singlet triplet qubits, DNP usually involves the degeneracy point between the j S i and j T þi states. This degeneracy is lifted by a transverse gradient (Taylor et al. , 2007; Petta, Lu, and Gossard, 2010; Stepanenko et al. , 2012; Nichol et al. , 2015), which is typically generated via the hyperfine interaction between the electron and nuclear spins [Fig. 22(a)]. As the DQD is adiabatically detuned across the ST þ avoided crossing, the electrons transition from j S i to j T þi via the transverse Overhauser field and a nuclear spin must change its state to conserve angular momentum in the electron-nuclear subsystem (Ribeiro and Burkard, 2009; Brataas and Rashba, 2011; Neder, Rudner, and Halperin, 2014). If repeated rapidly enough, this process can flip a large number of nuclear spins and can be used to ' pump ' both the average ð B z 1 þ B z 2 Þ = 2 (Petta et al. , 2008) and difference ð B z 2 -B z 1 Þ longitudinal magnetic fields of the DQD (Foletti et al. , 2009; Bluhm et al. , 2010; Shulman et al. , 2012; Nichol et al. , 2015, 2017). It is not surprising that the average field should be affected, if one assumes that this process flips nuclear spins in both dots with approximately the same probability. However, the underlying mechanism that builds up the difference field remains an active area of theoretical research (Gullans et al. , 2010, 2013).

In addition to dynamic nuclear polarization, micromagnets can also be used to generate σ x rotations (Wu et al. , 2014; Fogarty et al. , 2018). Although additional fabrication is required, micromagnets eliminate the requirement for DNP, which adds experimental overhead. In Si ST 0 qubits, g -factor differences between dots can naturally lead to the existence of a σ x term, even in the presence of a uniform magnetic field (Kerckhoff et al. , 2021; Liu et al. , 2021). Finally, when the Zeeman energy equals a valley splitting, the resonance that occurs between different valley states, together with spinvalley coupling, can also enable rapid σ x rotations in Si ST 0 qubits (Jock et al. , 2022).

Dynamical decoupling experiments illustrate the potential for using fluctuating hyperfine fields for full ST 0 control. Bluhm et al. (2011) and Malinowski et al. (2017) used exchange pulses to decouple ST 0 qubits from magnetic noise, resulting in a nearly 5 order of magnitude improvement in coherence. These experiments, in addition to later studies in SiGe (Kerckhoff et al. , 2021), also uncover the spectrum of the Overhauser field, revealing the significance of the Larmor precession of the individual nuclei (Neder et al. , 2011). Stabilized magnetic gradients also enable ST 0 qubits to be decoupled from charge noise (Dial et al. , 2013; Shulman

et al. , 2014) as well as charge-noise spectroscopy (Dial et al. , 2013; Connors et al. , 2022; Jock et al. , 2022).

For ST þ qubits, the σ x interaction can arise from transverse magnetic gradients (Taylor et al. , 2007; Petta, Lu, and Gossard, 2010; Stepanenko et al. , 2012; Nichol et al. , 2015), which can be created via hyperfine fields or micromagnets. However, unlike longitudinal gradients, transverse gradients are not amenable to DNP and are thus difficult to stabilize. Transverse gradients also contain spectral components at the Larmor precession frequencies of the individual nuclei (Nichol et al. , 2015). As a result, the naturally occurring hyperfine polarization is typically not stable enough to generate usable x rotations. Spin-orbit coupling can also induce a ST þ splitting (Stepanenko et al. , 2012; Nichol et al. , 2015), but detuning charge noise in this case can create substantial decoherence. In silicon, spinvalley coupling can induce a sizable ST -splitting (Cai et al. , 2023), which enables universal quantum control. As an alternative to conventional qubit manipulation, repeated Landau-Zener sweeps through the avoided crossing were proposed as a mechanism to achieve universal control of ST þ qubits (Petta, Lu, and Gossard, 2010; Ribeiro, Petta, and Burkard, 2010). The axis of rotation on the Bloch sphere in this mode is controlled by the timing of two consecutive Landau-Zener sweeps.

In part to avoid issues associated with charge noise, a variant of the ST 0 qubit, the ' resonantly driven ST 0 qubit, ' which is related to the ' flip-flop qubit ' (Tosi et al. , 2017), was developed (Klauser, Coish, and Loss, 2006; Shulman et al. , 2014; Nichol et al. , 2017; Takeda et al. , 2020). This qubit s basis states ' j ↑↓ i and j ↓↑ i are equal superpositions of the original singlet and triplet states. In such a resonantly driven ST 0 qubit, a large magnetic gradient, from either a micromagnet or hyperfine fields, generates the primary qubit energy splitting. An oscillating voltage applied to a plunger or barrier gate creates an oscillating exchange splitting. If driven at a frequency corresponding to the magnetic gradient, this oscillating exchange coupling can drive transitions. Because the qubit energy splitting does not depend on electric fields, decoherence due to charge noise can be suppressed.

## 3. Two-qubit gates

van Weperen et al. (2011) measured the shift in the exchange oscillation frequency of one ST 0 qubit due to changes in the charge configuration of another nearby ST 0 qubit, providing the capacitive interaction for a two-qubit gate (Taylor et al. , 2005). The electrostatic interaction translates to spin, as with spin initialization and readout, via PSB. Consider two ST 0 qubits in proximity. The first qubit will, depending on its state (singlet or triplet), have a slightly different charge configuration [ ð 0 2 ; Þ or ð 1 1 ; Þ ]. As a result, the second qubit experiences a different electrostatic potential and thus energy splitting J that depends on the state of the first qubit. This leads to an effective Ising interaction between the two ST 0 qubits of the form H int ∝ ð dJ =d 1 μ 1 Þð dJ =d 2 μ 2 Þð σ z -I Þ ⊗ ð σ z -I Þ (Taylor et al. , 2005; Stepanenko and Burkard, 2007; Shulman et al. , 2012), which can be used to implement, for instance, a CZ gate; see Fig. 23.

FIG. 23. Two-qubit operations in ST 0 qubits. (a) Bell-state fidelity during a capacitive entangling operation between two ST 0 qubits. From Shulman et al. , 2012. (b) Concurrence during a twoqubit operation between capacitively coupled, resonantly driven ST 0 qubits. From Nichol et al. , 2017.

<!-- image -->

Charge noise adversely impacts the performance of this capacitive coupling mechanism. Low-frequency charge noise may be refocused by applying spin-echo-like pulses to both qubits using stabilized magnetic gradients (Shulman et al. , 2012; Dial et al. , 2013). If refocusing pulses are applied to both qubits simultaneously, single-qubit dephasing is substantially reduced, while the two-qubit interaction is preserved. Nichol et al. (2017) partially overcame charge-noise limitations this way using the resonantly driven ST 0 qubit, where Δ B z ≫ J . Although the qubit in this regime is sensitive to fluctuating nuclear fields, nuclear spin noise can be refocused much more effectively than charge noise (Bluhm et al. , 2011). One complication with this approach that is not present in the static ST -qubit 0 case is that the form and magnitude of the coupling depends on the frequencies of the two qubits (Calderon-Vargas and Kestner, 2018). By exploiting DNP, Nichol et al. (2017) tuned the qubit energies to resonance and performed a rotary echo to suppress lowfrequency noise. Neighboring ST 0 qubits can also be coupled via the exchange interaction (Levy, 2002; Klinovaja et al. , 2012; Li, Hu, and You, 2012; Wardrop and Doherty, 2014; Cerfontaine, Otten et al. , 2020), and experimental investigations of this approach were recently initiated (Qiao, Kandel, Dyke et al. , 2021).

## 4. Limits of fidelity: Randomized benchmarking

Single-qubit gate fidelities for conventional ST 0 qubits exceed 99.5% in GaAs qubits, as measured via RB using stabilized hyperfine gradients (Cerfontaine, Botzem et al. , 2020). Based on simulations, the gate infidelities were attributed to charge noise. For resonantly driven ST 0 qubits in GaAs, single-qubit gate fidelities are ∼ 99% as measured via RB, likely limited by both hyperfine and charge noise (Nichol et al. , 2017).

Two-qubit operations for GaAs ST 0 qubits have thus far been assessed only through state and process tomography. For conventional ST 0 qubits, the maximum Bell-state fidelity is about 70% (Shulman et al. , 2012), as it is limited by charge noise. For resonantly driven ST 0 qubits, the maximum entangling gate fidelity is about 90% (Nichol et al. , 2017) as measured via process tomography, with a corresponding Bell-state fidelity above 90%. A limitation associated with single- and two-qubit state tomography in ST 0 qubits is that the required tomographic rotations can be difficult to tune precisely (Shulman et al. , 2012; Takahashi, Bartlett, and Doherty, 2013; Nichol et al. , 2017).

## D. Exchange-only qubits

A necessary first step in developing TQDs, identified early as the minimum system size for EO control (Bacon et al. , 2000; DiVincenzo et al. , 2000; Kempe et al. , 2001), was the determination of the voltage bias conditions for populating each dot with a single spin, and the identification of charge regimes enabling initialization, readout, and control (Gaudreau et al. , 2006, 2009; Schröer et al. , 2007; Granger et al. , 2010; Pan et al. , 2012). The familiar two-dimensional charge stability ' honeycomb ' of the DQD becomes a threedimensional cell structure in gate-voltage space. For pairs of TQDs, six-dot arrays require calibration, necessitating even more complex, multidimensional bias tuning procedures to populate each QD with a single charge. Recently automation and machine learning have been brought to bear on this problem (Botzem et al. , 2018; van Diepen et al. , 2018; Mills, Feldman et al. , 2019; Hsiao et al. , 2020; Zwolak et al. , 2020).

## 1. Initialization and readout

For initialization and readout of TQD EO qubits, two of the QDs are used and subjected to the same PSB procedure that is employed for ST 0 qubits (DiVincenzo et al. , 2000; Petta et al. , 2005; Maune et al. , 2012; Jones et al. , 2019). In both cases, the initialization procedure creates a singlet state j S i as described in Sec. V.C.1; for the ST 0 qubit, this is exactly one of the qubit states j 0 i . For a TQD, a third spin is present in a third dot, but this third spin need not be initialized. As detailed in Sec. II.D, the encoded j 1 i state in the TQD case is a superposition of two of the triplet states. Since Pauli blockade is based on spin parity, it distinguishes between the singlet and triplet (but not triplet projections), which suffices for TQD qubit readout via PSB. However, a TQD qubit has a third leaked state, with total angular momentum S ¼ 3 = 2 , which is also composed of a superposition of triplet states of the two dots undergoing Pauli blockade. Therefore, a leaked state has the same PSB readout signature as the encoded j 1 i state.

TQDs present a convenient way to assess exchange for a single pair of QDs, even when full qubit control is not available. By initializing a singlet on one pair of dots (1 and 2) and then pulsing exchange on a second overlapping pair (2 and 3), a ' triple-dot Rabi ' experiment enables coherent exchange oscillations to be measured without the use of magnetic-field gradients. Laird et al. (2010) demonstrated such oscillations for early pulsed EO qubit experiments in GaAs, and Reed et al. (2016) used it for the development of exchange sweet spots in isotopically enhanced Si TQDs. Unlike single-spin or singlet triplet coherent oscillations, exchange oscillations decay due to a combination of charge noise and hyperfine dephasing due to the ability of the encoded qubit to dephase into degenerate leakage states during exchange (Ladd, 2012). Recent measurements of initalization and readout fidelity in a Si = SiGe TQD system achieved a fidelity of 99.75% (Blumoff et al. , 2022).

## 2. Exchange-only single-qubit gates

Early coherent measurements of TQD states employed Landau-Zener transitions (Gaudreau et al. , 2012; PoulinLamarre et al. , 2015), as utilized for ST þ qubits (Sec. V.C).

Such experiments validate energy-level structure using tools familiar from DQD qubits, but they do not exploit true EO operation; indeed, they explicitly rely on mechanisms other than exchange to traverse anticrossings.

The EO modality takes its power from the ability to operate by idling qubits in a degenerate, nonevolving decoherence-free subsystem or subspace, and then lifting selective singlet triplet degeneracies with pulsed pairwise exchange (Bacon et al. , 2000; DiVincenzo et al. , 2000; Andrews et al. , 2019). In contrast to LD and resonant ST 0 qubits that use oscillating fields for quantum control, EO systems rely on the control of energy splittings that are dynamically increased and decreased by changing the trapping potential of electrons.

The TQD EO qubit is defined only by whether the first two spins are in a singlet state j S i or any triplet state j T . Timei domain control of the exchange interaction J 12 ð Þ t lowers the energy of the singlet state relative to any of the triplets, and therefore when pulsed on for a duration T provides a phase such that α j 0 iþ j i β 1 → α j 0 iþ exp ½ -ð i= /uni210F Þ R T 0 J t dt ð Þ /C138 β j 1 i . This interaction may be taken as a rotation of the encoded qubit about ˆ z .

Complete control of the EO qubit is accomplished by pulsing another overlapping pair, say, dots 2 and 3. To assess the geometric effect of exchange between these two dots, one may use angular momentum recoupling coefficients [Racah or Wigner 6 j coefficients (Varshalovich, Moskalev, and Khersonskii, 1988)], i.e., the matrix elements h S 12 ; S 3 ; S 123 j S ; S 1 23 ; S 123 i , where Sjk /C1/C1/C1 refers to the total angular momentum of spins j; k; … . For Sj ¼ 1 2 = and Sjk being either 0 or 1 for singlet or triplet, these coefficients describe a basis change that rotates the ˆ z axis to the vector ˆ n ¼ cos ð 2 π = 3 Þ ˆ z -sin ð 2 π = 3 Þ ˆ x . The encoded qubit under exchange J 23 between spins 2 and 3 therefore rotates about this ˆ n axis, as shown in Fig. 2. At most four pulses are needed to perform an arbitrary Bloch sphere rotation under these geometric constraints (Lowenthal, 1972), generalized Euler angles for such constructions are known (Chatzisavvas et al. , 2009), and a table of solutions for the 24 single-qubit Clifford operations using 17 distinct angles and an average exchange-pulse count of 2.7 was given by Andrews et al. (2019).

Medford, Beil, Taylor, Bartlett et al. (2013) demonstrated complete EO qubit control in a GaAs TQD. Here J 12 ð Þ t and J 23 ð Þ t were controlled, sweeping the integrated phase during the exchange pulses. Singlet triplet readout via PSB was performed, and a self-consistent tomography technique showed that the basic operation was consistent with theory. The decoherence-free subsystem predicating EO control depends on homogeneous magnetic fields which maintain the total angular momentum of the spins S 123 as a conserved quantum number. Inhomogeneous magnetic fields, which are strong in GaAs due to hyperfine interactions (see Sec. VI.B), prevent more than a few operations before leakage of the encoded qubit. A promising route to mitigate hyperfine effects is to implement EO systems in isotopically purified Si. Eng et al. (2015) first demonstrated the longest composite singlequbit Clifford sequence (the four-pulse π rotation about the ˆ y axis) in a Si = SiGe QW structure with 29 Si content reduced to

/g72

FIG. 24. Gradient-free exchange oscillations from an isotopically enhanced Si = SiGe TQD (Eng et al. , 2015). At significantly negative detunings, dots 2 and 3 are exchange coupled and exchange oscillations are geometrically interpreted as a qubit rotation about ˆ n [see Fig. 2(c)]; at less negative detunings, dots 1 and 2 are coupled and geometrically interpreted as rotation about ˆ z . Exchange increases exponentially with detuning. At ε ¼ -7 mV, both exchange couplings are active, as would be required for operation in the RX regime.

<!-- image -->

800 ppm (Fig. 24). Calibrated operation of all composite gates for the 24 Clifford operations was later shown by Andrews et al. (2019) and is further discussed in Sec. V.D.5.

## 3. Resonant-exchange single-qubit gates

EO control in GaAs is more practical when multiple exchange interactions are constantly active, such as in the RX mode of operation; see Medford, Beil, Taylor, Rashba et al. (2013) and Taylor, Srinivasa, and Medford (2013) and Sec. II.D. This qubit results from tuning a TQD to a regime where J 12 ð Þ t and J 23 ð Þ t are simultaneously active; see Fig. 24. RX application is directly analogous to the rotating-frame Hamiltonian for single spins (see the Appendix), enabling the use of familiar rotating-frame rf sequences for decoupling and dynamic compensation. As such, multipulse dynamical decoupling is a viable technique to mitigate hyperfine effects (Malinowski, Martins et al. , 2017).

In Si = SiGe, the valley degree of freedom has enabled a hybrid between RX and EO qubits. As discussed in Sec. II.E, when two of the three electrons occupy a common dot whose valley splitting is within reach of microwave control, the resulting qubit has the same spin encoding as an EO qubit, but the singlet and triplet states of the doubly occupied QDs are perpetually split in energy by the valley splitting, which is analogous to the always-on exchange of the RX qubit. A combination of microwave control, as in the RX qubit, and pulsed exchange, as in the EO qubit, similarly allow biasing to low charge-noise regions and complete qubit control, with demonstrations in isotopically natural Si showing fidelities in the mid-90% range (Koh et al. , 2012; Shi et al. , 2012, 2014; Kim et al. , 2014).

## 4. Two-qubit gates

There are three strategies for EO two-qubit gates. One is to exploit the singlet triplet character of the EO encoding and use capacitive charge coupling in the high-detuning regime, as discussed in Sec. V.A.3. This would be possible for both EO

and RX qubits, would admit a wide variety of two-qubit gating modalities (Pal, Rashba, and Halperin, 2014, 2015), and would be able to exploit long-distance transmission line couplers (Srinivasa, Taylor, and Tahan, 2016). Doherty and Wardrop (2013) proposed a second strategy for the RX qubit modality in which large exchange values are maintained within each TQD qubit and a smaller exchange is activated to couple the two EO qubits. The lowest-order perturbative effect of the small interqubit exchange generates an entangling gate, with leakage effects occurring at higher order in the ratio of the interqubit to intraqubit exchange. Both of these coupling mechanisms are susceptible to charge noise.

The third method is to use true EO sequences between spins in which charge-noise sensitivity during the two-qubit gate is no worse than that between spins during single-qubit operations. Schemes using a combination of single-pair and multipair exchange for the four-spin qubit were shown by Bacon et al. (2000), and pairwise entangling exchange sequences for the three-spin qubit were proposed by DiVincenzo et al. (2000) in the same year, although the latter sequence presents another subtle difficulty. The decoherencefree subsystem of a TQD is insensitive at the single-qubit level to its total spin projection m ¼ m 1 þ m 2 þ m 3 , which may take values /C6 1 2 = in the S 123 ¼ 1 = 2 encoded subspace. This total spin projection is referred to as the gauge spin and may be left unpolarized in single-qubit experiments. However, when two such qubits are combined, the two gauge spins may combine into singlet or triplet states, and the action of intraqubit exchange will behave differently in these two distinct subsystems. The sequential gate of DiVincenzo et al. )) requires the gauge spins to be in a triplet state, which 2000 would most likely be achieved via spin polarization. Such polarization is generally not available in an EO system.

Fong and Wandzura (2011) derived a sequential gaugeindependent CNOT sequence. It has the same entangling action on the two-qubit encoded subsystem regardless of whether gauge spins are in singlet or triplet subspaces. Such gauge invariance also means that they function equivalently on fourspin and three-spin EO qubits. This sequence has a core gauge-invariant structure consisting of 12 π = 2 pulses pairwise connecting five of the six spins (i.e., spin ffiffiffiffiffiffiffiffiffi ffi SWAP gates), some p number of π pulses to swap spins into place to achieve a particular connectivity of spins (Setiawan et al. , 2014), and some number of single-qubit pulses to convert to a desired operation. The CNOT gate implemented in a linear device architecture then summed to 22 pulses (Fong and Wandzura, 2011). Zeuch and Bonesteel (2016) showed that the core entangling part of this gate may be decomposed into three uses of a primitive five-spin sequence that swaps two spins and depends on the encoded state of a single EO qubit. This decomposition and other constructions may lead to other twoqubit gate constructions beyond the Fong-Wandzura sequence family (Zeuch and Bonesteel, 2020). Other constructions based on decoupling concepts have also been proposed (van Meter and Knill, 2019). The Fong-Wandzura sequence and all two-qubit Clifford gates, variations of Fong-Wandzura related to leakage management, and logical SWAPs between encoded qubits were all demonstrated in a six-dot SLEDGE device via tomography and full two-qubit randomized benchmarking by Weinstein et al. (2023).

## 5. Limits of fidelity: Randomized benchmarking

Andrews et al. (2019) performed RB using a TQD in an isotopically enhanced Si = SiGe QW device using overlapping aluminum gates. The RB procedure was modified by randomly choosing whether a sequence of Clifford operations composed to identity or σ x . Recalling that a measurement of a triplet state may correspond either to encoded j 1 i , which responds to exchange, or to a S 123 ¼ 3 2 = leakage state, which does not, the presence of leakage could be deduced on average over many random sequences. An error rate per Clifford operation of 0.35% was observed, with half of the error resulting from leakage. Ha et al. (2022) performed the same experiment using the SLEDGE architecture for a similar Si = SiGe QW and observed an error rate per Clifford gate of 0.12%; this was extended to six dots and two qubits by Weinstein et al. (2023), who found that an average two-qubit Clifford gate had an error rate of 2.9%.

The fidelity in these experiments depended on the details of the quantum control sequence. With substantial idle time added between calibrated exchange pulses, the error was limited by hyperfine dephasing that occurs due to leakage between degenerate S 123 ¼ 1 2 3 = ; = 2 states. If pulses are applied more quickly, the leakage per Clifford operation improves by simply outracing the leakage process, but another error limit is then reached due to the dynamic miscalibration of exchange pulses. The limitations of such an error is a key outcome of RB, as it may be hard to observe in state or process tomography experiments, and it is ' contextual ' (i.e. it depends on the control sequence employed). Improved pulse delivery to the qubit as well as increased isotopic enhancement should further improve EO qubit operation fidelities. The results, however, are promising for exchange-based gates in silicon QDs in isotopically enhanced materials, as the noncontextual, nonhyperfine error from exchange pulses themselves (for instance, due to charge noise; see Sec. VI), which occur an average of 2.7 times per Clifford gate in the single-qubit case

(a)

(b)

n +

poly-Si

SiO

2

28

Si

(d)

100 nm

1

/g80

m

FIG. 25. (a) Nanowire spin-orbit qubit. From Nadj-Perge et al. , 2010. (b) Spin-orbit qubit in a Si MOS DQD. From Jock et al. , 2018. (c) Carbon nanotube qubit. From Cubaynes et al. , 2019. (d) Four-qubit quantum processor based on holes in Ge = SiGe. From Hendrickx et al. , 2021.

<!-- image -->

and 41.1 times per Clifford gate in the two-qubit case, is substantially less than 10 -3 in these experiments.

## E. Alternative material platforms

Spin qubits have been realized predominantly using electrons in GaAs and Si, with recent encouraging results from holes in Ge and Si as well. In this section we review results from several other materials systems (shown in Fig. 25) that have been investigated as suitable platforms for spin-based quantum information processing.

## 1. Carbon nanotubes

Carbon (C) is another group IV element that naturally occurs mostly in the form of an I ¼ 0 isotope (the natural abundance of 12 C is 99%). One can therefore expect long electron spin decoherence times since the deleterious effects of the hyperfine coupling will be weak. The fact that the valence electrons of C are in the atomic p shell further reduces the hyperfine coupling; see Sec. VI.

Carbon nanotubes (CNTs) are a one-dimensional form of carbon with an electronic band structure that can be either metallic or semiconducting (Laird et al. , 2015). The presence of a band gap in semiconducting CNTs allows for the formation of QDs using electrostatic gating (Sapmaz et al. , 2006). Kuemmeth et al. (2008) measured the spin and valley degeneracies of single electrons in a QD formed in a clean CNT, as well as their coupling via a spin-orbit interaction due to the CNT curvature. PSB in the transport through a CNT DQD (Pályi and Burkard, 2010) enables a measurement of the spin relaxation and dephasing times in 13 C-enriched (Churchill et al. , 2009) and natural CNTs (Pei et al. , 2012). Pei et al. (2012) and Laird, Pei, and Kouwenhoven (2013) realized mixed spin-valley qubits in bent single-walled CNT devices, and Cubaynes et al. (2019) observed the coupling of an electron spin localized in a CNT QD to a microwave cavity.

## 2. Spin-orbit qubits

As described in Secs. III.D and V.A.2, electrical control of single spins can be achieved using the intrinsic SOC of a material and electrical driving. The theory for EDSR in a spinorbit field predicts an effective ac magnetic-field strength that is inversely proportional to λ SO , with a Rabi frequency that is proportional to the electronic g factor (Golovach, Borhani, and Loss, 2006). While λ SO ∼ 8 μ m in GaAs, heavier III/V compound semiconductors have a much shorter λ SO. For example λ SO ¼ 100 nm for InSb and 400 nm for InAs. In addition, the bulk electronic g factor is 15 in InAs and 50 in InSb. These factors, combined with a small effective mass, resulted in the development of spin-orbit qubits beyond early demonstrations in GaAs (Nowack et al. , 2007).

Nadj-Perge et al. (2010) implemented EDSR in a bottomgated InAs nanowire DQD. Owing to the strong spin-orbit coupling present in InAs, the g factors for the left and right dots were different, allowing for selective control of each spin. Fast Rabi frequencies were achieved ( fR ¼ 58 MHz), but as in GaAs the Rabi oscillations were strongly damped due to hyperfine coupling. Ramsey decay times T /C3 2 ¼ 8 ns and

spin-echo coherence times ( T 2 ¼ 50 ns) were extracted. Possible reasons for the short T 2 relative to that observed in GaAs include the large, quadrupolar-split nuclear spin I ¼ 9 = 2 of indium and charge noise.

These experiments have been extended to different operating regimes and materials platforms. Schroer et al. (2011) used EDSR to spectroscopically probe the strong anisotropy of the electronic g factor in an InAs nanowire DQD. In a related experiment, Nadj-Perge et al. (2012) performed spectroscopy of InSb spin qubits in the two-electron regime with highly anisotropic g factors. Spectroscopy of the energy levels as a function of magnetic field allowed for a direct measurement of the spin-orbit gap Δ SO , which was largest when the external magnetic field was parallel to the nanowire axis. Subsequently it was shown that the EDSR driving mechanism strongly depends on the DQD energy-level detuning (Stehlik et al. , 2014). While early experiments performed EDSR at high level detuning in an effectively single-QD regime, EDSR when driven around ε ¼ 0 exhibited a standard single photon resonance condition hf ¼ g μ BB as well as multiple harmonics nhf ¼ g μ BB , with n as high as 8. An even-odd dependence in the strength of the PSB leakage current was also observed. These observations were attributed to Landau-Zener physics, where near ε ¼ 0 the DQD is repeatedly driven through avoided crossings in the energylevel diagram (Nadj-Perge et al. , 2010; Schroer et al. , 2011, 2012; Petersson et al. , 2012). Similarly, Jock et al. (2018, 2022) observed large spin-orbit and spin-valley couplings in Si MOS devices, leading to demonstrations of DQD spin-orbit singlet triplet qubits. The stronger spin-orbit interaction of valence band states has also led to further experiments in Si and Ge hole qubits.

## 3. Holes in Si and Ge GeSi =

Hole-spin qubits have shown rapid progress in recent years, particularly in Si and Ge (Hu et al. , 2007; Katsaros et al. , 2010; Li et al. , 2015; Scappucci et al. , 2021). It had previously been known that holes in III-IV semiconductor QDs can have long spin relaxation times (Heiss et al. , 2007; Trif, Simon, and Loss, 2009). Holes have several attractive features: stronger SOI (and hence faster EDSR) as well as weaker nuclear hyperfine coupling, low in-plane effective mass, and the absence of degenerate valleys (Bulaev and Loss, 2005, 2007). However, the degenerate p -like states and SOI lead to strong band mixing. Strain and confinement further complicate the band mixing; the HH versus LH nature of the ground state differs for planar and nanowire devices, and strong structure and tune-up dependence of key parameters is expected.

Si holes can be confined in MOS QDs due to the large valence band offset (Ando, Fowler, and Stern, 1982), and it is possible to even make ambipolar devices capable of confining electrons or holes (Betz et al. , 2014). Early demonstrations of PSB in planar (Li et al. , 2015) and SOI nanowire hole devices (Bohuslavskyi et al. , 2016), followed by a qubit demonstration in the latter platform (Maurand et al. , 2016), have occurred in the few-hole regime. The reported values of T /C3 2 ∼ 2 μ s are consistent with nuclear spin dephasing. On the other hand, T 2 is limited by charge noise, which is found to depend on the magnetic-field orientation, with a maximum T 2 ¼ 88 μ s at the optimized field direction (Piot et al. , 2022).

Gate-reflectometry dispersive readout and coherent control in the few-hole regime in silicon was achieved by Crippa et al. (2019). Recent work showing shell filling (Liles et al. , 2018) and single-hole g -tensor measurements in a planar MOS dot (Liles et al. , 2021) are promising for single-hole coherent operation. In general, the observation of highly voltagesensitive anisotropic g tensors in MOS QDs (Crippa et al. , 2018; Liles et al. , 2021) and Ge nanowires (Brauns et al. , 2016) demonstrates the microscopic complexity of these devices. For few-hole Si nanowire MOSFET devices, it has been predicted that g -tensor resonance can yield Rabi frequencies exceeding 600 MHz (Voisin et al. , 2016). Rabi frequencies of 400 MHz have been achieved with hole-spin qubits in Ge Si core-shell nanowires, with wide tunability of the SOC = strength, Rabi frequency, and electronic g factor (Froning et al. , 2021). Si FinFET devices offer a high degree of tunability (Bosco, Het´ enyi, and Loss, 2021) and Rabi frequencies of 150 MHz at 4 K (Camenzind et al. , 2022).

Holes in Ge have demonstrated promise on several fronts. Higginbotham, Larsen et al. (2014) showed extrinsic noisedominated measurements of T /C3 2 ¼ 180 ns in a Ge Si core-= shell nanowire and Watzinger et al. (2018) demonstrated single-qubit control in the few-hole regime of Ge hut nanowire DQDs on Si. Recently more emphasis has fallen on planar Ge GeSi QWs; the compressive strain in such wells enforces = a HH ground subband, with a HH-LH splitting of 10 -50 meV, and the in-plane effective mass is predicted to be about 0 06 . m 0 (Sch¨ affler, 1997; Terrazos et al. , 2021). The low disorder of this system and its ability to leverage design concepts and infrastructure from GaAs and Si = SiGe devices has enabled rapid experimental progress in the last few years. Theory predictions indicate that suitable choices of the growth direction and QD shape in combination with the Rashba SOC in planar Ge allow for fine-tuning of the qubit properties (Bosco et al. , 2021; Xiong et al. , 2021).

Hendrickx, Franke et al. (2020) demonstrated single- and two-qubit operation in the multihole regime with a singlequbit fidelity of 99.3%. These results were quickly followed by reports of a single-hole qubit (Hendrickx, Lawrie et al. , 2020), a singlet triplet qubit (Jirovec et al. , 2021), and hole manipulation in a 2 × 2 array (Lawrie et al. , 2020; Hendrickx et al. , 2021; van Riggelen et al. , 2021). Dephasing times out to 1 μ s and T 1 &gt; 32 ms have been reported. Theoretical studies have investigated the hyperfine interactions and their effect on hole-spin qubits in GaAs and Si (Fischer et al. , 2008; Testelin et al. , 2009; Philippopoulos, Chesi, and Coish, 2020; Bosco and Loss, 2021). It remains to be seen whether nuclear spins or charge noise provide the dominant dephasing mechanism in experimental settings.

## F. Discussion

Figure 26 plots single- and two-qubit RB data drawn from many (but not all) recent publications on a common axis. Return probability P (that is, the probability of returning to the n -qubit initialized state) is shown. Some researchers have reported the difference y between a measured return and a measured spin flip, which is converted here to return

<!-- image -->

Number of Clifford Gates

Number of Clifford Gates

probability with the unbiased model P ≈ 1 2 = n þð 1 -1 = 2 n Þ y . The x axis counts the number of Clifford gates prior to a single (uncounted) recovery Clifford gate. The fidelities indicated are per Clifford gate, which may or may not include multiple primitive gates, depending on the control modality. As can be seen, there is significant variance in the SPAM fidelity, approximately indicated by the intercept at zero Clifford gates, but recent spin-qubit fidelities indicated by the decay rates of the exponential curves are similar. As randomized benchmarking requires a substantial amount of elements of a qubit apparatus to behave correctly, a key conclusion here is that all previously discussed spin-qubit technologies have passed the critical test of showing the practical reality of performing quantum gates. Fidelities still have room for improvement, but values greater than 99% for basic gates are now firmly established across the semiconductor qubit community and continue to advance.

identify that noise process, how may it be eliminated to improve fidelity? In this section we review the decoherence processes that are most relevant to semiconductor spin qubits.

## VI. DEPHASING AND DECOHERENCE

In Sec. V, we assessed the operation and performance of each major qubit type. For semiconductor qubits, the fidelity is limited by some dephasing or decoherence process. Consider the first exchange oscillations observed in GaAs and Si = SiGe (reproduced in Fig. 20). The first oscillation in each trace corresponds to a π pulse, which may be considered a SWAP gate for an LD qubit, or a Z gate for a ST 0 or EO qubit. Note that the visibility of this fringe is imperfect, and its reduction is a rough measure of the infidelity of the associated gate. The loss of visibility is evident both as a function of time and as exchange is reduced. Why does the fringe visibility decay at the rate that it does? What noise process is responsible for making these qubits imperfect, and if we

The processes leading to decoherence may be classified into a few important categories. In a relaxation process, nondegenerate spin sublevels exchange magnetic energy with the environment (via phonons, photons, etc.). In pure dephasing, random energy-conserving elastic processes dynamically alter the phase of the qubit. For inhomogeneous dephasing, a single qubit s phase remains steady for long periods of time but is ' poorly synchronized with a clock, another qubit, or with itself a significant period of time later. In the context of the Bloch equations, which describe NMR, the timescales corresponding to these effects are T 1 (relaxation), T 2 (decoherence), and T /C3 2 (inhomogeneous dephasing) (Abragam, 1961; Vandersypen and Chuang, 2005; Slichter, 2010). ' Rotatingframe ' analogs of these timescales, which are relevant during coherent driving, include T ;R 2 (the timescale of the decay of Rabi oscillations) and T 1 ρ (the timescale of the decay when spins are driven along a parallel rotating-frame axis).

While the Bloch equations successfully describe the dynamics observed in many ensemble NMR and ESR experiments, the phenomenological exponential decay that they describe is seldom observed for semiconductor spin qubits (for instance, the time decay in Fig. 20 is Gaussian). An improved language for describing dephasing and decoherence is the filter-function formalism (Ithier et al. , 2005), employing the power spectral density of the responsible environmental noise mechanism and the filter on that noise provided by the experiment probing the decoherence mechanism. We review this formalism in Sec. VI.A and then proceed to describe some of the most prominent physical noise sources that cause dephasing and decoherence in spin qubits; see Fig. 27.

FIG. 27. Decoherence and relaxation mechanisms for spin qubits in semiconductor QDs or donors. Energy levels are shown as horizontal dashed lines. Decoherence and relaxation mechanisms (a) -(c) for a LD qubit and (d) -(f) for singlet triplet qubits in DQDs. (a) Spin relaxation through emission (absorption) of energy quanta (such as phonons) to or from the environment. (b) Charge noise, as represented by the squiggly lines (cyan) leading to a fluctuating confinement potential and electronic wave function. When SOI or a magnetic-field gradient (vertical arrows, in green) is present, charge noise leads to spin dephasing. (c) Electron spin dephasing due to the hyperfine coupling to nuclear spins. (d) Singlet triplet spin relaxation. (e) Charge noise affecting detuning ε . (f) Charge noise affecting interdot tunneling t c .

<!-- image -->

Many more thorough reviews of the formalism are available; see Chirolli and Burkard (2008).

## A. Filter-function formalism

## 1. T 1 via noise-correlation function

upward rates proportional to S b ⊥ ð -ω L Þ , which will lead to thermal equilibrium for the detailed balance condition S b ⊥ ð ω L Þ ¼ e /uni210F ω L =k B T S b ⊥ ð -ω L Þ . For details on handling equilibration and the assumptions inherent in finite-temperature BRW theory, see Abragam (1961), Goldman (2001), and Clerk et al. (2010).

A basic model for noise impacting spin qubits is captured by a spin s ' coupling to a noisy magnetic field via the Hamiltonian H noise ¼ -/uni210F b ð Þ t · S , where b is a vector angular frequency describing a stationary, zero-mean noise process. For example, if the noise is a literal fluctuating magnetic field δ B ð Þ t ; b ð Þ ¼ t g μ δ B B ð Þ t = /uni210F and if b is parallel to a large applied magnetic field, b t ð Þ ¼ j b ð Þj t is the fluctuation of the spin s Larmor frequency. '

Starting with this Hamiltonian, if we presume an applied magnetic field along the z axis providing spin Zeeman splitting /uni210F ω 0 and define b /C6 ð Þ ¼ t b x ð Þ /C6 t ib y ð Þ t , then Bloch-Redfield-Wangsness (BRW) theory approximates that T 1 at temperatures T ≪ /uni210F ω L=kB (corresponding to a spin only losing a quantum of energy /uni210F ω L and relaxing to its ground state) is given by

<!-- formula-not-decoded -->

Equation (28) indicates that exponential relaxation at a rate 1 =T 1 is due to the noise power spectral density of transverse fluctuating magnetic fields, S b ⊥ ð ω Þ , at the Larmor frequency ω L , an intuitive result given that noise at ω L is required to overcome the Zeeman splitting EZ ¼ /uni210F ω L between opposite spin states. At finite temperature, T 1 processes also include

In the context of BRW theory, energy-conserving dephasing processes are described as exponential decay with a rate 1 =T 2 :

<!-- formula-not-decoded -->

In Eq. (29) the dephasing rate depends on the spectral density of longitudinal noise at zero frequency S zz b ð 0 Þ . Equation (29) suggests that only true dc noise contributes to dephasing. As discussed in Sec. VI.A.2, however, noise at low frequencies also contributes to dephasing. The filter-function formalism provides a prescription for understanding how such noise contributes to dephasing.

## 2. Filter-function derivation

The concept of a filter function was formalized in a quantum information theory context for qubits by Ithier et al. )), Uhrig (2007), Cywinski 2005 et al. (2008), and Green, Uys, and Biercuk (2012). Notable extensions and higher-order corrections, especially for the slow noise processes typical of spin qubits, were detailed by Barnes et al. (2016). The filter-function derivation utilizes an interaction picture in which S acquires time dependence due to the action of the control of some experiment,

<!-- formula-not-decoded -->

As a result of ˜ H noise ð Þ ¼ t -/uni210F b ð Þ t · ˜ S z ð Þ t , a spin or qubit evolves according to a quantum process during a total time T as ρ ð T Þ ¼ Λ ½ ρ ð 0 Þ/C138 . If Λ is decomposed into a Choi matrix Λ ½ ρ /C138 ¼ P jk λ jk σ ρσ j k for Pauli matrices σ j and including σ 0 as the identity matrix, then the infidelity of this noise process is taken as 1 -λ 00 , which is cast into a decay function exp ½ -χ ð T Þ/C138 . Using cumulant expansion considerations, χ ð T Þ is expanded to second order in the noise field b ð Þ t and filter functions F αβ ð ω T Þ depend on U control (Cywinski et al. , 2008), which is defined to satisfy

<!-- formula-not-decoded -->

where the single-sided noise spectral density corresponds to the noise-correlation function via

<!-- formula-not-decoded -->

In the most commonly encountered situation where ω 0 ≫ j b j , one appeals to a rotating reference frame in which the perpendicular terms b /C6 ð Þ t oscillate at frequency ω 0 , and therefore integrate to noise contributions of the order of j b = ω 0 j 2 , which we neglect. For dominant noise terms, which we discuss later in this section, this secular approximation is valid for applied magnetic fields above a few milliteslas and in some cases remains valid even in fields as low as Earth s ' magnetic field. However, transverse noise terms should not be forgotten, as they do play roles in multipulse experiments in regimes in which pulses occur at rates comparable to ω 0 , for instance, in fast-pulsing and low-magnetic-field cases. It is often assumed that the control pulses described in U control are instantaneous π pulses about an axis orthogonal to the z axis, from which it follows that ˜ S z ð Þ t may be written as ˜ S z ð Þ ¼ t r t ð Þ S z , where r t ð Þ takes only the values /C6 1 , switching between the two for each π pulse. Under these simplifications, only the z component of b and only S zz b are important, and we may therefore drop the component superscripts. Moreover, it may easily be derived that the filter function F ð ω Þ ¼ F zz ð ω Þ is simply

<!-- formula-not-decoded -->

## 3. Dephasing time T /C3 2

With the filter function derived, we are now in a position to calculate dephasing (decoherence) rates T /C3 2 ( T 2 ). T /C3 2 is the rate of decay during a ' free evolution ' experiment, analogous to a free-induction decay experiment in magnetic resonance. For single-spin qubits in which measurements of S z are performed (see Sec. II.A), the relevant experiment is a time ensemble of Ramsey experiments, in which the spin is prepared along an axis orthogonal to a large applied field using a single rf pulse, precession happens for a swept time duration T , and the spin then undergoes a second rf pulse of a known phase, mapping the x y --plane precession onto the ensemble-measured observable h S z i . In either case, r t ð Þ is constant for the duration T and

F ð ω Þ is proportional to sin 2 ð ω T= 2 Þ . For slow noise phenomena [i.e., when Sb ð ω Þ is strongly peaked near ω ¼ 0 , as it is for the hyperfine noise discussed in Sec. VI.B], the shape of the decay curve exp ½ -χ ð Þ/C138 t then predicts decay of oscillations going as exp ½ -ð t=T /C3 2 Þ 2 /C138 , which defines T /C3 2 . More generally, the structure of the low-frequency noise may lead to a power law decay exp ½ -ð t=T /C3 2 Þ α /C138 including α ¼ 1 for white noise. Either way, T /C3 2 is defined via χ ð T /C3 2 Þ ¼ 1 .

The previously defined interpretation of T /C3 2 requires some care, as spin-qubit systems often violate the assumption of ergodicity (i.e., that a series of Ramsey measurements made sequentially in time accurately reflects an ensemble average.) For example, for Sb ð f Þ ∝ 1 =f α and without a low-frequency cutoff, χ ð T Þ diverges. The usual resolution of this divergence is to introduce a low-frequency cutoff determined by the total amount of time used to average an experiment. Formal treatments of such low-frequency cutoffs were discussed by Burkard (2009), Barnes et al. (2016), and Madzik et al. (2020). Eng et al. (2015) and Jock et al. (2018), in particular, presented measured T /C3 2 as a function of averaging time in Si = SiGe and Si MOS dots, and in both the logarithmic dependence on averaging time expected for 1 =f α noise is observed. For a spin qubit in GaAs, the dephasing time was measured to be dependent on the acquisition time (Delbecq et al. , 2016). In short, a measurement of T /C3 2 for a qubit does not by itself indicate an intrinsic property of the qubit, as it depends on experimental averaging details.

The relationship between T /C3 2 and the overall performance of a qubit critically depends on control. Since T /C3 2 results from slow drifts in the qubit frequency, it is well known that it can be compensated for via dynamical decoupling or noise compensation sequences. For GaAs spin qubits, T /C3 2 ∼ 10 ns (see Sec. VI.B), meaning that noise compensation is critical for scaling into useful processors. For silicon, T /C3 2 is generally much longer.

## 4. Decoherence time T 2 and rotating-frame timescales

If compensation is employed, its efficacy will depend on how quickly Sb ð ω Þ reduces with ω relative to the available speed of control. This efficacy is somewhat captured by the parameter T 2 , often taken as the 1 =e point [ χ ð T 2 Þ ¼ 1 ] for decay in the Hahn spin-echo experiment, in which the previously described Ramsey experiment is interrupted halfway by a single π pulse applied orthogonal to the z axis. r t ð Þ has one switch from þ 1 to -1 , and F ð ω Þ ¼ 4 sin 4 ð ω T= 4 Þ . Since F ð ω Þ ∝ ω 4 as ω → 0 , the Hahn echo cancels noise at ω ¼ 0 and passes noise at higher frequency. Once again, T 2 is defined relative to the experiment used to measure it (Cywinski et al. , 2008).

Coherent driving of a spin will also extend pulse sequence times, as Rabi flopping at frequency f Rabi acts as continuous dynamical decoupling. Two types of noise may be relevant. First, there may be noise on the control field itself, for instance, f Rabi ¼ f Rabi ð Þ t , due to charge noise in EDSR and, second, noise from spurious magnetic fields such as Overhauser fields. If the phase of the microwave signal causes rotations about an axis on the Bloch sphere equator and the spin is initialized along ˆ z , the decay time of Rabi oscillation is T ;R 2 , which is different in general from the T /C3 2 of a freely

evolving spin. If the spin is initialized along an axis on the Bloch sphere equator and then driven along that same axis, the associated decay timescale is T 1 ρ . If f Rabi ð Þ t ≫ R Sb ð ω Þ d ω , the decay exponent χ ð T Þ for either experiment is likely to be limited by noise on f Rabi ð Þ t , with a filter function comparable to that for T 1 and relating to f Rabi ð Þ t ' s phase stability. If f Rabi is highly stable and only a transverse magnetic noise b t ð Þ is present, this experiment will correspond to shifting the filter function for noise on b by -f Rabi , which leads to drastically slower decay for the same spectrum of the noise Sb ð ω Þ .

## 5. Filters for multispin qubits

Natural generalizations of the filter-function formalism may be made for qubits composed of several spins (ST , EO, etc.). 0 In this case generalized spin operators and magnetic fields are defined (see Fig. 4), which may be related back to physical spin operators, usually with suitable sums over QDs (Kerckhoff et al. , 2021). A key difference relative to LD qubits, however, arises from the fact that both ST 0 and EO qubits are degenerate when idle. This means that the T /C3 2 and T 2 experiments track dephasing for two degenerate levels (a twospin-singlet state is prepared, allowed to mix with a triplet due to noise, and compared again to a singlet). As observed experimentally by Johnson et al. (2005) and Koppens et al. (2005), rapid hyperfine mixing can occur at low magnetic fields, where any direction of b is important in each dot, leading to more complex filter functions (Kerckhoff et al. , 2021). In these qubits, the analog of a Rabi experiment involves preparing two spins in a coherent superposition of degenerate singlet and triplet states, and then driving oscillations between them with a dc voltage bias that induces exchange. Oscillations occur at frequency J and dephasing occurs due to noise on J t ð Þ , with the decay envelope given by the previously mentioned filter-function equations, replacing Sb ð ω Þ with SJ ð ω Þ . A constant pulse still has a filter function proportional to sin 2 ð ω T=T Þ , and modifications employing π pulses or rotating-frame-type experiments are also possible (Dial et al. , 2013; Eng et al. , 2015), enabling characterization of the charge noise SJ ð ω Þ .

## 6. Non-Markovian and contextual noise

The filter-function formalism presented assumes an independent, stationary noise source. However, dephasing, decoherence, and relaxation timescales have been observed to depend on the same control sequences that are used to measure them, due to such phenomena as rf heating or related pulse-induced frequency shifts (Freer et al. , 2017; Zwerver et al. , 2022), DNP (Sec. V.C), and pulse-driven nuclear spin dynamics (Madzik et al. , 2020; Kerckhoff et al. , 2021). This measurement-induced backaction is not easily accounted for in filter-function theory. In addition, dephasing of qubits is made relative to a clock or a timed control sequence. If that clock or control sequence dephases, it is equivalent to the qubit dephasing from a quantum control standpoint (Ball, Oliver, and Biercuk, 2016). However, measurements of long dephasing and decoherence times under some pulse sequences are a necessary but not sufficient criterion for high-fidelity qubit control. Actual performance is better evaluated through qubit characterization tools such as RB or GST (see Sec. V), but these likewise are challenged by non-Markovian and contextual noise. For example, RB decay is expected to be exponential for Markovian noise, but decay may be nonexponential due to 1 =f noise (Fogarty et al. , 2015), or even nonmonotonic due to leakage (Andrews et al. , 2019). Development of filter-function generalizations or characterization processes robust to non-Markovian effects remains a critical and open area in the development of spin qubits.

## B. Spin dephasing due to hyperfine interactions

Burkard, Loss, and DiVincenzo (1999) and Coish and Loss (2004, 2005) predicted that dephasing due to the hyperfine interaction between an electron spin and the spins of many lattice nuclei in the host crystal would be a significant challenge to spin qubits. Indeed, early experiments in GaAs DQDs extracted T /C3 2 ∼ 10 ns and T 2 ∼ 1 μ s (Petta et al. , 2005). Hyperfine-induced spin dephasing can be mitigated by a variety of methods, including isotopic purification, nuclear polarization, and dynamic decoupling. In this section, we provide an overview of the physics of the hyperfine interaction in QDs and donors, including nuclear dynamics, followed by a summary of nuclear-limited measurements of T /C3 2 and T 2 . Despite significant research in understanding hyperfine dynamics (Chekhovich et al. , 2013), questions remain about the ultimate limits of hyperfine coherence and the fundamental timescales for nuclear spin dynamics.

The dominant effect of nuclear spins is static dephasing mediated by the hyperfine interaction [Eq. (13)], impacting T /C3 2 . In this case, T /C3 2 ; ∞ depends on σ 2 b , the variance of the magnetic field experienced by electron spins due to full randomization of the nuclear magnetization. The variance of the effective angular-frequency magnetic field b ¼ Ak I k for an ensemble of independent nuclei, all with spin I , is summed as

<!-- formula-not-decoded -->

The factor of 3 in the denominator of Eq. (34) is relevant at high fields, where the I þ k S -flip-flop terms average away at a timescale negligibly short relative to dephasing experiments. At zero field, in the case of electron spins, all three nuclear spin directions are of relevance and σ 2 b is 3 times higher. For holes there is a preferred direction for the hyperfine coupling that can result in extended T 2 , depending on the direction of the applied magnetic field (Prechtel et al. , 2016; Bosco and Loss, 2021).

Nuclear fluctuations are slow in both GaAs and Si (of the order of 1 ms) relative to the microsecond timescales of qubit coherence measurements (Ladd et al. , 2005; Reilly et al. , 2010; Madzik et al. , 2020). As such, Sb ð ω Þ is strongly peaked at ω ¼ 0 and the Ramsey decay is Gaussian. For a LD qubit, the envelope decay for an experiment lasting time T , following Eq. (31), goes as exp ð -σ 2 b T = 2 2 Þ , and T /C3 2 ; ∞ ¼ ffiffi ffi 2 p = σ b . For a ST 0 qubit, the assumed independent, identical distributions of static noisy fields from two dots have adding variances, and the ST 0 analog of free-induction decay (in which a singlet is

prepared, allowed to evolve for time T , and then measured) decays as exp ð -σ 2 b T 2 Þ , with T /C3 2 ; ∞ ¼ 1 = σ b .

All Ga and As isotopes have nuclear spin I ¼ 3 = 2 , leading to T /C3 2 ; ∞ ∼ 10 ns (Petta et al. , 2005). In Si, however, only 4.7% of naturally occurring Si isotopes feature nonzero nuclear spin ( 29 Si, I ¼ 1 2 = ), and in Ge only 7.8% of naturally occurring isotopes ( 73 Ge, I ¼ 9 = 2 ) have nonzero spin. The reduced number of spin-carrying nuclei in natural-abundance Si (no enrichment) leads to a significant improvement in T /C3 2 ; ∞ . Further increases are feasible using isotopic enrichment, which was demonstrated as far back as 1958, when a 31 Pdoped sample with under 1200 ppm 29 Si was observed to have longer T /C3 2 than a natural-abundance sample using ensemble ESR (Feher et al. , 1958; Gordon and Bowers, 1958).

In addition to isotopic content, the overall size of the electronic wave function also impacts σ 2 b . With the envelope wave function overlapping many nuclear sites, Eq. (34) leads to

<!-- formula-not-decoded -->

where N is the total number of nuclei for which j ψ ð r k Þj 2 is larger than some threshold and pI is the probability that a given lattice nucleus has spin. Therefore, in the many-nuclei limit, electronic wave functions enveloping a larger number of spin-carrying nuclei have a longer dephasing time due to averaging over more nuclear spins. This occurs because the individual Ak diminish as the electron wave function spreads out over more nuclear spins. However, this scaling cannot extend to small wave functions, since T /C3 2 cannot go to zero. In fact, for small dots with low pI , the value of T /C3 2 ; ∞ varies widely from device to device [the standard deviation of 1 = T ð /C3 2 ; ∞ Þ 2 scales as pI ð 1 -pI Þ =N 3 ]. Whether dephasing occurs quickly or slowly will depend randomly on how often spinful nuclei are located in regions of the electron wave function in which j ψ ð r k Þj 2 is high. In a device such as a 31 P donor, it is plausible to have only one spinful nucleus, the 31 P nucleus itself, which may be coherently controlled and rarely undergoes randomization. Under these circumstances our approximations for the ergodic T /C3 2 ; ∞ do not apply (Madzik et al. , 2020).

To observe a pure dephasing effect on a single qubit due to nuclear spins, the nuclear spins cannot be frozen; they must fluctuate on the timescale of the measurement. Moreover, if nuclear hyperfine effects limit T 2 and we want to compensate for nuclear dephasing, some notion of how quickly nuclei change their polarization state is required. In a dense, homogeneous crystal of nuclear spins, flip-flop rates driven by the dipole-dipole interaction happen frequently, causing Brownian spin diffusion with a noise spectrum Sb ð f Þ scaling as 1 =f 2 (Abragam, 1961). In sparse spin systems and in the presence of field gradients and highly localized dot or donor electrons, the strength of this coupling varies drastically between nuclear spin pairs, as it depends on the inverse cube of the distance between randomly placed nuclei and any changes in their local magnetic field due to field gradients or the hyperfine field of electron spins. Hence, pairs will have varying flip-flop rates and the noise spectrum Sb ð f Þ might be expected to be closer to 1 =f , as anticipated from a broad range of two-level fluctuators. Such a spectrum is observed in silicon systems (Eng et al. , 2015; Madzik et al. , 2020). Solving with morerigor the problem of how coupled nuclear spins impact the coherence of a central electron spin, the ' central spin problem, ' depends on the rich and efficacious use of many-body-physics approximations. Theoretical headway on this problem occurred in the spin-qubit context with the employment of coupled-cluster expansion techniques, which were able to theoretically predict Hahn T 2 values in silicon donor and other systems (Witzel et al. , 2010) but still do not capture all relevant effects, especially the slow dynamics governing T /C3 2 .

Experimental measurements of spin coherence have been performed in a variety of systems. In GaAs QDs, T 2 ∼ 1 μ s for the ST 0 qubit (Petta et al. , 2005). Koppens, Nowack, and Vandersypen (2008) measured T 2 ¼ 500 ns in GaAs using ESR. Various theoretical studies of dephasing of spin qubits in GaAs QDs have taken into account the three nuclear isotopes present in GaAs (Cywinski, Witzel, and Das Sarma, 2009a, 2009b; Neder et al. , 2011). In silicon with &lt; 50 ppm 29 Si content, ensemble ESR measurements of electrons bound to 31 P donors yielded T 2 ≈ 2 s (Tyryshkin et al. , 2012). In isotopically enriched Si, Saeedi et al. (2013) demonstrated an ensemble nuclear spin coherence time of over 39 min. Hahn echo measurements of T 2 in electron spin qubits in isotopically purified silicon at fields greater than 100 mT gave comparable results, showing coherence times of the order of 1 ms in the small donor system (with larger hyperfine gradients) (Muhonen et al. , 2014), of the order of 1.2 ms in the somewhat larger Si MOS dot systems (Veldhorst et al. , 2014), and of the order of 30 μ s to 1 ms in the larger Si = SiGe QD systems (Kawakami et al. , 2014; Sigillito, Loy et al. , 2019; Kerckhoff et al. , 2021). Stano and Loss (2022) compiled a thorough list of coherence times measured in semiconductor spin qubits at the time. Some of these studies involve samples with micromagnets for EDSR, where the T 2 and T /C3 2 values are limited not by nuclear spins but rather by charge noise transduced to magnetic noise due the micromagnet field gradient. We address these effects in Sec. VI.D.

## C. Phonon-mediated spin relaxation

As discussed in Sec. VI.A.1, spin relaxation requires an energy exchange with the environment. For typical QD spin splittings, this often occurs via the emission of acoustic phonons coupled with a spin-mixing perturbation such as spin-orbit, hyperfine, or external magnetic gradient (Hanson et al. , 2007; Zwanenburg et al. , 2013). In polar semiconductors such as GaAs, the dominant phonon interaction is piezoelectric (Khaetskii and Nazarov, 2001). In nonpolar materials like Si, the deformation potential plays a key role (Tahan and Joynt, 2014). For single-phonon-mediated decay, the spin relaxation rate of Eq. (28) can be expressed in Fermi golden rule form as

<!-- formula-not-decoded -->

where ρ ð Δ E Þ is the density of modes (photon or phonon) at the level splitting Δ E , which is equal to the Zeeman splitting

for single-spin relaxation, and the electron-phonon interaction Hp couples the spin states j ˜ ↑ i and j ˜ ↓ i , which are renormalized by the spin-mixing mechanism.

Evaluation of these rates for spin-orbit-mediated decay under the dipole approximation (valid for small energies) leads to characteristic scaling laws 1 =T 1 ∝ B 5 and B 7 , respectively, for piezoelectric-limited and deformationpotential-limited one-phonon relaxation, which is in good agreement with single-spin T 1 measurements in GaAs (Fujisawa et al. , 2002; Hanson et al. , 2003) and Si (Xiao, House, and Jiang, 2010). The same microscopic interactions contribute to singlet triplet decay in single QDs and DQDs. However, since the relevant spin splitting in those cases is usually exchange rather than Zeeman limited and the excitedstate structure is strongly dependent on Coulomb interactions and confinement potential, the scaling and bias dependencies can change drastically (Meunier et al. , 2007; Golovach, Khaetskii, and Loss, 2008; Danon, 2013).

One recent development is the observation of spin relaxation ' hot spots ' when the spin splitting is resonant with another excited level (Stano and Fabian, 2006). Hot spots are especially relevant in Si QDs, where typical valley splittings of the order of 100 μ eV can equal Zeeman energies at teslascale magnetic fields. Like spin-orbit coupling, spin-valley coupling admixes the excited spin states with valley states of opposite spin, which then decay to the ground state via phonon or photon emission (Huang and Hu, 2014b). Valley relaxation is generally dominated by valley-orbit mixing due to interfacial disorder and is typically much faster than pure spin relaxation (Tahan and Joynt, 2014; Penthorn et al. , 2020). This leads to large enhancements in the single-spin relaxation rate when the spin and valley splittings are brought into resonance by tuning the magnetic field; relaxation suppression or ' cold spots ' due to the interplay of disorder are also possible (Yang et al. , 2013; Zhang et al. , 2020; Hosseinkhani and Burkard, 2021). The Zeeman energy of relaxation hot spots can be used to directly measure valley splittings in Si QDs (Yang et al. , 2013; Petit et al. , 2018). Spin-valley effects also play an important role in donor spin relaxation, as discussed by Zwanenburg et al. (2013) and Tahan and Joynt (2014). The weak interactions in these systems allow observations of spin lifetimes of up to 30 s in donor states (Watson et al. , 2017). Electric-field-induced spin-orbit coupling can also significantly enhance the donor spin relaxation rate (Weber et al. , 2018).

In general, spin lifetimes are shortened when spin-charge hybridization is enhanced. The previously described spinvalley hot spots are one such example of this; another is the enhancement of interdot spin relaxation observed in GaAs DQDs at particular detunings where the excited spin state of one dot is resonant with an orbital energy in the other (Srinivasa et al. , 2013). The directional dependence of SOC also leads to an anisotropic dependence of spin T 1 on the in-plane magnetic-field orientation (Scarlino et al. , 2014). Furthermore, external magnetic gradients can provide a synthetic spin-orbit field that contributes to spin relaxation. In the dipole approximation limit, 1 =T 1 ∝ B 5 for deformation potential interactions due to a fixed external gradient. Experimentally, spin relaxation rates at high fields in micromagnet devices tend to increase more slowly (Borjans et al. , 2019; Hollmann et al. , 2020), possibly due to phonon bottleneck effects at these energies.

Hyperfine interactions provide yet another pathway for spin relaxation. Coupling of an electron with local nuclear spins admixes spin states of different orbitals (Erlingsson and Nazarov, 2002), enabling relaxation via phonon or photon emission. The resulting single-spin relaxation rate scales as B 3 and B 5 for piezoelectric and deformation potential phonons, respectively. Hyperfine-induced relaxation in Si QDs is typically expected to be negligible due to the paucity of spinful nuclei (Tahan and Joynt, 2014). Camenzind et al. (2018) observed a long spin T 1 of around 57 /C6 15 s in a GaAs QDat B ¼ 0 6 . -0 7 . T, which increased as B 3 at low fields and was insensitive to field orientation, strongly suggesting hyperfine-limited relaxation. Hyperfine-induced relaxation can also lift Pauli spin blockade at low magnetic fields, as observed experimentally for ð 1 1 ; Þ triplet decay in a GaAs DQD as a function of detuning (Johnson et al. , 2005).

Single-phonon relaxation processes typically dominate at low temperatures, but two-phonon processes can become relevant at high temperatures. This leads to distinct temperature scalings that are observed in spin lifetime measurements above 200 mK in Si MOS (Petit et al. , 2018) and Si = SiGe QDs (Borjans et al. , 2019). At small spin splittings, for instance, low magnetic fields for single spins or modest exchange splittings in singlet triplet states, phonon-assisted decay is suppressed by the reduced density of states and suppression of deformation potential coupling (in Si) at long wavelengths. In such cases the dominant relaxation process may instead be mediated by charge noise, as described later.

Overall, the long spin lifetimes in semiconductors mean that current spin-qubit gate fidelities are rarely limited by T 1 . In contrast, spin relaxation can lead to errors in spin readout when the readout time becomes comparable to T 1 . The rich physics of spin relaxation rewards close study, as it offers many insights into the microscopic physics of spin qubits.

## D. Charge noise

Charge noise can significantly limit the performance of spin qubits. In principle, a spin does not interact with fluctuating electric fields, but for all qubits discussed in this review there is some form of spin-to-charge coupling, allowing charge noise to dephase, decohere, or otherwise reduce the operational fidelity of the spin qubits. Charge noise generally refers to random electric fields that occur at the spin location, which may be caused by fluctuating defect states in the device gate stack, by crystal deformations from phonons (Hu, 2011), by spurious voltage noise transmitted through control gates, or by random charge motion from anywhere else in the device, such as the measurement channel. Semiconductor charge-noise processes typically have a 1 =f noise spectral density (Dutta and Horn, 1981), but white noise (such as thermal Johnson-Nyquist noise) may also be present, usually at levels lower than 1 =f noise. A specific type of thermal noise is the evanescent-wave Johnson noise from nearby metallic structures (Langsjoen et al. , 2012; Tenberg et al. , 2019). Noise sources can to some extent be distinguished by how their spectral character

translates to relaxation (via the filter-function formalism discussed in Sec. VI.A) and their temperature dependence (Beaudoin and Coish, 2015).

Although 1 =f noise varies significantly from device to device, measurements in GaAs dots, Si MOS dots, Si donors near MOS gates, and Si = SiGe dots all see charge-noise-induced energy fluctuations in the range of A μ ¼ 0 1 . -10 μ eV = ffiffiffiffiffi ffi Hz at 1 Hz, meaning that the chemical p potential of the charge carrying the spin has a noise spectral density S μ ð f Þ ¼ A 2 μ ð 1 Hz =f Þ (Petersson et al. , 2010; Freeman, Schoenfield, and Jiang, 2016; Mi, Kohler, and Petta, 2018; Connors et al. , 2022).

Charge noise can affect spin qubits via the large magneticfield gradients that enable EDSR for LD qubits (Sec. III.D). The stray electric fields of charge noise translate directly to a fluctuating magnetic field, and in turn to fluctuations in both the Zeeman splitting and the transverse driving field, and therefore impacting all relaxation parameters T ; T 1 /C3 2 ; T 2 ; T 1 ρ , and T 2 ;R . For instance, Borjans et al. (2019) and Hollmann et al. (2020) showed that the T 1 dependence of a Si = SiGe spin qubit in a large gradient is weakly field dependent at low magnetic fields, strongly suggesting 1 =f or Johnson-noiselimited relaxation at these low energies.

Charge noise as translated to spin by gradients or by spin-orbit effects (Huang and Hu, 2014a) may also be observed in multipulse-sequence noise spectroscopy (Sec. VI.A). Nakajima et al. (2020) examined a GaAs device, Kawakami et al. (2016) investigated an isotopically natural Si = SiGe dot, Yoneda et al. (2018) examined a 800-ppm 29 Si = SiGe dot, and Struck et al. (2020) investigated a 60-ppm 29 Si = SiGe dot. In all of these cases, the large micromagnet-induced gradient resulted in both T /C3 2 and T 2 being limited by 1 =f charge noise. In contrast, noise spectroscopy performed on natural-abundance and 800-ppm Si = SiGe dots with no micromagnet (Kerckhoff et al. , 2021) showed T /C3 2 and T 2 limited by hyperfine effects, although in Si these still had 1 =f character, as discussed in Sec. VI.B. Chan et al. (2018) used noise spectroscopy in a Si MOSquantum device and found a predominantly 1 =f -chargenoise-limited spectrum. In this case charge noise couples to the spin due to intrinsic spin-orbit or spin-valley effects. Petit et al. (2018) observed Johnson-noise-limited spin T 1 at Zeeman energies below the valley splitting in a Si MOS device without a micromagnet. Hole qubits also feature large spin-orbit fields and therefore have T /C3 2 and T 2 times limited by charge noise (Maurand et al. , 2016; Hendrickx, Lawrie et al. , 2020).

EO qubits in Si = SiGe may not suffer from SOI or field gradient effects but are still susceptible to charge noise since they utilize an exchange coupling J that is a sensitive function of the wave function overlap between two spins. Although fluctuations in the confinement potential come from multiple sources, we refer to it as though it arises from fluctuations in gate voltages Vk . The exchange noise may therefore be written as δ J ¼ P k ð ∂ J= Vk ∂ Þ δ Vk , and hence for 1 =f charge noise, it has the following noise spectrum from the noisy voltages:

<!-- formula-not-decoded -->

Thepartial derivatives ∂ J= Vk ∂ quantify the sensitivity to charge noise (Hu and Das Sarma, 2006) and can be estimated through the Fermi-Hubbard ansatz (Culcer and Zimmerman, 2013), Heitler-London or Hund-Mulliken estimates (Culcer, Hu, and Das Sarma, 2009), or FCI calculations (Sec. IV.C). They can also be measured to make a map of sensitivity to charge noise in bias space (Dial et al. , 2013; Martins et al. , 2016; Reed et al. , 2016), enabling an empirical search for operating regions of low charge-noise sensitivity (called sweet spots).

Approximately, the simplest Fermi-Hubbard model ansatz asserts that gates directly above the QDs impact the chemical potential μ j of dot j via a constant factor known as the lever arm α V ; hence, ∂ μ j = Vk ∂ ¼ e α δ V jk . The dependence of tunnel couplings on gate voltages is more complex but is typically assumed to be an exponential function of some linear sum of voltages, in which case ∂ t c = Vk ∂ ∝ t c . Under this model, one finds that in a DQD in the weak exchange limit sensitivity to charge noise is maximized at high detuning and minimized at ε ¼ 0 . The latter condition means that the chemical potential of two dots are held equal, leaving only weaker tunnelcoupling noise (Taylor et al. , 2007; Bertrand et al. , 2015; Martins et al. , 2016; Reed et al. , 2016). We caution, however, that at high exchange and for simultaneous exchange across more than two dots, simple Fermi-Hubbard models are inaccurate at estimating charge-noise sensitivity, as dot electrons merge into a regime in which exchange may be dominated by multidot orbital energies not parametrized by these models (Pan et al. , 2020); see Sec. IV.C.

Recently charge-noise spectral densities in Si ST 0 qubits have confirmed a nearly 1 =f spectrum over nearly 12 decades in frequency in both Si = SiGe (Connors et al. , 2022) and Si MOS (Jock et al. , 2018). Moreover, temperature and fabrication dependencies of the 1 =f noise amplitude point to fluctuations in materials or interfaces in the gate stack, as opposed to noise emanating from the bulk of the semiconductor or instrumentation.

In aggregate, the last 20 years of spin-qubit research have indicated that, while material choices and judicious engineering of charge-noise sensitivity may improve charge-noiseinduced decoherence, the underlying sources of 1 =f charge noise are unlikely to be completely removed from semiconductor devices (unlike hyperfine noise, which may be eliminated with sufficient isotopic enrichment). The ease of control that comes from micromagnet-induced EDSR or RX qubits comes at the cost of persistent sensitivity to everpresent charge noise. When only SOC is at play, as in hole qubits and high-field Si MOS systems, relaxation and decoherence due to charge noise may be lower, and it may be lowest in the nearly gradient-free and low spin-orbit environment of low-field ST 0 or EO qubits, but it is still activated during exchange pulsing and therefore provides some limits to control fidelity. The balance of the speed and convenience of qubit control against sensitivity to charge noise remains a key design space for semiconductor spin qubits across multiple materials and modalities.

## VII. HYBRID SYSTEMS

The short-range nature of exchange coupling (see Sec. IV.A) is most efficiently applied to implement two-qubit

gates between nearest-neighbor spin qubits. However, it has been experimentally shown that fully connected quantum information processors can operate with higher fidelities than systems that provide only nearest-neighbor coupling (Linke et al. , 2017). Beyond the advantage of high connectivity for quantum computing, the coupling of stationary qubits to mobile photonic qubits could form the basis of widespread quantum networks (Kimble, 2008). Some approaches for achieving long-range coupling of spin qubits are outlined in Sec. IV.F. This section is focused on one particularly promising approach, namely, the development of hybrid devices consisting of semiconductor QDs embedded in a microwave cavity, to achieve long-range coupling of spin qubits and high-fidelity readout.

## A. Overview of superconducting circuit QED

Hybrid quantum systems consisting of QDs embedded in microwave cavities are an outgrowth of the field of cQED. The main physical concepts associated with cQED were first explored by atomic physicists in the field of cavity QED (Mabuchi and Doherty, 2002; Miller et al. , 2005; Haroche and Raimond, 2006; Walther et al. , 2006). In cavity QED, a twolevel atom with transition frequency ω a is coupled to an optical cavity with a resonance frequency ω c . The photonic mode and atom interact through the electric-dipole interaction H int ¼ -e E d · , where E is the cavity electric field at the position of the atom and d is the dipole moment associated with the atomic transition.

The Jaynes-Cummings Hamiltonian H JC ¼ /uni210F ω c a a † þ /uni210F ω σ a z = 2 þ /uni210F g a ð σ þ þ a † σ -Þ describes the system dynamics in cases where the rotating-wave approximation is appropriate (Jaynes and Cummings, 1963). Here a † ð a Þ are the photon creation (annihilation) operators, σ z describes the state of the atom, and σ þ ð σ -Þ are atomic raising (lowering) operators. When ω a ¼ ω c , the atom and cavity can exchange an excitation at a rate set by the vacuum Rabi frequency g . In the energy domain, the light-atom coupling manifests itself as the vacuum Rabi splitting between energy eigenstates formed as coherent superpositions that are part atom and part photon. It is directly observable in the cavity transmission in the strong-coupling regime, where g exceeds the cavity decay rate κ and the atomic dephasing rate γ .

In the early 2000s, significant efforts were made to demonstrate cavity-QED physics in solid-state systems. Strong-coupling physics was observed in systems consisting of self-assembled QDs embedded in a distributed Bragg reflector cavity (Yoshie et al. , 2004), self-assembled QDs embedded in a photonic crystal cavity (Reithmaier et al. , 2004), and a superconducting Cooper pair box embedded in a microwave cavity (Wallraff et al. , 2004). These seminal experiments demonstrated that a superconducting artificial atom could be coherently coupled to a microwave frequency photon in the strong-coupling regime with an interaction precisely described by the Jaynes-Cummings Hamiltonian (Blais et al. , 2004, 2007). For a review of cQED physics with superconducting qubits, see Blais, Girvin, and Oliver (2020) and Blais et al. (2021).

The energy scales associated with gate-defined QDs (charge transitions in a DQD and the Zeeman energy of a single spin in a moderate field B ¼ 0 25 . T) are nicely matched with the energy of microwave frequency photons f ¼ 5 -15 GHz. Rapid developments in the cQED architecture led to growing interest in QD cQED and a number of theoretical proposals for physical implementations (Childress, Sorensen, and Lukin, 2004; Burkard and Imamoglu, 2006; Hu, Liu, and Nori, 2012; Jin et al. , 2012; Li, Hu, and You, 2012; Kerman, 2013; Tosi et al. , 2014; Li et al. , 2015; Russ and Burkard, 2015b; Benito et al. , 2016, 2017; Benito, Petta, and Burkard, 2019). Beyond coupling to charge through the electric-dipole interaction, semiconductor QDs allow for cavity coupling to electron spins, long-range spin-spin interactions, and possibly even nuclear spin-state readout. The main modes of interaction are described in Sec. VII.B.

## B. Coherent interactions in quantum-dot circuit QED

In this section we review the theory of charge-photon coupling, spin-photon coupling, and cavity-mediated spinspin interactions in hybrid quantum systems consisting of semiconductor DQDs embedded in microwave cavities. The experimental signatures of coherent interactions in each of these cases are also presented.

## 1. Charge-photon coupling

The physics of a single electron confined in a semiconductor DQD is described by a charge-qubit Hamiltonian H 0 ¼ ð ε = 2 Þ τ z þ t c τ x , where ε is the DQD level detuning, t c is the interdot tunnel coupling, and the matrices τ x and τ z are Pauli matrices (see the Appendix) operating on the charge state of the qubit, i.e., τ z j L i ¼ τ z jð 1 0 ; Þi ¼ jð 1 0 ; Þi and τ z j R i ¼ τ z jð 0 1 ; Þi ¼ -jð 0 1 ; Þi . The cavity electric field E cav ¼ E 0 ð a þ a † Þ couples to the charge dipole moment of an electron confined in a DQD through the interaction term H int ¼ /uni210F gc ð a þ a † Þ τ z . The charge-photon interaction strength is gc ¼ eE d 0 , where d is the interdot spacing and E 0 is the amplitude of the vacuum electric-field fluctuations in the cavity, which characterizes the strength of the charge-photon interaction (Burkard et al. , 2020). Diagonalizing H 0 , transforming H int into the eigenbasis of H 0 , moving into a frame rotating at a probe frequency fp , and making the rotatingwave approximation yield the transverse coupling Hamiltonian H ¼ð 1 2 = Þ Ω τ z þ ˜ gc ð a τ þ þ a † τ -Þþ Δ a a † . Here Ω ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi ε 2 þ 4 t 2 c p is the charge-qubit transition energy, ˜ gc ¼ g t c 0 = Ω is the coupling strength, and Δ ¼ 2 π ð fc -fp Þ is the detuning between the cavity resonance frequency fc ¼ ω c = 2 π and the probe frequency. Note that from a practical perspective Ω is first-order insensitive to charge noise at ε ¼ 0 . The coupling strength ˜ gc is maximal at the interdot charge transition ( ε ¼ 0 ) as well. Input-output theory (Collett and Gardiner, 1984; Benito et al. , 2017; Burkard et al. , 2020) is used to calculate the cavity response. In the steady-state limit \_ a ¼ \_ τ -¼ 0 , the transmission amplitude through the cavity is

<!-- formula-not-decoded -->

FIG. 28. Cavity transmission for a charge qubit coupled to a superconducting microwave resonator. (a) As the double-dot detuning is swept across the tunneling transition, the charge-qubit frequency comes into resonance with the cavity frequency. As a result of the strong coupling between the cavity and charge qubit, the system hybridizes, and two distinct transmission peaks separated by the vacuum Rabi splitting are observed. The eigenenergies of the uncoupled system are shown as dashed lines, and the eigenergies of the coupled system are indicated as solid lines. (b) Cavity transmission at two different values of detuning, with theoretical predictions overlaid. From Mi, Cady, Zajac, Deelman, and Petta, 2017.

<!-- image -->

with the electric susceptibility χ ¼ ˜ gc = ð -Ω þ 2 π fp þ i γ = 2 Þ and the photon loss rates κ 1 2 ; at the cavity ports 1 and 2, where κ ¼ κ 1 þ κ 2 þ κ i and κ i denotes the intrinsic photon loss rate. In terms of the resonator frequency and quality factor Qc , κ = 2 π ¼ fc=Qc .

Strong coupling between the qubit and cavity will occur when ˜ gc 2 &gt; ½ γ 2 c þð κ = 2 Þ 2 /C138 = 2 , where γ c = 2 π is the charge-qubit decoherence rate. When γ is dominated by inhomogeneous dephasing of the qubit, γ = 2 π ¼ 1 =T /C3 2 . In the strong-coupling regime, the cavity resonance splits into two distinct vacuum Rabi peaks separated by 2 ˜ gc , as shown in Fig. 28. It is challenging to reach the strong-coupling regime because in semiconductor systems the qubit decoherence rate γ can be sizable, for instance, several tens of megahertz for GaAs. This can be overcome by increasing ˜ gc or by suppressing γ . Both strategies have successfully been implemented to reach the strong-coupling regime: an enhancement of ˜ gc ∝ E 0 ∝ ffiffiffi Z p to a GaAs DQD was achieved by increasing the impedance Z ¼ ffiffiffiffiffiffiffiffi ffi L=C p of the resonator (Stockklauser et al. , 2017), while a reduction of γ was possible using a Si DQD (Mi, Cady, Zajac, Deelman, and Petta, 2017).

## 2. Spin-photon coupling

For spin qubits, one is ultimately interested in coupling the spin to the cavity mode. While for optical cavities SOC in the valence band of III-V semiconductors can enable spin-photon coupling (Imamoglu et al. , 1999), the coupling to microwave photons requires mechanisms acting entirely in the conduction (valence) band for electrons (holes). Spin-charge hybridization using SOC or magnetic-field gradients allows for a sizable coupling between the electron spin and the cavity electric field (Burkard et al. , 2020). In particular, the coupling of a flopping-mode spin qubit via spin-charge hybridization using a magnetic-field gradient Δ B x ¼ B x 1 -B x 2 in a Si DQD can be described by the additional term ð Δ B x = 2 Þ σ τ x z in the single-electron Hamiltonian H 0 (Benito et al. , 2017). The direction of this gradient field is perpendicular to the homogeneous magnetic field B z ¼ ð B z 1 þ B z 2 Þ = 2 described by the Zeeman term ð B z = 2 Þ σ z . In the case of holes in the valence band of Si or Ge, the intrinsic SOC could be used instead of a gradient field (Kloeffel et al. , 2013; Mutter and Burkard, 2021).

Transforming H int into the eigenbasis of H 0 , one obtains a coupling of the form H int ¼ gc ð a þ a † Þ P 3 n;m ¼ 0 dnm j n ih m j , where the sum represents the electric-dipole operator in the spin-charge-hybridized DQD eigenbasis j n i . For microwave transmission through the cavity, one again finds Eq. (38) with the susceptibility χ ¼ P 3 n ¼ 0 P 3 -n j ¼ 1 dn;n þ j χ n;n þ j and χ ij follows from the stationary limit of the quantum master equation. The relevant low-energy eigenstates of H 0 are j 0 i ≈ -j ; ↓ i and j 1 i ≈ cos ð Φ = 2 Þj -; ↑ i þ sin ð Φ = 2 Þjþ ; ↓ i , with the spinorbit mixing angle Φ ¼ arctan ½ Δ B x = ð 2 t c -B z Þ/C138 (in the symmetric case where ε ¼ p 0 ) and hybridized orbital states j/C6i ¼ ½jð 1 0 ; Þi /C6 jð 0 1 ; Þi/C138 = ffiffi ffi 2 . The dipole transition matrix element for the predominantly spinlike transition between these two states is d 01 ≈ -sin ð Φ = 2 Þ , whereas chargelike transitions to the next higher state are less important but can lead to an asymmetry in the vacuum Rabi peaks. The resulting spin-photon coupling in this simplest two-level description and within the rotating-wave approximation can be described with a Jaynes-Cummings model

<!-- formula-not-decoded -->

where Ω s is the spin-qubit transition frequency and the spinphoton coupling gs ≈ gc j d 01 j ≈ gc j sin ð Φ = 2 Þj . A strength of this architecture is the electrical tunability of the spin-charge admixture via the interdot tunnel coupling t c .

Strong spin-photon coupling will occur when gs &gt; γ s ; κ , where γ s is the spin decoherence rate. This condition is not identical to the strong-coupling condition for charge, and in fact the spin-photon system can be in the strong-coupling regime, while the charge-photon system is not. A key signature of strong-coupling, vacuum Rabi splitting has been observed in the microwave transmission through a superconducting Nb cavity with an embedded Si DQD (Mi et al. , 2018). A similar experiment with NbTiN superconducting circuitry has also reached the strong-coupling regime (Samkharadze et al. , 2018); see Fig. 29. The coupling of RX qubits to an electromagnetic cavity (Russ, Ginzel, and Burkard, 2016) has been realized using a TQD in GaAs

FIG. 29. Cavity transmission for a single-spin qubit coupled to a superconducting microwave resonator. As the magnetic field is swept, the spin qubit comes into resonance with the cavity at about 6.03 GHz, and the qubit-cavity coupling splits the cavity resonance into two hybrid spin-photon modes. The characteristic vacuum Rabi splitting indicates the strong-coupling regime. From Samkharadze et al. , 2018.

<!-- image -->

coupled to a NbTiN superconducting cavity (Landig et al. , 2018).

## 3. Cavity-mediated spin-spin interactions

The coherent coupling [Eq. (39)] of individual submicronscale spin qubits to a single cavity mode extending over 100 μ m or more lends itself to the pairwise coupling of spin qubits over distances much longer than their typical nearestneighbor separation. The exchange of virtual cavity photons in the dispersive limit and within the rotating-wave approximation gives rise to an effective coupling between spin qubits of the form

<!-- formula-not-decoded -->

with the coupling J ¼ gs 2 = 2 Δ and detuning Δ ¼ Ω s -ω c (Benito, Petta, and Burkard, 2019; Warren, Barnes, and Economou, 2019). The transverse ( XY ) coupling [Eq. (40)] is known to generate the universal ffiffiffiffiffiffiffiffiffiffi ffi i SWAP (Imamoglu p et al. , 1999) and i SWAPgates, as shown by Schuch and Siewert (2003) and in the Appendix.

Cavity photon loss and qubit decoherence imply opposing requirements for the degree of spin-charge mixing, with the optimum defined by the ratio κ = γ c (Benito et al. , 2019). Fast and high-fidelity two-qubit gates in the presence of realistic charge noise have been supported by numerical calculations (Warren, Barnes, and Economou, 2019; Young, Jacobson, and Petta, 2022).

One challenge with experiments demonstrating cavitymediated coupling between single spins involves bringing multiple spin qubits into resonance with each other and a cavity. For example, differences in qubit-micromagnet positioning of around 10 nm, which are within typical fabrication tolerances, can easily detune two single-spin qubits from each other, even at the same value of the external magnetic field. To surmount this challenge, the micromagnets on different qubits can be fabricated at an angle with respect to each other (Astner et al. , 2017; Borjans et al. , 2020; Harvey-Collard et al. , 2022). By adjusting the angle and magnitude of the external magnetic field, the two spins can be brought into resonance with each other and the cavity. When two qubits, instead of just one, are tuned into resonance with the same cavity, an enhancement of

FIG. 30. Resonant cavity-mediated spin-spin interactions. Measured cavity transmission A=A 0 as a function of the in-plane field angle ϕ , showing an avoided crossing between both qubits and the resonator at the expected angle. From Borjans et al. , 2020.

<!-- image -->

the spin-photon coupling rate gs is observed (Fig. 30), as reported for single electrons in Si DQDs coupled to both Nb (Borjans et al. , 2020) and NbTiN superconducting resonators (Harvey-Collard et al. , 2022). Moreover, when both spins are detuned from the cavity but in resonance with each other, an avoided crossing between spins due to the cavity-mediated dispersive coupling can be observed (HarveyCollard et al. , 2022). Microwave-photon-mediated coupling between charge qubits has also been demonstrated (van Woerkom et al. , 2018).

## C. Applications for readout

Cavity-coupled QDs can be readily probed by measuring the transmission through, or reflection from, the microwave cavity. Measurements are generally performed in the dispersive regime, where the detuning between the QD transition frequency and cavity photon is greater than the cavity linewidth: j ω a -ω c j ≫ κ , where ω a is the charge-qubit or spinqubit frequency. In this dispersive (i.e., off-resonant) regime, the Jaynes-Cummings Hamiltonian simplifies to the form H ≈ /uni210F ð ω c þ χ d σ z Þð a a † þ 1 = 2 Þ þ /uni210F ω σ a z = 2 with the dispersive shift χ d ¼ g = 2 ð ω a -ω c Þ . The first term in the Hamiltonian gives insight into the nature of the measurement. The barecavity photon energy (energy in the absence of a qubit) /uni210F ω c is shifted by an amount χ d that depends on the state of the qubit.

Detection of charge states using microwave photons has been demonstrated in GaAs, InAs, carbon nanotube, and Si = SiGe DQDs (Frey et al. , 2012; Petersson et al. , 2012; Viennot et al. , 2016; Mi, Cady, Zajac, Deelman, and Petta, 2017). The dispersive shift can be detected by probing the cavity transmission amplitude j A j or phase shift δϕ . Measurements of δϕ as a function of the DQD gate voltages can be used to map out DQD charge stability diagrams and quantitatively extract the interdot tunnel coupling t c and the charge-qubit coupling rate gc . High-speed and high sensitivity real-time charge detection have benefited from the adoption of nearly quantum-limited superconducting parametric amplifiers. Stehlik et al. (2015) demonstrated ' video mode ' acquisition of DQD charge stability diagrams in 20 ms. It is also possible to use the cavity response at a single

<!-- image -->

B

dot-to-lead charge transition for charge state readout with a large signal-to-noise ratio of &gt; 450 and an integration time of around 1 μ s (Borjans, Mi, and Petta, 2021).

Cavity readout of spin states can be achieved using at least two different approaches. In the first approach, the Pauli exclusion principle is used to distinguish spin-singlet and spin-triplet states in a two-electron DQD. Pauli blocking is evident in the magnetic-field dependence of the cavity response. With B ¼ 0 , the spin-singlet state is the ground state and tunneling from S ð 1 1 ; Þ to S ð 2 0 ; Þ leads to a large cavity response. In contrast, when g μ BB &gt; tc , the polarized spin-triplet state T þ (or T -, depending on the sign of the g factor) becomes the ground state near the charge transition. Owing to Pauli blockade, charge tunneling from T þð 1 1 ; Þ to S ð 2 0 ; Þ is forbidden, and there is no cavity response. The magnetic-field dependence of the interdot charge transition signal can thereby be used to determine the charge parity of a DQD interdot charge transition (Schroer et al. , 2012). Control of two-electron spin states at a large DQD detuning, followed by cavity readout at zero detuning, has been used to distinguish singlet and triplet spin states in an InAs DQD (Petersson et al. , 2012), and later in a cavity-coupled Si = SiGe DQD (Zheng et al. , 2019). Using an ancilla dot capacitively coupled to a singlet triplet qubit has led to singlet triplet spinstate readout with a fidelity of 99.2% (Borjans, Mi, and Petta, 2021).

A second approach for spin-state readout in the oneelectron regime of a DQD utilizes spin-photon coupling and the dispersive interaction. For a spin interacting with a cavity photon, the dispersive shift is χ d σ z . Dispersive readout of a single-electron spin state using cQED was first demonstrated using a cavity-coupled Si = SiGe DQD (Mi et al. , 2018). Figure 31 shows the cavity phase response as a function of magnetic field and microwave probe frequency. The spin-photon detuning dependence is evident in the data, with the phase shift changing sign as the spin is taken through resonance with the cavity. The magnitude of the dispersive shift also decreases with detuning, as expected from the 1 = Δ dependence in the dispersive form of the Jaynes-Cummings Hamiltonian. Rabi oscillations of a single spin have been measured by probing the cavity with a microwave tone after the spin was driven with a microwave field. The signal-tonoise ratio of the dispersive readout of a single spin in a DQD coupled to a microwave cavity was analyzed and optimized by D Anjou and Burkard (2019). '

## D. New avenues of research in cQED

Cavity-coupled QDs have enormous potential for applications in quantum information science. In the span of a few years, coherent charge-photon and spin-photon interactions have been demonstrated, as well as evidence for long-range cavity-mediated spin-spin interactions. Future research is likely to extend these results to spin-spin coupling in the dispersive limit, a time-domain demonstration of a cavitymediated two-qubit gate, and extensions to larger quantum networks. There is also the potential for cQED to probe the nuclear spin degree of freedom in dot-donor systems (Mielke, Petta, and Burkard, 2021).

Within the field of quantum information processing, hybrid systems employing cQED approaches may enable new forms of quantum information processors that could benefit from the

FIG. 32. Cavity-mediated coupling between a triple-dot resonant-exchange qubit and a transmon superconducting qubit. Here a superconducting cavity is driven near its resonance frequency of about 5.6 GHz. The y axis indicates the drive frequency of the resonant-exchange qubit, and the x axis corresponds to changes in the electrochemical potential of the middle dot, which changes the overall energy of the spin qubit. The color scale indicates the transmission through the cavity. The small dashed (black) lines indicate the eigenenergies of the system in the absence of coupling, and the large dashed (red) lines indicate the eigenenergies of the system, including the coupling. From Landig et al. , 2019.

<!-- image -->

advantages of different platforms. For example, recent work illustrates the feasibility of coupling spin qubits to superconducting qubits through microwave resonators; see Fig. 32 (Landig et al. , 2019; Scarlino et al. , 2019). A challenge for future hybrid systems such as these will be to ensure strong enough coupling rates to simultaneously capitalize on the benefits of the separate platforms while not introducing excess decoherence.

Hybrid quantum systems have had a major impact on the field of mesoscopic physics as well. For example, voltage biased DQDs have been shown to emit microwave photons (Liu et al. , 2014; Stockklauser et al. , 2015; Bruhat et al. , 2016), and even enable the creation of a maser (Liu et al. , 2015). Given the sensitivity with which charge state physics can be probed, signatures of electron-phonon coupling in suspended nanowire DQDs have been observed (Hartke et al. , 2018). Kondo physics has been explored (Desjardins et al. , 2017), and there is the potential to probe Majorana modes as well (Dartiailh et al. , 2017). In Si = SiGe DQDs, cQED has proven to be useful as a quantitative probe of valley splitting and intervalley coupling (Burkard and Petta, 2016; Mi, Peterfalvi et al. , 2017; Borjans et al. , 2021). Looking ahead, microwave spectroscopy may provide insight into a broader class of materials systems (Gramse et al. , 2017; Shim et al. , 2019; Lee et al. , 2021) and qubit functionalities (de Lange et al. , 2015; Larsen et al. , 2015; van Woerkom et al. , 2017).

## VIII. OUTLOOK

Semiconductor spin qubits are uniquely positioned to benefit from the technologies that are available for classical semiconductor-based information processing devices. The most important observation is that no single roadblock stands in the way of reaching the types of yields now driving the industry of Si CMOS for classical information processing. Fidelities for both single-qubit and multiqubit gates appear to be limited by processes with clear routes for reduction, such as judicious bias regimes for reducing sensitivity to charge noise and isotopic enhancement for reducing magnetic noise (Mills, Guinn, Gullans et al. , 2022; Noiri et al. , 2022; Xue et al. , 2022; Weinstein et al. , 2023). Readout visibilities and speeds have also improved substantially in recent years (Borjans, Mi, and Petta, 2021; Blumoff et al. , 2022; Madzik et al. , 2022; Mills, Guinn, Gullans et al. , 2022).

A clear advantage of semiconductor spin qubits is therefore the potential for their massive scaling and miniaturization. Owing to their small size, semiconductor spin qubits have the distinction of having the most stringent demands on fabrication in comparison to superconducting qubits, trapped ion qubits, and photonic qubits. As a result, the route to large arrays of spin qubits has been slower, as numerous problems have to be overcome to more reliably yield qubit arrays (Zajac et al. , 2016; Ha et al. , 2022). In the past decade the progress not only for the most heroic of devices but also for yielding routine device arrays from many groups in many countries and using many different control strategies has indicated a positive trend. The number of demonstrations of coherent operation published worldwide has grown accordingly.

It seems too early to say which type of spin qubit (LD, ST 0 , EO, etc.), spin-qubit carrier (electron, hole, or nucleus), and material (Si, Ge, etc.), or which combination thereof, will end up being optimal for realizing a functioning large-scale quantum processor. While LD qubits offer an efficient use of the available resources and high robustness against charge noise, ST 0 and EO qubits allow for baseband electrical control, in the case of EO qubits without the need for SOC or on-chip micromagnets. While electrons in Si offer extremely high coherence, holes in Si or Ge allow for spinorbit engineering of electrically controlled qubit operations. The extremely long coherence time of nuclear spins can be contrasted with the readily available fast exchange coupling between electronic spins.

Even if fault-tolerant quantum computers are many years away, qubits serve as our most sensitive solid-state electrometers and magnetometers and, in the case of semiconductor spin qubits, they serve this role within the workhorse materials underpinning the most pervasive information processing technology in modern society. Advances in the understanding of semiconductor device physics are at least one guaranteed outcome in the pursuit of future scalable quantum computers based on semiconductor spin qubits.

Until fault-tolerant quantum computation can be realized, computational demonstrations using noisy intermediate-scale quantum (referred to as NISQ) devices provide valuable proofs of principle (Preskill, 2018). Examples that can be tackled with noisy devices are simulations of condensed matter and quantum chemistry as well as optimization problems. Analog quantum simulations of condensed matter systems with three to four spin qubits have been demonstrated (Hensgens et al. , 2017; Dehollain et al. , 2020; van Diepen et al. , 2021). On the level of two qubits, the variational quantum eigensolver method (Xue et al. , 2022) and small quantum algorithms (Watson et al. , 2018; Noiri et al. , 2022) have been implemented.

Ultimately, the utility of spin qubits, and in fact all other quantum computing platforms, lies in their ability to reach quantum fault tolerance since practical applications depend on a scale demanding lower-error operation than would be possible without quantum error correction. It is not clear when we can declare any qubit sufficient for fault tolerance, since many estimates of fault-tolerant thresholds, for example, for the widespread surface code (Fowler et al. , 2012), make geometric layout and error-correlation assumptions that are not consistent with semiconductor spin qubits as presently operated. Nearer-term approaches to error corrected logical qubits may nonetheless be pursued, even in strictly onedimensional qubit arrays using the methodologies and geometries presently under study (Jones et al. , 2018), from which we may anticipate significant discovery, not only about the pathways to scalable quantum computers but also to serendipitous advances in the understanding of the physics of solidstate devices.

## ACKNOWLEDGMENTS

We thank John B. Carpenter of HRL Laboratories for assistance with generating the figures in this review. J. R. P. thanks members of the Petta Group for constructive feedback on the review. G. B. and J. R. P. acknowledge the support of Army Research Office Grant No. W911NF-15-1-0149.

G. B. also acknowledges funding from the European Union under Grant Agreement No. 951852 (Quantum Technology Flagship/QLSI) and the German Research Foundation (Deutsche Forschungsgemeinschaft, DFG) under Project No. 450396347. J. M. N. acknowledges support of Army Research Office Grants No. W911NF-16-1-0260 and No. W911NF-19-1-0167 and Office of Naval Research Grant No. N00014-20-1-2424. The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies, either expressed or implied, of the Army Research Office or the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for Governmental purposes notwithstanding any copyright notation herein.

## APPENDIX: SPIN ROTATION GATES

In this review we have discussed multiple encodings of spin qubits in terms of spin operators S , which are typically represented as Pauli operators. However, we reserve the notation of Pauli operators represented as Pauli matrices

<!-- formula-not-decoded -->

for the two encoded states of qubits j 0 i and j 1 i . Canonical quantum computing is accomplished by application of unitary qubit rotations generated by Pauli operators, i.e., single-qubit operations

<!-- formula-not-decoded -->

and two-qubit operations such as the controlled-Z (CZ) operation

<!-- formula-not-decoded -->

Two-qubit gates for semiconductor spin qubits are drawn from three families. First are the controlled rotations such as controlled NOT (CNOT) and controlled Z, which result from the product of single-qubit rotations and the two-qubit unitary exp ð -i θσ σ z 1 z 2 Þ , with θ ¼ π = 4 for a fully entangling gate. Second are fractional SWAP gates, which result from the group of two-qubit unitaries exp ð -i θ σ 1 · σ 2 Þ , with a full SWAP at θ ¼ π = 4 and a fully entangling ffiffiffiffiffiffiffiffiffi ffi SWAP at p θ ¼ π = 8 . Finally, the product of commuting controlled-Z, SWAP, and single-qubit R z rotations is the i SWAP, which, unlike SWAP, is entangling. Since ½ σ σ z 1 z 2 ; σ 1 · σ 2 /C138 ¼ 0 , it may readily be seen that

<!-- formula-not-decoded -->

Hence, the XY coupling σ σ x 1 x 2 þ σ σ y 1 y 2 , of importance to cavitycoupled dots as discussed in Sec. VII.B.3, generates a fractional i SWAP, with a full i SWAP at θ ¼ π = 4 .

A π pulse with unitary R n ð π Þ applies -i n · σ , so if n is along x y , , or z , this is a Pauli operator with an overall phase. A Pauli operator or π pulse applies /C6 1 to the two eigenstates of a qubit in the associated basis. In the two-spin singlet triplet basis, a π pulse of the exchange operator U ¼ exp ð -i π S 1 · S 2 Þ applies a spin swap, which from the antisymmetry of the spin pair for the singlet and symmetry for the triplet states applies a -1 phase to the singlet and thus is analogous to the Pauli operations for singlet triplet and exchange-only systems. Exchange occurring for an arbitrary duration generates a superposition of swapping and not swapping spins such that

<!-- formula-not-decoded -->

Single qubits driven by rf signals (single-spin qubits controlled by ESR or EDSR, RX qubits, etc.) use a rotating frame for single-qubit control. This means that the laboratoryframe Hamiltonian for qubit j is

<!-- formula-not-decoded -->

where ω is the driving frequency, ϕ is the drive phase relative to a local oscillator, and Ω is proportional to the amplitude of the driving rf or microwave field. In a rotating-frame analysis, we presume the driving frequency ω is close to the qubit resonant frequency ω j , and both of these are always much larger than the Rabi frequency Ω . Under these assumptions we transform Hj and other operators to a frame rotating at the drive frequency ω and local oscillator phase for each qubit,

<!-- formula-not-decoded -->

The terms oscillating at frequency 2 ω with amplitude Ω when Ω ≪ ω are generally negligible; the lowest-order effect of these terms is the Bloch-Siegert shift (Abragam, 1961), which amounts to a slight detuning of the resonance of the order of ð Ω = ω Þ 2 . As such, these terms are generally dropped, resulting in the nominally time-independent rotating-frame Hamiltonian

<!-- formula-not-decoded -->

for which U ¼ exp ð -iHjt= ˜ /uni210F Þ enables any single-qubit rotation R n ð θ Þ via control of the amplitude Ω , phase ϕ , and detuning Δ ω of the drive frequency. Since the phase ϕ is relative to a local oscillator, a z -axis rotation is generally accomplished by a frame shift in which the phase of the local oscillator is updated without touching the qubit.

## REFERENCES

Abragam, A., 1961, The Principles of Nuclear Magnetism , International Series of Monographs on Physics (Clarendon Press, Oxford).

Abragam, A., and M. Goldman, 1978, Rep. Prog. Phys. 41 , 395. Abram, R., and M. Jaros, 1989, Band Structure Engineering in Semiconductor Microstructures (Plenum Press, New York).

Anderson, C. R.,

M. F.

Gyure, S. Quinn, A. Pan, R. S. Ross, and

A. A. Kiselev, 2022, AIP Adv.

12

,

065123.

Ando, T., A. B. Fowler, and F. Stern, 1982, Rev. Mod. Phys. 54 , 437.

- Andrews, R. W., et al. , 2019, Nat. Nanotechnol. 14 , 747.
- Angus, S. J., A. J. Ferguson, A. S. Dzurak, and R. G. Clark, 2007, Nano Lett. 7 , 2051.
- Ansaloni, F., A. Chatterjee, H. Bohuslavskyi, B. Bertrand, L. Hutin, M. Vinet, and F. Kuemmeth, 2020, Nat. Commun. 11 , 6399.
- Asaad, S., et al. , 2020, Nature (London) 579 , 205.
- Assali, L. V., H. M. Petrilli, R. B. Capaz, B. Koiller, X. Hu, and S. D. Sarma, 2011, Phys. Rev. B 83 , 165301.
- Astner, T., S. Nevlacsil, N. Peterschofsky, A. Angerer, S. Rotter, S. Putz, J. Schmiedmayer, and J. Majer, 2017, Phys. Rev. Lett. 118 , 140502.
- Awschalom, D. D., R. Hanson, J. Wrachtrup, and B. B. Zhou, 2018, Nat. Photonics 12 , 516.
- Baart, T. A., T. Fujita, C. Reichl, W. Wegscheider, and L. M. K. Vandersypen, 2017, Nat. Nanotechnol. 12 , 26.
- Baart, T. A., S. Shafiei, F. Takafumi, C. Reichl, W. Wegscheider, and L. M. K. Vandersypen, 2016, Nat. Nanotechnol. 11 , 330.
- Bacon, D., and S. T. Flammia, 2009, Phys. Rev. Lett. 103 , 120504.
- Bacon, D., J. Kempe, D. A. Lidar, and K. B. Whaley, 2000, Phys. Rev. Lett. 85 , 1758.
- Bakker, M. A., S. Mehl, T. Hiltunen, A. Harju, and D. P. DiVincenzo, 2015, Phys. Rev. B 91 , 155425.
- Ball, H., W. D. Oliver, and M. J. Biercuk, 2016, npj Quantum Inf. 2 , 16033.
- Ban, Y., X. Chen, S. Kohler, and G. Platero, 2019, Adv. Quantum Technol. 2 , 1900048.
- Ban, Y., X. Chen, and G. Platero, 2018, Nanotechnology 29 , 505201. Barnes, E., J. P. Kestner, N. T. T. Nguyen, and S. Das Sarma, 2011, Phys. Rev. B 84 , 235309.
- Barnes, E., M. S. Rudner, F. Martins, F. K. Malinowski, C. M. Marcus, and F. Kuemmeth, 2016, Phys. Rev. B 93 , 121407.
- Barthel, C., M. Kjærgaard, J. Medford, M. Stopa, C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2010, Phys. Rev. B 81 , 161308.
- Barthel, C., J. Medford, H. Bluhm, A. Yacoby, C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2012, Phys. Rev. B 85 , 035306.
- Barthel, C., D. J. Reilly, C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2009, Phys. Rev. Lett. 103 , 160503.
- Baruffa, F., P. Stano, and J. Fabian, 2010a, Phys. Rev. B 82 , 045311.
- Baruffa, F., P. Stano, and J. Fabian, 2010b, Phys. Rev. Lett. 104 , 126401.
- Bastard, G., 1991, Wave Mechanics Applied to Semiconductor Heterostructures (Wiley, New York).
- Beaudoin, F., and W. A. Coish, 2015, Phys. Rev. B 91 , 165432.
- Benito, M., X. Croot, C. Adelsberger, S. Putz, X. Mi, J. R. Petta, and G. Burkard, 2019, Phys. Rev. B 100 , 125430.
- Benito, M., X. Mi, J. M. Taylor, J. R. Petta, and G. Burkard, 2017, Phys. Rev. B 96 , 235434.
- Benito, M., J. R. Petta, and G. Burkard, 2019, Phys. Rev. B 100 , 081412.
- Benito, M., M. J. A. Schuetz, J. I. Cirac, G. Platero, and G. Giedke, 2016, Phys. Rev. B 94 , 115404.
- Bertrand, B., H. Flentje, S. Takada, M. Yamamoto, S. Tarucha, A. Ludwig, A. D. Wieck, C. B¨ auerle, and T. Meunier, 2015, Phys. Rev. Lett. 115 , 096801.
- Bertrand, B., S. Hermelin, S. Takada, M. Yamamoto, S. Tarucha, A. Ludwig, A. D. Wieck, C. B¨ auerle, and T. Meunier, 2016, Nat. Nanotechnol. 11 , 672.
- Betz, A. C., M. F. Gonzalez-Zalba, G. Podd, and A. J. Ferguson, 2014, Appl. Phys. Lett. 105 , 153113.
- Blais, A., J. Gambetta, A. Wallraff, D. I. Schuster, S. M. Girvin, M. H. Devoret, and R. J. Schoelkopf, 2007, Phys. Rev. A 75 , 032329.
- Blais, A., S. M. Girvin, and W. D. Oliver, 2020, Nat. Phys. 16 , 247.

| Blais, A., A. L. Grimsmo, S. M. Girvin, and A. Wallraff, 2021, Rev. Mod. Phys. 93 , 025005. A., R.-S. Huang, A. Wallraff, S. M. Girvin, and R. J.                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blais, Schoelkopf, 2004, Phys. Rev. A 69 , 062320.                                                                                                                                                                                                                                                                                                                          |
| Bluhm, H., S. Foletti, D. Mahalu, V. Umansky, and A. Yacoby, 2010, Phys. Rev. Lett. 105 , 216803. Bluhm, H., S. Foletti, I. Neder, M. S. Rudner, D. Mahalu,                                                                                                                                                                                                                 |
| V. Umansky, and A. Yacoby, 2011, Nat. Phys. 7 , 109.                                                                                                                                                                                                                                                                                                                        |
| Blumoff, J. Z., et al. , 2022, PRX Quantum 3 , 010352.                                                                                                                                                                                                                                                                                                                      |
| Bohuslavskyi, H., et al. , 2016, Appl. Phys. Lett. 109 , 193101. Borjans, F., X. G. Croot, X. Mi, M. J. Gullans, and J. R. Petta, 2020, Nature (London) 577 , 195.                                                                                                                                                                                                          |
| Borjans, F., X. Mi, and J. Petta, 2021, Phys. Rev. Appl. 15 , 044052. Borjans, F., D. M. Zajac, T. M. Hazard, and J. R. Petta, 2019, Phys. Rev. Appl. 11 , 044063.                                                                                                                                                                                                          |
| and J. Petta, 2021, PRX Quantum 2 , 020309.                                                                                                                                                                                                                                                                                                                                 |
| Borjans, F., X. Zhang, X. Mi, G. Cheng, N. Yao, C. Jackson, L. Edge, Borselli, M. G., et al. , 2011a, Appl. Phys. Lett. 99 , 063109.                                                                                                                                                                                                                                        |
| Borselli, M. G., et al. , 2011b, Appl. Phys. Lett. 98 , 123118. B 104 , 115425. Bosco, S., B. Het´ enyi, and D. Loss, 2021, PRX Quantum 2                                                                                                                                                                                                                                   |
| Bosco, S., M. Benito, C. Adelsberger, and D. Loss, 2021, Phys. Rev. , 010348.                                                                                                                                                                                                                                                                                               |
| Bosco, S., and D. Loss, 2021, Phys. Rev. Lett. 127 , 190501.                                                                                                                                                                                                                                                                                                                |
| Bose, S., 2003, Phys. Rev. Lett. 91 , 207901. 48 , 13.                                                                                                                                                                                                                                                                                                                      |
| Bose, S., 2007, Contemp. Phys. C. G. L., S. P. Harvey, S. Fallahi, G. C. Gardner, Manfra, U. Vool, S. D. Bartlett, and A. Yacoby, 2022,                                                                                                                                                                                                                                     |
| Bøttcher,                                                                                                                                                                                                                                                                                                                                                                   |
| Commun. 13 , 4773.                                                                                                                                                                                                                                                                                                                                                          |
| M. J. Nat.                                                                                                                                                                                                                                                                                                                                                                  |
| Botzem, T., et al. , 2018, Phys. Rev. Appl. 10 , 054026. Boykin, T. B., G. Klimeck, M. Friesen, S. N. Coppersmith, P. von                                                                                                                                                                                                                                                   |
| Allmen, F. Oyafuso, and S. Lee, 2004, Phys. Rev. B 70 , 165325. Braakman, F. R., P. Barthelemy, C. Reichl, W. Wegscheider, and L. M. K. Vandersypen, 2013, Nat. Nanotechnol. 8 , 432. Bracker, A. S., et al. , 2005, Phys. Rev. Lett. 94 , 047402. Brataas, A., and E. I. Rashba, 2011, Phys. Rev. B 84 , 045301. Brauns, M., J. Ridderbos, A. Li, E. P. A. M. Bakkers, and |
| F. A. Zwanenburg, 2016, Phys. Rev. B 93 , 121408. Broome, M. A., T. F. Watson, D. Keith, S. K. Gorman, M. G. House, J. G. Keizer, S. J. Hile, W. Baker, and M. Y. Simmons, 2017, Phys.                                                                                                                                                                                      |
| Rev. Lett. 119 , 046802.                                                                                                                                                                                                                                                                                                                                                    |
| Broome, M. A., et al. , 2018, Nat. Commun. 9 , 980. Bruhat, L. E., J. J. Viennot, M. C. Dartiailh, M. M. Desjardins, T.                                                                                                                                                                                                                                                     |
| Kontos, and A. Cottet, 2016, Phys. Rev. X 6 , 021014. Brunner, R., Y.-S. Shin, T. Obata, M. Pioro-Ladri` ere, T. Kubo, K.                                                                                                                                                                                                                                                   |
| Yoshida, T. Taniyama, Y. Tokura, and S. Tarucha, 2011, Phys. Rev.                                                                                                                                                                                                                                                                                                           |
| Lett. 107 , 146801.                                                                                                                                                                                                                                                                                                                                                         |
| Bulaev, D. V., and D. Loss, 2005, Phys. Rev. Lett. 95 , 076805.                                                                                                                                                                                                                                                                                                             |
| 98 , 097202.                                                                                                                                                                                                                                                                                                                                                                |
| Bulaev, D. V., and D. Loss, 2007, Phys. Rev. Lett. Burkard, G., 2009, Phys. Rev. B 79 , 125317.                                                                                                                                                                                                                                                                             |
| Burkard, G., M. J. Gullans, X. Mi, and J. R. Petta, 2020, Nat. Rev. Phys. 2 , 129. Burkard, G., and A. Imamoglu, 2006, Phys. Rev. B 74 ,                                                                                                                                                                                                                                    |
| 041307(R). Burkard, G., D. Loss, and D. P. DiVincenzo, 1999, Phys. Rev. B , 2070. Burkard, G., D. Loss, D. P. DiVincenzo, and J. A.                                                                                                                                                                                                                                         |
| 59 Phys. Rev. B 60 , 11404.                                                                                                                                                                                                                                                                                                                                                 |
| Burkard, G., and J. R. Petta, 2016, Phys. Rev. B 94 , 195305.                                                                                                                                                                                                                                                                                                               |
| et al. , 2013, Nat. Nanotechnol. 8 , 261.                                                                                                                                                                                                                                                                                                                                   |
| Busl, M.,                                                                                                                                                                                                                                                                                                                                                                   |
| Bussmann, E., M. Rudolph, G. S. Subramania, S. Misra, S. M. Carr,                                                                                                                                                                                                                                                                                                           |
| Smolin, 1999,                                                                                                                                                                                                                                                                                                                                                               |

- Calderón, M. J., B. Koiller, and S. Das Sarma, 2006, Phys. Rev. B 74 , 045310.
- Calderon-Vargas, F. A., and J. P. Kestner, 2018, Phys. Rev. B 97 , 125311.
- Camenzind, L. C., S. Geyer, A. Fuhrer, R. J. Warburton, D. M. Zumb¨ uhl, and A. V. Kuhlmann, 2022, Nat. Electron. 5 , 178.
- Camenzind, L. C., L. Yu, P. Stano, J. D. Zimmerman, A. C. Gossard,
- D. Loss, and D. M. Zumbuhl, 2018, Nat. Commun. 9 , 3454. Campos Venuti, L., C. Degli Esposti Boschi, and M. Roncaglia, 2006, Phys. Rev. Lett. 96 , 247206.
- Cayao, J., M. Benito, and G. Burkard, 2020, Phys. Rev. B 101 , 195438.
- Cerfontaine, P., T. Botzem, J. Ritzmann, S. S. Humpohl, A. Ludwig, D. Schuh, D. Bougeard, A. D. Wieck, and H. Bluhm, 2020, Nat. Commun. 11 , 4144.
- Cerfontaine, P., R. Otten, M. A. Wolfe, P. Bethke, and H. Bluhm, 2020, Phys. Rev. B 101 , 155311.
- Chan, K. W., et al. , 2018, Phys. Rev. Appl. 10 , 044017.
- Chan, K. W., et al. , 2021, Nano Lett. 21 , 1517.
- Chancellor, N., and S. Haas, 2012, New J. Phys. 14 , 095025.
- Chatzisavvas, K. C., G. Chadzitaskos, C. Daskaloyannis, and S. G. Schirmer, 2009, Phys. Rev. A 80 , 052329.
- Chekhovich, E. A., M. N. Makhonin, A. I. Tartakovskii, A. Yacoby, H. Bluhm, K. C. Nowack, and L. M. K. Vandersypen, 2013, Nat. Mater. 12 , 494.
- Chen, E. H., et al. , 2021, Phys. Rev. Appl. 15 , 044033.
- Childress, L., and R. Hanson, 2013, MRS Bull. 38 , 134.
- Childress, L., A. S. Sorensen, and M. D. Lukin, 2004, Phys. Rev. A 69 , 042302.
- Childs, A. M., and W. van Dam, 2010, Rev. Mod. Phys. 82 , 1. Chirolli, L., and G. Burkard, 2008, Adv. Phys. 57 , 225.
- Churchill, H. O. H., F. Kuemmeth, J. W. Harlow, A. J. Bestwick, E. I. Rashba, K. Flensberg, C. H. Stwertka, T. Taychatanapat, S. K. Watson, and C. M. Marcus, 2009, Phys. Rev. Lett. 102 , 166802.
- Chutia, S., M. Friesen, and R. Joynt, 2006, Phys. Rev. B 73 , 241304.
- Ciorga, M., A. S. Sachrajda, P. Hawrylak, C. Gould, P. Zawadzki, S. Jullian, Y. Feng, and Z. Wasilewski, 2000, Phys. Rev. B 61 , R16315.
- Ciriano-Tejel, V. N., et al. , 2021, PRX Quantum 2 , 010353.
- Clerk, A. A., M. H. Devoret, S. M. Girvin, F. Marquardt, and R. J. Schoelkopf, 2010, Rev. Mod. Phys. 82 , 1155.
- Coish, W. A., and D. Loss, 2004, Phys. Rev. B 70 , 195340.
- Coish, W. A., and D. Loss, 2005, Phys. Rev. B 72 , 125337.
- Cole, J. H., A. D. Greentree, L. Hollenberg, and S. D. Sarma, 2008, Phys. Rev. B 77 , 235418.
- Colless, J. I., A. C. Mahoney, J. M. Hornibrook, A. C. Doherty, H. Lu, A. C. Gossard, and D. J. Reilly, 2013, Phys. Rev. Lett. 110 , 046805.
- Collett, M. J., and C. W. Gardiner, 1984, Phys. Rev. A 30 , 1386.
- Connors, E. J., J. Nelson, L. F. Edge, and J. M. Nichol, 2022, Nat. Commun. 13 , 940.
- Connors, E. J., J. J. Nelson, and J. M. Nichol, 2020, Phys. Rev. Appl. 13 , 024019.
- Cottet, A., and T. Kontos, 2010, Phys. Rev. Lett. 105 ,
- Crippa, A., et al. , 2018, Phys. Rev. Lett. 120 ,
- 160502. 137702.
- Crippa, A., et al. , 2019, Nat. Commun. 10 , 2776.
- Croot, X. G., X. Mi, S. Putz, M. Benito, F. Borjans, G. Burkard, and J. R. Petta, 2020, Phys. Rev. Res. 2 , 012006(R).
- Cubaynes, T., et al. , 2019, npj Quantum Inf. 5 , 47.
- Culcer, D., X. Hu, and S. Das Sarma, 2009, Appl. Phys. Lett. 95 , 073102.
- Culcer, D., X. Hu, and S. D. Sarma, 2010, Phys. Rev. B 82 , 205315.

| Culcer, D., and N. M. Zimmerman, 2013, Appl. Phys. Lett. 102 ,                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 232108. Cywinski, L., R. M. Lutchyn, C. P. Nave, and S. Das Sarma, 2008, Phys. Rev. B 77 , 174509. Cywinski, L., W. M. Witzel, and S. Das Sarma, 2009a, Phys. Rev. Lett. 102 , 057601. Cywinski, L., W. M. Witzel, and S. Das Sarma, 2009b, Phys. Rev. B 79 , 245314. D Anjou, B., and G. Burkard, 2019, Phys. Rev. B ' 100 , 245427. |

- Ercan, H. E., S. Coppersmith, and M. Friesen, 2021, Phys. Rev. B 104 , 235302.
- Erlingsson, S. I., and Y. V. Nazarov, 2002, Phys. Rev. B 66 , 155327.
- Farooq, U., A. Bayat, S. Mancini, and S. Bose, 2015, Phys. Rev. B 91 , 134303.
- Fedele, F., A. Chatterjee, S. Fallahi, G. C. Gardner, M. J. Manfra, and F. Kuemmeth, 2021, PRX Quantum 2 , 040306.

Feher, G., 1959, Phys. Rev.

114

,

1219.

- Feher, G., J. P. Gordon, E. Buehler, E. A. Gere, and C. D. Thurmond, 1958, Phys. Rev. 109 , 221.
- Feng, M., L. H. Zaw, and T. S. Koh, 2021, npj Quantum Inf. 7 , 112. Ferdous, R., et al. , 2018, npj Quantum Inf. 4 , 26.
- Feynman, R. P., 1982, Int. J. Theor. Phys. 21 , 467.
- Field, M., C. G. Smith, M. Pepper, D. A. Ritchie, J. E. F. Frost, G. A. C. Jones, and D. G. Hasko, 1993, Phys. Rev. Lett. 70 , 1311. Fischer, J., W. A. Coish, D. V. Bulaev, and D. Loss, 2008, Phys. Rev. B 78 , 155329.
- Flindt, C., A. S. Sørensen, and K. Flensberg, 2006, Phys. Rev. Lett. 97 , 240501.
- Fogarty, M. A., M. Veldhorst, R. Harper, C. H. Yang, S. D. Bartlett, S. T. Flammia, and A. S. Dzurak, 2015, Phys. Rev. A 92 , 022326. Fogarty, M. A., et al. , 2018, Nat. Commun. 9 , 4370.
- Foletti, S., H. Bluhm, D. Mahalu, V. Umansky, and A. Yacoby, 2009, Nat. Phys. 5 , 903.
- Fong, B. H., and S. M. Wandzura, 2011, Quantum Inf. Comput. 11 , 1003.
- Fowler, A. G., M. Mariantoni, J. M. Martinis, and A. N. Cleland, 2012, Phys. Rev. A 86 , 032324.
- Franke, D. P., M. P. Pfl¨ger, P.-A. Mortemousque, K. M. Itoh, and u M. S. Brandt, 2016, Phys. Rev. B 93 , 161303.
- Freeman, B. M., J. S. Schoenfield, and H. Jiang, 2016, Appl. Phys. Lett. 108 , 253108.
- Freer, S., et al. , 2017, Quantum Sci. Technol. 2 , 015009.
- Frey, T., P. J. Leek, M. Beck, A. Blais, T. Ihn, K. Ensslin, and A. Wallraff, 2012, Phys. Rev. Lett. 108 , 046807.
- Fricke, L., S. J. Hile, L. Kranz, Y. Chung, Y. He, P. Pakkiam, M. G. House, J. G. Keizer, and M. Y. Simmons, 2021, Nat. Commun. 12 , 1.
- Friesen, M., A. Biswas, X. Hu, and D. Lidar, 2007, Phys. Rev. Lett. 98 , 230503.
- Friesen, M., and S. N. Coppersmith, 2010, Phys. Rev. B 81 , 115324. Friesen, M., J. Ghosh, M. A. Eriksson, and S. N. Coppersmith, 2017, Nat. Commun. 8 , 15923.
- Froning, F. N. M., L. C. Camenzind, O. A. H. van der Molen, A. Li, E. P. A. M. Bakkers, D. M. Zumbuhl, and F. R. Braakman, 2021, Nat. Nanotechnol. 16 , 308.
- Fuechsle, M., J. A. Miwa, S. Mahapatra, H. Ryu, S. Lee, O. Warschkow, L. C. L. Hollenberg, G. Klimeck, and M. Y. Simmons, 2012, Nat. Nanotechnol. 7 , 242.
- Fujisawa, T., D. G. Austing, Y. Tokura, Y. Hirayama, and S. Tarucha, 2002, Nature (London) 419 , 278.
- Fujita, T., T. A. Baart, C. Reichl, W. Wegscheider, and L. M. K. Vandersypen, 2017, npj Quantum Inf. 3 , 22.
- Gamble, J. K., N. T. Jacobson, E. Nielsen, A. D. Baczewski, J. E. Moussa, I. Montaño, and R. P. Muller, 2015, Phys. Rev. B 91 , 235318.
- Gamble, J. K., et al. , 2016, Appl. Phys. Lett. 109 , 253101.
- Gaudreau, L., G. Granger, A. Kam, G. C. Aers, S. A. Studenikin, P. Zawadzki, M. Pioro-Ladriere, Z. R. Wasilewski, and A. S. Sachrajda, 2012, Nat. Phys. 8 , 54.
- Gaudreau, L., A. Kam, G. Granger, S. A. Studenikin, P. Zawadzki, and A. S. Sachrajda, 2009, Appl. Phys. Lett. 95 , 193101.
- Gaudreau, L., S. A. Studenikin, A. S. Sachrajda, P. Zawadzki, A. Kam, J. Lapointe, M. Korkusinski, and P. Hawrylak, 2006, Phys. Rev. Lett. 97 , 036807.
- Geyer, S., L. C. Camenzind, L. Czornomaz, V. Deshpande, A. Fuhrer, R. J. Warburton, D. M. Zumb¨ uhl, and A. V. Kuhlmann, 2021, Appl. Phys. Lett. 118 , 104004.
- Ginzel, F., A. R. Mills, J. R. Petta, and G. Burkard, 2020, Phys. Rev. B 102 , 195418.
- Goldman, M., 2001, J. Magn. Reson. 149 , 160.
- Golovach, V. N., M. Borhani, and D. Loss, 2006, Phys. Rev. B 74 , 165319.
- Golovach, V. N., A. Khaetskii, and D. Loss, 2008, Phys. Rev. B 77 , 045328.
- Golub, L. E., and E. L. Ivchenko, 2004, Phys. Rev. B 69 , 115333. Gonzalez-Zalba, M. F., S. Barraud, A. J. Ferguson, and A. C. Betz, 2015, Nat. Commun. 6 , 6084.
- Gordon, J. P., and K. D. Bowers, 1958, Phys. Rev. Lett. 1 , 368.
- Gorman, S. K., M. A. Broome, J. G. Keizer, T. F. Watson, S. J. Hile, W. J. Baker, and M. Y. Simmons, 2016, New J. Phys. 18 , 053041.
- Gramse, G., A. Kölker, T. Lim, T. J. Z. Stock, H. Solanki, S. R. Schofield, E. Brinciotti, G. Aeppli, F. Kienberger, and N. J. Curson, 2017, Sci. Adv. 3 , e1602586.
- Granger, G., L. Gaudreau, A. Kam, M. Pioro-Ladri` ere, S. A. Studenikin, Z. R. Wasilewski, P. Zawadzki, and A. S. Sachrajda, 2010, Phys. Rev. B 82 , 075304.
- Green, T., H. Uys, and M. J. Biercuk, 2012, Phys. Rev. Lett. 109 , 020501.
- Greentree, A. D., J. H. Cole, A. R. Hamilton, and L. C. L. Hollenberg, 2004, Phys. Rev. B 70 , 235317.
- Gullans, M., J. J. Krich, J. M. Taylor, H. Bluhm, B. Halperin, C. M. Marcus, M. Stopa, A. Yacoby, and M. D. Lukin, 2010, Phys. Rev. Lett. 104 , 226807.
- Gullans, M., J. J. Krich, J. M. Taylor, B. Halperin, and M. D. Lukin, 2013, Phys. Rev. B 88 , 035309.
- Gullans, M. J., and J. R. Petta, 2020, Phys. Rev. B 102 , 155404.
- Gustafsson, M., T. Aref, A. Kockum, M. Ekstrom, G. Johansson, and P. Delsing, 2014, Science 346 , 207.
- Gyure, M. F., A. A. Kiselev, R. S. Ross, R. Rahman, and C. G. Van de Walle, 2021, MRS Bull. 46 , 634.
- Ha, W., et al. , 2022, Nano Lett. 22 , 1443.
- Hada, Y., and M. Eto, 2003, Phys. Rev. B 68 , 155322.
- Hanson, R., and G. Burkard, 2007, Phys. Rev. Lett. 98 , 050502.
- Hanson, R., L. P. Kouwenhoven, J. R. Petta, S. Tarucha, and L. M. K. Vandersypen, 2007, Rev. Mod. Phys. 79 , 1217.
- Hanson, R., B. Witkamp, L. M. K. Vandersypen, L. H. W. van Beveren, J. M. Elzerman, and L. P. Kouwenhoven, 2003, Phys. Rev. Lett. 91 , 196802.
- Haroche, S., and J. M. Raimond, 2006, Exploring the Quantum: Atoms, Cavities, and Photons (Oxford University Press, Oxford). Hartke, T. R., Y.-Y. Liu, M. J. Gullans, and J. R. Petta, 2018, Phys. Rev. Lett. 120 , 097701.
- Harvey-Collard, P., J. Dijkema, G. Zheng, A. Sammak, G. Scappucci, and L. M. Vandersypen, 2022, Phys. Rev. X 12 , 021026.
- Harvey-Collard, P., et al. , 2017a, Nat. Commun. 8 , 1029.
- Harvey-Collard, P., et al. , 2017b, in Proceedings of the 63rd IEEE International Electron Devices Meeting (IEDM), San Francisco, 2017 (IEEE, New York), pp. 36.5.1 -36.5.4, 10.1109/IEDM.2017 .8268507.
- Harvey-Collard, P., et al. , 2018, Phys. Rev. X 8 , 021046.
- Harvey-Collard, P., et al. , 2019, Phys. Rev. Lett. 122 , 217702.
- Hatano, T., S. Amaha, T. Kubo, Y. Tokura, Y. Nishi, Y. Hirayama, and S. Tarucha, 2008, Phys. Rev. B 77 , 241301.

- Hayashi, T., T. Fujisawa, H. D. Cheong, Y. H. Jeong, and Y. Hirayama, 2003, Phys. Rev. Lett. 91 , 226804.
- He, Y., S. K. Gorman, D. Keith, L. Kranz, J. G. Keizer, and M. Y. Simmons, 2019, Nature (London) 571 , 371.
- Heiss, D., S. Schaeck, H. Huebl, M. Bichler, G. Abstreiter, J. J. Finley, D. V. Bulaev, and D. Loss, 2007, Phys. Rev. B 76 , 241306. Helsen, J., I. Roth, E. Onorati, A. H. Werner, and J. Eisert, 2022, PRX Quantum 3 , 020357.
- Hendrickx, N. W., D. P. Franke, A. Sammak, G. Scappucci, and M. Veldhorst, 2020, Nature (London) 577 , 487.
- Hendrickx, N. W., W. I. L. Lawrie, L. Petit, A. Sammak, G. Scappucci, and M. Veldhorst, 2020, Nat. Commun. 11 , 3478.
- Hendrickx, N. W., W. I. L. Lawrie, M. Russ, F. van Riggelen, S. L. de Snoo, R. N. Schouten, A. Sammak, G. Scappucci, and M. Veldhorst, 2021, Nature (London) 591 , 580.
- Hensgens, T., T. Fujita, L. Janssen, X. Li, C. J. Van Diepen, C. Reichl, W. Wegscheider, S. Das Sarma, and L. M. K. Vandersypen, 2017, Nature (London) 548 , 70.
- Higginbotham, A. P., F. Kuemmeth, M. P. Hanson, A. C. Gossard, and C. M. Marcus, 2014, Phys. Rev. Lett. 112 , 026801.
- Higginbotham, A. P., T. W. Larsen, J. Yao, H. Yan, C. M. Lieber,

C. M. Marcus, and F. Kuemmeth, 2014, Nano Lett.

14

,

3582.

Hile, S. J., et al.

,

2018, Sci. Adv.

4

,

eaaq1459.

- Hill, C. D., E. Peretz, S. J. Hile, M. G. House, M. Fuechsle, S. Rogge, M. Y. Simmons, and L. C. L. Hollenberg, 2015, Sci. Adv. 1 , e1500707.
- Hofmann, A., V. Maisi, T. Kr¨ ahenmann, C. Reichl, W. Wegscheider, K. Ensslin, and T. Ihn, 2017, Phys. Rev. Lett. 119 , 176807.

Hollmann, A., et al.

,

2020, Phys. Rev. Appl.

13

,

034068.

Hosseinkhani, A., and G. Burkard, 2021, Phys. Rev. B

104

,

085309.

- Hsiao, T. K., C. J. van Diepen, U. Mukhopadhyay, C. Reichl, W. Wegscheider, and L. M. K. Vandersypen, 2020, Phys. Rev. Appl. 13 , 054018.
- Hu, X., 2011, Phys. Rev. B 83 , 165322.
- Hu, X., and S. Das Sarma, 2000, Phys. Rev. A 61 , 062301.
- Hu, X., and S. Das Sarma, 2001, Phys. Rev. A 64 , 042312.
- Hu, X., and S. Das Sarma, 2006, Phys. Rev. Lett. 96 , 100501.
- Hu, X., Y.-x. Liu, and F. Nori, 2012, Phys. Rev. B 86 , 035314.
- Hu, Y., H. O. H. Churchill, D. J. Reilly, J. Xiang, C. M. Lieber, and C. M. Marcus, 2007, Nat. Nanotechnol. 2 , 622.
- Huang, P., and X. Hu, 2014a, Phys. Rev. B 89 , 195302.
- Huang, P., and X. Hu, 2014b, Phys. Rev. B 90 , 235315.
- Huang, W., et al. , 2019, Nature (London) 569 , 532.
- Imamoglu, A., D. D. Awschalom, G. Burkard, D. P. DiVincenzo, D. Loss, M. Sherwin, and A. Small, 1999, Phys. Rev. Lett. 83 , 4204. Ithier, G., et al. , 2005, Phys. Rev. B 72 , 134519.
- Jadot, B., P. Mortemousque, E. Chanrion, V. Thiney, A. Ludwig, A. Wieck, M. Urdampilleta, C. Bauerle, and T. Meunier, 2021, Nat. Nanotechnol. 16 , 570.
- Jaynes, E., and F. Cummings, 1963, Proc. IEEE 51 , 89.
- Jin, P.-Q., M. Marthaler, A. Shnirman, and G. Schön, 2012, Phys. Rev. Lett. 108 , 190506.
- Jirovec, D., et al. , 2021, Nat. Mater. 20 , 1106.
- Jock, R. M., N. T. Jacobson, M. Rudolph, D. R. Ward, M. S. Carroll, and D. R. Luhman, 2022, Nat. Commun. 13 , 641.
- Jock, R. M., et al. , 2018, Nat. Commun. 9 , 1768.
- Joecker, B., A. D. Baczewski, J. K. Gamble, J. J. Pla, A. Saraiva, and A. Morello, 2021, New J. Phys. 23 , 073007.
- Johnson, A. C., J. R. Petta, and C. M. Marcus, 2005, Phys. Rev. B 72 , 165308.
- Johnson, A. C., J. R. Petta, J. M. Taylor, A. Yacoby, M. D. Lukin, C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2005, Nature (London) 435 , 925.
- Jones, A., et al. , 2019, Phys. Rev. Appl. 12 , 014026.
- Jones, C., M. A. Fogarty, A. Morello, M. F. Gyure, A. S. Dzurak, and T. D. Ladd, 2018, Phys. Rev. X 8 , 021058.
- Jordan, S., 2021, https://quantumalgorithmzoo.org/ (accessed April 26, 2021).
- Jouravlev, O. N., and Y. V. Nazarov, 2006, Phys. Rev. Lett. 96 , 176804.
- Kalra, R., A. Laucht, C. D. Hill, and A. Morello, 2014, Phys. Rev. X 4 , 021044.
- Kandel, Y. P., H. Qiao, S. Fallahi, G. C. Gardner, M. J. Manfra, and J. M. Nichol, 2019, Nature (London) 573 , 553.
- Kandel, Y. P., H. Qiao, S. Fallahi, G. C. Gardner, M. J. Manfra, and J. M. Nichol, 2021, Nat. Commun. 12 , 1.
- Kane, B. E., 1998, Nature (London) 393 , 133.
- Kastner, M. A., 1992, Rev. Mod. Phys. 64 , 849.
- Kato, Y., R. C. Myers, D. C. Driscoll, A. C. Gossard, J. Levy, and D. D. Awschalom, 2003, Science 299 , 1201.
- Katsaros, G., P. Spathis, M. Stoffel, F. Fournel, M. Mongillo, V. Bouchiat, F. Lefloch, A. Rastelli, O. G. Schmidt, and S. De Franceschi, 2010, Nat. Nanotechnol. 5 , 458.
- Kavokin, K. V., 2001, Phys. Rev. B 64 , 075305.
- Kavokin, K. V., 2004, Phys. Rev. B 69 , 075302.
- Kawakami, E., P. Scarlino, D. R. Ward, F. R. Braakman, D. E. Savage, M. G. Lagally, M. Friesen, S. N. Coppersmith, M. A. Eriksson, and L. M. K. Vandersypen, 2014, Nat. Nanotechnol. 9 , 666.
- Kawakami, E., et al. , 2016, Proc. Natl. Acad. Sci. U.S.A. 113 , 11738. Keith, D., S. K. Gorman, L. Kranz, Y. He, J. G. Keizer, M. A. Broome, and M. Y. Simmons, 2019, New J. Phys. 21 , 063011.
- Keith, D., M. G. House, M. B. Donnelly, T. F. Watson, B. Weber, and M. Y. Simmons, 2019, Phys. Rev. X 9 , 041003.
- Keller, M., A. Eichenberger, J. Martinis, and N. Zimmerman, 1999, Science 285 , 1706.
- Keller, M. W., J. M. Martinis, N. M. Zimmerman, and A. H. Steinbach, 1996, Appl. Phys. Lett. 69 , 1804.
- Kempe, J., D. Bacon, D. A. Lidar, and K. B. Whaley, 2001, Phys. Rev. A 63 , 042307.
- Kerckhoff, J., et al. , 2021, PRX Quantum 2 , 010347.
- Kerman, A. J., 2013, New J. Phys. 15 , 123011.
- Khaetskii, A. V., and Y. V. Nazarov, 2001, Phys. Rev. B 64 , 125316. Kim, D., et al. , 2014, Nature (London) 511 , 70.
- Kimble, H. J., 2008, Nature (London) 453 , 1023.
- Klauser, D., W. A. Coish, and D. Loss, 2006, Phys. Rev. B 73 , 205302.
- Klinovaja, J., D. Stepanenko, B. I. Halperin, and D. Loss, 2012, Phys. Rev. B 86 , 085423.
- Kloeffel, C., M. Trif, P. Stano, and D. Loss, 2013, Phys. Rev. B 88 , 241405.
- Koch, M., J. G. Keizer, P. Pakkiam, D. Keith, M. G. House, E. Peretz, and M. Y. Simmons, 2019, Nat. Nanotechnol. 14 , 137.
- Kogan, A., S. Amasha, D. Goldhaber-Gordon, G. Granger, M. A. Kastner, and H. Shtrikman, 2004, Phys. Rev. Lett. 93 , 166602.
- Koh, T. S., J. K. Gamble, M. Friesen, M. A. Eriksson, and S. N. Coppersmith, 2012, Phys. Rev. Lett. 109 , 250503.
- Koiller, B., X. Hu, and S. Das Sarma, 2001, Phys. Rev. Lett. 88 , 027903.
- Koiller, B., X. Hu, and S. Das Sarma, 2002, Phys. Rev. B 66 , 115201. Koppens, F. H. L., C. Buizert, K. J. Tielrooij, I. T. Vink, K. C. Nowack, T. Meunier, L. P. Kouwenhoven, and L. M. K. Vandersypen, 2006, Nature (London) 442 , 766.
- Koppens, F. H. L., J. A. Folk, J. M. Elzerman, R. Hanson, L. H. W. van Beveren, I. T. Vink, H. P. Tranitz, W. Wegscheider, L. P. Kouwenhoven, and L. M. K. Vandersypen, 2005, Science 309 , 1346.

Koppens, F. H. L., K. C. Nowack, and L. M. K. Vandersypen, 2008, Phys. Rev. Lett. 100 , 236802.

- Koski, J. V., et al. , 2020, Nat. Phys. 16 , 642.
- Kouwenhoven, L., D. G. Austing, and S. Tarucha, 2001, Rep. Prog. Phys. 64 , 701.
- Kouwenhoven, L., and C. Marcus, 1998, Phys. World 11 , 35.
- Kroutvar, M., Y. Ducommun, D. Heiss, M. Bichler, D. Schuh, G. Abstreiter, and J. J. Finley, 2004, Nature (London) 432 , 81.
- Kuemmeth, F., S. Ilani, D. C. Ralph, and P. L. McEuen, 2008, Nature (London) 452 , 448.
- Kyriakidis, J., and G. Burkard, 2007, Phys. Rev. B 75 , 115324.
- Ladd, T. D., 2012, Phys. Rev. B 86 , 125408.
- Ladd, T. D., J. R. Goldman, F. Yamaguchi, Y. Yamamoto, E. Abe, and K. M. Itoh, 2002, Phys. Rev. Lett. 89 , 017901.
- Ladd, T. D., D. Maryenko, Y. Yamamoto, E. Abe, and K. M. Itoh, 2005, Phys. Rev. B 71 , 014401.
- Lai, N. S., W. H. Lim, C. H. Yang, F. A. Zwanenburg, W. A. Coish, F. Qassemi, A. Morello, and A. S. Dzurak, 2011, Sci. Rep. 1 , 110. Laird, E. A., F. Kuemmeth, G. A. Steele, K. Grove-Rasmussen, J. Nygård, K. Flensberg, and L. P. Kouwenhoven, 2015, Rev. Mod. Phys. 87 , 703.
- Laird, E. A., F. Pei, and L. P. Kouwenhoven, 2013, Nat. Nanotechnol. 8 , 565.
- Laird, E. A., J. M. Taylor, D. P. DiVincenzo, C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2010, Phys. Rev. B 82 , 075403.
- Landauer, R., 1991, Phys. Today 44 , No. 5, 23.
- Landig, A. J., J. V. Koski, P. Scarlino, U. C. Mendes, A. Blais, C. Reichl, W. Wegscheider, A. Wallraff, K. Ensslin, and T. Ihn, 2018, Nature (London) 560 , 179.
- Landig, A. J., et al. , 2019, Nat. Commun. 10 , 5037.
- Langsjoen, L. S., A. Poudel, M. G. Vavilov, and R. Joynt, 2012, Phys. Rev. A 86 , 010301.
- Larsen, T. W., K. D. Petersson, F. Kuemmeth, T. S. Jespersen, P. Krogstrup, J. Nygård, and C. M. Marcus, 2015, Phys. Rev. Lett. 115 , 127001.
- Laucht, A., et al. , 2015, Sci. Adv. 1 , e1500022.
- Laucht, A., et al. , 2017, Nat. Nanotechnol. 12 , 61.
- Lawrie, W. I. L., et al. , 2020, Appl. Phys. Lett. 116 , 080501.
- Lee, D., S. Meyer, S. Gong, R. Lu, and K. Lai, 2021, Appl. Phys. Lett. 119 , 214101.
- Levy, J., 2002, Phys. Rev. Lett. 89 , 147902.
- Li, R., X. Hu, and J. Q. You, 2012, Phys. Rev. B 86 , 205306.
- Li, R., F. E. Hudson, A. S. Dzurak, and A. R. Hamilton, 2015, Nano Lett. 15 , 7314.
- Lidar, D. A., I. L. Chuang, and K. B. Whaley, 1998, Phys. Rev. Lett. 81 , 2594.
- Lieb, E., and D. Mattis, 1962, Phys. Rev. 125 , 164.
- Liles, S., et al. , 2021, Phys. Rev. B 104 , 235303.
- Liles, S. D., R. Li, C. H. Yang, F. E. Hudson, M. Veldhorst, A. S. Dzurak, and A. R. Hamilton, 2018, Nat. Commun. 9 , 3255.
- Linke, N. M., D. Maslov, M. Roetteler, S. Debnath, C. Figgatt, K. A. Landsman, K. Wright, and C. Monroe, 2017, Proc. Natl. Acad. Sci. U.S.A. 114 , 3305.
- Liu, Y.-Y., L. A. Orona, S. F. Neyens, E. R. MacQuarrie, M. A. Eriksson, and A. Yacoby, 2021, Phys. Rev. Appl. 16 , 024029.
- Liu, Y.-Y., K. D. Petersson, J. Stehlik, J. M. Taylor, and J. R. Petta, 2014, Phys. Rev. Lett. 113 , 036801.
- Liu, Y.-Y., J. Stehlik, C. Eichler, M. J. Gullans, J. M. Taylor, and J. R. Petta, 2015, Science 347 , 285.
- Liu, Z.-H., O. Entin-Wohlman, A. Aharony, and J. Q. You, 2018, Phys. Rev. B 98 , 241303.
- Loss, D., and D. P. DiVincenzo, 1998, Phys. Rev. A 57 , 120.
- Lowenthal, F., 1972, Can. J. Math. 24 , 713.
- Lyding, J. W., T. Shen, J. S. Hubacek, J. R. Tucker, and G. C. Abeln, 1994, Appl. Phys. Lett. 64 , 2010.
- Mabuchi, H., and A. C. Doherty, 2002, Science 298 , 1372.
- Macklin, C., K. O Brien, D. Hover, M. E. Schwartz, V. Bolkhovsky, '
- X. Zhang, W. D. Oliver, and I. Siddiqi, 2015, Science 350 , 307. Madzik, M. T., A. Laucht, F. E. Hudson, A. M. Jakob, B. C. Johnson,
- D. N. Jamieson, K. M. Itoh, A. S. Dzurak, and A. Morello, 2021, Nat. Commun. 12 , 181.
- Madzik, M. T., et al. , 2020, Sci. Adv. 6 , eaba3442.
- Madzik, M. T., et al. , 2022, Nature (London) 601 , 348.
- Magesan, E., J. M. Gambetta, and J. Emerson, 2011, Phys. Rev. Lett. 106 , 180504.
- Majer, J., et al. , 2007, Nature (London) 449 , 443.
- Mak, W. Y., F. Sfigakis, K. Das Gupta, O. Klochan, H. E. Beere, I. Farrer, J. P. Griffiths, G. A. C. Jones, A. R. Hamilton, and D. A. Ritchie, 2013, Appl. Phys. Lett. 102 , 103507.
- Malinowski, F. K., F. Martins, P. D. Nissen, S. Fallahi, G. C. Gardner, M. J. Manfra, C. M. Marcus, and F. Kuemmeth, 2017, Phys. Rev. B 96 , 045443.
- Malinowski, F. K., et al. , 2017, Nat. Nanotechnol. 12 , 16.
- Malinowski, F. K., et al. , 2019, Nat. Commun. 10 , 1196.
- Manfra, M. J., 2014, Annu. Rev. Condens. Matter Phys. 5 , 347.
- Martins, F., F. K. Malinowski, P. D. Nissen, E. Barnes, S. Fallahi, G. C. Gardner, M. J. Manfra, C. M. Marcus, and F. Kuemmeth, 2016, Phys. Rev. Lett. 116 , 116801.
- Martins, F., F. K. Malinowski, P. D. Nissen, S. Fallahi, G. C. Gardner, M. J. Manfra, C. M. Marcus, and F. Kuemmeth, 2017, Phys. Rev. Lett. 119 , 227701.
- Maune, B. M., et al. , 2012, Nature (London) 481 , 344.
- Maurand, R., et al. , 2016, Nat. Commun. 7 , 13575.
- McJunkin, T., et al. , 2021, Phys. Rev. B 104 , 085406.
- McNeil, R. P. G., M. Kataoka, C. J. B. Ford, C. H. W. Barnes, D. Anderson, G. A. C. Jones, I. Farrer, and D. A. Ritchie, 2011, Nature (London) 477 , 439.
- Medford, J., J. Beil, J. M. Taylor, S. D. Bartlett, A. C. Doherty, E. I. Rashba, D. P. DiVincenzo, H. Lu, A. C. Gossard, and C. M. Marcus, 2013, Nat. Nanotechnol. 8 , 654.
- Medford, J., J. Beil, J. M. Taylor, E. I. Rashba, H. Lu, A. C. Gossard, and C. M. Marcus, 2013, Phys. Rev. Lett. 111 , 050501.
- Melnikov, D. V., and J.-P. Leburton, 2006, Phys. Rev. B 73 , 155301.
- Meunier, T., V. E. Calado, and L. M. K. Vandersypen, 2011, Phys. Rev. B 83 , 121403.
- Meunier, T., I. T. Vink, L. H. W. van Beveren, K.-J. Tielrooij, R. Hanson, F. H. L. Koppens, H. P. Tranitz, W. Wegscheider, L. P. Kouwenhoven, and L. M. K. Vandersypen, 2007, Phys. Rev. Lett. 98 , 126601.
- Mi, X., M. Benito, S. Putz, D. M. Zajac, J. M. Taylor, G. Burkard, and J. R. Petta, 2018, Nature (London) 555 , 599.
- Mi, X., J. V. Cady, D. M. Zajac, P. W. Deelman, and J. R. Petta, 2017, Science 355 , 156.
- Mi, X., S. Kohler, and J. R. Petta, 2018, Phys. Rev. B 98 , 161404.
- Mi, X., C. G. Peterfalvi, G. Burkard, and J. R. Petta, 2017, Phys. Rev. Lett. 119 , 176803.
- Mielke, J., J. R. Petta, and G. Burkard, 2021, PRX Quantum 2 , 020347.
- Miller, R., T. E. Northup, K. M. Birnbaum, A. Boca, A. D. Boozer, and H. J. Kimble, 2005, J. Phys. B 38 , S551.
- Mills, A., C. Guinn, M. M. Feldman, A. J. Sigillito, M. J. Gullans, M. T. Rakher, J. Kerckhoff, C. A. C. Jackson, and J. R. Petta, 2022, Phys. Rev. Appl. 18 , 064028.

Mills, A. R., M. M. Feldman, C. Monical, P. J. Lewis, K. W. Larson, A. M. Mounce, and J. R. Petta, 2019, Appl. Phys. Lett. 115 , 113501.

- Mills, A. R., C. R. Guinn, M. J. Gullans, A. J. Sigillito, M. M. Feldman, E. Nielsen, and J. R. Petta, 2022, Sci. Adv. 8 , eabn5130.
- Mills, A. R., D. M. Zajac, M. J. Gullans, F. J. Schupp, T. M. Hazard, and J. R. Petta, 2019, Nat. Commun. 10 , 1063.
- Mohiyaddin, F. A., R. Kalra, A. Laucht, R. Rahman, G. Klimeck, and A. Morello, 2016, Phys. Rev. B 94 , 045314.
- Mohseni, M., A. T. Rezakhani, and D. A. Lidar, 2008, Phys. Rev. A 77 , 032322.
- Montanaro, A., 2016, npj Quantum Inf. 2 , 15023.
- Morello, A., et al. , 2010, Nature (London) 467 , 687.
- Mortemousque, P.-A., E. Chanrion, B. Jadot, H. Flentje, A. Ludwig, A. D. Wieck, M. Urdampilleta, C. B¨ auerle, and T. Meunier, 2021, Nat. Nanotechnol. 16 , 296.
- Mourik, V., K. Zuo, S. M. Frolov, S. R. Plissard, E. P. A. M. Bakkers, and L. P. Kouwenhoven, 2012, Science 336 , 1003.
- Muhonen, J. T., et al. , 2014, Nat. Nanotechnol. 9 , 986.
- Muhonen, J. T., et al. , 2015, J. Phys. Condens. Matter 27 , 154205. Mutter, P. M., and G. Burkard, 2021, Phys. Rev. Res. 3 , 013194.
- Nadj-Perge, S., S. M. Frolov, E. P. A. M. Bakkers, and L. P. Kouwenhoven, 2010, Nature (London) 468 , 1084.
- Nadj-Perge, S., V. S. Pribiag, J. W. G. van den Berg, K. Zuo, S. R. Plissard, E. P. A. M. Bakkers, S. M. Frolov, and L. P. Kouwenhoven, 2012, Phys. Rev. Lett. 108 , 166801.
- Nakajima, T., et al. , 2020, Phys. Rev. X 10 , 011060.
- Nakaoka, T., S. Tarucha, and Y. Arakawa, 2007, Phys. Rev. B 76 , 041301(R).
- Neder, I., M. S. Rudner, H. Bluhm, S. Foletti, B. I. Halperin, and A. Yacoby, 2011, Phys. Rev. B 84 , 035441.
- Neder, I., M. S. Rudner, and B. I. Halperin, 2014, Phys. Rev. B 89 , 085403.
- Nestoklon, M. O., E. L. Ivchenko, J.-M. Jancu, and P. Voisin, 2008, Phys. Rev. B 77 , 155328.
- Nichol, J. M., S. P. Harvey, M. D. Shulman, A. Pal, V. Umansky, E. I. Rashba, B. I. Halperin, and A. Yacoby, 2015, Nat. Commun. 6 , 7682.
- Nichol, J. M., L. A. Orona, S. P. Harvey, S. Fallahi, G. C. Gardner, M. J. Manfra, and A. Yacoby, 2017, npj Quantum Inf. 3 , 3.
- Nielsen, E., E. Barnes, J. P. Kestner, and S. Das Sarma, 2013, Phys. Rev. B 88 , 195131.
- Nielsen, E., J. K. Gamble, K. Rudinger, T. Scholten, K. Young, and R. Blume-Kohout, 2021, Quantum 5 , 557.
- Nielsen, E., R. Rahman, and R. P. Muller, 2012, J. Appl. Phys. 112 , 114304.
- Nielsen, M. A., and I. L. Chuang, 2000, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England).
- Noiri, A., K. Takeda, T. Nakajima, T. Kobayashi, A. Sammak, G. Scappucci, and S. Tarucha, 2022, Nature (London) 601 , 338.
- Noiri, A., K. Takeda, J. Yoneda, T. Nakajima, T. Kodera, and S. Tarucha, 2020, Nano Lett. 20 , 947.
- Nowack, K. C., F. H. L. Koppens, Y. V. Nazarov, and L. M. K. Vandersypen, 2007, Science 318 , 1430.
- Nowack, K. C., M. Shafiei, M. Laforest, G. E. D. K. Prawiroatmodjo, L. R. Schreiber, C. Reichl, W. Wegscheider, and L. M. K. Vandersypen, 2011, Science 333 , 1269.
- O Gorman, J., ' N. H. Nickerson, P. Ross, J. J. Morton, and S. C. Benjamin, 2016, npj Quantum Inf. 2 , 15019.
- Oh, S., M. Friesen, and X. Hu, 2010, Phys. Rev. B 82 , 140403.
- Oh, S., Y.-P. Shim, J. Fei, M. Friesen, and X. Hu, 2013, Phys. Rev. A 87 , 022332.
- Ono, K., D. G. Austing, Y. Tokura, and S. Tarucha, 2002, Science 297 , 1313.
- Orona, L. A., J. M. Nichol, S. P. Harvey, C. G. L. Bøttcher, S. Fallahi, G. C. Gardner, M. J. Manfra, and A. Yacoby, 2018, Phys. Rev. B
- 98 , 125404.
- Paget, D., G. Lampel, B. Sapoval, and V. I. Safarov, 1977, Phys. Rev. B 15 , 5780.
- Pakkiam, P., A. Timofeev, M. House, M. Hogg, T. Kobayashi, M. Koch, S. Rogge, and M. Simmons, 2018, Phys. Rev. X 8 , 041032. Pal, A., E. I. Rashba, and B. I. Halperin, 2014, Phys. Rev. X 4 , 011012.
- Pal, A., E. I. Rashba, and B. I. Halperin, 2015, Phys. Rev. B 92 , 125409.
- Pályi, A., and G. Burkard, 2010, Phys. Rev. B 82 , 155424.
- Pan, A., T. E. Keating, M. F. Gyure, E. J. Pritchett, S. Quinn, R. S. Ross, T. D. Ladd, and J. Kerckhoff, 2020, Quantum Sci. Technol. 5 , 034005.
- Pan, H., M. G. House, X. Hao, and H. W. Jiang, 2012, Appl. Phys. Lett. 100 , 263109.
- Pantelides, S. T., 1978, Rev. Mod. Phys. 50 , 797.
- Pei, F., E. A. Laird, G. A. Steele, and L. P. Kouwenhoven, 2012, Nat. Nanotechnol. 7 , 630.
- Penthorn, N. E., J. S. Schoenfield, L. F. Edge, and H. Jiang, 2020, Phys. Rev. Appl. 14 , 054015.
- Petersson, K., J. Petta, H. Lu, and A. Gossard, 2010, Phys. Rev. Lett. 105 , 246804.
- Petersson, K. D., L. W. McFaul, M. D. Schroer, M. Jung, J. M. Taylor, A. A. Houck, and J. R. Petta, 2012, Nature (London) 490 , 380.
- Petit, L., H. Eenink, M. Russ, W. Lawrie, N. Hendrickx, S. Philips, J. Clarke, L. Vandersypen, and M. Veldhorst, 2020, Nature (London) 580 , 355.
- Petit, L., et al. , 2018, Phys. Rev. Lett. 121 , 076801.
- Petrosyan, D., G. M. Nikolopoulos, and P. Lambropoulos, 2010, Phys. Rev. A 81 , 042307.
- Petta, J. R., A. C. Johnson, C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2004, Phys. Rev. Lett. 93 , 186802.

Petta, J. R., A. C. Johnson, J. M. Taylor, E. Laird, A. Yacoby, M. D.

- Lukin, C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2005, Science 309 , 2180.
- Petta, J. R., H. Lu, and A. C. Gossard, 2010, Science 327 , 669.
- Petta, J. R., and D. C. Ralph, 2001, Phys. Rev. Lett. 87 , 266801.
- Petta, J. R., and D. C. Ralph, 2002, Phys. Rev. Lett. 89 , 156802.
- Petta, J. R., J. M. Taylor, A. C. Johnson, A. Yacoby, M. D. Lukin,
- C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2008, Phys. Rev. Lett. 100 , 067601.
- Philippopoulos, P., S. Chesi, and W. A. Coish, 2020, Phys. Rev. B 101 , 115302.
- Picó-Cort´ es, J., F. Gallego-Marcos, and G. Platero, 2019, Phys. Rev. B 99 , 155421.
- Pioro-Ladriere, M., T. Obata, Y. Tokura, Y. S. Shin, T. Kubo, K. Yoshida, T. Taniyama, and S. Tarucha, 2008, Nat. Phys. 4 , 776. Piot, N., et al. , 2022, Nat. Nanotechnol. 17 , 1072.
- Pla, J. J., K. Y . Tan, J. P. Dehollain, W. H. Lim, J. J. L. Morton, D. N. Jamieson, A. S. Dzurak, and A. Morello, 2012, Nature (London) 489 , 541.
- Pla, J. J., K. Y . Tan, J. P. Dehollain, W. H. Lim, J. J. L. Morton, F. A. Zwanenburg, D. N. Jamieson, A. S. Dzurak, and A. Morello, 2013, Nature (London) 496 , 334.
- Poulin-Lamarre, G., J. Thorgrimson, S. A. Studenikin, G. C. Aers, A. Kam, P. Zawadzki, Z. R. Wasilewski, and A. S. Sachrajda, 2015, Phys. Rev. B 91 , 125417.
- Prada, M., G. Klimeck, and R. Joynt, 2011, New J. Phys. 13 , 013009.

Prechtel, J. H., A. V . Kuhlmann, J. Houel, A. Ludwig, S. R. Valentin,

A. D. Wieck, and R. J. Warburton, 2016, Nat. Mater.

15

,

981.

Preskill, J.,

2018, Quantum

2

,

79.

- Qiao, H., Y. P. Kandel, K. Deng, S. Fallahi, G. C. Gardner, M. J. Manfra, E. Barnes, and J. M. Nichol, 2020, Phys. Rev. X 10 , 031006.
- Qiao, H., Y. P. Kandel, J. S. V. Dyke, S. Fallahi, G. C. Gardner, M. J. Manfra, E. Barnes, and J. M. Nichol, 2021, Nat. Commun. 12 , 2142.
- Qiao, H., Y. P. Kandel, S. Fallahi, G. C. Gardner, M. J. Manfra, X. Hu, and J. M. Nichol, 2021, Phys. Rev. Lett. 126 , 017701.
- Rashba, E. I., and A. L. Efros, 2003, Phys. Rev. Lett. 91 , 126405. Reed, M. D., et al. , 2016, Phys. Rev. Lett. 116 , 110402.
- Reilly, D. J., C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2007, Appl. Phys. Lett. 91 , 162101.
- Reilly, D. J., J. M. Taylor, J. R. Petta, C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2010, Phys. Rev. Lett. 104 , 236802.
- Reimann, S. M., and M. Manninen, 2002, Rev. Mod. Phys. 74 , 1283. Reithmaier, J. P., G. S k, ę A. Löffler, C. Hofmann, S. Kuhn, S. Reitzenstein, L. V. Keldysh, V. D. Kulakovskii, T. L. Reinecke, and A. Forchel, 2004, Nature (London) 432 , 197.
- Ribeiro, H., and G. Burkard, 2009, Phys. Rev. Lett. 102 , 216802. Ribeiro, H., J. R. Petta, and G. Burkard, 2010, Phys. Rev. B 82 , 115445.
- Rontani, M., 2006, J. Chem. Phys. 124 , 124102.
- Roth, L. M., 1960, Phys. Rev. 118 , 1534.
- Ruskov, R., M. Veldhorst, A. S. Dzurak, and C. Tahan, 2018, Phys. Rev. B 98 , 245424.
- Russ, M., and G. Burkard, 2015a, Phys. Rev. B 91 , 235411.
- Russ, M., and G. Burkard, 2015b, Phys. Rev. B 92 , 205412.
- Russ, M., F. Ginzel, and G. Burkard, 2016, Phys. Rev. B 94 , 165411.
- Russ, M., J. R. Petta, and G. Burkard, 2018, Phys. Rev. Lett. 121 , 177701.
- Russ, M., D. M. Zajac, A. J. Sigillito, F. Borjans, J. M. Taylor, J. R. Petta, and G. Burkard, 2018, Phys. Rev. B 97 , 085421.
- Saeedi, K., S. Simmons, J. Z. Salvail, P. Dluhy, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, J. J. L. Morton, and M. L. W. Thewalt, 2013, Science 342 , 830.
- Sala, A., and J. Danon, 2017, Phys. Rev. B 95 , 241303.
- Salfi, J., J. A. Mol, D. Culcer, and S. Rogge, 2016, Phys. Rev. Lett. 116 , 246801.
- Salfi, J., B. Voisin, A. Tankasala, J. Bocquel, M. Usman, M. Simmons, L. Hollenberg, R. Rahman, and S. Rogge, 2018, Phys. Rev. X 8 , 031049.
- Samkharadze, N., G. Zheng, N. Kalhor, D. Brousse, A. Sammak, U. C. Mendes, A. Blais, G. Scappucci, and L. M. K. Vandersypen, 2018, Science 359 , 1123.
- Sánchez, R., F. Gallego-Marcos, and G. Platero, 2014, Phys. Rev. B 89 , 161402.
- Sánchez, R., G. Granger, L. Gaudreau, A. Kam, M. Pioro-Ladriere, S. A. Studenikin, P. Zawadzki, A. S. Sachrajda, and G. Platero, 2014, Phys. Rev. Lett. 112 , 176803.
- Sapmaz, S., P. Jarillo-Herrero, L. P. Kouwenhoven, and H. S. J. van der Zant, 2006, Semicond. Sci. Technol. 21 , S52.
- Saraiva, A. L., M. J. Calderón, X. Hu, S. Das Sarma, and B. Koiller, 2009, Phys. Rev. B 80 , 081305.
- Saraiva, A. L., M. J. Calderón, and B. Koiller, 2007, Phys. Rev. B 76 , 233302.
- Savytskyy, R., et al. , 2023, Sci. Adv. 9 , eadd9408.
- Scappucci, G., C. Kloeffel, F. A. Zwanenburg, D. Loss, M. Myronov, J.-J. Zhang, S. De Franceschi, G. Katsaros, and M. Veldhorst, 2021, Nat. Rev. Mater. 6 , 926.
- Scarlino, P., E. Kawakami, P. Stano, M. Shafiei, C. Reichl, W. Wegscheider, and L. Vandersypen, 2014, Phys. Rev. Lett. 113 , 256802.
- Scarlino, P., et al. , 2019, Nat. Commun. 10 , 1.
- Sch¨ affler, F., 1997, Semicond. Sci. Technol. 12 , 1515.
- Schoelkopf, R. J., P. Wahlgren, A. A. Kozhevnikov, P. Delsing, and D. E. Prober, 1998, Science 280 , 1238.
- Schofield, S. R., N. J. Curson, M. Y. Simmons, F. J. Rueß, T. Hallam, L. Oberbeck, and R. G. Clark, 2003, Phys. Rev. Lett. 91 , 136104.
- Schroer, M. D., M. Jung, K. D. Petersson, and J. R. Petta, 2012, Phys. Rev. Lett. 109 , 166804.
- Schroer, M. D., K. D. Petersson, M. Jung, and J. R. Petta, 2011, Phys. Rev. Lett. 107 , 176811.
- Schröer, D., A. D. Greentree, L. Gaudreau, K. Eberl, L. C. L. Hollenberg, J. P. Kotthaus, and S. Ludwig, 2007, Phys. Rev. B 76 , 075306.
- Schuch, N., and J. Siewert, 2003, Phys. Rev. A 67 , 032301.
- Seidler, I., T. Struck, R. Xue, N. Focke, S. Trellenkamp, H. Bluhm, and L. R. Schreiber, 2022, npj Quantum Inf. 8 , 100.
- Setiawan, F., H.-Y. Hui, J. P. Kestner, X. Wang, and S. D. Sarma, 2014, Phys. Rev. B 89 , 085314.
- Shi, Z., et al. , 2012, Phys. Rev. Lett. 108 , 140503.
- Shi, Z., et al. , 2014, Nat. Commun. 5 , 3020.
- Shim, Y.-P., R. Ruskov, H. M. Hurst, and C. Tahan, 2019, Appl. Phys. Lett. 114 , 152105.
- Shim, Y.-P., and C. Tahan, 2016, Phys. Rev. B 93 , 121410.
- Shim, Y.-P., and C. Tahan, 2018, Phys. Rev. B 97 , 155402.
- Shor, P. W., 1997, SIAM J. Comput. 26 , 1484.
- Shulman, M. D., O. E. Dial, S. P. Harvey, H. Bluhm, V. Umansky, and A. Yacoby, 2012, Science 336 , 202.
- Shulman, M. D., S. P. Harvey, J. M. Nichol, S. D. Bartlett, A. C. Doherty, V. Umansky, and A. Yacoby, 2014, Nat. Commun. 5 , 5156.
- Sigillito, A., J. Loy, D. Zajac, M. Gullans, L. Edge, and J. Petta, 2019, Phys. Rev. Appl. 11 , 061006.
- Sigillito, A. J., M. J. Gullans, L. F. Edge, M. Borselli, and J. R. Petta, 2019, npj Quantum Inf. 5 , 110.
- Sigillito, A. J., A. M. Tyryshkin, T. Schenkel, A. A. Houck, and S. A. Lyon, 2017, Nat. Nanotechnol. 12 , 958.
- Sillanpaa, M. A., J. I. Park, and R. W. Simmonds, 2007, Nature (London) 449 , 438.
- Slichter, C. P., 2010, Principles of Magnetic Resonance (Springer, New York).
- Smith, J. S., A. Budi, M. C. Per, N. Vogt, D. W. Drumm, L. C. L. Hollenberg, J. H. C. Cole, and S. P. Russo, 2017, Sci. Rep. 7 , 6010. Srinivasa, V., J. Levy, and C. S. Hellberg, 2007, Phys. Rev. B 76 , 094411.
- Srinivasa, V., K. C. Nowack, M. Shafiei, L. M. K. Vandersypen, and J. M. Taylor, 2013, Phys. Rev. Lett. 110 , 196803.
- Srinivasa, V., J. M. Taylor, and C. Tahan, 2016, Phys. Rev. B 94 , 205421.
- Stano, P., and J. Fabian, 2005, Phys. Rev. B 72 , 155410.
- Stano, P., and J. Fabian, 2006, Phys. Rev. B 74 , 045320.
- Stano, P., and D. Loss, 2022, Nat. Rev. Phys. 4 , 672.
- Stehlik, J., Y .-Y . Liu, C. M. Quintana, C. Eichler, T. R. Hartke, and
- J. R. Petta, 2015, Phys. Rev. Appl. 4 , 014018.
- Stehlik, J., M. D. Schroer, M. Z. Maialle, M. H. Degani, and J. R. Petta, 2014, Phys. Rev. Lett. 112 , 227601.
- Stepanenko, D., and G. Burkard, 2007, Phys. Rev. B 75 , 085324. Stepanenko, D., M. S. Rudner, B. I. Halperin, and D. Loss, 2012, Phys. Rev. B 85 , 075416.

- Stockklauser, A., V. F. Maisi, J. Basset, K. Cujia, C. Reichl, W. Wegscheider, T. Ihn, A. Wallraff, and K. Ensslin, 2015, Phys. Rev. Lett. 115 , 046802.
- Stockklauser, A., P. Scarlino, J. V. Koski, S. Gasparinetti, C. K. Andersen, C. Reichl, W. Wegscheider, T. Ihn, K. Ensslin, and A. Wallraff, 2017, Phys. Rev. X 7 , 011030.
- Struck, T., et al. , 2020, npj Quantum Inf. 6 , 40.
- Studenikin, S. A., J. Thorgrimson, G. C. Aers, A. Kam, P. Zawadzki, Z. R. Wasilewski, A. Bogan, and A. S. Sachrajda, 2012, Appl. Phys. Lett. 101 , 233101.
- Szabo, A., and N. S. Ostlund, 1996, Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory (Dover Publications, New York).
- Tahan, C., and R. Joynt, 2014, Phys. Rev. B 89 , 075302.
- Takahashi, M., S. D. Bartlett, and A. C. Doherty, 2013, Phys. Rev. A 88 , 022120.
- Takeda, K., A. Noiri, J. Yoneda, T. Nakajima, and S. Tarucha, 2020, Phys. Rev. Lett. 124 , 117701.
- Takeda, K., et al. , 2016, Sci. Adv. 2 , 1600694.
- Tankasala, A., J. Salfi, J. Bocquel, B. V oisin, M. Usman, G. Klimeck, M. Y. Simmons, L. C. L. Hollenberg, S. Rogge, and R. Rahman, 2018, Phys. Rev. B 97 , 195301.
- Tanttu, T., et al. , 2019, Phys. Rev. X 9 , 021028.
- Taylor, J. M., H.-A. Engel, W. Dur, A. Yacoby, C. M. Marcus, P. Zoller, and M. D. Lukin, 2005, Nat. Phys. 1 , 177.
- Taylor, J. M., J. R. Petta, A. C. Johnson, A. Yacoby, C. M. Marcus, and M. D. Lukin, 2007, Phys. Rev. B 76 , 035315.
- Taylor, J. M., V. Srinivasa, and J. Medford, 2013, Phys. Rev. Lett. 111 , 050502.
- Tenberg, S. B., et al. , 2019, Phys. Rev. B 99 , 205306.
- Terrazos, L. A., et al. , 2021, Phys. Rev. B 103 , 125201.
- Testelin, C., F. Bernardot, B. Eble, and M. Chamarro, 2009, Phys. Rev. B 79 , 195440.
- Tettamanzi, G. C., S. J. Hile, M. G. House, M. Fuechsle, S. Rogge, and M. Y. Simmons, 2017, ACS Nano 11 , 2444.
- Tokura, Y., W. G. van der Wiel, T. Obata, and S. Tarucha, 2006, Phys. Rev. Lett. 96 , 047202.
- Tosi, G., F. A. Mohiyaddin, H. Huebl, and A. Morello, 2014, AIP Adv. 4 , 087122.
- Tosi, G., F. A. Mohiyaddin, V. Schmitt, S. Tenberg, R. Rahman, G. Klimeck, and A. Morello, 2017, Nat. Commun. 8 , 450.
- Tracy, L. A., T. W. Hargett, and J. L. Reno, 2014, Appl. Phys. Lett. 104 , 123101.
- Tracy, L. A., D. R. Luhman, S. M. Carr, N. C. Bishop, G. A. Ten Eyck, T. Pluym, J. R. Wendt, M. P. Lilly, and M. S. Carroll, 2016, Appl. Phys. Lett. 108 , 063101.
- Trif, M., V. N. Golovach, and D. Loss, 2008, Phys. Rev. B 77 , 045434.
- Trif, M., P. Simon, and D. Loss, 2009, Phys. Rev. Lett. 103 , 106601.
- Tyryshkin, A. M., et al. , 2012, Nat. Mater. 11 , 143.
- Uhrig, G. S., 2007, Phys. Rev. Lett. 98 , 100504.
- Urdampilleta, M., et al. , 2019, Nat. Nanotechnol. 14 , 737.
- Vahapoglu, E., et al. , 2021, Sci. Adv. 7 , eabg9158.
- van Beveren, L. H. W., R. Hanson, I. T. Vink, F. H. L. Koppens, L. P. Kouwenhoven, and L. M. K. Vandersypen, 2005, New J. Phys. 7 , 182.
- Vandersypen, L. M. K., H. Bluhm, J. S. Clarke, A. S. Dzurak, R. Ishihara, A. Morello, D. J. Reilly, L. R. Schreiber, and M. Veldhorst, 2017, npj Quantum Inf. 3 , 34.
- Vandersypen, L. M. K., and I. L. Chuang, 2005, Rev. Mod. Phys. 76 , 1037.
- van der Wiel, W. G., S. De Franceschi, J. M. Elzerman, T. Fujisawa, S. Tarucha, and L. P. Kouwenhoven, 2002, Rev. Mod. Phys. 75 , 1.
- van der Wiel, W. G., M. Stopa, T. Kodera, T. Hatano, and S. Tarucha, 2006, New J. Phys. 8 , 28.
- van Diepen, C. J., P. T. Eendebak, B. T. Buijtendorp, U. Mukhopadhyay, T. Fujita, C. Reichl, W. Wegscheider, and L. M. K. Vandersypen, 2018, Appl. Phys. Lett. 113 , 033101.
- van Diepen, C. J., T.-K. Hsiao, U. Mukhopadhyay, C. Reichl, W. Wegscheider, and L. M. K. Vandersypen, 2021, Phys. Rev. X 11 , 041025.
- van Meter, J. R., and E. Knill, 2019, Phys. Rev. A 99 , 042331. van Riggelen, F., N. W. Hendrickx, W. I. L. Lawrie, M. Russ, A. Sammak, G. Scappucci, and M. Veldhorst, 2021, Appl. Phys. Lett. 118 , 044002.
- van Weperen, I., B. D. Armstrong, E. A. Laird, J. Medford, C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2011, Phys. Rev. Lett. 107 , 030506.
- van Woerkom, D. J., A. Proutski, B. van Heck, D. Bouman, J. I. Vayryne, L. I. Glazman, P. Krogstrup, J. Nygard, L. P. Kouwenhoven, and A. Geresdi, 2017, Nat. Phys. 13 , 876.
- van Woerkom, D. J., et al. , 2018, Phys. Rev. X 8 , 041018.
- Varshalovich, D. A., A. N. Moskalev, and V. K. Khersonskii, 1988, Quantum Theory of Angular Momentum (World Scientific, Singapore).
- Veldhorst, M., R. Ruskov, C. H. Yang, J. C. C. Hwang, F. E. Hudson, M. E. Flatt´ e, C. Tahan, K. M. Itoh, A. Morello, and A. S. Dzurak, 2015, Phys. Rev. B 92 , 201401.
- Veldhorst, M., et al. , 2014, Nat. Nanotechnol. 9 , 981.
- Veldhorst, M., et al. , 2015, Nature (London) 526 , 410.
- Venitucci, B., L. Bourdet, D. Pouzada, and Y. Niquet, 2018, Phys. Rev. B 98 , 155319.
- Viennot, J. J., M. R. Delbecq, L. E. Bruhat, M. C. Dartiailh, M. M. Desjardins, M. Baillergeau, A. Cottet, and T. Kontos, 2016, C.R. Phys. 17 , 705.
- Vink, I. T., T. Nooitgedagt, R. N. Schouten, L. M. K. Vandersypen, and W. Wegscheider, 2007, Appl. Phys. Lett. 91 , 123512.
- Vion, D., A. Aassime, A. Cottet, P. Joyez, H. Pothier, C. Urbina, D. Esteve, and M. H. Devoret, 2002, Science 296 , 886.
- Vitanov, N. V., A. A. Rangelov, B. W. Shore, and K. Bergmann, 2017, Rev. Mod. Phys. 89 , 015006.
- Voisin, B., R. Maurand, S. Barraud, M. Vinet, X. Jehl, M. Sanquer, J. Renard, and S. De Franceschi, 2016, Nano Lett. 16 , 88.
- Volk, C., et al. , 2019, npj Quantum Inf. 5 , 29.
- Vrijen, R., E. Yablonovitch, K. Wang, H. W. Jiang, A. Balandin, V. Roychowdhury, T. Mor, and D. DiVincenzo, 2000, Phys. Rev. A 62 , 012306.
- Wallraff, A., D. I. Schuster, A. Blais, L. Frunzio, R. S. Huang, J. Majer, S. Kumar, S. M. Girvin, and R. J. Schoelkopf, 2004, Nature (London) 431 , 162.
- Walther, H., B. T. H. Varcoe, B.-G. Englert, and T. Becker, 2006, Rep. Prog. Phys. 69 , 1325.
- Wang, Y., A. Tankasala, L. C. L. Hollenberg, G. Klimeck, M. Y. Simmons, and R. Rahman, 2016, npj Quantum Inf. 2 , 16008. Warburton, R. J., 2013, Nat. Mater. 12 , 483.
- Wardrop, M. P., and A. C. Doherty, 2014, Phys. Rev. B 90 , 045418.
- Warren, A., E. Barnes, and S. E. Economou, 2019, Phys. Rev. B 100 , 161303.
- Watson, T. F., B. Weber, Y.-L. Hsueh, L. C. L. Hollenberg, R.
- Rahman, and M. Y. Simmons, 2017, Sci. Adv. 3 , e1602811.
- Watson, T. F., et al. , 2018, Nature (London) 555 , 633.

Watzinger, H., J. Kuku č ka, L. Vuku i š ć , F. Gao, T. Wang, F. Sch¨ affler,

- J.-J. Zhang, and G. Katsaros, 2018, Nat. Commun. 9 , 3902. Weber, B., Y.-L. Hsueh, T. F. Watson, R. Li, A. R. Hamilton, L. C. L. Hollenberg, R. Rahman, and M. Y. Simmons, 2018, npj Quantum Inf. 4 , 61.
- Weber, B., Y. H. M. Tan, S. Mahapatra, T. F. Watson, H. Ryu, R. Rahman, L. C. L. Hollenberg, G. Klimeck, and M. Y. Simmons, 2014, Nat. Nanotechnol. 9 , 430.
- Weinstein, A. J., et al. , 2023, Nature (London) 615 , 817.
- Wellard, C. J., L. C. L. Hollenberg, F. Parisoli, L. M. Kettle, H.-S. Goan, J. A. L. McIntosh, and D. N. Jamieson, 2003, Phys. Rev. B 68 , 195209.
- West, A., et al. , 2019, Nat. Nanotechnol. 14 , 437.
- White, Z., and G. Ramon, 2018, Phys. Rev. B 97 , 045306.
- Wilson, D. K., and G. Feher, 1961, Phys. Rev. 124 , 1068.
- Witzel, W. M., M. S. Carroll, A. Morello, L. Cywi ń ski, and S. Das Sarma, 2010, Phys. Rev. Lett. 105 , 187602.
- Witzel, W. M., X. Hu, and S. Das Sarma, 2007, Phys. Rev. B 76 , 035212.
- Wójcik, A., T. Ł uczak, P. Kurzy ń ski, A. Grudka, T. Gdala, and M. Bednarska, 2005, Phys. Rev. A 72 , 034303.
- Wolfowicz, G., A. M. Tyryshkin, R. E. George, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. Thewalt, S. A. Lyon, and J. J. Morton, 2013, Nat. Nanotechnol. 8 , 561.
- Wolfowicz, G., M. Urdampilleta, M. L. Thewalt, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, and J. J. Morton, 2014, Phys. Rev. Lett. 113 , 157601.
- Wu, X., et al. , 2014, Proc. Natl. Acad. Sci. U.S.A. 111 , 11938. Xiao, M., M. G. House, and H. W. Jiang, 2010, Phys. Rev. Lett. 104 , 096801.
- Xiao, M., I. Martin, E. Yablonovitch, and H. W. Jiang, 2004, Nature (London) 430 , 435.
- Xiong, J.-X., S. Guan, J.-W. Luo, and S.-S. Li, 2021, Phys. Rev. B 103 , 085309.
- Xue, X., M. Russ, N. Samkharadze, B. Undseth, A. Sammak, G. Scappucci, and L. M. Vandersypen, 2022, Nature (London) 601 , 343.
- Xue, X., T. Watson, J. Helsen, D. Ward, D. Savage, M. Lagally, S. Coppersmith, M. Eriksson, S. Wehner, and L. Vandersypen, 2019, Phys. Rev. X 9 , 021011.
- Xue, X., et al. , 2021, Nature (London) 593 , 205.
- Yang, C., et al. , 2019, Nat. Electron. 2 , 151.
- Yang, C. H., A. Rossi, R. Ruskov, N. S. Lai, F. A. Mohiyaddin, S. Lee, C. Tahan, G. Klimeck, A. Morello, and A. S. Dzurak, 2013, Nat. Commun. 4 , 2069.
- Yannouleas, C., and U. Landman, 2002, J. Phys. Condens. Matter 14 , L591.
- Yoneda, J., T. Otsuka, T. Nakajima, T. Takakura, T. Obata, M. PioroLadri` ere, H. Lu, C. J. Palmstrøm, A. C. Gossard, and S. Tarucha, 2014, Phys. Rev. Lett. 113 , 267601.
- Yoneda, J., K. Takeda, A. Noiri, T. Nakajima, S. Li, J. Kamioka, T. Kodera, and S. Tarucha, 2020, Nat. Commun. 11 , 1.
- Yoneda, J., et al. , 2018, Nat. Nanotechnol. 13 , 102.
- Yoneda, J., et al. , 2021, Nat. Commun. 12 , 4114.
- Yoshie, T., A. Scherer, J. Hendrickson, G. Khitrova, H. M. Gibbs, G. Rupper, C. Ell, O. B. Shchekin, and D. G. Deppe, 2004, Nature (London) 432 , 200.
- Young, S. M., N. T. Jacobson, and J. R. Petta, 2022, Phys. Rev. Appl. 18 , 064082.
- Yu, P. Y., and M. Cardona, 2010, Fundamentals of Semiconductors (Springer, Berlin).
- Yugova, I. A., A. Greilich, D. R. Yakovlev, A. A. Kiselev, M. Bayer, V. V. Petrov, Y. K. Dolgikh, D. Reuter, and A. D. Wieck, 2007, Phys. Rev. B 75 , 245302.
- Zajac, D. M., T. M. Hazard, X. Mi, E. Nielsen, and J. R. Petta, 2016, Phys. Rev. Appl. 6 , 054013.
- Zajac, D. M., A. J. Sigillito, M. Russ, F. Borjans, J. M. Taylor, G. Burkard, and J. R. Petta, 2018, Science 359 , 439.
- Zanardi, P., and M. Rasetti, 1997, Mod. Phys. Lett. B 11 , 1085.
- Zeuch, D., and N. E. Bonesteel, 2016, Phys. Rev. A 93 , 010303.
- Zeuch, D., and N. E. Bonesteel, 2020, Phys. Rev. B 102 , 075311.
- Zhang, L., J.-W. Luo, A. Saraiva, B. Koiller, and A. Zunger, 2013, Nat. Commun. 4 , 2396.
- Zhang, X., et al. , 2020, Phys. Rev. Lett. 124 , 257701.
- Zhao, R., et al. , 2019, Nat. Commun. 10 , 5500.
- Zheng, G., N. Samkharadze, M. L. Noordam, N. Kalhor, D. Brousse, A. Sammak, G. Scappucci, and L. M. K. Vandersypen, 2019, Nat. Nanotechnol. 14 , 742.
- Zumb¨ uhl, D. M., C. M. Marcus, M. P. Hanson, and A. C. Gossard, 2004, Phys. Rev. Lett. 93 , 256801.
- Zutic, I., J. Fabian, and S. Das Sarma, 2004, Rev. Mod. Phys. 76 , 323. Zwanenburg, F. A., A. S. Dzurak, A. Morello, M. Y. Simmons,
- L. C. L. Hollenberg, G. Klimeck, S. Rogge, S. N. Coppersmith, and M. A. Eriksson, 2013, Rev. Mod. Phys. 85 , 961.
- Zwerver, A. M. J., et al. , 2022, Nat. Electron. 5 , 184.
- Zwolak, J. P., T. McJunkin, S. S. Kalantre, J. Dodson, E. MacQuarrie, D. Savage, M. Lagally, S. Coppersmith, M. A. Eriksson, and J. M. Taylor, 2020, Phys. Rev. Appl. 13 , 034075.

Correction: The article identification number in a reference was incorrect and has been fixed. The reference now links to the intended article.