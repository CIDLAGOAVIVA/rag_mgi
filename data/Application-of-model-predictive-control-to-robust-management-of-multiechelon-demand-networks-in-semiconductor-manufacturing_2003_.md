## Application of Model Predictive Control to Robust Management of Multiechelon Demand Networks in Semiconductor Manufacturing

Martin W. Braun ∗

Daniel E. Rivera †

Department of Chemical and Materials Engineering Control Systems Engineering Laboratory Arizona State University Tempe, AZ 85287-6006 daniel.rivera@asu.edu

## W. Matthew Carlyle ‡

Department of Industrial Engineering Arizona State University Tempe, AZ 85287-5906

## Karl G. Kempf

Decision Technologies Intel Corporation 5000 W. Chandler Boulevard Chandler, AZ 85226-3699

Model predictive control (MPC) is presented as a robust, flexible decision framework for dynamically managing inventories and satisfying customer demand in demand networks. In this paper, a formulation and the benefits of an MPC-based, control-oriented tactical inventory management system meaningful to the semiconductor industry are presented via two significant examples. The translation of available information in the supply chain problem into MPC variables is demonstrated with a single-product, two-node supply chain example. Simulations demonstrating the ability of a properly tuned MPC control system to maintain performance and robustness despite plant-model mismatch are shown. Insights gained from these simulations are used to formulate a partially decentralized MPC implementation for a six-node, two-product, three-echelon demand network problem developed by Intel Corporation. These simulations show that the demand network is well managed under conditions that involve simultaneous demand forecast inaccuracies and plant-model mismatch.

Keywords: Supply chain management, model predictive control, inventory control

## 1. Introduction

A supply chain (a.k.a. demand network or value web) consists of the interconnected components required to transform ideas and raw materials into delivered products and services. The entire structure is organized and managed with the goal of maintaining a high level of customer service while minimizing costs and maximizing revenues.

Companiesnolongercompeteagainstothercompanies.Instead, supply chains compete against other supply chains. The supply chain that gains market share does so by providing customers the right product, in the right amount, at the right time, for the right price, and at the right place [1, 2].

- ∗ Currently with Texas Instruments, Inc., 13570 N. Central Expressway, MS 3701, Dallas, TX 75243.
- † To whom all correspondence should be addressed.
- ‡ Currently with the Operations Research Department, Naval Postgraduate School, Monterey, CA 93943.

SIMULATION, Vol. 79, Issue 3, March 2003 139-156 ' 2003 The Society for Modeling and Simulation International

Among the most difficult of supply chains to optimize are those in the semiconductor industry. The combination of features that make semiconductor supply chains especially challenging includes long production lead times and large demand forecast errors combined with short product life cycles. Traditional planning methods applied in these circumstances lead to safety stock levels that cover as much as a year's worth of demand [3]. Recent literature suggests that billions of dollars can be achieved through improved management of semiconductor supply chains [2, 4].

|

|

|

|

|

|

In this paper, an approach using model predictive control (MPC) is proposed as a means to manage supply chains in general and those in the semiconductor industry in particular. It is proposed that the long and variable lead times and error-prone demand forecasts encountered in semiconductor supply chains can be robustly controlled using MPC. Since the semiconductor industry generates enormous wealth, direct experimentation involves untenable financial risk, and simulation is required. The MPC framework is shown to control qualitatively realistic simulations of semiconductor supply chains with safety stock levels well below levels suggested by industry heuristics. Control is demonstrated on a simple one-product, two-echelon, two-node problem, then scaled up for a more realistic two-product, three-echelon, six-node problem. Further upscaling is needed for larger semiconductor problems, but the initial results are very encouraging. In addition, MPC is regularly used in large-scale plantwide control applications in the petroleum refining and chemical manufacturing industries [5].

Recently, work using MPC has been found to provide an attractive alternative for inventory control [6] and supply chain management [7, 8]. These approaches are conceptually different and require less detailed knowledge in comparison with cost-optimal stochastic programming solutions that require many 'what-if' cases to be run and examined by highly skilled professionals [9]. Yet MPC offers the same flexibility in terms of the information sharing, network topology, and constraints that can be handled. The appeal of MPC for dynamic inventory management in supply chains can be summarized as follows: as an optimizer, MPC can minimize or maximize an objective function that represents a suitable measure for supply chain performance. As a controller, MPC can be tuned to achieve stability, robustness, and performance in the presence of plant-model mismatch, failures, and disturbances that affect the system.

