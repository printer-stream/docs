## **C O N F I D E N T I A L** 

## **ESC =** 

SETTING COMMAND 

[Name] Select peripheral device [Format] ASCII ESC = n Hex 1B 3D n Decimal 27 61 n [Range] TM-T90, TM-L90, TM-P60, TM-U230, TM-U220 **: 1** ≤ **n** ≤ **3** TM-T20 **,** TM-T88IV **,** TM-T88V **: 0** ≤ n ≤ **255 TM-T70: 1** ≤ **n** ≤ **3 [When ANK model and TM-T88IV command-compatible is disabled] 0** ≤ **n** ≤ **255 [When ANK model and TM-T88IV command-compatible is enabled] 1** ≤ **n** ≤ **3 [Japanese model]** 

- [Default] TM-J2000/J2100 **: Serial interface model:** n **= 1 When [memory switch [DM-D (customer display) connection] is OFF.** n **= 2 When [memory switch [DM-D (customer display) connection] is ON. Parallel interface model:** n **= 1** 

- TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60, TM-U230, TM-U220 **:** n **= 1** 

- [Printers not featuring this command] None 

[Default] Selects the device to which the host computer transmits data, using n as follows: 

|n|**Function**|
|---|---|
|1,3|Enables printer.|
|2|Disables printer.|



- [Notes] ■ When the printer is disabled, it ignores all received data and commands with the exception of ESC = and real-time commands. 

   - If ASB is enabled when the printer is disabled by this command, the printer transmits the ASB status message whenever the status changes. See the description of GS a for ASB function. 

   - Settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off. 
