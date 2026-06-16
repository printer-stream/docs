| E-Mask Bit Value     | Bit             | Error Number    | Meaning                                                                                                                                                                    |
|----------------------|-----------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 2 4 8 16 32 64 128 | O 1 2 3 4 5 6 7 | 1 2 3 4 5 6 7 8 | Instruction not recognized Wrong number of parameters Bad parameter Not used Unknown character set Position overflow Not used , Vector or PD received with pinch wheels up |

The default E-mask value of 223 (128 + 64 + 16 + 8 + 4 + 2 + 1) will specify that all errors except error 6 will set the error bit in the status byte and turn on the ERROR LED whenever they occur. Error 6 will not set the error bit or turn on the ERROR LED if it occurs, since it is not included in the E-mask value. Errors 4 and 7 never occur so setting the E-mask to 151will set the same conditions as the default value 223.

The S-mask value specified is the sum of any of the bit values shown below. It determines when a service request message will be sent. When a bit of the status byte changes value, the status byte is ANDed with the S-maskin a bit-by-bit fashion to determine if bit 6 of the status byte is to be set and the service request message sent. The status of bit 6 changes as plotter conditions change, and is cleared or set as required.

| S-Mask Bit Value   | Status Bit Number   | Meaning                                                                                                                   |
|--------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------|
| 1 2 4 8 16 32 64   | 0 5 6               | Pen down P1 or P2 changed Digitized point available lnitialized Ready for data; pinch wheels down Error Not used Not used |
|                    | 1                   |                                                                                                                           |
|                    | 2                   |                                                                                                                           |
|                    | 3                   |                                                                                                                           |
|                    | 4                   |                                                                                                                           |
| 128                | 7                   |                                                                                                                           |

For example, an S-mask value of 4 specifies that when a digitized point is available, setting bit 2, the service request message will be sent. Setting other bits will not send the service request message.
