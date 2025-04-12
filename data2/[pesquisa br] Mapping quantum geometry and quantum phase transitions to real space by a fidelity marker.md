## Mapping quantum geometry and quantum phase transitions to real space by a fidelity marker

Matheus S. M. de Sousa , Antonio L. Cruz, and Wei Chen Department of Physics, PUC-Rio, 22451-900 Rio de Janeiro, Brazil

<!-- image -->

(Received 16 January 2023; accepted 10 May 2023; published 17 May 2023)

The quantum geometry in the momentum space of semiconductors and insulators, described by the quantum metric of the valence-band Bloch state, has been an intriguing issue owing to its connection to various material properties. Because the Brillouin zone is periodic, the integration of quantum metric over momentum space represents an average distance between neighboring Bloch states, which we call the fidelity number. We show that this number can further be expressed in real space as a fidelity marker, which is a local quantity that can be calculated directly from diagonalizing the lattice Hamiltonian. A linear-response theory is further introduced to generalize the fidelity number and marker to finite temperature and moreover demonstrates that they can be measured from the global and local optical absorption power against linearly polarized light. In particular, the fidelity number spectral function in two-dimensional systems can be easily measured from the opacity of the material. Based on the divergence of quantum metric, a nonlocal fidelity marker is further introduced and postulated as a universal indicator of any quantum phase transitions provided the crystalline momentum remains a good quantum number, and it may be interpreted as a Wannier state correlation function. The ubiquity of these concepts is demonstrated for a variety of topological insulators and topological phase transitions in different dimensions.

DOI: 10.1103/PhysRevB.107.205133

## I. INTRODUCTION

For materials with a band gap like insulators or semiconductors, the completely filled valence bands at zero temperature define a compact manifold parametrized by the crystalline momentum k owing to the periodicity of the Brillouin zone (BZ). Recently, the notion of quantum geometry [1] of the valence-band Bloch states | ψ ( k ) 〉 on this compact manifold emerges as an important issue that has been linked to various materials properties [2-20]. As in differential geometry and general relativity, the discussion of quantum geometry starts by equipping the manifold with a quantum metric g µν ( k ) defined from the overlap of neighboring Bloch states |〈 ψ ( k ) | ψ ( k + δ k ) 〉| = 1 -g µνδ k µ δ k ν / 2, which can also be viewed as a fidelity susceptibility defined with respect to momentum k [21-27]. Once the metric is defined, one can proceed to introduce various geometrical quantities like Ricci scalars, Riemann tensors, geodesics, etc. and discuss their physical interpretations. For instance, the geodesics have the physical interpretation as the trajectories in the momentum space along which the Bloch state | ψ ( k ) 〉 as a unit vector rotates the least in the Hilbert space.

From a differential geometrical point of view, the D -dimensional BZ manifold is special in the sense that it is a T D torus, and hence it is possible to lay a single coordinate chart k = ( k 1 , k 2 . . . kD ) for the entire manifold. It then follows that the momentum integration of the quantum metric ∫ d D k g µν ( k ) over the T D torus represents an average distance between neighboring Bloch states | ψ ( k ) 〉 and | ψ ( k + δ k ) 〉 , thereby serving as a characteristic differential geometrical property of the manifold, which has been related to the spread of Wannier functions [28-30]. In this paper, we call this momentum integration the fi- delity number, in a way completely analogous to the Chern number as a momentum integration of the Berry curvature, except the fidelity number needs not be quantized. We first use the linear-response theory recently developed for the Chern number [31] and spin Chern number [32] to generalize the fidelity number to finite temperature, which also recognizes it as the absorption power of the material against linearly polarized light, whose dependence on the frequency of the light is described by a spectral function. This indicates that the optical absorption measurements, which have been performed in semiconductors for decades, can actually be used to reveal the quantum geometrical properties of the material. Particularly for two-dimensional (2D) materials, we will elaborate that this spectral function can be easily measured from the opacity of the material [33].

We then proceed to convert the fidelity number into a real-space object that we call the fidelity marker. This marker is introduced through drawing analogy with the theory of Chern marker [34-36], which maps the Chern number of 2D materials into a real-space quantity through a projector formalism and has been recently generalized to topological materials in any dimension and symmetry class [37]. In fact, this projector formalism has been applied to the spread of Wannier functions, yielding a localization marker that can be used to distinguish metals and insulators [38]. In contrast, we will apply this projector formalism directly to the fidelity number to obtain what we call the fidelity marker, which is equivalently to a symmetrized localization marker that is experimentally measurable. Moreover, we introduce a nonlocal fidelity marker from the Fourier transform of the quantum metric, which has the physical meaning of a Wannier state correlation function, and is suggested to be a

universal indicator for quantum phase transitions owing to the divergence of quantum metric, provided the crystalline momentum k remains a good quantum number.

To demonstrate the applications of the local and nonlocal fidelity markers, we turn to generic topological insulators (TIs) and topological phase transitions (TPTs) from onedimensional (1D) to three-dimensional (3D). Our survey is motivated by a recently discovered connection between the topological order and quantum metric, namely, the module of the curvature functions that integrates to the topological invariant is equal to the determinant of the quantum metric [2,4-6,39,40], a relation that has been called the metriccurvature correspondence [41]. This correspondence holds for Dirac models in any dimension and symmetry class [42-45], as can be derived from a universal topological invariant [46]. In addition, because the curvature function generally diverges at the gap-closing high-symmetry points (HSPs) in the BZ as the material approaches a TPT [47-52], the quantum metric must diverge accordingly. As a consequence, the optical absorption of the whole lattice, i.e., the fidelity number, is predicted to show some anomaly near TPTs.

The structure of the paper is organized in the following manner. In Sec. II, we first introduce the fidelity number and marker from a projector formalism, and then use a linearresponse theory to generalize them to finite temperature and relate them to optical absorption power. A nonlocal fidelity marker is subsequently introduced from Fourier transform of the quantum metric. Section III gives concrete results for generic TIs in 1D, 2D, and 3D, with a clear demonstration of the singular behavior near TPTs. Finally, we summarize our results in Sec. IV, and give an outlook on other possible applications of the fidelity marker.

