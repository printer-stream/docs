## C O N F I D E N T I A L

- (*2)  Processing according to response (unsent data exists, identified by send data set 'Identification status')
- ■ Processing the codes except for ACK, NAK, and CAN performs the same processing as CAN .
- (*3)  Processing according to response (no unsent data, identified by send data set 'Identification status')

| Response code   | Process                              |
|-----------------|--------------------------------------|
| ACK             | Start send processing for next data. |
| NAK             | Resend previously sent data.         |
| CAN             | End processing for this command.     |

| Response code   | Process                          |
|-----------------|----------------------------------|
| ACK, CAN        | End processing for this command. |
| NAK             | Resend previously sent data.     |

## Program Example 1 (Write data for record $1)

PRINT #1, CHR$(&amp;H1D);"(C";CHR$(18);CHR$(0);CHR$(0);CHR$(1);CHR$(0);"$1";"EPSON ESC/POS"; ¬ ← &lt;Function 1&gt;

## Program Example 2 (Read data for record %5)

←

```
PRINT #1, CHR$(&H1D);"(C";CHR$(5);CHR$(0);CHR$(0);CHR$(2);CHR$(0);"%5"; ¬ *LOOP: GOSUB *RECEIVE ← "Header to NUL" is received and stored under ST$ (details omitted) PRINT #1,CHR$(6); ← Response code is sent PRINT MID$(ST$,4) ← Record (%5) data is displayed on CRT IF MID$(ST$,3,1)=CHR$(65) THEN *LOOP ← Check for any subsequent data
```

&lt;Function 2&gt;

## Program Example 3 (Read available memory capacity)

```
PRINT #1, CHR$(&H1D);"(C";CHR$(3);CHR$(0);CHR$(0);CHR$(4);CHR$(0); ← <Function 4> GOSUB *RECEIVE ← "Header to NUL" is received and stored under ST$ (details omitted) PRINT MID$(ST$,4) ← Available capacity is displayed on CRT
```
