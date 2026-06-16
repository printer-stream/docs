<!-- image -->

## GS	(	A	pL	pH	n	m

Name

Test print

Code

ASCII GS ( A pL pH n m

Hex. 1D 28 41 pL pH n m

Decimal 29 40 65 pL pH n m

Defined Region

$${pL+ (pH×256) } = 2 (pL = 2, pH = 0)$$

0 ≤ n ≤ 2, 48 ≤ n ≤ 50

1 ≤ m ≤ 3, 49 ≤ m ≤ 51

Function

Executes the specified test print.

- Specifies the parameter count following pL and pH in (pL + (pH x 256)) bytes.

- n specifies the paper to use in the test print shown in the tables below.

| n           | Paper Type               |
|-------------|--------------------------|
| 0, 48       | Basic sheet (paper roll) |
| 1, 49 2, 50 | Paper Roll               |

- m specifies the type of test print shown in the tables below.

| m     | Type of Test Print          |
|-------|-----------------------------|
| 1, 49 | Hex. Dump                   |
| 2, 50 | Printer Status (Self Print) |
| 3, 51 | Rolling Pattern Print       |

## Details

- This command is effective only when processed at the top of the line when standard mode is being used.
- When in page mode, this command is ignored.
- When processing this command while defining a macro, the macro definition is terminated and the command commences with processing.
- After the test print is completed, the printer executes a hardware reset.  Therefore, download characters and download bit images and macros are handled as being undefined and the reception buffer and print buffer are cleared.  The printer returns all settings to their default status.
- After the final test print, this executes a paper cut.
- After the command is processed, the printer enters a BUSY state.