## II. MAPPING QUANTUM GEOMETRY AND QUANTUM PHASE TRANSITIONS TO REAL SPACE

## A. Local fidelity marker at zero temperature

Our aim is to elaborate that the momentum-integrated quantum metric serves as a characteristic quantum geometrical property that can be defined on lattice sites and to construct a linear-response theory to connect it to experimental measurables. Focusing on insulating materials with a band gap, we will reserve the index n for valence bands, m for conduction bands, /lscript for all the bands, and likewise for the summations { ∑ ∑ n , m , ∑ /lscript } . The 〈 r | /lscript k 〉 = /lscript k ( r ) = e -i k r · ψ/lscript k ( r ) is the periodic part of the Bloch state satisfying /lscript k ( r ) = /lscript k ( r + R ), where r and R are Bravais lattice vectors. The Bloch state of each band | /lscript k 〉 corresponds to a Wannier state | R /lscript 〉 according to

<!-- formula-not-decoded -->

where the corresponding Wannier function 〈 r R | n 〉 = Wn ( r -R ) is highly localized around the home cell R .

For a system of N -valence bands, the fully antisymmetric valence-band Bloch state at momentum k is given by

<!-- formula-not-decoded -->

Our interest is the quantum metric of this state defined from [1]

<!-- formula-not-decoded -->

which amounts to the expression [41]

<!-- formula-not-decoded -->

The key aspect of the present work is the fidelity number calculated from momentum integration of the quantum metric, which can further be expressed as overlap of Wannier states [31]:

<!-- formula-not-decoded -->

where the third line is valid due to the fact that the matrix elements vanish if k = k ′ . In deriving the above expression we have used the identity [29,30,36,49,50,53]

/negationslash

<!-- formula-not-decoded -->

/negationslash for m = n . Within the context of differential geometry, G µν in Eq. (5) measures the average distance between neighboring points on the BZ torus T D , as can be understood from the definition in Eq. (3). Note that in systems with a zero-energy flat band, the momentum-integration of quantum metric of the flat band alone has been related to the superfluid weight [54-57], which may be relevant to the superconductivity in twisted bilayer graphene [58]. In contrast, here we consider insulators or semiconductors, and the appropriate quantum metric is that of the fully antisymmetric state described by Eq. (2) that includes the contribution from all the valence bands.

Now suppose we have a tight-binding Hamiltonian H = ∑ rr ′ σσ ′ t rr ′ σσ ′ c † r σ c r ′ σ ′ , where r labels the lattice sites on a D -dimensional lattice, which has been diagonalized

and the eigenstates are found via H E | /lscript 〉 = E /lscript | E /lscript 〉 . The projectors to the filled and empty-lattice eigenstates can be constructed analogously from the projectors to the valence and conduction-band states integrated over momentum, yielding [36]

<!-- formula-not-decoded -->

Using these projectors and following the same construction for the local Chern marker [36], the fidelity number may be written as

<!-- formula-not-decoded -->

where N is the number of unit cells. The diagonal elements in the trace yield what we call the local fidelity marker

<!-- formula-not-decoded -->

where σ denotes any internal degrees of freedom within a unit cell such as spin, orbit, sublattice, etc. We should call the operator ˆ G µν ≡ [ ˆ ˆ P µ ˆ ˆ Q P ν ˆ + ˆ ˆ P Q ν ˆ ˆ µ ˆ ] P / 2 in these equations the fidelity operator. In Eq. (8), we have replaced the trace by an equivalent Tr[ ˆ ˆ P µ ˆ ˆ ] Q ν = Tr[ ˆ ˆ P µ ˆ ˆ Q P ν ˆ ], which seems to be redundant since ˆ ˆ PP = ˆ , P but it is know that this step is crucial to get the nonzero diagonal elements [36], i.e., the fidelity marker in Eq. (9), as we also confirm numerically. Interestingly, in contrast to the Chern marker that acts like the commutator of the two operators ˆ ˆ P µ ˆ ˆ Q ν and ˆ ˆ P Q ν ˆ ˆ µ [34-36], the quantum metric marker is constructed from the anticommutator of the same two operators. Finally, we remark that our fidelity marker is equivalent to the previously proposed localization marker L µν but symmetrized in the two indices µ and ν , as elaborated in Appendix. This symmetrization stems from the very definition of the quantum metric in Eq. (4) and makes our marker experimentally measurable, as we shall see in Sec. II C.

## B. Detecting quantum phase transitions by a nonlocal fidelity marker

Recent works suggest that in addition to using the diagonal element of the fidelity operator at site r to define the local topological marker, one may use the off-diagonal matrix elements corresponding to two different lattice sites r and r + R of the same operator to define a nonlocal marker [31,32,37]. Such a nonlocal marker is equivalently a Wannier state correlation function calculated from the Fourier transform of the curvature function [49-51]. Here we demonstrate that a similar formalism gives rises to a nonlocal fidelity marker that can also be interpreted as a Wannier state correlation function, as we shall see below.

Consider the Fourier transform of the quantum metric denoted by ˜ g µν ( R ), which can be expressed in terms of Wannier states by [31]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where we have used the fact that | ψ k n 〉 e i k R · projected to 〈 r | is equal to | ψ k n 〉 projected to 〈 r + R | due to the cell periodicity n ( r ) = n ( r + R ). On the other hand, if in the projector formalism we consider the ( r + R r , )th off-diagonal element of the matrix and call it the nonlocal fidelity marker G µν ( r + R r , )

then it becomes clear that the Wannier state correlation function ˜ g µν ( R ) is the clean, thermodynamic limit of the nonlocal fidelity marker lim N →∞ G µν ( r + R r , ) = ˜ g µν ( R ).

