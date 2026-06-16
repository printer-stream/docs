## Error Status

There are t hree poss i ble error t ypes: a ut oma ti cally recoverable errors, recoverable errors, a n d un recoverable errors.

## Automatically Recoverable Errors

Pr inting i s n o lo ng er poss i ble whe n a ut oma ti cally recoverable errors occ u r. They ca n be recovered eas i ly, as descr i bed below.

| Error                        | Error description                                                       | Error LED flash code Approx. 160 ms   | Recovery measure                                            |
|------------------------------|-------------------------------------------------------------------------|---------------------------------------|-------------------------------------------------------------|
| Roll paper cover open error  | The roll paper cover was opened during printing.                        |                                       | Recovers automatically when the roll paper cover is closed. |
| Print head temperature error | A high temperature outside the head drive operating range was detected. |                                       | Recovers automatically when the print head cools.           |

## Recoverable Errors

Pr inting i s n o lo ng er poss i ble whe n recoverable errors occ u r. They ca n be recovered eas i ly by tu r ning t he power o n a g a in or se n d ing a n error recovery comma n d from t he dr i ver af t er el i m in a ting t he ca u se of t he error.

| Error            | Error description                   | Error LED flash code Approx. 160 ms   | Recovery measure                                                                                                                                       |
|------------------|-------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Autocutter error | Autocutter does not work correctly. | Approx.2.56 s                         | Remove the jammed paper or foreign matter in the printer, close the roll paper cover, send the error recover command, or turn the power on to recover. |

The error recovery command is valid only if a recoverable error (excluding automatically recoverable errors) occurs.

1
