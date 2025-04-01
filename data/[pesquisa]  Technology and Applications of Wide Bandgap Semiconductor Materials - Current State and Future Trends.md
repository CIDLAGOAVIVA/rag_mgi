<!-- image -->

<!-- image -->

Review

## Technology and Applications of Wide Bandgap Semiconductor Materials: Current State and Future Trends

Omar Sarwar Chaudhary 1 , Mouloud Denaï 1, * , Shady S. Refaat 1,2 and Georgios Pissanidis 3

- 1 School of Physics, Engineering and Computer Science, University of Hertfordshire, Hatfield AL10 9AB, UK; o.s.chaudhary2@herts.ac.uk (O.S.C.); s.khalil3@herts.ac.uk (S.S.R.)
- 2 Department of Electrical and Computer Engineering, Texas A&amp;M University at Qatar, Doha 23874, Qatar
- 3 Enoda Ltd., Edinburgh EH3 9EG, UK; g.pissanidis@enodatech.com
- * Correspondence: m.denai@herts.ac.uk

Abstract: Silicon (Si)-based semiconductor devices have long dominated the power electronics industry and are used in almost every application involving power conversion. Examples of these include metal-oxide-semiconductor field-effect transistors (MOSFETs), insulated-gate bipolar transistors (IGBTs), gate turn-off (GTO), thyristors, and bipolar junction transistor (BJTs). However, for many applications, power device requirements such as higher blocking voltage capability, higher switching frequencies, lower switching losses, higher temperature withstand, higher power density in power converters, and enhanced efficiency and reliability have reached a stage where the present Si-based power devices cannot cope with the growing demand and would usually require large, costly cooling systems and output filters to meet the requirements of the application. Wide bandgap (WBG) power semiconductor materials such as silicon carbide (SiC), gallium nitride (GaN), and diamond (Dia) have recently emerged in the commercial market, with superior material properties that promise substantial performance improvements and are expected to gradually replace the traditional Si-based devices in various power electronics applications. WBG power devices can significantly improve the efficiency of power electronic converters by reducing losses and making power conversion devices smaller in size and weight. The aim of this paper is to highlight the technical and market potential of WBGsemiconductors. A detailed short-term and long-term analysis is presented in terms of cost, energy impact, size, and efficiency improvement in various applications, including motor drives, automotive, data centers, aerospace, power systems, distributed energy systems, and consumer electronics. In addition, the paper highlights the benefits of WBG semiconductors in power conversion applications by considering the current and future market trends.

Keywords: Wide Bandgap Semiconductor; semiconductor materials; power electronic devices

## 1. Introduction

Power electronics has been the key technology driver for efficient electrical power conversion for more than two decades, covering a breadth of application areas ranging from aerospace, automotive, consumer electronics, industry, utility systems, and many other areas. It is estimated that by 2030, around 80% of the worldwide energy generation and consumption will be processed through power electronics [1]. While, in the case of many renewable energy applications, including solar photovoltaic (PV) inverters, 100% of the electrical energy is processed by a power converter consisting of different switching devices. As global demand for energy continues to rise due to economic growth and population increase, improvement in energy efficiency has become a crucial challenge. The largest amount of power losses that occurs in power electronic converters is dissipated in the power semiconductor devices. Currently, even with these various limitations, the mature and very well-established Si-based technology is still playing a leading role in satisfying the constantly growing demands of power semiconductor devices [2]. A bibliometric

<!-- image -->

<!-- image -->

Citation: Chaudhary, O.S.; Denaï, M.; Refaat, S.S.; Pissanidis, G. Technology and Applications of Wide Bandgap Semiconductor Materials: Current State and Future Trends. Energies 2023 , 16 , 6689. https://doi.org/ 10.3390/en16186689

Academic Editors: Massimiliano

Luna and Marcello Pucci

Received: 27 July 2023 Revised: 11 September 2023 Accepted: 13 September 2023 Published: 18 September 2023

<!-- image -->

Copyright: © 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).

R PEER REVIEW

2  of  28

bibliometric analysis based on a thesaurus fi

le  from the dimension's website was con- analysis based on a thesaurus file from the dimension's website was conducted to shape the review structure, as illustrated in Figure 1. The proposed bibliometric visualization for the author-supplied keywords was created with VOS viewer software from 2018 to 2023. It shows three topic clusters: WBG semiconductor materials, technology and applications, and current state and future trends. ducted to shape the review structure, as illustrated in Figure 1. The proposed bibliometric visualization for the author-supplied keywords was created with VOS viewer software from 2018 to 2023. It shows three topic clusters: WBG semiconductor materials, technology and applications, and current state and future trends.

Figure 1. Bibliometric analysis of author-supplied keywords, with node size indicating frequency of recurrence and node connections indicating co-occurrence within the same quartile. Figure 1. Bibliometric analysis of author-supplied keywords, with node size indicating frequency of recurrence and node connections indicating co-occurrence within the same quartile.

<!-- image -->

Si-based devices are widely used in power converters, which include bipolar, unipolar, controlled, and uncontrolled devices. Examples of such devices are power diodes, thyristors (gate turn-o ff s (GTO); gate-controlled thyristors (GCT)), BJTs (bipolar junction transistors), IGBTs, and MOSFETs. A new generation of IGBTs is now able to handle voltages up to 6.5 kV and currents up to 1700 A. The IGBT (insulated gate bipolar transistor) represents  a  power  semiconductor  device  comprising  four  layers  and  three  terminals.  It serves as a merged unit combining the a tt ributes of power MOSFET and BJT, facilitating rapid switching and elevated power-handling capacity. The IGBT is characterized by its capability to deliver e ffi cient switching with minimal power loss in the ON state, along with superior ratings when compared to both MOSFET and BJT devices. IGBTs are commonly used in motor drives, converters circuits, and power supplies applications where there is a demand for high voltage and currents. Power MOSFETs, on the other hand, are increasingly used by the power supply community and in low-power inverters due to Si-based devices are widely used in power converters, which include bipolar, unipolar, controlled, and uncontrolled devices. Examples of such devices are power diodes, thyristors (gate turn-offs (GTO); gate-controlled thyristors (GCT)), BJTs (bipolar junction transistors), IGBTs, and MOSFETs. A new generation of IGBTs is now able to handle voltages up to 6.5 kV and currents up to 1700 A. The IGBT (insulated gate bipolar transistor) represents a power semiconductor device comprising four layers and three terminals. It serves as a merged unit combining the attributes of power MOSFET and BJT, facilitating rapid switching and elevated power-handling capacity. The IGBT is characterized by its capability to deliver efficient switching with minimal power loss in the ON state, along with superior ratings when compared to both MOSFET and BJT devices. IGBTs are commonly used in motor drives, converters circuits, and power supplies applications where there is a demand for high voltage and currents. Power MOSFETs, on the other hand, are increasingly used by the power supply community and in low-power inverters due to their high switching ability and ease of drive circuitry in contrast to IGBTs [3]. Si-based MOSFETs have long been hindered due to their high on-state resistance, which substantially increases power losses in the devices. The on-state resistance increases in proportion with the blocking voltage, which makes them unsuitable for high-voltages applications above 600 V [4].

The physical limitations of the current generation of Si-based MOSFETs and IGBTs their high switching ability and ease of drive circuitry in contrast to IGBTs [3]. Si-based MOSFETs have long been hindered due to their high on-state resistance, which substantially increases power losses in the devices. The on-state resistance increases in proportion with the blocking voltage, which makes them unsuitable for high-voltages applications above 600 V [4]. The physical limitations of the current generation of Si-based MOSFETs and IGBTs have hindered the progress in achieving high efficiency, reliability, and compact form factor in power applications. It is desirable to convert power at high frequencies for power converters and other electronic system applications. There are many advantages when switching at higher frequencies, such as a reduction in the size, weight, and cost of the converter. The limitation of Si-based power semiconductors arises due to a decrease in

have hindered the progress in achieving high e ffi

ciency, reliability, and compact form fac- tor in power applications. It is desirable to convert power at high frequencies for power

converters and other electronic system applications. There are many advantages when

efficiency and a substantial increase in temperature stress cycles as the switching frequency increases [5].

## Technical Challenges Facing Si Semiconductor Devices

The design and fabrication of Si power devices with enhanced functionality, efficiency, and reliability offer several benefits and advantages in numerous areas, especially for efficient grid integration of renewable and distributed energy sources. Additionally, the integration of Si power devices in advanced converters topologies offers tremendous benefits in terms of cost of energy, improvement in efficiency, and converter size reduction. To achieve higher efficiencies in power conversion applications, semiconductor switches must exhibit the lowest power losses. Currently, Si-based switches such as MOSFETs, IGBTs, and thyristors have many limitations in terms of design and material properties, which tend to affect the overall performance of the power conversion application [6].

High Losses: Since Si has a low bandgap (1.1 eV) and low critical electric field (30 MV/cm), the thickness of the device will increase considerably with high voltages, which leads to high resistance and consequently increased conduction losses. Also, in critical applications, the low bandgap of Si affects its robustness against disturbances such as intense magnetic fields, radiation, and heat.

Low Switching Frequency: Si-based power MOSFETs exhibit relatively high losses at higher switching frequencies due to increased die size. This large die surface area is designed to minimize conductions, but it results in higher gate capacitance and the generation of large peak currents from gate charge, which in turn increases the switching losses at higher frequencies. Si-based IGBTs have a smaller die surface area than MOSFETs, as they utilize minority carriers for conductivity modulation. However, the long lifetime of minority carriers decreases the overall frequency range. Thus, at higher frequencies, both MOSFETs and IGBTs exhibit higher losses and are often operated at lower switching frequencies, which is not advantageous in many power applications; hence, this impacts the overall efficiency of power applications and devices.

Poor Performance at High Temperature : The low Si bandgap also contributes to high intrinsic carrier concentrations in Si-based devices. This translates into increased leakage currents at higher temperatures. Temperature variation of the bipolar gain in IGBTs amplifies the leakage and limits the maximum junction temperature of many IGBTs to 125 ◦ C [7]. Due to this fact, current systems with Si-based semiconductors require expensive and bulky cooling systems for heat removal. There are many areas where power semiconductors are operated at high temperatures, such as military, aerospace, highpower applications, and optoelectronics. The High-Temperature Electronics Network of Excellence (HITEN) has estimated the high-temperature electronics market's worth around USD 9.5 billion, and it is expected to grow above USD 19.5 billion [8]. Recently, there has been extensive and ongoing research and development on the design of advanced and effective cooling systems for power electronics components. Smart cooling systems can considerably increase the lifetime and efficiency of semiconductor devices by operating the device within its physical limits. In many high-power electronics applications, microcooling systems comprising chip control, integrated control loops, liquid cooling systems, and temperature sensors are designed to effectively remove the excessive heat from the device. The reliability, efficiency, and lifetime of semiconductor materials decrease when operated under high temperatures and various stress conditions. Table 1 shows the effects of temperature on selected major sensors and semiconductor devices [9].

Table 1. Effect of temperature on major semiconductor devices [9].

| Major Semiconductor Devices                           | Effect of High Temperature ( T )                                                                                                                                       |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Thermistor Piezo-resistive sensors with PN insulation | glyph[squaresolid] Number of charge carriers and conductivity increases glyph[squaresolid] Sensitivity decreases glyph[squaresolid] Junction leakage current increases |

PN diodes

Bipolar transistor

JFET

MESFET

MOSFET











Reverse current increases with

𝑇

Voltage drop in the forward direction decreases

Leakage current increases exponentially

Base-emi

4 of 27 er voltage decreases at collector current tt

Current ampli fi

cation increases with

𝑇 ௫

(

1 &lt; 𝑥 &lt; 2)



Channel mobility decreases with

𝑇 ଷ/ଶ



Pinch-o ff

voltage increases higher current, voltage, packaging density, and temperature is constantl

| Major Semiconductor Devices   | Effect of High Temperature ( T )                                                                                                                                                                                                                                                                                                      |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schottky diodes               | glyph[squaresolid] Forward voltage-drop decreases glyph[squaresolid] Reverse current increases with T 2 Similar to JFET   Channel mobility decreases with  𝑇 ଷ/ଶ                                                                                                                                                                      |
| PN diodes                     | glyph[squaresolid] Voltage drop in the forward direction decreases glyph[squaresolid] Leakage current increases exponentially  Leakage current of PN junctions increases exponentially                                                                                                                                                |
| Bipolar transistor            | glyph[squaresolid] Base-emitter voltage decreases at collector current glyph[squaresolid] Current amplification increases with T x ( 1 &lt; x &lt; 2 )  Threshold voltage decreases                                                                                                                                                         |
| JFET                          | glyph[squaresolid] Channel mobility decreases with T 3/2 glyph[squaresolid] Pinch-off voltage increases 2. WBG Material Properties and Market Trend                                                                                                                                                                                    |
| MESFET                        | glyph[squaresolid] Similar to JFET                                                                                                                                                                                                                                                                                                     |
| MOSFET                        | glyph[squaresolid] Channel mobility decreases with T 3/2 glyph[squaresolid] Leakage current of PN junctions increases exponentially glyph[squaresolid] Threshold voltage decreases In the last decade, numerous improvements have been made to the e technology  in  terms  of  structure,  design,  and  material  properties. As  th |

based power devices have gradually started approaching their performance

In the last decade, numerous improvements have been made to the existing silicon technology in terms of structure, design, and material properties. As the demand for higher current, voltage, packaging density, and temperature is constantly growing, Sibased power devices have gradually started approaching their performance limits. While, WBG semiconductors have begun to emerge as a potential alternative technology. They offer better inherent material advantages over Si, such as higher voltage breakdown, higher switching frequency, comparable carrier mobility, higher energy bandgap, and higher thermal conductivity [10]. WBG semiconductors have begun to emerge as a potential alternative tec o ff er  be tt er  inherent  material  advantages  over  Si,  such  as  higher  voltag higher switching frequency, comparable carrier mobility, higher energy higher thermal conductivity [10]. WBG-based semiconductors such as silicon carbide (SiC), gallium nitri diamond (Dia) are superior to Si semiconductors and o ff er many advanta conversion applications. The physical characteristics of SiC, GaN, and Dia, i

## 2. WBG Material Properties and Market Trend

WBG-based semiconductors such as silicon carbide (SiC), gallium nitride (GaN), and diamond (Dia) are superior to Si semiconductors and offer many advantages for power conversion applications. The physical characteristics of SiC, GaN, and Dia, include higher bandgap width (3~4 times), higher breakdown field (4-20 times), higher thermal conductivity (3-13 times), larger saturated electron drift velocity, low intrinsic carrier concentration (between 10-35 order of magnitude), and higher bandgap energy as compared to those of Si [3]. Figure 2 illustrates the thermal, voltage, and frequency characteristics of Si, SiC, and GaN materials. bandgap width (3~4 times), higher breakdown fi eld (4-20 times), higher th tivity (3-13 times), larger saturated electron drift velocity, low intrinsic carr tion (between 10-35 order of magnitude), and higher bandgap energy as those of Si [3]. Figure 2 illustrates the thermal, voltage, and frequency chara SiC, and GaN materials.

Figure 2. Si, SiC, and GaN properties. Figure 2. Si, SiC, and GaN properties.

