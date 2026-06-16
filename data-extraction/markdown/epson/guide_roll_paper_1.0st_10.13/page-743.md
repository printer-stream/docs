## C O N F I D E N T I A L

- Print density is based on the setting (print density) when a = 5.
- ■ Buzzer function: Enabling/disabling optional external buzzer (when a = 119)
- Set to Enabled when connecting the optional external buzzer.
- Set to Disabled when not connecting the optional external buzzer or connecting a drawer.
- The optional external buzzer is connected to the DKD connector; therefore, a drawer cannot be used at the same time. Both signals of drawer kick-out connector pins 2 and 5 are used.
- ■ Buzzer function: Buzzer frequency (Error) (when a = 120) (optional external buzzer)
- This function applies to when an error occurs (unrecoverable errors, recoverable errors, automatic recovery) or when a paper-end occurs.

<!-- image -->

|   ( nL + nH × 256) | Enabling/disabling optional external buzzer   |
|--------------------|-----------------------------------------------|
|                  0 | Disabled                                      |
|                  1 | Enabled                                       |

<!-- image -->

|   ( nL + nH × 256) | Buzzer frequency (Error)   |
|--------------------|----------------------------|
|                  0 | No sound                   |
|                  1 | 1 time                     |
|              65535 | Continuous                 |
