<!-- image -->

## &lt;Function 64&gt; ESC GS ) B pL pH fn m k d1…dk (fn = 64)

[Name] Define the text search string

[Code]

ASCII

ESC GS ) B pL pH fn n m k d1 ... dk

Hexadecimal

1B

1D

29

42

pL

pH

fn

n

m

k

d1

...

dk

Decimal

27 29 41 66 pL pH fn n m k d1 ... dk

[Code]

ASCII

ESC GS ) B pL pH fn n m k d1 ... dk

Hexadecimal

1B

1D

29

42

pL

pH

fn

n

m

k

d1

...

dk

Decimal

27 29 41 66 pL pH fn n m k d1 ... dk

[Defined Area]

4 ≤ (pL + pH x 256) ≤ 65535  (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 255)

fn = 64

1 ≤ n ≤ 100

1 ≤ m ≤ 100

0 ≤ k ≤ 32

32 ≤ d ≤ 255

[Initial Value]

Depends on setting registered in the non-volatile memory (At the time of shipment: no string definition)

[Function]

Defines the text search string for number n.

If the text search string for number n is already defined, it is overwritten.

M specifies the text search macro number to run.

K specifies the size of the defined data in bytes.

D specifies the defined data.

When the parameter has an invalid value, no definition.

This definition is applied to printer operations when this command is processed.

This definition is registered to non-volatile memory by the ESC GS ) B &lt;Function 80) command.

This command is ignored when the text search macro is running.

Disabled in Page Mode.

## &lt;Function 65&gt; ESC GS ) B pL pH fn m k1 k2 d1…dk (fn = 65)

[Name]

Define the text search macro

[Code]

ASCII

ESC GS ) B pL pH fn m k1 k2 d1 ...  dk

Hexadecimal

1B 1D 29 42 pL pH fn m k1 k2 d1 ...  dk

Decimal

27 29 41 66 pL pH fn m k1 k2 d1 ...  dk

[Defined Area]

4 ≤ (pL + pH x 256) ≤ 65535  (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 255)

fn = 65

1 ≤ m ≤ 100

0 ≤ (k = k1 + k2 x 256) ≤ 7680  (0 ≤ k1 ≤ 255, 0 ≤ k2 ≤ 30)

(Size of defined area = 7,680 bytes)

0 ≤ d ≤ 255

## [Initial Value]

Depends on setting registered  in  the  non-volatile  memory  (At  the  time  of  shipment:  no  text search macro definition)

[Function]

Defines the text search macro for number m.

If the text search macro for number m is already defined, it is overwritten.

(k = k1 + k2 x 256) specifies the size of the defined data in bytes.

d specifies the defined data.

If the parameter has an invalid value, processing of this command ends at that point.

This definition is applied to printer operations when this command is processed.

This definition is registered to non-volatile memory by the ESC GS ) B &lt;Function 80) command.

This command is ignored when the text search macro is running.

Disabled in Page Mode.

-----------------------------------------------------------------------------
