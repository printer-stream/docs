The P-mask value specifies which of the status-byteconditions will result in a logical 1 response to a parallel poll over the HP-IB interface.

| P-Mask Bit Value   | Status Bit Number   | Meaning                                                                                                 |
|--------------------|---------------------|---------------------------------------------------------------------------------------------------------|
| 1 2 4 8 16 32      | 0 1 2 3 4 5         | Pen down P1 or P2 changed Digitized point available Initialized Ready for data; pinch wheels down Error |

For example, a P-mask value of 48 specifies that only bits 4 and 5 (16 + 32) of the status byte can cause the plotter to respond to a parallel poll with a logical 1 on the appropriate data line.

The plotter, when set to default values or initialized, automatically sets the E-mask to 223, the S-mask to 0, and the P-mask to 0. An IM command without parameters or with invalid parameters also sets the masks to the default values 223,0,0.
