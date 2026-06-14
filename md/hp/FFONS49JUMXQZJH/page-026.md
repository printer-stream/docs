The P-mask value specifies which of the status-byte conditions will result in a logical 1 response to a parallel poll over the HP-IB interface. 

|P-Mask|Status Bit|||
|---|---|---|---|
|BitValue|Number||Meaning|
|1|0|Pen down||
|2|1|P1 or P2 changed||
|4|2|Digitized point available||
|8|3|Initialized||
|16|4|Ready for|data; pinch wheels down|
|32|5|Error||



For example, a P-mask value of 48 specifies that only bits 4 and 5 (16 + 32) of the status byte can cause the plotter to respond to a parallel poll with a logical 1 on the appropriate data line. 

The plotter, when set to default values or initialized, automatically sets the E-mask to 223, the S-mask to 0, and the P-mask to 0. An IM command without parameters or with invalid parameters also sets the masks to the default values 223,0,0. 

1-14 GETTING STARTED 