The paper is organized as follows. Section 2 provides an overview of MPC. Section 3 presents a two-node demand network problem consisting of a factory and retailer to describe, simulate, and evaluate the fundamentals of the MPC-based inventory management decision tool. The translation of the available information in a supply chain setting to process control variables and the selection of proper tuning parameters are demonstrated to result in well-behaved management of a two-node supply chain. These insights are used in Section 4 to manage a six-node, two-product, three-echelon network that mimics the 'back-end' configuration of a semiconductor chain. The network is robustly managed using MPC under realistic information and modeling inaccuracies. Details of the simulation development and implementation environment are presented in Section 5. The paper concludes with a summary of the ideas presented and some extensions for future research (Section 6).

## 2. Model Predictive Control Decision Framework

MPC has long been the preferred algorithm for robust, multivariable control in the process industries, with implementations numbering in the thousands. The popularity of MPC stems from the relative ease with which it can be understood and its ability to handle input and output constraints [5]. The objective function of an MPC controller can be written as

<!-- formula-not-decoded -->

where Qe(/lscript) , Q ∆ u (/lscript) , and Qu(/lscript) represent penalty weights on the control error, control move size, and control signal, respectively. The move suppression weight Q ∆ u (/lscript) plays a particularly important role in providing robustness to the MPC control system, as will become evident in the examples and case studies presented in Sections 3 and 4. p and m represent the controller prediction and move horizons, respectively, while k represents time. r represents the setpoint trajectory, u is the control signal/manipulated variable, and ˆ y is the estimated output; the relationship of these variables to demand network information is summarized in Table 1 and further discussed in Section 3. The three terms in the MPC cost function penalize predicted setpoint tracking error, excess movement of the manipulated variable, and deviation of the manipulated variable from a target value, respectively.

The MPC optimization problem can be written

<!-- formula-not-decoded -->

s.t.

<!-- formula-not-decoded -->

The optimization problem is readily solved by standard quadratic programming (QP) algorithms. Only the first control element of the solution is implemented. At the next time step, the optimization problem is solved again with updated information from the system. This is referred to as the receding-horizon property of MPC, as illustrated in Figure 1. Note that the MPC controller explicitly uses a model relating the inputs and measured disturbances to the outputs.

Table 1. Variable mapping for model predictive control (MPC) controllers

| Process Control Variable                     | Demand Network Information                                         |
|----------------------------------------------|--------------------------------------------------------------------|
| Setpoints r                                  | Inventory targets of species A                                     |
| Outputs y                                    | Inventories of species A minus cumulative outstanding backorders   |
| Estimated outputs ˆ y                        | Forecasted inventories of species A                                |
| Measured disturbances u d                    | Demand or orders for species A being placed at the node            |
| Estimated future measured disturbances ˆ u d | Forecasted demand or orders for species A being placed at the node |
| Estimated inputs ˆ u                         | Forecasted orders for species A being placed at the upstream node  |
| Inputs u                                     | Orders for species A being placed at the upstream node             |

Figure 1. Model predictive control (MPC) receding-horizon philosophy

<!-- image -->

## 3. Single-Product, Two-Echelon, Two-Node Problem Analysis

In this section, a single-product, two-node demand network representing a factory and a retailer is used to establish the linkages between the inventory management problem and the process control one. The assignment of demand network variables to process control variables is summarized in Table 1. Figure 2 illustrates the material flows from the factory to the retailer and on to the customer. The dynamics of each node are simulated with a difference equation arising from the conservation of total mass where

<!-- formula-not-decoded -->

I A is the inventory of A S A , 1 is the incoming stream of A S A , 2 is the outgoing stream of A , Θ p represents the processing delay, and PA(k) is the material that has completed processing at time k of species A . Figure 3 provides a graphi-

<!-- formula-not-decoded -->

Figure 2. Two-node network material flows

<!-- image -->

Figure 3. Two-node network model predictive control (MPC) information flows

<!-- image -->

cal representation of the information transfer between the MPC controllers and nodes of the two-node system.

Current customer demand is fed directly to the retailer, and the retailer can immediately fill that demand that day. It is assumed that a demand forecast is known, although it may have bias or random error as dictated by the simulation conditions. The demand (measured disturbance) and demand forecasts (estimated future measured disturbances) are fed to the first echelon MPC controller. Using the current inventory (outputs) information from the retailer, the first echelon MPC controller decides what orders (inputs) for product A should be placed with the factory and what the order forecast (estimated inputs) will look like. This order forecast is shared with the second echelon MPC controller.

