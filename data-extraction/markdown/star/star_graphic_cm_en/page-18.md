<!-- image -->

Rev. 2.31

## 3-1-3) Status

## ESC RS a n

[Name]

Set status transmission conditions

[Code]

ASCII

ESC RS a n

Hex.

1B 1E 61 n

Decimal

27 30 97 n

[Defined Area]  0

≤ n ≤ 3, 48 ≤ n ≤ 51('0' ≤ n ≤ '3')

n=16,n=255

## [Initial Value] [Function]

Set by memory switches.

Sets the status transmission conditions.

See Appendix 1 for details regarding ASB status.

See each printer's product specifications manual for details on the memory switch settings.

| n     | Status transmission conditions                                                  |
|-------|---------------------------------------------------------------------------------|
| 0, 48 | ASB Invalid , NSB Invalid                                                       |
| 1, 49 | ASB Valid , NSB Invalid                                                         |
| 2, 50 | ASB Invalid , NSB Valid                                                         |
| 3, 51 | ASB Valid , NSB Valid                                                           |
| 16    | Returns theASB and NSB settings to the initial state previously set by the MSW. |
| 255   | Sends theASB status information.                                                |

## ESC ACK SOH

[Name]

Real-time printer status (ASB status)

[Code]

ASCII

ESC ACK  SOH

Hex.

1B 06 01

Decimal

27 6 1

[Defined Area] - - -

[Initial Value]

- - -

[Function]

Sends ASB status information to the host.

This command is not used when ASB is valid.

See Appendix 1, Automatic Status for details regarding ASB status.

--------------------------------------------------------------------------------------
