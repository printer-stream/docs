<!-- image -->

## GS	V	m

Name

Cut paper

Code

ASCII GS V m

Hex.

1D 56 m

Decimal

29 86 m

Defined Region

m = 0,1,48,49

Function

Executes specified paper cut.

| m     | Function                                                                                                      |
|-------|---------------------------------------------------------------------------------------------------------------|
| 0, 48 | Full cut                                                                                                      |
| 1, 49 | Partial cut (one point uncut)                                                                                 |
| 2, 50 | Not Used                                                                                                      |
| 3, 51 | Not Used                                                                                                      |
| 65    | Feeds paper to (cutting position + [n x basic calculated pitch]) and performs a full cut                      |
| 66    | Feeds paper to (cutting position + [n x basic calculated pitch]) and performs a partial cut (one point uncut) |
| 67    | Not Used                                                                                                      |
| 68    | Not Used                                                                                                      |

## Details

STAR

- This command is effective only when processed at the top of the line when standard mode is being used.
- Cuts paper.
- The auto-cut function differs according to the model.  A partial cut is executed on those models that cannot perform a full cut.

A full cut is executed on those models that cannot perform a partial cut.  Refer to the product specifications manual for the specifications of the auto-cut function.

- Models that do not have the auto-cut function do not cut paper.  However, commands that accompany a paper feed of (cutting position + [n x basic calculated pitch]) (n = 65, 66), a paper feed of (tear bar position + [n x basic calculated pitch]) is executed.

Reference

ESC i, ESC m
