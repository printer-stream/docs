<!-- image -->

## 1-1-6 Precautions	When	Switching	the	BUSY	Conditions

DIPSW Settings: Conditions for BUSY

ON

=

Reception buffer full or printer is offline (Default)

OFF  =  Reception buffer full

To set the busy conditions to reception buffer full (OFF), operators should be aware of the following points.

- Printing will stop but the printer will not enter a BUSY state when printing stops because of an error, the cover is open, paper is out when printing stops are enabled, or when paper feeds are executed using the paper feed switch.
- When using DLE EOT, DLE ENQ and DLE DC4, the reception buffer does not enter a buffer full status.
- Precautions on the host which cannot receive data transmissions when the printer is BUSY   DLEEOT, DLEENQ and DLEDC4 cannot be used when an error occurs when the printer has entered a BUSY state because the reception buffer is full.
- Precautions on the host which can receive data transmissions when the printer is BUSY DLEEOT, DLEENQ and DLEDC4 are handled as bit image data when using the DLEEOT, DLEENQ and DLEDC4 partway through the bit image data when the reception buffer is full when transmitting bit image data. Also, it is possible to lose data when received while the reception buffer is full.