The objective of introducing this nonlocal fidelity marker is to examine whether its spatial profile can serve as a universal indicator for any kind of quantum phase transitions. This postulate is made because the quantum metric is essentially a fidelity susceptibility defined by treating momentum k as a tuning parameter. Thus as the system approaches a quantum phase transition, the quantum metric is expected to diverge at some momentum provided that momentum remains a good quantum number [21-27], and, consequently, the nonlocal fidelity marker as the Fourier transform of the quantum metric should become more long ranged. We shall use some concrete examples in the following sections to support this conjecture.

## C. Linear-response theory of finite-temperature fidelity number

We now generalize the fidelity number and marker to finite temperature using the linear-response theory developed previously for the Chern marker and spin Chern marker [31,32], and elaborate that it can be measured by optical absorption of the material. Remarkably, our formalism implies that the gauge-invariant part of the (symmetrized) spread of Wannier functions can be measured by optical absorption power,

which may help to experimentally verify the theoretical results obtained from first-principle calculations [28-30]. We start from a quantum metric spectral function derived from the response of the system under an oscillating electric field [59],

<!-- formula-not-decoded -->

The superscript d stands for 'dressed' since the formalism is valid at finite temperature (and potentially including many-body interactions as well, although they will not be addressed here).

Experimentally, g d µν ( ω ) in Eq. (12) is related to the optical response at momentum k . This can be seen by considering the current operator in momentum space ˆ j µ = e ∂µ H , where ∂µ ≡ ∂/∂ k µ and H = H ( k ) is the momentum space singleparticle Hamiltonian, and we will assume a D -dimensional cubic lattice of unit-cell volume a D . The usual linear-response theory for noninteracting system gives the finite-temperature longitudinal optical conductivity at momentum k at frequency of the light ω by [60]

<!-- formula-not-decoded -->

which can be used to extract the diagonal components of the quantum metric spectral function g d µµ ( k , ω ). Here | /lscript 〉 ≡ | /lscript k 〉 is the periodic part of the Block state, and the index /lscript enumerates both the valence- and conduction-band states, since at finite temperature both of them contribute to the conductivity. The f ( ε k /lscript ) is the Fermi distribution of the eigenenergy ε k /lscript . Moreover, because the optical conductivity corresponds to the optical absorption process, δ ω ( + ε k /lscript / ł h -ε k /lscript ′ / ł ) h with ω &gt; 0 ensures that ε k /lscript &lt; ε /lscript k ′ , as denoted by the summation ∑ /lscript&lt;/lscript ′ . Many previous works [28,59,61-63] have already pointed out that the frequency integration of this spectral function gives the quantum metric g d µµ ( k ) = ∫ ω 0 d ω g d µµ ( k , ω ) that in the zero-temperature limit lim T → 0 g d µν ( k ) = g µν ( k ) recovers the expression in Eq. (4). In contrast, we will focus on the spectral function g d µµ ( k , ω ) itself for the purpose that will become clear below.

The conductivity of the whole sample, which is also what is measured in real space, is given by the momentum integration of the above quantity:

<!-- formula-not-decoded -->

which defines what we call the fidelity number spectral function G d µµ ( ω ). On the other hand, in a D -dimension material, if we denote the polarized oscillating field by

E µ ( ω, t ) = E 0 cos ω t and the current that it induces by j µ ( ω, t ) = σµµ ( ω ) E 0 cos ω t , where E 0 is the strength of the field, then the optical absorption power per unit cell at frequency ω is

<!-- formula-not-decoded -->

which can be used to extract the spectral function G d µµ ( ω ), where 〈 . . . 〉 t denotes the time average. Particularly in 2D systems, the incident power of the light per unit area is Wi = c ε 0 E 2 0 / 2, and hence the opacity of the 2D system as the incident light has frequency ω and polarization µ is [33]

<!-- formula-not-decoded -->

where α = e 2 / 4 πε 0 ł hc is the fine-structure constant. Thus the fidelity number spectral function can be simply extracted experimentally from the opacity by

<!-- formula-not-decoded -->

In other words, it is simply the opacity at ω and polarization µ measured in units of πα ≈ 2 3% and then divided by 4 . πω . We expect that this simple protocol should be broadly applicable to 2D systems, as has been elaborated recently for 2D Dirac materials like graphene and silicene [64].

To extract the off-diagonal components of the fidelity number spectral function, such as G d xy ( ω ), one may consider linearly polarized light with a phase different [8] E ± = E 0 (ˆ x ± ˆ ), y and the current operators ˆ j ± = ˆ j x ± ˆ j y and conductivities σ ± ( k , ω ) defined accordingly. Using the offdiagonal component g d xy ( k , ω ) in Eq. (12), the same analysis leads to the conclusion that the difference of optical conductivity between the two polarizations gives

<!-- formula-not-decoded -->

and after a momentum integration, the difference in absorption power gives

<!-- formula-not-decoded -->

which may be used to extract the off-diagonal component G d xy ( ω ). For 2D systems, the incident power of the two polarizations we considered is Wi ± = c ε 0 E 2 0 | ˆ x ± | ˆ y 2 / 2 = c ε 0 E 2 0 , and hence

<!-- formula-not-decoded -->

indicating that one may use the difference in opacity under the two polarizations to extract G d xy ( ω ).

## D. Finite-temperature fidelity marker

After the spectral function as a function of frequency ω is obtained, the dressed fidelity number can further be obtained

via a frequency integration, which can be expressed in terms of eigenstates | E /lscript 〉 of lattice models using the procedure outlined in Sec. II A, rendering

<!-- formula-not-decoded -->

Here | ψ/lscript k 〉 is the full Bloch state and | /lscript 〉 ≡ | /lscript k 〉 is the periodic part of the Block state satisfying 〈 r | ψ/lscript k 〉 = e i k r · 〈 r | /lscript 〉 . The fidelity number is then expressed to the real-space version using the projectors

<!-- formula-not-decoded -->

where | E /lscript 〉 is a lattice eigenstate obtained from diagonalizing the lattice Hamiltonian H E | /lscript 〉 = E /lscript | E /lscript 〉 , and we denote its projector by S /lscript = | E /lscript 〉〈 E /lscript | . At zero temperature f ( E /lscript ) = θ ( -E /lscript ), it is evident that the dressed fidelity number recovers the zero-temperature one lim T → 0 G d µν = G µν , as can be easily seen by comparing Eqs. (21) and (8).

