## C O N F I D E N T I A L

## GS ( P

[Name]

Page mode control

[Printers not featuring this command]

[Description]

[Notes]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-U220 , TM-U230

Executes various controls regarding page mode.

- The function is specified with the function code ( fn ).
- pL and pH specify the number of bytes following fn as ( pL + pH × 256).
- [parameter] is covered in the description of each function.
- ■ With this command, the function is decided by the function code ( fn ). The detailed operation differs with each function.

|   fn | Function No.   | Function name                                     |
|------|----------------|---------------------------------------------------|
|   48 | Function 48    | Printable area setting when page mode is selected |

```
Program example
```

```
PRINT #1, CHR$(&h1D);"(P";CHR$(8);CHR$(0);CHR$(48); ← <Function 48> PRINT #1, CHR$(255);CHR$(255); PRINT #1, CHR$(144);CHR$(1); ← Sets the vertical size of the printable area to 400 when the page mode is selected PRINT #1, CHR$(0);CHR$(0); PRINT #1, CHR$(1);
```

[Model-dependent variations]

TM-P60

## TM-P60

TM-P60 with Peeler supports this function.

EXECUTING COMMAND
