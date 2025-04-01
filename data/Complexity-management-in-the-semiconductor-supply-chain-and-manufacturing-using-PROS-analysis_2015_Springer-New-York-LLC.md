Complexity Management in the Semiconductor Supply

Chain and Manufacturing Using PROS Analysis Can Sun 1, 2 , Thomas Rose 1, 3 , Hans Ehm 2 , and Stefan Heilmayer 2 1 RWTH Aachen University, Templergraben 55, 52062 Aachen, Germany

2

Infineon Technologies AG, Am Campeon 1-12, 85579 Neubiberg, Germany

3

Fraunhofer FIT, Schloss Birlinghoven, 53754 Sankt Augustin, Germany

{Can.Sun,Hans.Ehm,Stefan.Heilmayer}@infineon.com,

Thomas.Rose@fit.fraunhofer.de

Abstract. Supply chain complexity is a rising problem, especially in the semiconductor industry. Many innovative activities occur in the daily supply chain and manufacturing, and these changes inevitably bring in the complexities to the organization. But not all of them are valuable to the business goals. Decision makers want to keep value-added complexity and reduce non-value-added complexity.  To  manage  the  complexity,  we  propose  a  framework  with  four steps from changes identification towards the final decision making. The core solution  of  this  framework  is  PROS  (process,  role,  object,  state)  idea,  which provides  an  understandable  and  structural  way  to  describe  the  complexity.  A simplified small real example from semiconductor supply chain is used to demonstrate this approach. The results indicate that the PROS idea is able to analyze  complexity  from  different  aspects  and  extract  most  key  information; however, how to measure the structural complexity of a large complex system without complete information is still under investigation.

Keywords:

supply  chain  complexity,  change  management,  process  model, complexity assessment, semiconductor industry.

1

Introduction

The semiconductor industry is considered to be one of the most complex industries. From the raw material of silicon to the advanced semiconductor chips, there are more than 500

processing steps involved in the manufacturing. It also faces a highly volatile and turbulent market due to economic cycles, which bring the challenge to manage dynamic production environments with the pace of change in the industry [1], [2], [3]. The semiconductor supply chain is characterized by long throughput times, high levels of  stochasticity,  non-linearity  in  the  manufacturing  process  [4],  and  short  product  life cycles. These all lead to complexity to be managed in the supply chain. It is reflected as: network  complexity  (e.g.  multiple  production  sites  and  global  distribution  centers),

K. Liu et al. (Eds.): ICISO 2015, IFIP AICT 449, pp. 166-175, 2015. ' IFIP International Federation for Information Processing 2015 process  complexity  (manufacturing  and  business  processes),  product  complexity  (e.g. about 10,000 Stock keeping units and 500,000 order line item buckets), organizational complexity (e.g. many geographic regions with various tax and customs regulations), and

Complexity Management in the Semiconductor Supply Chain 167 information complexity (data structure and information flow) [5]. And all of them are interlinked. Managing  complexity  in  the  supply  chain  adds  value  to  business.  According  to A.T. Kearney's report, companies can increase their Earnings before interest and tax (EBIT) by 3 to 5 percent on average through systematic complexity management [6]. Many  changes  via  innovations  are  ongoing  in  operational,  tactical  and  strategic supply chain activities and thus complexities are added but not all of them are valuable to the business goals. Therefore, we need to distinguish: the 'good' complexity which adds value to the supply chain whereas the 'bad'' one does not. Value-adding ('good') complexity offers ways to meet customer demands and create a real competitive advantage; while value-destroying ('bad') complexity dissatisfy customers and sends the company into chaos and confusion [6], [7]. These two different categories of  complexity  require  companies  to  employ  distinctive  strategies.  The  value-adding complexity should be controlled efficiently to create value; for the value-destroying complexity, the part that does not add value needs to be eliminated, reduced and minimized [8], [9], and avoided in the early phase of generation. In reality these two types of complexity often occur together and thus a strategic balance is demanding, e.g., lead firms increase complexity by placing new demands on the value chain and in parallel adopt strategies to reduce the complexity of these transactions [10]. This brings the challenges to detect the complexity-added part and then to evaluate them in order to get rid of the non-valuable parts and support decision

making.

## 1.1 Research Question

