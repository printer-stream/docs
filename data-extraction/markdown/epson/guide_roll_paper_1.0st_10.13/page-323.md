## C O N F I D E N T I A L

## [Recommended Functions]

This command is supported only by some printer models and may not be supported by future models.

It is recommended to use graphics function ( GS ( L GS 8 L : &lt;Function 50&gt; and &lt;Function 113&gt;). The graphics functions are better than GS Q 0 for the following reasons:

- Selecting a color for printing is possible.
- Selecting a size in dot units is possible.
- ■ In standard mode, this command is effective only when data is not in the print buffer and the printer is at the beginning of the line.
- ■ This command processes k bytes data of d1...dk as a bit image data. Image data ( d ) specifies a bit printed to 1 and not printed to 0.
- ■ If a variable vertical bit image that exceeds the print area for a line is specified, the excess image data is ignored.
- ■ The scales for width and height of NV bit images are specified by m . Therefore, in page mode with 90 ° or 270 ° clockwise-rotated NV bit image, the printer applies print area and dot density from [width: direction of paper feed, height: perpendicular to direction of paper feed].
- ■ Character size and all print modes such as emphasize, underline, 90 ° clockwise rotation, or upside-down, do not affect printing of a variable vertical size bit image data.
- ■ This command feeds paper for the amount needed for printing a variable vertical bit image regardless of the paper feed setting set by paper feed setting commands.
- ■ Do not use this command during macro execution because the command cannot be included in a macro.
- ■ After printing a variable vertical bit-image, normal data processing is started.
- The print position is set to the left of the print area. The printer is at the beginning of a line and data is not
- in the print buffer.

[Notes]
