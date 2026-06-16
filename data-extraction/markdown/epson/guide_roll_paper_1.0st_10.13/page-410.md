## C O N F I D E N T I A L

## ESC i

EXECUTING COMMAND

[Name]

Partial cut (one point left uncut)

[Format]

ASCII

ESC i

Hex

1B 69

Decimal

27 105

[Range]

None

[Default]

None

[Printers not featuring this command] TM-J2000/J2100 , TM-T90 , TM-L90 , TM-P60 , TM-U230

[Description]

Executes a partial cut of the roll paper.

[Recommended Functions]

This command is supported by some printer models but will not be supported by future printer models. GS V is recommended for cutting paper. GS V &lt;Function A&gt; gives the same result as this command.

[Notes]

- ■ See GS V &lt;Function A&gt; for details.

- ■ The cutting shape depends on the specification of the mounted autocutter.

See program example and print sample for ESC i and ESC m.

[Model-dependent variations]

TM-T20 , TM-T88IV , TM-T88V , TM-U220

## TM-T20 , TM-T88IV , TM-T88V

The distance from print head to autocutter is about 15 mm {0.59 inch}.

After executing a paper cut, a paper feed for 1 mm {14/360 inches} before starting the next printing can provide the best printing result without uneven paper feeding.

## TM-U220

This printer may make 'dot displacement' after autocutting. It is recommended to feed approximately 2.116 mm or more for printing the next line to prevent 'dot displacement after cutting.'
