<!-- image -->

<!-- image -->

Article

## Self-Vibration of a Liquid Crystal Elastomer Fiber-Cantilever System under Steady Illumination

Kai Li , Yufeng Liu, Yuntong Dai and Yong Yu *

School of Civil Engineering, Anhui Jianzhu University, Hefei 230601, China

- * Correspondence: yyu@ahjzu.edu.cn

Abstract: A new type of self-oscillating system has been developed with the potential to expand its applications in fields such as biomedical engineering, advanced robotics, rescue operations, and military industries. This system is capable of sustaining its own motion by absorbing energy from the stable external environment without the need for an additional controller. The existing self-sustained oscillatory systems are relatively complex in structure and difficult to fabricate and control, thus limited in their implementation in practical and complex scenarios. In this paper, we creatively propose a novel light-powered liquid crystal elastomer (LCE) fiber-cantilever system that can perform self-sustained oscillation under steady illumination. Considering the well-established LCE dynamic model, beam theory, and deflection formula, the control equations for the self-oscillating system are derived to theoretically study the dynamics of self-vibration. The LCE fiber-cantilever system under steady illumination is found to exhibit two motion regimes, namely, the static and self-vibration regimes. The positive work done by the tension of the light-powered LCE fiber provides some compensation against the structural resistance from cantilever and the air damping. In addition, the influences of system parameters on self-vibration amplitude and frequency are also studied. The newly constructed light-powered LCE fiber-cantilever system in this paper has a simple structure, easy assembly/disassembly, easy preparation, and strong expandability as a one-dimensional fiberbased system. It is expected to meet the application requirements of practical complex scenarios and has important application value in fields such as autonomous robots, energy harvesters, autonomous separators, sensors, mechanical logic devices, and biomimetic design.

Keywords: self-vibration; liquid crystal elastomer; light-powered; fiber-cantilever

## 1. Introduction

Self-excited oscillation refers to a recurring oscillatory phenomenon that arises from external steady excitations. Conventional mechanical oscillation is usually subjected to periodic external stimulus that generates periodic forced motion in time and space. In contrast to forced oscillation, self-oscillation can actively adjust its own motion, provide feedback in response to steady external stimulus, and obtain regular energy to maintain its periodic motion [1-4]. Self-oscillation can not only obtain energy directly and independently from the external environment to maintain its own motion mode, but also its vibration frequency and amplitude depend only on the inherent parameters of the structure. It does not require other complex controllers to achieve periodic oscillation [5,6], so from the perspective of dynamics theory, self-oscillation is of great significance for understanding new behaviors such as bifurcation, chaos, synchronization, and other non-equilibrium dynamics in nonlinear systems. It is a typical non-equilibrium dynamical process in nonlinear systems [7]. Self-oscillating systems have broad application prospects and revolutionary impact on autonomous robots [8-12], energy harvesters [13,14], independent separators, sensors [15], mechanical logic devices [16], and biomimetic design.

In recent years, active materials such as hydrogels [17,18], dielectric elastomers [19], ion gels [20], and thermally responsive polymer materials [21] have exhibited different

<!-- image -->

<!-- image -->

Citation: Li, K.; Liu, Y.; Dai, Y.; Yu, Y. Self-Vibration of a Liquid Crystal Elastomer Fiber-Cantilever System under Steady Illumination. Polymers 2023 , 15 , 3397. https://doi.org/ 10.3390/polym15163397

Academic Editors: Valeriy V. Ginzburg and Alexey V. Lyulin

Received: 19 July 2023

Revised: 8 August 2023

Accepted: 11 August 2023

Published: 13 August 2023

<!-- image -->

Copyright: © 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).

responses under different stimulus conditions. These responses generally change the morphology and motion state of the active materials themselves. People have established various self-oscillating systems and multiple self-sustained motion modes using the properties of active materials, including bending [22-24], swimming [25], swinging [26], rolling [2,9,10,27], rotating [28,29], twisting [30,31], vibration [6], and even synchronized motion of several coupled self-oscillators [32,33]. In general, in all dynamic systems, there is energy dissipation [34], and in practical environments, the vibrations tend to approach an equilibrium state. Therefore, designing different types of self-oscillating systems is a challenging process. In a constant environment, how to enable the system to absorb energy autonomously, compensate for the damping dissipation, and maintain periodic motion is the key to realize self-oscillation. A large number of self-excited oscillatory systems have been established based on various feedback mechanisms. These different feedback mechanisms typically lead to different self-sustained motion modes, such as self-shadowing [35-37], coupling of liquid evaporation and membrane deformation [38], coupling mechanism of air expansion and liquid column motion [39], and coupling of plate bending and chemical reaction [40], all of which can cause self-excited oscillations.

Theadvantagesoflightinvariousstimuliareitssustainability , accuracy , controllability [41,42], and non-contact. Optically-responsive materials that can convert near-infrared and visible light into thermal energy, such as carbon nanotubes, graphene, and liquid crystal elastomers (LCEs) [43-48] have good photomechanical effects [49-54]. Among them, LCEs are important optically responsive materials, synthesized from anisotropic rod-shaped liquid crystal molecules and stretchable long-chain polymers. When liquid crystal monomers are subjected to external stimuli such as light, heat, electricity, and magnetism, they will rotate or undergo phase transitions, thereby changing their configuration and generating macroscopic deformation [55,56]. LCEs typically offer advantages of large deformation, fast deformation response, recoverable deformation, low noise, easy remote control, and easy manipulation. Based on LCEs, photomechanical effects have been utilized to build various selfsustained oscillatory systems, including but not limited to shuttling [57], bending [58], rotation [29,30,55], spinning [59], curling [60], oscillating [61,62], buckling [63-65], rolling [28], floating [66], twisting [67], vibration [68], swimming [25], chaos [69], and even several synchronous motions coupled with self-excited oscillations [2,27,34]. These LCE-based self-sustained oscillatory systems have attracted much attention in both fundamental and applied research [55,70-72].

Although a large number of self-sustained oscillatory systems have been constructed, these systems generally have complex structures, are difficult to manufacture and control, and may not meet the requirements of complex practical applications. In this article, we propose a novel and simple LCE fiber-cantilever system that exhibits self-sustained oscillation under steady illumination and essentially functions as a 'self-shadowing' system. Compared to previous self-oscillating systems such as balls [66] and tubes [42], the structure of one-dimensional fiber is relatively simple, making it easy to assemble and disassemble. It should also be noted that the proposed LCE fiber-cantilever system may exhibit a dependence on the angle of illumination in practice. Furthermore, the system is highly extensible, holding potential for constructing more complex LCE fiber-based systems to achieve advanced self-sustained motions. The objective of this research is to build the LCE fiber-cantilever system and investigate its self-oscillation characteristics under stable illumination. Meanwhile, we discuss the underlying mechanisms of self-oscillation and systematically explore the impacts of various physical and geometric parameters on the system's amplitude and frequency.

The organization of this paper is as follows. First, in Section 2, considering the dynamic LCE model and beam theory, the theoretical model and control equations for the LCE fibercantilever system are established. Then, in Section 3, two motion regimes of the LCE fiber-cantilever system are obtained by numerical calculations, and the mechanism of its self-vibration is explained in detail. Next, in Section 4, the influences of various system

Polymers

2023

,

15

, x FOR PEER REVIEW

3  of  19

of its self-vibration is explained in detail. Next, in Section 4, the in fl

uences of various sys- tem parameters on the amplitude and frequency of self-vibration are discussed in detail.

parameters on the amplitude and frequency of self-vibration are discussed in detail. Finally, the results are summarized. Finally, the results are summarized.

2. Theoretical Model and Formulation

## 2. Theoretical Model and Formulation In this section, we fi

rst propose a light-powered self-oscillation system containing an

In this section, we first propose a light-powered self-oscillation system containing an LCE fiber, an oblique bending cantilever, and a mass block. Then, we present a theoretical model for the self-oscillation system based on the dynamic LCE model [8] and beam theory [73]. The dynamic control equations of the system, the evolution law of the cis number fraction in LCE, and the nondimensionalization of the system parameters are then given in turn. LCE fi ber, an oblique bending cantilever, and a mass block. Then, we present a theoretical model for the self-oscillation system based on the dynamic LCE model [8] and beam theory [73]. The dynamic control equations of the system, the evolution law of the cis number fraction in LCE, and the nondimensionalization of the system parameters are then given in turn.

## 2.1. Dynamics of System 2.1. Dynamics of System

Figure 1 schematically describes the proposed LCE fiber-cantilever system, in which an LCE fiber, a lightweight cantilever beam and a mass block are included. The lightweight cantilever of length LB at an angle q from the horizontal, is fixed on a vertical rigid base. The mass block with mass m at the cantilever end is connected by the LCE fiber fixed on another vertical rigid base to form a tension string system. The bending effect of gravity on the cantilever can be ignored as it is much smaller than other forces. Both the torsion and displacement of the cantilever along the length are small, so the mass block is assumed to move in a plane. We take the initial position of the mass block as the origin of the coordinate system and establish the coordinate axis along the direction of cantilever deflection. The initial length of LCE fiber is L 0. In addition, the masses of the LCE fiber and the cantilever are much less than the mass m , so they are neglected. Figure 1 schematically describes the proposed LCE fi ber-cantilever system, in which an LCE fi ber,  a  lightweight cantilever beam and a mass block are included. The lightweight cantilever of length B L at an angle θ from the horizontal, is fi xed on a vertical rigid base. The mass block with mass m at the cantilever end is connected by the LCE fi ber fi xed on another vertical rigid base to form a tension string system. The bending e ff ect of gravity on the cantilever can be ignored as it is much smaller than other forces. Both the torsion and displacement of the cantilever along the length are small, so the mass block is assumed to move in a plane. We take the initial position of the mass block as the origin of the coordinate system and establish the coordinate axis along the direction of cantilever de fl ection. The initial length of LCE fi ber is 0 L . In addition, the masses of the LCE fi ber and the cantilever are much less than the mass m , so they are neglected.

