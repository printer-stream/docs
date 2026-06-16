## C O N F I D E N T I A L

## Program example for ESC i and ESC m

## Program Example

```
PRINT #1,"    AAAAA"; PRINT #1,CHR$(&H1B);"d";CHR$(5); PRINT #1,CHR$(&H1B);"m"; ← Cut paper PRINT #1,"    BBBBB"; PRINT #1,CHR$(&H1B);"d";CHR$(5); PRINT #1,CHR$(&H1B);"m"; ← Cut paper
```

## TM-T20 , TM-T88IV , TM-T88V

The distance from print head to autocutter is about 15 mm {0.59 inch}.

After executing a paper cut, a paper feed for 1 mm {14/360 inches} before starting the next printing can provide the best printing result without uneven paper feeding.

## TM-U220

Uneven pitch may occur with subsequent paper feed due to the operation of the autocutter. It is recommended to feed approximately 2.116 mm or more for printing the next line to prevent 'dot displacement after cutting.'

Since the TM-U220D is not equipped with an autocutter, this command is ignored by the TM-U220D .

The setting is partial cut (one point is left) when the printer is shipped.

The distance from print head to autocutter is about 27 mm {1.06 inches} in the TM-U220A and TM-U220B .

## Print Sample

AAAAA

ESC m leaves paper joined in three places.

ESC i leaves paper joined in one place.

BBBBB
