<!-- image -->

## 3.8.  Presenter Related Command Details

The following commands control the presenter functions.

The following commands are effective only on models equipped with a presenter.

## ESC SYN 0 n

[Name]

Execute presenter paper recovery

[Code]

ASCII ESC  SYN 0 n

Hex.

1B 16 30 n

Decimal

27 22 48 n

[Defined Area]

n = 0, n = 48 ('0')

[Initial Value]

- - -

[Function]

Executes presenter paper recovery.

This command is ignored when a presenter is not connected.

Also, this command is executed when paper is supplied by the presenter, exists in the presenter and the paper has been cut.   This command is ignored with under all other conditions.   (Ignored when paper is being recovered.)

## ESC SYN 1 n

[Name] Set presenter paper automatic recovery function and automatic recovery time

[Code]

ASCII ESC  SYN 1 n

Hex.

1B 16 31 n

Decimal 27 22 49 n

[Defined Area]

0 ≤ n ≤ 255

[Initial Value]

Memory switch setting

[Function]

Sets presenter paper automatic recovery function and automatic recovery time.

This command is ignored when a presenter is not connected.

Settings using this command are effective from the next sheet when the printer processes this command and paper has already been supplied to the presenter.

| N           | Functions                                                                                            |
|-------------|------------------------------------------------------------------------------------------------------|
| n = 0       | Paper automatic recovery function invalid.                                                           |
| 1 ≤ n ≤ 255 | Paper automatic recovery function valid. Automatic recovery time: n x 0.5 sec (0.5 sec to 127.5 sec) |

-----------------------------------------------------------------------------
