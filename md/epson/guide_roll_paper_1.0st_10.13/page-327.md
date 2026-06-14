## **C O N F I D E N T I A L** 

## **DLE EOT** 

EXECUTING COMMAND 

[Name] Transmit real-time status [Format] ASCII DLE EOT n [a] Hex 10 04 n [a] Decimal 16 4 n [a] 

[Printers not featuring this command] None 

[Range] TM-J2000/J2100 **: 1** ≤ n ≤ **4,** n **= 7** a **= 1, 2 [When** n **= 7]** TM-T90, TM-T70, TM-P60, TM-U230, TM-U220 **: 1** ≤ n ≤ **4,** n **= 7** TM-T20,TM-T88IV, TM-T88V **: 1** ≤ n ≤ **4** 

TM-L90 **: 1** ≤ n ≤ **4,** n **= 8,** a **= 3 (when** n **= 8) (** TM-L90 **with Peeler) 1** ≤ n ≤ **4 (** TM-L90 **without Peeler)** 

TM-P60 **: 1** ≤ n ≤ **4,** n **= 8,** a **= 3 (when** n **= 8) (** TM-P60 **with Peeler) 1** ≤ n ≤ **4 (** TM-P60 **without Peeler)** 

[Description] Transmits the real-time status, using n as follows: 

|n|a|**Function**|
|---|---|---|
|1|--|Transmit printer status|
|2|--|Transmit offline status|
|3|--|Transmit error status|
|4|--|Transmit roll paper sensor status|
|7|1|Transmit ink status A|
||2|Transmit ink status B|
|8|3|Transmit peeler status|



Omit the parameter **a** when (1 ≤ n ≤ 4) Transmit the parameter **a** when (n = 7) 

DLE EOT **BEL** is DLE EOT **(** n **=7)** ; for some previous printer models this command is called DLE EOT **BEL** . 
