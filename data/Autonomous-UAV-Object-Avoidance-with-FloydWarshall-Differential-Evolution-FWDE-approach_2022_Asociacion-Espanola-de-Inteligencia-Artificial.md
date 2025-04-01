<!-- image -->

## INTELIGENCIA ARTIFICIAL

http://journal.iberamia.org/

## Autonomous UAV Object Avoidance with Floyd-Warshall Differential Evolution (FWDE) approach

Guruprasad Y K , Nageswara Guptha M Sri Venkateshwara College of engineering, Bengaluru, India, 562154. guruprasadyk@gmail.com

Abstract. Unmanned Aerial Vehicles (UAVs) are recently focused significant research attention on commercial to  military  industries.  Due  to  its  wide  range  of  applications  such  as  traffic  monitoring,  surveillance,  aerial photography, and rescue mission, many research studies were conducted related to UAV development. UAVs are commonly called 'drones' used to suit dull, dangerous, and dirty missions that can be suited by manned aircraft. UAVs  can  be  controlled  either  remotely  or  using  automation  approaches  so  that  they  can  be  traveled  into predefined paths. To make an autonomous UAV, the most complex issue that is faced by UAVs is obstacle/object avoidance. Obstacle detection and avoidance are important for UAVs, and it is the complex problem to solve due to the payload restriction. This will limit the sensor count mounted on the vehicle. A radar was used to find the distance  between  the  object  and  the  vehicle.  This  can  help  to  detect  and  track  the  moving  objects'  speed  and direction  toward  the  vehicle.  This  paper  considered  the  object  avoidance  problem  as  a  path-planning  problem. There  were  many  path  planning  methods  related  to  UAVs  that  formulate  path  planning  as  an  optimization problem to avoid obstacles. With this consideration, this paper proposed an efficient and optimal approach called the  Floyd  Warshall-  Differential  evolution  (FWDE)  approach  to  detect  the  frontal  obstacles  of  UAVs.  Finally, statistical  analysis  of  the  simulated  environment  reveals  that  the  proposed  evolutionary  method  can  efficiently avoid both static and dynamic objects for UAVs. This efficient avoidance algorithm for UAVs can experiment with  a  simulation  environment  with  three  kinds  of  scenarios  having  different  numbers  of  cells.  The  obtained accuracy and recall value of the proposed system is 95.21% and 91.56%.

Keywords : Unmanned Aerial Vehicles (UAV), Drones, Evolutionary, Differential Evolution, Genetic Algorithm, Floyd warshall, Object Avoidance.

## 1 Introduction

Unmanned Aerial Vehicles (UAVs) becomes the recent research focus from the civilian and military fields due to their terrific advantages including flexibility, strong mobility, good concealment, and lightweight [1]. Because of the wide range of applications such as traffic monitoring, surveillance, aerial photography, and rescue missions, many research studies on UAV development are done [2]. The growth of the applications of UAV technologies changes many industries' development direction and also brings huge outcomes in economic and market benefits [3].  One  of  the  major  issues  of  UAVs  with  autonomous  motion  is  to  ensure  the  aircraft  can  explore  space efficiently  with  the  avoidance  of  collision  of  objects  in  a  dynamic  environment.  With  these  complications  of aircraft mission and usage scenarios, there is a need for technologies related to autonomous flight capabilities with intelligent UAVs and autonomous obstacle avoidance for UAVs [4].  The sudden improvement of UAVs in the commercial  application  of  larger  scenarios  will  increase  the  requirement  for  safe  and  reliable  approaches  for handling UAVs as efficiently [5-7]. Since UAVs were important for sensing technologies development such as thermal, hyperspectral, and multispectral they can change society with the creation of innovative applications and solutions [8-13]. The aircraft obstacle avoidance approaches are divided into two categories:

- I. This method's major goal is to convert the object avoidance problem into a path-planning problem [14]. With the advancement of UAV research, new path-planning systems have been developed, each with its own set of benefits and drawbacks. This algorithm includes graph theory-based Voronoi diagram [15],  field  theory-based  artificial  potential  field  approach  [16],  sampling  theory-based  RRT  [17], heuristic  information-based  A*  algorithm  [18],  swarm  intelligence-based  optimization  approaches [19-21], Graph based approaches not suited well for larger environments.
- II. Second category is related to the geometric relationship-based approaches for obstacle avoidance based on relative distance [25], angle [26], speed [27,28], and other related information [29] of aircraft and collisions.  Compared to the first  method related to path planning-based object avoidance, With the use of onboard sensors data from the scenario that comprises detection and avoidance, this method can avoid dynamic obstructions in the path.

This research work proposed a path planning-based dynamic object avoidance system. Aircraft path planning is  a  type  of  UAV  operation  that  generates  the  best  aircraft  path  from  point  A  to  point  B.  The  route  planning approaches  for  UAVs  can  formulate  the  path  planning  problem  as  an  optimization  problem  by  navigating  the UAV in three dimensions  with obstacles. To solve this problem, two groups of algorithms are  used. They are heuristic  and  non-heuristic  methods.  Heuristic  methods  are  providing  the  optimal  solution  with  efficient computation time. Non-heuristic methods provide the optimal solution with expensive computational time and use mathematical  principles.  The  path  planning  problem  is  solved  from  break  down  the  detected  area  into computational  domains  with  the  help  of  technologies  including  tessellation  or  decomposition  of  matrix  or combination  of  two.  After  the  path  generation,  the  UAV  can  travel  that  path  with  the  smoothen  process  [30]. Differential evolution is a population-based evolutionary method that is frequently utilized in UAV path planning due to  its  real-world  application  optimization  efficiency.  It  is  also  employed  in  non-linear  and  non-differential optimization problems. Due to its good convergence capabilities, DE is also employed in a variety of applications [31]. The contribution of this paper is as follows:

- · Initially, object models are built in the aircraft waypoint. There are three kinds of object models have been constructed such as square, cylinder, circle, and hemisphere-based objects.
- · The detected objects avoided in the aircraft path using the proposed path planning approach called the Floyd-Warshall method enhanced with the evolutionary algorithm called differential evolution.
- · The  proposed  FW-DE-based  path  planning  approach  finds  the  aircraft  path  with  the  waypoints without  obstacles  and  provides  the  UAV  with  safe  travel  from  the  origin  to  the  destination.  This evolutionary-based  enhancement  will  make  sure  low  computational  complexity,  flexibility,  strong searching ability, and improved robustness.

