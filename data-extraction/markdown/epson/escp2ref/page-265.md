## The attribute byte for NLQ 9-pin characters

With NLQ characters, the attribute byte determines the width of the character only.

Determine the width of your pattern data in columns (1 to 12) and set the attribute byte equal to the number of columns. Repeat the data within the brackets for each character you are defining. You must send an attribute byte for each character you define.

## Examples

The following example replaces the + character with the following 9-pin, draft, user-defined character:

<!-- image -->

## Note:

Only the characters with codes between 58 and 63 may be user-defined on an LXseries printer.

First set the attributes. The following commands do this (see 'Setting userdefined character traits'):

ESC x 0 Selects draft mode

ESC 5 Cancels italic printing

Next, send the data for the character. You must select the beginning and ending column if you want to use the character during proportional spacing; also, in this example you will be using the upper 8 pins.

To determine the value of the attribute byte, look at the chart above; your character starts in column 0 and ends in column 10.

Value Beginning column is 0 0 Ending column is 10 10 Upper 8 pins 128 Total attribute byte = 138 Following the attribute byte is the pattern data.
