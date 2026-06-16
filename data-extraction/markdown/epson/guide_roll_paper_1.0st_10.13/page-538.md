## C O N F I D E N T I A L

## GS g 2

```
[Name] Transmit maintenance counter [Format] ASCII GS g 2 m nL nH Hex 1D 67 32 00 nL nH Decimal 29 103 50 0 nL nH [Printers not featuring this command] TM-U230 , TM-U220 [Range] m = 0 TM-J2000/J2100 : 30 ≤ ( nL + nH × 256) ≤ 34, ( nL + nH × 256) = 50, 70 158 ≤ ( nL + nH × 256) ≤ 162, ( nL + nH × 256) = 178, 198 TM-T90 , TM-T88IV , TM-T70 , TM-P60 : ( nL + nH × 256) = 20, 21, 50, 70 ( nL + nH × 256) = 148, 149, 178, 19 TM-T20 , TM-T88V : ( nL + nH × 256) = 20, 21, 22, 50, 70, 148, 149, 150, 178, 198 ( nL = 20, 21, 22, 50, 70, 148, 149, 150, 178, 198, nH = 0) TM-L90 : ( nL + nH × 256) = 20, 21, 70 [ TM-L90 with Peeler] ( nL + nH × 256) = 148, 149, 198 ( nL + nH × 256) = 20, 21, 50, 70 [ TM-L90 ( nL + nH × 256) = 148, 149, 178, 198
```

[Description]

EXECUTING COMMAND

```
models without Peeler]
```

Transmits the value of the maintenance counter specified by the number.

| ( nL + nH × 256)   | Type         | Maintenance counter                              |
|--------------------|--------------|--------------------------------------------------|
| 10~19              | Resettable   | Serial impact head                               |
| 20~29              | Resettable   | Thermal head                                     |
| 30~39              | Resettable   | Ink jet head                                     |
| 40~49              | Resettable   | Shuttle head                                     |
| 50~59              | Resettable   | Devices that conform to the normal specification |
| 60~69              | Resettable   | Option devices                                   |
| 70~79              | Resettable   | Time                                             |
| 138~147            | Accumulation | Serial impact head                               |