My  research  aims  to  manage  the  complexities  from  the  computer  science  view.  By tracking the changes on the system level, the complexity drivers can be identified and described in a systematic way. After all the key information related to complexity being captured and structured, we can assess the complexity through selected instruments and categorize it as a value-added complexity or not. In the end, the results should be validated and thus can support decision making by applying corresponding strategies (e.g. reduce complexity, avoid complexity, etc.).

1.2

Status of Problem Domain and Related Solutions

## Much relevant research has been done on complexity management. Literature shows that  most  analysis  is  on  the  theoretical  level  based  on  an  abstract  model  instead  of

operational excellence on the practical level [11]. However, the mapping process from

'a real complex problem' to 'a defined model for complexity' is not much explored. Research on change management is mostly analyzed from the organizational view [12], small amount is viewed from the system engineering field, which is more related to  the  business  process  re-engineering  and  process  management  [13]  and  provides certain  process  meta-models  or  patterns  for  change  management  [14].We  are  more interested  in  the  latter  direction,  however,  the  connection  between model of  system change and the complexity management is not obvious.

168 C. Sun et al. Complexity in a supply chain is often viewed from three aspects: product, process and organization [15], [16], [17]. Research on the complexity analysis usually focuses on certain aspects, e.g. product variety, while it is not common to consider the complexity from a holistic view. Considering the inter-dependencies of different aspects of complexity, we prefer to use a comprehensive approach to capture all the important features of a complex system. Regarding the methods and instruments of complexity assessment, much research

is  on  the  strategic  level  and  only  provides  qualitative  evaluation;  some  quantitative methods are available but still lack practicability and tools [11], [15], [18], [19]. To support decision making, we are also interested in the implementation details, such as, formal indicators and structural measurement. From above analysis, it is seen that there is a gap between the existing approaches to handle complex problems and our objective. Therefore, we bring in a framework including 4 steps to manage complexity: 1) Identify complexity caused by changes 2) Represent  complexity  3)  Assess  complexity  via  developed  instruments  4)  Evaluate and support decision making. In this paper we address the first three steps on a real problem from semiconductor industry, which are also expected to be beneficial in the last  stage of decision  making. And in the second step a proposed conceptual model called PROS to describe complexity is highlighted.

## 2

Proposed approach

## 2.1 Identification of Changes and Complexity

Change is one of the main reasons to cause the complexity, so our research starts from the  change  analysis.  The  goal  of  this  step  is  to  capture  the  complexity  caused  by changes on the detailed level. Two parts related to changes should be considered: the change itself and its impact to the system. The change itself, also referred to as the initial change or one-time-change, means the 'effort to implement a change', which normally only execute once. For the impact of change, it is 'the potential consequence of a change on a system or what needs to be modified of a system in order to accomplish  a  change'  [20].  This  often  requires  executing  affected  processes  regularly  in order to maintain the change of system. Both change related parts usually lead to increased complexity. The output of this step is the added processes during the initial change phase; and the affected processes during the maintenance phase. 2.2 Information Extraction and Representation - PROS Idea

The purpose of this step is  to  represent  the  complexity  in  a  structural  way  without losing any important information. System models are employed to formalize the com-

## plexities receiving from the 1 st phase using modeling language such as SysML.

The premise to accurately describe supply chain complexity is to define the boun- dary of the complex system and its environment. We adopt a system delimitation technique from a generic Systems Engineering (SE) methodology to define the environment and intervention system [21], [22]. Some similar approaches, e.g., a knowledge

Complexity Management in the Semiconductor Supply Chain 169 representation language called Telos [23] can also be used to distinguish the environ- ment in a later stage. Once the investigation area is reduced, we can identify the elements and their relationships using the system consideration of SE. Then we develop a conceptual model called  PROS  (Process,  Role,  Object,  State),  which  defines  the  basic  elements  and relationships in a complex system. The idea of PROS originated from Object Process Methodology (OPM) [24], [25].

OPM  defines  three  basic  entities:  objects  with  states  and  processes.  Among  them objects and processes are higher-level building blocks, while states are always associated  with  objects  and  cannot  be  state-alone.  It  can  be  used  to  model  the  complex dynamic systems and embedded into other models for specified application [26]. Also we notice that supply chain is similar to economic, ecological, and social systems, which are characterized by interactive 'agents'' (roles) [27], [28].Therefore, we assume    role is as important as the object and process, while OPM only handles hu- man as an instance of object. Comparing with OPM, PROS also considers the human

