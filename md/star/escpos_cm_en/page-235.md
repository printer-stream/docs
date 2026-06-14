Rev.2.52 

## **4-3-12 STAR Original Page Function Commands** 

## **ESC GS h 0 k m n** 

Name 180˚ inversion function Code ASCII ESC GS h 0 k m n Hex. 1B 1D 68 30 k m n Decimal 27 29 104 48 k m n 0 ≤ k ≤ 1 m=0 n=0 Defined Area Initial Value --Function Enables/disables 180˚ inversion function 

|Defned Area<br>Initial Value<br>Function|Hex.<br>1B<br>1D<br>68<br>30<br>k<br>m<br>n<br>Decimal<br>27<br>29 104<br>48<br>k<br>m<br>n<br>0≤k≤1<br>m=0 n=0<br>---<br>Enables/disables 180˚ inversion function|
|---|---|
|n|180˚ Inversion Function|
|0|Disabled|
|1|Enabled|



## <180˚ Inversion Function> 

Executes a 180˚ inversion by a 180˚ inversion trigger when this function is set. 

However, this function is executed on print data built-up in the image buffer. 

The 180˚ inversion function is ignored if there is print data longer than the image buffer. 

Also, the 180 degree inversion function is ignored if printing is started by settings other than the following 180 degree inversion trigger while the print startup control is set for each line, if page mode is selected or if a macro is being registered or executed. 

This setting is not cleared by <ESC> @ or <CAN>. 

180˚ inversion triggers 

• Cut command: <GS> V m n ,<GS> V m • BM detection command: <GS> <FF>, <FF> • Print start command: <ESC> <GS> g 0 m n 

Usage example 

1) 180˚ inversion function enabled: <ESC> <GS> h 0 k m n (k=0x01,m=0x00,n=0x00) 2) Print data transmission: Print data (Print length should be within image buffer length) 3) Trigger command transmission: <GS> V m n (Cutter command is 180˚ inversion trigger.) 

ESC/POS Command Specifications 

235 
