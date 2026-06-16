<!-- image -->

- &lt; Text search functional overview &gt;

The following gives an example of command transmission used to set the printer to print the 'first logo' at the end of receipt when the print data contains a character string 'Cheese burger'.

|    |                                                                      | Function No.   | Contents                                                                                                                                                                                                                                                                                                                                                                                                     |
|----|----------------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | 1C 71 ..                                                             | --             | Register the logo as the first logo (see FS q).                                                                                                                                                                                                                                                                                                                                                              |
|  2 | 1B 1D 29 42 02 00 51 00                                              | Function 81    | Initialize the settings and definitions of functions 48, 49, 50, 64, 65, and 66.                                                                                                                                                                                                                                                                                                                             |
|  3 | 1B 1D 29 42 02 00 30 01                                              | Function 48    | Enable text searching.                                                                                                                                                                                                                                                                                                                                                                                       |
|  4 | 1B 1D 29 42 02 00 31 00                                              | Function 49    | Set the text search macro to run once.                                                                                                                                                                                                                                                                                                                                                                       |
|  5 | 1B 1D 29 42 02 00 32 00                                              | Function 50    | Configure the print setting for the matched text string such that the matched text string is printed.                                                                                                                                                                                                                                                                                                        |
|  6 | 1B 1D 29 42 11 00 40 01 01 0D 43 68 65 65 73 65 20 62 75 72 67 65 72 | Function 64    | Set the text search string with string number 1 to 'Cheese burger,' and set the text search macro that is executed when this string is included to text search macro 1.                                                                                                                                                                                                                                      |
|  7 | 1B 1D 29 42 08 00 41 01 04 00 1C 70 01 00                            | Function 65    | Define text search macro 1 as a command to print logo 1 (see FS p).                                                                                                                                                                                                                                                                                                                                          |
|  8 | 1B 1D 29 42 03 00 42 01 01                                           | Function 66    | Set the execution time for the text search macro that is ex - ecuted when text search string 1 is included (text search macro 1 in this case) to immediately before cutting.                                                                                                                                                                                                                                 |
|  9 | 1B 1D 29 42 02 00 60 00                                              | Function 96    | Print the settings and definitions of functions 48, 49, 50, 64, 65, and 66. Check the settings and definitions.                                                                                                                                                                                                                                                                                              |
| 10 | 1B 1D 29 42 02 00 61 01                                              | Function 97    | Check the settings and definitions. Make sure the macro runs properly.                                                                                                                                                                                                                                                                                                                                       |
| 11 | .. 43 68 65 65 73 65 20 62 75 72 67 65 72 .. 0A 1D 56 42 00          | --             | Send print data that includes a string such as that shown in fig. 1 ('Cheese burger') and a trigger command, and check to make sure that the printed result is similar to fig. 2.                                                                                                                                                                                                                            |
| 12 | 1B 1D 29 42 02 00 50 00                                              | Function 80    | Register the text search settings and definitions to non- volatile memory. After you make sure that everything works properly, use this command to register the text search set - tings and definitions to non-volatile memory. Afterward, even if you do not send commands 1 to 10, you can obtain a printed result such as that shown in fig. 2 simply by sending print data such as that shown in fig. 1. |

Before setting the text search

## SOOO OOOO IOK OK STAR BURGER ORC OK OK ROKR KOK IK

1. Cheese burger

-*

1 $1.50

ont

.

aetti

os,

&lt;

ye

suneeeeeeeeeeeneneeeeet®

:

:

:

ates

.

The first logo is printed becu -ase the data contains the string 'Cheese burger'.

5

After setting the text search

## SOOO OOK ICKIOK STAR BURGER

SECO

1. stheese" burger 1 feeee Burger

1

$1.50

1

$10

wa.

ttstSCS

A

$2.50

ar

FREE!!

Small Fries with your next Mega Burger!

<!-- image -->

Y