<!-- image -->

Other advantages of WBG semiconductors are their thinner drift regions due to increased electric critical field value, which can result in lower on-resistance and better coefficient of

Other advantages of WBG semiconductors are their thinner drift regions due to in- creased electric critical

fi eld value, which can result in lower on-resistance and be

tt er co-

e

ffi cient of thermal expansion (CTE). Materials having CTE closer to the available electri-

cally insulating and thermally conductive ceramics layers can be adopted more easily for higher power and temperature applications compared to Si. There are also some disad-

vantages of WBG semiconductors, such as their electrons and holes mobility, which might thermal expansion (CTE). Materials having CTE closer to the available electrically insulating and thermally conductive ceramics layers can be adopted more easily for higher power and temperature applications compared to Si. There are also some disadvantages of WBG semiconductors, such as their electrons and holes mobility, which might in some cases make them inappropriate for bipolar devices. For high-power and high-temperature applications, WBG semiconductors offer physical properties relatively superior to those of Si-based semiconductor technology. As temperature increases, the degradation of the semiconductor material will continue until it fails to provide sufficient functionality. There are certain amount of thermal electron and hole carriers called intrinsic carriers. As temperature increases, the number of carriers increases exponentially, which causes a degradation in the electrical conductivity of the doped regions in Si-based semiconductors. The other source of degradation is due to the P-N junction leakage current, which is directly related to the intrinsic concentration of the semiconductor. Since WBG semiconductors have lower intrinsic carrier concentration, the leakage currents are smaller as compared to silicon. Another fundamental mechanism in semiconductors is the ability of carriers to move through the semiconductor. When the temperature increases, the ability of carriers to move inside the crystal decreases. This is due to atoms in the crystal lattice acquiring more energy as the temperature increases, hence increasing the thermal vibrational energy that results in more collisions through the crystal. This leads to a reduction in the amount of current that a diode or a transistor can carry due to a decrease in carrier mobility [11]. With the combination of improved material properties, WBG can significantly reduce losses by 95% up to 98% or higher depending on the application [12]. This substantially reduces the cooling requirements and size of passive components, leading to a reduction in size, weight, and cost [13]. in some cases make them inappropriate for bipolar devices. For high-power and hightemperature applications, WBG semiconductors o ff er physical properties relatively superior to those of Si-based semiconductor technology. As temperature increases, the degradation of the semiconductor material will continue until it fails to provide su ffi cient functionality. There are certain amount of thermal electron and hole carriers called intrinsic carriers. As temperature increases, the number of carriers increases exponentially, which causes a degradation in the electrical conductivity of the doped regions in Si-based semiconductors. The other source of degradation is due to the P-N junction leakage current, which is directly related to the intrinsic concentration of the semiconductor. Since WBG semiconductors  have  lower  intrinsic  carrier  concentration,  the  leakage  currents  are smaller as compared to silicon. Another fundamental mechanism in semiconductors is the ability of carriers to move through the semiconductor. When the temperature increases, the ability of carriers to move inside the crystal decreases. This is due to atoms in the crystal la tt ice acquiring more energy as the temperature increases, hence increasing the thermal vibrational energy that results in more collisions through the crystal. This leads to a reduction in the amount of current that a diode or a transistor can carry due to a decrease in carrier mobility [11]. With the combination of improved material properties, WBG can signi fi cantly reduce losses by 95% up to 98% or higher depending on the application [12]. This substantially reduces the cooling requirements and size of passive components, leading to a reduction in size, weight, and cost [13]. Despite all these advantages, SiC-, GaN-, and Dia-based semiconductors are still in

Despite all these advantages, SiC-, GaN-, and Dia-based semiconductors are still in their early stages of research and development. Because of its higher thermal conductivity, ultrawide bandgap, and higher carrier mobility as compared to other semiconductors, Dia is set to become the best semiconductor material in the future. Even though Dia is the best semiconductor, the device material and fabrication technology is less mature and less developed as compared to SiC and GaN [14]. Currently, the WBG semiconductors market represents a small segment in the global power electronics industry, and power electronics in turn are small fraction of the global semiconductor market. The U.S. is leading the market share for WBG research and development, but the rising competition from Europe, China, and Japan is changing this landscape [15]. Figure 3 presents the WBG market share within the semiconductor industry. It shows that the semiconductor sales market share within the region rose from USD 337.30 billion in 2015 to USD 583.20 billion in 2022 [16], while Figure 4 illustrates the projected yearly growth of WBG market by application [17]. It shows that EV application has the highest growth compared with other applications. their early stages of research and development. Because of its higher thermal conductivity, ultrawide bandgap, and higher carrier mobility as compared to other semiconductors, Dia is set to become the best semiconductor material in the future. Even though Dia is the best semiconductor, the device material and fabrication technology is less mature and less developed as compared to SiC and GaN [14]. Currently, the WBG semiconductors market represents a small segment in the global power electronics industry, and power electronics in turn are small fraction of the global semiconductor market. The U.S. is leading the market share for WBG research and development, but the rising competition from Europe, China, and Japan is changing this landscape [15]. Figure 3 presents the WBG market share within the semiconductor industry. It shows that the semiconductor sales market share within the region rose from USD 337.30 billion in 2015 to USD 583.20 billion in 2022 [16], while Figure 4 illustrates the projected yearly growth of WBG market by application [17]. It shows that EV application has the highest growth compared with other applications.

Figure 3. WBG power electronics within total semiconductor industry [16]. Figure 3. WBGpower electronics within total semiconductor industry [16].

<!-- image -->

, x FOR PEER REVIEW

Figure 4. Projected annual growth by application of WBG market [17].

<!-- image -->

## Figure 4. Projected annual growth by application of WBG market [17]. 2.1. Performance Advances and Market Trends of SiC

2.1. Performance Advances and Market Trends of SiC There  are  many  challenges  that  arise  when  developing  new  generation  of  WBGbased semiconductors for various applications. For SiC-based devices, the di ffi culty arises from the presence of crystal defects and lack of abundant wafers during the material processing. These factors have ultimately contributed to the slow commercial development of SiC power devices. SiC has well over 150 di ff erent polytypes, but only 6H-SiC and 4HSiC are commercially available in the form of abundant wafers and epitaxial layers [18]. Among these two, 4H-SiC exhibits be tt er characteristics because of its higher carrier mobility and higher electric breakdown fi eld, which helps reduce the size of the epitaxial layers. The reduction in the size of the drift layer helps reduce the low drift resistance, There are many challenges that arise when developing new generation of WBG-based semiconductors for various applications. For SiC-based devices, the difficulty arises from the presence of crystal defects and lack of abundant wafers during the material processing. These factors have ultimately contributed to the slow commercial development of SiC power devices. SiC has well over 150 different polytypes, but only 6H-SiC and 4H-SiC are commercially available in the form of abundant wafers and epitaxial layers [18]. Among these two, 4H-SiC exhibits better characteristics because of its higher carrier mobility and higher electric breakdown field, which helps reduce the size of the epitaxial layers. The reduction in the size of the drift layer helps reduce the low drift resistance, which in turn reduces the forward voltage drop and conduction losses [19]. Table 2 presents a comparison between material properties of Si, 6H-SiC, and 4H-SiC semiconductors [19].

[19].

𝜖

| Parameters                                                                                                                                                                                                                                            | 4H-SiC                | 6H-SiC              | Si                 | GaN                   | Diamond               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|---------------------|--------------------|-----------------------|-----------------------|
| Table 2.  4H-SiC, 6H-SiC, Si, and diamond material properties [19].  Parameters  𝐸௚ (ଷ଴଴ ௄)   (eV)  𝑛௜ (ଷ଴଴ ௄) (cm 3 )  - 𝐸௖௥௜௧ (ଷ଴଴ ௄)   (V/cm)  E g ( 300 K ) (eV) n i ( 300 K ) (cm - 3 ) E crit ( 300 K ) e S m n max , ⊥ (cm 2 m p max , ⊥ (cm 2 | 3.26                  | 2.90                | 1.12               | 3.39 2 × 10 -         | 5.47 -                |
|                                                                                                                                                                                                                                                       | 1.5 × 10 - 8          | 2.1 × 10 - 5        | 10 10              | 10                    | 10 20                 |
| (V/cm)                                                                                                                                                                                                                                                | 4H-SiC  2.2 × 10 6    | 6H-SiC  2.5 × 10 6  | Si  0.25 × 10 6    | GaN  3.3 × 10 6       | Diamond  5.6 × 10 6   |
|                                                                                                                                                                                                                                                       | 3.26  9.66            | 2.90  9.66          | 1.12  11.7         | 3.39  9.5             | 5.47  5.7             |
| /Vs)                                                                                                                                                                                                                                                  | - 8 1000 - 1140       | - 5 415             | 1400               | - 10 1250             | - 1800                |
| /Vs)                                                                                                                                                                                                                                                  | 1.5 × 10 124          | 2.1 × 10 99         | 10 10 450          | 2 × 10 200            | 10 20                 |
| VSAT (cm/s)                                                                                                                                                                                                                                           | 2.2 × 10 6 2.1 × 10 7 | 2.5 × 10 6 2 × 10 7 | 0.25 × 10 6   10 7 | 3.3 × 10 6 2.7 × 10 7 | 5.6 × 10 6 2.7 × 10 7 |

ௌ

9.66

9.66

11.7

9.5

5.7

𝜇௡,௠௔௫ ⊥ (cm 2 /Vs) 1000 -1140 415 1400 1250 1800 𝜇௣,௠௔௫ ⊥ (cm 2 /Vs) 124 99 450 200 𝑉 ௌ஺் (cm/s) 2.1 × 10 7 2 × 10 7 10 7 2.7 × 10 7 2.7 × 10 7 SiC-based semiconductors are relatively new in the power industry. The fi rst commercial power device was introduced in 2001 as the SiC-based Scho tt ky diode [20]. Despite being relatively new in the commercial marketplace, signi fi cant improvements have been made over the years. One of the SiC leading manufacturers, Cree, was the fi rst to announce in 2012 the production of 150 mm SiC wafers and a range of power MOSFETs [21]. Initially, SiC wafers su ff ered from defects such as micropipes; however, wafer quality has improved quite signi fi cantly over these past years. The defects were in the range of 510/cm 2  in 2006 [22], improving to 0.75/cm 2  in 2014 [23], and recently, the Japanese manufacturer Showa Denko lowered the defect densities of 150 mm (6 inch) SiC wafers by up to  0.25/cm 2   [2].  SiC  devices'  cost  is  expected  to  decrease  gradually  as  manufacturers SiC-based semiconductors are relatively new in the power industry. The first commercial power device was introduced in 2001 as the SiC-based Schottky diode [20]. Despite being relatively new in the commercial marketplace, significant improvements have been made over the years. One of the SiC leading manufacturers, Cree, was the first to announce in 2012 the production of 150 mm SiC wafers and a range of power MOSFETs [21]. Initially, SiC wafers suffered from defects such as micropipes; however, wafer quality has improved quite significantly over these past years. The defects were in the range of 5-10/cm 2 in 2006 [22], improving to 0.75/cm 2 in 2014 [23], and recently, the Japanese manufacturer Showa Denko lowered the defect densities of 150 mm (6 inch) SiC wafers by up to 0.25/cm 2 [2]. SiC devices' cost is expected to decrease gradually as manufacturers improve the fabrication processes by improving the production capabilities and wafer sizes. Figure 5 illustrates the current and future market demand for the 150 mm SiC wafer size in comparison to 100 mm [24], while Figure 6 depicts the key milestones in the research and development in SiC technology. Due to the improvements in wafer fabrication and

Energies

2023

,

16

, x FOR PEER REVIEW

7  of  28

improve the fabrication processes by improving the production capabilities and wafer sizes. Figure 5 illustrates the current and future market demand for the 150 mm SiC wafer

improve the fabrication processes by improving the production capabilities and wafer

7 of 27 sizes. Figure 5 illustrates the current and future market demand for the 150 mm SiC wafer size in comparison to 100 mm [24], while Figure 6 depicts the key milestones in the re

search and development in SiC technology. Due to the improvements in wafer fabrication size in comparison to 100 mm [24], while Figure 6 depicts the key milestones in the re- -

increased production volumes, SiC power devices' costs have significantly declined since the introduction of first SiC Schottky diode and MOSFETs. The initial cost of the SiC Schottky diode was USD 5000 for a two-inch wafer, USD 1200-USD 1400 in 2009 for a four-inch wafer, and USD 600-USD 750 in 2012 [25]. Also, during this time span, SiC power devices sales increased by three times over the years [26]. and increased production volumes, SiC power devices' costs have signi i fi cantly declined since the introduction of fi rst SiC Scho tt ky diode and MOSFETs. The initial cost of the SiC Scho o tt ky diode was USD 5000 for a two-inch wafer, USD 1200-USD 1400 in 2009 for a four-inch wafer, and USD 600-USD 750 in 2012 [25]. Also, during this time span, SiC power devices sales increased by three times over the years [26]. and increased production volumes, SiC power devices' costs have sign fi cantly declined since the introduction of fi rst SiC Scho tt ky diode and MOSFETs. The initial cost of the SiC Sch tt ky diode was USD 5000 for a two-inch wafer, USD 1200-USD 1400 in 2009 for a four-inch wafer, and USD 600-USD 750 in 2012 [25]. Also, during this time span, SiC power devices sales increased by three times over the years [26].

search and development in SiC technology. Due to the improvements in wafer fabrication

Figure 5. Production of various SiC substrate wafers. Figure 5. Production of various SiC substrate wafers. Figure 5. Production of various SiC substrate wafers.

<!-- image -->

Figure 6. Milestones in SiC power electronics development. Figure 6. Milestones in SiC power electronics development. Figure 6. Milestones in SiC power electronics development.

<!-- image -->

