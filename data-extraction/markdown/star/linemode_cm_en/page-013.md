<!-- image -->

| Class              | Commands   | Name                                            |
|--------------------|------------|-------------------------------------------------|
| Chinese characters | ESC p      | Set to JIS Kanji character mode                 |
|                    | ESC q      | Cancel JIS Kanji character mode                 |
|                    | ESC $      | Set/cancel JIS Kanji character mode             |
|                    | ESC s      | Set two byte Kanji characters left/right spaces |
|                    | ESC t      | Set 1 byte Kanji characters left/right spaces   |
|                    | ESC r      | Register Chinese download characters            |
| Others             | CAN        | Cancel print data and initialize commands       |
| Others             | ESC@       | Command initialization                          |
| Others             | ESC GS #   | Set memory switch                               |
| Others             | ESC ?      | Reset printer                                   |
| Others             | ESC GS r   | Get CRC code                                    |
| Macro              | ESC GS +   | Register macro                                  |

## (*)  Kanji character commands

-  Kanji character control commands are ignored on printers not installed with Kanji character fonts (those intended for overseas).
-  All Kanji character control commands are ignored if the specification for the location of use is specified as SBCS (single byte countries) by the memory switch.

## · Raster related commands

| Class           | Commands        | Name                                                                  |
|-----------------|-----------------|-----------------------------------------------------------------------|
| Raster commands | ESC * r R       | Initialize raster mode                                                |
|                 | ESC * r A       | Enter raster mode                                                     |
|                 | ESC * r B       | Quit raster mode                                                      |
|                 | ESC * r C       | Clear raster data                                                     |
|                 | ESC * r D       | Drive drawer                                                          |
|                 | ESC * r E       | Set EOT mode                                                          |
|                 | ESC * r F       | Set FF mode                                                           |
|                 | ESC * r P       | Set page length                                                       |
|                 | ESC * r Q       | Set print quality                                                     |
|                 | ESC * r m l     | Set left margin                                                       |
|                 | ESC * r m r     | Set right margin                                                      |
|                 | ESC * r T       | Set top margin                                                        |
|                 | ESC * r K       | Set print color                                                       |
|                 | b n1 n2 d1...dk | Transfer raster data (auto line feed)                                 |
|                 | k n1 n2 d1...dk | Transfer raster data                                                  |
|                 | ESC * r Y       | Position movement in vertical direction (Line break at specified dot) |
|                 | ESC FF NUL      | Execute form feed mode                                                |
|                 | ESC FF EOT      | Execute EOT mode                                                      |
|                 | ESC * r N       | Discard data for specified byte count                                 |
|                 | ESC * r V       | Execute external buzzer drive                                         |
|                 | ESC * r e s NUL | Set print data cancel function                                        |
|                 | ESC * r S       | Playback NV audio                                                     |
|                 | ESC * r s 0     | Set NV audio playback number                                          |
|                 | ESC * r s 1     | Set NV audio playback count                                           |
|                 | ESC * r s 2     | Set NV audio playback delay time                                      |
|                 | ESC * r s 3     | Set NV audio playback interval                                        |

-----------------------------------------------------------------------------