Our goal now is to construct a finite-temperature fidelity marker that spatially sums to the fidelity number G d µµ = ∑ r G d µµ ( r ) / N in Eq. (21). To achieve this, the issue now is that according to what discussed after Eq. (9), one has to add an extra projector ˆ P to the last line of Eq. (21) in order to get the correct fidelity marker. However, at finite temperature, thermal broadening renders the notion of filled and empty states rather ambiguous, let alone their projectors ˆ and P ˆ Q in Eq. (7). To incorporate this extra projector at finite temperature, we propose to first calculate the matrix

<!-- formula-not-decoded -->

where f /lscript/lscript ′ ≡ f ( E /lscript ) -f ( E /lscript ′ ), and then define the fidelity marker by

<!-- formula-not-decoded -->

which spatially sums to the fidelity number G d µν = ∑ r G d µν ( r ) / N because ∑ r | r 〉〈 r | = I and S /lscript ′ S /lscript ′ = δ /lscript ′ /lscript ′ S /lscript ′ , and moreover recovers the zero-temperature one lim T → 0 G d µν ( r ) = G µν ( r ) in Eq. (9), and therefore serves our purpose. Likewise, the nonlocal fidelity marker can also be generalized to finite temperature as the off-diagonal element of this operator

<!-- formula-not-decoded -->

which represents the Fourier transform of the finitetemperature quantum metric g d µν = ∫ ∞ 0 d ω g d µν ( ω ) [defined in Eq. (13)] that may be used to examine the finite-temperature behavior near quantum phase transitions.

It is also convenient to introduce a fidelity marker spectral function from the frequency-dependent matrix

<!-- formula-not-decoded -->

where the δ function is simulated by a Lorentzian δ ( x ) = η/π ( x 2 + η 2 ) in practice, so the interpretation of its square root is straightforward. The fidelity marker spectral function is then defined by

<!-- formula-not-decoded -->

which spatially sums to the fidelity number spectral function G d µν ( ω ) = ∑ r G d µν ( r , ω ) / N in Eq. (14). Analogous to Eq. (15), this spectral function corresponds to the local optical absorption power of the unit cell at r :

<!-- formula-not-decoded -->

and likewise the off-diagonal component G d xy ( r , ω ) corresponds to the absorption power difference in Eq. (19) defined locally at r . Given this connection to the absorption power, we anticipate that thermal probes that can detect the heating caused by the light down to atomic scale, such as scanning thermal microscopy [65-68], may be able to detect the local absorption power Wa ( r , ω ) and subsequently extract G d µµ ( r , ω ).

FIG. 1. Analytical results for homogeneous linear Dirac models of TIs in 1D (top row), 2D (middle row), and 3D (bottom row), where in panels (a), (e), and (i) we show the momentum profile of the quantum metric [in panel (i) we plot the momentum surfaces at two constant values), in panels (b), (f), (j) the fidelity number or marker spectral function, in panels (c), (g), (k) the fidelity number or marker near TPTs at zero (solid lines) and a finite (dotted lines) temperatures, and in panels (d), (h), (l) the spatial profile of the nonlocal fidelity marker for a parameter close to (blue) and far away from (yellow) the critical point.

<!-- image -->

## III. APPLICATIONS TO TOPOLOGICAL INSULATORS AND TOPOLOGICAL PHASE TRANSITIONS

## A. Continuous models of topological insulators

As a concrete example, we investigate the generic D -dimensional TIs in any symmetry class described by N × N Dirac models H = ∑ D i = 0 di /Gamma1 i , where /Gamma1 i are the Dirac matrices, and di characterizes the momentum dependence of the Hamiltonian [42,43,45]. In this case, it has been proved that the fully antisymmetric valence band Bloch state of the TI at momentum k , described by Eq. (2), gives the quantum metric [41]

<!-- formula-not-decoded -->

Denoting d = ( ∑ i d i 2 ) 1 2 / , the model has N / 2-fold degenerate valence-band states of energy ε n = -d and conduction-band states of energy ε m = d . The diagonal elements of fidelity number of this model have been considered in a previous work under the name of Marzari-Vanderbilt cumulant [69]. In contrast, we emphasize the frequency- and temperaturedependence of the spectral function to draw relevance to the optical absorption power. Because the model is homogeneous, the fidelity number spectral function in Eq. (14) and fidelity marker spectral function in Eq. (27) are the same

<!-- formula-not-decoded -->

We first address the analytical results of linear Dirac models and then investigate more realistic lattice models by numerical calculations.

/negationslash

Analytical expression of G d µν ( ω ) can be given for linear Dirac models parametrized by d 0 = M and di = 0 = v ki , where v is the Fermi velocity. These models well describe the critical behavior of TIs and TSCs near TPTs. Using Eq. (29), the quantum metric of these models is [69]

<!-- formula-not-decoded -->

We will focus on the diagonal component g µµ , whose momentum profile is shown in Figs. 1(a), 1(e), and 1(i) for 1D, 2D, and 3D, respectively. In any dimension, the g µµ near the gap-closing point k = 0 has a Lorentzian shape:

<!-- formula-not-decoded -->

whose height diverges like g µµ ( 0 ) ∼ 1 / M 2 and width vanishes like 1 /ξ ∼| M | as the system approaches the TPT M → 0, manifesting the divergence behavior anticipated at the end of Sec. II B, with a critical exponent ν = 1. The integration over momentum gives the diagonal components of the fidelity marker spectral function:

<!-- formula-not-decoded -->

where /Omega1 D = 2 π D 2 //Gamma1 ( D 2 ) for D &gt; 1, and /Omega1 1 = 1. Explicitly from 1D to 3D, it has the expressions

<!-- formula-not-decoded -->