behaviors and their initiatives. PROS model is characterized by entities, relationships and constraints. Entities .    A Process is a pattern of transformation that an object undergoes; A Role is a person to execute a process. This definition can be extended to: A role could be a person, a department, a customer, a supplier or any other group of persons or a software tool to execute a process. An Object is a thing that has the potential of stable, unconditional physical or mental existence. A State is a situation or position at which the object can exist for a period of time.

Relationships . We customize the OPM relationship set [24] for our purpose and define 6  relevant  pairs  of  relations:  Process-Process,  Process-Role,  Process-State,  ProcessObject, Object-Object, Object-State. For each pair, there are one  or more  subrelationships.  E.g.,  there  are  several  different  types  of  Process-State  relationships.  The attributes of these relationships are also defined: name, direction, symbols, dynamics, etc. Constraints .  Two constraints are highlighted: Cardinality and Relationship rule. Car- dinality defines 3 types of data structure: one-to-one relationship, one-to-many relationship and many-to-many relationship. Relationship rules imply that all the relationship definitions should follow the rules of the above 6 pairs strictly. The cardinality constraints and relationship rule can be used together. PROS Diagram and Prototype .  In  working  with  complex problems  we  found out that representation is an important goal for PROS. Thus we design a PROS diagram to

visualize the entities and their relationships, which can be viewed as the integration of the use case and object diagram of UML notations. We also developed a prototype as shown in Fig.1.  The  layout  divides  the  canvas  into  5  areas,  and  each  contains  one independent diagram. In the area marked with 1, the navigation of the whole object diagram  is  shown.  Area  2  shows  the  navigation  of  the  complete  process  diagram. Area 3 shows the dynamic object and state diagram for a running process. It reflects the details and changes of the objects during the processing.    Area 4 shows the roles involved in the process. Area 5 shows the running step for the process. Area 1 and 2

170 C. Sun et al. do not change during the whole process analysis, only the analyzed area of processes and objects is highlighted. Other areas change with the process step in analysis. PROS  analysis  normally  starts  with  the  process  aspect,  similar  to  other  system modeling languages like BPMN and UML. Besides this process-oriented analysis, the human-oriented analysis can also be applied. Agent-based modeling and simulation is Vand UML. Besides this process-oriented analysis, the so be Agent-based modeling and simulation is applied.

a widely used technique to formalize the human (agents in broad definition) behavior

Fig. 1. Visualization Prototype for PROS

<!-- image -->

The results  of  the  PROS  analysis  contain  most  key  information  from  a  complex system and which can be used as an input for the assessment step.

2.3

Structural Complexity Measurement Using PROS

## Structural complexity is about the complexity resulting from physical interconnection

of components. It belongs to the physical domain and can be directly calculated from the elements and the relationships among them [15], [31]. Since this information can be received from the step 2, we can at least calculate the  complexity oriented from elements (states of a system) and the complexity oriented from relationships (number of  all  connections).  A  further  step  measure  is  to  calculate  the  entropy  of  statistical complexity based on the Shannon information theory [18]. Besides the basic quantity (size) information, we assume that the structural complexity is also decided by the attributes of each individual element, such as category, importance or diversity, and whether it is interrelated to the rest of system. We also need to highlight the impact of roles (often humans), as their behaviors can lead to uncertainty  and  thus  complexity  of  the  system.  To  be  able  to  distinguish  the  complexity impact of different roles, we added a weight value for each role by considering the number of involved processes [32].

Complexity Management in the Semiconductor Supply Chain 171 3 Case Study 3.1 Shared reticle vs. Mono Reticle We select  a  case  from  semiconductor  manufacturing  to  explain  how  complexity  is generated. A set of reticles (up to 35) is needed to produce a wafer. In this paper we call  the  reticle  set  ''reticle''  for  simplicity.  Comparing  with  the  as-is  solution  with mono reticle, an alternative solution using shared reticle could produce more products on one wafer, and thus reduce the quantity of reticles required. The reduction of reticle costs decreases manufacturing costs substantially. There is certain degree of truth that, shared reticle technology is cost beneficial, but

the flip side of the coin is that the change process from mono reticle to share reticle is not that simple. For example, certain processes need to be updated, people need to be motivated to accept the changes, etc., which leads to increased complexities. Before making decision to adopt the shared reticle solution or not, it is necessary to assess its increased supply chain complexity and evaluate whether the reduced reticle cost offsets the increased complexity. The cost saving from the economic view is given on monetary values; however, the change process and its increasing complexity are not systematically assessed. Current Business Process Management (BPM) solution cannot reflect all aspects of the complex problem, while other supply chain process models are not detailed on the opera-

