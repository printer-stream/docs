At the end of the line, send the CR and LF commands. Move the horizontal print position as necessary. Then send the ESC * command for the next line of graphics.

## Note:

- Since the vertical dot density during 8-dot mode is different for 9 and 24/48pin printers, printed graphics will differ slightly (graphics on 9-pin printers will appear slightly compressed vertically).
- You must send the ESC * command for each line of graphics.

## Mixing text and bit-image graphics with ESC/P 2 printers

<!-- image -->

ESC/P 2 printers can process more than one line of data at a time; this allows for advanced features such as scalable fonts and raster graphics.

More memory has been provided for processing data than previous ESC/P versions. By processing data within this memory before printing, mixing bitimage graphics and text of all point sizes is possible.

To provide the most efficient processing of data in the memory available, ESC/P 2 has the following rules:

- You cannot move the vertical print position more than 179/360 inch (one dot less than 1/2 inch) in the negative direction.
- You cannot move the vertical print position in the negative direction if you have just sent graphics data, or if the print position would move above previously printed graphics data.

Because of these rules, you should process data with text data always leading graphics data by 1/2 inch.

Follow the steps below for this process.

1. Use the ESC + 48 command to set the line spacing to match the print head height.
2. Send the first 1/2 inch of text data to the printer. You can print any combination of fonts (large and small point sizes, etc.) on multiple lines; however, make sure the baseline of all characters is located within this 1/2inch.
3. Use the ESC ( V or ESC ( v commands to move the print position to the top of the 1/2-inch zone.
4. Use the ESC * command to send one line of graphics data (see the previous section). End the graphics line with the CR and LF commands. Note that the height of one line of graphics is equal to the height of the print head (48/360inch).
