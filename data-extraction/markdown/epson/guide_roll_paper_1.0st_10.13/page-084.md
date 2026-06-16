## C O N F I D E N T I A L

[Model-dependent variations]

## TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-U230 , TM-U220

## Program Example (Line thermal)

```
PRINT #1, "AAAAA";CHR$(&HD); PRINT #1, "     BBBBB";CHR$(&HA);
```

## Program Example (Serial dot head)

```
PRINT #1, "AAAAA";CHR$(&HD); PRINT #1, "     BBBBB";CHR$(&HA);
```

## TM-J2000/J2100

Auto line feed for a parallel interface is selected by Memory switch 1-5.

This printer has only a serial dot head.

## TM-T90

Auto line feed for a parallel interface is selected by Memory switch 1-5.

This printer has only a line thermal head.

## TM-T20

Auto line feed is selected by Memory switch 1-5.

This printer has only a line thermal head.

## TM-T88IV , TM-T88V , TM-T70

Auto line feed for a parallel interface is selected by DIP switch 1-1.

This printer has only a line thermal head.

## Print Sample (Line thermal)

```
AAAAA ← Auto line feed enabled BBBBB AAAAA     BBBBB ← Auto line feed disabled
```

## Print Sample (Serial dot head)

AAAAA

BBBBB

← Auto line feed enabled

AAAAABBBBB

← Auto line feed disabled
