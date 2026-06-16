## C O N F I D E N T I A L

## FS ( A

[Name]

Select Kanji character style(s)

[Printers not featuring this command] TM-T20 , TM-T88IV , TM-U230 , TM-U220

[Description]

Selects the multi-byte code character style.

- Function code fn specifies the function.
- pL , pH specifies ( pL + pH × 256) as the number of bytes after pH ( fn and [parameters] ). The [parameters] are described in each function.
- ■ This command is specified function by function code ( fn ). Operation details are different depending on function.
- ■ Settings of this command affect multilingual characters and user-defined characters.
- ■ Settings of this command are effective until it is redefined, ESC @ is executed, the printer is reset, or the power is turned off.

|   fn | Function No.   | Function name               |
|------|----------------|-----------------------------|
|   48 | Function 48    | Select Kanji character font |

| Program Example                                                                                                                                                                                                                                                                                                                                                                                            | Print Sample   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| PRINT #1, CHR$(&h1C);"C";CHR$(0); ← Select JIS code system PRINT #1, CHR$(&h1C);"&"; PRINT #1, CHR$(&h1C);"(A";CHR$(2);CHR$(0);CHR$(48);CHR$(48); ← <Function 48> PRINT #1, CHR$(&h34);CHR$(&h41);CHR$(&h3B);CHR$(&h7A);CHR$(&hA); PRINT #1, CHR$(&h1C);"(A";CHR$(2);CHR$(0);CHR$(48);CHR$(50); ← <Function 48> PRINT #1, CHR$(&h34);CHR$(&h41);CHR$(&h3B);CHR$(&h7A);CHR$(&hA); PRINT #1, CHR$(&h1C);"."; |                |

[Notes]

SETTING COMMAND
