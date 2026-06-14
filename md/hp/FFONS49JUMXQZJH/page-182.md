The Reset Handshake Instruction, ESC .R 

The reset handshake instruction, ESC. R, resets all handshake parameters to their default values. 

| USES | The instruction may be used to set the plotter’s handshake responses to a known state with hardwire handshake enabled. 

-R 

Executing this command is the same as executing the following commands without parameters: ESC. @, ESC. H, ESC. I, ESC. M, and ESC .N. x 

The following table shows the default values of parameters used to establish handshakes. 

**==> picture [313 x 208] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||
|---|---|---|---|---|---|---|---|---|
|block|size|80|
|enquiry|character|0 —|no|enquiry|character|
|acknowledgment|string|0 —|no|acknowledgment|string|
|turnaround|delay|0 —|no|delay|
|output|trigger|character|0 —|no|trigger|character|
|echo|terminate|character|0|—|no|echo|terminate|character|
|output|terminator|13;0;|—|carriage|return|
|output|initiator|0 —|no|output|initiator|
|intercharacter|delay|0 —|no|delay|
|immediate|response|string|0 —|no|immediate|response|string|
|monitor|mode|disabled|
|hardwire handshake|(pin|20)|enabled|

**----- End of picture text -----**<br>


10-40 RS-232-C/CCITT V.24 INTERFACING 
