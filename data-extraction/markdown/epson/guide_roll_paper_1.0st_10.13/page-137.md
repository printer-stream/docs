## C O N F I D E N T I A L

## ESC r

```
[Name] Select print color [Format] ASCII ESC  r n Hex 1B 72 n Decimal 27 114 n [Range] n = 0, 1, 48, 49 [Default] n = 0
```

[Printers not featuring this command] TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60

[Description]

[Notes]

Selects a print color, using n as follows:

| n     | Print color   |
|-------|---------------|
| 0, 48 | Black         |
| 1, 49 | Red           |

- ■ When standard mode is selected, this command is enabled only when processed at the beginning of the line.
- ■ When page mode is selected, the color setting is the same for all data collectively printed by FF or ESC FF .
- ■ This command is effective until ESC @ is executed, the printer is reset, or the power is turned off.
- ■ GS ( N and GS ( L are available to define two-color printing. It is recommended that the commands shown below be used with the models that feature these commands.

| Printing data       | Command <Function>                              |
|---------------------|-------------------------------------------------|
| Character           | GS ( N <Function48>                             |
| Background          | GS ( N <Function49>                             |
| Graphics            | GS ( L <Function50> <Function112> <Function113> |
| NV graphics         | GS ( L <Function67> <Function68> <Function69>   |
| Downloaded graphics | GS ( L <Function83> <Function84> <Function85>   |

SETTING COMMAND
