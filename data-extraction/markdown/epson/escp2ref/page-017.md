## Format

<!-- formula-not-decoded -->

## Parameter range

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Function

Sets the page length in the specified number of units-previously defined with the ESC ( U command-according to the following formula:

(page length) =((mH × 256) + mL) × (defined unit)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Default

Depends on default-setting mode or DIP-switch setting

## Notes

- This command is available only on printers featuring ESC/P 2.
- Set the page length before paper is loaded or when the print position is at the top-ofform position. Otherwise, the current print position becomes the top-of-form position (this results in undesirable contradictions between the actual and logical page settings).
- Setting the page length cancels the top and bottom-margin settings.
- Changing the defined unit does not affect the current page-length setting.

Printers not featuring this command

All non-ESC/P 2 printers

Model-dependent variations

None

## Related topics

ESC ( U, ESC ( c, ESC C, FF, LF, ESC N, Set the Print Area, Setting page length
