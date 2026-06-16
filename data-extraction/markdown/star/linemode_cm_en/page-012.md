<!-- image -->

| Class                         | Commands      | Name                                                              |
|-------------------------------|---------------|-------------------------------------------------------------------|
| Page control commands         | FF            | Form feed                                                         |
| Page control commands         | ESC C         | Set page length to n lines                                        |
| Page control commands         | ESC C 0       | Set page length in 24 mm units                                    |
| Page control commands         | VT            | Feed paper to vertical tab position                               |
| Page control commands         | ESC B         | Set vertical tab position                                         |
| Page control commands         | ESC N         | Set bottom margin to n lines                                      |
| Page control commands         | ESC O         | Cancel bottom margin                                              |
| Horizontal direction position | ESC l         | Set left margin                                                   |
| Horizontal direction position | ESC Q         | Set right margin                                                  |
| Horizontal direction position | HT            | Move print position to horizontal tab position                    |
| Horizontal direction position | ESC D         | Set/cancel horizontal tab position                                |
| Horizontal direction position | ESC GSA       | Move absolute position                                            |
| Horizontal direction position | ESC GS R      | Move relative position                                            |
| Horizontal direction position | ESC GS a      | Specify position alignment                                        |
| Download                      | ESC &         | Register/delete 12 x 24 dot font download characters              |
| Download                      | ESC%          | Set/cancel download characters                                    |
| Bit image graphics            | ESC K         | Standard density bit image                                        |
| Bit image graphics            | ESC L         | High density bit image                                            |
| Bit image graphics            | ESC k         | Fine bit image                                                    |
| Bit image graphics            | ESC X         | Fine bit image                                                    |
| Logos                         | ESC FS q      | Register logo data                                                |
| Logos                         | ESC FS p      | Print logo data                                                   |
| Logos                         | ESC RS L      | Print registered logo in batch/ Batch control of registered logos |
| Bar code                      | ESC b         | Print bar code                                                    |
| Cutter control                | ESC d         | Paper cutter instruction                                          |
| External device Drive         | ESC BEL       | Set pulse width for external device drive                         |
| External device Drive         | BEL           | External device 1 drive instruction                               |
| External device Drive         | FS            | External device 1 drive instruction                               |
| External device Drive         | SUB           | External device 2 drive instruction                               |
| External device Drive         | EM            | External device 2 drive instruction                               |
| External device Drive         | ESC GS BEL    | Ring buzzer                                                       |
| External device Drive         | ESC GS EM DC1 | External buzzer drive pulse condition settings                    |
| External device Drive         | ESC GS EM DC2 | External buzzer drive execution                                   |
| Print settings                | ESC RS d      | Set print density                                                 |
| Print settings                | ESC RS r      | Set printing speed                                                |
| Status                        | ESC RS a      | Set status transmission conditions                                |
| Status                        | ESC ACK SOH   | Real-time printer status (ASB Status)                             |
| Status                        | ENQ           | Real-time printer status (1)                                      |
| Status                        | EOT           | Real-time printer status (2)                                      |
| Status                        | ESC ACK CAN   | Real-time printer reset                                           |
| Status                        | ETB           | Update ETB status                                                 |
| Status                        | ESC RS E      | Clear ETB counter, ETB status                                     |
| Status                        | ESC GS ETX    | Send print end counter and initialize                             |
| Status                        |               | Print data cancel function                                        |

-----------------------------------------------------------------------------
