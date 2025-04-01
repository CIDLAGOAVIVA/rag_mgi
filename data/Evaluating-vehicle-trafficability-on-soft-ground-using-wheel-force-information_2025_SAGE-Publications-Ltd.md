<!-- image -->

## Evaluating vehicle trafficability on soft ground using wheel force information

Mingming Liu 1,2 , Longlong Chen 3 and Yanxi Ren 2

## Abstract

In the areas of aerospace and military industry, wheeled vehicles are expected to have the ability of passing various ground surfaces, including lunar soil, sand, marsh, mud flat, etc. This makes vehicle trafficability on soft ground become a very hot research topic. There are very a few difficulties in the present research of vehicle trafficability on soft ground, such as obtaining wheel-ground interaction information, inaccurate identification of soil mechanical characteristics parameters, and single evaluation index. In this paper, a novel approach of evaluating the vehicle trafficability on soft ground using wheel force information is proposed. As parts of the proposed approach, the methods of obtaining wheel force information, identification of soil mechanical characteristics parameters and integated method of trafficability evaluation, are discussed in detail. The proposed approach was validated through a practical test.

## Keywords

Trafficability, wheel force, soil mechanical property parameters

Date received: 25 February 2023; accepted: 30 April 2023

## Introduction

In recent years, with the rapid progress of vehicle technology and its applications in the areas of aerospace and military industry, wheeled vehicles are expected to run on various kinds of ground, such as lunar soil, sand, marsh, mud flat, etc. This makes the vehicle trafficability on soft ground, that is, the vehicle trafficability on soft ground without geometric features, become a hot research topic. In addition, if the possibility of vehicles passing through the soft ground can be predicted only by use of vehicle parameters and soft ground soil parameters, it will benefit the implementation of space programs or military activities, and avoid unnecessary losses as well.

efficiency proposed by Zhang Kejian. Thereinto, traction coefficient is widely accepted as a better index of evaluating the capability of vehicles passing soft ground, and then it has attracted more attention by scholars. Traction coefficient is equal to adhesive force minus resistance, divided by the vehicle weight, that is, pulling force exerted on the hook per weight of the vehicle. It is an integrated index, which reflects the soil strength reserveand vehicle power performance (e.g. acceleration, climbing and so on), and then is considered as a better index for evaluating vehicle trafficability. 4 The core of traction coefficient is the pulling force exerted on the hook.

The study of vehicle trafficability on soft ground involves two nonlinear systems, namely vehicle and soil. The interaction between the two systems is very complex, and there is no consensual theory or method in the research field. Especially, an effective evaluation and prediction system for vehicle trafficability has not been established. 1 At present, the representative evaluation index of vehicle trafficability on soft ground include: (i) traction coefficient, which is equal to the pulling force exerted on the hook per weight of the vehicle, proposed by Bekker; (ii) vehicle cone index (VCI) proposed by the US Corps of Engineers Waterway Test Station ; (iii) 2 average maximum pressure (MMP) proposed by the British Ministry of Defense ; iv) driving 3

In order to calculate the pulling force, Bekker proposed the classical semi-empirical model, which was based on the test, and then obtained the approximate equation of the relationship between tire and soil parameters by means of theoretical analysis and mathematical analysis. 5 Based on the classical semi-empirical

## Corresponding author:

Mingming Liu, School of Machinery and Vehicle, Beijing University of Technology, 100 Pingleyuan, Chaoyang District, Beijing 100124, China. Email: 1633778097@qq.com

<!-- image -->