/negationslash where Z ( ω ) ≡ [ f ( -ł h ω 2 ) -f ( ł h ω 2 )], and the off-diagonal components µ = ν vanish after the angular integration. The frequency dependence of G d µµ ( ω ) at zero temperature is shown in Figs. 1(b), 1(f), and 1(j) for the 1D, 2D, and 3D cases. The spectral function is practically zero at frequency lower than the band gap, as expected. Moreover, the frequency dependence above the band gap highly depends on the dimension, which gives a concrete prediction to the low-frequency behavior of the optical absorption in Dirac models.

Particularly at zero temperature f ( -ł h ω 2 ) -f ( ł h ω 2 ) = 1, after performing a frequency integration G d µµ = ∫ ω cut 2 | M | / ł h d /Omega1, G d µµ ( ω ) of the spectral function from the band gap 2 | M | / ł h to some cutoff frequency ω cut that represents the bandwidth, we obtain

<!-- formula-not-decoded -->

 in agreement with the previous calculation of Marzari-Vanderbilt cumulant [69]. In short, the fidelity marker diverges in 1D and 2D as the system approaches the critical point M → 0 of a TPT, while saturates to a constant in 3D, as indicated in Figs. 1(c), 1(g), and 1(k), which also show that the effect of finite temperature is to smear out the anomaly at the critical point. Finally, in Figs. 1(d), 1(h), and 1(l) we show the nonlocal fidelity marker obtained from numerically performing a Fourier transform on the quantum metric. In any spatial dimension, one sees that the decay length of the nonlocal marker increases as the system approaches the critical point Mc = 0, consistent with the diverging quantum metric discussed after Eq. (32). Note that, for the Lorentzian shape in Eq. (32) with correlation length ξ = √ 2 | v / M | , its Fourier transform in 1D at large R gives a simple exponential decay ˜ g µµ ( R ) ∝ e -R /ξ , but in 3D the Fourier transform ˜ g µµ ( R ) ∝ e -R /ξ / R has an extra factor of 1 / R , making the nonlocal marker in Fig. 1(l) look more short-ranged in comparison with the exponential decay in Fig. 1(d).

## B. Lattice models of topological insulators

In this section, we use prototype lattice models of TIs in 1D, 2D, and 3D to demonstrate the real-space profiles of the local and nonlocal fidelity markers. We will adopt the recipe in Sec. II to directly calculate the fidelity marker on every lattice site by diagonalizing the lattice Hamiltonian in the periodic boundary condition (PBC). Note that although we only calculate the marker for some specific models, one should keep in mind that the critical behavior of the marker

FIG. 2. Numerical results of 1D SSH model, where we investigate (a) the fidelity marker G xx ( r ) at far from δ t = -0 2 and close . to δ t = -0 1 (in . units of the uniform hopping t = 1) the critical point, and at zero and finite temperatures, and (b) the nonlocal fidelity marker at far from and close to the critical point.

<!-- image -->

for all the TIs in the same dimension should be the same according to Eq. (35).

## 1. 1D Su-Schrieffer-Heeger model

A prototype example in 1D is the spinless Su-ShriefferHeeger (SSH) model [70] described by the Hamiltonian

<!-- formula-not-decoded -->

where cAi and cBi are fermion annihilation operators on the A and B sublattices in the unit cell at i , and δ t is the difference between the hopping on the even and odd bonds that controls the topological order. The numerical result for the fidelity marker is shown in Fig. 2(a) for a lattice of 100 unit cells. Deep inside the bulk, the marker remains a constant value that agrees with the momentum-integration of quantum metric in Eq. (5), and the value increases as the system approaches the critical point δ t → 0, in agreement with Eq. (35) and that presented in Fig. 1(c) for the low-energy Dirac model. Near the boundary sites, however, the marker starts to deviate from the constant value even if PBCs are imposed, a problem known for this type of projector formalism since the position operator ˆ in Eq. (9) does not respect the translational invarix ance [36]. In Fig. 2(b), we show that the nonlocal marker decays with distance R , with a decay length that grows as the system approaches the critical point δ t → 0, in agreement with that discussed at the end of Sec. II B. The maximal value of the nonlocal marker at R = 0 recovers the local marker [setting R = 0 in Eq. (11) recovers Eq. (9)], i.e., the maxima of Fig. 2(b) are equal to the flat values in Fig. 2(a). In addition, the nonlocal marker also oscillates with a wavelength of two lattice constants, owing to the fact that the nonlocal marker is the Fourier transform of the quantum metric that peaks at k = π in this model.

## 2. 2D Chern insulator

We proceed to use the lattice model of Chern insulator as a concrete example for 2D TIs, which is described by the spinless basis ( c k s , c k p ) T and the momentum space Hamiltonian [71,72]

<!-- formula-not-decoded -->

FIG. 3. Numerical results of the 2D Chern insulator, where we show (a) the fidelity marker G xx ( r ) along the ˆ x direction at far from ( M = -2, blue lines) and close to ( M = -1, black lines) the critical point Mc = 0, and at zero and finite temperatures, and (b) the spatial profile of the nonlocal fidelity marker.

<!-- image -->

The corresponding lattice model in real space is [73]

<!-- formula-not-decoded -->

where we set the parameters to be t = A / 2 = 1 and t ′ = B = 1, σ = { s , p } are the orbitals, and δ = { a , b } are the lattice constants. We will focus on the Mc = 0 critical point where the bulk gap closes at k = (0 , 0), since the critical behavior near other critical points are similar, and plot the marker along the (1,0) crystalline direction. From Fig. 3(a) one sees that the marker saturates to a constant value deep inside the bulk that agrees with the momentum integration in Eq. (5), and the value slightly decreases as temperature increases owing to the thermal broadening. Interestingly, the fidelity marker at M = -2 is higher than that at M = -1, even though the latter is closer to the critical point Mc = 0, which seems to contradict the continuous model in Sec. III A. We find that this is because the real lattice models can exhibit a more sophisticate momentum profile of the quantum metric beyond the Lorentzian shape of Eq. (32), hence its momentum integration may not monotonically increase as M → Mc . The divergence of fidelity number in this model only takes place roughly in the range -0 2 . &lt; M &lt; 0, which requires a much larger lattice to capture. Nevertheless, the nonlocal marker in Fig. 3(b) simulated on a 14 × 14 lattice already shows a clear decay with distance R , with a decay length that increases as M → 0, indicating that the nonlocal marker serves as a faithful indicator for TPTs in this model even at such a small lattice size.

