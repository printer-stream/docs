## C O N F I D E N T I A L

## ESC S

[Name]

Select standard mode

[Format]

ASCII

ESC S

Hex

1B 53

Decimal

27 83

[Range]

None

[Default]

None

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

[Notes]

Switches from page mode to standard mode.

- ■ This command is enabled only in page mode. Page mode can be selected by ESC L .
- ■ When this command is executed, data in all the print areas is cleared, the print area set by ESC W returns to the default value, but the value set by ESC T is maintained.
- ■ The following commands switch the settings for standard mode because these commands can be set independently in standard mode and in page mode:
- ESC SP , ESC 2 , ESC 3 , ESC U, and FS S .
- ■ In standard mode, CAN , ESC FF , GS $ , GS Q and GS \ are ignored.
- ■ The settings of ESC T and ESC W , GS ( P do not affect printing in standard mode.
- ■ The printer selects page mode with ESC L .
- ■ Standard mode is selected as the default.

[Model-dependent variations]

None

EXECUTING COMMAND
