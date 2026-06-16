## C O N F I D E N T I A L

- ■ The same symbol can be printed by executing &lt;Function 381&gt; repeatedly after executing &lt;Function 380&gt; of this command.
- ■ Using &lt;Function 382&gt; of this command, the size of the symbol printed with &lt;Function 381&gt; can be acquired.

## [Notes for Composite Symbology processing (when cn = 52 is specified)]

- ■ The composite symbol (line element/2D composite element) symbol data specified by &lt;Function 480&gt; of this command (d1...dk) is temporarily stored in the archive area of the printer and is printed by &lt;Function 481&gt;.
- ■ The setting value of &lt;Function 467&gt; and &lt;Function 472&gt; is used when processing &lt;Function 481&gt; and &lt;Function 482&gt; of this command. Furthermore, the setting value of &lt;Function 471&gt; is used when processing GS1 DataBar Expanded Stacked. If the printing area is narrow, it may not be possible to print the symbol.
- ■ The same symbol can be printed by executing &lt;Function 481&gt; repeatedly after executing &lt;Function 480&gt; of this command.
- ■ Composite Symbology with a different combination can be printed by resending other symbol data with either of the line element or 2D composite element as it is.

Step 1) Specify &lt;Function 480: (a = 49, b = 65)&gt;, and send the 2D composite element data.

Step 2) Specify &lt;Function 480: (a = 48, b = 70)&gt;, and send the line element data.

Step 3) Print Composite Symbology of which GS1 DataBar Omnidirectional is the line element with &lt;Function 481&gt;.

- Step 4) Specify &lt;Function 480: (a = 48, b = 74)&gt;, and send the line element data.

Step 5) Print Composite Symbology of which GS1 DataBar Limited is the line element with &lt;Function 481&gt;.

- ■ Using &lt;Function 482&gt; of this command, the size of the symbol printed with &lt;Function 481&gt; can be acquired.

[Notes for transmission process]

- ■ Transmission process is performed by &lt;Function 082&gt;, &lt;Function 182&gt;, &lt;Function 282&gt;, &lt;Function 382&gt;, and &lt;Function 482&gt;. When you use this command, follow these rules.