tional level. This gap hinders the making of high-quality decisions.

## 3.2 Results Achieved so Far

By following the framework provided in section 2, we have achieved some intermediate results, which are mainly centered on the changes and complexities identification and measurement. Changes  and  Complexity  Identification  and  Presentation .  The  change  manage- ment can be analyzed from the aspects of process, organization (roles) via PROS. The process analysis follows the supply chain operations reference-model (SCOR)

model, the most widely accepted framework for standardization in supply chain management, developed by the Supply Chain Council 1 . It defines the first three levels of supply chain processes. The top level has 5 processes: Plan, Source, Make, Deliver and Return . Each level-1 process has 10-20 level-2 processes and spans multiple level-3  and  4  processes.  Processes  below  level  3  are  defined  by  the  companies  themselves. Following the SCOR model, the major processes of shared reticle up to level 4 can be identified. Considering  around  all  500  steps  of  Produce  and  Test  Process  (sub-process  of Make ) related to wafer manufacturing with mono and shared reticle, it can be roughly said that 480 steps are not changed. Complexity is mainly added in the Test process (for simplicity step 480 to 490) and the Optical Control process (for simplicity step

1 http://www.apics.org/sites/apics-supply-chain-council

172 C. Sun et al.

490 to 500). For the Plan Process, the overall planning including short-term plan and

mid-term plan need to be changed; and Front End Plan needs to be rescheduled. The main affected processes and their added complexities are listed in Table 1. It is important to highlight which types of change the complexity belongs to, as this would

| be part of assessment on the next stage.                                    |                                                                                                                  |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| R is regular maintenance)  SCOR  Process Changed                            | Added complexity CT                                                                                              |
| Model  Layer  1.1.2  Make-Front End-Test  1.1.2  Make-Front End-Test        | Equipment  reprogramming  in  order  to  manage the changes  O  For  shared  reticle,  in  testing  at  least  R |
|                                                                             | every  second  product  is  different  and  thus  the  testing  process  needs  to  be                           |
| 1.1.3  Make-Front  End  -Optical  Control                                   | switched too.  Equipment update O                                                                                |
| 1.1.3  Make-Front  End  -Optical  Control  1.1.3  Make-Front  End  -Optical | Training the operators O  More  operators  are  allocated  to  work  O                                           |
| Control  1.1.3  Make-Front  End  -Optical                                   | with optical inspections systems  Monitor the optical inspection systems  R                                      |
| Control  2.1.1  Plan- Production Program                                    | Overall planning processes are changed  O                                                                        |
| 2.1.1  Plan- Production Program                                             | Execute  the  changed  planning  processes  R                                                                    |
| …  …                                                                        | … …                                                                                                              |

We also notice that the stakeholders' attitudes towards these affected processes may influence the new solution and thus lead to complexity. Research shows people may not like change or may not adopt changes [33], [34].Therefore, we need to consider the human goals in order to measure complexity accurately in the next step. Based on the interviews and process analysis, we identify the key stakeholders involved in the change project and assess their interests. Here a goal-oriented modeling

approach is employed, e.g.,  -Star can be used to analyze personal goals and behaviors i of  alternative  solutions  [30].  For  each  stakeholder,  first  we  analyze  their  goals  and corresponding actions, and then we can check how these actions benefit or hurt their goals. By doing that the relationships among stakeholders are detected too. One part of our result shows that, test engineer does not like to accept the change as it hurts his goal while the development engineer is motivated for this change. The main object involved in this change is wafer and its states are related to the different stages of manufacturing process steps. PROS approach can be used as a guide to obtain the key elements of processes, roles and objects, as well as different relationships. We could gain this information:

· Description about the stakeholders and their goals · Description about the changed process

Complexity Management in the Semiconductor Supply Chain 173 · Description about the objects and their states involved in the processes · Partial information about the dependencies network

Complexity assessment . We can get statistic information from above analysis, e.g., the change includes 4 processes and 10 sub-processes, 7 roles and 2 objects with 10 states. Using  the  measurement  methodology  proposed  in  section  2.3,  we  can  calculate  its element complexity. However, for the relationships among these elements, it is not easy to detect all dependencies within a large complex system.

