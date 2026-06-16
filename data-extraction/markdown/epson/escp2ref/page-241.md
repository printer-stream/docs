- The margins must be set at the beginning of the line (before any printable data is sent); otherwise, the printer ignores any data preceding these commands.
- Always set pitch before setting left and right margins. Do not assume what the pitch setting will be.

The diagram below shows the margins set by sending the following commands when 8 1/2-inch wide paper is used and the left edge of the paper is at the leftmost mechanically printable position.

| ESC @    | Resets printer settings                                |
|----------|--------------------------------------------------------|
| ESC P    | Selects 10-cpi printing (character width of 1/10 inch) |
| ESC l 10 | Sets a 1-inch left margin                              |
| ESC Q75  | Sets a 1-inch right margin                             |

<!-- image -->

## Setting page length

Because the method of page handling is different, the method for setting the page length differs for ESC/P 2 and previous ESC/P versions. This section explains both methods.

<!-- image -->

The ESC/P 2 method of setting the page length allows you to use the same program for both single-sheet and continuous paper.

The page length setting is effective only when you are using continuous paper. However, since the printer ignores the setting during single-sheet printing, the printer is always ready to print on either type of paper.
