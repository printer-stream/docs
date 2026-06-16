## C O N F I D E N T I A L

## GS ( k &lt;Function 180&gt;

[Name] QR Code: Store the data in the symbol storage area [Format] ASCII GS ( k pL pH cn fn m d1...dk Hex 1D 28 6B pL pH 31 50 30 d1...dk Decimal 29 40 107 pL pH 49 80 48 d1...dk [Range] 4 ≤ ( pL + pH × 256) ≤ 7092 (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 27) cn = 49 fn = 80 m = 48 0 ≤ d ≤ 255 k = ( pL + pH × 256) - 3

[Description]

[Notes]

Stores the QR Code symbol data ( d1...dk ) in the symbol storage area.

- ■ The symbol data saved in the symbol storage area by this function is encoded by &lt;Function 081&gt; and &lt;Function 082&gt; of this command. After &lt;Function 081&gt; and &lt;Function 082&gt; are executed, the symbol data in the symbol storage area is kept.
- ■ k bytes of d1...dk are processed as symbol data.
- ■ It is possible to encode to a QR Code as follows. Be sure not to include anything except the following data in the data d1...dk .
- ■ Settings of this function are effective until the following processing is performed:
- Function 080 or 180 or 280 or 380 or 480 is executed
- ESC @ is executed

| Category of data       | Characters it is possible to specify              |
|------------------------|---------------------------------------------------|
| Numerical Mode data    | '0' ~ '9'                                         |
| Alphanumeric Mode data | '0' ~ '9', 'A' ~ 'Z', SP, $, %, *, +, -, . , /, : |
| Kanji Mode data        | Shift JIS value (Shift value from JISX0208)       |
| 8-Bit Byte Mode data   | 00H ~ FFH                                         |
