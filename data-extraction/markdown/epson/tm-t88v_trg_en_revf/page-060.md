## For Ethernet/Wireless LAN/USB Interface

## DIP Switch Bank 1

| SW        | Function                | ON             | OFF             | Default setting   |
|-----------|-------------------------|----------------|-----------------|-------------------|
| 1-1       | Auto line feed          | Always enabled | Always disabled | OFF               |
| 1-2       | Receive buffer capacity | 45 bytes       | 4 KB            | OFF               |
| 1-3 ∼ 1-8 | Undefined               | -              | -               | OFF               |

## DIP Switch Bank 2

| SW        | Function                                                                                                                     | ON                                                                                           | OFF                                                                                          | Default setting   |
|-----------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------|
| 2-1       | Handshaking (BUSY condition)                                                                                                 | Receive buffer full                                                                          | • Offline • Receive buffer full                                                              | OFF               |
| 2-2       | Reserved (Do not change setting)                                                                                             | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-3 ∼ 2-4 | Selects print density                                                                                                        | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | OFF               |
| 2-5       | Sets the release condition of the receive buffer BUSY state. (This function is effective when DIP Switch 1-2 is set to off.) | Releases the BUSY state when the remaining capacity of the receive buffer reaches 138 bytes. | Releases the BUSY state when the remaining capacity of the receive buffer reaches 256 bytes. | OFF               |
| 2-6 ∼ 2-7 | Reserved (Do not change settings)                                                                                            | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-8       | Reserved (Do not change setting)                                                                                             | Fixed to ON                                                                                  | Fixed to ON                                                                                  | ON                |

<!-- image -->

For DIP Switch 2-1 (BUSY condition), see also "Selecting the BUSY Status" on page 62.