Creative Commons CC BY: This article is distributed under the terms of the Creative Commons Attribution 4.0 License (https://creativecommons.org/licenses/by/4.0/) which permits any use, reproduction and distribution of the work without further permission provided the original work is attributed as specified on the SAGE and Open Access pages (https://us.sagepub.com/en-us/nam/ open-access-at-sage).

<!-- image -->

Measurement and Control 2025, Vol. 58(2) 147-154 /C211 The Author(s) 2024 Article reuse guidelines: sagepub.com/journals-permissions DOI: 10.1177/00202940231212949 journals.sagepub.com/home/mac

<!-- image -->

model, many researchers have developed various modified and improved models, including shear stress model, soil bearing property model, and sliding settlement in the semi-empirical model. 6-12 Most of the existing studies involve the estimation of pulling force exerted on the hook or the analysis of influence parameters, and validate the vehicle trafficability through practical test. Xue et al. 13 reviewed the methods of estimating in-orbit mechanics of the wheel soil and the identification methods for the mechanical parameters of the wheel soil model. Liang et al. 14 used three correction coefficients to obtain the accurate wheel lateral force model. Nagatani et al. 15 used the soil pressure and shear model to estimate the traction force and the vertical force. In recent years, with the development of numerical computation method and computer application technology, numerical simulation methods based on finite element analysis (FEM) and discrete element analysis (DEM) have been used to the nonlinear research of wheel and soil. 16 It used computer simulation software and combined soil mechanics theory, elastic-plastic theory and constitutive relationship theory to simulate the interaction process between soilwheel. This method could get more actual situation of reflecting the interaction process, and to some extent, solved the problem that cannot be analyzed by traditional mechanics.

There are three challenges by using the existing research results to solve the problem of vehicle trafficability on soft ground. First of all, the technology of obtaining wheel force information is not mature. As the direct result of the interaction between vehicle and road, the wheel force is of great significance for evaluating vehicle running condition, calculating traction coefficient, etc. Generally, in the existing methods, the wheel force is not directly obtained, but estimated by means of models. It has great effect on the accuracy of calculating key indicators of vehicle trafficability such as traction coefficient. Secondly, the parameters of soft ground mechanical characteristic, which are very important for the vehicle trafficability analysis, cannot be estimated in real time. Most of the existing monitoring methods are off-line measures, which usually use professional instruments. It cannot meet the requirements for real-time analysis of vehicle trafficability. Finally, the theoretical method of evaluating vehicle trafficability on soft ground only uses a single traction coefficient as the evaluation index. The correlation and integration of different evaluation indexes need to be further investigated to improve the accuracy of vehicle trafficability evaluation.

Based on the above analysis, this paper proposes an integrated method for unmanned cluster trafficability evaluation and migration based on wheel force information. Firstly, wheel force sensors are used to obtain the wheel force information. Secondly, based on the wheel force information, the accurate identification of the mechanical parameters of soft ground is realized. Finally, through establishing a multi-index layered trafficability evaluation method, the vehicles trafficability index on soft ground is obtained.

The remainder of this paper is organized as follows: Section 2 analyzes the method of obtaining wheel force in detail, and presents a decoupling scheme to improve the accuracy of obtaining wheel force; Section 3 proposes the method of identifying the soil mechanical properties parameters for soft ground based on wheel force information; Section 4 stated the construction method of vehicle trafficability index; Section 5 gives some concluding remarks.

## Technology for obtaining wheel force information

## Approach of obtaining wheel force

In recent years, the technology of obtaining wheel force information has made a rapid progress. Depending on the obtaining locations, it can be divided into three research branches, that is, on-tire, on-wheel and onaxle obtaining, as shown in Figure 1. On-tyre obtaining, which is called smart tire method, installs the sensors inside or on the surface of the tire, and thus can directly obtain data from the interaction point between the wheel and the road. 17 Considering the anisotropic deformation difference of tire material when running and the difficulties of in-tire sensor layout, the existing in-tire obtaining methods are only applied to intermittently obtaining quite a few parameters. Besides, the mechanical and spatial dynamic parameters of the remaining dimensions still need to be obtained through indirect estimation methods. On-wheel obtaining, which is called wheel force transducer method, directly designs the spoke as a multi-dimensional force sensor, which can obtain rich information (complete six mechanical dimensions) and has high accuracy. It is often used as the true value of wheel force in vehicle development and even aircraft landing gear testing. 18 Nevertheless, its design is very difficult, and its cost is extremely high. On-axle obtaining, which is called load sensing bearing method, embeds sensors into the bearing without modifying the wheel, and then its obtaining cost is the lowest one. 19 Nevertheless, the obtaining position is on-axle, which is far away from the touchpoint between the wheel and the road, and the movement of bearing balls can generate periodic interference, thus the accuracy and reliability of on-axle obtaining will be affected. 20

## Force-space coupling analysis

Different from the coupling interference of isomorphic data channels in traditional multi-dimensional perception, the research object of inter-dimensional coupling in the direct perception of wheel dynamics parameters is the force-space coupling effect between the mechanical dimension and the spatial dynamic dimension in the perception information. The reason for generating

Figure 1. Wheel information obtaining schemes: (a) intelligent wheel, (b) wheel force sensor, and (c) force bearing.

<!-- image -->

force-space coupling is that the perception and calculation of the wheel dynamics parameters need to be carried out in the wheel coordinate system and the body coordinate system respectively. Thus, the relative motion of the wheel and the body will directly affect the perception results in the wheel coordinate system. 21 The phenomenon of force-space coupling has attracted the attention of scholars in the early direct perception experiments. 22 With the enrichment of experimental methods and further investigation, force-space coupling, according to the formation reasons of coupling, is further divided into: (i) the attitude coupling generated by the relative attitude of the wheel coordinate system and the body coordinate system 23 ; and (ii) the inertial coupling generated by the relative maneuver between the coordinate systems, 24 as shown in Figure 2.

## Method of wheel force decoupling

Two contributions 25,26 stated the decoupling method of attitude coupling in detail, including the method of measuring wheel rotation angle, the method of calibrating initial value for the rotation angle of wheel-body

Figure 2. Coupling effect in obtaining wheel force information.

<!-- image -->

coordinate system, and the method of correcting angle measurement deviation during the wheel steering process. We can use the above method, and the sensor output in the wheel coordinate system and the wheel rotation angle as well, then a good attitude decoupling effect can be achieved, as shown in Figure 3.

The purpose of inertial decoupling is to estimate and compensate the inertial load deviation caused by the installation of wheel force obtaining equipment. The premise of decoupling is to mathematically describe the inertial coupling phenomenon, that is, to establish the deviation load ( D Finertial represents the force deviation caused by the inertial coupling, D Minertial represents the moment deviation caused by the inertial coupling), mass change ( D m represents the additional unsprung mass, D J represents the additional unsprung rotational inertia), and acceleration ( a represents the linear acceleration, \_ v represents the angular acceleration). The model is shown in equation (1).

<!-- formula-not-decoded -->

The software of multi-field coupling finite element analysis is used to establish wheel finite element models for pre- and post-installation of the wheel force obtaining equipment. Through changing the outer ring mass, as well as applying the acceleration in three directions ( a = ½ ax , ay , az /C138 T ) and angular acceleration ( \_ v = ½ \_ v x , \_ v y , \_ v z /C138 T ), we then can simulate the stress condition of the wheel force obtaining equipment at the motion field. The equivalent static inertia load of the motion field is determined by means of analyzing the strain beam deformation. Because the mass change in f inertial ( /C1 ) model can be measured offline, we mainly studies the coupling relationship between acceleration and inertial load. In order to facilitate description, here we take the coupling between linear acceleration and inertial force as an example to state the specific modeling method.

In the motion field only with linear acceleration, the output of single-dimensional inertial force channel is shown in equation (2).

Figure 3. Decoupling effect of wheel force and attitude.

<!-- image -->

Figure 4. The result actual effect of wheel force inertia decoupling.

<!-- image -->

<!-- formula-not-decoded -->

6

Where m ii ( ai ) means the sensor output generated by the force of the i -channel at the i -channel, and d ji ( aj ) means the coupled output generated by the force of the j -channel at the i -channel.

output of main channel inertia force m jj ( /C1 ),namely d ji aj /C0 /C1 = d ji ( m jj /C0 1 ( D Fj )). Given m ii /C1Þ ð and m jj ( /C1 ), we can adopt SVR method to train D Fi and D Fj . Then, the nonlinear error model d ji ( m jj /C0 1 ( D Fj )) can be obtained. Further, the linear coupling model can be modified. The result of wheel force inertia decoupling is shown in Figure 4.

Let main input channel m ii ( /C1 ) be a linear function, and coupled input channel d ji ( /C1 ) be a nonlinear function. m ii ( /C1 ) is solved by use of linear least squares regression. According to Lagrange mean value theorem, we then know when coupling error is \ 10%, the secondary coupling between sensor channels can be ignored (error is \ 1%). Therefore, aj in d ji ( aj ) can be replaced with the inverse function of the corresponding

## Approach of identifying soil mechanical properties parameters for soft ground

## Identifying soft ground type based on wheel force

The identification of soft ground type is helpful to approximate soil mechanical parameters, and lays foundation for accurately identifying mechanical parameters.

Figure 5. Different types of soft ground in the test.

<!-- image -->

Here we carried out a practical test, in which five types of soft ground are selected as the identification objects, including clay, sandy loam, sandy land, marsh land and plowed land, as shown in Figure 5.

In order to cover different conditions of vehicles sliding on the above five types of soft ground, and facilitate analyzing the factors of vehicle trafficability, we here design the following configuration scheme:

- (i) Test vehicles: select two types of vehicle, including Dongfeng Mengshi vehicles and Buick Sail vehicles.
- (ii) Driving behavior: include speedup, slowdown, and continuous driving behavior composed of speedupand slowdown. Speedup test is carried out through controlling accelerator of the vehicle, while slowdown test is conducted through controlling initial velocity and brake of the vehicle.
- (iii) Tire pressure: change the pressure of wheel tire in sequence from high to low, that is, 320, 300, 270, 240 and 210 kpa.
- (iv) Load: change load of the vehicle by means of loading/unloading standard test sandbag (50 kg/bag), then let the increment load be 200, 400, 600, 800 and 1000 kg respectively.
- (v) Soft ground: when testing on each kind of soft ground, we consider two situations, namely firstpass and multi-pass. In first-pass test, select the route that has never been chosen before, and recover the soft ground to the initial status after a certain number of tests. On the contrary, in multipass test, select the route that has been chosen before.

Through combining different configuration schemes on different road surfaces, we then carry out vehicle trafficability test. Each test for different configuration combination is carried out three times, and the data collected from each test is used to subsequent analysis and processing.

The common used methods of identifying soft ground type include: ground image features based approach, vibration signal of wheel/body based approach, and combination of the two approaches. In one of our previous studies, we found that the excitation of ground is transmitted to the body of vehicle through its wheels. Theoretically, the stress on the wheels can directly reflect the differences of various soft grounds. Therefore, we here use the integrated approach using wheel force features and ground image features to identifying soft ground type. Because of the mutual independence between wheel force feature and ground image feature, a dual-view classifier based on wheel force and ground image features is established using the collaborative training framework. Besides, wavelet support vector machine is utilized to training the classifier, as well as road identification and classification. The accuracy of identifying soft ground type is shown in Table 1. It can be concluded that the identification method based on wheel force can precisely identify soft ground type.

## Identifying soil mechanical characteristics parameters

After obtaining the soft ground type, we then can determine the initial value of soil parameters according to the empirical value. Next, using the theoretical models (i.e. the Bekker's soil pressure model and Janosi's soil shear mode), and taking the measured wheel states (including wheel force, slip rate, wheel settlement, etc.) as the feedback information, we establish the procedure of soil parameters estimation, as shown in Figure 6.

Table 1. Accuracy of identifying soft ground type.

| Soft ground type     | Clay   | Sandy loam   | Cultivated land   | Sand   | Swamp   |
|----------------------|--------|--------------|-------------------|--------|---------|
| Recognition accuracy | 97%    | 98%          | 97%               | 99%    | 97%     |

Figure 6. Procedure of soil parameters estimation.

<!-- image -->

Table 2. Results of Identifying soil mechanical property parameters of soft ground.

| Mechanical property parameters   | c (kPa)   | u ( /C176 )   | L (kN/m n+2 )   | n      | K (m)   |
|----------------------------------|-----------|---------------|-----------------|--------|---------|
| Initial values                   | 6.064     | 11.23         | 515.9           | 0.6825 | 0.02321 |
| Solution results                 | 6.880     | 15.50         | 588.2           | 0.9004 | 0.02614 |
| Error                            | 9.23%     | 10.71%        | 8.79%           | 5.92%  | 4.43%   |
| Solution time                    | 0.87 s    |               |                 |        |         |

In the above procedure, it adopts the optimization framework based on diversification strategy. Then, based on the exploration capability the global search algorithm and the mining capability of local search algorithm, the optimal value of soil parameters estimation can be obtained.

In order to verify the accuracy of soil parameters estimation, we get the real value through measuring soil parameters of the test ground by use of soil parameter measurement equipment (e.g. shear penetration tester, etc.). Then, the proposed estimation approach is compared to the traditional semi-empirical model of soil parameters estimation.

There are various types of soil parameters, including cohesion, internal friction angle, shear modulus of elasticity, friction modulus and settlement index. If all soil parameters are considered, it will not only reduce the speed of subsequent optimization, but also easily cause the instability of optimization results.

Through sensitivity analysis of soil parameters, this paper uses the method of parameters sensitivity theoretical analysis based on variance decomposition. Then, six parameters of soil characteristics, which play a major role, are determined, namely soil cohesion c , internal friction angle u , Shear modulus of elasticity K , cohesion modulus kc , friction modulus k u . Usually, kc and k u appear in the formula simultaneously. In order to reduce the complexity of the model and facilitate its resolution, since the wheel width is certain, the two parameters are combined to one joint parameter L , which is defined as L = kc = b + k u , b is the wheel width. Table 2 shows the results of identifying soil mechanical characteristic parameters in a certain test. It can be seen that the estimation accuracy of each parameter has been generally improved through optimization iteration.

## Method of v evaluating vehicle trafficability

## Identifying key indicators of vehicle trafficability

The traction on the hook and torque, as the indicators of vehicle trafficability, are the result of the interaction between vehicle and ground. Also, there is a coupling relationship between them, and their value is closely related to vehicle parameters, wheel status when driving and soil parameters. In this paper, the relationship between them is regarded as a complex nonlinear black box system, and can be resolved by regression algorithm.

There is very complex nonlinear relationship between vehicle and ground. Besides, the common used machine learning models, including support vector machine, multi-layer perceptron and Boosting algorithm, have limitations to model complex functions under limited samples and computing units, and have poor generalization ability for complex classification/ regression problems. Therefore, a deep neural network with deep nonlinear network structure is used to model the relationship between hook traction/torque and various influencing parameters, as shown in Figure 7. The estimation results are shown in Figure 8. It can be seen that this method can achieve more accurate identification of key trafficability indicators.

## Integrated evaluation system of vehicle trafficability

In order to effectively improve the evaluation and reliability of wheeled vehicles trafficability on soft ground, a fuzzy reasoning model with multi-rule, multi-input and single-output is utilized. The input of fuzzy reasoning the model include traction on the hook, as well as

Figure 7. Estimating hook traction/torque based on deep neural network.

<!-- image -->

physical parameters of the vehicle, that is, tire type, tire pressure, engine power, and soil parameters of the ground. Meanwhile, its output is the confidence of vehicle trafficability. Figure 9 shows the evaluation results, which is shown in GIS map.

## Conclusions and future research

In order to realize effective evaluation of vehicle trafficability on soft ground, this paper presented an approach of evaluating vehicle trafficability on soft ground using wheel force information. The proposed approach uses wheel force information as the main data source, and improves the accuracy of identifying soil mechanical properties parameters through classifying

Figure 9. Evaluation result of vehicle trafficability.

<!-- image -->

ground type. Then, the key indexes of vehicle trafficability are estimated. Finally, an integrated evaluation system of vehicle trafficability based on fuzzy reasoning model was established. The results of a real vehicle test showed that the proposed approach can effectively estimate vehicle trafficability on soft ground, and the passing probability map can guide path planning for the vehicle running on soft ground.

Aside from the topic in the paper, it must be pointed out that there are still several other topics for further research in the future as follows: First, it does not distinguish initial pressure and re-pressing well, and evaluating vehicle trafficability for re-pressing needs to be further investigated; Second, the results of vehicle trafficability evaluation are highly relevant to vehicles, namely it cannot be used to other vehicles, then it need further study on applying the research results for one type vehicle to others.

Figure 8. Estimation results of hook traction and torque.

<!-- image -->

## Declaration of conflicting interests

The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article.

## Funding

The author(s) received no financial support for the research, authorship, and/or publication of this article.

## ORCID iD

Mingming Liu https://orcid.org/0009-0009-2676-7553

## References

- 1. Pytka J. Modeling and system identification of a wheelsoil system. SAE Tech Pap Ser 2007-01-0482, 2007.
- 2. Mulhearn PJ. Methods of Obtaining Soil Strength Data for Modelling Vehicle Trafficability on Beaches. DSTO Aeronautical and Maritime Research Laboratory , 2001.
- 3. Priddy JD and Willoughby WE. Clarification of vehicle cone index with reference to mean maximum pressure. J Terramechanics 2006; 43: 85-96.
- 4. Wong JY. Terramechanics and off-road vehicle engineering: terrain behavior. Vehicle Design and Performance , 2013.
- 5. Bekker MG. Off-the-road locomotion. In: Research and Developments in Terramechanics . Ann Arbor: The University of Michigan Press, 1960, p. 220.
- 6. Janoshi Z and Hanamoto B. An Analysis of the Pull vs Slip Relationship for Track Laying Vehicles. Report #69 . Michigan: Land Locomotion Laboratory, 1961.
- 7. Reece AR. Problems of Soil-Vehile Mechanics. U.S. Army L.L.L, ATAC, No.8479 warren, Mich.,1966.
- 8. Wong JY. Computer Aided Analysis of the effects of design parameters on the performance of tracked vehicles. J Terramechanics 1986; 23: 95-124.
- 9. Azimi A, Kovecses J and Angeles J. Wheel-soil interaction model for Rover simulation and analysis using elastoplasticity theory. IEEE Trans Robot 2013; 29(5): 1271-1288.
- 10. Lyasko M. Slip sinkage effect in soil-vehicle Mechanics. J Terramechanics 2010; 47: 21-31.
- 11. Lee JH, Huang D, Johnson TH, et al. Slip-based experimental studies of a vehicle interacting with natural snowy terrain. J Terramechanics 2012; 49: 233-244.
- 12. Ding L, Gao HB, Deng ZQ, et al. Wheel Slip-Sinkage and its prediction model of lunar Rover. J Central South Univ Technol 2010; 17: 129-135.
- 13. Xue L, Dang Z, Chen B, et al. Zou Meng Progress and prospect of ground mechanics in the study of mechanical parameter estimation of. Martian Soil J Astronaut 2020; 41(02): 136-146.
- 14. Liang Z, Wang Y and Haibo G. Deng Zongquan Research on lateral force model of manned lunar rover wheels based on stress correction. J Mech Eng 2017; 53(9): 14-21.
- 15. Nagatani K, Ikeda A, Sato K, et al. Accurate Estimation of Drawbar Pull or Wheeled Mobile Robots Traversing Sandy Terrain Using Built-in Force Sensor Array Wheel[C]// Intelligent Robots and Systems, 2009. In: IEEE/RSJ International Conference on IROS 2009, IEEE , 2009.
- 16. Futoshi W and Yoshiaki T. Numerical simulation of tireground system considering soft ground characteristics. J Syst Des Dyn 2011; 5(8): 1650-1661.
- 17. Bastiaan J. Estimation of tyre forces using smart tyre sensors and artificial intelligence. Int J Veh Des 2018; 76(1/2/ 3/4): 110-139.
- 18. Pytka J, Jo ´ zwik J, Budzyn ´ ski P, et al. Wheel dynamometer system for aircraft landing gear testing. Measurement 2019; 148: 106918.
- 19. Kerst S, Shyrokau B and Holweg E. A model-based approach for the estimation of bearing forces and moments using outer ring deformation. IRE Trans Ind Electron 2020; 67(1): 461-470.
- 20. Madhusudhanan AK, Corno M and Holweg E. Vehicle sideslip estimator using load sensing bearings. Control Eng Pract 2016; 54: 46-57.
- 21. You SS. Effect of added mass of spindle wheel force transducer on vehicle dynamic response. SAE Technical Paper, 2012.
- 22. Falco D, Di Massa G, Pagano S, et al. Wheel Force Transducer for Shimmy Investigation. World Congress on Engineering. IAENG, London, 2015:1207-1212.
- 23. Matsumura R and Ishigami G. Visualization and analysis of wheel camber angle effect for slope traversability using an in-wheel camera. J Terramechanics 2021; 93: 1-10.
- 24. Agliullin T, Gubaidullin R, Sakhabutdinov A, et al. Addressed fiber bragg structures in load-sensing wheel hub bearings. Sensors 2020; 20(21): 6191.
- 25. Wang D, Lin G, Zhang WG, et al. The new method of initial calibration with the wheel force transducer. Sens Rev 2014; 34(1): 98-109.
- 26. Wang D, Lin G, Zhang W, et al. Angle error compensation in wheel force transducer. Measurement 2016; 77: 203-212.