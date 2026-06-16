<!-- image -->

[TERM]

The response is the decimal equivalent of a 16-bitimme­ diate status word, followed by the output terminator. The maximum value output is 40.

The extended status word bits are as defined in the following table.

| Bit   | State   | Decimal Value   | Meaning                                                             |
|-------|---------|-----------------|---------------------------------------------------------------------|
| 0-2   | 0       | 0               | Not used, always zeros. Re­ served for plotters with paper advance. |
| 3     | 0 1     | 0 8             | Buffer is not empty. Buffer is empty and ready for data.            |
| 4, 5  | 00      | 0               | Ready to process or process­ ing HP-GLinstructions.                 |
|       | 01      | 16              | Paper loaded, VIEWbutton pressed so graphics sus­ pended.           |
|       | 10      | 32              | Paper lever raised so graph­ ics suspended.                         |

Combinations of these bits allow five different responses to the ESC . O instruction.

|   Response | Meaning                                                                     |
|------------|-----------------------------------------------------------------------------|
|          0 | Buffer is not empty and plotter is process­ ing HP-GLinstructions.          |
|          8 | Buffer is empty and is ready to process or is processing HP-GLinstructions. |
|         16 | Buffer is not empty and VIEW has been pressed.                              |
|         24 | Buffer is empty and VIEWhas been pressed.                                   |
|         32 | Buffer is not empty and paper lever and pinch wheels are raised.            |
|         40 | Buffer is empty and paper lever and pinch wheels are raised.                |

The output terminator defaults to carriage return unless it is set by ESC . M.
