## C O N F I D E N T I A L

```
Program Example 1 (Set customized memory value) PRINT #1, CHR$(&H1D);"(E";CHR$(3);CHR$(0);CHR$(1);CHR$(73);CHR$(78); ← <Function 1> GOSUB *RECEIVE ← Check "mode change notice" (Details omitted) PRINT #1, CHR$(&H1D);"(E";CHR$(10);CHR$(0);CHR$(3);CHR$(1); ← <Function 3> PRINT #1, CHR$(50);CHR$(50);CHR$(50);CHR$(50);CHR$(48);CHR$(49);CHR$(48);CHR$(49); PRINT #1, CHR$(&H1D);"(E";CHR$(2);CHR$(0);CHR$(4);CHR$(1); ← <Function 4> GOSUB *RECEIVE 4  ← Check the setting (Details omitted) PRINT #1, CHR$(&H1D);"(E";CHR$(7);CHR$(0);CHR$(5);CHR$(1);CHR$(2);CHR$(0);CHR$(2);CHR$(5);CHR$(0); ← <Function 5> PRINT #1, CHR$(&H1D);"(E";CHR$(2);CHR$(0);CHR$(6);CHR$(1); ← <Function 6> GOSUB *RECEIVE 6  ← Check the setting (Details omitted) PRINT #1, CHR$(&H1D);"(E";CHR$(4);CHR$(0);CHR$(2);CHR$(79);CHR$(85);CHR$(84); ← <Function 2>
```

## Program Example 2 (Read back customized memory value)

PRINT #1, CHR$(&amp;H1D);"(E";CHR$(2);CHR$(0);CHR$(6);CHR$(1); ← &lt;Function 6&gt;

[Model-dependent variations]

## TM-J2000/J2100 , TM-T90

This printer supports &lt;Function 1&gt;, &lt;Function 2&gt;, and the following functions:

- ■ Functions related to printer operational settings: &lt;Function 3 ~ 6&gt;.
- ■ Functions related to editing user-defined pages: &lt;Function 7 ~ 10&gt;.
- ■ Functions related to the serial interface: &lt;Function 11&gt; &lt;Function 12&gt;.

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U220

## TM-T20

This printer supports &lt;Function 1&gt;, &lt;Function 2&gt;, and the following functions:

- ■ Functions related to printer operational settings: &lt;Function 3 ~ 6 &gt;.
- ■ Functions related to the serial interface: &lt;Function 11&gt; &lt;Function 12&gt;.
- ■ Functions related to the USB interface: &lt;Function 15&gt; &lt;Function 16&gt;.