Cree is one of the world's largest growing power semiconductor manufacturers. Fig- ure 7 shows the Cree SiC power devices' costs trend over the past few years [27]. The performance of SiC power devices has also gradually improved over the last years since their introduction in 2001. Figure 8 illustrates the current density growth from 2010 to 2012 and a prediction of future trends up to 2020 [28]. For high-voltage SiC power devices, there is a steady increase in current density, while for lower-voltage SiC power devices, the current density is expected to slow down around the end of this decade due to the cost of SiC modules and long-term reliability [29]. In 2005, Scho tt ky diodes were available at current rating up to 25 A; nowadays, the current ratings of these devices can reach 50 A [30]. Also, signi fi cant progress has been made in SiC power MOSFETs technology, which led to an increase in the performance of each generation of devices. Due to SiC maturity over GaN, higher breakdown voltage and current capabilities are commercially available (SiC MOSFETs available up to 1.7 kV and thyristor up to 6.5 kV), while Wolfspeed (Cree) successfully tested 10 kV MOSFETs and further developed 15 kV SiC [31]. In 2011, a 1200 Cree is one of the world's largest growing power semiconductor manufacturers. Fig ure 7 shows the Cree SiC power devices' costs trend over the past few years [27]. The performance of SiC power devices has also gradually improved over the last years since their introduction in 2001. Figure 8 illustrates the current density growth from 2010 to 2012 and a prediction of future trends up to 2020 [28]. For high-voltage SiC power devices, there is a steady increase in current density, while for lower-voltage SiC power devices, the current density is expected to slow down around the end of this decade due to the cost of SiC modules and long-term reliability [29]. In 2005, Scho tt ky diodes were available at current rating up to 25 A; nowadays, the current ratings of these devices can reach 50 A [30]. Also, signi fi cant progress has been made in SiC power MOSFETs technology, which led to an increase in the performance of each generation of devices. Due to SiC maturity over GaN, higher breakdown voltage and current capabilities are commercially available (SiC MOSFETs available up to 1.7 kV and thyristor up to 6.5 kV), while Wolfspeed (Cree) successfully tested 10 kV MOSFETs and further developed 15 kV SiC [31]. In 2011, a 1200 Cree is one of the world's largest growing power semiconductor manufacturers. Figure 7 shows the Cree SiC power devices' costs trend over the past few years [27]. The performance of SiC power devices has also gradually improved over the last years since their introduction in 2001. Figure 8 illustrates the current density growth from 2010 to 2012 and a prediction of future trends up to 2020 [28]. For high-voltage SiC power devices, there is a steady increase in current density, while for lower-voltage SiC power devices, the current density is expected to slow down around the end of this decade due to the cost of SiC modules and long-term reliability [29]. In 2005, Schottky diodes were available at current rating up to 25 A; nowadays, the current ratings of these devices can reach 50 A [30]. Also, significant progress has been made in SiC power MOSFETs technology, which led to an increase in the performance of each generation of devices. Due to SiC maturity over GaN, higher breakdown voltage and current capabilities are commercially available (SiC MOSFETs available up to 1.7 kV and thyristor up to 6.5 kV), while Wolfspeed (Cree) successfully tested 10 kV MOSFETs and further developed 15 kV SiC [31]. In 2011, a 1200 V SiC MOSFET had switching losses around 0.78 mJ, and in 2013, the average switching losses of the next-generation SiC power MOSFETs were 0.56 mJ, i.e., a 28% decrease [25]. These performance enhancements were the results of the recent advances made in material development and fabrication processes [32].

Energies

2023

9

8

7

6

5

4

3

2

1

0

A/mm 2

,

16

, x FOR PEER REVIEW

8  of  28

V SiC MOSFET had switching losses around 0.78 mJ, and in 2013, the average switching losses of the next-generation SiC power MOSFETs were 0.56 mJ, i.e., a 28% decrease [25].

These performance enhancements were the results of the recent advances made in mate-

8 of 27 V SiC MOSFET had switching losses around 0.78 mJ, and in 2013, the average switching losses of the next-generation SiC power MOSFETs were 0.56 mJ, i.e., a 28% decrease [25].

These performance enhancements were the results of the recent advances made in mate- rial development and fabrication processes [32].

rial development and fabrication processes [32].

Figure 7. Decline of device cost for Cree SiC products over the last years [27]. Figure 7. Decline of device cost for Cree SiC products over the last years [27]. Figure 7. Decline of device cost for Cree SiC products over the last years [27].

<!-- image -->

Figure 8. Current density evolution for SiC [16]. Figure 8. Current density evolution for SiC [16].

<!-- image -->

2010

2011

2012

2013

2014

2015

2016

2017

2018

2019

2020

Figure 8. Current density evolution for SiC [16]. ompanies in the market. Table 3 gives a list of these At  present,  SiC  power  electronics'  technological  development  and  production  is   to mainly carried out by a few key companies in the market. Table 3 gives a list of these  opcompanies, their market share, and their revenue in 2010 [26]. In 2021, the global SiC  onpower electronics industry was estimated to be worth USD 1.090 million and is due to   Jareach USD 6.297 million by 2027 [33]. The companies leading the research and develop- pan ment are mainly In fi neon, Mitsubishi Electric, ON Semiconductor, and STMicroelectronics. SiC fabrication facilities are mainly in Europe (55%), the United States (41%), and Japan (2%). By 2020, the market share of SiC devices is expected to shift radically, with Japan capturing 35% of the global market share due to considerable investment from the JapaAt  present,  SiC  power  electronics'  technological  development  and  production  is mainly carried out by a few key c companies, their market share, and their revenue in 2010 [26]. In 2021, the global SiC power electronics industry was estimated to be worth USD 1.090 million and is due reach USD 6.297 million by 2027 [33]. The companies leading the research and devel ment are mainly In fi neon, Mitsubishi Electric, ON Semiconductor, and STMicroelectr ics. SiC fabrication facilities are mainly in Europe (55%), the United States (41%), and pan (2%). By 2020, the market share of SiC devices is expected to shift radically, with Ja capturing 35% of the global market share due to considerable investment from the Japanese government and industry [34]. Toyota is one of the Japanese car manufacturers currently testing hybrid vehicles and buses based on SiC power devices [35]. At present, SiC power electronics' technological development and production is mainly carried out by a few key companies in the market. Table 3 gives a list of these companies, their market share, and their revenue in 2010 [26]. In 2021, the global SiC power electronics industry was estimated to be worth USD 1.090 million and is due to reach USD 6.297 million by 2027 [33]. The companies leading the research and development are mainly Infineon, Mitsubishi Electric, ON Semiconductor, and STMicroelectronics. SiC fabrication facilities are mainly in Europe (55%), the United States (41%), and Japan (2%). By 2020, the market share of SiC devices is expected to shift radically, with Japan capturing 35% of the global market share due to considerable investment from the Japanese government and industry [34]. Toyota is one of the Japanese car manufacturers currently testing hybrid vehicles and buses based on SiC power devices [35].

nese government and industry [34]. Toyota is one of the Japanese car manufacturers curTable 3. Distribution of leading SiC power electronics device makers by market share in 2021.

| Company             | SiC Power Electronics Market Growth   | Headquarters   |
|---------------------|---------------------------------------|----------------|
| STMicroelectronics  | 55%                                   | Switzerland    |
| Infineon            | 126%                                  | Germany        |
| ONSemiconductor     | 43%                                   | USA            |
| Wolfspeed           | 53%                                   | USA            |
| Mitsubishi Electric | 8%                                    | Japan          |
| ROHM                | 5%                                    | USA            |

rently testing hybrid vehicles and buses based on SiC power devices [35].

## 2.2. Performance Advances in GaN

GaNoffers many features such as faster switching speed, smaller size, higher efficiency, and lower cost. Currently, GaN-based devices are already commercialized for lasers and RF applications, while for high-power applications, GaN technology is still at its early stage. Due to the lack of abundance of high-quality, defect-free GaN substrates, GaN epilayers are designed on foreign substrates such as Si, SiC, and sapphire. Among these, GaN epilayers grown on Si offer lower cost and better performance in comparison to the other substrate materials. AlGaN/GaN heterostructure field-effect transistors (HFETs) and high electron mobility transistor (HEMTs) have been commercially available since 2005 and have mostly been used in RF and optoelectronics. Recently, many power electronic design companies have opted for AlGaN/GaN HEMTs in various power applications, such as power converters. The most interesting property is the existence of two-dimensional electron gas (2DEG) formed in AlGaN/GaN structures due to the discontinuity difference between GaN and AlGaN. 2DEG is a gas of electrons free to move in two dimensions but tightly confined in the third. This tight confinement leads to quantized energy levels for motion in the third direction. Also, due to presence of polarization fields for AlGaN/GaN HEMTs, this allows for a high 2DEG concentration with large mobility values. Table 4 shows GaN epilayers grown on different substrates and their properties [36].

Table 4. GaN epilayers grown on different substrate properties [36].

|                               | GaN   | SiC   | Sapphire   | Si    |
|-------------------------------|-------|-------|------------|-------|
| κ , Wm 1 K · - · - 1          | 150 - | 420 - | 35         | 150 - |
| κ (T - η )                    | T 1.4 | T 1.3 | T - 1      | T 1.3 |
| TBR, × 10 - 8 W 1 m 2 - · · K |       |       |            |       |
| Interface                     |       | 3.3   | 12         | 3.3   |
| Temperature, ◦ C              |       | 190   | 240        | 300   |

The developed power GaN HEMTs are increasingly entering the market and are well suited for high-power and high-voltage applications. This market is projected to achieve a significant performance improvement up to 100 times in comparison to Si [37]. GaN HEMTs for normally on and normally off architectures are commercially available in the voltage breakdown range of 200 to 650 V. GaN-based MOSFETs are still undergoing research and development, and different manufacturers have developed and commercialized SiO2/GaNinterfaced MOSFETs and AlGaN/GaN-based MOS-HEMTs with high blocking voltage (2.5 kV) and high channel mobility values (170 cm 2 /Vs). In 2010, International Rectifier announced their first GaN on silicon HEMT for high-power applications. This release was quickly followed by the launch of GaN devices in the range of 200 V by Efficient Power Conversion (EPC). The success of these devices was due to improvements in GaN-on-silicon epitaxy techniques [38]. This technique facilitated the creation of substrates with less impressive properties but at relatively low prices compared to GaN on SiC or GaN substrates. The price of the 4-inch silicon wafer was USD 100 for GaN epitaxy, while the 4-inch SiC wafer was at USD 130 and USD 7500 for the GaN wafer [39]. Figure 9 depicts the milestones and development of GaN power electronics devices throughout the past few years. The first GaN power devices were introduced during early 2010 to late 2011, where the first GaN power devices were released by International Rectifier, and since then, several successfully developed transistors have been reported, such as the GaN transistors (eGaN), 600 V GaN HEMTs, and 600 V GaN-on-SiC transistor. From early 2012 to mid-2014, the 6-inch GaN on Si was developed, whereas the 8-inch GaN on SiC was developed from mid-2014 to late 2016. Moreover, from 2018 to late 2019, the GaN system reached 150 A at 650 V [40].

dicted future trend up to 2020 [41]. Other GaN advancements include moving to larger 8- inch GaN-on-silicon wafers [42] and the introduction of gate injection transistors (GITs) in

the power electronics market. GITs are tailor-made to perform well in the high-voltage range, with some of the devices rated up to 600 V. The major progress in GaN devices'

early 2012 to mid-2014, the 6-inch GaN on Si was developed, whereas the 8-inch GaN on SiC

was developed from mid-2014 to late 2016. Moreover, from 2018 to late 2019, the GaN system reached 150 A at 650 V [40].

research and development is a tt

ributed entirely to research labs and universities. The Uni- versity of California Santa Barbara has been the leader in the development of high-quality

GaN devices for power electronics [42].

The performance of GaN power devices has also improved since their introduction in 2010. Figure 10 illustrates the growth in current density from 2010 to 2012 and its pre-

<!-- image -->

transistor

Most companies involved in GaN devices are from the U.S. apart from MicroGaN and In fi neon Technologies. Initially, E ffi cient Power Conversion (EPC), Transphorm, and MicroGaN were solely involved in the development of GaN power electronics devices. Now, other major companies such as Panasonic, In fi neon, and Texas Instruments, who have been traditionally involved with Si-based devices, are also developing GaN devices. GaN power market was worth USD 126 million in 2021 and is expected to reach USD 6 billion  by  2027  [43].  Table  5  shows  GaN  devices'  development  stage  and  the  di ff erent product types upon which each company is focusing [44]. The performance of GaN power devices has also improved since their introduction in 2010. Figure 10 illustrates the growth in current density from 2010 to 2012 and its predicted future trend up to 2020 [41]. Other GaN advancements include moving to larger 8-inch GaN-on-silicon wafers [42] and the introduction of gate injection transistors (GITs) in the power electronics market. GITs are tailor-made to perform well in the high-voltage range, with some of the devices rated up to 600 V. The major progress in GaN devices' research and development is attributed entirely to research labs and universities. The University of California Santa Barbara has been the leader in the development of high-quality GaN devices for power electronics [42]. Figure 9. Milestones in GaN power electronics development.

Most companies involved in GaN devices are from the U.S. apart from MicroGaN and Infineon Technologies. Initially, Efficient Power Conversion (EPC), Transphorm, and MicroGaN were solely involved in the development of GaN power electronics devices. Now, other major companies such as Panasonic, Infineon, and Texas Instruments, who have been traditionally involved with Si-based devices, are also developing GaN devices. GaN power market was worth USD 126 million in 2021 and is expected to reach USD 6 billion by 2027 [43]. Table 5 shows GaN devices' development stage and the different product types upon which each company is focusing [44]. Most companies involved in GaN devices are from the U.S. apart from MicroGaN and In fi neon Technologies. Initially, E ffi cient Power Conversion (EPC), Transphorm, and MicroGaN were solely involved in the development of GaN power electronics devices. Now, other major companies such as Panasonic, In fi neon, and Texas Instruments, who have been traditionally involved with Si-based devices, are also developing GaN devices. GaN power market was worth USD 126 million in 2021 and is expected to reach USD 6 billion  by  2027  [43].  Table  5  shows  GaN  devices'  development  stage  and  the  di ff erent product types upon which each company is focusing [44].

Figure 10. Current density trend for GaN [41].

<!-- image -->

Figure 10.

Current density trend for GaN [41].

Table 5. Development stages and product types for companies involved in GaN power electronics [44].

| Vendor        | Products     | Products      | Technology       | Development   | Development   | Product Types   | Product Types   | Product Types   |
|---------------|--------------|---------------|------------------|---------------|---------------|-----------------|-----------------|-----------------|
| Vendor        | Open Market  | Closed Market | Foundry Services | Collaborative | In-House      | Discrete        | IC              | Module          |
| IRF           |              | glyph[check]  |                  |               |               | glyph[check]    |                 | glyph[check]    |
| EPC           | glyph[check] |               |                  |               |               | glyph[check]    |                 |                 |
| Transphorm    |              | glyph[check]  |                  |               |               |                 |                 | glyph[check]    |
| Fujitsu       |              |               |                  |               | glyph[check]  |                 |                 |                 |
| Sanken        |              |               |                  |               | glyph[check]  |                 | glyph[check]    |                 |
| MicroGaN      |              | glyph[check]  | glyph[check]     |               |               | glyph[check]    |                 |                 |
| Infineon      |              |               |                  |               | glyph[check]  | glyph[check]    |                 |                 |
| HRL           |              |               |                  |               | glyph[check]  | glyph[check]    |                 |                 |
| Panasonic     |              |               |                  |               | glyph[check]  | glyph[check]    | glyph[check]    |                 |
| STM           |              |               |                  |               | glyph[check]  | glyph[check]    | glyph[check]    |                 |
| RFMD          |              | glyph[check]  | glyph[check]     |               |               | glyph[check]    |                 |                 |
| Toshiba       |              |               |                  |               | glyph[check]  | glyph[check]    |                 |                 |
| GaN Systems   |              |               |                  |               | glyph[check]  | glyph[check]    |                 |                 |
| NXP           |              |               |                  | glyph[check]  |               | glyph[check]    |                 |                 |
| TI            |              |               |                  |               | glyph[check]  | glyph[check]    | glyph[check]    |                 |
| Freescale     |              |               |                  |               | glyph[check]  | glyph[check]    | glyph[check]    |                 |
| Powdec        |              |               |                  |               | glyph[check]  | glyph[check]    |                 |                 |
| Renesas       |              |               |                  |               | glyph[check]  | glyph[check]    |                 |                 |
| Furukawa      |              |               |                  |               | glyph[check]  | glyph[check]    |                 |                 |
| POWI          |              |               |                  |               | glyph[check]  |                 | glyph[check]    |                 |
| ONSemi        |              |               |                  | glyph[check]  |               | glyph[check]    | glyph[check]    |                 |
| Intersil      |              |               |                  | glyph[check]  | glyph[check]  |                 | glyph[check]    |                 |
| Alpha &amp; Omega |              |               |                  |               | glyph[check]  | glyph[check]    |                 |                 |

