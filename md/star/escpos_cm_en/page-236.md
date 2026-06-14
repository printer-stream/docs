Rev.2.52 

## **ESC GS h 1 k m n** 

Name Water mark function Code ASCII ESC GS h 1 k m n Hex. 1B 1D 68 31 k m n Decimal 27 29 104 49 k m n 0 ≤ k ≤ 2 0 ≤ m ≤ 2 1 ≤ n ≤ 255 Defined Area Initial Value --Function Enables/disables water mark function. 

|Function|Enables/disables water mark function.|
|---|---|
|k|Water Mark Function|
|0|Disabled|
|1|Enabled<br>Prints 1 logo specifed byn atposition centered in horizontal and vertical directions.|
|2|<br>Enabled<br>Repeatedly prints the logo specifed by n from top edge of page to bottom edge of page at<br>position centered in horizontal direction.|



To make the image appropriate for a water mark, set the logo data forming method to print as the water mark using this setting. 

If it is not possible to the appropriate image using this setting, reregister the logo data registered as the water mark after forming it to the appropriate data. 

||To make the image appropriate for a water mark, set the logo data forming method t<br>the water mark using this setting.<br>If it is not possible to the appropriate image using this setting, reregister the logo dat<br>registered as the water mark after forming it to the appropriate data.|
|---|---|
|m|Water Mark Data FormingMethod<br>|
|0|Prints logo data specifed byn as it is.<br>|
|1|<br>Thins logo data specifed byn 25% forprinting.<br>|
|2|<br>Thins logo data specifed byn 12.5% forprinting.|
|<br>Specify the registered logo as the water mark.||



|m<br>0<br>1<br>2|Water Mark Data FormingMethod<br>Prints logo data specifed byn as it is.<br>Thins logo data specifed byn 25% forprinting.<br>Thins logo data specifed byn 12.5% forprinting.<br>Specify the registered logo as the water mark.|
|---|---|
|n|Logo Number|
|1-255|Registered logo number<br>If the specifed logo number is not registered,the water mark will not beprinted.|



## <Water Mark Function> 

When the water mark function is enabled, the water mark is printed by a water mark printing trigger. 

However, this function is executed on print data built-up within the image buffer length. 

Water mark printing is ignored when there is print data beyond the length of the image buffer. 

Water mark is ignored when in 2-color mode, page mode, when registering macros and when executing macros if printing is started by anything other than the following water mark triggers. This setting is not cleared by <ESC> @ or <CAN>. 

Water mark triggers 

• Cut command: <GS> V m n,<GS> V m • BM detection command: <GS> <FF>,<FF>,<GS> < • Print start command: <ESC> <GS> g 0 m n 

## Usage example 

1) Register logo to logo number 1 when using water mark. 

- 2) Water mark function enable: <ESC> <GS> h 1 k m n (k=0x02,m=0x01,n=0x01) 3) Print data transmission:  Print data (Print length should be within image buffer length) 4) Trigger command transmission: <GS> V m n (Cutter command is water mark print trigger.) 

ESC/POS Command Specifications 

236 