The simulation results of the proposed UAV object avoidance system show efficient results with minimum computation time and error in avoiding the obstacles in the flight path.

The remaining section of this paper is as follows: Section 2 discusses about the literature related to UAV path planning  and  object  avoidance.  Section  3  introduced  the  proposed  evolutionary-based  algorithm  for  object avoidance.  Section  4  simulated  the  environment  to  implement  a  proposed  system  and  discussed  the  evaluated results. Section 5 concludes the proposed work with future work.

## 2 Related works

This section discussed the works of literature related to obstacle avoidance and path planning for UAVs.  In terms of optimal solutions with reduced computation time, papers [14] and [32] compared the path-planning approaches in various scenarios and object layouts. They conclude that in terms of optimality, the path-planning approaches often conflict with each other. Sasongko et al., [27] developed an obstacle avoidance approach by calculating a group of waypoints to avoid the obstacles according to the obstacle model and UAV speed vector.

Al-Kaff et al. [28] devised an avoidance strategy that involved tracking a group of obstacle feature points in the flight  boundary  and  determining  the  link  between  aircraft  and  obstacle  coordinates.  Based  on  the  aircraft's forward speed and the difference between the obstacle and the vehicle, Zheng et al. [25] designed a fuzzy rulebased avoidance system. For UAV path planning, BesadaPortar [33] compared evolutionary methods. The control parameter for those evolutionary algorithms is not discussed in detail in this study.

By discovering the region of an item, Levente Kovacs et al. [34] devised a deconvolution approach to build a feature  map  called  D-map.  The  obstacle  is  captured  using  the  monocular  camera  with  less  collision  ratio.  The method used in this paper can be used in surveillance, navigation system, and odometry. Jacob engel et al., [35] discussed  UAV  navigation  in  GPS  (Global  Positioning  System)  based  surroundings.  This  system  is  based quadcopter  with  a  SLAM  approach,  Extended  Kalman  filter  for  sensor  fusing.  This  system  can  be  helpful  for

outdoor surroundings having a location accuracy of 18 cm and for indoor surroundings with a position accuracy of 4.9cm. It provides navigation estimation accurately.

Drone  collision  avoidance  algorithm  developed  by  Omid  esrafilian  et  al.,  [36].  (Aerial  Quadrotor).  The  front camera records video feeds, and the Drone's data navigation is communicated to the ground station via wireless networks.  SLAM  (Simultaneously  localization  and  mapping)  was  utilized  for  navigation  and  mapping.  To generate a 3D map, the data is processed using an Oriented fast and rotate brief (ORB). Using linear filtering, the monocular  SLAM  scaling  parameter  is  computed.  Roghair  et  al.,2021  [37]  proposed  a  deep  reinforcement algorithm  called  Deep  Q  network  for  UAV  object  avoidance.  UAV  exploration  of  obstacle  avoidance  was improved using two methods a convergence-based and a guidance-based approach which is implemented in the 3D simulation environment.  Compared to state of art methods, this secured two-fold improvement in avoiding UAV obstacles.

Wang et  al.,  2020  [38]  developed  deep-learning-based  object  detection,  RGB-D  information  fusion,  and  Task Control systems (TCS) for UAV obstacle avoidance. The simulation results show the detection accuracy of CNN as  75.4%  and  the  processing  time  of  the  single  image  is  53.33ms  and  it  depends  on  the  distance  between  the camera and the object. The outcome of this experiment indicates that the proposed system autonomously performs the  obstacle  avoidance  policy  and  explores  the  minimum  distance  flight  path  according  to  RGB-D  fusion information.

Guo et al., 2021 [39] proposed a circular arc trajectories method to avoid obstacles in UAVs. Using the onboard system,  the  obstacles  that  are  irregular  are  detected.  The  circular  arc  trajectory  for  obstacle  avoidance  was generated using convex bodies. The suggested system can avoid both static and dynamic impediments in the route of the UAV, according to numerical simulation findings. Radmanesh et al., 2018 [40] did a comprehensive survey with the comparison of existing UAV path planning algorithms for heuristic and non-heuristic methods. To test the performance of the UAV path planning method, three kinds of obstacle layout has been used. They concluded that the Genetic algorithm secured low sensitivity to time and MSLAP secured the fastest solution.

Lee et al., 2021 [41] developed a deep learning-based monocular obstacle avoidance approach for UAV-based tree plantations  using  Faster  Region-based  Convolutional  Neural  Network  (Faster  R-CNN).  Faster  RCNN  has  been used here to train tree trunk detection. To avoid collision with trees, the control strategy is used. This can be used to travel the UAV in the safest area. The simulation has experimented with 11 flights in real tree plantations in two various locations. An evaluated result proves that the proposed system is accurate and robust.

Pedro et al., 2021 [42] proposed neural network pipelines and flow clustering-based collision avoidance on UAVs. This  deep  learning-based  model  is  incorporated  for  real-time  dynamic  obstacle  avoidance  using  off-the-shelf commercial  vision  sensors.  A  video  dataset  was  created  and  made  available.  Transfer  learning  also  tested  and obtained positive results on computational processing and consumption of power. Yasin et al., 2020 [43] reviewed about the collision avoidance approaches used in UAVs. Various collision avoidance methods are explained with a comparative study based on different technical and scenario aspects. They also discussed about the sensors that may be used for efficient collision avoidance on UAVs. However, the reviewed object avoidance approaches are not  applicable  to  small  aerial  vehicles  due  to  the  cost,  weight,  and  energy  consumption  issues.  Most  UAV avoidance  systems  can  support  only  static  objects.  To  overcome  these  issues,  the  proposed  evolutionary algorithm-based approach has been developed to support a robust object avoidance system that can support static and dynamic objects.  In another study, UAV flight path planning was made to take into account how the particle swarm  may  be  made  to  avoid  obstacles.  The  use  of  swarm  dynamics  improves  optimization  difficulties.  By explaining  avoiding  obstacles  and  modifying  course  planning  for  UAVs,  this  is  meant.  To  avoid  both  static impediments,  the  idea  of  concurrent  restructuring  has  been  incorporated  into  the  path  design  process.  This optimization method seeks to save processing time and find the shortest path possible during path planning [59].

## 3 Proposed Methodology

