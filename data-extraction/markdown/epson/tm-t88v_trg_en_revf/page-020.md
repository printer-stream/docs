## Error Status

There are three possible error types: automatically recoverable errors, recoverable errors, and unrecoverable errors.

## Automatically Recoverable Errors

Printing is no longer possible when automatically recoverable errors occur. They can be recovered easily, as described below.

| Error                        | Error description                                                       | Error LED flash code          | Recovery measure                                            |
|------------------------------|-------------------------------------------------------------------------|-------------------------------|-------------------------------------------------------------|
| Roll paper cover open error  | The roll paper cover was opened during printing.                        | LED ON LED OFF Approx. 160 ms | Recovers automatically when the roll paper cover is closed. |
| Print head temperature error | A high temperature outside the head drive operating range was detected. | LED ON LED OFF Approx. 160 ms | Recovers automatically when the print head cools.           |

## Recoverable Errors

Printing is no longer possible when recoverable errors occur. They can be recovered easily by turning the power on again or sending an error recovery command from the driver after eliminating the cause of the error.

| Error            | Error description                   | Error LED flash code                          | Recovery measure                                                                                                                                        |
|------------------|-------------------------------------|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Autocutter error | Autocutter does not work correctly. | LED ON LED OFF Approx. 160 ms Approx. 2560 ms | Remove the jammed paper or foreign matter in the printer, close the roll paper cover, send the error recovery command, or turn the power on to recover. |

The error recovery command is valid only if a recoverable error (excluding automatically

recoverable errors) occurs.