## 3. 3D time-reversal-symmetric TIs

For 3D TIs, we consider a class AII model that preserves time-reversal symmetry and is relevant to materials such as Bi2Se3 and Bi2Te3, described by the /Gamma1 matrices and the

FIG. 4. Numerical results of the 3D time-reversal symmetric TIs, where we show (a) the fidelity marker G xx ( r ) along the ˆ direction at x far from M = -2 and close to M = -1 the critical point Mc = 0 at zero temperature. (b) The spatial profile of the nonlocal fidelity marker G xx ( r + R r , ) along the same direction.

<!-- image -->

spinor [74,75],

<!-- formula-not-decoded -->

where we use s and p to label the P 1 + -and P 2 -+ orbitals in real materials. Keeping only lowest-order terms, the low-energy Hamiltonian is given by

<!-- formula-not-decoded -->

The regularization on the whole BZ and a Fourier transform to real-space yields the lattice model [73]

<!-- formula-not-decoded -->

where ˜ M = M + 2 M 1 + 4 M 2 , t ‖ = A 0 / 2, t ⊥ = B 0 / 2, { I , I } = { p s , } , σ = {↑ ↓} , is the spin index, and δ = { a , b c , } denotes the lattice constants. We use the parameters µ = 0 5 and . t ‖ = t ⊥ = M 1 = M 2 = 1, and two values of M = -2 and M = -1 that are far from and close to the critical point Mc = 0, respectively.

Figure 4(a) shows the numerical results of G xx ( r ) simulated on a Lx × Ly × Lz = 20 × × 8 8 lattice plotted along the elongated ˆ x direction. Owing to the significant computational cost at finite temperature, we focus on the zero-temperature limit of this model. The results in Fig. 4(a) indicates that deep

inside the bulk, G xx ( r ) saturates to a constant value that agrees with momentum-integration of the quantum metric gxx ( k ) in Eq. (5), and again the value does not monotonically increase at the system approaches the critical point M → 0 owing to the complicated momentum profile of gxx ( k ) in the lattice model. Nevertheless, the nonlocal marker G xx ( r + R r , ) shown in Fig. 4(b) becomes more long-ranged as M → 0, and hence the nonlocal marker still serves as a faithful index to identify the TPTs in this lattice model.

## IV. CONCLUSIONS

In summary, we investigate the fidelity number G µν defined from momentum integration of the quantum metric g µν of the fully antisymmetric valence-band state, which quantifies the average distance between neighboring valence-band states in the BZ torus. Using a linear-response theory, we generalize the fidelity number to finite temperature denoted by G d µν and suggest that they correspond to the optical absorption power against linearly polarized light, whose frequency dependence is described by a spectral function G d µν ( ω ). Especially for 2D systems, this spectral function can be simply extracted from the frequency dependence of the opacity measured in units of fine-structure constant. We then show that the fidelity number can be mapped to real space as a fidelity marker G d µν ( r ) defined locally on every unit cell, whose spectral function G d µν ( r , ω ) corresponds to the local heating rate that may be measured by atomic scale thermal probes, offering a possibility to measure the gauge-invariant part of the spread of Wannier functions. Moreover, in contrast to the diagonal elements of the fidelity operator that give the local fidelity marker, the off-diagonal elements of the same operator yield a nonlocal fidelity marker G µν ( r + R r , ) that is equivalent to the Fourier transform of the quantum metric, and represents an overlap between Wannier states. The relation between various quantities introduced in the present work is summarized in Fig. 5.

Particularly for TIs, the quantum metric g µν diverges at the gap-closing HSPs at the system approaches TPTs, rendering a fidelity number G d µν that diverges at the critical point in 1D and 2D, while approaching a constant in 3D. The predicted fidelity number spectral function G d µν ( ω ) also strongly depends on the dimension of the system and is readily measurable in realistic TIs by optical absorption. The nonlocal marker G µν ( r + R r , ) is found to decay with a correlation length ξ that diverges near TPTs, with a critical exponent ν = 1 that is universal for linear Dirac models in any dimension and symmetry class. We then use prototype lattice models of TIs in 1D, 2D, and 3D to investigate the behavior these markers near critical points in realistic materials, suggesting the ubiquity of these markers in characterizing the quantum geometry and quantum criticality in topological materials.

These properties of fidelity number and marker immediately imply a great number of applications. First, because the marker is locally defined, it may be used to explore the influence of real-space inhomogeneity, such as impurities and grain boundaries, on the quantum geometry of the material. Second, because the nonlocal fidelity markers is equivalently the Fourier transform of the quantum metric, we postulate that it can detect any quantum phase transitions provided

FIG. 5. Schematics of the linear-response theory, measurement protocols, and Wannier function interpretation of various quantities related to the fidelity number and marker. The terminology is given by the blue text, and the orange text indicates the corresponding physical quantity in the proposed optical absorption experiment using linearly polarized light shown in the two figures, and the black arrows indicate how to derive one quantity from another. We use the abbreviations absor. = absorption, spec. = spectral, and fn. = function.

<!-- image -->

momentum remains a good quantum number. This conjecture is made because quantum metric g µν ( k ) is essentially the fidelity susceptibility of the valence-band state defined with respect to momentum k [21-27], which is expected to diverge at quantum phase transitions, causing the decay length of the nonlocal marker to diverge accordingly. Even if the transition is driven by weak interactions, given the recent generalization of quantum metric to interacting systems [59], it may still be possible to define the fidelity marker perturbatively in terms of Green's function and investigate its critical behavior near the transition. All of these intriguing questions await further investigations to clarify, which may help to shed some new insight on quantum geometry and quantum phase transitions.

## ACKNOWLEDGMENTS

The authors acknowledge stimulating discussions with A. Marrazzo and J. Mitscherling, which help us to clarify various aspects about quantum metric and the Wannier state interpretations, as well as the financial support from the productivity in research fellowship from CNPq.