turbances (plus safety stock) for the first echelon controller. For the factory, the inventory targets are an exact replication (plus safety stock) of the estimated measured disturbances for the factory since there is no direct feed-through (i.e., orders placed today are only on backorder if not filled tomorrow).

The second echelon MPC controller uses the order forecast (now an estimated future measured disturbance) from the first echelon MPC controller and the inventory information (outputs) from the factory to decide on production starts (inputs) for the day. Both MPC controllers contain models that determine the effect that orders (measured disturbances) from downstream entities have on the future inventories (estimated outputs) in their node. This model also relates orders to the factory (inputs for the first echelon MPC controller) and production starts (inputs for the second echelon controller) to the inventory levels (outputs). The inventory targets (setpoint trajectories) are a forward time-shifted version of the estimated future measured dis-

From Figure 3, it is clear that each node entity has its ownMPCcontroller to manage inventory levels. Both controllers are developed with a slight modification of the interpretation of inventory. Namely, the net stock [10] is used as the measured output of the system. Net stock is the measured inventory at time k less the cumulative outstanding backorders at time k . Relying on net stock improves the performance of the network since the effect of backorders on the controlled variable is now recognized by the MPC controllers.

Figures 4 and 5 show the responses of the proposed MPC structure to a scenario in which the production leadtime in the factory and the shipping delay to the retailer are 2 and 0 time units, respectively. With no plant-model mismatch and in the absence of constraints on production and shipping quantities, there is no need to use move suppression. As shown in Figures 4 and 5, demand is perfectly satisfied with no backorders; inventory levels are systematically built up or diminished to meet demand.

The MPC control approach is then evaluated under conditions of plant-model mismatch. The production leadtime in the factory is actually 3 time units, while the factory

Figure 4. Retailer responses and metrics, two-node example, no move suppression, no plant-model mismatch

<!-- image -->

Figure 5. Factory responses and metrics, two-node example, no move suppression, no plant-model mismatch

<!-- image -->

MPC controller makes use of a model that assumes a production leadtime of 2 time units. The retailer MPC controller is implemented as if there exists no shipping delay between the factory and the retailer, but in the simulation, there is 1 time unit of delay. There is no production delay in the retailer for either simulation or controller. First, the controllers are implemented with no move suppression. The time series and metrics for the retailer and factory are shown in Figures 6 and 7, respectively. Inventory levels show wild fluctuations and increase to exorbitant levels; customer service could be better. Using move suppression values of 150 for both controllers, the system is stabilized, and the 1500 units of safety stock are sufficient to eliminate backorders, as shown in Figures 8 and 9.

## 4. Two-Product, Three-Echelon, Six-Node Problem Analysis

The performance and robustness of the MPC control systemarenowdemonstratedonasix-nodenetworksimulated using realistic plant-model mismatch, biased forecast error, and a realistic demand profile. These conditions were recommended for evaluation by Intel Corporation on a sixnode, two-product, three-echelon simulation. The simulation mimics the packaging, distribution, and retail sale of semiconductor products in each of the three echelons.

Figure 10 illustrates the interconnections of the material flows for the six-node Intel problem [11]. As noted in the diagram, transportation delays range from 2 to 4 days. The direct shipment routes each require 2 days. The crossshipment routes require 3 days between assembly/test and warehouse echelons. The cross-shipment routes require 4 days between warehouse and retailer echelons. In the warehouse and retailer nodes, material that enters the receiving dock does not show up in the inventory until the following day. The assembly/test nodes require an additional 10 days for processing.

For this demand network pattern, the transportation delays can be modeled in the same way as was done with the two-node supply chain. There are three new modeling entities to consider: factories, geographic warehouses, and retailers. Each has a different configuration of input and output flows. For the single-inflow, two-outflow factory, as shown in Figure 12, the material balances for each species can be written

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

with the constitutive relationships

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

As with the two-node problem, I represents inventory, S represents in and out stream values, Θ p represents processing delays, and PA(k) and PB(k) represent material that has completed processing at time k of species A and B , respectively. These material balances are subject to the following constraints:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

These constraints represent capacity limitations on inventory, shipping for stream 1, release rate from the factory, shipping for stream 2, and shipping for stream 3, respectively.

The next entity to consider is the two-inflow, twooutflow warehouse, as represented in Figure 13. The material balances of this system are a natural extension of the single-inflow, two-outflow material balance equations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