Reference state

<!-- image -->

Figure 1. Schematic of an LCE fi ber-cantilever system containing an LCE fi ber, a lightweight cantilever beam, and a mass block: ( a ) Reference state; ( b ) Current state; ( c ) Force analysis. L F denotes the tension of the LCE fi ber, B F represents the force exerted by the beam on the mass block, D F represents the air damping force, γ is the angle between the cantilever de fl ection and the horizontal direction, and θ is the inclined angle of cantilever. Figure 1. Schematic of an LCE fiber-cantilever system containing an LCE fiber, a lightweight cantilever beam, and a mass block: ( a ) Reference state; ( b ) Current state; ( c ) Force analysis. FL denotes the tension of the LCE fiber, FB represents the force exerted by the beam on the mass block, FD represents the air damping force, g is the angle between the cantilever deflection and the horizontal direction, and q is the inclined angle of cantilever.

<!-- image -->

<!-- image -->

The system is placed under steady illumination as shown in Figure 1b, with the yellow region representing the illumination zone with a height of δ .  Generally,  chromophores in the LCE fi ber upon illumination undergo series of trans-cis-trans isomerization cycles ending up in the change of the orientation of the trans-isomer long axis [74]. In case of non-polarized light illumination, the long axes orient towards the illumination direction, while in case of illumination with polarized light, the long axes orient perpendicular to the light polarization, because of the direction-dependent absorption of the chromophore. These changes can change the order parameter of the LCE and lead in some geometries to contraction of the fi ber. As the LCE fi ber contracts, the cantilever bends further into the dark zone. When the LCE fi ber is in the dark, the azobenzene molecules in it switch from cis to trans , causing the light-driven contraction of the LCE fi ber to recover. Subsequently, the tension of the LCE fi ber decreases andthe cantilever returns to the illuThe system is placed under steady illumination as shown in Figure 1b, with the yellow region representing the illumination zone with a height of d . Generally, chromophores in the LCE fiber upon illumination undergo series of trans-cis-trans isomerization cycles ending up in the change of the orientation of the trans-isomer long axis [74]. In case of non-polarized light illumination, the long axes orient towards the illumination direction, while in case of illumination with polarized light, the long axes orient perpendicular to the light polarization, because of the direction-dependent absorption of the chromophore. These changes can change the order parameter of the LCE and lead in some geometries to contraction of the fiber. As the LCE fiber contracts, the cantilever bends further into the dark zone. When the LCE fiber is in the dark, the azobenzene molecules in it switch from cis to trans , causing the light-driven contraction of the LCE fiber to recover. Subsequently, the tension of the LCE fiber decreases andthe cantilever returns to the illumination zone due to the structural resistance. Through the proper adjustment of the system parameters and initial conditions, the LCE fiber-cantilever system can maintain continuous self-oscillation.

The mass block is subjected to the tension of LCE fiber, the structural resistance form cantilever, and the air damping force, as depicted in Figure 1c. In the deflection direction,

the control equation for the nonlinear dynamics model of mass block can be expressed as follows:

<!-- formula-not-decoded -->

where .. w refers to the acceleration of the mass block, FL denotes the tension of the LCE fiber, FB represents the force exerted by the beam on the mass block, FD represents the air damping force, and g is the angle between the cantilever deflection and the horizontal direction.

Through the beam deflection theory, the moment of inertia formula, and the trigonometric function, it can be calculated g = arctan [ r 2 tan q ] -q , where r refers to the ratio of cantilever height to width.

The tension of LCE fiber is related to its elongation and cross-sectional area, which can be described as

<!-- formula-not-decoded -->

where FL refers to the elastic modulus of the LCE fiber, AL refers to the cross-sectional area of the LCE fiber, L 0 is the original length of LCE fiber, w t ( ) represents the cantilever-end deflection, i.e., the displacement of the mass block, and # L ( ) t represents the light-driven contraction strain of LCE fiber.

It is assumed that the cantilever beam is always in a state of small deformation, while the theory of linear elasticity is applied, thus the structural resistance from cantilever is proportional to the displacement, that is

<!-- formula-not-decoded -->

where LB is the cantilever length, EBIB is the bending stiffness of the cantilever.

The damping force is assumed to be linearly proportional to the velocity of the mass block, with the formula being

<!-- formula-not-decoded -->

where b denotes the air damping coefficient and . w is the velocity of the mass block.

Thus far, substituting Equations (2)-(4) into Equation (1), we have

<!-- formula-not-decoded -->

## 2.2. Dynamic LCE Model

This section mainly describes the dynamic model of the light-driven contraction in LCE fiber. The fiber radius is assumed to be much smaller than the penetration depth of light, and no absorption gradient within the fiber is considered. The LCE fiber-cantilever system uses a linear model, which is adopted to describe the relationship between the cis number fraction j ( ) t in LCE and the light-driven contraction of LCE, that is

<!-- formula-not-decoded -->

where C 0 is the contraction coefficient.

The light-driven contraction in LCE depend on the cis number fraction j ( ) t [75,76]. The study by Yu et al. found that the trans-to-cis isomerization of LCE could be induced by UV or laser with wavelength less than 400 nm [77]. In this study, a 'push-pull' mechanism is considered to calculate the cis number fraction [76]. The number fraction j ( ) t of the cisisomer depends on the thermal excitation from trans to cis , the thermally driven relaxation from cis to trans , and the light driven relaxation from trans to cis . Supposing that the thermal

excitation from trans to cis can be ignored, the governing equation for the evolution of the cis number fraction can be formulated as

<!-- formula-not-decoded -->

where T 0 refers to the thermally driven relaxation time from the cis to trans , I 0 denotes the light intensity, and h 0 is the light absorption constant. By solving Equation (7), the cis number fraction can be described as

<!-- formula-not-decoded -->

where j 0 represents the initial cis number fraction at t = 0.

In illuminated state, for initially zero-number fraction, i.e., j 0 = 0, Equation (8) can be simplified as

<!-- formula-not-decoded -->

In non-illuminated state, namely I 0 = 0, Equation (8) can be simplified as

<!-- formula-not-decoded -->

where the undetermined j 0 can be set to be the maximum value of j ( ) t in Equation (9), namely, j 0 = h 0 T I 0 0 h 0 T I 0 0 + 1 . Then Equation (10) can be rewritten as

<!-- formula-not-decoded -->

## 2.3. Nondimensionalization

We introduce the following dimensionless quantities by defining: w = w L 0 , initial velocity . w 0 = T w 0 . 0 L 0 , t = t T 0 , spring constant KL = EL AT 2 0 mL 0 , flexural stiffness KB = 3 EB I B T 2 0 mL B 3 , b = b T 0 m , I 0 = h 0 T I 0 0, d = d L 0 , and j = j h ( 0 T I 0 0 + ) 1 h 0 T I 0 0 , to simplify the governing equations Equations (5) and (9)-(11).

The dimensionless form of Equation (5) can be expressed as

<!-- formula-not-decoded -->

In illuminated state, Equation (9) can be rewritten as

<!-- formula-not-decoded -->

and in non-illuminated state, Equation (11) becomes

<!-- formula-not-decoded -->

Equations (12)-(14) are utilized to regulate the self-vibration of the LCE fiber-cantilever system in the presence of steady illumination. These equations involve a time-varying fractional quantity associated with the cis isomer and closely linked to the light intensity. To solve these intricate linear equations, the fourth-order Runge-Kutta method is employed for numerical computations using the Matlab software. Moreover, Equations (13) and (14) are employed to determine the cis number fraction j and time length t , enabling the calculation of tension FL , air damping force FD , and structural resistance FB of the LCE fiber. By iterating calculation with given parameters . w 0, KL , KB , b , I 0, C 0, q , r , and d , the dynamics of the LCE fiber-cantilever system can be obtained.

## 3. Two Motion Regimes and Mechanism of Self-Vibration

In this section, through solving the control equation Equation (12), we first propose two typical motion regimes of the LCE fiber-cantilever system, which are distinguished as static regime and self-vibration regime. Next, the corresponding mechanism of self-vibration is elaborated in detail.

## 3.1. Two Motion Regimes

In order to further study the self-vibration behavior of the LCE fiber-cantilever system, we first need to determine the typical values for the dimensionless system parameters. Based on the existing experiments and information [78-80], Table 1 gathers the typical values of the system parameters required in current paper. The corresponding dimensionless parameters are listed in Table 2. In the following section, these values of parameters are used to study the self-vibration of the LCE fiber-cantilever system under steady illumination. It is worth noting that the small deformation hypothesis can be verified under these given parameters.

Table 1. Material properties and geometric parameters.

| Parameter   | Definition                             | Value   | Unit         |
|-------------|----------------------------------------|---------|--------------|
| I 0         | Light intensity                        | 0~10    | kW/m 2       |
| C 0         | Contraction coefficient                | 0~0.5   | /            |
| KL          | Spring constant                        | 0.1~1   | N/m          |
| KB          | Flexural stiffness                     | 0.3~3   | N/m          |
| b           | Damping coefficient                    | 0~0.001 | kg/s         |
| w 0         | Initial velocity                       | 0~0.5   | mm/s         |
| d           | Height of illumination zone            | 0~0.1   | m            |
| r           | Ratio of cantilever height to width    | 1~20    | /            |
| q           | Inclined angle of cantilever           | 0~1.2   | rad          |
| T 0         | Cis- to trans- thermal relaxation time | 1~100   | ms           |
| h 0         | Light-absorption constant              | 0.001   | m 2 /(s W) · |

