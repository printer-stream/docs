<!-- image -->

- Executes a paper feed for the height of the bar code (including HRI characters when HRI character printing is specified) regardless of the line feed amount using the following commands.
- This is valid only when there is no data in the print buffer. When there is data in the print buffer, it is received by the counter and then discarded.
- Sets the next print position to the beginning of the next line after printing the bar code.
- Print mode (enhanced printing, duplex printing, underlines, character size, 90˚ rotation) is unaffected, except upside-down printing.

- a. ESC 2:   Set default line spacing

- b. ESC 3:   Set line feed amount

## When in page mode:

- Only the bar code is deployed. Printing is not executed. After deploying the bar code, the next dot of the final bar code data becomes the start position for the next data deployment.
- When d exceeds the region, command processing is stopped, and data is received for the counter and discarded.

The data deployment start position is not moved at this point.

- When the width of the bar code exceeds the print area for one line, the data deployment start position for bar code printing is moved to the left beyond the print area and printing is not executed.
- &lt;When using CODE 93 bar code (m = 72)&gt;
- Prints an HRI character (□) of the start characters at the top of the HRI character string.
- Prints an HRI character (□) of the end characters at the top of the HRI character string.
- Prints HRI characters of the control characters (00H to 1FH and 7FH) combining (■) and one letter of the alphabet.

| Control Characters   | Control Characters   | Control Characters   | HRI Characters   | Control Characters   | Control Characters   | Control Characters   | HRI Characters   |
|----------------------|----------------------|----------------------|------------------|----------------------|----------------------|----------------------|------------------|
| ASCII                | Hex.                 | Decimal              | HRI Characters   | ASCII                | Hex.                 | Decimal              | HRI Characters   |
| NUL                  | 00                   | 0                    | ■U               | DLE                  | 10                   | 16                   | ■P               |
| SOH                  | 01                   | 1                    | ■A               | DC1                  | 11                   | 17                   | ■Q               |
| STX                  | 02                   | 2                    | ■B               | DC2                  | 12                   | 18                   | ■R               |
| ETX                  | 03                   | 3                    | ■C               | DC3                  | 13                   | 19                   | ■S               |
| EOT                  | 04                   | 4                    | ■D               | DC4                  | 14                   | 20                   | ■T               |
| ENQ                  | 05                   | 5                    | ■E               | NAK                  | 15                   | 21                   | ■U               |
| ACK                  | 06                   | 6                    | ■F               | SYN                  | 16                   | 22                   | ■V               |
| BEL                  | 07                   | 7                    | ■G               | ETB                  | 17                   | 23                   | ■W               |
| BS                   | 08                   | 8                    | ■H               | CAN                  | 18                   | 24                   | ■X               |
| HT                   | 09                   | 9                    | ■I               | EM                   | 19                   | 25                   | ■Y               |
| LF                   | 0A                   | 10                   | ■J               | SUB                  | 1A                   | 26                   | ■Z               |
| VT                   | 0B                   | 11                   | ■K               | ESC                  | 1B                   | 27                   | ■A               |
| FF                   | 0C                   | 12                   | ■L               | FS                   | 1C                   | 28                   | ■B               |
| CR                   | 0D                   | 13                   | ■M               | GS                   | 1D                   | 29                   | ■C               |
| SO                   | 0E                   | 14                   | ■N               | RS                   | 1E                   | 30                   | ■D               |
| SI                   | 0F                   | 15                   | ■O               | US                   | 1F                   | 31                   | ■E               |
|                      |                      |                      |                  | DEL                  | 7F                   | 127                  | ■T               |
