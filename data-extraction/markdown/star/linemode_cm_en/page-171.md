<!-- image -->

## ESC GS h 1 k m n

## [ N a m e ]

Water mark function

[Code]

ASCII

ESC GS h 1 k m n

Hex.

1B

1D

68

31

k

m

n

Decimal

27 29  104 49 k m N

[Defined Area]

0 ≤ k ≤ 2, 0 ≤ m ≤ 2, 1 ≤ n ≤ 255

[Initial Value]

---

[Function]

Sets the water mark function to be valid/invalid.

|   k | Water Mark Function                                                                                                   |
|-----|-----------------------------------------------------------------------------------------------------------------------|
|   0 | Invalid                                                                                                               |
|   1 | Valid Prints one specified logo at a position centered horizontally and vertically.                                   |
|   2 | Valid Repeats printing of the specified logo from the top edge to the bottom edge at positions centered horizontally. |

- To set to an appropriate image as the water mark using this setting, set the method for forming The logo data to be printed as the water mark.

If it is not possible to set an appropriate image with this setting, form the logo data registered as the water mark into the appropriate data and reregister it.

|   m | Water Mark Data Forming                            |
|-----|----------------------------------------------------|
|   0 | Prints the logo data specified by n as it is.      |
|   1 | Prints the logo data specified by n thinned 25%.   |
|   2 | Prints the logo data specified by n thinned 12.5%. |

- Specify the registered logo in the water mark.

| n        | Logo Number                                                                                                  |
|----------|--------------------------------------------------------------------------------------------------------------|
| 1 to 255 | Registered logo numbers. If the specified logo number is not registered, the water mark will not be printed. |

## &lt;Water Mark Function&gt;

When the water mark function is valid, the water mark is printed by its trigger.

However, this function is effective for print data that can be contained in the image buffer length.

Print data  beyond the image buffer length is unaffected by this function.

Printing that is started other than the water mark trigger ignores the water mark print.

When in 2-color printing, this function is ignored.

Water mark printing triggers

- Cutter command:

&lt;ESC&gt; d n

- FF command:

&lt;FF&gt;

- BM detection command:

&lt;ESC&gt; d n, &lt;FF&gt;

- Print start command:

&lt;ESC&gt; &lt;GS&gt; g 0 m n

- Raster mode:

When &lt;FF&gt; is executed.

Use example

- 1) Register logo to use as water mark in logo number 1.
- 2) Water mark function is enabled:
- 2) Print data transfer:
- 3) Trigger command transfer:

&lt;ESC&gt; &lt;GS&gt; h 1 k m n (k = 0x02, m = 0x01, n = 0x01)

Print data (Print length is less than length of image buffer.)

&lt;ESC&gt; d n (Cutter command is water mark printing trigger.)

-----------------------------------------------------------------------------
