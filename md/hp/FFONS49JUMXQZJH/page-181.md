RESPONSE 

<DEC> The response is the decimal equivalent of a 16-bit immediate status word, followed by the output terminator. The maximum value output is 40. 

The extended status word bits are as defined in the following table. 

|||Decimal||
|---|---|---|---|
|Bit||State|Value|Meaning|
|0-2|0|0|Not used, always zeros. Re-|
||||served for plotters with|
||||paper advance.|
|3|0|0|Buffer is not empty.|
||1|8|Buffer is empty and ready|
||||for data.|
|4,5|00|0|Ready toprocess or process-|
||||ing HP-GL instructions.|
||01|16|Paper loaded, view button|
||||pressed so graphics sus-|
||||pended.|
||10|32|Paper leverraised so graph-|
||||icssuspended.|



Combinations of these bits allow five different responses to the ESC . O instruction. 

|0|Buffer is notempty and plotter is process-|
|---|---|
||ing HP-GL instructions.|
|8|Buffer is empty and is ready to process|
||or is processing HP-GL instructions.|
|16|Buffer is not empty and view has been|
||pressed.|
|24|Buffer is empty and view has been|
||pressed.|
|32|Buffer is not empty and paper lever and|
||pinch wheels are raised.|
|40|Buffer is empty and paper lever and|
||pinchwheelsareraised.|



[TERM] The output terminator defaults to carriage return unless itis set by ESC . M. 

RS-232-C/CCITT V.24 INTERFACING 10-39 