This  paper  aimed  to  propose  an  object  avoidance  approach  for  real-time  autonomous  UAVs  based  on  an evolutionary algorithm according to find the best path between UAV and object through object modeling. The overall schematic of the proposed system is shown in Fig 1. The object model is built with a waypoint path. Once the object model is built, the objects are detected. Detected objects are avoided using the proposed Floyd warshall enhanced  with  an  optimization  algorithm  called  the  Differential  Evolution  approach.  Using  this  approach,  the shortest path between the origin and destination is found without obstacles. Once the path has been found without object  then  waypoint  gets  tracked  for  movement.  Or  else  the  objects  are  avoided  by  executing  the  object avoidance algorithm again. Once the waypoint path tracking ends the UAV also stopped.

Figure 1: Proposed UAV guidance architecture

<!-- image -->

## 3.1 Mathematical modelling of Object avoidance

## 3.1.1Object modelling

When  the  UAV  is  flying,  there  are  numerous  potential  things  on  the  path,  such  as  buildings,  trees,  and mountains. It's difficult to handle this irregular object directly, and the things recognized by the onboard sensors aren't  complete.  The complexity and efficiency of the object avoidance strategy  will be harmed if  you pay too much attention to finding the object shapes. Objects have the most round, square, and cylinder shapes based on the sampling sites observed by aircraft. For square objects, the location and sectors are classified and for a cylindrical object, the centre and radius give the objects information.

## (i) Square Objects

From the laser scanning radar, one or two sides of the square objects can be seen at the same time. If one side of the object gets detected, then the object is located in one sector boundary. Vertical length is calculated by the shortest  distance  from  the  UAV's  current  position  to  the  object  side.  The  remaining  two  sectors'  distance  is declared as infinity.  Figure 2 shows the square object detection with one boundary and two boundaries.

Figure 2: Square Object detection with shortest distance solution

<!-- image -->

When two  boundaries  of  a  square  object  are  in  the  same  sector,  the  distance  between  the  two  boundaries endpoints and UAV position are compared by the sensor. The minimum distance is considered as output. If there is any intersection between sectors and object boundary, need to find the distance between the terminal point and UAV's current position of the sector with the intersection point. The value with less value is considered.

## (ii) Circle objects

