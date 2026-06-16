## C O N F I D E N T I A L

## GS ( L pL pH m fn &lt; Function 50 &gt;

```
[Name] Print the graphics data in the print buffer. [Format] ASCII GS ( L pL pH m fn Hex 1D 28 4C 02 00 30 fn Decimal 29 40 76 2 0 48 fn [Range] ( pL + pH × 256) = 2 ( pL = 2, pH = 0) m = 48 fn = 2, 50
```

[Description] [Notes]

Prints the buffered graphics data stored by the process of GS ( L &lt;Function 112 or 113&gt;.

- ■ The printer cannot print when there is no graphics data stored in the print buffer.
- ■ Functions 112 and 113 of this command are used to store graphics data in the print buffer.
- ■ This function cannot be used when the page mode is enabled.
- ■ Feeds the paper the required distance when printing graphics data, regardless of line feed pitch settings entered using the Set line feed command.
- ■ Moves print position to the left side of the print area after printing of graphics data is completed. The printer then enters the 'beginning of the line' or 'no data in print buffer' state.
