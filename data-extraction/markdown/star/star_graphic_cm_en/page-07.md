<!-- image -->

Rev. 2.31

## 2. COMMAND FUNCTION LIST

## ● Standard Commands

| Classification        | Command       | Name                                      | Line mode   | Raster mode   |
|-----------------------|---------------|-------------------------------------------|-------------|---------------|
| External device drive | ESC BEL       | Set pulse width for external device drive | OK          | OK            |
| External device drive | BEL           | External device 1 drive instruction       | OK          | OK            |
| External device drive | FS            | External device 1 drive instruction       | OK          | OK            |
| External device drive | SUB           | External device 2 drive instruction       | OK          | OK            |
| External device drive | EM            | External device 2 drive instruction       | OK          | OK            |
| External device drive | ESC GS BEL    | Ring buzzer                               | OK          | OK            |
| External device drive | ESC GS EM DC1 | Set external buzzer drive pulse condition | OK          | OK            |
| External device drive | ESC GS EM DC2 | Output External buzzer drive pulse        | OK          | OK            |
| Print settings        | ESC RSA       | Set print area                            | OK          | OK            |
| Print settings        | ESC RS d      | Set print density                         | OK          | OK            |
| Print settings        | ESC RS r      | Set printing speed                        | OK          | OK            |
| Print settings        | ESC GS c      | Set reduced printing                      | OK          | OK            |
| Status                | ESC RS a      | Set status transmission conditions        | OK          | OK            |
| Status                | ESCACK SOH    | Real-time printer status (ASB status)     | OK          | OK            |
| Status                | ETB           | Update ETB status                         | OK          | OK            |
| Status                | ESC RS E      | Clear ETB counter, ETB status             | OK          | OK            |
| Status                | ESC GS ETX    | Document start, Document end              | OK          | OK            |
| Other                 | ESC GS #      | Set memory switch                         | OK          | OK            |
| Other                 | ESC ?         | Reset printer                             | OK          | OK            |
| Other                 | ESC GS L DC1  | Set LED blink condition                   | OK          | OK            |
| Other                 | ESC GS L DC2  | LED blink                                 | OK          | OK            |

## ● Raster related commands

| Classification   | Command           | Name                                    | Line mode   | Raster mode   |
|------------------|-------------------|-----------------------------------------|-------------|---------------|
| Raster           | ESC * r R         | Initialize raster mode                  | OK          | OK            |
| Raster           | ESC * r A         | Enter raster mode                       | OK          | OK            |
| Raster           | ESC * r B         | Quit raster mode                        | No          | OK            |
| Raster           | ESC * r C         | Clear raster data                       | No          | OK            |
| Raster           | ESC * r D         | Drive drawer                            | No          | OK            |
| Raster           | ESC * r E         | Set EOT mode                            | No          | OK            |
| Raster           | ESC * r F         | Set FF mode                             | No          | OK            |
| Raster           | ESC * r P         | Set page length                         | No          | OK            |
| Raster           | ESC * r Q         | Set print quality                       | No          | OK            |
| Raster           | ESC * r m l       | Set left margin                         | No          | OK            |
| Raster           | ESC * r m r       | Set right margin                        | No          | OK            |
| Raster           | ESC * r t         | Set top margin                          | No          | OK            |
| Raster           | ESC * r K         | Set print color                         | No          | OK            |
| Raster           | b n1 n2 d1 ．．． dk | Transfer raster data (auto line feed)   | No          | OK            |
| Raster           | k n1 n2 d1 ．．． dk | Transfer raster data                    | No          | OK            |
| Raster           | ESC * r Y         | Position movement in vertical direction | No          | OK            |
| Raster           | ESC FF NUL        | Execute FF mode                         | No          | OK            |
| Raster           | ESC FF EOT        | Execute EOT mode                        | No          | OK            |
| Raster extension | ESC * r a         | Start block                             | OK          | OK            |
| Raster extension | ESC * r b         | End block                               | No          | OK            |
| Raster extension | ESC * r e         | Set EM mode                             | No          | OK            |
| Raster extension | ESC FF EM         | Execute EM mode                         | No          | OK            |
| Raster extension | ESC FF LF         | Execute LF mode                         | No          | OK            |

--------------------------------------------------------------------------------------
