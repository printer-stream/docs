## C O N F I D E N T I A L

- ■ When Kanji mode is selected, the printer processes a character code that corresponds to the first byte of Kanji code, and then processes a consecutive byte as the second byte of Kanji code. Therefore, when Kanji code is specified, an ASCII code character that corresponds to the first byte of Kanji code cannot be printed.
- ■ Kanji mode is selected at default.

## Program Example

```
PRINT #1, CHR$(&H1C);"C";CHR$(0); PRINT #1, CHR$(&H1C);"&"; PRINT #1, CHR$(&H34);CHR$(&H41);
```

PRINT #1, CHR$(&amp;H3B);CHR$(&amp;H7A); CHR$(&amp;HA);

←

Select JIS code system

- ← Specify Kanji mode

Print Sample