Table 2. Dimensionless parameters.

| Parameter   | I 0   | C 0   | KL    | KB   | b     | . w 0   | d     | r    | q      |
|-------------|-------|-------|-------|------|-------|---------|-------|------|--------|
| Value       | 0~1   | 0~0.5 | 0~1.2 | 0~1  | 0~0.2 | 0~5     | 0~0.1 | 1~20 | 0~ 2 p |

By solving Equations (12)-(14), the time histories and phase trajectories for the LCE fiber-cantilever system can be obtained, with examples for I 0 = 0.25 and I 0 = 0.5 shown in Figure 2. The other parameters used in the calculation are set as C 0 = 0.25, KL = 0.2, KB = 0.7, b = 0.02, . w 0 = 0, d = 0.03, r = 2 and q = p 4 . In Figure 2a,b, the amplitude of the cantilever-end deflection gradually decreases with time due to the damping dissipation, and the system eventually reaches a stationary position at equilibrium, which is referred to as the static regime. In contrast, Figure 2c,d show that the system initially vibrates from a static equilibrium position and then progressively increases in vibration amplitude over time until it remains constant. On exposure to steady illumination, the LCE fibercantilever system eventually presents a continuous periodic vibration, which we refer to as the self-vibration regime.

the damping dissipation, and the system eventually reaches a stationary position a librium, which is referred to as the static regime. In contrast, Figure 2c,d show th

system  initially  vibrates  from  a  static  equilibrium  position  and  then  progressiv creases in vibration amplitude over time until it remains constant. On exposure to

illumination, the LCE

7 of 18 ber-cantilever system eventually presents a continuous pe fi

vibration, which we refer to as the self-vibration regime.

<!-- image -->

Self-vibration

0.03

0.4

## 3.2. Mechanism of the Self-Vibration 3.2. Mechanism of the Self-Vibration

In this section, the mechanism of self-vibration will be explained in detail. To understand the energy compensation mechanism of the LCE fi ber-cantilever syste plot the relationship curves for some key physical quantities in the self-vibration pr In  this  case,  the  system  parameters  are  selected  as 5 . 0 0 = I , 25 . 0 0 = C , = L K 7 . 0 = B K , 02 . 0 = β , 0 0 = w  , 03 . 0 = δ , 2 = r , and 4 π θ = . Figure 3a illustrates th tilever-end de fl ection over time, with the yellow area indicating that the LCE fi be the illumination zone. As the system vibrates continuously, the LCE fi ber also osc back and forth between the illumination and dark zones, and the change in the cis n In this section, the mechanism of self-vibration will be explained in detail. To better understand the energy compensation mechanism of the LCE fiber-cantilever system, we plot the relationship curves for some key physical quantities in the self-vibration process. In this case, the system parameters are selected as I 0 = 0.5, C 0 = 0.25, KL = 0.25, KB = 0.7, b = 0.02, . w 0 = 0, d = 0.03, r = 2, and q = p 4 . Figure 3a illustrates the cantilever-end deflection over time, with the yellow area indicating that the LCE fiber is in the illumination zone. As the system vibrates continuously, the LCE fiber also oscillates back and forth between the illumination and dark zones, and the change in the cis number fraction j over time is drawn in Figure 3b. It is clearly observed that as the illumination condition changes, the cis number fraction changes rapidly at first and then slowly approaches a critical value determined by the contraction coefficient C 0. In addition, Figure 4 illustrates several characteristic snapshots for the self-vibration of the LCE fiber-cantilever system during one cycle under steady illumination.

Figure 3c presents the periodic time variation of the tension of the LCE fiber. The tension decreases first and then increases in the illumination zone, while the opposite is true in the dark zone. The hysteresis loop shown in Figure 3d indicates that the LCE fiber-cantilever system maintains its oscillation as the LCE fiber absorbs light energy and does work. The area enclosed by the loop represents the net work done by the tension of the LCE fiber in one cycle, with a value of approximately 0.0029. Like the tension of the LCE fiber, it is clear from Figure 3e that the damping force also presents a periodic time variation. Figure 3f plots the dependence of the damping force on the cantilever-end deflection, which also forms a closed loop representing the damping dissipation, with a value being calculated to be about 0.0029. The net work done by the tension of LCE fiber is exactly equal to the damping dissipation, implying that the energy consumed by the system

Polymers

2023

,

15

, x FOR PEER REVIEW

8  of  19

fraction

ϕ

over time is drawn in Figure 3b. It is clearly observed that as the illumination condition changes, the

cis number fraction changes rapidly at

fi rst and then slowly ap-

proaches a critical value determined by the contraction coe ffi

cient

0

C

. In addition, Figure motion is compensated by the light energy absorbed by the LCE fiber, thus maintaining the self-vibration. 4 illustrates several characteristic snapshots for the self-vibration of the LCE fi ber-cantilever system during one cycle under steady illumination.

<!-- image -->

,

9

Figure 4. Snapshots of the LCE fi ber-cantilever system in one cycle during the self-vibration. U steady illumination, the system exhibits a continuous periodic self-vibration due to the peri variation of light-driven contraction. Figure 4. Snapshots of the LCE fiber-cantilever system in one cycle during the self-vibration. Under steady illumination, the system exhibits a continuous periodic self-vibration due to the periodic variation of light-driven contraction.

<!-- image -->

Figure 3c presents the periodic time variation of the tension of the LCE

fi ber.

tension decreases fi

rst and then increases in the illumination zone, while the opposi true in the dark zone. The hysteresis loop shown in Figure 3d indicates that the LCE

fi cantilever system maintains its oscillation as the LCE

fi ber absorbs light energy and

Polymers

2023

Polymers

2023

## 4. Parametric Study

In the mechanical model of the self-vibration for the LCE fiber-cantilever system described above, there are nine dimensionless system parameters: I 0, C 0, KL , KB , b , . w 0, d , r , and q . In this section, we investigate in detail the effects of these system parameters on the self-vibration of the LCE fiber-cantilever system, including its frequency and amplitude. The dimensionless self-vibration frequency and amplitude are denoted by f and A , respectively.

## 4.1. Effect of Light Intensity

,

The effect of light intensity on the self-vibration is discussed in current subsection. In this case, the values of the other parameters are, C 0 = 0.25, KL = 0.25, KB = 0.7, b = 0.02, . w 0 = 0, d = 0.03, r = 2, and q = p 4 . The limit cycles of the self-vibration are depicted in Figure 5a, where I 0 = 0.39 is the critical value of light intensity between the static and self-vibration regimes. When the light intensity is below 0.39, the system is in static regime, while above 0.39, the system is in self-vibration regime. When the light intensity is relatively small, the LCE fiber does not absorb enough light energy to offset the damping dissipation, thus it cannot maintain its continuous motion and comes to rest. Conversely, when the light intensity is large enough, the light energy absorbed by the system can compensate for the damping dissipation, so as to maintain its own motion. Figure 5b describes the effect of light intensity on the self-vibration amplitude and frequency. With the increasing light intensity, the amplitude increases, while the frequency remains essentially constant. Larger light intensity allows the system to absorb more light energy, thereby maintaining oscillation with higher amplitude. These results suggest that increasing the light intensity is crucial for improving the energy utilization efficiency of the LCE fiber-cantilever system. 15 , x FOR PEER REVIEW 10  of  19 remains essentially constant. Larger light intensity allows the system to absorb more light energy, thereby maintaining oscillation with higher amplitude. These results suggest that increasing the light intensity is crucial for improving the energy utilization e ffi ciency of the LCE fi ber-cantilever system.

<!-- image -->

Figure 5. E ff ect of light intensity on the self-vibration. ( a ) Limit cycles with 5 . 0 0 = I , 0 0 = I 7 . 0 0 = I . ( b ) Variations of amplitude and frequency with di ff erent light intensities. Figure 5. Effect of light intensity on the self-vibration. ( a ) Limit cycles with I 0 = 0.5, I 0 = 0.6 and I 0 = 0.7. ( b ) Variations of amplitude and frequency with different light intensities.

<!-- image -->

6

.

and

## 4.2. E ff ect of Contraction Coe 4.2. Effect of Contraction Coefficient

ffi cient

This subsection mainly discusses the e ff ect of contraction coe ffi cient on the self-vibration.  Here,  the  values  of  the  other  parameters  are 5 . 0 0 = I , 25 . 0 = L K , 7 . 0 = B K , 02 . 0 = β , 0 0 = w  , 03 . 0 = δ , 2 = r , and 4 π θ = . Figure 6a plots the limit cycles for different contraction coe ffi cients. Obviously, there exists a critical value for contraction coeffi cient to trigger the self-vibration, which is numerically determined to be 0.207. A small contraction coe ffi cient means a low light energy input, and there is not enough energy to compensate for the damping dissipation. For 25 . 0 0 = C , 35 . 0 0 = C ,  and 45 . 0 0 = C ,  the self-vibration can be triggered. Figure 6b presents the dependencies of the self-vibration amplitude and frequency on the contraction coe ffi cient. The larger the contraction coe ffi -cient,  the  higher  the  amplitude. As  the  contraction  coe ffi cient  increases,  the  LCE fi ber makes more e ffi cient use of the illumination, absorbs more light energy, and shifts the system from a static regime to a self-vibration regime, resulting in an increase in the amplitude. The result implies that increasing the contraction coe ffi cient of LCE material can improve the e ffi cient conversion of light energy to mechanical energy. This subsection mainly discusses the effect of contraction coefficient on the selfvibration. Here, the values of the other parameters are I 0 = 0.5, KL = 0.25, KB = 0.7, b = 0.02, . w 0 = 0, d = 0.03, r = 2, and q = p 4 . Figure 6a plots the limit cycles for different contraction coefficients. Obviously, there exists a critical value for contraction coefficient to trigger the self-vibration, which is numerically determined to be 0.207. A small contraction coefficient means a low light energy input, and there is not enough energy to compensate for the damping dissipation. For C 0 = 0.25, C 0 = 0.35, and C 0 = 0.45, the self-vibration can be triggered. Figure 6b presents the dependencies of the self-vibration amplitude and frequency on the contraction coefficient. The larger the contraction coefficient, the higher the amplitude. As the contraction coefficient increases, the LCE fiber makes more efficient use of the illumination, absorbs more light energy, and shifts the system from a static regime to a self-vibration regime, resulting in an increase in the amplitude. The result implies that increasing the contraction coefficient of LCE material can improve the efficient conversion of light energy to mechanical energy.

