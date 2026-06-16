9-Pin ESC/P

Since you will not add any space to the left or right of the character, set the a0 and a2 parameters to 0. Since the character width is 34 columns, set a1 equal to 34. Then send the dot data.

The resulting command is as follows:

ESC &amp; 0 43 43 0 34 0

The data (102 bytes) is as follows

0, 0, 0, 32, 0, 16, 0, 0, 0, 32, 0, 16, 0, 0, 0, 32, 0, 16, 0, 0, 0, 32, 0, 16, 31, 255, 224, 32, 0, 16, 31, 255, 244, 32, 0, 16, 0, 0, 0, 32, 0, 16, 0, 0, 0, 32, 0, 16, 0, 0, 0, 32, 0, 16, 0, 0, 0, 32, 0, 16, 0, 0, 0, 32, 0, 16, 0, 0, 0, 32, 0, 16, 31, 255, 224, 32, 0, 16, 31, 255, 224, 32, 0, 16, 0, 0, 0, 32, 0, 16, 0, 0, 0, 32, 0, 16, 0, 0, 0, 32, 0, 16

The character is now stored in location 43, the former + location. You can print the character by switching to RAM printing (see 'Switching to RAM character printing') and then sending code 43 (the + character).

Use the ESC &amp; command to send user-defined data to the printer. The format of the command is:

Draft characters:

ESC &amp; NUL n m [a d0 d1 d2 . . . dk]

NLQ-mode characters:ESC &amp; NUL n m [0 a 0 d0 d1 d2 . . . dk]

The value for n is the location of the first consecutive character you wish to redefine; m is the last character. See the ASCII character table in the Appendix for the order of the characters. To define just one character, n is the same as m.

Parameter a is called the attribute byte; the purpose of the attribute byteis different for draft and NLQ characters. Both explanations are included below.

The attribute byte for draft 9-pin characters

With draft 9-pin characters, the attribute byte sets the following parameters of the character you are defining:

- The pin group (the upper 8 pins or the lower 8 pins
- -Select the upper 8 pins if your character has no descenders.
- -Select the lower 8 pins if your character has descenders.
- The beginning column (during proportional spacing)
- -The ending column (during proportional spacing)
