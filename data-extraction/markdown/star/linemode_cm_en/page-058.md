<!-- image -->

## ESC FS p n m

[Name] [Code]

Print logo

ASCII

ESC FS p n m

Hex.

1B 1C 70 n m

Decimal

27 28 112 n m

[Defined Area]

1 ≤ n ≤ 255 0 ≤ m ≤ 3 48 ≤ m ≤ 51 ('0' ≤ m ≤ '3')

[Initial Value] [Function]

- - -

Prints the logo of registration number n registered using the logo registration command (ESC FS q) according to the print mode m.

| m     | Logo print mode       |
|-------|-----------------------|
| 0, 48 | Normal mode           |
| 1, 49 | Double wide mode      |
| 2, 50 | Double high mode      |
| 3, 51 | Double high/wide mode |

If there is unprinted data in the line buffer, this command is executed after printing that data.

Therefore, it is not possible to print with other data in the same line (characters, bit images, bar codes).

Form feed obeys the vertical print size of the logo.

If the logo horizontal print size exceeds the horizontal print region, the portion exceeding the area is not printed.

Logos are printed according to the following command settings.

- Left margin (ESC I n)
- Right margin (ESC Q n)
- Position alignment (ESC GS a n)
- Absolute position movement (ESC GS A n1 n2)
- Relative position movement (ESC GS R n1 n2)
- Upside-down printing (SI)

Invalid in page mode.

## ESC RS L m

[Name]

Spec. A Print logo in batch

Spec. B Batch control of registered logos

[Code]

ASCII ESC RS L m

Hex.

1B 1E 4C m

Decimal 27 30 76 m

[Defined Area]

Spec. A

0 ≤ m ≤ 3  48 ≤ m ≤ 51 ('0' ≤ m ≤ '3')

Spec. B

0 ≤ m ≤ 3  48 ≤ m ≤ 51 ('0' ≤ m ≤ '3'),m=255

[Initial Value] [Function]

- - -

Spec. A Prints all registered logos according to a print mode specified by m. Executes a printer reset after printing.

Spec. B Controls logos as specified by the parameter m.

After execution, this resets the printer.

Invalid in page mode.

## Spec. A

| m     | Logo print mode       |
|-------|-----------------------|
| 0, 48 | Normal mode           |
| 1, 49 | Double wide mode      |
| 2, 50 | Double high mode      |
| 3, 51 | Double high/wide mode |

-----------------------------------------------------------------------------
