## **C O N F I D E N T I A L** 

## TM-L90 

**When it meets either of the following requirements, bit 0 of [Position Information B] becomes “The print start operation of the label is possible now.” Set the paper layout (** sb, sd, se **) using Function 49 of** GS ( E **.** 

- **(1)When position information A is “Standby at the label peeling position” (soon after executing this command** fn **= 65) and when it meets either of the following requirements:** 

■ **If (** se ≤ sd **), 24 mm {0.94 inch}** ≤ **(** sb **-** se **) and 3.6 mm {0.14 inch}** ≤ **(** sd **-** se **)** 

■ **If (** sd **<** se **), 24 mm {0.94 inch}** ≤ **(** sb × **2 -** se **) and 3.6 mm {0.14 inch}** ≤ **(** sb **+** sd **–** se **)** 

- **(2)When position information A is “Standby at the cutting position” (soon after executing this command** fn **= 66) and when it meets either of the following requirements:** 

■ **If (** se ≤ sd **), 14 mm {0.55 inch}** ≤ **(** sb **-** se **) and 3.6 mm {0.14 inch}** ≤ **(** sd **-** se **)** 

■ **If (** sd **<** se **), 14 mm {0.55 inch}** ≤ **(** sb × **2 –** se **) and 3.6 mm {0.14 inch}** ≤ **(** sb **+** sd **–** se **) When it meets either of the following requirements, bit 1 of [Position information B] becomes “The print start operation of the next label is possible.”** 

- **(1)When position information A is “Standby at the label peeling position” (soon after executing this command** fn **= 65) and when it meets either of the following requirements:** 

■ **If (** se ≤ sd **), 24 mm {0.94 inch}** ≤ **(** sb × **2 –** se **) and 3.6 mm {0.14 inch}** ≤ **(** sb **+** sd **–** se **)** 

■ **If (** sd **<** se **), 24 mm {0.94 inch}** ≤ **(** sb × **3 –** se **) and 3.6 mm {0.14 inch}** ≤ **(** sb × **2 +** sd **–** se **) (2)When position information A is “Standby at the cutting position” (soon after executing this command** fn **= 66) and when it meets either of the following requirements:** 

■ **If (** se ≤ sd **), 14 mm {0.55 inch}** ≤ **(** sb × **2 –** se **) and 3.6 mm {0.14 inch}** ≤ **(** sb **+** sd **–** se **)** 

■ **If (** sd **<** se **), 14 mm {0.55 inch}** ≤ **(** sb × **3 –** se **) and 3.6 mm {0.14 inch}** ≤ **(** sb × **2 +** sd **–** se **)** 
