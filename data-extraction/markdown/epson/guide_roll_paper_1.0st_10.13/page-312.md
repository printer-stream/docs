## C O N F I D E N T I A L

- k indicates the number of the definition data. k is an explanation parameter; therefore, it does not need to be transmitted.

## [Recommended Functions]

This command is supported only by some printer models and may not be supported by future models. It is recommended that downloaded graphics function (GS ( L GS 8 L: &lt;Function 52 &gt; and &lt;Function 80 &gt; ~ &lt;Function 85&gt;) be used because they offer the following additional features:

- Multiple number of logo data and mark data can be specified (except for some models).
- Data control by key code is possible.
- Redefining or deleting the same data is possible for each key code.
- Selecting a color for printing is possible.
- Defining data by raster format is possible.
- The remaining capacity of the definition area can be confirmed.
- ■ Data ( d ) specifies a bit printed to 1 and not printed to 0.
- ■ The downloaded bit image is not defined as the default.
- ■ Once a downloaded bit image has been defined, it is available until another definition is made, ESC @ is executed, the printer is reset, or the power is turned off.
- ■ On some models a downloaded bit image and a user-defined character cannot be defined simultaneously.
- When this command is executed, the user-defined character is cleared.
- When ESC &amp; is executed, the downloaded bit image data is cleared.
- ■ The downloaded bit image is printed by GS / .

## [Notes]
