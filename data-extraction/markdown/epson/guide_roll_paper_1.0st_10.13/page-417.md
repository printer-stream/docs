## C O N F I D E N T I A L

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U230 , TM-U220

## Program Example for all printers

PRINT #1, "          AAAAA"; CHR$(&amp;HA); PRINT #1, CHR$(&amp;H1D);"V";CHR$(66);CHR$(0); ← Feed paper and cut

## TM-J2000/J2100

The vertical motion unit is specified by GS P .

The cutting shapes of ( m = 0,48) and ( m = 1,49) are the same as the cutting shape of ( m = 65) and ( m = 66). Whether the operation is a full cut or a partial cut (one point is left) is determined by the installation position of the autocutter. The distance from print head to autocutter is about 24.5 mm {1 inch}.

## TM-T90

The vertical motion unit is specified by GS P .

The cutting shapes of ( m = 0,48) and ( m = 1,49) are the same as the cutting shape of ( m = 65) and ( m = 66). The setting is partial cut (one point is left) when the printer is shipped. It can be changed to full cut setting by dealer's option. The distance from print head to the autocutter is about 14 mm {0.55 inch}.

After executing a paper cut, a paper feed for 1 mm {other than Japanese specifications:14/360 inches/Japanese specification:16/406 inches} before starting the next printing can provide the best printing result without uneven paper feeding. If the printer is left until the next printing after executing a paper cut, feeding paper more than 1 mm can avoid a paper jam inside the autocutter.

## TM-L90

## TM-L90 with Peeler:

The printer does not support this command.

## Print Sample

Paper fed to the cutting position and partial cut (one point left uncut) performed

AAAAA