## APPENDIX: COMPARISON WITH THE LOCALIZATION MARKER

We now make a detailed comparison between our fidelity marker and the localization marker proposed in Ref. [38]. Normalizing the spatial sum of localization marker L µν to the same unit as the fidelity number G µν and use the notation in the present work, the expression is

<!-- formula-not-decoded -->

/negationslash where 〈 . . . 〉 denotes the average over Wannier states, which defines the localization marker L µν ( r ). If we call ˆ L µν ≡ ˆ ˆ P µ ˆ ˆ Q P ν ˆ the operator that renders the localization marker, then a direct comparison with our fidelity operator ˆ G µν ≡ [ ˆ ˆ P µ ˆ ˆ Q P ν ˆ + ˆ ˆ P Q ν ˆ ˆ µ ˆ ] P / 2 in Eq. (8) immediately suggests that the diagonal components of them are equal ˆ G µµ = ˆ L µµ , and the off-diagonal components are related by ˆ G µν µ | = ν = ( ˆ L µν + ˆ L νµ ) / 2. As a result, the diagonal components of the fidelity marker is exactly equal to that of the localization marker. Moreover, shall one define a nonlocal localization marker by L µν ( r + R r , ) = 〈 r + R | ˆ L µν | r 〉 , then it is clear that the diagonal components of it will be equal to our nonlocal fidelity

- [1] J. P. Provost and G. Vallee, Commun. Math. Phys. 76 , 289 (1980).
- [2] Y.-Q. Ma, S.-J. Gu, S. Chen, H. Fan, and W.-M. Liu, Europhys. Lett. 103 , 10008 (2013).
- [3] M. Kolodrubetz, V. Gritsev, and A. Polkovnikov, Phys. Rev. B 88 , 064304 (2013).
- [4] Y.-Q. Ma, Phys. Rev. E 90 , 042133 (2014).
- [5] L. Yang, Y.-Q. Ma, and X.-G. Li, Phys. B (Amsterdam, Neth.) 456 , 359 (2015).
- [6] F. Piéchon, A. Raoux, J.-N. Fuchs, and G. Montambaux, Phys. Rev. B 94 , 134423 (2016).
- [7] M. Kolodrubetz, D. Sels, P. Mehta, and A. Polkovnikov, Phys. Rep. 697 , 1 (2017).
- [8] T. Ozawa and N. Goldman, Phys. Rev. B 97 , 201117(R) (2018).
- [9] G. Palumbo and N. Goldman, Phys. Rev. Lett. 121 , 170401 (2018).
- [10] G. Palumbo, Eur. Phys. J. Plus 133 , 23 (2018).
- [11] M. F. Lapa and T. L. Hughes, Phys. Rev. B 99 , 121111(R) (2019).
- [12] M. Yu, P. Yang, M. Gong, Q. Cao, Q. Lu, H. Liu, S. Zhang, M. B. Plenio, F. Jelezko, T. Ozawa, N. Goldman, and J. Cai, Natl. Sci. Rev. 7 , 254 (2020).
- [13] M. Chen, C. Li, G. Palumbo, Y.-Q. Zhu, N. Goldman, and P. Cappellaro, Science 375 , 1017 (2022).
- [14] Y.-Q. Ma, arXiv:2001.05946.
- [15] G. Salerno, N. Goldman, and G. Palumbo, Phys. Rev. Res. 2 , 013224 (2020).
- [16] Y.-P. Lin and W.-H. Hsiao, Phys. Rev. B 103 , L081103 (2021).
- [17] J. Mitscherling, Phys. Rev. B 102 , 165151 (2020).
- [18] J. Mitscherling and T. Holder, Phys. Rev. B 105 , 085154 (2022).

marker too. However, the off-diagonal components are not the same, since our fidelity marker is symmetrized. In summary,

/negationslash

/negationslash

<!-- formula-not-decoded -->

/negationslash

We emphasize that our definition of the marker stems from the consideration of experimental measurability, especially its link to the optical absorption power in 3D and opacity in 2D, as explained in Sec. II C. In particular, the off-diagonal element G µν µ | = ν defined in our way corresponds to the difference in absorption power or opacity of two specific polarizations, as elaborated in Eqs. (19) and (20), which is readily measurable. Moreover, the symmetrized form of ˆ G µν is also a natural consequence of the valence state quantum metric in Eq. (4) that is symmetric in the two indices µ and ν . Finally, through comparing with these previous works, one sees that our experimental proposal can directly measure the so-called gauge-invariant part of the spread of Wannier functions given by the first line of Eq. (A1) and usually denoted by /Omega1 I [28,29], which may help to compare the first-principle calculation with experimental results.

- [19] J. Ahn, G.-Y. Guo, and N. Nagaosa, Phys. Rev. X 10 , 041041 (2020).
- [20] J. Ahn, G.-Y. Guo, N. Nagaosa, and A. Vishwanath, Nat. Phys. 18 , 290 (2022).
- [21] W.-L. You, Y.-W. Li, and S.-J. Gu, Phys. Rev. E 76 , 022101 (2007).
- [22] P. Zanardi, P. Giorda, and M. Cozzini, Phys. Rev. Lett. 99 , 100603 (2007).
- [23] S.-J. Gu, H.-M. Kwok, W.-Q. Ning, and H.-Q. Lin, Phys. Rev. B 77 , 245109 (2008).
- [24] S. Yang, S.-J. Gu, C.-P. Sun, and H.-Q. Lin, Phys. Rev. A 78 , 012304 (2008).
- [25] A. F. Albuquerque, F. Alet, C. Sire, and S. Capponi, Phys. Rev. B 81 , 064418 (2010).
- [26] S.-J. Gu, Int. J. Mod. Phys. B 24 , 4371 (2010).
- [27] A. Carollo, D. Valenti, and B. Spagnolo, Phys. Rep. 838 , 1 (2020).
- [28] I. Souza, T. Wilkens, and R. M. Martin, Phys. Rev. B 62 , 1666 (2000).
- [29] N. Marzari and D. Vanderbilt, Phys. Rev. B 56 , 12847 (1997).
- [30] N. Marzari, A. A. Mostofi, J. R. Yates, I. Souza, and D. Vanderbilt, Rev. Mod. Phys. 84 , 1419 (2012).
- [31] P. Molignini, B. Lapierre, R. Chitra, and W. Chen, arXiv:2207.00016.
- [32] W. Chen, J. Phys.: Condens. Matter 35 , 155601 (2023).
- [33] R. R. Nair, P. Blake, A. N. Grigorenko, K. S. Novoselov, T. J. Booth, T. Stauber, N. M. R. Peres, and A. K. Geim, Science 320 , 1308 (2008).
- [34] E. Prodan, T. L. Hughes, and B. A. Bernevig, Phys. Rev. Lett. 105 , 115501 (2010).