Polymers

2023

,

self-vibration can be triggered. Figure 6b presents the dependencies of the self-vibration amplitude and frequency on the contraction coe

ffi cient. The larger the contraction coe

ffi

-

cient,  the  higher  the  amplitude. As  the  contraction  coe ffi

cient  increases,  the  LCE

fi ber

makes more e ffi

cient use of the illumination, absorbs more light energy, and shifts the system from a static regime to a self-vibration regime, resulting in an increase in the am-

plitude. The result implies that increasing the contraction coe ffi

cient of LCE material can improve the e

ffi cient conversion of light energy to mechanical energy.

<!-- image -->

<!-- image -->

15

, x FOR PEER REVIEW

11  of  19

coe ffi

cients.

## 4.3. Effect of Spring Constant 4.3. E ff

ect of Spring Constant

This subsection mainly focuses on the effect of spring constant on the self-vibration. In this case, the values of the other parameters are I 0 = 0.5, C 0 = 0.25, KB = 0.7, b = 0.02, . w 0 = 0, d = 0.03, r = 2, and q = p 4 . Figure 7a displays the limit cycles for different spring constants, among which two critical spring constants exist for triggering the self-vibration. It is clear to see that the system is in the static regime when the spring constant is below 0.214 or above 0.951. This can be explained by the relationship between the spring constant and the tension of the LCE fiber. When the spring constant is small, the tension of the LCE fiber is small, which is not enough to force the system to remain in oscillation. When the spring constant is large, the tension of the LCE fiber can be equal to the structural resistance, thus allowing the whole system to equilibrate the forces and reach a static regime. Figure 7b illustrates that the spring constant has a significant effect on the amplitude and frequency of the self-vibration. As the spring constant increases, the amplitude increases, while the frequency decreases. This is because the spring constant determines the driving force of the system, which in turn affects the oscillatory behavior of the system. Therefore, when we design the LCE fiber-cantilever system, the adjustment of the spring constant can be used to control its amplitude and frequency to achieve better performance. For example, in some robotic applications, the LCE fiber-cantilever system is required to realize stable motion or grasp an object, we can select the appropriate spring constant according to the desired motion mode and the weight of the object, so as to keep the system stable and have good accuracy during operation. In addition, when designing suspended structures or other oscillatory systems, the amplitude and frequency can also be controlled according to the variation of the spring constant to achieve better performance. This subsection mainly focuses on the e ff ect of spring constant on the self-vibration. In  this  case,  the  values  of  the  other  parameters  are 5 . 0 0 = I , 25 . 0 0 = C , 7 . 0 = B K , 02 . 0 = β , 0 0 = w  , 03 . 0 = δ , 2 = r , and 4 π θ = . Figure 7a displays the limit cycles for di ff erent spring constants, among which two critical spring constants exist for triggering the self-vibration. It is clear to see that the system is in the static regime when the spring constant is below 0.214 or above 0.951. This can be explained by the relationship between the spring constant and the tension of the LCE fi ber. When the spring constant is small, the tension of the LCE fi ber is small, which is not enough to force the system to remain in oscillation. When the spring constant is large, the tension of the LCE fi ber can be equal to the  structural  resistance,  thus  allowing  the  whole  system  to  equilibrate  the  forces  and reach a static regime. Figure 7b illustrates that the spring constant has a signi fi cant e ff ect on the amplitude and frequency of the self-vibration. As the spring constant increases, the amplitude increases, while the frequency decreases. This is because the spring constant determines the driving force of the system, which in turn a ff ects the oscillatory behavior of the system. Therefore, when we design the LCE fi ber-cantilever system, the adjustment of the spring constant can be used to control its amplitude and frequency to achieve be tt er performance. For example, in some robotic applications, the LCE fi ber-cantilever system is required to realize stable motion or grasp an object, we can select the appropriate spring constant according to the desired motion mode and the weight of the object, so as to keep the system stable and have good accuracy during operation. In addition, when designing suspended structures or other oscillatory systems, the amplitude and frequency can also be controlled according to the variation of the spring constant to achieve be tt er performance.

<!-- image -->

Figure 7. E ff ect of spring constant on the self-vibration  ( . a ) Limit cycles with 25 . 0 = L K , L K , and 45 . 0 = L K ( b ) Variations of amplitude and frequency with di ff erent spring constants. Figure 7. Effect of spring constant on the self-vibration. ( a ) Limit cycles with KL = 0.25, KL = 0.35, and KL = 0.45. ( b ) Variations of amplitude and frequency with different spring constants.

<!-- image -->

4.4. E

ff ect of Flexural Sti

ff ness

The  in

C

fl uence  of

0

25

.

0

=

,

fl

=

25

.

0

L

K

,

exural  sti

β

ff ness  on  the  self-vibration  is  provided  for

=

02

.

0

,

5

.

0

0

=

I

,

=

0

π

0

w



,

03

.

0

=

δ

,

2

=

r

, and

4

θ =

.

The limit cycles for di

ff erent

fl exural sti

ff nesses are drawn in Figure 8a. The

fl exural sti

ff ness has two crit-

ical values for the transition between the static and self-vibration regimes, which are nu-

=

0

.

35

Polymers

2023

## 4.4. Effect of Flexural Stiffness

,

The influence of flexural stiffness on the self-vibration is provided for I 0 = 0.5, C 0 = 0.25, KL = 0.25, b = 0.02, . w 0 = 0, d = 0.03, r = 2, and q = p 4 . The limit cycles for different flexural stiffnesses are drawn in Figure 8a. The flexural stiffness has two critical values for the transition between the static and self-vibration regimes, which are numerically calculated to be around 0.19 and 0.81. When the flexural stiffness is small, the structural resistance of the cantilever is small, and the net work done by the tension of the LCE fiber is not sufficient to maintain the self-vibration. When the flexural stiffness is large, the structural resistance from the cantilever is so great that the tension of the LCE fiber cannot drive the system to oscillate. Figure 8b plots the variations of self-vibration amplitude and frequency with different flexural stiffnesses. As the flexural stiffness increases, the amplitude decreases, while the frequency increases. This can be explained by the beam theory, where the greater the flexural stiffness of the beam, the greater the recovery force on the beam, thus preventing further bending of the beam. As a result, the amplitude decreases. Therefore, to improve the system stability, it is a good way to choose the appropriate flexural stiffness of the beam. 15 , x FOR PEER REVIEW 12  of  19 amplitude and frequency with di ff erent fl exural sti ff nesses. As the fl exural sti ff ness increases, the amplitude decreases, while the frequency increases. This can be explained by the beam theory, where the greater the fl exural sti ff ness of the beam, the greater the recovery force on the beam, thus preventing further bending of the beam. As a result, the amplitude decreases. Therefore, to improve the system stability, it is a good way to choose the appropriate fl exural sti ff ness of the beam.

<!-- image -->

<!-- image -->

5

,

ff

nesses.

## 4.5. Effect of Damping Coefficient

4.5. E ff ect of Damping Coe ffi cient Figure 9 presents the in fl uence of damping coe ffi cient on the self-vibration, with parameters 5 . 0 0 = I , 25 . 0 0 = C , 25 . 0 = L K , 7 . 0 = B K , 0 0 = w  , 03 . 0 = δ , 2 = r , and 4 π θ = . The limit cycles for di ff erent damping coe ffi cients can be observed in Figure 9a. It is not di ffi cult to fi nd that the variation of damping coe ffi cient does not a ff ect the motion regime of the LCE fi ber-cantilever system. For di ff erent damping coe ffi cients, the system is always in a self-vibration regime. The dependencies of the self-vibration amplitude and frequency  on  the  damping  coe ffi cient  are  depicted  in  Figure  9b.  With  the  increase  of damping coe ffi cient,  the  amplitude  decreases  sharply  and  then  slowly,  presenting  the characteristics of an exponential function. In contrast, changes in the damping coe ffi cient have li tt le  e ff ect on the frequency. This suggests that the damping coe ffi cient plays an important role in in fl uencing the amplitude and energy level of self-vibration systems. Proper adjustment of the damping coe ffi cient can control the vibration amplitude and energy level of the system to ensure the system stability. Moreover, as the damping coe ffi -cient has li tt le e ff ect on the frequency, the damping coe ffi cient and frequency need to be considered  comprehensively  during  the  system  design  process  to  obtain  the  optimal scheme. These research results not only provide important application value in the fi eld of engineering design and manufacture, but also provide new ideas and methods for the Figure 9 presents the influence of damping coefficient on the self-vibration, with parameters I 0 = 0.5, C 0 = 0.25, KL = 0.25, KB = 0.7, . w 0 = 0, d = 0.03, r = 2, and q = p 4 . The limit cycles for different damping coefficients can be observed in Figure 9a. It is not difficult to find that the variation of damping coefficient does not affect the motion regime of the LCE fiber-cantilever system. For different damping coefficients, the system is always in a self-vibration regime. The dependencies of the self-vibration amplitude and frequency on the damping coefficient are depicted in Figure 9b. With the increase of damping coefficient, the amplitude decreases sharply and then slowly, presenting the characteristics of an exponential function. In contrast, changes in the damping coefficient have little effect on the frequency. This suggests that the damping coefficient plays an important role in influencing the amplitude and energy level of self-vibration systems. Proper adjustment of the damping coefficient can control the vibration amplitude and energy level of the system to ensure the system stability. Moreover, as the damping coefficient has little effect on the frequency, the damping coefficient and frequency need to be considered comprehensively during the system design process to obtain the optimal scheme. These research results not only provide important application value in the field of engineering design and manufacture, but also provide new ideas and methods for the in-depth understanding of complex systems.

