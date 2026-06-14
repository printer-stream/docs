## **C O N F I D E N T I A L** 

**most suitable vertical size depends on the specifications of the PC, the interface used and other factors.** 

**Example: (** yL **+** yH × **256)** ≤ **831 (when zoom of (** by **= 1 is specified)).** 

**With the above method, if banding appears in the print results and the processing time is not reduced, it is possible that data transmission from the PC is not fast enough for the processing time of the printer. Check the PC data transmission speed.** 

**If there is a problem with the PC, it may be possible to prevent banding occurring by slowing down printing speed with** GS ( K **<Function 50>, but the performance will decrease.** 

## TM-T88IV 

**Refer to** GS ( E **<Function 5> for specifying printing control (single-color/two-color).** 

**The dot density and maximum print area are the same as Function 69. See the model information of Function 69.** 

**Use the following settings (except when using a serial interface) for fastest processing time.** 

- ❏ **Check that there is space in the receive buffer of the printer before transmitting this function when transmitting the first graphic data. (You can check that the receive buffer is empty by executing status receiving of** GS r **(** n **= 1, 49)).** 

## **Example: Example of data processing:** 

GS r **-> Status receiving -> This function (color 1) -> This function (color 2) -> This command <Function 50> -> This function (color 1) -> This function (color 2) -> This command <Function 50>** 

- ❏ **Specify standard mode.** 

- ❏ **Specify "Left-justified" with** ESC a **.** 

- ❏ **Specify left margin as 0, and the horizontal position to a position that is a multiple of 8, and specify the horizontal size of the graphic to the dot which is the multiple of 8. (Example: the left margin = 0, horizontal position = 8, 16, or 24, 32, etc., (** xL **+** xH × **256) = 64, 128, or 256 etc.)** 

- ❏ **Specify the scaling to the original size (** bx **= 1,** by **= 1).** 
