<!-- image -->

## Plotter Default Conditions

| Plotting mode                        | Absolute (PA)                                                        |
|--------------------------------------|----------------------------------------------------------------------|
| Relative character direction         | Horizontal (DR1,0)                                                   |
| Line type                            | Solid line                                                           |
| Line pattern length                  | 4%of the distance from P1 to P2                                      |
| Input window                         | Mechanical limits of plotter                                         |
| Relative character size              | (SR .75 , 1.5) width = 0.75% of (P2XVPix) height : 1.5%of (P2y- Ply) |
| Scale                                | Off                                                                  |
| Symbol mode                          | Off                                                                  |
| Tick length (on either side of axis) | 0.5%of (P2x -Plx) or (P2y - Ply)                                     |
| Standard character set               | Set 0                                                                |
| Alternate character set              | Set 0                                                                |
| Labelterminator                      | ETX (ASCII decimal equivalent 3)                                     |
| Character slant                      | 00                                                                   |
| Mask value                           | 223 , O,0                                                            |
| Digitize clear                       | On                                                                   |
| Pen velocity                         | 38.1cm/s (15in./s)                                                   |
| *Chord angle                         | Set to 5 degrees for AA, AR, and CI                                  |

P1 and P2 are changed only with the initialize command (IN). They are not affected by device clear and the default command (DF).

*Applicable only to RS-232-Cplotters that have the serial prefix number 2312A or higher.
