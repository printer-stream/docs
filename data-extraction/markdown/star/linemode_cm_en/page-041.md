<!-- image -->

## 3.3.5. Pa ge Control

<!-- image -->

Commands

FF

[Name]

Form feed

[Code]

ASCII

FF

Hex.

0C

Decimal

12

[Defined Area]

- - -

[Initial Value]

- - -

[Function]

Executes a form feed.

If the current position is at the top of the page, it form feeds to the top of the next page. If there is data existing in the line buffer when executing a form feed, it prints that data, then executes the form feed.

However, by printing data remaining in the buffer, and moving to the top of the next page, a form feed is considered to have been executed, so form feed is not performed. Invalid in page mode.

## ESC C n

[Name] [Code]

Set page length to n lines

ASCII

ESC C n

Hex.

1B 43 n

Decimal

27 67 n

[Defined Area]

1 ≤ n ≤ 127

[Initial Value]

(Form feed amount initial value x 42)

[Function]

The position whereat this command is processed is considered the top of the page and sets the page length to (current form feed amount x n).

This command cancels the bottom margin setting when setting page length.

The page length set using this command is unaffected by changing the form feed amount later. Moving to the top of the page is performed using the following commands.

- Form feed command (FF):

Executes a form feed.

- Cutter command (ESC d n):

Sets cutter position at top of page.

- Raster command (ESC * r B):

Sets top of page when quitting raster mode.

- Error cancel operations:

Sets position when quitting error cancellation operations at top of page.

-----------------------------------------------------------------------------