in-depth understanding of complex systems.

-

Polymers

2023

Polymers

2023

,

15

,

, x FOR PEER REVIEW

15

, x FOR PEER REVIEW

13  of  19

13  of  19

<!-- image -->

<!-- image -->

Figure  9.

E

ff ect  of  damping  coe

)  Limit  cycles  with

01

.

0

=

β

,

,

e

ffi cients.

ect of Initial Velocity

4.6. E ff ect of Initial Velocity The e rameters ff ect of initial velocity 0 w  on the self-vibration is displayed in Figure 10, with other parameters  being 5 . 0 0 = I , 25 . 0 0 = C , 25 . 0 = L K , 7 . 0 = B K , 02 . 0 = β , 03 . 0 = δ , 2 = r , and  on, and the limit cycles are plo 4 π θ = . 0 0 = w  , 5 . 0 0 = w  , and  ed in Figure 10a. It is worth men1 0 = w  are  found  to  successfully trigger the self-vibration, and the limit cycles are plo tt ed in Figure 10a. It is worth mentioning that the limit cycles for these three initial velocities overlap. As can be seen in Figure 10b, the variation of the initial velocity does not a ff ect the amplitude and frequency of the system. Since the self-vibration results from the energy conversion between the damping dissipation and the network done by the tension of the LCE fi ber, the self-vibration amplitude and frequency are determined by the internal properties of the system, which is consistent with other self-vibration systems. The initial velocity therefore has no e ff ect The effect of initial velocity . w 0 on the self-vibration is displayed in Figure 10, with other parameters being I 0 = 0.5, C 0 = 0.25, KL = 0.25, KB = 0.7, b = 0.02, d = 0.03, r = 2, and q = p 4 . . w 0 = 0, . w 0 = 0.5, and . w 0 = 1 are found to successfully trigger the self-vibration, and the limit cycles are plotted in Figure 10a. It is worth mentioning that the limit cycles for these three initial velocities overlap. As can be seen in Figure 10b, the variation of the initial velocity does not affect the amplitude and frequency of the system. Since the self-vibration results from the energy conversion between the damping dissipation and the network done by the tension of the LCE fiber, the self-vibration amplitude and frequency are determined by the internal properties of the system, which is consistent with other self-vibration systems. The initial velocity therefore has no effect on the final amplitude of the system. The e ff ect of initial velocity 0 w  on the self-vibration is displayed in Figure 10, with other pa being 5 . 0 0 = I , 25 . 0 0 = C , 25 . 0 = L K , 7 . 0 = B K , 02 . 0 = β , 03 . 0 = δ , 2 = r , and 4 π θ = . 0 0 = w  , 5 . 0 0 = w  , and 1 0 = w  are  found  to  successfully trigger the self-vibrati tt tioning that the limit cycles for these three initial velocities overlap. As can be seen in Figure 10b, the variation of the initial velocity does not a ff ect the amplitude and frequency of the system. Since the self-vibration results from the energy conversion between the damping dissipation and the network done by the tension of the LCE fi ber, the self-vibration amplitude and frequency are determined by the internal properties of the system, which is consistent with other self-vibration systems. The initial velocity therefore has no e ff ect on the fi nal amplitude of the system.

## 4.6. Effect of Initial Velocity 4.6. E ff

on the

<!-- image -->

<!-- image -->

fi nal amplitude of the system.

5

5

.

.

0

0

=

=

and frequency with di

ff erent initial velocities.

4.7. E ff ect of Illumination Zone Height This subsection presents a discussion on the e ff ect of illumination zone height on the self-vibration.  In  the  calculation,  we  set  other  parameters  as 5 . 0 0 = I , 25 . 0 0 = C , 25 . 0 = L K , 7 . 0 = B K , 02 . 0 = β , 0 0 = w  , 2 = r , and 4 π θ = . As  observed  from  Figure 4.7. E ff ect of Illumination Zone Height This subsection presents a discussion on the e ff ect of illumination zone height on the self-vibration.  In  the  calculation,  we  set  other  parameters  as 5 . 0 0 = I , 25 . 0 0 = C , 25 . 0 = L K , 7 . 0 = B K , 02 . 0 = β , 0 0 = w  , 2 = r , and 4 π θ = . As  observed  from  Figure This subsection presents a discussion on the effect of illumination zone height on the self-vibration. In the calculation, we set other parameters as I 0 = 0.5, C 0 = 0.25, KL = 0.25, KB = 0.7, b = 0.02, . w 0 = 0, r = 2, and q = p 4 .As observed from Figure 11a, for the phase transition between the static and self-vibration regimes, two critical illumination zone heights exist with values of 0.001 and 0.037, respectively. When the illumination zone height is less than 0.001 or greater than 0.037, the system is in astatic regime. When the illumination zone height is within the interval of 0.001 and 0.037, the system is in a self-vibration regime. The effect of illumination zone height on the amplitude and frequency is shown in the Figure 11b. Obviously, the amplitude and frequency do not vary with increasing the illumination zone height. This is contributed to the fact that as the illumination zone expands, the tension of the LCE fiber increases, and the structural resistance from cantilever also increases accordingly. Consequently, the system encounters

## , and 1 w 0 =  . ( b ) Variations of amplitude 4.7. Effect of Illumination Zone Height

Polymers

2023

lumination zone heights exist with values of 0.001 and 0.037, respectively. When the illu- mination zone height is less than 0.001 or greater than 0.037, the system is in astatic regime.

When the illumination zone height is within the interval of 0.001 and 0.037, the system is in a self-vibration regime. The e

ff ect of illumination zone height on the amplitude and

frequency is shown in the Figure 11b. Obviously, the amplitude and frequency do not vary with increasing the illumination zone height. This is contributed to the fact that as

the illumination zone expands, the tension of the LCE

fi ber increases, and the structural

resistance from cantilever also increases accordingly. Consequently, the system encoun- greater resistance during self-vibration, resulting in a drop in amplitude. In conclusion, adjusting the appropriate range of the illumination zone can be more effective in improving the efficiency of light utilization. ters greater resistance during self-vibration, resulting in a drop in amplitude. In conclusion, adjusting the appropriate range of the illumination zone can be more e ff ective in improving the e ffi ciency of light utilization.

<!-- image -->

<!-- image -->

,

## 4.8. Effect of Ratio of Cantilever Height to Width 4.8. E ff ect of Ratio of Cantilever Height to Width

This subsection mainly discusses how the ratio of cantilever height to width affects the self-vibration. In this case, the other dimensionless parameters are selected as I 0 = 0.5, C 0 = 0.25, KL = 0.25, KB = 0.7, b = 0.02, . w 0 = 0, d = 0.03, and q = p 4 . Figure 12a shows the three limit cycles for ratios of cantilever height to width of r = 2, r = 4, and r = 6. The system is in the static regime when the ratio is below 1.48, while it is in the self-vibration regime when the ratio exceeds 1.48. This is due to the small deflection angle of the cantilever end when the ratio of cantilever height to width is small. The longitudinal deflection of the cantilever end is too small for the system to leave the illumination zone, so the system becomes static. Figure 12b depicts how the ratio of cantilever height to width affects the self-vibration amplitude and frequency. As the ratio of cantilever height to width increases, the self-vibration amplitude will first decrease rapidly, and then a marginal effect occurs, slowing down the reduction rate. At the same time, the self-vibration frequency will first increase rapidly, and then a marginal effect appears, slowing down its increase. These findings underscore the significance of meticulous selection of the ratio of cantilever height to width and suggest that opting for an appropriate ratio can effectively enhance the efficiency of converting light energy into mechanical energy. This subsection mainly discusses how the ratio of cantilever height to width a ff ects the self-vibration. In this case, the other dimensionless parameters are selected as 5 . 0 0 = I , 25 . 0 0 = C , 25 . 0 = L K , 7 . 0 = B K , 02 . 0 = β , 0 0 = w  , 03 . 0 = δ , and 4 π θ = . Figure 12a shows the three limit cycles for ratios of cantilever height to width of 2 = r , 4 = r ,  and 6 = r . The system is in the static regime when the ratio is below 1.48, while it is in the selfvibration regime when the ratio exceeds 1.48. This is due to the small de fl ection angle of the cantilever end when the ratio of cantilever height to width is small. The longitudinal de fl ection of the cantilever end is too small for the system to leave the illumination zone, so the system becomes static. Figure 12b depicts how the ratio of cantilever height to width a ff ects  the  self-vibration  amplitude  and  frequency. As  the  ratio  of  cantilever  height  to width increases, the self-vibration amplitude will fi rst decrease rapidly, and then a marginal e ff ect occurs, slowing down the reduction rate. At the same time, the self-vibration frequency will fi rst increase rapidly, and then a marginal e ff ect appears, slowing down its increase. These fi ndings underscore the signi fi cance of meticulous selection of the ratio of cantilever height to width and suggest that opting for an appropriate ratio can e ff ectively enhance the e ffi ciency of converting light energy into mechanical energy.