## 2.3. Performance Advances in Diamond

Diamond's outstanding physical and electrical characteristics, which includes the highest known thermal conductivity, excellent electrical insulator properties, high breakdown voltage, and high carrier mobility, make it theoretically the best semiconductor for the next generation of power electronic devices [45]. Some of the potential applications include high-voltage power electronics, high-frequency high-power devices, and high-power optoelectronics devices, such as laser diodes and LEDs. During the last few years, diamond growth techniques have been significantly enhanced, and doping control methods for p, p+, n-type, and intrinsic diamond have been designed. Therefore, the electrical properties of diamond devices can now be characterized not just theoretically but also experimentally through device structures. Recently, planar diamond power Schottky barrier diode (SBD) test results reported a maximum breakdown field of 9.5 MV/m [46], blocking voltage of Vmax &gt; 10 kV [47,48], high current operation above 20 A [49], and low switching losses with fast operation [50], making diamond SBDs an attractive material for power electronics applications. The first diamond-based power switching device was introduced in 1980s by Prins, using natural diamond crystals to form a bipolar junction transistor (BJT) with the usage of diamond crystals as the base electrode, while the n-type emitter and collector region were formed by carbon ion implantation [51]. However, due to device's geometrical issues associated with the fabrication process, the current gain was less than unity. Since then, other diamond-based power semiconductor devices such as metal-semiconductor FETs (MISFETs) [52] and metal-insulator-semiconductor FETs (MISFETs) were also designed using diamond crystals through ion implantation or diffusion doping. In the last decade, the situation has drastically changed with the introduction of various techniques of diamond epitaxial growth by chemical vapor deposition (CVD), high-pressure high-temperature (HPHT), microwave-enhanced chemical vapor deposition (MWCVD), and mosaic-type method. Producing high-quality defect-free wafers produced from diamond crystals is still a big challenge even with the application of different single-crystal growth techniques. With the HPHT technique, high-quality defect-free wafers of only few millimeters have been achieved so far, while for the SiC wafer. sizes up to 150 mm are available. The MWCVDand mosaic-type techniques are quite promising and are approaching wafer sizes of 2 inches, even though the defect density needs to be reduced in order to commercialize

single-crystal growth techniques. With the HPHT technique, high-quality defect-free wa- fers of only few millimeters have been achieved so far, while for the SiC wafer. sizes up to

12 of 27 150 mm are available. The MWCVD and mosaic-type techniques are quite promising and are approaching wafer sizes of 2 inches, even though the defect density needs to be re-

duced in order to commercialize the device on a large scale. Another interesting technique the device on a large scale. Another interesting technique involves the heteroepitaxy of diamond on iridium, enabling the development of diamond films of up to 4 inches. Further development is required to reproduce controlled processes for manufacturing using this technique. Additionally, single-wafer material manufacturing for electronic applications is significantly impacted due to the difficulty of n-type doping with the lack of an efficient charge donor. Since p-type doping of naturally insulating diamond can easily be achieved by using boron, a great deal of development is being achieved on the fabrication of unipolar devices. Some of the CVD equipment makers for developing high-quality diamond wafers are shown in Figure 11 [53]. They can be broadly categorized into two groups based on method: hot filament chemical vapor deposition (HF CVD) and MW CVD. involves the heteroepitaxy of diamond on iridium, enabling the development of diamond fi lms of up to 4 inches. Further development is required to reproduce controlled processes for manufacturing using this technique. Additionally, single-wafer material manufacturing for electronic applications is signi fi cantly impacted due to the di ffi culty of n-type doping with the lack of an e ffi cient charge donor. Since p-type doping of naturally insulating diamond can easily be achieved by using boron, a great deal of development is being achieved on the fabrication of unipolar devices. Some of the CVD equipment makers for developing high-quality diamond wafers are shown in Figure 11 [53]. They can be broadly categorized into two groups based on method: hot fi lament chemical vapor deposition (HF CVD) and MW CVD.

Figure 11. CVD equipment makers for development of high-quality diamond wafers. Figure 11. CVD equipment makers for development of high-quality diamond wafers.

<!-- image -->

## 2.4. Figure of Merit (FOM)

2.4. Figure of Merit (FOM) Various researchers have used numerous fi gures of merit (FOM) in order to evaluate di ff erent  semiconductor  materials  performance.  In  1965,  Johnson  [54]  evaluated  WBG semiconductor material for the fi rst time and proposed an equation that could help identify possible future semiconductor materials. This author proposed that a semiconductor transistor performance can be evaluated using the critical breakdown fi eld 𝐸௖ and the electron drift velocity Vୱୟ୲ and came up with a FOM as JM = (E  V ୡ ୱୟ୲ /π) ଶ .  Later, Keyes [33]  de fi ned  another  FOM  to  evaluate  semiconductors  device  performance  as KM = λඥVୱୟ୲ /ε ,  where λ is  the  thermal  conductivity, and ε is  the  dielectric  constant.  In  this FOM, power frequency for low-voltage transistors is also taken into account. When comparing these two FOMs, it becomes clear that saturation velocity and dielectric constant can be used on a broader level to evaluate some of the semiconductor devices. It is challenging, when evaluating a device's performance completely, to consider simultaneously Various researchers have used numerous figures of merit (FOM) in order to evaluate different semiconductor materials performance. In 1965, Johnson [54] evaluated WBG semiconductor material for the first time and proposed an equation that could help identify possible future semiconductor materials. This author proposed that a semiconductor transistor performance can be evaluated using the critical breakdown field Ec and the electron drift velocity Vsat and came up with a FOM as JM = ( Ec Vsat/ π ) 2 . Later, Keyes [33] defined another FOM to evaluate semiconductors device performance as KM = λ √ Vsat/ , # where λ is the thermal conductivity, and # is the dielectric constant. In this FOM, power frequency for low-voltage transistors is also taken into account. When comparing these two FOMs, it becomes clear that saturation velocity and dielectric constant can be used on a broader level to evaluate some of the semiconductor devices. It is challenging, when evaluating a device's performance completely, to consider simultaneously the material's bandgap, thermal conductivity, and critical breakdown field.

the material's bandgap, thermal conductivity, and critical breakdown fi eld. To improve the e ffi ciency and performance of semiconductor devices, it is essential to minimize power losses. Baliga [55] proposed the FOM, BM = ε μ E ଷ ୡ ,  where µ represents the carrier mobility. This FOM helps reduce the conduction losses in power FETs. This FOM can only be evaluated for low frequencies, as it assumes that power losses are To improve the efficiency and performance of semiconductor devices, it is essential to minimize power losses. Baliga [55] proposed the FOM, BM = #m Ec 3 , where m represents the carrier mobility. This FOM helps reduce the conduction losses in power FETs. This FOMcan only be evaluated for low frequencies, as it assumes that power losses are only due to current flowing through the on-resistance. To include higher-frequency switching losses, the author proposed another FOM, BHFM = m Ec 2 , which assumes that losses occur when charging and discharging the input capacitance of FETs [56]. Another important factor contributing to power losses is the thermal conductivity. Shenai et al. defined three different thermal FOMs to incorporate various scenarios and factors. The first case scenario considers that if the thermal conductivity properties of heat sink material are different

compared to active device area, then the FOM is defined as QF1 = λ s A. In the case of perfect heat sink material and with the assumption of an active device area at ambient temperature, the FOM can be defined as QF2 = λ s A Ec . Finally, excluding any assumption related to heat sink material or geometry, the FOM can be defined as QF3 = s A. For all three cases, s Ais equal to Baliga's FOM (i.e., #m Ec 3 ) [57].

As more accurate data relating to new semiconductor materials properties became available, FOMs slowly evolved over time. Chow [58] discussed the problem with the assumption of the universal relationship between energy bandgap and breakdown voltage value when using Baliga's FOM for low frequencies. This universal relationship is not true for WBG semiconductors and hence cannot be effectively used to evaluate some devices. Baliga's FOM for higher frequencies is based on the assumption of linear relationship between energy bandgap and critical electric field, which is not true as well. Hence, there is a need for further investigation to develop new FOMs. Table 6 shows some FOMs normalized against Si, which were contributed from various researchers [59].

Table 6. FOMs contributed by various researchers [59].

| Material            | JM   | KM   | BM     |    BHFM | QF1     | QF2       | QF3    |
|---------------------|------|------|--------|---------|---------|-----------|--------|
| Si                  | 1.00 | 1.00 | 1.00   |    1    | 1.00    | 1.00      | 1.00   |
| Ge                  | -    | -    | 0.13   |    0.28 | 0.05    | 0.02      | 0.13   |
| Diamond ( n )       | 5330 | 31   | 14,860 | 1080    | 198,100 | 5,784,410 | 14,860 |
| Diamond (p)         | 6220 | 32   | 11,700 |  850    | 155,990 | 4,554,840 | 11,700 |
| InP                 | 13   | 0.72 | 10     |    6.6  | 26      | 38        | 10     |
| InN ( m = 3000 )    | 58   | 6    | 46     |   19    | 150     | 460       | 46     |
| InN ( m = 30, 000 ) | 58   | 6    | 450    |  185    | 1500    | 4570      | 450    |
| AlP                 | -    | -    | 6.5    |    1.5  | -       | -         | 6.5    |
| AIN ( m = 14 )      | 5120 | 2.6  | 390    |   14    | 660     | 25,520    | 390    |
| AlN ( m = 1090 )    | 5120 | 2.6  | 31,670 | 1100    | 52,890  | 2,058,620 | 31,670 |
| AlAs                | 630  | -    | 7.3    |    2    | -       | -         | 7.3    |
| AlSb                | 270  | -    | 1.2    |    0.59 | -       | -         | 1.2    |
| GaAs                | 11   | 0.45 | 28     |   16    | 9.4     | 16        | 28     |
| GaN                 | 790  | 1.8  | 910    |  100    | 910     | 10,300    | 910    |
| GaP                 | 37   | 0.73 | 16     |    3.8  | 9.4     | 41        | 16     |
| BP                  | -    | -    |        |    0.95 | -       | -         | -      |
| ZnSe                | -    | -    | 84     |   17    | -       | -         | 84     |
| ZnS                 | -    | -    | 94     |   17    | -       | -         | 94     |
| ZnO                 | -    | -    | 110    |   14    | -       | -         | 106    |
| CdTe                | -    | -    | 5.3    |    3    | -       | -         | 5.3    |
| CdSe                | -    | -    | 7.1    |    3.3  | -       | -         | 7.1    |
| CdS                 | -    | -    | 14     |    6.1  | -       | -         | 14     |
| HgS                 | -    | -    | -      |    0.45 | -       |           |        |
| 6H-SiC              | 260  | 5.1  | 90     |   13    | 300     | 2440      | 90     |
| 3C-SiC              | 110  | 5.8  | 40     |   12    | 130     | 550       | 40     |
| 4H-SiC              | 410  | 5.1  | 290    |   34    | 950     | 9630      | 290    |
| SnO2                | -    | -    | -      |   26    | -       | -         | -      |
| In2O3               | -    | -    | -      |    1.8  |         |           |        |

With the availability of new datasets for the critical electric field, Hudgins et al. [14] proposed a new derivation for the relationship between the critical electric field ( # c, V/cm) and bandgap energy ( EG , eV) for direct and indirect bandgap semiconductors and a new specific on-resistance ( Ronsp ) to evaluate all semiconductor materials. The new generic relationship between critical electric field and bandgap energy is proposed as # C = ( a EG ) n , where a is a prefactor fit parameter, and n is the exponent fit parameter. Table 7 shows values of a and n for direct, indirect, and for general semiconductor materials.

Table 7. Pre-factor fit ( a ) and exponent fit ( n ) parameters [14].

|                       | a            |     n |
|-----------------------|--------------|-------|
| All semiconductors    | 1.7485 × 105 | 2.359 |
| Indirect bandgap only | 2.3818 × 105 | 1.995 |
| Direct bandgap only   | 1.7348 × 105 | 2.506 |

Table 7.

Table 7.

Pre-factor

Pre-factor fi

t (

a

) and exponent fi

t (

a

) and exponent

All semiconductors

All semiconductors

Indirect bandgap only

Indirect bandgap only

n

) parameters [14]. .

) parameters [14]

𝒂

𝒂

1.7485 × 105

1.7485 × 105

2.3818 × 105

2.3818 × 105

𝒏

𝒏

2.359

2.359

1.995

1.995

Direct bandgap only

Direct bandgap only

1.7348 × 105

2.506

1.7348 × 105

2.506

Using Table 7, the equation of the critical electric field for indirect semiconductors is # C = 2.38 @ 105 ( EG ) 2 , and for direct bandgap, # C = 1.73 @ 105 ( EG ) 2.5 . Using Table 7, the equation of the critical electric fi eld for indirect semiconductors is εେ େ = 2.38 @ 105 (EG) ଶ , and for direct bandgap, εେ େ = 1.73 @ 105 (EG) ଶ.ହ . Using Table 7, the equation of the critical electric fi eld for indirect semiconductors is ε = 2.38 @ 105 (EG) ଶ , and for direct bandgap, ε = 1.73 @ 105 (EG) ଶ.ହ .

Figures 12 and 13 show the original and new critical field equation difference for direct and indirect semiconductors. Figures 12 and 13 show the original and new critical fi eld equation di i ff erence for direct and indirect semiconductors. Figures 12 and 13 show the original and new critical fi eld equation d ff erence for direct and indirect semiconductors.

Figure 12. Direct bandgap semiconductors and new and old critical fi eld di i ff erence [14]. . Figure 12. Direct bandgap semiconductors and new and old critical field difference [14]. Figure 12. Direct bandgap semiconductors and new and old critical fi eld d ff erence [14]

<!-- image -->

Figure 13. Indirect bandgap semiconductors and new and old critical fi eld di i ff erence [14]. . Figure 13. Indirect bandgap semiconductors and new and old critical fi eld d ff erence [14] Figure 13. Indirect bandgap semiconductors and new and old critical field difference [14].

<!-- image -->

Speci i fi c  on-resistance  in  terms  of  bandgap  and  voltage  breakdown  for  indirect bandgap semiconductors was de fi ned by Hudgins et al. [60] as follows: Spec fi c  on-resistance  in  terms  of  bandgap  and  voltage  breakdown  for  indirect bandgap semiconductors was de fi ned by Hudgins et al. [60] as follows: Specific on-resistance in terms of bandgap and voltage breakdown for indirect bandgap semiconductors was defined by Hudgins et al. [60] as follows:

<!-- formula-not-decoded -->

where Ronsp is the specific on-resistance, VB is the breakdown voltage, EG denotes the bandgap energy, m e is the electron mobility, and # r represents the relative permittivity. And for direct bandgap, the following is true:

<!-- formula-not-decoded -->

