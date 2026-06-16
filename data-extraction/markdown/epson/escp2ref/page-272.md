| ESC/P 2   | ESC/P   | 9-Pin ESC/P   |
|-----------|---------|---------------|

You can change up to 12 of the characters in the current character table with the ESC R command. These 12 characters are called international character sets because they correspond to characters commonly used in several foreign languages.

The format for this command is as follows:

ESC R n

The parameter n determines which character set is selected.

The table below shows these characters and their codes in the Helvetica typeface, as well as the value of the parameter used in the ESC R command to select each character set.

<!-- image -->

|   n | Set name     | Dec Hex   | 35 23   | 36 24   | 64 40   | 91 5B   | 92 5C   | 93 5D   | 94 5E   | 96 60   | 123 7B   | 124 7C   | 125 7D   | 126 7E   |
|-----|--------------|-----------|---------|---------|---------|---------|---------|---------|---------|---------|----------|----------|----------|----------|
|   0 | USA          |           | #       | $       | @       | [       | \       | ]       | ^       | `       | {        | &#124;   | }        | ~        |
|   1 | France       |           | #       | $       | à       | °       | ç       | §       | ^       | `       | é        | ù        | è        | ¨        |
|   2 | Germany      |           | #       | $       | §       | Ä       | Ö       | Ü       | ^       | `       | ä        | ö        | ü        | ß        |
|   3 | UK           |           | £       | $       | @       | [       | \       | ]       | ^       | `       | {        | &#124;   | }        | ~        |
|   4 | Denmark l    |           | #       | $       | @       | Æ       | Ø       | Å       | ^       | `       | æ        | ø        | å        | ~        |
|   5 | Sweden       |           | #       | ¤       | É       | Ä       | Ö       | Å       | Ü       | é       | ä        | ö        | å        | ü        |
|   6 | Italy        |           | #       | $       | @       | °       | \       | é       | ^       | ù       | à        | ò        | è        | ì        |
|   7 | Spain l      |           | Pt      | $       | @       | ¡       | Ñ       | ¿       | ^       | `       | ¨        | ñ        | }        | ~        |
|   8 | Japan ( Eng) |           | #       | $       | @       | [       | ¥       | ]       | ^       | `       | {        | &#124;   | }        | ~        |
|   9 | Norway       |           | #       | ¤       | É       | Æ       | Ø       | Å       | Ü       | é       | æ        | ø        | å        | ü        |
|  10 | Denmark ll   |           | #       | $       | É       | Æ       | Ø       | Å       | Ü       | é       | æ        | ø        | å        | ü        |
|  11 | Spain ll     |           | #       | $       | á       | ¡       | Ñ       | ¿       | é       | `       | í        | ñ        | ó        | ú        |
|  12 | Lat America  |           | #       | $       | á       | ¡       | Ñ       | ¿       | é       | ü       | í        | ñ        | ó        | ú        |
|  13 | Korea        |           | #       | $       | @       | [       | W       | ]       | ^       | `       | {        | &#124;   | }        | ~        |
|  64 | Legal        |           | #       | $       | §       | °       | '       | '       | ¶       | `       | ©        | ®        | †        | ™        |