Figure 12. E ff ect of ratio of cantilever height to width on the self-vibration  ( . a )  Limit cycles with 2 = r , 4 = r ,  and 6 = r . ( b ) Variations of amplitude and frequency with di ff erent ratios of cantilever height to width. Figure 12. Effect of ratio of cantilever height to width on the self-vibration. ( a ) Limit cycles with r = 2, r = 4, and r = 6. ( b ) Variations of amplitude and frequency with different ratios of cantilever height to width.

<!-- image -->

<!-- image -->

## 4.9. E ff ect of Inclined Angle of Cantilever 4.9. Effect of Inclined Angle of Cantilever

,

The inclined angle of cantilever a ff ecting the self-vibration is investigated in this subsection,  where  the  other  dimensionless  parameters  are  chosen  as 5 . 0 0 = I , 25 . 0 0 = C The inclined angle of cantilever affecting the self-vibration is investigated in this subsection, where the other dimensionless parameters are chosen as I 0 = 0.5, C 0 = 0.25,

K

25

.

0

=

L

,

7

.

0

=

B

K

,

02

.

0

=

β

,

0

0

=

w



,

03

.

0

=

δ

,

and

2

=

r

.

Figure  13a  illustrates the limit cycles for di

ff erent inclined angles, in which

2

π

123

π

45

θ =

and

360

θ =

are the two critical inclined angles for the phase transition between the static and the self-vibration

Polymers

2023

,

KL = 0.25, KB = 0.7, b = 0.02, . w 0 = 0, d = 0.03, and r = 2. Figure 13a illustrates the limit cycles for different inclined angles, in which q = 2 p 45 and q = 123 p 360 are the two critical inclined angles for the phase transition between the static and the self-vibration regimes. The self-vibration can be triggered with inclined angles of q = p 6 , q = p 4 , and q = p 3 , while the system is in the static regime with q &lt; 2 p 45 and q &gt; 123 p 360 . Clearly observed from Figure 13b that as the inclined angle of cantilever increases, the self-vibration frequency first increases and then decreases, and conversely the amplitude first decreases and then increases, indicating that there is an optimal inclined angle for the self-excited oscillation. In summary, setting an appropriate inclined angle of cantilever can promote the self-vibration. Too large- or too small- inclined angle of cantilever is not conducive to the self-vibration of the system. 15 , x FOR PEER REVIEW 16  of  19 the self-vibration. Too large- or too small- inclined angle of cantilever is not conducive to the self-vibration of the system.

<!-- image -->

<!-- image -->

θ =

π

6

,

) Variations of amplitude and frequency with di

,  and

