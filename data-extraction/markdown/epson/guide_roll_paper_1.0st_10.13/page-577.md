## C O N F I D E N T I A L

- ■ The relationship between the defined data and a print result is as follows. Example: data of the definition of the user defined character (2 bytes in vertical × 16 dots in horizontal) is necessary. ( k = 32)

| d1   | d3   | d5   | ...   | d27   | d29   | d31   | MSB   |
|------|------|------|-------|-------|-------|-------|-------|
|      |      |      |       |       |       |       | LSB   |
| d2   |      | d6   | ...   | d28   | d30   | d32   | MSB   |
|      | d4   |      |       |       |       |       | LSB   |

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U230 , TM-U220

| Program Example                                                                                                                                                                                                                                                                                                                                                                                                               | Print Sample   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| PRINT #1, CHR$(&H1C);"C"; CHR$(0): ← Select JIS code system PRINT #1, CHR$(&H1C);"2"; PRINT #1, CHR$(&H77);CHR$(&H21); FOR k = 1 To 32 READ d: PRINT #1, CHR$(d); NEXT k PRINT #1, CHR$(&H1C);"&"; ← Specify Kanji mode PRINT #1, CHR$(&H77);CHR$(&H21); PRINT #1, CHR$(&H33);CHR$(&H30); PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA); PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA); PRINT #1, CHR$(&H1C);"."; ← Cancel Kanji mode |                |
| DATA &H00, &H00, &H00, &H00, &H01, &HE0, &H07, &HF0 DATA &H0F, &HF0, &H1F, &HF2, &H3F, &HE2, &H7F, &HFE DATA &H7F, &HFE, &H3F, &HE2, &H1F, &HF2, &H0F, &HF0 DATA &H07, &HF0, &H01, &HE0, &H00, &H00, &H00, &H00                                                                                                                                                                                                               |                |
