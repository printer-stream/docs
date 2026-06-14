Rev.2.52 

- Notes: • The printer transmits all data after starting transmission of the header without confirming whether the host computer can receive data.  Therefore, when using this command, the host reception buffer size should be set to (transmission data + 2) to ensure that reception is not lost. 

- Real-time command (DLE expansion command) is ignored while transmitting data. Also, ASB status is not transmitted while transmitting data even when the ASB function is enabled. Therefore, status changes in the printer while transmitting data are not known.  The operator should be aware of this. 

- STAR • STAR printers ignore this command.   (They receive and discard FS g 2 m a1 a2 a3 a4 nL nH.) 

- Reference FS g 1 

ESC/POS Command Specifications 

81 
