<!-- image -->

Rev. 2.31

- USB -I/F related commands

| Classification   | Command   | Name                                  | Line mode   | Raster mode   |
|------------------|-----------|---------------------------------------|-------------|---------------|
| USB-I/F          | ESC##W    | Register/Initialize USB serial number | OK          | OK            |

## ● Print mode related commands

|                   | Command   | Name                         | Line mode   | Raster mode   |
|-------------------|-----------|------------------------------|-------------|---------------|
| Select print mode | ESC RS C  | Select print mode            | OK          | OK            |
| Select print mode | ESC RS S  | Select print startup setting | OK          | OK            |

- Print er information related commands

| Classification               | Command    | Name                               | Line mode   | Raster mode   |
|------------------------------|------------|------------------------------------|-------------|---------------|
| Register printer information | ESC GS ( S | Register/Clear printer information | OK          | OK            |
| Send printer information     | ESC GS ) I | Send printer information           | OK          | OK            |
|                              | ESC # *    | Inquire printer version            | OK          | OK            |

## ● Customer Display commands

| Classification    | Command    | Name                            | Line mode   | Raster mode   |
|-------------------|------------|---------------------------------|-------------|---------------|
| Select print mode | ESCGSB@    | Send data to a customer display | OK          | OK            |
| Select print mode | ESC RS B A | Status request                  | OK          | OK            |
| Select print mode | ESC GS B B | Customer display data request   | OK          | OK            |
| Select print mode | ESC GS B C | Buffer clear                    | OK          | OK            |

--------------------------------------------------------------------------------------