Besides that, we should measure the different types of process changes separately. Table 1 shows two types of changes: the one-time-change needs only to be calculated once, while the regular maintenance needs to be calculated periodically. To evaluate whether the benefits of a new solution outweigh the added complexity, we could calculate the deviated complexity from two solutions (the changes part) and compare  it  with  the  saved  costs.  For  example,  if  the  cost  of  added  complexity  is smaller than the saved reticle benefits, we can identify 'switch to shared reticle' as a

value-adding complexity, otherwise, it is the value-destroying complexity.

3.3 Discussion It  is  seen  from  above  analysis,  PROS  approach  helps  to  analyze  from  different  aspects: the processes and their required changes, people and their conflicts. However, for a large complex system, it is not feasible to use an exhaustive method to detect all relationships between elements. How to estimate the relationship intelligently (sufficiently accurate within a given time) is still a challenge for us.

The lessons learned focus on two areas: 1) each aspect of a complex problem can be  detailed  and  deeply  analyzed  by  following  a  certain  model  or  method  -  e.g., process analysis with SCOR, role analysis with goal-oriented mode. For large systems the accuracy within a given time is a challenge. 2) The qualitative analysis is not sufficient for decision making, to make better decision we need to quantify complexity oriented from all aspects of a system. The PROS approach is promising but a formula ending up with a complexity number is still missing.

4

Conclusion and Future Work

## This paper introduces a framework to manage supply chain complexity from comput-

er science view, which sets up a connection between change management and com- plexity management. We conclude that complexity should be managed from a systematic view instead of the single aspect. The core part of this framework is the PROS conceptual model, which represents and visualizes the complex system by capturing its important elements and relationships.  It  can  supplement  the  quantitative  complexity  measurement  by  separating  it into the elements and relationships part. Calculating the numerous relationships in a

large system requires more sophisticated methodologies. An industrial case from the semiconductor industry with two alternative solutions is analyzed from different aspects and the measurement of added complexity is discussed

174 C. Sun et al. in order to select the optimal solution. The framework is not limited to the semiconductor industry or supply chain field and could be extended to a broad area: project management, organization changes, government policy analysis, etc. In future research we optimize the PROS approach to larger systems and improve the quantitative measurement of complexity. Two aspects will be addressed: 1) Understand

and track the dynamic interaction between elements. 2) Investigate the weight value of human behaviors and their impact, and other components leading to uncertainties and

thus complexity of the system.