These material balances are subject to the following constraints:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

These constraints represent capacity limitations on inventory, shipping for stream 1, shipping for stream 2, total inflow rate, shipping for stream 3, shipping for stream 4, and release rate from the warehouse, respectively.

For the two-inflow, single-outflow retailer (Fig. 14), the material balances are written

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

These material balances are subject to the following constraints:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 6. Retailer responses and metrics, two-node example, no move suppression, with plant-model mismatch

<!-- image -->

Figure 7. Factory responses and metrics, two-node example, no move suppression, with plant-model mismatch

<!-- image -->

Figure 8. Retailer responses and metrics, two-node example, with move suppression and plant-model mismatch

<!-- image -->

Figure 9. Factory responses and metrics, two-node example, with move suppression and plant-model mismatch

<!-- image -->

Figure 10. Six-node Intel network material flow

<!-- image -->

Figure 11. Six-node Intel network information flow

<!-- image -->

Figure 14. Two-inflow, single-outflow retailer material streams

<!-- image -->

These constraints represent capacity limitations on inventory, shipping for stream 1, shipping for stream 2, total inflow rate, and shipping/release for stream 3 from the retailer, respectively.

Having investigated different facets of the demand network management problem with the two-node network, this insight can be applied to the six-node problem. Figure 11 illustrates the information flow between the three MPCcontrollers and the six nodes of the demand network. For this problem, one monolithic MPC controller would become computationally prohibitive. A fully decentralized structure (one controller for each node) would require intervention by an outer layer to manage the constraints due to the interconnections of the nodes, the release rate capacities, and the shipping capacities. Due to the nature of the constraints, a compromise can be made between the two strategies. Three controllers are used. Each controller handles the flow and composition decisions for each echelon, passing forecasted information to the upstream node and receiving forecasted information from the downstream node. By resolving the information flows in this manner, the solution is scalable yet still feasible for managing the constraints.

The MPC controllers for the warehouse and retailer echelons of the network have to be modified slightly to account for the cross-shipment routes that can occur between echelons. The problem inputs now number eight since there are two shipping lanes from each node, and each lane can transport either or both products. To handle the extra degrees of freedom this brings to the problem, the

penalties Qu for the cross-shipment routes are purposefully set high, so these routes are not favored in the cost function. This penalty also allows for a unique solution to the MPC problem.

Experience with the actual performance of assembly/ test nodes and the estimated lead times by facility personnel suggest that the facility personnel traditionally provide themselves a lead time buffer of 1 day. So, for example, if in reality the process takes 9 days to complete, a 10-day lead time estimate will be quoted to others in the organization. Thus, a 9-day actual/10-day estimate plant-model mismatch is adopted for both assembly/test facilities.

The sales and marketing personnel have been generally known to determine forecasts that are biased in an optimistic manner. As an example, the sales forecast for the next time period might be 11,000 units, when in fact the actual sales will be 10,000 units. To mimic this type of forecast bias, all demand forecasts passed to the retailer-level MPC controller are biased by + 1000 units.

Last, products have been observed to follow demand patterns that may be correlated at times and uncorrelated at other times. To mimic this type of behavior, the demand patterns for product A and product B follow correlated, deterministic steps up until time 110. The remainder of the time, the demand patterns remain uncorrelated. This behavior can be observed in Figure 15.

The experiment is run with a value of 300 for all move suppression parameters Q ∆ u , 0 for all penalties for values other than zero for direct shipment Qu , and a penalty of 100 for all penalties for values other than zero for crossshipments Qu . Table 2 holds the prediction horizons Np and control horizons Nu for all three MPC controllers. Safety stock is set at 5000 units per product, per node. All inventory control error weights Qe are left at 1. All entities use a 'pecking order' dispatch rule. The orders of warehouse 1, retailer 1, and customer 1 take precedence over the orders of the corresponding counterparts. Secondarily, orders for product A take precedence over orders for product B . Figures 16 and 17 demonstrate the performance of this approach with plots of inventories, demands, shipments, and factory starts.

At time 1, the retailer MPC controller adjusts orders and order forecasts to the upstream nodes to start bringing in more product since the demand forecast is now 11,000, even though the actual amounts being demanded are 10,000. Because of the move suppression, the increases in order amounts are less than 1000. The increase in orders is evident in the increase in direct shipments and crossshipments from the warehouse echelon. Soon the retailer MPC echelon realizes that the actual amount supplied to customers is not increasing, as suggested by the forecast, and the retailer MPC adjusts to account for the forecast error and reduce inventory.

