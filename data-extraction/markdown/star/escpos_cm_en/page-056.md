<!-- image -->

## ESC @

| Name     | Initialize printer                                                                    |
|----------|---------------------------------------------------------------------------------------|
| Code     | ASCII ESC @                                                                           |
|          | Hex. 1B 40                                                                            |
|          | Decimal 27 64                                                                         |
| Function | Clears data from the print buffer and sets the printer to its default settings.       |
| Details  | • DIP switch settings are not reload.                                                 |
|          | • Data in the reception buffer is maintained.                                         |
|          | • Macro definition information is maintained.                                         |
|          | •NV bit image definition information is maintained.                                   |
|          | • User NV memory data is maintained.                                                  |
|          | •When page mode is selected, this recovers to standard mode.                          |
| STAR     | The printer is initialized by this command under the following conditions.            |
|          | • Selection of an effective paper out detector for paper out signal output (ESC c 3n) |
|          | • Select an effective paper out detector for printing stop (ESC c 4n)                 |
