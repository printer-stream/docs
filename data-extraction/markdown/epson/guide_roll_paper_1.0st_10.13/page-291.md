## C O N F I D E N T I A L

- ❏ Specify the size of image data not to exceed the current print area.
- ❏ Do not specify data again for already saved colors.

Example: Specifying (Color 1 -&gt; Color 2 -&gt; Color 1 -&gt; Print) causes a drop in performance.

- ❏ A graphic that exceeds the size limit of ( yL + yH × 256) can be printed by the repeated use of the combination of this function and &lt;Function 50&gt; of this command. In that case, the performance may be best when the vertical size is specified less than half of the domain by this function. The most suitable vertical size depends on the specifications of the PC, the interface used and other factors.

Example: ( yL + yH × 256) ≤ 831 (when zoom of ( by =1 is specified)) when single-color printing control is specified.

With the above method, if banding appears in the print results and the processing time is not reduced, it is possible that data transmission from the PC is not fast enough for the processing time of the printer. Check the PC data transmission speed.

If there is a problem with the PC, it may be possible to prevent banding occurring by slowing down printing speed with GS ( K &lt;Function 50&gt; or by increasing the number of head energizing strokes with GS ( K &lt;Function 97&gt;, but the performance will decrease.

## TM-T88V

The dot density and maximum print area are the same as Function 69. See the model information of Function 69.

Use the following settings (except when using a serial interface) for fastest processing time.

- ❏ Check that there is space in the receive buffer of the printer before transmitting this function when transmitting the first graphic data. (You can check that the receive buffer is empty by executing status receiving of GS r ( n = 1, 49)).

Example: Example of data processing:

GS r -&gt; Status receiving -&gt; This function (color 1) -&gt; This command &lt;Function 50&gt; -&gt; This function (color 1) -&gt; This command &lt;Function 50&gt;

- ❏ Specify standard mode.
- ❏ Specify "Left-justified" with ESC a .
