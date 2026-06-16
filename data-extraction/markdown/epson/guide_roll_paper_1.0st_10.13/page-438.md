## C O N F I D E N T I A L

## (*2) 'Battery remaining amount' is as indicated in the following table.

| Battery remaining amount   | Battery remaining amount   | Information                       |
|----------------------------|----------------------------|-----------------------------------|
| Hex                        | Decimal                    | Information                       |
| 30H                        | 48                         | Battery remaining amount: H level |
| 31H                        | 49                         | Battery remaining amount: Mlevel  |
| 32H                        | 50                         | Battery remaining amount: L level |
| 33H                        | 51                         | Battery remaining amount: S level |
| 34H                        | 52                         | Battery isn't installed           |

- When the battery remaining amount is 'L level,' we recommend replacing or charging the battery.
- When the battery remaining amount is 'S level,' the printer terminates printing and goes offline.

You can confirm the battery remaining amount by looking at the 'battery LED' (BAT). When memory switch [Msw 8-2] is On, this printer beeps when it enters the 'L level' or 'S level.' When the printer power is on:

| Battery       | AC adapter    | Battery LED (BAT.) status                       |
|---------------|---------------|-------------------------------------------------|
| Installed     | Not installed | OFF: Battery remaining amount: H level          |
| Installed     | Not installed | Blinking: Battery remaining amount: Mlevel      |
| Installed     | Not installed | ON: Battery remaining amount: L level or S (*1) |
| Installed     | Installed     | Always Off                                      |
| Not installed | Installed     | Always Off                                      |

(*1) When battery remaining amount is S level, the ERROR LED is On.