In the first few time units, inventories in the factory echelon and warehouse echelon are drained below their target levels. The factory echelon MPC controller now observes the effects of the plant-model mismatch since the effects of changes in the starts show up sooner than expected. The inventory levels of the assembly/test nodes fluctuate, but the fluctuation remains at reasonable levels. No backorders take place throughout the entire experiment. This is rather impressive since the general rule of thumb practiced for this network requires a safety stock level equivalent to between two and four times the expected demand for the next time period (e.g., if tomorrow's demand is expected to be 10,000 units, safety stock held today may range from 20,000 to 40,000 units).

Note that the cross-shipments in this example are used whenever there are rapid changes in the order/demand forecasts. The MPC controllers make use of the crossshipments since the costs associated with the move suppression weightings of the direct shipments become comparatively large at these times. This may make sense not only from an optimization standpoint, but in a realistic setting, it may also allow nodes to hedge against uncertainties or disturbances in transportation links or nodes connected by the direct shipment lanes.

## 5. Simulation Details

All simulation runs reported were performed on a Pentium IV 1.33-GHz processor with 128 MB of memory. The runs were on the order of minutes for the two-node network and 14 hours for the six-node network for typical runs.

The simulations were constructed and run in a MATLAB 5.3/Simulink 3.0 environment. The work began by creating a library of Simulink blocks and accompanying S-functions for each of the representative types of nodes that might be used in the construction of a supply-demand network: factory, warehouse, retailer. Each library block was designed so that multiple blocks could be placed in the same Simulink model file with the material and information flows readily connected to form the network. Each node was designed with a Graphical User Interface (GUI) mask to allow for custom configuration of each node. Demandsourceblocksare constructed to read in deterministic or create stochastic demands. Blocks to determine forecasts from the stochastic demand source blocks and deterministic demand source blocks were included in the library. Finally, the MPC management blocks were constructed to allow for scalar and vector forecast inputs to accommodate real-time orders or real-time and future order forecasts. These blocks make use of the Optimization toolbox for MATLAB,andtheaccompanying GUI masks allow the user to readily modify all relevant optimization, constraint, and horizon length parameters. Every block constructed includes options for generating high-quality plots of the final results, as well as diagnostic plots at intermediate time steps in the simulation.

The MATLAB/Simulink simulation environment and the model library constructed allow for rapid redesign and configuration in a visual, object-oriented manner. The GUI

Figure 15. Demand profiles for products A and B , six-node Intel network

<!-- image -->

Table 2. Prediction and control horizons used in six-node controllers

| Parameter   |   Echelon #1 |   Echelon #2 |   Echelon #3 |
|-------------|--------------|--------------|--------------|
| Np          |           49 |           41 |           33 |
| Nu          |           42 |           34 |           12 |

masks not only serve for quick configuration, but variables can be directly put in place of static values to allow for scripting. Since MATLAB readily allows for a master script document to control the Simulink model file, a set of runs for a given design of experiments (DOE) can be readily scripted and executed with little need for user intervention. The myriad of subroutine toolboxes available for MATLAB allow for quick implementation of ideas to generate proof-of-concept results. Moreover, the powerful graphical tools of MATLAB can readily be accessed for plotting results from intermediate time steps in a simulation run, the summary results from a given run, or full-response surfaces from a given DOE.

Some of the drawbacks to the approach include the fact that MATLAB is commercial software and additional toolboxes are added at additional cost. The MATLAB language is interpretive, which slows down the performance compared to compiled language environments, but the Compiler toolbox can be used with modifications to the custom code. The Optimization toolbox routines are not streamlined and robust for MPC application; additional work to improve constraint handling and indeterminant solutions would be beneficial. Last, the simulation time could benefit substantially from a parallel processing approach, which could solve the MPC blocks in parallel, rather than in a sequential manner. This is not an existing feature of the MATLAB/Simulink environment.

## 6. Conclusions

As demonstrated throughout this paper, MPC offers the ability to develop decision policies that stabilize inventory in supply chains despite imperfect information regarding the system dynamics and inaccurate demand forecasts. The movesuppressiontermintheMPCcostfunctionrepresents a penalty on order changes; incorporating this term in the MPC optimization problem leads to increased robustness, which may not result from optimization schemes based on strictly cost-optimal approaches. This was demonstrated through simulations performed with the two-node supply chain. An MPC approach was shown to be flexible enoughtomanageasystemapproachingindustrial size and configuration-the six-node demand network proposed by Intel Corporation.

<!-- image -->

Factory 2 Product A Q

∆

50

100

150

Factory 2 Product B Q

u3=300

∆

200

u3=300

50

100

150

200

Warehouse 2 Product A Q

∆

250

u2=300

50

100

150

200

Warehouse 2 Product B Q

∆

250

u2=300

50

100

150

200

Retailer 2 Product A Q

∆

50

100

150

Retailer 2 Product B Q

250

u1=300

∆

50

100

150

200

u1=300

200

250

250

Time

Time

Units

Units

Units

Units

Units

Units

2

1.5

1

2

1.5

1

2

1.5

1

2

1.5

1

2

1.5

1

2

1.5

1

4

x 10

4

x 10

4

x 10

4

x 10

4

x 10

4

x 10

250

Figure 17. Material flows product A (dashed) and product B (solid). Demand: product A (dotted) and product B (dash-dot) and corresponding customer receipts product A (dashed) and product B (solid).

<!-- image -->

A natural extension of this work is to incorporate the demand management side of the organization. Sales and marketing functions serve to manipulate and predict demand forecasts, which may also be used to further maximize profits or minimize costs for the organization. By incorporating advertising and marketing models to predict sales volume as a function of advertising dollars spent, the supply chain management function and sales and marketing function may be better integrated.

## 7. Acknowledgment

Financial support from the National Science Foundation (NSF-DMI Award 0075682) and the Intel Research Council is gratefully acknowledged.

## 8. References

- [1] Bodington, C. E., and D. E. Shobrys. 1999. Optimize the supply chain. In Advanced process control and information systems for the process industries , edited by L. A. Kane, 236-40. Houston, TX: Gulf.
- [2] Kempf, K., K. Knutson, B. Armbruster, P. Babu, and B. Duarte. 2001. Fast accurate simulation of physical flows in demand networks. In Advanced simulation technologies conference , 111-16. Seattle, WA: Society for Computer Simulation International.
- [3] Lee, H. L., V . Padmanabhan, and S. Whang. 1997. The bullwhip effect in supply chains. Sloan Management Review 93-102.
- [4] PriceWaterhouseCoopers. 2000. Silicon 2000: Millennium semiconductor survey on supply chain management . Retrieved from http://www.ebusiness.pwcglobal.com/external/gen-reg.nsf/ semi?OpenForm&amp;Seq=1
- [5] García, C. E., D. M. Prett, and M. Morari. 1989. Model predictive control: Theory and practice-a survey. Automatica 25 (3): 33548.
- [6] Tzafestas, S., G. Kapsiotis, and E. Kyriannakis. 1997. Model-based

predictive control for generalized production planning problems. Computers in Industry 34 (2): 201-20.

- [7] Flores, M. E., D. E. Rivera, and V. Smith- Daniels. 2000. Managing supply chains using model predictive control. Paper presented at the AIChE 2000 annual meeting, November, Los Angeles.
- [8] Perea-Lopez, E., I. E. Grossman, and B. E. Ydstie. 2000. Application of mpc to decentralized dynamic models for supply chain management. Paper presented at the AIChE 2000 Annual Meeting, November, Los Angeles.
- [9] Kafoglis,C. C. 1999. Maximize competitive advantage with a supply chain vision. Hydrocarbon Processing 47-50.
- [10] Silver, E. A., D. F. Pyke, and R. Peterson. 1998. Inventory management and production planning and scheduling . New York: John Wiley.
- [11] Armbruster, D., R. Chidambaram, G. Godding, K. G. Kempf, and I. Katzorke. 2001. Modeling and analysis of decision flows in complex supply networks. In Proceedings of IV SIMPOI/POMS 2001 , Guaruja, Brazil, pp. 1106-14.

Martin W. Braun is a member of the technical staff at the Kilby Center of Texas Instruments, Inc., Dallas, Texas.

Daniel E. Rivera is an associate professor in the Department of Chemical and Materials Engineering, Control Systems Engineering Laboratory, Arizona State University, Tempe. He is also the program director for the ASU Control Systems Engineering Laboratory.

- W. Matthew Carlyle is an associate professor in the Operations Research Department, Naval Postgraduate School, Monterey, California.

Karl G. Kempf is director of decision technologies at the Intel Corporation and an adjunct professor at Arizona State University.