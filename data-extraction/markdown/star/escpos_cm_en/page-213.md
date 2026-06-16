<!-- image -->

## ESC	GS	/	4	nL	nH	d1	d2	...	dk

Name

Set user macro 2

Code

ASCII ESC GS / 4 nL nH d1 d2...dk

Hex. 1b 1d 2f 34 nL nH d1 d2...dk

Decimal 27 29 47 52 nL nH d1 d2...dk

Defined Region

1 ≤ nL ≤ 64

nH = 0

1 ≤ (nL+nHx256)  ≤ 64

dk =  (nL+nHx256)

0 ≤ d ≤ 255

Initial Value

No user macro 2 setting

Function

Sets the user macro 2 of the Auto Logo function.

This command is registered to the non-volatile memory by the '&lt;ESC&gt; &lt;GS&gt; / W' command.

This command is ignored when Auto Logo is being executed.

Registers print data in user macro 2.

A maximum of 64 bytes of data can be registered.

Note that it is prohibited to register Auto Logo command characters in a user macro.

Reference

ESC GS / W, ESC GS / C, ESC GS / 1, ESC GS / 2, ESC GS / 3, ESC GS / 5, ESC GS / 6
