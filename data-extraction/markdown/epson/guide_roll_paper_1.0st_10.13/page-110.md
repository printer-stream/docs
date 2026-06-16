## C O N F I D E N T I A L

- ■ The printer cannot underline the space set by HT , ESC $ , and ESC \ .

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-U230 , TM-U220

```
Program Example for all printers PRINT #1, CHR$(&H1B);"!";CHR$(0); "AA"; PRINT #1, CHR$(&H1B);"!";CHR$(8); "BB"; PRINT #1, CHR$(&H1B);"!";CHR$(16); "CC"; PRINT #1, CHR$(&H1B);"!";CHR$(24); "DD"; PRINT #1, CHR$(&H1B);"!";CHR$(32); "EE"; PRINT #1, CHR$(&H1B);"!";CHR$(40); "FF"; PRINT #1, CHR$(&H1B);"!";CHR$(48); "GG"; PRINT #1, CHR$(&H1B);"!";CHR$(56); "HH"; CHR$(&HA); PRINT #1, CHR$(&H1B);"!";CHR$(129); "AA"; PRINT #1, CHR$(&H1B);"!";CHR$(137); "BB"; PRINT #1, CHR$(&H1B);"!";CHR$(145); "CC"; PRINT #1, CHR$(&H1B);"!";CHR$(153); "DD"; PRINT #1, CHR$(&H1B);"!";CHR$(161); "EE"; PRINT #1, CHR$(&H1B);"!";CHR$(169); "FF"; PRINT #1, CHR$(&H1B);"!";CHR$(177); "GG"; PRINT #1, CHR$(&H1B);"!";CHR$(185); "HH"; CHR$(&HA);
```

```
Print Sample ← Font A ← Font B with underline
```

```
AA: Normal BB: Emphasized CC: Double-height DD: Emphasized + Double-height EE: Double-width FF: Emphasized + Double-width GG: Double-height + Double-width HH: Emphasized + Double-height + Double-width
```

## TM-J2000/J2100 , TM-T90 , TM-L90

```
[Other than Japanese Kanji model] Character configurations Bit 0: Font 1 = Font A (12 × 24) Font 2 = Font B (9 × 17) Each character's baseline is as follows: Font A (12 × 24): 21 dots from the top of a character. Font B (9 × 17): 16 dots from the top of a character. [Japanese model]
```
