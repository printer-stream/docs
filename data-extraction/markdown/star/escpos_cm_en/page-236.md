<!-- image -->

## ESC	GS	h	1	k	m	n

Name

Water mark function

Code

ASCII

ESC GS h 1 k m n

Hex. 1B 1D 68 31 k m n

Decimal 27 29 104 49 k m n

Defined Area

0 ≤ k ≤ 2 0 ≤ m ≤ 2 1 ≤ n

≤ 255

Initial Value

---

Function

Enables/disables water mark function.

|   k | Water Mark Function                                                                                                                          |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------|
|   0 | Disabled                                                                                                                                     |
|   1 | Enabled Prints 1 logo specified by n at position centered in horizontal and vertical directions.                                             |
|   2 | Enabled Repeatedly prints the logo specified by n from top edge of page to bottom edge of page at position centered in horizontal direction. |

To make the image appropriate for a water mark, set the logo data forming method to print as the water mark using this setting.

If it is not possible to the appropriate image using this setting, reregister the logo data registered as the water mark after forming it to the appropriate data.

|   m | Water Mark Data Forming Method                     |
|-----|----------------------------------------------------|
|   0 | Prints logo data specified by n as it is.          |
|   1 | Thins logo data specified by n 25% for printing.   |
|   2 | Thins logo data specified by n 12.5% for printing. |

Specify the registered logo as the water mark.

| n     | Logo Number                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------|
| 1-255 | Registered logo number If the specified logo number is not registered, the water mark will not be printed. |

## &lt;Water Mark Function&gt;

When the water mark function is enabled, the water mark is printed by a water mark printing trigger.

However, this function is executed on print data built-up within the image buffer length.

Water mark printing is ignored when there is print data beyond the length of the image buffer.

Water mark is ignored when in 2-color mode, page mode, when registering macros and when executing macros if printing is started by anything other than the following water mark triggers. This setting is not cleared by &lt;ESC&gt; @ or &lt;CAN&gt;.

## Water mark triggers

- Cut command:

&lt;GS&gt; V m n,&lt;GS&gt; V m

- BM detection command:

&lt;GS&gt; &lt;FF&gt;,&lt;FF&gt;,&lt;GS&gt; &lt;

- Print start command:

&lt;ESC&gt; &lt;GS&gt; g 0 m n

- 1) Register logo to logo number 1 when using water mark.
- 2) Water mark function enable:  &lt;ESC&gt; &lt;GS&gt; h 1 k m n (k=0x02,m=0x01,n=0x01)
- 3) Print data transmission:    Print data (Print length should be within image buffer length)
- 4) Trigger command transmission:  &lt;GS&gt; V m n (Cutter command is water mark print trigger.)

## Usage example
