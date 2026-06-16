<!-- image -->

## 6-4 Appendix	4	Standard	Mode

EPSON has models that have 180 DPI and 203 DPI print heads.  STAR's print head is 203 DPI.  Therefore, when targeting models with the EPSON 180 DPI print head, it is necessary to correct the line spacing that will be caused by the difference in the head's print density.  Correction is done using the memory switches (Print dot count: ESC/ POS Compatible Mode/Max).  Setting the memory switches to ESC/POS compatible mode artificially makes the number of dot counts the same as an EPSON printer.  However, if the target model has a 203 DPI print head, cor -rection is unnecessary so memory switches for print dot settings are not equipped.

## 6-4-1 Printing	Region

## 1. TSP600/TSP700

## Print Region Initial Values

| Print Region Setting    | Printing Dot Count Setting   | Initial Value   | Initial Value   | Initial Value   |
|-------------------------|------------------------------|-----------------|-----------------|-----------------|
| (Memory Switch Setting) | (Memory Switch Setting)      | nL              | nH              | Print region    |
| 80mm                    | ESC/POS Compatible Mode      | 56              | 2               | 71mm            |
| 80mm                    | Max.                         | 128             | 2               | 80mm            |
| 72mm                    | ESC/POS Compatible Mode      | 0               | 2               | 64mm            |
| 72mm                    | Max.                         | 64              | 2               | 72mm            |
| 52.5mm                  | ESC/POS Compatible Mode      | 120             | 1               | 47mm            |
| 52.5mm                  | Max.                         | 164             | 1               | 52.5mm          |
| 50.8mm                  | ESC/POS Compatible Mode      | 104             | 1               | 45mm            |
| 50.8mm                  | Max.                         | 150             | 1               | 50.8mm          |

Basic calculated pitch initial value:  X=1/180 (inch), Y=1/360 (inch)

## 2 TSP800

## Print Region Initial Values

| Print Region Setting    | Initial Value   | Initial Value   | Initial Value   |
|-------------------------|-----------------|-----------------|-----------------|
| (Memory Switch Setting) | nL              | nH              | Print region    |
| 104mm                   | 64              | 3               | 104mm           |

Basic calculated pitch initial value:  X=1/180 (inch), Y=1/360 (inch)

## 3 TUP900

Print Region Initial Values

| Print Region Setting   | Initial Value   | Initial Value   | Initial Value   |
|------------------------|-----------------|-----------------|-----------------|
| (Memory Switch         | nL              | nH              | Print region    |
| 104mm                  | 64              | 3               | 104mm           |
| 80mm                   | 128             | 2               | 80mm            |
| 72mm                   | 64              | 2               | 72mm            |
| 56mm                   | 192             | 1               | 56mm            |

Basic calculated pitch initial value:  X=1/203 (inch), Y=1/203 (inch)
