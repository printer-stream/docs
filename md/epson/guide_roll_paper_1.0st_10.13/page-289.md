## **C O N F I D E N T I A L** 

- ❏ **A graphic that exceeds the size limit of (** yL **+** yH × **256) can be printed by the repeated use of the combination of this function and <Function 50> of this command. In that case, the performance may be best when the vertical size is specified as [59** ≤ **(** yL **+** yH × **256)** ≤ **246 (reference value)] by this function. However, the value is only a reference value. The most suitable vertical size depends on the specifications of the PC, the interface used and other factors.** 

**If the time of processing this function cannot be shortened when processing the above-mentioned item, the printing result may include horizontal stripes. In this case, transmit the graphic data specified within the maximum range of (** yL **+** yH × **256) one time to prevent the horizontal stripe but the performance will decrease.** 

## TM-T20 

**The dot density and maximum print area are the same as Function 69. See the model information of Function 69.** 

**Use the following settings (except when using a serial interface) for fastest processing time.** 

❏ **Check that there is space in the receive buffer of the printer before transmitting this function when transmitting the first graphic data. (You can check that the receive buffer is empty by executing status receiving of GS r (** n **= 1, 49)).** 

## **Example: Example of data processing:** 

GS r **-> Status receiving -> This function (color 1) -> This command <Function 50> -> This function (color 1) -> This command <Function 50>** 

- ❏ **Specify standard mode.** 

- ❏ **Specify "Left-justified" with** ESC a **.** 

- ❏ **Specify the scaling to the original size (** bx **= 1,** by **= 1).** 

- ❏ **Specify the size of image data not to exceed the current print area.** 

- ❏ **Do not specify data again for already saved colors. Example: Specifying (Color 1 -> Color 1 -> Print) causes a drop in performance.** 

- ❏ **A graphic that exceeds the size limit of (** yL **+** yH × **256) can be printed by the repeated use of the combination of this function and <Function 50> of this command. In that case, the performance may be best when the vertical size is specified less than half of the domain by this function. The** 
