<!-- image -->

## ESC FS q n [x11 x12 y11 y12 d1...dk]1...[xn1 xn2 yn1 yn2 d1...dk]n

```
[Name] Register logo [Code] ASCII ESC FS n  [x11 x12 y11 y12 d1 … dk]1 … [xn1  xn2  yn1  yn2 d1 ... dk]n q Hex. 1B 1C 71 n  [x11 x12 y11 y12 d1 … dk]1 … [xn1  xn2  yn1  yn2 d1 ... dk]n Decimal 27 28  113 n  [x11 x12 y11 y12 d1 … dk]1 … [xn1  xn2  yn1  yn2 d1 ... dk]n
```

[Defined Area]

1 ≤ n ≤ 255 0 ≤ xn1 ≤ 255,  0 ≤ xn2 ≤ 3 1 ≤ (xn1 + xn2 x 256) ≤ 1023 0 ≤ yn1 ≤ 255,  0 ≤ yn2 ≤ 1 1 ≤ yn1 + yn2 x 256) ≤ 288 0 ≤ d ≤ 255

k = {(xn1 + xn2 x 256) x (yn1 + yn2 x 256) x 8}

[Initial Value] [Function]

- - -

Parameter details

• n:

Specifies registered logo count

- xn1, xn2:

Horizontal size of registered logo {(xn1 + xn2 x 256) x 8} dots

- yn1, yn2:

Vertical size of registered logo {(yn1 + yn2 x 256) x 8} dots

- d:

Registered logo data

- k:

Logo data count

This command should be specified at the top of the line.

When the first parameter is determined to be free of error, the printer starts processing this command.

When logo register processing starts, all previously defined data is deleted.

(It is not possible to reregister a portion of a plurality of defined logo data.)

Logo registration numbers are defined in rising order from 1.

If the defined area specified by the parameter is not empty, or if there is an error in the parameter specification, register processing is aborted.  (The pre-registered and complete data is effective.) The printer should be initialized if logo registration is completed or register processing is aborted. If an error occurs while performing register processing (the time from when the first parameter is OK until th printer initialization is completed after registering a logo), error processing, mechanical operation and status processing cannot be performed.

The relationships between input data and the actual print are shown on the next page.

- &lt;When registering logos for 2 color printing&gt;

Registration is possible regardless of the 2 color printing mode being specified or cancelled.

Register logos with the same capacity as the logo register number n (odd number) and n + 1 (even number).

If the capacity differs or the logo register number is 255, this command is ignored by the logo print command in the 2 color print mode.

-----------------------------------------------------------------------------
