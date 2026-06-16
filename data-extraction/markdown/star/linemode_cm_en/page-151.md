<!-- image -->

## 3.14. Page Function Command Details

## ESC GS h 0 k m n

[ N a m e ]

180 degree turnover

[Code]

ASCII

ESC GS h 0 k m n

Hex.

1B 1D 68 30 k m n

Decimal

27 29  104 48 k m n

[Defined Area]

0 ≤ k ≤ 1, m = 0, n = 0

[Initial Value]

[Function]

---

Sets 180 degree turnover function to be valid/invalid.

|   n | 180 Degree Turnover Function   |
|-----|--------------------------------|
|   0 | Invalid                        |
|   1 | Valid                          |

## &lt;180 Degree Turnover Function&gt;

When set to the 180 degree turnover function, that function is executed at the trigger.

However, this function is effective for print data that can be contained in the image buffer length. Print data beyond the image buffer length is unaffected by this function.

Printing that is started other than the 180 degree turnover trigger ignores this function.

- 180 degree turnover triggers

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

- 1) When 180 degree turnover function is enabled:

n = 0x00)

- 2) Print data transfer:
- 3) Trigger command transfer:

&lt;ESC&gt; &lt;GS&gt; h 0 k m n (k = 0x01, m = 0x00,

Print data (Print length is less than length of image buffer.)

&lt;ESC&gt; d n (Cutter command is 180 degree turnover trigger.)

-----------------------------------------------------------------------------
