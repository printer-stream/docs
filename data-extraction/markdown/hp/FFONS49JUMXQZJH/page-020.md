2. Decimal Format -a number between -128.0000 and 1279999 with an optional decimal point and decimal fraction with up to four significant digits. If no sign is specified, the parameter is assumed to be positive.
3. Label Fields -any combination of text, numeric expressions, or string variables. Refer to The Label Instruction, LB, Chapter 5, for a complete description.

Some instructions such as PA, PR, PU, and PD may have multiple parameters. Separators are required between these parameters. These optional parameters are shown in parentheses in the syntax descriptions.

The syntax shown under the description of each HP-GL instruction uses the following notations:

| MNemonic            | For readability, the mnemonic is shown upper­ case and separated from the parameters and/ or terminator.                          |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| necessary parameter | All typeset items are required parameters.                                                                                        |
| ( )                 | All items in parentheses are optional.                                                                                            |
| C....C              | Any number oflabeling characters.                                                                                                 |
| (,.-)               | Any number of X,Ycoordinate pairs.                                                                                                |
| terminator          | ; or any nonnumeric or nonalphabetic character such as $ or #, or the next mnemonic. LF is also valid for HP-IBand HP-ILplotters. |
| (terminator)        | Terminator for an instruction which will execute after the last necessary parameter is received.                                  |

The following table shows the 7470'sHP-GL instruction set.

## Plotter Instruction Set

| Instruction             | Instruction                                                                                            | Description                                                                                                                               |
|-------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| AA AR CA CI CP CS DC DF | X,Y,arc angle (, chord angle) X,Y, arc angle (, chord angle) 11 radius (, chord angle) spaces, lines m | Arc absolute* Arc re1ative* Designate alternate set 11 Circle* Character plot Designate standard set In Digitize clear Set default values |
