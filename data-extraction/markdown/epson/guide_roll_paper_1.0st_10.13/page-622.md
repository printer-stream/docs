## C O N F I D E N T I A L

## GS ( k &lt;Function 181&gt;

```
[Name] QR Code: Print the symbol data in the symbol storage area [Format] ASCII GS ( k pL pH cn fn m Hex 1D 28 6B 03 00 31 51 m Decimal 29 40 107 3 0 49 81 m [Range] ( pL + pH × 256) = 3 ( pL = 3, pH = 0 ) cn = 49 fn = 81
```

```
m = 48
```

Encodes and prints the QR Code symbol data in the symbol storage area using the process of &lt;Function 180&gt;.

- ■ In standard mode, use this function when printer is 'at the beginning of a line,' or 'there is no data in the print buffer.'
- ■ The symbol size that exceeds the print area cannot be printed.
- ■ If there is any error described below in the data of the symbol storage area, it cannot be printed.
- There is no data (Function 180 is not processed).
- If the data of the symbol storage area is more than the data allowed by specified model and data compaction mode. (This case is an abnormal number of data.)
- The four data compaction modes are listed below (in order of compaction rate). Automatically selects best compaction mode by the data of the symbol storage area.
- Numerical mode
- Alphanumeric mode
- Kanji mode
- 8-Bit Byte Mode
- ■ The following data are added automatically by the encode processing.
- Position Detection Patterns
- Separators for Position Detection Patterns
- Timing Patterns

[Description] [Notes]