.  (

b

ff erent inclined angles of

## 5. Conclusions

4

3

cantilever.

5. Conclusions Self-excited oscillatory systems can maintain continuous motion by absorbing energy from the stable external environment, and possess potential applications in biomedicine, advanced robotics, rescue operations, military industry, and other fi elds. In order to overcome the disadvantages of existing self-sustained oscillatory systems that are relatively complex in structure and di ffi cult to fabricate and control, we creatively propose a novel light-powered LCE fi ber-cantilever system composed of an LCE fi ber, a lightweight cantilever beam, and a mass block under steady illumination. The dynamic control equations for the LCE fi ber-cantilever system are derived based on the established LCE dynamic model, beam theory, and de fl ection formula. The solutions of the nonlinear control equations are obtained using the Runge-Ku tt a numerical calculation method with MATLAB software. The results show that the LCE fi ber-cantilever system evolves into two motion regimes, namely the static and self-vibration regimes. We have described these two motion regimes speci fi cally and also revealed the energy compensation mechanism of the system. In a constant illumination, the positive work done by the tension of the LCE fi ber is used to compensate for the structural resistance from the cantilever and the air dampSelf-excited oscillatory systems can maintain continuous motion by absorbing energy from the stable external environment, and possess potential applications in biomedicine, advanced robotics, rescue operations, military industry, and other fields. In order to overcome the disadvantages of existing self-sustained oscillatory systems that are relatively complex in structure and difficult to fabricate and control, we creatively propose a novel light-powered LCE fiber-cantilever system composed of an LCE fiber, a lightweight cantilever beam, and a mass block under steady illumination. The dynamic control equations for the LCE fiber-cantilever system are derived based on the established LCE dynamic model, beam theory, and deflection formula. The solutions of the nonlinear control equations are obtained using the Runge-Kutta numerical calculation method with MATLAB software. The results show that the LCE fiber-cantilever system evolves into two motion regimes, namely the static and self-vibration regimes. We have described these two motion regimes specifically and also revealed the energy compensation mechanism of the system. In a constant illumination, the positive work done by the tension of the LCE fiber is used to compensate for the structural resistance from the cantilever and the air damping, resulting in the contraction and relaxation.

ing, resulting in the contraction and relaxation. Further numerical calculations show that the light intensity, contraction coe ffi cient, spring constant, fl exural sti ff ness, damping coe ffi cient, ratio of cantilever height to width, and the inclined angle of the cantilever have a considerable e ff ect on the self-vibration amplitude of the system. The spring constant of the LCE fi ber and the fl exural sti ff ness of the cantilever beam signi fi cantly a ff ect the self-vibration frequency of the system. The illumination zone height has li tt le e ff ect on the amplitude and frequency, and the amplitude and frequency are not a ff ected by the initial velocity. The LCE fi ber-cantilever system constructed in this paper is a simple, easy-to-assemble and disassemble, easy-to-prepare, and highly expandable one-dimensional fi ber-based system. It is expected to meet the application requirements of practical complex scenarios and has important application value Further numerical calculations show that the light intensity, contraction coefficient, spring constant, flexural stiffness, damping coefficient, ratio of cantilever height to width, and the inclined angle of the cantilever have a considerable effect on the self-vibration amplitude of the system. The spring constant of the LCE fiber and the flexural stiffness of the cantilever beam significantly affect the self-vibration frequency of the system. The illumination zone height has little effect on the amplitude and frequency, and the amplitude and frequency are not affected by the initial velocity. The LCE fiber-cantilever system constructed in this paper is a simple, easy-to-assemble and disassemble, easy-to-prepare, and highly expandable one-dimensional fiber-based system. It is expected to meet the application requirements of practical complex scenarios and has important application in the

fi elds of autonomous robotics, energy harvesters, autonomous separators, sensors,

mechanical logic devices, and bionic design.

Author Contributions:

The contribution of the authors are as follows: Data curation, Visualization,

Validation,  Methodology,  Software,  K.L.;  Validation,  Methodology,  Software,  Writing-Original

value in the fields of autonomous robotics, energy harvesters, autonomous separators, sensors, mechanical logic devices, and bionic design.

Author Contributions: The contribution of the authors are as follows: Data curation, Visualization, Validation, Methodology, Software, K.L.; Validation, Methodology, Software, Writing-Original draft preparation, Y.L.; Validation, Writing-Reviewing and Editing, Y.D.; Conceptualization, Investigation, Supervision, Writing-Reviewing and Editing, Y.Y. All authors have read and agreed to the published version of the manuscript.

Funding: This study was supported by University Natural Science Research Project of Anhui Province under Grant Nos. 2022AH020029 and KJ2020A0453, National Natural Science Foundation of China under Grant Nos. 12172001 and 12202002, and Anhui Provincial Natural Science Foundation under Grant Nos. 2208085Y01 and 2008085QA23.

Institutional Review Board Statement: Not applicable.

Data Availability Statement: Not applicable.

Acknowledgments: Not applicable.

Conflicts of Interest: The authors declare that they have no known competing financial interest or personal relationships that could have appeared to influence the work reported in this paper.

## References

- 1. Ding, W. Self-Excited Vibration ; Springer: Berlin/Heidelberg, Germany, 2010.
- 2. Sangwan, V.; Taneja, A.; Mukherjee, S. Design of a robust self-excited biped walking mechanism. Mech. Mach. Theory 2004 , 39 , 1385-1397. [CrossRef]
- 3. Wang, X.; Tan, C.F.; Chan, K.H.; Lu, X.; Zhu, L.; Kim, S.; Ho, G.W. In-built thermo-mechanical cooperative feedback mechanism for self-propelled multimodal locomotion and electricity generation. Nat. Commun. 2018 , 9 , 3438. [CrossRef]
- 4. Nocentini, S.; Parmeggiani, C.; Martella, D.; Wiersma, D.S. Optically driven soft micro robotics. Adv. Opt. Mater. 2018 , 6 , 1800207. [CrossRef]
- 5. Wang, X.; Ho, G.W. Design of untethered soft material micromachine for life-like locomotion. Mat. Today 2022 , 53 , 197-216. [CrossRef]
- 6. Hu, W.; Lum, G.Z.; Mastrangeli, M.; Sitti, M. Small-scale soft-bodied robot with multimodal locomotion. Nature 2018 , 554 , 81-85. [CrossRef] [PubMed]
- 7. Cheng, Y.; Lu, H.; Lee, X.; Zeng, H.; Priimagi, A. Kirigami-based light-induced shape-morphing and locomotion. Adv. Mater. 2019 , 32 , 1906233. [CrossRef] [PubMed]
- 8. Yang, L.; Chang, L.; Hu, Y.; Huang, M.; Ji, Q.; Lu, P.; Liu, J.; Chen, W.; Wu, Y. An autonomous soft actuator with light-driven self-sustained wavelike oscillation for phototactic self-locomotion and power generation. Adv. Funct. Mater. 2020 , 30 , 1908842. [CrossRef]
- 9. Shin, B.; Ha, J.; Lee, M.; Park, K.; Park, G.H.; Choi, T.H.; Cho, K.-J.; Kim, H.-Y. Hygrobot: A self-locomotive ratcheted actuator powered by environmental humidity. Sci. Robot. 2018 , 3 , eaar2629. [CrossRef]
- 10. Liao, B.; Zang, H.; Chen, M.; Wang, Y.; Lang, X.; Zhu, N.; Yang, Z.; Yi, Y. Soft Rod-Climbing Robot Inspired by Winding Locomotion of Snake. Soft Robot. 2020 , 7 , 500-511. [CrossRef] [PubMed]
- 11. He, Q.; Yin, R.; Hua, Y.; Jiao, W.; Mo, C.; Shu, H.; Raney, J. A modular strategy for distributed, embodied control of electronics-free soft robots. Sci. Adv. 2023 , 9 , eade9247. [CrossRef]
- 12. Chun, S.; Pang, C.; Cho, S.B. A micropillar-assisted versatile strategy for highly sensitive and effificient triboelectric energy generation under in-plane stimuli. Adv. Mater. 2020 , 32 , 1905539. [CrossRef]
- 13. Zhao, D.; Liu, Y. A prototype for light-electric harvester based on light sensitiveliquid crystal elastomer cantilever. Energy 2020 , 198 , 117351. [CrossRef]
- 14. Tang, R.; Liu, Z.; Xu, D.; Liu, J.; Yu, L.; Yu, H. Optical pendulum generator based on photomechanical liquid-crystalline actuators. ACS Appl. Mater. Interf. 2015 , 7 , 8393-8397. [CrossRef]
- 15. White, T.J.; Broer, D.J. Programmable and adaptive mechanics with liquid crystal polymer networks and elastomers. Nat. Mater. 2015 , 14 , 1087-1098. [CrossRef] [PubMed]
- 16. Rothemund, P.; Ainla, A.; Belding, L.; Preston, D.J.; Kurihara, S.; Suo, Z.; Whitesides, G.M. A soft, bistable valve for autonomous control of soft actuators. Sci. Robot. 2018 , 3 , eaar7986. [CrossRef] [PubMed]
- 17. Yoshida, R. Self-oscillating gels driven by the Belousov-Zhabotinsky reaction as novel smart materials. Adv. Mater. 2010 , 22 , 3463-3483. [CrossRef] [PubMed]
- 18. Hua, M.; Kim, C.; Du, Y.; Wu, D.; Bai, R.; He, X. Swaying gel: Chemo-mechanical self-oscillation based on dynamic buckling. Matter 2021 , 4 , 1029-1041. [CrossRef]

- 19. Wu, J.; Yao, S.; Zhang, H.; Man, W.; Bai, Z.; Zhang, F.; Wang, X.; Fang, D.; Zhang, Y. Liquid crystal elastomer metamaterials with giant biaxial thermal shrinkage for enhancing skin regeneration. Adv. Mater. 2021 , 33 , 2170356. [CrossRef]
- 20. Boissonade, J.; Kepper, P.D. Multiple types of spatio-temporal oscillations induced by differential diffusion in the Landolt reaction. Phys. Chem. 2011 , 13 , 4132-4137. [CrossRef]
- 21. Shen, Q.; Trabia, S.; Stalbaum, T.; Palmre, V.; Kim, K.; Oh, I. A multiple-shape memory polymer-metal composite actuator capable of programmable control, creating complex 3D motion of bending, twisting, and oscillation. Sci. Rep. 2016 , 6 , 24462. [CrossRef]
- 22. Hu, Y.; Ji, Q.; Huang, M.; Chang, L.; Zhang, C.; Wu, G.; Zi, B.; Bao, N.; Chen, W.; Wu, Y. Light-driven self-oscillating actuators with pototactic locomotion based on black phosphorus heterostructure. Angew. Chem. Int. Ed. 2021 , 60 , 20511-20517. [CrossRef] [PubMed]
- 23. Sun, J.; Hu, W.; Zhang, L.; Lan, R.; Yang, H.; Yang, D. Light-driven self-oscillating behavior of liquid-crystalline networks riggered by dynamic isomerization of molecular motors. Adv. Funct. Mater. 2021 , 31 , 2103311. [CrossRef]
- 24. Manna, R.K.; Shklyaev, O.E.; Balazs, A.C. Chemical pumps and flexible sheets spontaneously form self-regulating oscillators in solution Proc. Natl. Acad. Sci. USA 2021 , 118 , e2022987118. [CrossRef] [PubMed]
- 25. Li, Z.; Myung, N.V.; Yin, Y. Light-powered soft steam engines for self-adaptive oscillation and biomimetic swimming. Sci. Robot. 2021 , 6 , eabi4523. [CrossRef]
- 26. Zeng, H.; Lahikainen, M.; Liu, L.; Ahmed, Z.; Wani, O.M.; Wang, M.; Priimagi, A. Light-fuelled freestyle self-oscillators. Nat. Commun. 2019 , 10 , 5057. [CrossRef]
- 27. Chen, Y.; Zhao, H.; Mao, J.; Chirarattananon, P.; Helbling, E.F.; Hyun, N.P.; Clarke, D.R.; Wood, R.J. Controlled flight of a microrobot powered by soft artificial muscles. Nature 2019 , 575 , 324-329. [CrossRef] [PubMed]
- 28. Wang, Y.; Sun, J.; Liao, W.; Yang, Z. Liquid Crystal Elastomer Twist Fibers toward Rotating Microengines. Adv. Mater. 2022 , 34 , 2107840. [CrossRef] [PubMed]
- 29. Bazir, A.; Baumann, A.; Ziebert, F.; Kuli´ c, I.M. Dynamics of fiberboids, Soft. Matter 2020 , 16 , 5210-5223.
- 30. Hu, Z.; Li, Y.; Lv, J. Phototunable self-oscillating system driven by a self-winding fiber actuator. Nat. Commun. 2021 , 12 , 3211. [CrossRef]
- 31. Zhao, Y.; Chi, Y.; Hong, Y.; Li, Y.; Yang, S.; Yin, J. Twisting for soft intelligent autonomous robot in unstructured environments. Proc. Natl. Acad. Sci. USA 2022 , 119 , e2200265119. [CrossRef]
- 32. Ghislaine, V.; Lars, C.M.E.; Anne, H.G.; Meijer, E.W.; Alexander, Y.P.; Henk, N.; Dirk, J.B. Coupled liquid crystalline oscillators in Huygens' synchrony. Nat. Mater. 2021 , 20 , 1702-1706.
- 33. O'Keeffe, K.P.; Hong, H.; Strogatz, S.H. Oscillators that sync and swarm. Nat. Commun. 2017 , 8 , 1504. [CrossRef] [PubMed]
- 34. Li, K.; Zhang, B.; Cheng, Q.; Dai, Y.; Yu, Y. Light-Fueled Synchronization of Two Coupled Liquid Crystal Elastomer Self-Oscillators. Polymers 2023 , 15 , 2886. [CrossRef]
- 35. Vick, D.; Friedrich, L.J.; Dew, S.K.; Brett, M.J.; Robbie, K.; Seto, M.; Smy, T. Self-shadowing and surface diffusion effects in obliquely deposited thin films. Thin Solid Film. 1999 , 339 , 88-94. [CrossRef]
- 36. Kuenstler, A.; Chen, Y.; Bui, P.; Kim, H.; DeSimone, A.; Jin, L.; Hayward, R. Blueprinting photothermal shape-morphing of liquid crystal elastomers. Adv. Mater. 2020 , 32 , 2000609. [CrossRef]
- 37. Liu, X.; Liu, Y. Spontaneous photo-buckling of a liquid crystal elastomer membrane. Int. J. Mech. Sci. 2021 , 201 , 106473. [CrossRef]
- 38. Chakrabarti, A.; Choi, G.P.T.; Mahadevan, L. Self-excited motions of volatile drops on swellable sheets. Phys. Rev. Lett. 2020 , 124 , 258002. [CrossRef] [PubMed]
- 39. Lv, X.; Yu, M.; Wang, W.; Yu, H. Photothermal pneumatic wheel with high loadbearing capacity. Comp. Comm. 2021 , 24 , 100651. [CrossRef]
- 40. Wang, Y.; Liu, J.; Yang, S. Multi-functional liquid crystal elastomer composites. Appl. Phys. Rev. 2022 , 9 , 011301. [CrossRef]
- 41. Lendlein, A.; Jiang, H.; Jünger, O.; Langer, R. Light-induced shape-memory polymers. Nature 2005 , 434 , 879-882. [CrossRef]
- 42. Yu, Y.; Li, L.; Liu, E.; Han, X.; Wang, J.; Xie, Y.; Lu, C. Light-driven core-shell fiber actuator based on carbon nanotubes/liquid crystal elastomer for artificial muscle and phototropic locomotion. Carbon 2022 , 187 , 97-107. [CrossRef]
- 43. Ge, F.; Yang, R.; Tong, X.; Camerel, F.; Zhao, Y. A multifunctional dye-doped liquid crystal polymer actuator: Light-guided transportation, turning in locomotion, and autonomous motion. Angew. Chem. Int. Ed. 2018 , 57 , 11758-11763. [CrossRef] [PubMed]
- 44. Bubnov, A.; Domenici, V.; Hamplov á , V.; Kašpar, M.; Zalar, B. First liquid single crystal elastomer containing lactic acid derivative as chiral co-monomer: Synthesis and properties. Polymers 2011 , 52 , 4490-4497. [CrossRef]
- 45. Milavec, J.; Domenici, V.; Zupanˇ ciˇ c, B.; Rešetiˇ c, A.; Bubnov, A.; Zalar, B. Deuteron NMR resolved mesogen vs. crosslinker molecular order and reorientational exchange in liquid single crystal elastomers. Phys. Chem. Chem. Phys. 2016 , 18 , 4071-4077. [CrossRef]
- 46. Rešetiˇ c, A.; Milavec, J.; Domenici, V.; Zupanˇ ciˇ c, B.; Bubnov, A.; Zalar, B. Stress-strain and thermomechanical characterization of nematic to smectic A transition in a strongly-crosslinked bimesogenic liquid crystal elastomer. Polymers 2018 , 158 , 96-102. [CrossRef]
- 47. Wang, Y.; Yin, R.; Jin, L.; Liu, M.; Gao, Y.; Raney, J.; Yang, S. 3D-Printed Photoresponsive Liquid Crystal Elastomer Composites for Free-Form Actuation. Adv. Funct. Mater. 2023 , 33 , 2210614. [CrossRef]

- 48. Wang, Y.; Dang, A.; Zhang, Z.; Yin, R.; Gao, Y.; Feng, L.; Yang, S. Repeatable and Reprogrammable Shape Morphing from Photoresponsive Gold Nanorod/Liquid Crystal Elastomers. Adv. Mater. 2020 , 32 , 2004270. [CrossRef]
- 49. Ula, S.W.; Traugutt, N.A.; Volpe, R.H.; Patel, R.R.; Yu, K.; Yakacki, C.M. Liquid crystal elastomers, an introduction and review of emerging technologies. Liq. Cryst. Rev. 2018 , 6 , 78-107. [CrossRef]
- 50. Warner, M.; Terentjev, E.M. Liquid Crystal Elastomers ; Oxford University Press: Oxford, UK, 2007.
- 51. Domenici, V.; Milavec, J.; Bubnov, A.; Pociecha, D.; Zupanˇ ciˇ c, B.; Rešetiˇ c, A.; Hamplov á , V.; Gorecka, E.; Zalar, B. Effect of co-monomers' relative concentration on self-assembling behaviour of side-chain liquid crystalline elastomers. RSC Adv. 2014 , 4 , 44056-44064. [CrossRef]
- 52. Domenici, V.; Milavec, J.; Zupanˇ ciˇ c, B.; Bubnov, A.; Hamplov á , V.; Zalar, B. Brief overview on 2H NMR studies of polysiloxanebased side-chain nematic elastomers. Magn. Reson. Chem. 2014 , 52 , 649-655. [CrossRef]
- 53. Milavec, J.; Rešetiˇ c, A.; Bubnov, A.; Zalar, B.; Domenici, V. Dynamic investigations of liquid crystalline elastomers and their constituents by 2H NMR spectroscopy. Liq. Cryst. 2018 , 45 , 2158-2173. [CrossRef]
- 54. Rešetiˇ c, A.; Milavec, J.; Domenici, V.; Zupanˇ ciˇ c, B.; Zalar, B. Deuteron NMR investigation on orientational order parameter in polymer dispersed liquid crystal elastomers. Phys. Chem. Chem. Phys. 2020 , 22 , 23064-23072. [CrossRef]
- 55. Parrany, M. Nonlinear light-induced vibration behavior of liquid crystal elastomer beam. Int. J. Mech. Sci. 2018 , 136 , 179-187. [CrossRef]
- 56. Bishop, R.E.D.; Daniel, C.J. The Mechanics of Vibration ; Cambridge University Press: Cambridge, UK, 2011.
- 57. Yu, Y.; Du, C.; Li, K.; Cai, S. Controllable and versatile self-motivated motion of a fiber on a hot surface. EML 2022 , 57 , 101918. [CrossRef]
- 58. Xu, T.; Pei, D.; Yu, S.; Zhang, X.; Yi, M.; Li, C. Design of MXene composites with biomimetic rapid and self-oscillating actuation under ambient circumstances. ACS Appl. Mater. Interf. 2021 , 13 , 31978-31985. [CrossRef] [PubMed]
- 59. Ge, D.; Dai, Y.; Li, K. Light-powered self-spinning of a button spinner. Int. J. Mech. Sci. 2023 , 238 , 107824. [CrossRef]
- 60. Liu, J.; Zhao, J.; Wu, H.; Dai, Y.; Li, K. Self-Oscillating Curling of a Liquid Crystal Elastomer Beam under Steady Light. Polymers 2023 , 15 , 344. [CrossRef] [PubMed]
- 61. Shen, B.; Kang, S.H. Designing self-oscillating matter. Matter 2021 , 4 , 766-769. [CrossRef]
- 62. Zhou, L.; Dai, Y.; Fang, J.; Li, K. Light-powered self-oscillation in liquid crystal elastomer auxetic metamaterials with large volume change. Int. J. Mech. Sci. 2023 , 254 , 108423. [CrossRef]
- 63. Ge, D.; Dai, Y.; Li, K. Self-Sustained Euler Buckling of an Optically Responsive Rod with Different Boundary Constraints. Polymers 2023 , 15 , 316. [CrossRef]
- 64. Nayfeh, A.H.; Emam, S.A. Exact solution and stability of post buckling configurations of beams. Nonlinear Dyn. 2008 , 54 , 395-408. [CrossRef]
- 65. He, Q.; Wang, Z.; Wang, Y.; Wang, Z.; Li, C.; Annapooranan, R.; Zeng, J.; Chen, R.; Cai, S. Electrospun liquid crystal elastomer microfiber actuator. Sci. Robot. 2021 , 6 , eabi9704. [CrossRef]
- 66. Cheng, Q.; Cheng, W.; Dai, Y.; Li, K. Self-oscillating floating of a spherical liquid crystal elastomer balloon under steady illumination. Int. J. Mech. Sci. 2023 , 241 , 107985. [CrossRef]
- 67. Gelebart, A.H.; Mulder, D.J.; Varga, M.; Konya, A.; Vantomme, G.; Meijer, E.W.; Selinger, R.S.; Broer, D.J. Making waves in a photoactive polymer film. Nature 2017 , 546 , 632-636. [CrossRef]
- 68. Cunha, M.P.D.; Peeketi, A.R.; Ramgopal, A.; Annabattula, R.K.; Schenning, A.P.H.J. Light-driven continual oscillatory rocking of a polymer film. Chem. Open. 2020 , 9 , 1149-11525.
- 69. Xu, P.; Wu, H.; Dai, Y.; Li, K. Self-sustained chaotic floating of a liquid crystal elastomer balloon under steady illumination. Heliyon 2023 , 9 , e14447. [CrossRef]
- 70. Kim, Y.; Berg, J.; Crosby, A.J. Autonomous snapping and jumping polymer gels. Nat. Mater. 2021 , 20 , 1695-1701. [CrossRef] [PubMed]
- 71. Dawson, N.J.; Kuzyk, M.G.; Neal, J.; Luchette, P.; Palffy-Muhoray, P. Cascading of liquid crystal elastomer photomechanical optical devices. Opt. Commun. 2011 , 284 , 991-993. [CrossRef]
- 72. Zhao, D.; Liu, Y. Photomechanical vibration energy harvesting based on liquid crystal elastomer cantilever. Smart Mater. Struct. 2019 , 28 , 075017. [CrossRef]
- 73. Zhao, D.; Liu, Y. Effects of director rotation relaxation on viscoelastic wave dispersion in nematic elastomer beams. Math. Mech. Solids 2019 , 24 , 1103-1115. [CrossRef]
- 74. Ichimura, K.; Morino, S.; Akiyama, H. Three-dimensional orientational control of molecules by slantwise photoirradiation. Appl. Phys. Lett. 1998 , 73 , 921-923. [CrossRef]
- 75. Nagele, T.; Hoche, R.; Zinth, W.; Wachtveitl, J. Femtosecond photoisomerization of cisazobenzene. Phys. Rev. Lett. 1997 , 272 , 489-495.
- 76. Finkelmann, H.; Nishikawa, E.; Pereira, G.G.; Warner, M. A new opto-mechanical effect in solids. Phys. Rev. Lett. 2001 , 87 , 015501. [CrossRef]
- 77. Yu, Y.; Nakano, M.; Ikeda, T. Photomechanics: Directed bending of a polymer film by light-miniaturizing a simple photomechanical system could expand its range of applications. Nature 2003 , 425 , 145. [CrossRef]

- 78. Serak, S.V.; Tabiryan, N.V.; Vergara, R.; White, T.J.; Vaia, R.; Bunning, T. Liquid crystalline polymer cantilever oscillators fueled by light. Soft Matter 2010 , 6 , 779-783. [CrossRef]
- 79. Braun, L.B.; Hessberger, T.; Pütz, E.; Müller, C.; Giesselmann, F.; Serra, C.A.; Zentel, R. Actuating thermo- and photo-responsive tubes from liquid crystalline elastomers. J. Mater. Chem. C 2018 , 6 , 9093-9101. [CrossRef]
- 80. Camacho, L.M.; Finkelmann, H.; Palffy, M.P.; Shelley, M. Fast liquid-crystal elastomer swims into the dark. Nat. Mater. 2004 , 5 , 307-310. [CrossRef]

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.