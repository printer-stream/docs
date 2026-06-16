<!-- image -->

## 4-3-10 STAR	Original	Print	Starting	Trigger	Control	Commands

This command is for models equipped with an expansion control function for page control of line unit commands, by controlling the image buffer by page.

## ESC	GS	g	0	m	n

Name

Print starting trigger

Code

ASCII ESC GS g 0 m n

Hex. 1B 1D 67 30 m n

Decimal 27 29 103 48 m n

Defined Area

m = 0, n = 0

Initial Value

---

Function

Starts printing when there is unprinted data in the image buffer.

It is prohibited to send this command while in the raster mode.

## ESC	GS	g	1	m	n

Name

Print starting timer

Code

ASCII ESC GS g 1 m n

Hex. 1B 1D 67 31 m n

Decimal 27 29 103 49 m n

Defined Area

m = 0, 0 ≤ n ≤ 255

Initial Value

Depends on the model

Function

Sets the print starting timer specified at n x 10 msec.

The print starting timer starts measuring from the point where the print data reception stops, and measures up to the set print starting timer.

When the set print starting timer is reached, the printer starts printing if there is unprinted data in the image buffer.

It is prohibited to send this command while in the raster mode.

| n        | Operating Mode                       |
|----------|--------------------------------------|
| 0        | Print starting timer = initial value |
| 1 to 255 | Print starting timer n x 10 msec.    |