The circle objects with the sampling points are fitted using fitting algorithm such as least square method. For an object in circle shape, the radius r is calculated as in Equation (1) with the centers [Ox, Oy] T of an object as in Equation (2)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Where, ( , i=1,2,…n - convex hull of the sampling point , id - index value of Equation (1). Thus, the way the object in a circle shape is fitted and cover key parts or whole parts of the object. This will make the object avoidance algorithm easier to use. In certain circumstances, the UAV detects object models that are greater than the distance between the UAV and the item, while in others, the system is unable to capture the entire object or a crucial part of it due to its limitations. These cases are avoided with multiple circles have been used for larger objects as shown in Figure 3.

Figure 3: Object model of circle shape (a) simple circle object (b) complex circle object (iii) Cylinder shape objects

<!-- image -->

It is possible in some situations that an object has been modelled with other convex bodies such as cylinder, cone,  hemisphere  and  circular  table  based  on  detection  system.  The  computation  for  this  kind  of  objects  is expressed as in Equation (3) [39].

<!-- formula-not-decoded -->

Where, (x,y,z) - arbitrary points of the object, ( - coordinates of object center point, (p,q,r,l,m and n ) - constant of shape and size of the object model. Figure 4 represents the various kinds of convex bodies of objects with indicates the inside, surface and outside of the object model sequentially. The object model's shape and size remain fixed. Figure 4 depicts the several types of convex bodies of objects

with , indicating the inside, surface, and exterior of the object model in order.

<!-- image -->

Figure 4: Various convex body of object models

<!-- image -->

Based on these object models, while UAV detect objects in its path simple objects are modelled with single convex  body  and  complex  objects  are  modelled  with  combination  of  various  convex  bodies.  This  model  is implemented  using  the  proposed  object  avoidance  approach  called  Floyd-Warshall  Differential  evolution algorithm, based on this best path is find without obstacles.

## 3.1.2 Description of the difficulty of Object avoidance

This model considered the surface and inside of the object sector as no-fly zone or threat zone that is . The problem of UAV object avoidance is described by how to keep UAV outside of no-fly zone during the travel.

Assume the  UAV  mission  as  M,  Mt  is  a  threatened  or  object  area  that  is and  Ms-  safety  area  that  is

.  The relationship between safety and threaten zone are declared as in Equation (4). The UAV waypoint path to target is expressed as in Equation (5).

<!-- formula-not-decoded -->

Where, m- number of objects, - UAV target path, - object avoid at stage i.

## 3.2 Proposed Floyd-Warshall Differential evolution (FWDE)object avoidance algorithm

The key idea of FWDE is transform the object avoidance problem as path palling problem based on the swarm searching behaviour of UAV towards object.  This approach is contrary to the standard path planning approach called potential field approach where continuous and differential, the FW use pre-declared discretized cells to find the path. FW can obtain shortest path using weighted graph where each cell has its own weight and cost. Rather than the traditional weighted graph associates cell cost or weight [44], FW associates negative and positive edge weights. Vertex of the graph represent environment physical space and edge represents the distance between two vertices. FW can solve all paths shortest problem (APSP) and can be suited for offline path planning and not good for  dynamic  path  planning  [45].  The  other  variance  of  FW  in  [46]  shows  robustness  performance  for  location problem. The main objective of FW is to minimize the Equation (6) for shortest path finding from vertex i to vertex j from the set 1,2,…p as the intermediate points. p is the possible points that an UAV can cover [47, 48].

## = (6)

To make FW as dynamic path planning approach, it has been optimized with evolutionary algorithm called Differential  Evolution  (DE).  This  FW  with  DE  provides  the  path  planning  of  UAV  as  efficient  from  initial  to target points which is connected using virtual x-axis. Based on the count of waypoint in UAV path, virtual x-axis is divided into intervals of same number and form virtual y axis at same interval. This proposed FW-DE approach can optimize the path planning and the computational time. DE was first proposed by Storn and Price [49]. There are  five  parameters  in  DE  approach.  They  are  maximum  generation  number,  length  of  waypoints,  weight (differential),  population  size  and  crossover.  While  increasing  the  generation  number,  the  solution  may  evolve.

This solution length will decide the system complexity and also weight, crossover and population size will change the  performance.  This  approach  can  decide  the  population  size,  crossover  and  differential  weight  with  FW  to optimize  the  parameters.  So  that,  UAV  can  move  in  a  safe  path  with  sufficient  energy  in  the  map.  At  each coordinate of waypoint, the UAV can also maintain 100 m distance from the ground. The standard cost function is defined in Equation (7)

<!-- formula-not-decoded -->

Where, W- number of waypoints and l- length of previous and current location of UAV. It is similar to Genetic algorithm  and  involves  the  steps  such  as  selection,  crossover  and  mutation  with  different  sequence.  The population initialization started with random individuals in the search space. This population goes to mutation and individual is generated as in Equation (8) [50-54].

<!-- formula-not-decoded -->

Where x  -  individual  in  the  population  h ϵ (1,  N),  g  -  number  of  iteration  or  generation,  N  -  size  of  the population  and  DW  -  differential  weight.  Based  on  the  probability  of  crossover,  not  all  the  individuals  in  the mutation  used  for  next  iteration.  Trial  individual  in  the  population  called is  produced  by  the  crossover operation with the condition stated in Equation (9)

<!-- formula-not-decoded -->

Where j=1,2,…D, - random value lies between 0 and 1 for jth particle of ith individual. For selection process,  this  trial  population  is  forwarded.  Compare  to  GA,  DE  selection  process  compares  trial  and  current population. Individual with lowest cost found in Equation (6) will replace the current population individual as in Equation (7). The process is repeated until termination condition met from mutation and selection.

<!-- formula-not-decoded -->

The algorithmic steps of FWDE is as follows.

## Algorithm: FWDE object avoidance

Input: Population initialization, maximum iteration (max).

Output: Best possible path for UAV without object

Step 1: while (t&lt;=max)

Step 1: for each vertex v in the graph do

Step 2: distance (v,v) ← 0

Step 3:

end

Step 4:  for p in the cells of map do

Step 5: for i in the cells of map do

Step 6:

for j in the cells of map do

Step 7:

if (dist(i,j) &gt;dist(i, p)+dist (p, j)) then

Step 8:

x= dist(i,j) ←dist( i,p)+dist(p,j)

Step 9:

end

Step 10:          end

```
Step 11:    end Step 12: end Step 13: Mutation using Equation (8) Step 15: Crossover using Equation (9) Step 16: Selection using Equation (10) Step 17: t=t+1 Step 18: end while
```

## 4 Results and Discussion

This  section  describes  about  the  evaluated  results  using  proposed  object  avoidance  algorithm  implemented using Matlab. This proposed approach used UAV-viewed dataset [55] for object detection for simulation of object avoidance. Based on the type of object models and number of waypoints the evaluation is carried and the results are discussed. The data collection contains 50 video sequence of 70250 frames with the frame rate of 30 frames per second. A GoPro3 camera sensor is installed in the aircraft to capture the action. The target UAV in every movie is varies with appearance and shape. The dataset is split in 80:20 as training and testing dataset. The sample and object detected video frames are shown in Fig 5.

Figure 5: Sample video frame (left) and detected objects (right)

<!-- image -->

Evaluation of proposed object avoidance approach is carried with three object models in terms of computation time and optimal solution. This comparative analysis will differ in terms of different kind of scenarios based on object shape and complexity. Fig 6 shows the optimal path of three objects using proposed algorithm. Each object layout experiences cell with different resolution and the scenario is Scenario 1 - 900 cells, Scenario 2 - 90,000 cells  and  Scenario  3  -  9000000  cells.  This  will  help  to  analyze  the  scalability  of  the  proposed  approach.  The proposed approach is executed at three times and average outcome is tabulated. The error values of this execution is computed using Equation (8) and worst case results for the algorithm is calculated based on this error value.

<!-- formula-not-decoded -->

Figure 6: Simulation illustration of UAC avoid objects using proposed FEDE with three object models 4.1 Object layout 1 (Square shape objects)

<!-- image -->

The algorithmic output of the first layout of square object layer is shown in Table 1 with the comparison to existing approaches such as Circular Arc Trajectory Geometric Avoidance (CTGA) [39], Floyd Warshall, fuzzy logic [25] based UAV object avoidance.  The maximum error obtained by Floyd Warshall algorithm compared to other approaches of 1.4% and time as 2.53seconds. The standard deviation (std) of proposed work is 0.0031. The proposed FWDE approach secured minimum error percentage of 0.0012% and avoids the objects with less time as 0.2341seconds. compared to other approaches, proposed model performance is superior to other approaches in terms  of  Error,  computation  time  and  standard  deviation.  This  demonstrates  that  the  proposed  system  is  more efficient than alternative methods. In Figure 7, the error value comparison of object layout 1 is illustrated. This graph illustrates that proposed FWDE secures minimum error for all the scenarios with different cells.

object layout 1

|                 | Scenario 1   | Scenario 1   | Scenario 1   | Scenario 2   | Scenario 2   | Scenario 2   | Scenario 3   | Scenario 3   | Scenario 3   |
|-----------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| Methods         | CT (s)       | Error  (%)   | Std          | CT (s)       | Error  (%)   | Std          | CT (s)       | Error  (%)   | Std          |
| CTGA            | 1.4301       | 0.912        | 0.035        | 7.5261       | 3.12         | 0.0453       | 1029.12      | 3.152        | 0.0461       |
| Floyd  Warshall | 2.5351       | 1.431        | 0.0367       | 11.8928      | 6.342        | 0.0426       | 5981.92 9    | 5.925        | 0.0418       |
| Fuzzy  logic    | 3.7124       | 0.9913       | 0.0389       | 8.2913       | 5.827        | 0.0371       | 3293.11      | 4.203        | 0.0397       |
| Propo sed  FWDE | 0.2341       | 0.0012       | 0.0031       | 6.0283       | 0.011        | 0.0034       | 541.92       | 0.0101       | 0.0035       |

Figure 7: Error value comparison of UAV object avoidance methods - object layout 1

<!-- image -->

## 4.2 Object Layout 2 (Cylinder shape objects)

The algorithmic output of the second layout of square object layer is shown in Table 2 with the comparison to existing approaches such as Circular Arc Trajectory Geometric Avoidance (CTGA) [39], Floyd Warshall, fuzzy logic [25] based UAV object avoidance. The maximum error obtained by Floyd Warshall algorithm compared to other approaches of 1.53% and time as 6.3352 seconds. The proposed FWDE approach secured minimum error percentage of 0.0002% and avoid the objects with less time as 0.4342seconds with reduced standard deviation. This  demonstrates  that  the  proposed  system  is  more  efficient  than  alternative  methods.  The  error  value comparison of object layout 2 is shown in Fig 8. This graph illustrates that proposed FWDE secures minimum error for all the scenarios with different cells.

Table 2: Object avoidance methods comparison in terms of computation time and error for object layout 2

|                 | Scenario 1   | Scenario 1   | Scenario 1   | Scenario 2   | Scenario 2   | Scenario 2   | Scenario 3   | Scenario 3   | Scenario 3   |
|-----------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| Method s        | CT (s)       | Error  (%)   | Std          | CT (s)       | Error  (%)   | Std          | CT (s)       | Error  (%)   | Std          |
| CTGA            | 4.6302       | 0.8122       | 0.0352       | 11.5211      | 5.11         | 0.0411       | 1221.11      | 4.112        | 0.0352       |
| Floyd  Warshall | 6.3352       | 1.533        | 0.0412       | 16.8921      | 7.342        | 0.0397       | 6982.92      | 5.181        | 0.0462       |
| Fuzzy logic     | 5.7114       | 1.2313       | 0.0356       | 10.2213      | 6.871        | 0.0381       | 5291.12      | 5.131        | 0.0472       |
| Proposed  FWDE  | 0.4342       | 0.0002       | 0.0025       | 8.0281       | 0.0012       | 0.00288      | 623.81       | 0.0111       | 0.0362       |

Figure 8:  Error value comparison of UAV object avoidance methods - object layout 2

<!-- image -->

## 4.3 Object Layout 3 (Circle, Hemisphere shape objects)

The algorithmic output of the third layout of square object layer is shown in Table 3 with the comparison to existing approaches such as Circular Arc Trajectory Geometric Avoidance (CTGA) [39], Floyd Warshall, fuzzy logic [25] based UAV object avoidance. The maximum error obtained by Floyd Warshall algorithm compared to other  approaches  of  1.23%  and  time  as  6.29seconds.  The  proposed  FWDE  approach  secured  minimum  error percentage of 0.0001% and avoids the objects with less time as 0.38121seconds and reduced standard deviation. This  demonstrates  that  the  proposed  system  is  more  efficient  than  alternative  methods.  The  error  value comparison of object layout 3 is shown in Fig 9. This graph illustrates that proposed FWDE secures minimum error for all the scenarios with different cells.

Table 3: Object avoidance methods comparison in terms of computation time and error for object layout 2

|                | Scenario 1   | Scenario 1   | Scenario 1   | Scenario 2   | Scenario 2   | Scenario 2   | Scenario 3   | Scenario 3   | Scenario 3   |
|----------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| Methods        | CT (s)       | Error (%)    | Std          | CT (s)       | Error (%)    | Std          | CT (s)       | Error (%)    | Std          |
| CTGA           | 4.1271       | 1.8211       | 0.042        | 11.1281      | 5.82         | 0.038        | 1212.131     | 4.152        | 0.037        |
| Floyd Warshall | 6.2912       | 1.2312       | 0.043        | 16.2631      | 6.231        | 0.037        | 6837.221     | 5.625        | 0.036        |
| Fuzzy logic    | 5.1121       | 1.4123       | 0.038        | 10.2121      | 5.311        | 0.032        | 5592.15      | 4.727        | 0.039        |
| Proposed FWDE  | 0.3812       | 0.0001       | 0.003        | 8.1271       | 0.0011       | 0.0028       | 589.287      | 0.00142      | 0.0028       |

Figure 9:  Error value comparison of UAV object avoidance methods - object layout 3

<!-- image -->

The  evaluated  results  using  various  object  avoidance  approaches  applied  on  three  object  layers  as  per  the simulation. While problem complexity increases, the computation time also increases [56]. In the existing studies, the algorithms such Floyd Warshall, fuzzy logic were consuming more time to find the object path while size of the problem increased [57]. With the implementation of evolutionary algorithms, the consuming time and error rate are decreased, and objects are avoided which helps the UAV to travel in safety path. The parameter setting of DE  also  plays  vital  role  to  find  the  objects  in  front  of  UAV.  The  optimal  parameter  of  DE  for  maximum generation of 1000 is shown in Table 4.

Table 4: Optimized parameter settings at various generation number

| Generation    |   200 |   400 |   600 |   800 |   1000 |
|---------------|-------|-------|-------|-------|--------|
| Population    | 34    | 36    | 38    | 39    |  40    |
| Weight        |  0.11 |  0.12 |  0.12 |  0.14 |   0.14 |
| Crossover (%) | 64    | 51    | 40    | 31    |  26    |

The evaluated computation cost and error of three object layouts after parameter settings is shown in Table 5 for scenario 1. The optimized parameter setting of the execution of proposed system will decrease the computation cost, error percentage and standard deviation.

Table 5: computation time and error comparison of three layouts for scenario after optimized parameter settings

|                | Object layout 1   | Object layout 1   | Object layout 1   | Object layout 2   | Object layout 2   | Object layout 2   | Object layout 3   | Object layout 3   | Object layout 3   |
|----------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
| Methods        | CT (s)            | Error  (%)        | Std               | CT (s)            | Error  (%)        | Std               | CT (s)            | Error  (%)        | Std               |
| CTGA           | 0.4311            | 0.6021            | 0.028             | 3.3102            | 0.621             | 0.0323            | 3.1722            | 1.8211            | 0.034             |
| Floyd Warshall | 1.5151            | 1.1311            | 0.0276            | 5.1316            | 1.033             | 0.0372            | 5.2122            | 1.2312            | 0.026             |
| Fuzzy logic    | 2.1124            | 0.8132            | 0.0341            | 4.6141            | 1.113             | 0.0289            | 4.1013            | 1.4123            | 0.032             |
| Proposed  FWDE | 0.1341            | 0.0001            | 0.00276           | 0.3121            | 0.0001            | 0.00312           | 0.2812            | 0.0001            | 0.0021            |

The accuracy and recall of avoiding the objects in the path of UAV is evaluated and the results are shown in Fig 10 using the Equations (9) and (10). True positives (TP) are a collection of successfully identified things, whereas false positives (FP) are a group of wrongly discovered objects [58].

<!-- formula-not-decoded -->

The set of items that the detector does not detect is referred to as false negatives (FN). The value of recall is then calculated by dividing the number of detected items (TP) by the total number of data set objects as follows:

<!-- formula-not-decoded -->

.

Figure 10: performance comparison of proposed vs existing approaches in terms of accuracy and recall

<!-- image -->

From the illustration of Fig 8, the proposed FWDE secures improved accuracy on avoiding the objects in the aircraft  path  compared  to  other  traditional  approaches.  FWDE  secures  the  accuracy  and  recall  of  95.21%  and 91.56%. Various the other approaches such as CTGA, Floyd Warshall and Fuzzy logic obtained 83.18%, 76.92% and 81.27% sequentially.

## 4.4 . Statistical Analysis

After analysing the performance of the proposed model, the statistical analysis of the proposed FWDE model is performed. Table 6 shows the Friedman Test results that shows the global ranking of the considered models. The proposed FWDE leads the ranking compared to other approaches. The p value of the Friedman test is less than 0.0001 and the null hypothesis are rejected.

Table 6: Friedman test ranking

| Methods        |   Rank |
|----------------|--------|
| CTGA           |   2.12 |
| Floyd Warshall |   3.62 |
| Fuzzy logic    |   3.87 |
| Proposed FWDE  |   1.02 |

Once, the statistical difference between the methods is verified, the Holm's post hoc analysis is performed. We set FWDE is the best method and compared it with the other approaches. The p value and Holm's adjusted α are

showed  in  Table  7.  From  these  values ,  the  null  hypotheses  are  rejected  and  the  p  value  is  smaller  than  α. Therefore,  it  stated  that  there  is  statistical  difference  between  the  proposed  and  existing  models.  The  proposed model obtained the best result for our experiments.

Table 7: Holm's Post hoc Analysis

| Methods        |      p |     z |   Holm  α |
|----------------|--------|-------|-----------|
| CTGA           | 0.0016 | 5.256 |    0.0346 |
| Floyd Warshall | 0.0019 | 6.287 |    0.0562 |
| Fuzzy logic    | 0.0018 | 7.291 |    0.0352 |
| Proposed FWDE  | 0.0001 | 8.253 |    0.01   |

Holms  analysis  is  performed  on  final  results  on  selected  paths  are  good  or  bad  over  each  other  path comparison. The raw value is assumed as p-value and selected with smallest value for adjustment. After adjusting the p-values, the number which is biggest is taken for consideration. In CTGA, Floyd warshall, fuzzy logic, post hoc  Holm  analysis,  the  selected  final  paths  are  compared,  p  adjustment  is  0.0016,  .0019,.0018  and  statistical analysis z is 5.25, 6.28,7.29, Holm values (probability of least 1 error rate) is 0.0346,0.0562,0.0352 which higher than proposed Holm value of 0.0100. This shows proposed path prediction obtains less error rate.

## 5 Conclusion

A novel autonomous object avoidance algorithm called Floyd Warshall with Differential Evolution (FW-DE) for UAVs has been proposed and discussed in this paper. Initially, the object model is derived based on the shape of objects  based  on  convex  bodies  such  as  circle,  square,  cylinder  and  more  shapes  of  the  object  detected.  The proposed algorithm is implemented with this object model that not only transforms the object avoidance as path planning  but  also  simplifies  the  avoidance  problem.  The  developed  model  is  suitable  for  static  and  dynamic objects  according  to  the  geometric  relationship  between  UAV  and  objects.  The  evolutionary  algorithm  can improve  the  performance  of  Floyd  warshall  avoidance  to  obtain  less  computation  time,  error  and  improved accuracy.  This  efficient  avoidance  algorithm  for  UAV  can  be  experimented  with  simulation  environment  with three kinds of scenarios having different number of cells. For object layout 1, the proposed algorithm secured the time  of  computation  as  0.2341s,  6.0283s  and  541.928s  for  scenario  1,  2  and  3.  It  is  suitable  for  practical engineering. Likewise, the proposed system is evaluated in object layer 2 and 3. The accuracy and recall value of proposed system is 95.21% and 91.56%. Our future work includes applying the simulation environment into real UAV tests.

.

## References

- [1] P.E. Hart, N.J. Nilsson, and B. Raphael. A formal basis for the heuristic determination of minimum cost paths . IEEE Trans. System Science and Cybernetics SSC-4 , 2:100-107, 1968.
- [2] Richard E. Korf. Iterative-deepening A*: an optimal admissible tree search. In Proc. of the IX Int. Joint Conf.. on Artificial Intelligence (IJCAI'85) , pages 1034-1036, 1985.
- [3] Tobias Oetiker, Hubert Partl, Irene Hyna, and Elisabeth Schlegl. The not so short introduction to LaTeX2e, 2008.
- [4] Judea Pearl. Heuristics. Addison-Wesley, Readin, Massachusetts, 1984.
- [5] V. Vovk. Competing with wild prediction rules, Machine Learning , 69:193--212, 2007. doi: 10.1007/s10994007-5021-y
- [1] S. K. Chaturvedi, R. Sekhar, S. Banerjee, and H. Kamal. Comparative review study of military and civilian unmanned aerial vehicles (UAVs). INCAS Bulletin , 11(3): 183-198, 2019.
- [2] Cayero  J,  Morcego  B,  Nejjari  F.  Modelling  and  adaptive  backstepping  control  for  TX-1570  UAV  path tracking. Aerospace Science and Technology . 39: 342-351,2014.

- [3] Y. L. Kang and Y. Xi. Development situation, trend and countermeasure of consumer-level UAV market in China . ITM Web of Conferences . 11:1-23, 2017.
- [4] Y. Lan, L. Wang, and Y. Zhang. Application and prospect on obstacle avoidance technology for agricultural UAV. Transactions of the Chinese Society of Agricultural Engineering . 4(9): 104-113, 2018.
- [5] Shakhatreh, H.; Sawalmeh, A.H.; Al-Fuqaha, A.; Dou, Z.; Almaita, E.; Khalil, I.; Othman, N.S.; Khreishah, A.;  Guizani,  M.  Unmanned  Aerial  Vehicles  (UAVs):  A  Survey  on  Civil  Applications  and  Key  Research Challenges. IEEE Access . 9:1-23, 2019.
- [6] Zhong, Y.; Hu, X.; Luo, C.; Wang, X.; Zhao, J.; Zhang, L. WHU-Hi: UAV-borne hyperspdectral with high spatial  resolution  (H2)  benchmark  datasets  and  classifier  for  precise  crop  identification  based  on  deep convolutional neural network with CRF. Remote Sens. Environ .16:1-5, 2020.
- [7] Meinen, B.U.; Robinson, D.T. Mapping erosion and deposition in an agricultural landscape: Optimization of UAV image acquisition schemes for SfM-MVS. Remote Sens. Environ. 2020.
- [8] Bhardwaj,  A.;  Sam,  L.;  Akanksha.;  Martín-Torres,  F.J.;  Kumar,  R.  UAVs  as  remote  sensing  platform  in glaciology: Present applications and future prospects. Remote Sens. Environ .  175: 196-204, 2016.
- [9]  Yao, H.; Qin, R.; Chen, X. Unmanned Aerial Vehicle for Remote Sensing Applications-A Review . Remote Sens . 11: 1443-1456, 2019.
- [10]  Gerhards,  M.;  Schlerf,  M.;  Mallick,  K.;  Udelhoven,  T.  Challenges  and  Future  Perspectives  of  Multi/Hyperspectral Thermal Infrared Remote Sensing for Crop Water-Stress Detection: A Review. Remote Sens . 11:1240-1253, 2019.
- [11] Messina, G.; Modica, G. Applications of UAV thermal imagery in precision agriculture: State of the art and future research outlook. Remote Sens . 12: 1491-1503,2021
- [12]  Gaffey,  C.;  Bhardwaj,  A.  Applications  of  unmanned  aerial  vehicles  in  cryosphere:  Latest  advances  and prospects. Remote Sens. 2020, 12, 948.
- [13] Pedro, D.; Matos-Carvalho, J.P.; Azevedo, F.; Sacoto-Martins, R.; Bernardo, L.; Campos, L.; Fonseca, J.M.; Mora, A. FFAU- Framework for Fully Autonomous UAVs. Remote Sens . 12:3533-3542,2020.
- [14]  D.  Agarwal  and  P.  S.  Bharti.  A  review  on  comparative  analysis  of  path  planning  and  collision  avoidance algorithms. International Journal of Mechanical and Mechatronics Engineering . 12(6), 608-624, 2018.
- [15] H. Tong, W. W. chao, H. C. qiang, and X. Y. bo. Path planning of UAV based on Voronoi diagram and DPSO. Procedia Engineering . 29:4198-4203, 2012.
- [16] Y. B. Chen, G. C. Luo, Y. S. Mei, J. Q. Yu, and X. L. Su. UAV path planning using artificial potential field method updated by optimal control theor . International Journal of Systems Science . 47(6),1407-1420, 2016.
- [17] A. Kaur and M. S. Prasad. Path planning of multiple unmanned aerial vehicles based on RRT algorithm. In Advances in Interdisciplinary Engineering , pages 725-732, Springer, 2019.
- [18] C. Zammit and E. V. Kampen. Comparison between A  and RRT algorithms for UAV path planning. ∗ in 2018 AIAA Guidance, Navigation, and Control Conference, pages 1-23, Kissimmee, Florida, 2018.
- [19]  S.  A.  Gautam  and  N.  Verma.  Path  planning  for  unmanned  aerial  vehicle  based  on  genetic  algorithm  &amp; artificial neural network in 3D. in 2014 International Conference on Data Mining and Intelligent Computing (ICDMIC) , pages 1-5, Delhi, India, 2014.
- [20]  J.  Chen,  F.  Ye,  and  T.  Jiang.  Path  planning  under  obstacle  avoidance  constraints  based  on  ant  colony optimization algorithm . in 2017 IEEE 17th International Conference on Communication Technology (ICCT) , pages 1434-1438, Chengdu, China, 2017.
- [21]  K.  Y.  Kok  and  P.  Rajendran.  Differential-evolution  control  parameter  optimization  for  unmanned  aerial vehicle path planning. PLoS ONE , 11(3), article e0150558, 2016.
- [22] Hrabar S. 3D path planning and stereo-based obstacle avoidance for rotorcraft UAVs. Intelligent Robots and Systems. 2008 IROS IEEE/RSJ International Conference on: IEEE. pages 807-814, 2008.

- [23] Lin Y, Saripalli S. Sense and avoid for Unmanned Aerial Vehicles using ADS-B. Robotics and Automation (ICRA) , 2015 IEEE International Conference on: IEEE . pages, 6402-6407, 2015.
- [24] Lin Y, Saripalli S. Path planning using 3D dubins curve for unmanned aerial vehicles. Unmanned Aircraft Systems (ICUAS), 2014 International Conference on: IEEE . pages 296-304, 2014
- [25] J. Zheng, B. Liu, Z. Meng, and Y. Zhou. Integrated real time obstacle avoidance algorithm based on fuzzy logic and L1 control algorithm for unmanned helicopter. in 2018 Chinese Control and Decision Conference (CCDC ), pages 1865-1870, Shenyang, China, 2018.
- [26]  Z.  Lin,  L.  Castano,  E.  Mortimer,  and  H.  Xu.  Fast  3D  collision  avoidance  algorithm  for  fixed  wing  UAS. Journal of Intelligent &amp; Robotic Systems , 97(4), pp. 577-604, 2020
- [27]  R.  A.  Sasongko,  S.  S.  Rawikara,  and  H.  J.  Tampubolon,  UAV  obstacle  avoidance  algorithm  based  on ellipsoid geometry. Journal of Intelligent &amp; Robotic Systems , 88(4):567-581, 2017.
- [28]  A.  al-Ka  ff,  F.  García,  D.  Martín,  A.  de  la  Escalera,  and  J.  Armingol.  Obstacle  detection  and  avoidance system based on monocular camera and size expansion algorithm for UAVs. Sensors , 17(5):1061 -1082, 2017
- [29]  C.  Goerzen,  Z.  Kong  and  B.  Mettler,  A  survey  of  motion  planning  algorithms  from  the  perspective  of autonomous UAV guidance. Journal of Intelligent and Robotic Systems . 57(4): 65-100, 2000.
- [30] Fu Y, Ding M, Zhou C, Hu H. Route planning for unmanned aerial vehicle (UAV) on the sea using hybrid differential  evolution  and  quantum-behaved  particle  swarm  optimization .,  IEEE  Transactions  on  Systems, Man, and Cybernetics: Systems . 43(6): 1451-1465, 2013.
- [31]  Fan  Q,  Yan  X.  Self-adaptive  differential  evolution  algorithm  with  discrete  mutation  control  parameters. Expert Systems with Applications . 42(3): 1551-1572, 2015.
- [32] M. Radmanesh, M. Kumar, P. H. Guentert, and M. Sarim. Overview of path-planning and obstacle avoidance algorithms for UAVs: a comparative study. Unmanned Systems .6(2): 95-118, 2018.
- [33]  Besada-Portas  E,  De  La  Torre  L,  Moreno  A,  Risco-Martín  JL.  On  the  performance  comparison  of multiobjective evolutionary UAV path planners. Information Sciences .  238: 111-125, 2013.
- [34] L. Kovács, 'Visual Monocular Obstacle Avoidance for Small Unmanned Vehicles . Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshop , pages 59-66, 2016.
- [35]  J.  Engel,  et  al.  Camera-Based  Navigation  of  a  Low-Cost  Quadrocopter .    Intelligent  Robots  and  Systems (IROS), IEEE/RSJ International Conference on IEEE , pages1-10, 2012.
- [36] O. Esrafilian and H. D. Taghirad. Autonomous Flight and Obstacle Avoidance of a Quadrotor by Monocular SLAM. in Robotics and Mechatronics (ICROM), 4th International Conference on IEEE , pages 240-245, 2016
- [37] Jeremy  Roghair,  KyungtaeKo,  Amir  Ehsan  NiarakiAsli,  and  Ali  Jannesari.  A  Vision  Based  Deep Reinforcement Learning Algorithm for UAV Obstacle Avoidance. Intelligent Systems and Applications . 294: 115-128,2021.
- [38]  Dashuai  Wang,  Wei  Li,  Xiaoguang  Liu,  Nan  Li,  Chunlong  Zhang,  UAV  environmental  perception  and autonomous  obstacle  avoidance:  A  deep  learning  and  depth  camera  combined  solution, Computers  and Electronics in Agriculture. 175:105523-105539,2020.
- [39]  JiandongGuo  ,    Chenyu  Liang,  Kang  Wang,  Biao  Sang,  and  Yulin  Wu.  Three-Dimensional  Autonomous Obstacle  Avoidance  Algorithm  for  UAV  Based  on  Circular  Arc  Trajectory. International  Journal  of Aerospace Engineering. 2021:1-13,2021.
- [40]  MohammadrezaRadmanesh, Manish Kumar, Paul H. Guentert, and Mohammad Sarim. Overview of PathPlanning and Obstacle Avoidance Algorithms for UAVs: A Comparative Study. Unmanned Systems . 6(2), 124, 2020.
- [41] Lee, H.Y., Ho, H.W. &amp; Zhou, Y. Deep Learning-based Monocular Obstacle Avoidance for Unmanned Aerial Vehicle Navigation in Tree Plantations . J Intell Robot Syst. 101(5), 1-21, 2021.
- [42] Pedro, D.; Matos-Carvalho, J.P.; Fonseca, J.M.; Mora. A. Collision Avoidance on Unmanned Aerial Vehicles Using  Deep  Neural  Networks  and  Clustering  Techniques  with  RGB  Cameras. Remote  Sens .13:2643-2653, 2019.

- [43] J. N. Yasin, S. A. S. Mohamed, M. Haghbayan, J. Heikkonen, H. Tenhunen and J. Plosila. Unmanned Aerial Vehicles (UAVs): Collision Avoidance Systems and Approaches. IEEE Access, 8:105139-105155, 2020.
- [44] K. Rosen, Discrete Mathematics and Its Applications, 7th edn. (McGraw-Hill Science, New York, 2011).
- [45] B. Banerjee, A. Abukmail and L. Kraemer, Advancing the layered approach to agent-based crowd simulation, in Proc. 22nd Workshop on Principles of Advanced and Distributed Simulation . pages 185-192,2008.
- [46] E. Melachrinoudis and M. E. Helander. A single facility location problem on a tree with unreliable edges, Networks .27(3): 219-237,1996.
- [47] S. Hougardy. The Floyd-Warshall algorithm on graphs with negative cycles, Inform. Proc. Lett . 110(8): 279281,2010.
- [48] T. M. Chan, More algorithms for all-pairs shortest paths in weighted graphs .  SIAM J. Comput . 39(5): 20752089, 2010.
- [49]  Storn  R,  Price  K.  Differential  Evolution-A  simple  and  efficient  adaptive  scheme  for  global  optimization over continuous spaces. Journal of Global Optimization. 11(4): 1-12,1995.
- [50] Le-Anh L, Nguyen-Thoi T, Ho-Huu V, Dang-Trung H, Bui-Xuan T. Static and frequency optimization of folded  laminated  composite  plates  using  an  adjusted  Differential  Evolution  algorithm  and  a  smoothed triangular plate element. Composite Structures. 127: 382-394,2015.
- [51] Gao L, Zhou Y, Li X, Pan Q, Yi W. Multi-objective optimization based reverse strategy with differential evolution algorithm for constrained optimization problems. Expert Systems with Applications. 2015; 42 (14): 5976-5987.
- [52] Yi W, Gao L, Li X, Zhou Y. A new differential evolution algorithm with a hybrid mutation operator and selfadapting control parameters for global optimization problems. Applied Intelligence . 42(4): 642-660,2015.
- [53] Torres  SP,  Castro  CA.  Specialized  differential  evolution  technique  to  solve  the  alternating  current  modelbased transmission expansion planning problem. International Journal of Electrical Power &amp; Energy Systems . 68: 243-251, 2015.
- [54] Roque C, Martins P. Differential evolution optimization for the analysis of composite plates with radial basis collocation meshless method. Composite Structures . 124: 317-326, 2015.
- [55]  Jing  Li,  Dong  Hye  Ye,  Timothy  Chung,  Mathias  Kolsch,  Juan  Wachs,  Charles  Bouman.  Multi-target detection  and  tracking  from  a  single  camera  in  Unmanned  Aerial  Vehicles  (UAVs)", 2016  IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS ), pages 4992-4997, 2016.
- [56] Q.-K. Pan, M. F. Tasgetiren and Y.-C. Liang. A discrete particle swarm optimization algorithm for the nowait flowshop scheduling problem. Comput. Oper. Res . 35(9):2807-2839,2008.
- [57]  M.  Radmanesh,  P.  H.  Guentert,  M.  Kumar  and  K.  Cohen,  Analytical  pde  based  trajectory  planning  for unmanned  air  vehicles  in  dynamic  hostile  environments, in  American  Control  Conf.  (ACC),  2017  (IEEE, 2017 ), pages 4248-4253, 2017.
- [58] RaduRădesc u and MihaelaDragu. Automatic Analysis of Potential Hazard Events Using Unmanned Aerial Vehicle. In11th International Conference on Electronics, Computers and Artificial Intelligence (ECAI). Pages 1-6 , 2019.
- [59]  Mobarez,  E.  N.,  Sarhan,  A.,  &amp;Ashry,  M.  M.  Obstacle  avoidance  for  multi-UAV  path  planning  based  on particle swarm optimization. In IOP Conference Series: Materials Science and Engineering . Pages 1-6, 2021.