- [35] E. Prodan, J. Phys. A: Math. Theor. 44 , 113001 (2011).
- [36] R. Bianco and R. Resta, Phys. Rev. B 84 , 241106(R) (2011).
- [37] W. Chen, Phys. Rev. B 107 , 045111 (2023).
- [38] A. Marrazzo and R. Resta, Phys. Rev. Lett. 122 , 166602 (2019).
- [39] S. Panahiyan, W. Chen, and S. Fritzsche, Phys. Rev. B 102 , 134111 (2020).
- [40] B. Mera, A. Zhang, and N. Goldman, SciPost Phys. 12 , 018 (2022).
- [41] G. von Gersdorff and W. Chen, Phys. Rev. B 104 , 195133 (2021).
- [42] A. P. Schnyder, S. Ryu, A. Furusaki, and A. W. W. Ludwig, Phys. Rev. B 78 , 195125 (2008).
- [43] S. Ryu, A. P. Schnyder, A. Furusaki, and A. W. W. Ludwig, New J. Phys. 12 , 065010 (2010).
- [44] A. Kitaev, AIP Conf. Proc. 1134 , 22 (2009).
- [45] C.-K. Chiu, J. C. Y. Teo, A. P. Schnyder, and S. Ryu, Rev. Mod. Phys. 88 , 035005 (2016).
- [46] G. von Gersdorff, S. Panahiyan, and W. Chen, Phys. Rev. B 103 , 245146 (2021).
- [47] W. Chen, J. Phys.: Condens. Matter 28 , 055601 (2016).
- [48] W. Chen, M. Sigrist, and A. P. Schnyder, J. Phys.: Condens. Matter 28 , 365501 (2016).
- [49] W. Chen, M. Legner, A. Rüegg, and M. Sigrist, Phys. Rev. B 95 , 075116 (2017).
- [50] W. Chen and M. Sigrist, Advanced Topological Insulators (Wiley-Scrivener, Hoboken, NJ, 2019), Chap. 7.
- [51] W. Chen and A. P. Schnyder, New J. Phys. 21 , 073003 (2019).
- [52] P. Molignini, W. Chen, and R. Chitra, Europhys. Lett. 128 , 36001 (2019).
- [53] M. Gradhand, D. V. Fedorov, F. Pientka, P. Zahn, I. Mertig, and B. L. Györffy, J. Phys.: Condens. Matter 24 , 213202 (2012).
- [54] S. Peotta and P. Törmä, Nat. Commun. 6 , 8944 (2015).
- [55] A. Julku, S. Peotta, T. I. Vanhala, D.-H. Kim, and P. Törmä, Phys. Rev. Lett. 117 , 045303 (2016).
- [56] E. Rossi, Curr. Opin. Solid State Mater. Sci. 25 , 100952 (2021).
- [57] P. Törmä, S. Peotta, and B. A. Bernevig, Nat. Rev. Phys. 4 , 528 (2022).
- [58] F. Xie, Z. Song, B. Lian, and B. A. Bernevig, Phys. Rev. Lett. 124 , 167002 (2020).
- [59] W. Chen and G. von Gersdorff, SciPost Phys. Core 5 , 040 (2022).
- [60] G. D. Mahan, Many-Particle Physics (Springer, New York, 2000).
- [61] R. Resta, J. Phys.: Condens. Matter 14 , R625 (2002).
- [62] R. Resta, Eur. Phys. J. B 79 , 121 (2011).
- [63] T. Kashihara, Y. Michishita, and R. Peters, Phys. Rev. B 107 , 125116 (2023).
- [64] M. S. M. de Sousa, A. L. Cruz, and W. Chen, arXiv:2303.14549.
- [65] A. Majumdar, Annu. Rev. Mater. Sci. 29 , 505 (1999).
- [66] A. Kittel, W. Müller-Hirsch, J. Parisi, S.-A. Biehs, D. Reddig, and M. Holthaus, Phys. Rev. Lett. 95 , 224301 (2005).
- [67] S. Gomès, A. Assy, and P.-O. Chapuis, Phys. Status Solidi A 212 , 477 (2015).
- [68] Y. Zhang, W. Zhu, F. Hui, M. Lanza, T. Borca-Tasciuc, and M. Muñoz Rojo, Adv. Funct. Mater. 30 , 1900892 (2020).
- [69] S. Matsuura and S. Ryu, Phys. Rev. B 82 , 245113 (2010).
- [70] W. P. Su, J. R. Schrieffer, and A. J. Heeger, Phys. Rev. Lett. 42 , 1698 (1979).
- [71] X.-L. Qi and S.-C. Zhang, Rev. Mod. Phys. 83 , 1057 (2011).
- [72] B. A. Bernevig and T. L. Hughes, Topological Insulators and Topological Superconductors (Princeton University Press, Princeton, New Jersey, 2013).
- [73] W. Chen, Phys. Rev. B 101 , 195120 (2020).
- [74] H. Zhang, C.-X. Liu, X.-L. Qi, X. Dai, Z. Fang, and S.-C. Zhang, Nat. Phys. 5 , 438 (2009).
- [75] C.-X. Liu, X.-L. Qi, H. J. Zhang, X. Dai, Z. Fang, and S.-C. Zhang, Phys. Rev. B 82 , 045122 (2010).