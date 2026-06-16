<!-- image -->

## ESC GS * W

[Name] [Code]

Register mark format to non-volatile memory

ASCII

ESC

GS * W

Hex.

1B 1D 2A 57

Decimal

27 29 42 87

[Defined Area]

- - -

[Initial Value]

- - -

[Function]

Registers the mark format (mark height, mark line feed amount, each mark color, and each mark horizontal width) to the non-volatile memory.

After registering to the non-volatile memory, the printer is reset. Invalid in page mode.

## ESC GS * C

[Name] Initialize mark format in the non-volatile memory

[Code]

ASCII

ESC   GS * C

Hex.

1B 1D 2A 43

Decimal

27 29 42 67

[Defined Area]

- - -

[Initial Value]

- - -

[Function]

Initializes the registered mark format (mark height, mark line feed amount, each mark color, and each mark horizontal width) in the non-volatile memory. After initialization, the printer is reset.

## Initial Value of the Mark Format

- Mark Height::

'016' 16 dots

- Mark line feed amount::

'032' 32 dots

- Mark color:

'0' (White → All mark numbers)

- Mark horizontal width:

'080' 80 dots →

All mark numbers)

Invalid in page mode.

-----------------------------------------------------------------------------
