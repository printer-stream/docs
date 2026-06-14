## Operation 

**==> picture [1 x 2] intentionally omitted <==**

**----- Start of picture text -----**<br>
|<br>**----- End of picture text -----**<br>


The rear-panel switch labeled ¥/pD should be set to D. If it is set to y, the plotter must receive a plotter on instruction, ESC .( or ESC. Y, before it will respond to other commands from the terminal. The terminal should be set to half duplex in order to view the characters being sent to the plotter. Plotter output will be displayed on the terminal. The following diagram shows plotter operation when in the programmed-on state in a terminal-only environment. 

**==> picture [257 x 165] intentionally omitted <==**

**----- Start of picture text -----**<br>
TERMINAL<br>iN<br>HALF<br>DUPLEX<br>TL<br>PLOTTER —)<br>OUTPUT<br>PLOTTER<br>INSTRUCTIONS<br>**----- End of picture text -----**<br>


Terminal-only Environment, Programmed On 

## Connecting the RS-232-C Interface 

The 7470 plotter interfaces to the RS-232-C communications lines through a standard 25-pin female connector mounted on the back of the plotter. The 7470 is capable of operating in a three-wire (transmit, receive, ground) configuration. 

In hardwired handshake operation, the Data Terminal Ready line (pin 20 of the connector on the plotter) is used to monitor the space in the buffer available for input. The plotter outputs data when requested (refer to Hardwire Handshake in this chapter). 

If you are fabricating the cable assembly, the connector should be a 25-pin type “D” subminiature CINCH DBC-25P plug or equivalent. 

Connector pin allocations for the three-wire configuration are identified and described in the following table. 

10-10 RS-232-C/CCITT V.24 INTERFACING 
