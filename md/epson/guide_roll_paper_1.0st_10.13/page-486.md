## **C O N F I D E N T I A L** 

## **<The fourth byte: information for recoverable error>** 

|**Bit**|**Off/On **|**Hex **|**Decimal **|**Information**|
|---|---|---|---|---|
|**2**|**Off**|**00**|**0**|**Roll paper layout error hasn’t occurred.**|
||**On**|**04**|**4**|**Roll paper layout error hasn’t occurred.**|
|**3 ~ 5**|**-**|**-**|**-**|**Reserved.**|
|**6**|**On**|**40**|**64**|**Fixed.**|
|**7**|**0**|**00**|**0**|**Fixed.**|



## **Bit 0 is not supported by the** TM-L90 **with Peeler.** 

**When the error of bit 0 or bit 1 occurs, the error can be canceled by executing** DLE ENQ **(** n **= 2) after clearing the error cause.** 

**When the error of bit 2 occurs, the error can be canceled by either of the following. See the printer information of function 3 of** GS ( E **for memory switches details.** 

**When memory switch [Msw8-2] is OFF: execution of** DLE ENQ **(** n **= 2) or opening/closing the cover When memory switch [Msw8-2] is ON: execution of** DLE ENQ **(** n **= 2)** 

**When memory switch [Msw8-1] is OFF: execution of** DLE ENQ **(** n **= 2) or pressing the FEED button [** TM-L90 **with Peeler]** 

**When memoery switch [Msw8-1] is ON: execution of** DLE ENQ **(** n **= 2) [** TM-L90 **with Peeler]** 

## **<The fifth byte: information for unrecoverable error>** 

|**Bit**|**Off/On **|**Hex **|**Decimal **|**Function**|
|---|---|---|---|---|
|**0**|**Off**|**00**|**0**|**Roll paper cover open error hasn’t occurred.(When Msw [8-8] is OFF)**|
||**On**|**01**|**1**|**Roll paper cover open error has occurred.(When Msw [8-8] is OFF)**|
|**2 ~ 5**|**-**|**-**|**-**|**Reserved.**|
|**6**|**On**|**40**|**64**|**Fixed.**|
|**7**|**0**|**00**|**0**|**Fixed.**|
