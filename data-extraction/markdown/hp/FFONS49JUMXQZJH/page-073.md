| Decimal v(llU9                          | Set I] Stmdurd ASCII   | Set 1 9825 Set   | Set 2 French/Geruan   | Set 3 Scandinavim   | Set 4 SpanishlLatin Aneri can   |
|-----------------------------------------|------------------------|------------------|-----------------------|---------------------|---------------------------------|
| 35 39 91 92 93 94 95 96 123 124 125 126 | # ' [ \ 1 " ' { I } '  | #                | .€                    |                     |                                 |

## The Designate Standard Character Set Instruction, CS

DESCFHPTIUN The designate standard character set instruction, CS, provides the means of designating one of the five character sets (0 through 4) as the standard character set.

USES The instruction can be used to change the standard character set to one with characters appropriate for your application. It is espe­ cially useful when labels are in a language other than English.

SYNTAX CS character set number (terminator)

EXPLANAHONThe character set number can be 0 through 4. The set designated by the CS instruction is used for all labeling operations when the standard set is selected by the SS instruction or by the control character shift-in (decimal equivalent 15)in a label string. Character set 0 is automatically designated as the standard character set when­ ever the plotter is initialized or set to default values.

A CS command executed while the standard set is selected will imme­ diately change the character set used for labeling. CS commands