- References
- 1. Uzsoy, R., Lee, C.Y., Martin-Vega, L.A.: A Review Of Production Planning And Scheduling  Models  In  The  Semiconductor  Industry  Part  I:  System  Characteristics,  Performance Evaluation And Production Planning. IIE Transactions 24(4), 47-60 (1992)
- 2. Bauer, H., Kouris, I., Schlögl, G., Sigrist, T., Veira, J., Wee, D.: Mastering Variability In Complex Environments. Mckinsey Semiconductors (Autumn 2011) 3. Emami-Naeini, A., De Roover, D.: Control in Semiconductor Wafer Manufacturing. In:
- Proc. Symposium To Honor Bill Wolovich, 47th IEEE Conference on Decision and Control, Cancun, Mexico (2008) 4. Wang, W., Rivera, D.E.: Model Predictive Control For Tactical Decision-Making In Semiconductor Manufacturing Supply Chain Management. IEEE Transactions On Control Sys-
- tems Technology 16(5), 841-855 (2008) 5. Christopher, M.: The Agile Supply Chain: Competing In Volatile Markets. Industrial Marketing Management 29(1), 37-44 (2000)
- 6. Scheiter, S., Scheel, O., Klink, G.: How Much Does Complexity Really Cost? A.T. Kearney, Düsseldorf (2007), http://www.mycomplexity.com/publications.asp
- 7. Etheredge, K., O'Keefe, J.: Getting A Handle On Complexity. Supply Chain Management Review, A.T. Kearney (2010), http://www.atkearney.com/documents 8. Heywood,  S.,  Spungin,  J.,  Turnbull,  D.:  Cracking  the  complexity  code.  The  McKinsey
- Quarterly (2), 85-95 (2007) 9. Birkinshaw, J., Heywood, S.: Putting organizational complexity. The McKinsey Quarterly
- (3) (2010) 10. McKinsey and Company: McKinsey on Semiconductors (1) (Autumn 2012) 11. Aelker, J., Bauernhansl, T., Ehm, H.: Managing complexity in supply chains: a discussion
- of  current  approaches  on  the  example  of  the  semiconductor  industry.  Procedia  CIRP 7,
- 79-84 (2013) 12. Todnem By, R.: Organisational change management: A critical review. Journal of Change Management 5(4), 369-380 (2005) 13. Kettinger, W.J., Teng, J.T., Guha, S.: Business process change: a study of methodologies,
- techniques, and tools. MIS Quarterly, 55-80 (1997) 14. Weber, B., Reichert, M., Rinderle-Ma, S.: Change patterns and change support features-
- enhancing flexibility in process-aware information systems. Data &amp; knowledge Engineering 66(3), 438-466 (2008) 15. ElMaraghy,  H.A.,  Kuzgunkaya,  O.,  Urbanic,  R.J.:  Manufacturing  systems  configuration
- complexity. CIRP Annals-Manufacturing Technology 54(1), 445-450 (2005) 16. Deger, R.: Managing Complexity in Automotive Engineering. In: DSM 2007: Proceedings of the 9th International DSM Conference, Munich, Germany, October 16-18 (2007)
- Complexity Management in the Semiconductor Supply Chain 175 17. Lindemann, U., Maurer, M.: Facing multi-domain complexity in product development. In: The Future of Product Development, pp. 351-361. Springer, Heidelberg (2007)
- 18. Shannon, C.E.: A Mathematical Theory of Communication. Bell System Technical Journal 21, 623-656 (1948)
- 19. Schuh, G., Monostori, L., CsÆji, B.C., Doering, S.: Complexity-based modeling of reconfigurable  collaborations  in  production  industry.  CIRP  Annals-Manufacturing  Technology 57(1), 445-450 (2008)
- 20. Bohner,  S.A.,  Arnold,  R.S.:  Software  change  impact  analysis.  IEEE  Computer  Society Press, Los Alamitos (1996) 21. Haberfellner, R.: Systems Engineering: Methodik und Praxis. Daenzer, W.F. (ed.). Verlag Industrielle Organisation (2002)
- 22. Alard, R.: ETH Chair of Technology and Innovation Management, Systems Engineering Methodology (2013), http://www.timgroup.ethz.ch/en/courses?id=55 , retrieved on January 27, 2015
- 23. Mylopoulos, J., Borgida, A., Jarke, M., Koubarakis, M.: Telos: Representing knowledge about information  systems.  ACM  Transactions  on  Information  Systems  (TOIS) 8(4),  325-362 (1990)
- 24. Dori,  D.:  Object  Process  Methodology:  A  Holistic  Systems  Paradigm;  with  CD-ROM. Springer (2002) 25. Dori, D.: Object-process analysis: maintaining the balance between system structure and
- behaviour. Journal of Logic and Computation 5(2), 227-249 (1995) 26. Sharon, A., Dori, D.: A model-based approach for planning work breakdown structures of complex systems projects. In: Proc. 14th IFAC Symposium on Information Control Prob-
- lems in Manufacturing (2009) 27. Berry, B.J., Kiel, L.D., Elliott, E.: Adaptive agents, intelligence, and emergent human organization: Capturing complexity through agent-based modeling. Proceedings of the National  Academy  of  Sciences  of  the  United  States  of  America 99(Suppl.  3),  7187-7188 (2002)
- 28. Holling, C.S.: Understanding the complexity of economic, ecological, and social systems. Ecosystems 4(5), 390-405 (2001) 29. Helbing, D., Balietti, S.: How to do agent-based simulations in the future: From modeling
- social  mechanisms  to  emergent  phenomena  and  interactive  systems  design.  Tech.  Rep. 11-06-024, Santa Fe Institute, NM, USA, santa Fe Working Paper (June 2011) 30. Eric, S.K., Giorgini, P., Maiden, N. (eds.): Social modeling for requirements engineering. MIT Press (2011)
- 31. Salado,  A.,  Nilchiani,  R.:  The  Concept  of  Problem  Complexity.  Procedia  Computer Science 28, 539-546 (2014)
- 32. Sun, C., Rose, T., Ehm, H., Heilmayer, S.: Complexity Measurement in the Semiconductor Supply Chain. Presented at International Conference on Operations Research 2014: business analytics and optimization (Aachen 2014)
- 33. Bakker,  C.B.:  Why  people  don't  change.  Psychotherapy:  Theory,  Research  &amp;  Practice 12(2), 164 (1975) 34. Kotter, J.P., Cohen, D.S.: The heart of change: Real-life stories of how people change their organizations. Harvard Business Press (2002)