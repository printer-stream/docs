<!-- image -->

## &lt;Function 80&gt; ESC GS ) B pL pH fn m  (fn = 80)

[Name] Register text search settings and definitions in the non-volatile memory

[Code]

ASCII

ESC

GS

)

B

pL

pH

fn

m

Hexadecimal

1B

1D

29

42

pL

pH

fn

m

Decimal

27

29

41

66

pL

pH

fn

m

[Defined Area]

pL = 2, pH = 0

fn = 80

m = 0

[Initial Value]

---

[Function]

Registers the text search setting to non-volatile memory.

The following shows the contents to register.

| Function No.   | Contents                                                |
|----------------|---------------------------------------------------------|
| Function 48    | Enable and disables text search                         |
| Function 49    | Set the number of times to run the text search macro    |
| Function 50    | Set to print the string that matches in the text search |
| Function 64    | Define the text search string                           |
| Function 65    | Define the text search macro                            |
| Function 81    | Initialize text search settings and definitions         |

After registration ends, resets the printer.

The printer operates by reading the setting registered using this command the next time the printer power is turned on.

This command is ignored when the text search macro is running.

Consider the life of the non-volatile memory and avoid over-sue of this command.

Disabled in Page Mode.

## &lt;Function 81&gt; ESC GS ) B pL pH fn m  (fn = 81)

[Name] Initialize text search settings and definitions

[Code]

ASCII

ESC GS ) B pL pH fn m

Hexadecimal

1B 1D 29 42 pL pH fn m

Decimal

27 29 41 66 pL pH fn m

[Defined Area]

pL = 2, pH = 0

fn = 81

m = 0

[Initial Value]

---

[Function]

Initialize text search settings and definitions

The following shows the contents to initialize.

| Function No.   | Contents                                                | Initial Value                    |
|----------------|---------------------------------------------------------|----------------------------------|
| Function 48    | Enable and disables text search                         | Invalid                          |
| Function 49    | Set the number of times to run the text search macro    | 1 times                          |
| Function 50    | Set to print the string that matches in the text search | Prints the string                |
| Function 64    | Define the text search string                           | No text search string definition |
| Function 65    | Define the text search macro                            | No text search macro definition  |

This setting is applied to printer operations when this command is processed.

This setting is registered to non-volatile memory by the ESC GS ) B &lt;Function 80) command.

This command is ignored when the text search macro is running.

Disabled in Page Mode.

-----------------------------------------------------------------------------
