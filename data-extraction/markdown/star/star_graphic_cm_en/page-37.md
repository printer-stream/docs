<!-- image -->

Rev. 2.31

## ESC FF EM

[Name]

Execute EM mode

[Code]

ASCII

ESC FF EM

Hex

1B 0C 19

Decimal

27 12 25

[Defined Area]  ---

[Initial Value]

---

[Function]

Executes EM mode.

It runs the operation specified in EM mode setting command (ESC * r e n NUL).

If raster data exists in the image buffer for raster mode, EM mode is implemented after printing.

If raster data does not exist in the image buffer of raster mode, this command is executed.

(TSP100IIU) if the print paper length to be cut is less than 24mm, then empty feed is automatically added before cutting so that the printing paper length is 24mm.

## ESC FF LF

[Name]

Execute LF mode

[Code]

ASCII ESC FF LF

Hex

1B 0C 0A

Decimal 27 12

10

[Defined Area]  ---

[Initial Value]

---

[Function]

Executes LF mode.

Nothing operates at the time when this command is processed.

Then, when a certain period of time elapses without any data being received, it starts printing.

However,  if  there  is  no  non-printed  data  in  the  printer,  it  will  not  execute  a  line  break  or  operate FormFeed even if this command is received.

If the printer is command emulator mode, print out unprinted data and perform a line break.

If the printer is raster mode, printing will perform a FormFeed operation by the page length setting.

--------------------------------------------------------------------------------------
