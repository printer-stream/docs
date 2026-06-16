## C O N F I D E N T I A L

- ■ Power supply output (when a = 98)
- ■ Paper autocutting after closing the roll paper cover (when a = 100)
- ■ (ARP) Enabling/disabling reduction of excessive top margin (when a = 101)
- ■ ARP: Automatic Reduction of Paper
- ■ (ARP) Enabling/disabling reduction of excessive bottom margin (when a = 102)
- ■ (ARP) Reduction ratio of line spacing (when a = 103)

|   ( nL + nH × 256) | Power supply output   |        |        |
|--------------------|-----------------------|--------|--------|
|                  0 | Level 1               | Small  |        |
|                  1 | Level 2               | &#124; |        |
|                  2 | Level 3               | Large  | PS-180 |

|   ( nL + nH × 256) | Paper autocutting after closing the roll paper cover   |
|--------------------|--------------------------------------------------------|
|                  0 | Disabled                                               |
|                  1 | Enabled                                                |

|   ( nL + nH × 256) | Reduction of excessive top margine   |
|--------------------|--------------------------------------|
|                  0 | Disabled                             |
|                  1 | Enabled                              |

|   ( nL + nH × 256) | Reduction of excessive bottom margin   |
|--------------------|----------------------------------------|
|                  0 | Disabled                               |
|                  1 | Enabled                                |

|   ( nL + nH × 256) | Reduction ratio of line spacing   |
|--------------------|-----------------------------------|
|                  0 | None                              |
|                  1 | 25% reduction                     |
|                  2 | 50% reduction                     |
|                  3 | 75% reduction                     |
