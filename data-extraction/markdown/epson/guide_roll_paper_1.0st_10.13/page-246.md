## C O N F I D E N T I A L

## GS ( L pL pH m fn d1 d2 d3 &lt; Function 65&gt;

[Name] Delete all NV graphics data. [Format] ASCII GS ( L pL pH m fn d1 d2 d3 Hex 1D 28 4C 05 00 30 41 43 4C 52 Decimal 29 40 76 5 0 48 65 67 76 82 [Range] ( pL + pH × 256) = 5 ( pL = 5, pH = 0) m = 48 fn = 65 d1 = 67 d2 = 76 d3 = 82

[Description]

[Notes]

Deletes all NV graphics data that has been defined using Functions 67 or 68.

- Deleted areas are designated 'Unused areas.'
- All key codes are designated as undefined.
- ■ Use this function at the beginning of the line when the standard mode is selected.
- ■ This function is incompatible with macros, so be sure to avoid including it when defining macros.
- ■ When NV graphics data is being shared by multiple applications, executing this function will delete all data being used by all applications. Caution is required when using this function.
