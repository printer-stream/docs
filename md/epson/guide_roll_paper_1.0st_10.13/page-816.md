## **C O N F I D E N T I A L** 

**When "Layout reference (** sm **= "1," "2," "3")" and "vertical layout (** sa **= "0") are specified, even if paper feed of about 155 mm is executed, if the print reference cannot be found, a paper error occurs. This is caused by using paper that is outside the specifications. Loading paper that meets the product specifications recovers from the error.** 

**When "Layout reference (** sm **= "1," "2," "3")" and "vertical layout (** sa ≠ **"0") are specified, if any of the following situations are detected, a paper layout error occurs. This is because the paper used and the "vertical layout (** sa **)" setting value set with this function are different. After loading the correct paper,** DLE ENQ (n = 2) **recovers from the error.** 

- **(a) When the next print reference is detected when paper feed that does not fulfill (** sa **setting value - 1.25 mm) after the print reference is passed.** 

- **(b)When the next eject reference is detected when paper feed that does not fulfill (** sa **setting value - 1.25 mm) after the eject reference is passed.** 

- **(c) When the next print reference is not found even when paper feed that fulfills (** sa **setting value + 1.25 mm) after the print reference is passed.** 

- **(d)When the next eject reference is not found even when paper feed that fulfills (** sa **setting value + 1.25 mm) after the eject reference is passed.** 

- **(e) With mechanical initialization when memory switch [** Msw8-6 **] is on, in any of the following cases** 

   - **When the next print reference is detected when paper feed that does not fulfill (** sa **setting value - 1.25 mm - special machine value (setting value of <Function 80> of this command)) is being executed after mechanical initialization.** 

   - **When the next print reference is not found even when paper feed that fulfills (** sa **setting value + 1.25 mm + special machine value (setting value of <Function 80> of this command)) is executed after mechanical initialization.** 

- **Irrespective of whether the correct paper is used, if a paper layout error occurs when printing the first sheet after mechanical initialization (when the peeler cover is closed, when the power is turned on, or the printer is reset), the paper may not be set in the correct position. When it is difficult to position the paper, it is possible to avoid paper layout errors by changing the setting value of <Function 80>. Refer to <Function 80> of this command for details of this command.** 

**The horizontal size of the printable area, specified with horizontal layout (** sf **) and layout reference (** sm **) is as shown in the table below.** 