Figure 14 shows the specific on-resistance for direct and indirect bandgap calculated using the new equations in comparison with old generic, specific on-resistance equationbased calculations.

fi t (

fi

n

t (

Hence, Hudgins et al. proved that in the light of the new available data and derived equations, WBG semiconductors, especially GaN and SiC, are more favorable than previously thought [61].

Huang [62], on the other hand, proposed four new FOMs for different scenarios. If Ron and Qgd are known, HDFOM can be used to evaluate different devices and is defined as HDFOM = √ Ron · Qgd. HMFOM can be used to compare relative losses among the different devices and is defined as HFOM = Ec √ m , while HCAFOM can be used to compare optimal chip area/size and is defined as HCAFOM = # √ m Ec 2 . For the comparison of junction temperatures of different devices, HTFOM = s th / # Ec is employed. Table 8 shows a comparison of various semiconductor materials normalized against silicon, using the developed HMFOM, HCFOM, and HTFOM merits [10].

Table 8. Comparison of various semiconductor material using new FOMs (normalized against silicon) [10].

| Semiconductor Material   |   Electron Mobility m (cm 2 /V-s) |   Relative Dielectric Constant e |   Critical Field Ec (kV/cm) |   Thermal Conductivity s th (W/m-K) |   HMFOM Ec √ m |   HCFOM # √ m Ec 2 |   HTFOM s th / # Ec |
|--------------------------|-----------------------------------|----------------------------------|-----------------------------|-------------------------------------|----------------|--------------------|---------------------|
| GaAs                     |                              8500 |                            13.1  |                         400 |                                  55 |            3.3 |                4.9 |                 0.3 |
| GaN                      |                               900 |                             9    |                        3000 |                                 110 |            8   |               61.7 |                 0.1 |
| Ge                       |                              3900 |                            16    |                         100 |                                  58 |            0.6 |                0.3 |                 1   |
| Si                       |                              1400 |                            11.7  |                         300 |                                 130 |            1   |                1   |                 1   |
| GaP                      |                               250 |                            11.1  |                        1000 |                                 110 |            1.4 |                4.5 |                 0.3 |
| SiC ( 6H, a )            |                               330 |                             9.66 |                        2400 |                                 700 |            3.9 |               25.7 |                 0.8 |
| SiC ( 4H, a )            |                              1000 |                             9.7  |                        3180 |                                 700 |            7.5 |               65.9 |                 0.8 |
| Diamond                  |                              2200 |                             5.7  |                        5700 |                                2000 |           23.8 |              220.5 |                 1.7 |

Finally, Huang [10,63] concluded, using the new FOMs, that 4H-SiC will have 7.4 times lower losses compared to Si, a 65% smaller chip area, and 60% higher temperature. While GaN will have 8 times lower losses compared to Si, a 61.7% smaller area, and 10% higher temperature.

Energies

2023

,

16

, x FOR PEER REVIEW

Based on the above FOMs, it is clear that GaN and SiC have better inherent properties, better efficiencies and can provide higher performance in comparison to current Si-based devices. 16  of  28

Figure 14. New on-resistance for direct bandgap shown as (9a) and new on-resistance for indirect bandgap as (9b), while (10) indicates on-resistance using old equation [14]. Figure 14. New on-resistance for direct bandgap shown as (9a) and new on-resistance for indirect bandgap as (9b), while (10) indicates on-resistance using old equation [14].

<!-- image -->

## 3. Applications 3. Applications

The initial successes of SiC and GaN devices in the market were at di ff erent ends of the voltage spectrum. SiC devices are preferred at voltage levels of 1200 V and above, while GaN devices made inroads in applications with voltage ranges of up to 600 V and The initial successes of SiC and GaN devices in the market were at different ends of the voltage spectrum. SiC devices are preferred at voltage levels of 1200 V and above, while below. The two major reasons are the high switching speed and cost. GaN devices are

smaller; hence, electrons require less time to travel through the device. Also, GaN crystals have higher and faster mobility of electrons. Therefore, for applications in the range of 600

V and below, GaN-based devices that can switch at faster speeds can provide be tt

er e ffi

-

GaN devices made inroads in applications with voltage ranges of up to 600 V and below. The two major reasons are the high switching speed and cost. GaN devices are smaller; hence, electrons require less time to travel through the device. Also, GaN crystals have higher and faster mobility of electrons. Therefore, for applications in the range of 600 V and below, GaN-based devices that can switch at faster speeds can provide better efficiency. SiC devices, on the other hand, are preferred for higher-voltage applications due to their size and maturity in device fabrication. For many high-power applications such as motor drives, uninterrupted power supply (UPS) systems, and high-voltage DC transmission systems (HVDC), a substantial size reduction can be achieved by using SiC devices. The usage of GaN, in-contrast to SiC devices, at a voltage level of 600 V and below is due to the cost-effective method of producing GaN. A GaN transistor can be grown on Si substrate wafers, while SiC requires expensive substrate. Furthermore, GaN low-voltage devices do not need expensive and bulky packages that are required for Si MOSFETs and SiC transistors [64]. However, with a better balance-of-plant system design, the total per-watt cost could potentially be reduced. These savings may result from the use of smaller passive inductive and capacitive circuit elements, filters, cooling, etc. These improvements could justify the higher capital cost in many power applications [65]. High-impact opportunities exist across a wide variety of applications, as discussed below.

## 3.1. Motor Drives

Electric motors are widely used in vast range of residential, commercial, and industrial applications, accounting for about 50% of the global energy consumption [66]. The global electric motor market is expected to grow from USD 134 billion in 2022 to USD 186 billion by 2027 [67]. The major portion of energy consumed in the residential sector is for cooling, heating, and refrigeration (fans and compressors). Similarly, in the commercial sector, most of the energy is consumed by HVAC and refrigeration. While, in the industrial sector, a vast portion of motor energy is consumed by conveyor systems, followed by compressor and pumps. Figure 15 illustrates the power consumption of electric motors in the residential and commercial sectors [68].

In the residential sector, low-power (0.75 to 4 kW) with low-input grid voltage (110 to 460 V) motors are currently used. In the commercial sector, both low-power and mediumpower (4 kW to 375 kW) with medium-input voltage (200 V to 1000 V) motors are usually used. While, in the industrial sector, low-power, medium-power, and high-power (&gt;375 kW) with high-input voltage (2.3 kV to 13.8 kV) motors are usually used depending on the application [69].

Variable frequency drives (VFDs) are commonly used to achieve variable speed. They consist of an input grid voltage rectifier and an inverter to adjust the voltage and frequency of the incoming current to meet the power requirements of the load. In centrifugal processes, such as fans and pumps, VFDs can save 55% less energy when running at 75% speed, based on the cubic relationship between the motor power and the speed [67]. On the other hand, in the case of applications requiring constant torque motors, e.g., conveyor belts, 25% energy is saved when running at 75% speed based on the linear relationship that exists between motor speed and power [70].

VFDs can reduce overall energy consumption by approximately 10-30% [67]. Globally, it is estimated that by employing VFDs, an energy saving of 10%, 15%, and 20%, respectively, for refrigeration, air compressor, and pumps/fan could be achieved [71]. Current Si-based VFDs have 10% market penetration with an average efficiency of 94.5%. Assuming an average saving of 15% with the adoption of VFDs for industrial electric motors, with 100% market penetration, the overall global energy losses in industrial motors are estimated at 214 TWh/year.

WBG devices are set to play a key role in improving the performance of current Sibased inverters for motor drives. Also, the current VFDs are quite bulky, require significant space due to cooling needs, and their efficiency should be improved for a wider adoption. WBG-based motor drives can run at higher frequencies, which can reduce the size of passive

Energies

2023

,

16

quency of the incoming current to meet the power requirements of the load. In centrifugal processes, such as fans and pumps, VFDs can save 55% less energy when running at 75%

speed, based on the cubic relationship between the motor power and the speed [67]. On the other hand, in the case of applications requiring constant torque motors, e.g., conveyor

belts, 25% energy is saved when running at 75% speed based on the linear relationship that exists between motor speed and power [70].

VFDs can reduce overall energy consumption by approximately 10-30% [67]. Glob- components and reduce the audible system noise [72]. Additionally, WBG devices can withstand higher temperatures and thus can reduce the size and weight of the whole VFD, which is advantageous in many applications where space is a major constraint. The new generation of integrated motors drives (IMD) offers reduced weight, reduced volume, and higher efficiency. These motors drives are integrated inside a motor and can withstand high temperatures due to the superior physical characteristics of WBG-based power devices [73]. ally, it  is  estimated that by employing VFDs, an energy saving of 10%, 15%, and 20%, respectively, for refrigeration, air compressor, and pumps/fan could be achieved [71]. Current Si-based VFDs have 10% market penetration with an average e ffi ciency of 94.5%. Assuming an average saving of 15% with the adoption of VFDs for industrial electric motors, with 100% market penetration, the overall global energy losses in industrial motors are estimated at 214 TWh/year.

Figure 15.  a ( ) Residential and ( b ) commercial motor electricity use [69]. Figure 15. ( a ) Residential and ( b ) commercial motor electricity use [69].

<!-- image -->

, x FOR PEER REVIEW

WBG devices are set to play a key role in improving the performance of current Sibased inverters for motor drives. Also, the current VFDs are quite bulky, require signi fi -cant space due to cooling needs, and their e ffi ciency should be improved for a wider adoption. WBG-based motor drives can run at higher frequencies, which can reduce the size of passive components and reduce the audible system noise [72]. Additionally, WBG devices can withstand higher temperatures and thus can reduce the size and weight of the whole Generally, low-power motors have higher variance in efficiency based on load requirements in comparison to larger motors. Therefore, as the VFD load decreases, so does the efficiency. The decrease in efficiency based on load is a problem and hinders the market penetration of VFDs, especially for lower-power motors. Motor losses were estimated at about 16 TWh globally in 2015 due to VFDs inefficiency. Figure 16 shows the efficiency of Si-VFD and WBG-based VFD against load fraction and rated power [73-76]. 18  of  28

VFD, which is advantageous in many applications where space is a major constraint. The ers reduced weight, reduced vol-

ciency based on load re- ciency based on load is a problem and hinders the mar-

ffi

<!-- image -->

ciency

## 3.2. Automotive 3.2. Automotive

WBG devices provide high power density with improved energy e ffi ciency and are very promising for electrical vehicles (EVs) application. Some typical e ffi ciency values of di ff erent converters are given in Table 9. Electric power train vehicles (H/EVs) can be classi fi ed into three types: ba tt ery electric vehicles (BEVs), hybrid electric vehicles (HEVs), and plug-in hybrid vehicles (PHEVs). In a BEV, the ba tt ery is primarily charged via an onboard charger (OBC) through standard 120 V or 240 V grid outlet. Regenerative braking can also contribute to charging when driving. Some of the leading BEVs include all models from Tesla, Nissan Leaf, and BMW i3. An HEV is comprised of a combustion engine, electric motor, generator, and a small ba tt ery. The ba tt ery can be charged by the combustion engine and via the generator during regenerative braking. HEVs are the most popular among all H/EVs [77]. WBGdevices provide high power density with improved energy efficiency and are very promising for electrical vehicles (EVs) application. Some typical efficiency values of different converters are given in Table 9. Electric power train vehicles (H/EVs) can be classified into three types: battery electric vehicles (BEVs), hybrid electric vehicles (HEVs), and plug-in hybrid vehicles (PHEVs). In a BEV, the battery is primarily charged via an on-board charger (OBC) through standard 120 V or 240 V grid outlet. Regenerative braking can also contribute to charging when driving. Some of the leading BEVs include all models from Tesla, Nissan Leaf, and BMW i3. An HEV is comprised of a combustion engine, electric motor, generator, and a small battery. The battery can be charged by the combustion engine and via the generator during regenerative braking. HEVs are the most popular among all H/EVs [77].

Table 9.

E

ffi ciency of various converters in EVs.

Type

On-Board Charger

Inverters and HV

Low-Voltage DC-DC

Table 9. Efficiency of various converters in EVs.

| Type              | On-Board Charger   | Inverters and HV Converter    | Low-Voltage DC-DC Converter   |
|-------------------|--------------------|-------------------------------|-------------------------------|
| Power             | ~3.3 kW            | 12-400 kW 200-400 V 100-650 V | 1-10 kW                       |
| Input Voltage     | 120-240 V          |                               | 200-400 V                     |
| Output Voltage    | 200-400 V          |                               | 12-48 V                       |
| Si Efficiency     | 85-93%             | 83-95%                        | 85-90%                        |
| SiC Efficiency    | 95-96%             | 96-97%                        | 96-99%                        |
| GaN Efficiency    | 94-98%             | No data                       | 95-99%                        |
| Power Electronics | 600-900 V          | 600 V-1.2 kV                  | 600-900 V                     |
|                   | Discrete           | Module and Discrete           | Discrete                      |
| HEV               | X                  | glyph[check]                  | glyph[check]                  |
| PHEV              | glyph[check]       | glyph[check]                  | glyph[check]                  |
| BEV               | glyph[check]       | glyph[check]                  | glyph[check]                  |

Generally, electric drive systems in a typical EV consist of DC-DC buck/boost converter (mainly used in hybrid EVs) to step up the battery voltage up to 700 V, a traction inverter, a DC-DC converter for auxiliary loads, and an OBC.

- 1. The buck/boost converter requires high-voltage-rated devices typically in the range of 1.2 kV and a device for high switching frequencies in the order of tens of kilohertz (usually 100 kHz for a 20 kW buck/boost converter). Current SiC and GaN power devices can switch at higher frequencies without additional losses [12,78] and therefore are ideal candidates for this application. Operating these devices at higher frequencies can lower the overall footprint in terms of weight and size through a reduction in the output filter components, hence increasing the overall efficiency [79];
- 2. The traction inverter mainly requires lower switching and conduction losses and better thermal management. This makes SiC devices with a typical rating of 900 to 1.2 kV potential candidates for traction inverters. Also, the better thermal management of SiC devices translates into compact and lightweight heatsinks, which is necessary for traction inverters [80];
- 3. The DC-DC converter for handling auxiliary loads consists of both high-voltage interface and a low-voltage interface. For the high-voltage side, SiC is the best candidate, while for low voltages, GaN devices can easily fulfill the requirements. Also, the DC-DC converter typically requires higher-frequency operation (to decrease the size of the output filter components), which the current WBG devices can easily achieve without creating additional switching losses [81];
- 4. The present OBCs are currently designed for wired operation, while the future tendency is for the wireless charging. Furthermore, OBCs operate more efficiently with high-frequency switching devices. Toyota and APEI have developed a 6 kW SiC OBC system operating at switching frequencies up to 250 kHz, with an overall efficiency of 95% and 10 times improvement in power density [82]. Also, a SiC-based OBC of 6.8 kW demonstrated 50% reduction in component count and 2% increase in efficiency [83].

In an EV, energy efficiency can be achieved directly through the reduction of switching and other losses and indirectly by reducing the volume and weight of power electronics circuitry. The EV Everywhere Grand Challenge launched in the U.S. in 2013 required 35% reduction in size and 40% reduction in weight, which can be achieved by WBG devices, especially SiC [84]. Estimates of drive efficiencies can be determined by comparing Si and SiC drive performance over a range of speed and torque. Table 10 illustrates Si and SiC inverter efficiency over different drive cycles [85,86].

Energies

2023

,

16

Table 10. Inverter efficiency of Si and SiC over various drive cycles [85,86].

| Drive Cycle   | Type       | Si    | SiC   | Improvement   | Reduction of Losses   |
|---------------|------------|-------|-------|---------------|-----------------------|
| US06          | Aggressive | 95.1% | 97.1% | 2.1%          | 41%                   |
| EPA City      | City       | 90.9% | 97.9% | 7.7%          | 77%                   |
| EPA Highway   | Highway    | 97.7% | 99.7% | 2.0%          | 85%                   |
| Artemis Urban | City       | 86.2% | 96.6% | 12%           | 76%                   |
| Empa C1       | City       | 82.9% | 96.0% | 16%           | 77%                   |
| Hyzem Urban   | City       | 87.2% | 96.7% | 11%           | 75%                   |

As the price of SiC and GaN devices drops, more manufacturers in the automotive industry are adopting them. Toyota has already announced the introduction of the SiCbased power control unit (PCU) for EVs by 2020 [87]. While other automotive makers like Ford Motors have recently demonstrated a 40% reduction in switching losses and an overall fuel efficiency of 5% by adopting SiC MOSFETs [88]. It is expected that by adopting SiC MOSFETs in hybrid EVs, an improvement of up to 15% could be achieved, and significant savings could also be made by drivetrain electrification [56]. In addition, WBGbased converters enable efficient, lightweight, and low-cost DC charging infrastructure (&gt;120 kW), which, coupled with cleaner electricity generation in the transportation sector, can potentially reduce greenhouse gas emissions [89].

## 3.3. Data Centers

, x FOR PEER REVIEW

A data center consists of networked computers servers that are utilized for data processing, storage, and distribution. These servers are responsible of providing local intranets, data clouds, and Internet. Approximately, 2.5 billion people around the world are online now, with millions of searches, emails, and online transactions routed via these centers each minute [90]. As these numbers are increasing each year, data centers' efficiency has become quite critical. A major concern is the high electricity usage in the data center industry due to lack of motivation to improve the equipment efficiency. Figure 17 below shows global energy usage in data centers [91]. 20  of  28 online now, with millions of searches, emails, and online transactions routed via these centers each minute [90]. As these numbers are increasing each year, data centers' e ffi -ciency has become quite critical. A major concern is the high electricity usage in the data center industry due to lack of motivation to improve the equipment e ffi ciency. Figure 17 below shows global energy usage in data centers [91].

Figure 17. Electricity-saving potential in industrial electric motors Si-based VFDs vs. WBG-based VFDs [44]. Figure 17. Electricity-saving potential in industrial electric motors Si-based VFDs vs. WBG-based VFDs [44].

<!-- image -->

The increase in global data center electricity usage has led many governments across the world to introduce regulations and e ffi ciency standards for data centers. Energy usage in a modern data center includes mainly the IT load, UPS and cooling systems. The IT load consumes approximately half of the energy of a data center and consists of the servers, data storage, power supply unit (PSU), and network devices. The rest is utilized for additional power conversion involving UPS, transformers, and cooling units. Figure 18 below illustrates the energy usage breakdown of a data center [92]. The increase in global data center electricity usage has led many governments across the world to introduce regulations and efficiency standards for data centers. Energy usage in a modern data center includes mainly the IT load, UPS and cooling systems. The IT load consumes approximately half of the energy of a data center and consists of the servers, data storage, power supply unit (PSU), and network devices. The rest is utilized for additional power conversion involving UPS, transformers, and cooling units. Figure 18 below illustrates the energy usage breakdown of a data center [92].

the world to introduce regulations and e ffi

ciency standards for data centers. Energy usage in a modern data center includes mainly the IT load, UPS and cooling systems. The IT

load consumes approximately half of the energy of a data center and consists of the serv- ers, data storage, power supply unit (PSU), and network devices. The rest is utilized for

additional power conversion involving UPS, transformers, and cooling units. Figure 18

below illustrates the energy usage breakdown of a data center [92].

Figure 18. Global energy usage in data centers. Figure 18. Global energy usage in data centers.

<!-- image -->

The power system of a data center consists of a line frequency transformer, low-voltage power distribution network, and centralized backup unit voltage regulators. Typically, the power conversion tasks involved in an average data center account for 10.4% of the total energy consumed [93] There are several factors for the high-power usage of a data center, such as the underutilization of servers and UPS units that are on but not fully utilized and ine ffi cient cooling solutions. The power system of a data center consists of a line frequency transformer, low-voltage power distribution network, and centralized backup unit voltage regulators. Typically, the power conversion tasks involved in an average data center account for 10.4% of the total energy consumed [93] There are several factors for the high-power usage of a data center, such as the underutilization of servers and UPS units that are on but not fully utilized and inefficient cooling solutions.

Di ff erent energy e ffi ciency improvement schemes range from the adoption of lowpower losses converters to a complete redesign of the power delivery network. The la tt er would likely involve converting higher voltages at the rack level, where space is limited, and require an e ffi cient thermal management. WBG-based converters can play a key role Different energy efficiency improvement schemes range from the adoption of lowpower losses converters to a complete redesign of the power delivery network. The latter would likely involve converting higher voltages at the rack level, where space is limited, and require an efficient thermal management. WBG-based converters can play a key role in the development of efficient systems by reducing the impact of higher temperatures on the loads without incorporating expensive and bulky cooling solutions.

In a data center, power conversion equipment based on standard silicon devices such as rectifier, inverter, and converter are approximately 75 to 95% efficient [94]. Among the power conversion equipment are UPS and PSU systems.

AUPSunit is critical part of any data center, as it provides backup power to the load in case of electricity outage. The UPS employs a double-conversion strategy: during normal operation, the AC grid voltage is rectified into DC and then stored in a battery, while during grid failure, the inverter converts the stored DC voltage back into AC. Though this ensures a continuous supply of power, it ultimately generates significant losses during the conversion of AC-DC-AC [95]. SiC-based UPS are now commercially available from well-known manufacturers such as Toshiba and Mitsubishi. The G2020 UPS unit from Toshiba boasts half the losses, has a higher operating temperature, is compact in size, and is only 10% more expensive compared to a similarly sized silicon-based UPS system [96].

The PSU used in servers converts AC power from the power distribution unit (PDU) into low-voltage DC. It consists of an AC-to-DC rectifier, a step-down transformer, and a DC-DC converter. For most data centers, the input AC supply voltage to the PSU ranges from 200 V to 480 V, while the output voltage is typically 12 V DC. WBG power devices such as SiC are commercially available in the range of 600 V to 1.2 kV, while for GaN, the voltage is up to 600 V. These power devices can easily replace the existing silicon devices [97]. Similarly to the UPS systems, it is estimated that replacing the standard silicon power devices such as diodes and transistors with WBG can reduce the power losses by half [98]. In a study, GaN-based PSU for data centers demonstrated an efficiency of 96.3% at a switching frequency of 1MHz. This led to a reduction in the converter size, transformer winding losses, and heat produced by the converter. Figure 19 below shows energy usage of data center equipment based on Si and WBG devices [99].

[97]. Similarly to the UPS systems, it is estimated that replacing the standard silicon power devices such as diodes and transistors with WBG can reduce the power losses by half [98].

In  a  study,  GaN-based  PSU  for  data  centers  demonstrated  an  e ffi

ciency  of  96.3%  at  a switching frequency of 1MHz. This led to a reduction in the converter size, transformer

winding losses, and heat produced by the converter. Figure 19 below shows energy usage of data center equipment based on Si and WBG devices [99].

Figure 19. Data center electricity usage of Si and SiC equipment. Figure 19. Data center electricity usage of Si and SiC equipment.

<!-- image -->

Switching from Si-based devices to WBG-based devices can increase the energy conversion e ffi ciency from 90% to 98% in data centers [100]. This translates into an approximately 8.3% reduction in energy usage. In addition to the energy savings, due to lowpower losses, the WBG-based data center equipment can operate at higher temperatures Switching from Si-based devices to WBG-based devices can increase the energy conversion efficiency from 90% to 98% in data centers [100]. This translates into an approximately 8.3% reduction in energy usage. In addition to the energy savings, due to low-power losses, the WBG-based data center equipment can operate at higher temperatures without requiring expensive and bulky cooling solutions.

without requiring expensive and bulky cooling solutions.

## 3.4. Power Systems and Distributed Energy Resources

3.4. Power Systems and Distributed Energy Resources Power electronics technology is already playing an essential role in electric power systems applications, such fl exible  alternating  current  transmissions  systems  (FACTS), high-voltage direct current (HVDC) transmission, and the integration of distributed renewable energy sources such as solar photovoltaics (PV) and wind energy into the power Power electronics technology is already playing an essential role in electric power systems applications, such flexible alternating current transmissions systems (FACTS), highvoltage direct current (HVDC) transmission, and the integration of distributed renewable energy sources such as solar photovoltaics (PV) and wind energy into the power grid. Renewable energy resources vary from other traditional power generation sources (coal, oil, etc.) since the voltage is usually converted from DC to AC to supply power suitable for grid integration. The rapidly growing penetration of renewable energy resources has increased the opportunity for WBG devices. It is estimated that about 4% of all the electricity generated is lost in the power electronics devices [101].

In 2014, the U.S. alone generated 77 TBtu of energy from solar PV [102]. The energy savings when switching from Si- to SiC-based inverters are expected to increase from 96% to 99%, i.e., a 3% increase [103]. Additionally, WBG devices offer an increase in the system-level efficiency by operating PV systems at higher voltages. This reduces voltage conversions in a traditional PV converter by replacing the combiner boxes with DC-DC converters.

Onthe other hand, modern wind turbines generate variable AC power, which depends on wind speed. The variable frequency AC power needs to be rectified into DC and then back into AC to achieve a fixed grid frequency. Though the conversion process has a set of associated losses, it allows wind turbines to function at maximum efficiency. In 2014, approximately 572 TBtu of energy in the U.S. was produced through wind turbines [104]. An improvement from 93.5% to 97.8% with absolute 4.6% efficiency is possible by incorporating WBG devices for wind energy conversion systems [105]. A 100% penetration of SiC devices in the wind turbine converters industry is expected to generate an annual savings of 26.3 TBtu. WBG devices offer low system-level costs by operating at higher switching frequencies, which in turn reduces the size of passive components and overall system footprint. Also, WBG devices-based converters are robust and have a mean time to failure (MTTF) of more than 25 years [106]. This lowers the operation and maintenance of the equipment and thus the overall cost of the system in a distributed energy resources (DERs) application.

## 3.5. Consumer Electronics

In 2019, the International Energy Agency (IEA) reported that 1.7% of the global energy consumption, estimated at 50 TWh, consists of external power supplies (EPS) such as laptops and mobile phones [107]. It is estimated that 45% of this energy (23 TWh)

is dissipated in mobile phones, MP3, and AC adapters. This includes losses between electronic devices and AC sources. Various assumptions are made when estimating the energy usage of AC adapters and external power supplies (EPSs). A U.S. Department of Energy (DOE) study broadly identified four states of EPS modes-active, no-load, off, and unplugged, depending on its connection to the power source and the application and state of EPSs on/off switch. The active mode can be further classified into six states ranging from 66% of EPS power, in the case of the computer just being turned on, to a 0.6% output power, when the computer is fully charged and switched off [108].

GaNHEMTsareanideal candidate for electronic device adapters, especially for laptops, and could increase the efficiency by 3%. This is a conservative estimate, as laptop adapters usually offer a partial percentage of their rated power, and GaN HEMTs truly shine at lower levels. Table 11 illustrates the benefits of switching to WBG-devices-based adapters for laptops, mobile phones, and tablets [97]. An increase of 3% in the efficiency for laptops, 5% for mobile phones, and 9% for tablets should translate into an overall annual saving of 7670 GWh for the U.S. alone, which approximates the annual generation of an average-sized coal power plant. Another important benefit of using high-frequency GaN devices is a 10 times reduction in an average adapter size. Consumers would willingly pay a higher cost towards a more compact adaptor size based on GaN devices, which in turn will help drive the sales volume and achieve comparable cost reductions. In the future, when GaN power devices eventually reach a reasonable price, their introduction in flatscreen TV power supplies and various other consumer electronics will substantially increase.

Table 11. Potential impact of WBG components on global energy.

| Transistor Material   | Application   | Average Power Rating (W) (1)   | Average Active Mode Efficiency (1)   | Annual Loss per Unit (kWh)   | 2014 Global Sales (2)   | Assumed Product Life (Years) (3)   | Global Stock (MMUnits in Service)   | Annual Electricity Loss by Global Stock (GWh)   |
|-----------------------|---------------|--------------------------------|--------------------------------------|------------------------------|-------------------------|------------------------------------|-------------------------------------|-------------------------------------------------|
|                       | Laptop        | 60                             | 87%                                  | 11.0                         | 250                     | 3                                  | 750                                 | 8250                                            |
| Si                    | Tablet        | 12                             | 80%                                  | 1.9                          | 250                     | 3                                  | 750                                 | 1425                                            |
|                       | Cell phone    | 5                              | 63%                                  | 4.2                          | 1870                    | 3                                  | 5610                                | 23,562                                          |
|                       |               |                                |                                      | Total                        |                         |                                    |                                     | 33,237                                          |
|                       | Laptop        | 60                             | 90%                                  |                              | 250                     | 3                                  | 750                                 | 6346                                            |
| WBG                   | Tablet        | 12                             | 85%                                  | 1.5                          | 250                     | 3                                  | 750                                 | 1096                                            |
|                       | Cell phone    | 5                              | 72%                                  | 3.2                          | 1870                    | 3                                  | 5610                                | 18,125                                          |
|                       |               |                                |                                      | Total                        |                         |                                    |                                     | 25,567                                          |
|                       |               |                                |                                      | WBGSavings (GWh/year)        |                         |                                    |                                     | 7670                                            |
|                       |               |                                |                                      | WBGSavings (GWh/year)        |                         |                                    |                                     | 26.2                                            |

## 4. Challenges Facing WBG Devices

Despite exceptional headways in WBG semiconductors, significant work still needs to be done before the full potential of these materials is realized. As discussed above, essential research into material properties and processing, with improvement down the power electronics value chain into circuits and systems, represents a crucial stride in the development of these unique materials in order to receive the energy benefits through far-reaching applications. The current challenges preventing the widespread adoption of WBGdevices are summarized below.

Maturity and reliability -WBGsemiconductors and devices are relatively less mature than Si-based conventional counterparts. There is also a limited availability of WBG devices in the market due to the large demand-to-supply ratio.

Heat dissipation-While WBG materials can handle higher temperatures than silicon, they can still generate significant heat, especially in high-power applications.

Lack of standardization -WBGtechnologies are still developing, and there is a lack of standardization compared to Si-based conventional counterparts. This can result in compatibility issues and slower adoption in some industries.

Higher switching frequencies -Electromagnetic interference (EMI) and electromagnetic compatibility (EMC) compliance is a challenge during higher switching frequencies operation.

Cost and quality -WBGmaterial is very costly to manufacture due the high cost of SiC and GaN substrates and the difficulty to produce high-quality wafers with limited crystalline defects as compared to similarly rated Si-based devices.

Device design and fabrication -Novel design techniques are needed to realize the full potential of WBG devices properties to achieve the voltage and current requirements in various applications. Also, advanced device packaging and thermal management technologies need to be developed to improve operating temperatures, architectures, and manufacturing affordability for wide-scale adoption of WBG devices.

Systems integration -In many applications, simple drop-in replacement of Si with WBG devices is not always appropriate due to the significant differences in material properties. Therefore, for large and more complex systems, circuits must be redesigned for effective integration of WBG devices to utilize their full capability.

## 5. Conclusions

Even though WBG devices are rapidly gaining acceptance, there are risks and anxiety associated with the increased research and investment in WBG materials. There are concerns of losing intellectual property of WBG devices to countries like China that have large capabilities for semiconductors production facilities. Additionally, serious concerns regard the cost of WBG materials, from the possibility of never becoming lower or the reliability of WBG devices for large-scale adoption in various applications. Risks and uncertainties regarding the manufacturing cost of WBG devices can be broken down to three major categories.

Finally, external factors such as lenient efficiency standards in emerging markets and falling electricity prices due to the increased deployment of renewable energy power generation might deter businesses from using high-efficiency power electronics due to the long-term payback period. To alleviate some concerns regarding the reliability of WBGdevices, leading manufacturers Cree and GE recently released data showing marked improvements with each iteration of their devices. Also, it is expected that the cost of WBG devices will eventually reach price parity with current silicon devices (10 cent/A) in the next five years through the usage of commercial silicon foundries and may fall even below the current price (1.5 cent/A) through the introduction of a fine-line lithography technique made possible by flatter wafers. With the introduction of 8-inch SiC wafers in 8 years' time, prices could fall even lower (1 cent/A for 1200 V devices).

Funding: This research received no external funding.

Data Availability Statement: Not applicable.

Conflicts of Interest: The authors declare no conflict of interest.

## References

- 1. Kizilyalli, J.C.; Xu, Y.A.; Carlson, E.; Manser, J.; Cunningham, D.W. Current and future directions in power electronic devices and circuits based on wide band-gap semiconductors. In Proceedings of the 2017 IEEE 5th Workshop on Wide Bandgap Power Devices and Applications (WiPDA), Albuquerque, NM, USA, 30 October-1 November 2017; p. 417.
- 2. Millan, J.; Godignon, P.; Perpina, X.; Perez-Tomas, A.; Rebollo, J. A Survey of Wide Bandgap Power Semiconductor Devices. IEEE Trans. Power Electron. 2014 , 29 , 2155-2163. [CrossRef]
- 3. Saeed, H.T.R.; Kurdkandi, N.V.; Husev, O.; Vinnikov, D.; Tahami, F. An overview of lifetime management of power electronic converters. IEEE Access 2022 , 10 , 109688-109711.
- 4. Elasser, A.; Chow, T. Silicon carbide benefits and advantages for power electronics circuits and systems. Proc. IEEE 2002 , 90 , 969-986. [CrossRef]
- 5. Shenai, K. Potential impact of emerging semiconductor technologies on advanced power electronic systems. IEEE Electron. Device Lett. 1990 , 11 , 520-522. [CrossRef]
- 6. Langpoklakpam, C.; Liu, A.-C.; Chu, K.-H.; Hsu, L.-H.; Lee, W.-C.; Chen, S.-C.; Sun, C.-W.; Shih, M.-H.; Lee, K.-Y.; Kuo, H.-C. Review of silicon carbide processing for power MOSFET. Crystals 2022 , 12 , 245. [CrossRef]

- 7. Carlson, E.P.; Kizilyalli, I.C.; Cunningham, D.W.; Manser, J.S.; Xu, Y.A.; Liu, A.Y. Wide Band-Gap Semiconductor-Based Power Electronics for Energy Efficiency ; Advanced Research Projects Agency-Energy, US Department of Energy (USDOE): Washington, DC, USA, 2018.
- 8. Schafer, R.; Buchalter, J. Semiconductors: Technology and Market Primer 10.0 ; Oppenheimer &amp; Co.: New York, NY, USA, 2017.
- 9. Tuztasi, F.M.; Aydin, M. The Effect of Temperature Changes on Semiconductor Material Efficiency Under Load. In Proceedings of the 2022 11th International Conference on Renewable Energy Research and Application (ICRERA), Istanbul, Turkey, 18-21 September 2022; IEEE: Piscataway, NJ, USA, 2022; pp. 496-501.
- 10. Ballest n-Fuertes, J.; Muñoz-Cruzado-Alba, J.; Sanz-Osorio, J.F.; Laporta-Puyal, E. Role of wide bandgap materials in power í electronics for smart grids applications. Electronics 2021 , 10 , 677. [CrossRef]
- 11. Neudeck, P.G.; Okojie, R.S.; Chen, L.-Y. High-temperature electronics-A role for wide bandgap semiconductors? Proc. IEEE 2002 , 90 , 1065-1076. [CrossRef]
- 12. Armstrong, K.O.; Das, S.; Cresko, J. Wide bandgap semiconductor opportunities in power electronics. In Proceedings of the 2016 IEEE 4th Workshop on Wide Bandgap Power Devices and Applications (WiPDA), Fayetteville, AR, USA, 7-9 November 2016; IEEE: Piscataway, NJ, USA, 2016; pp. 259-264.
- 13. California Energy Commision. Go Solar California Project. List of Eligible Inverters per SB1 Guidelines ; California Energy Commission: Sacramento, CA, USA, 2016.
- 14. Hudgins, J.; Simin, G.; Santi, E.; Khan, M. An assessment of wide bandgap semiconductors for power devices. IEEE Trans. Power Electron. 2003 , 18 , 907-914. [CrossRef]
- 15. White House. Press Release: President Obama Announces New Public-Private Manufacturing Innovation Institute. 2014. Available online: https://www.presidency.ucsb.edu/documents/fact-sheet-president-obama-announces-new-manufacturinginnovation-institute-competition (accessed on 26 July 2023).
- 16. Semiconductor Sales Worldwide from 2015 to 2022, by Region. Available online: https://www.statista.com/statistics/249509 /forecast-of-semiconductor-revenue-in-the-americas-since-2006/ (accessed on 26 July 2023).
- 17. Eden, R. The World Market for Silicon Carbide &amp; Gallium Nitride Power Semiconductors ; IHS Technology: London, UK, 2016.
- 18. Nalwa, H.S. (Ed.) Handbook of Surfaces and Interfaces of Materials ; Five-Volume Set; Elsevier: Amsterdam, The Netherlands, 2001.
- 19. St˛ eszewski, J.; Jakubowski, A. Comparison of 4H-SiC and 6H-SiC MOSFET I-V characteristics simulated with Silvaco Atlas and Crosslight Apsys. J. Telecommun. Inf. Technol. 2007 , 3 , 93-95.
- 20. Singh, R. Reliability and performance limitations in SiC power devices. Microelectron. Reliab. 2006 , 46 , 713-730. [CrossRef]
- 21. Casady, J.B. SiC power devices and modules maturing rapidly. Power Electron. Eur. 2013 , 1 , 16-19.
- 22. Cree Inc. Milestones. About Cree. From 580. 2014. Available online: http://www.cree.com/About-Cree/History-andMilestones/Milestones (accessed on 28 October 2014).
- 23. Hiroaki, F.; Ito, M.; Ito, H.; Kamata, I.; Naito, M.; Hara, K.; Yamauchi, S.; Suzuki, K.; Yajima, M.; Mitani, S. Development of a 150 mm 4H-SiC epitaxial reactor with high-speed wafer rotation. Appl. Phys. Express 2013 , 7 , 015502.
- 24. Xu, Y.A. ARPA-E Impacts: A Sampling of Project Outcomes ; Advanced Research Projects Agency-Energy (ARPA-E), US Department of Energy (USDOE): Washington, DC, USA, 2018; Volume III.
- 25. JCN Newswire. SDK Increases Capacity to Produce 6' SiC Epi-Wafers for Power Devices. Sys-con Media. 2014. Available online: http://www.sys-con.com/node/3192617 (accessed on 28 October 2014).
- 26. Hull, B. SiC Power Devices-Fundamentals, MOSFETs and High Voltage Devices. In Proceedings of the 1st IEEE Workshop on Wide Bandgap Power Devices and Applications, Columbus, OH, USA, 27-29 October 2013; IEEE: Piscataway, NJ, USA, 2013.
- 27. Seal, S.; Mantooth, H.A. High performance silicon carbide power packaging-Past trends, present practices, and future directions. Energies 2017 , 10 , 341. [CrossRef]
- 28. Department of Energy. Wide Bandgap Power Electronics Technology Assessment. Available online: https://www.energy.gov/ sites/prod/files/2015/02/f19/QTR%20Ch8%20-%20Wide%20Bandgap%20TA%20Feb-13-2015.pdf (accessed on 28 October 2014).
- 29. Maddi, H.L.R.; Yu, S.; Zhu, S.; Liu, T.; Shi, L.; Kang, M.; Xing, D.; Nayak, S.; White, M.H.; Agarwal, A.K. The road to a robust and affordable SiC power MOSFET technology. Energies 2021 , 14 , 8283. [CrossRef]
- 30. Yole D veloppement. é Status of the Power Electronics Industry: A Comprehensive Overview of the Power Electronics Semiconductors Business ; Yole D veloppement: Rhone-Alpes, France, 2012. é
- 31. O'Loughlin, M.; Burk, A.; Tsvetkov, D.; Ustin, S.; Palmour, J.W. Advances in 3x150 mm Hot-Wall and 6x150 mm Warm-Wall SiC Epitaxy for 10kV-Class Power Devices. Mater. Sci. Forum 2016 , 858 , 167-172. [CrossRef]
- 32. Zolper, J.C. Emerging silicon carbide power electronics components. In Proceedings of the Twentieth Annual IEEE Applied Power Electronics Conference and Exposition, Austin, TX, USA, 6-10 March 2005; IEEE: Piscataway, NJ, USA, 2005; Volume 1, pp. 11-17. [CrossRef]
- 33. Yole D veloppement. é Power SiC 2018: Materials, Devices and Applications by the Power &amp; Wireless Team at Market Research and Strategy Consulting Company ; Yole D veloppement: Rhone-Alpes, France, 2018. é
- 34. Friedrichs, P. Further Prospects with SiC power semiconductors-Schottky diodes, JFET transistors and package considerations. In Proceedings of the 1st IEEE Workshop on Wide Bandgap Power Devices and Applications, Columbus, OH, USA, 27-29 October 2013; IEEE: Piscataway, NJ, USA, 2013.
- 35. Roussel, P . All Change for Silicon Carbide. Compound Semiconductor. 2013. Available online: http://www.compoundsemiconductor. net/article/90863-all-change-for-silicon-carbide.html (accessed on 28 October 2014).

- 36. Green Car Congress. Toyota Beginning On-Road Testing of New SiC Power Semiconductor Technology; Hybrid Camry Fuel Cell Bus. 29 January. Available online: http://www.greencarcongress.com/2015/01/20150129-toyotasic.html (accessed on 28 October 2014).
- 37. Chernykh, M.Y.; Andreev, A.A.; Ezubchenko, I.S.; Chernykh, I.A.; Mayboroda, I.O.; Kolobkova, E.M.; Khrapovitskaya, V.; Grishchenko, J.V.; Perminov, P.A.; Sedov, V.S.; et al. GaN-based heterostructures with CVD diamond heat sinks: A new fabrication ap-proach towards efficient electronic devices. Appl. Mater. Today 2022 , 26 , 101338. [CrossRef]
- 38. Yaozong, Z.; Zhang, J.; Wu, S.; Jia, L.; Yang, X.; Liu, Y.; Zhang, Y.; Sun, Q. A review on the GaN-on-Si power electronic devices. Fundam. Res. 2022 , 2 , 462-475.
- 39. Sarua, A.; Ji, H.; Hilton, K.; Wallis, D.; Uren, M.; Martin, T.; Kuball, M. Thermal Boundary Resistance Between GaN and Substrate in AlGaN/GaN Electronic Devices. IEEE Trans. Electron Devices 2007 , 54 , 3152-3158. [CrossRef]
- 40. Yole Developpement. A comprehensive overview of the 680 power electronics semiconductors business. In Status of the Power Electronics Industry ; Yole Developpement: Villeurbanne, France, 2012.
- 41. Würfl, J.; Hilt, O. Power Electronic Devices Based on GaN: Advantages and Perspectives ; Societe des Ingenieurs de l'Automobile (SIA): SURESNES CEDEX, France, 2013; Available online: https://www.sia.fr/publications/241-power-electronic-devices-based-ongan-advantages-and-perspectives?lng=en (accessed on 23 June 2019).
- 42. Ravkowski, J.; Peftitsis, D.; Nee, H.-P. Recent Advances in Power Semiconductor Technology. In Power Electronics for Renewable Energy Systems, Transportation and Industrial Applications ; Abu-Rub, H., Malinowski, M., Al-Haddad, K., Eds.; John Wiley &amp; Sons, Ltd: Chichester, UK, 2014. [CrossRef]
- 43. Yolegroup. Power GaN Supply Chain. 2018. Available online: https://www.yolegroup.com/Power\_GaN\_SupplyChain\_ HEMTcomparison.aspx (accessed on 23 June 2019).
- 44. ORNL. Oak Ridge National Lab Wide Band Gap Device Suppliers Survey ; ORNL: Oak Ridge, TN, USA, 2013.
- 45. Diel, Z. Commercial Status of the GaN-on-Silicon Power Industry. Compound Semiconductor. 11-15 March 2013. Available online: http://venture-q.com/pdf/Venture-QArticle-Web.03.05.13.pdf (accessed on 28 October 2014).
- 46. Umezawa, H. Recent advances in diamond power semiconductor devices. Mater. Sci. Semicond. Process. 2018 , 78 , 147-156. [CrossRef]
- 47. Volpe, P.-N.; Muret, P.; Pernot, J.; Omn è s, F.; Teraji, T.; Jomard, F.; Planson, D.; Brosselard, P.; Dheilly, N.; Vergne, B.; et al. High breakdown voltage Schottky diodes synthesized on p-type CVD diamond layer. Phys. Status. Solidi A 2010 , 207 , 2088-2092. [CrossRef]
- 48. Volpe, P.-N.; Muret, P.; Pernot, J.; Omn è s, F.; Teraji, T.; Koide, Y.; Jomard, F.; Planson, D.; Brosselard, P.; Dheilly, N.; et al. Extreme dielectric strength in boron doped homoepitaxial diamond. Appl. Phys. Lett. 2010 , 97 , 223501. [CrossRef]
- 49. Suzuki, M. High voltage diamond pin diodes: Feasibility study on ultimate properties of diamond toward ultimate power devices. Oyo Buturi 2016 , 85 , 218-222.
- 50. Bormashov, V.S.; Terentiev, S.A.; Buga, S.G.; Tarelkin, S.A.; Volkov, A.P.; Teteruk, D.V.; Kornilov, N.V.; Kuznetsov, M.S.; Blank, V.D. Thin large area vertical Schottky barrier diamond diodes with low on-resistance made by ion-beam assisted lift-off technique. Diam. Relat. Mater. 2017 , 75 , 78-84. [CrossRef]
- 51. Umezawa, H.; Shikata, S.; Funaki, T. Diamond Schottky barrier diode for high-temperature, high-power, and fast switching applications. Jpn. J. Appl. Phys. 2014 , 53 , 05fp06. [CrossRef]
- 52. Prins, J.F. Bipolar-transistor action in ion-implanted diamond. Appl. Phys. Lett. 1982 , 41 , 950-952. [CrossRef]

53.

Zeisse, C.R.; Hewett, C.A.; Nguyen, R.; Zeidler, J.R.; Wilson, R.G. An ion-implanted diamond metal-insulator semiconductor field-effect transistor.

IEEE Electron Device Lett.

1991

,

12

,

602-604. [CrossRef]

- 54. Yole Developpement. Diamond Materials for Semiconductor Applications ; Yole Developpement: Villeurbanne, France, 2013.
- 55. Keyes, R.W. Figure of Merit for Semiconductors for High-Speed Switches. Proc. IEEE 1972 , 60 , 225-232. [CrossRef]
- 56. Baliga, B.J. Power Semiconductor Device Figure of Merit for High-Frequency Applications. IEEE Electron Device Lett. 1989 , 10 , 455-457. [CrossRef]
- 57. Ozpineci, B.; Tolbert, L. Comparison of Wide-Bandgap Semiconductors for Power Electronics Applications. Master's Thesis, U.S. Department of Energy, Washington, DC, USA, 2003.
- 58. Werner, M.; Fahrner, W. Review on materials, microsensors, systems and devices for high-temperature and harsh-environment applications. IEEE Trans. Ind. Electron. 2001 , 48 , 249-257. [CrossRef]
- 59. Chow, T.; Tyagi, R. Wide bandgap compound semiconductors for superior high-voltage unipolar power devices. IEEE Trans. Electron Devices 1994 , 41 , 1481-1483. [CrossRef]
- 60. Oleksiy, S.; Flicker, J.; Dickerson, J.; Shoemaker, J.; Binder, A.; Smith, T.; Goodnick, S.; Kaplar, R.; Hollis, M. Analysis of the dependence of critical electric field on semiconductor bandgap. J. Mater. Res. 2022 , 37 , 849-865.
- 61. Tsao, J.Y.; Chowdhury, S.; Hollis, M.A.; Jena, D.; Johnson, N.M.; Jones, K.A.; Kaplar, R.J.; Rajan, S.; Van de Walle, C.G.; Bellotti, E.; et al. Ultrawide-bandgap semiconductors: Research opportunities and challenges. Adv. Electron. Mater. 2018 , 4 , 1600501. [CrossRef]
- 62. Shenai, K.; Scott, R.; Baliga, B. Optimum semiconductors for high-power electronics. IEEE Trans. Electron Devices 1989 , 36 , 1811-1823. [CrossRef]
- 63. Zhang, L.; Zheng, Z.; Lou, X. A review of WBG and Si devices hybrid applications. Chin. J. Electr. Eng. 2021 , 7 , 1-20. [CrossRef]
- 64. Huang, A. New Unipolar Switching Power Device Figures of Merit. IEEE Electron Device Lett. 2004 , 25 , 298-301. [CrossRef]

- 65. Epc-co.com. Efficient Power Conversion Corporation. 2015. Available online: http://epcco.com/epc/CEOInsights/ FastJustGotFasterBlog/December2013.aspx (accessed on 15 October 2017).
- 66. Casady, J. Power products commercial roadmap for SiC from 2012-2020. In Proceedings of the US DOE High MW Direct-Drive Motor Workshop, Gaithersburg, MD, USA, 4 September 2014.
- 67. Waide, P.; Brunner, C. Energy-Efficiency Policy Opportunities for Electric Motor-Driven Systems ; IEA: Paris, France, 2011.
- 68. Research, G. Global Electric Motor Sales Market Size Report, 2021-2028. Grandviewresearch.com. 2018. Available online: https://www.grandviewresearch.com/industry-analysis/electric-motor-market?utm\_source=wordpress&amp;utm\_medium= social&amp;utm\_campaign=Gaurav\_July3\_ict\_ElectricDCMotor\_RD2&amp;utm\_content=Content (accessed on 18 July 2019).
- 69. Goetzler, W.; Sutherland, T.; Reis, C. Energy Savings Potential and Opportunities for High-Efficiency Electric Motors in Residential and Commercial Equipment ; OSTI: Oak Ridge, TN, USA, 2013.
- 70. McCoy, G.A.; Douglass, J.G. Premium Efficiency Motor Selection and Application Guide-A Handbook for Industry ; US Department of Energy: Washington, DC, USA, 2014.
- 71. Kizilyalli Isik, C.; Carlson Eric, P.; Cunningham Daniel, W.; Manser Joseph, S.; Xu, Y.; Liu, A.Y. Wide Band-Gap Semiconductor Based Power Electronics for Energy Efficiency. ARPA.e, 13 March 2018. Available online: https://arpa-e.energy.gov/sites/ default/files/documents/files/ARPA-E\_Power\_Electronics\_Paper-April2018.pdf (accessed on 28 October 2014).
- 72. Lowe, M.; Golini, R.; Gereffi, G. US Adoption of High-Efficiency Motors and Drives: Lessons Learned. Durham, NC. 2010. Available online: http://www.cggc.duke.edu/pdfs/CGGC-Motor\_and\_Drives\_Report\_Feb\_25\_2010.pdf (accessed on 28 October 2014).
- 73. Kohei, S.; Swamy, M.; Kang, J.K.; Hisatsune, M.; Wu, Y.; Kebort, D.; Honea, J. Advantages of High Frequency PWM in AC Motor Drive Applications. In Proceedings of the 2012 IEEE Energy Conversion Congress and Exposition, ECCE 2012, Raleigh, NC, USA, 15-20 September 2012; pp. 2977-2984. [CrossRef]
- 74. Jahns, T. The Past, Present, and Future of Power Electronics Integration Technology in Motor Drives. CPSS Trans. Power Electron. Appl. 2017 , 2 , 197-216. [CrossRef]
- 75. Di, H.; Ogale, A.; Li, S.; Li, Y.; Sarlioglu, B. Efficiency Characterization and Thermal Study of GaN Based 1 kW Inverter. In Proceedings of the IEEE Applied Power Electronics Conference and Exposition-APEC, Fort Worth, TX, USA, 16-20 March 2014; pp. 2344-2350. [CrossRef]
- 76. Rice, J.; Mookken, J. Economics of High Efficiency SiC MOSFET Based 3-Ph Motor Drive. In Proceedings of the PCIM Europe 2014: International Exhibition and Conference for Power Electronics, Intelligent Motion, Renewable Energy and Energy Management, Nuremberg, Germany, 20-22 May 2014; pp. 1003-1010.
- 77. Vogel, K.; Rossa, A.J. Improving Efficiency in AC Drives: Comparison of Topologies and Device Technologies. In Proceedings of the PCIM Europe 2014: International Exhibition and Conference for Power Electronics, Intelligent Motion, Renewable Energy and Energy Management, Nuremberg, Germany, 20-22 May 2014; pp. 509-516.
- 78. Ozpineci, B. Oak Ridge National Laboratory Annual Progress Report for the Power Electronics and Electric Motors Program. 2015. Available online: http://info.ornl.gov/sites/publications/files/Pub59624.pdf (accessed on 26 July 2023).
- 79. Sten, K.; Kushnir, D. How Energy Efficient Is Electrified Transport. In Systems Perspectives on Electromobility ; Sand n, B., é Wallgren, P., Eds.; Chalmers University of Technology: Gothenburg, Sweden, 2013; p. 184. Available online: https://publications. lib.chalmers.se/records/fulltext/179113/local\_179113.pdf (accessed on 26 July 2023).
- 80. Mitova, R.; Ghosh, R.; Mhaskar, U.; Klikic, D.; Wang, M.; Dentella, A. Investigations of 600-V GaN HEMT and GaN Diode for Power Converter Applications. IEEE Trans. Power Electron. 2014 , 29 , 2441-2452. [CrossRef]
- 81. Burger, B.; Kranzer, D.; Stalter, O. Cost Reduction of PV-Inverters with SiC-DMOSFETs. In Proceedings of the 2008 5th International Conference on Integrated Power Systems, Nuremberg, Germany, 11-13 March 2008.
- 82. Stubbe, T.; Kunze, M. GaN Power Semiconductors for PV Inverter Applications-Opportunities and Risks. In Proceedings of the CIPS 2014: 8th International Conference on Integrated Power Electronics Systems, Nuremberg, Germany, 25-27 February 2014.
- 83. Shiozaki, K.; Toshiyuki, K.; Lee, J.; Miyagi, K. Verification of High Frequency SiC On-Board Vehicle Battery Charger for PHV ; SAE Technical Paper 2016-01-1210; SAE: Warrendale, PA, USA, 2016.
- 84. Su, G.-J.; Tang, L. An integrated onboard charger and accessory power converter using WBG devices. In Proceedings of the 2015 IEEE Energy Conversion Congress and Exposition (ECCE), Montreal, QC, Canada, 20-24 September 2015; pp. 6306-6313.
- 85. EV Everywhere: Grand Challenge Blueprint. 31 January 2013. Available online: https://www.energy.gov/sites/prod/files/2014 /02/f8/eveverywhere\_blueprint.pdf (accessed on 26 July 2023).
- 86. Ricardo, F.; Moura, P.; Delgado, J.; De Almeida, A.T. A Sustainability Assessment of Electric Vehicles as a Personal Mobility System. Energy Convers. Manag. 2012 , 61 , 19-30. [CrossRef]
- 87. Chinthavali, M.; Otaduy, P.; Ozpineci, B. Comparison of Si and SiC Inverters for IPM Traction Drive. In Proceedings of the 2010 IEEE Energy Conversion Congress and Exposition, Atlanta, GA, USA, 12-16 September 2010; pp. 3360-3365. [CrossRef]
- 88. Hamada, K.; Nagao, M.; Ajioka, M.; Kawai, F. SiC-emerging power device technology for next-generation electrically powered environmentally friendly vehicles. IEEE Trans. Electron. Devices 2015 , 62 , 278-285. [CrossRef]
- 89. Su, M.; Chen, C.; Sharma, S.; Kikuchi, J. Performance and cost considerations for SiC-based HEV traction inverter systems. In Proceedings of the 2015 IEEE 3rd Workshop on Wide Bandgap Power Devices and Applications (WiPDA), Blacksburg, VA, USA, 2-4 November 2015; pp. 347-350.
- 90. Williams, J.; Haley, B.; Kahrl, F.; Moore, J.; Jones, A.; Torn, M.; McJeon, H. Pathways to Deep Decarbonization in the United States ; Energy and Environmental Economics, Inc.: San Francisco, CA, USA, 2014.

- 91. Sadik, O.; Acar, F.; Selamogullari, U.S. Comparison of Silicon Carbide MOSFET and IGBT Based Electric Vehicle Traction Inverters. In Proceedings of the 2015 International Conference on Electrical Engineering and Informatics (ICEEI), Denpasar, Indonesia, 10-11 August 2015. [CrossRef]
- 92. Pierre, D.; Whitney, J. Data Center Efficiency Assessment. 2014. Available online: http://www.nrdc.org/energy/data-centerefficiency-assessment.asp (accessed on 26 July 2023).
- 93. Brown, R.; Masaet, E.; Nordman, B.; Shehabi, B.T.A.; Stanley, J.; Koomey, J.; Sartor, P.; Chan, P.; Alliance to Save Energy; ICF Incorporated; et al. Report to Congress on Server and Data Center Energy Efficiency: Public Law 109-431 ; Lawrence Berkeley National Laboratory: Berkeley, CA, USA, 2007. Available online: https://www.osti.gov/servlets/purl/929723 (accessed on 26 July 2023).
- 94. Scheihing, P. DOE Data Center Energy Efficiency Program. April 2009. Available online: https://www1.eere.energy.gov/ manufacturing/tech\_assistance/pdfs/doe\_data\_centers\_presentation.pdf (accessed on 26 July 2023).
- 95. Pearsall, N.M. Introduction to photovoltaic system performance. In The Performance of Photovoltaic (PV) Systems ; Woodhead Publishing: Cambridge, UK, 2017; pp. 1-19.
- 96. Masanet, E.R.; Brown, R.E.; Shehabi, A.; Koomey, J.G.; Nordman, B. Estimating the Energy Use and Efficiency Potential of U.S. Data Centers. Proc. IEEE 2011 , 99 , 1440-1453. [CrossRef]
- 97. Simonetti, V. Lo Standard a Protezione Dell'ambiente e Dei Consumatori: Un Caricabatterie Comune per Gli Stati Membri UE ; Luiss Guido Carli: Rome, Italy, 2022.
- 98. Eykyn, J. The World Market for AC-DC &amp; DC-DC Merchant Power Supplies-2013 Edition ; IHS: Wellingborough, UK, 2013; Volume 9790.
- 99. Huston, E.; Swisher, J.; Burns, C.; Seal, J.; Emerson, B. Design Recommendations for High-Performance Data Centers ; Rocky Mountain Institute: Snowmass, CO, USA, 2003.
- 100. Morrow, L. Mitsubishi Electric Introduces New SUMMIT Series UPS. Mission Critical , 8 September 2015.
- 101. ORNL. Power Electronics for Distributed Energy Systems and Transmission and Distribution Applications ; ORNL: Oak Ridge, TN, USA, 2006.
- 102. SMA Solar Technology. Technical Information Efficiency and Derating WKG-Derating-US-TI-en-15 Version 1.5 ; SMA Solar Technology: Niestetal, Germany, 2016.
- 103. EIA. Annual Energy Outlook 2013. Available online: http://www.eia.gov/forecasts/aeo/ (accessed on 26 July 2023).
- 104. McDonald, T. Impact of Commercialization of GaN based Power Devices on PV Solar Power 625 Generation. International Rectifier. 2011. Available online: http://www.arpa-626e.energy.gov/sites/default/files/documents/files/SolarADEPT\_Workshop\_ NxtGenPwr\_McDonald.pdf (accessed on 26 July 2023).
- 105. NREL. 2012 Renewable Energy Data Book. 2012. Available online: http://www.nrel.gov/docs/fy14osti/60197.pdf (accessed on 26 July 2023).
- 106. Zhang, H.; Tolbert, L.M.; Ozpineci, B. Impact of SiC Devices on Hybrid Electric and Plug-In Hybrid Electric Vehicles. IEEE Trans. Ind. Appl. 2011 , 47 , 912-921. [CrossRef]
- 107. Yu, L.; Dunne, G.; Matocha, K.; Cheung, K.; Suehle, J.; Sheng, K. Reliability Issues of SiC MOSFETs: A Technology for HighTemperature Environments. IEEE Trans. Device Mater. Reliab. 2010 , 10 , 418-426. [CrossRef]
- 108. Ellis, M.; Jollands, N. Gadgets and Gigawatts: Policies for Energy Efficient Electronics ; International Energy Agency: Paris, France, 2009. Available online: https://www.iea.org/reports/gadgets-and-gigawatts-2 (accessed on 26 July 2023).

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.