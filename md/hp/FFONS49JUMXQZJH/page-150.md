## Monitor Mode 

> Afterexclusivethe monitorplotter ismodesin the mayon-line,be enabledprogrammed-onusing the setstate,plottertwoconfigura-mutually | tion instruction, ESC .@. Depending upon which monitor mode is enabled, either all data (including device control instructions) are retransmitted to the terminal CRT or only HP-GL data are retransmitted as they are parsed from the plotter’s buffer. All plotter output responses are sent to both the computer and terminal. Refer to The Set Plotter Configuration Instruction, ESC . @, for complete information. 

The plotter monitors for a terminal-generated Break signal. Receipt of a Break signal will cause the same results as described under the on-line, programmed-on state. Then, new plotter on and set plotter configuration instructions from the computer are required to resume plotting operations with monitor mode active. The following diagram shows how the plotter processes data while in monitor mode. 

**==> picture [329 x 173] intentionally omitted <==**

**----- Start of picture text -----**<br>
COMPUTER<br>Ht TERMINAL<br>= ~L oS<br>PLOTTER ——s<br>PROCESSOR<br>SCANS FOR<br>“BREAK”<br>PLOTTER<br>INSTRUCTIONS<br>**----- End of picture text -----**<br>


Monitor Mode 

10-8 RS-232-C/CCITT V.24 INTERFACING 
