## C O N F I D E N T I A L

## GS ( k &lt;Function 367&gt;

- [Name] 2-dimensional GS1 DataBar: Set the width of the module [Format] ASCII GS ( k pL pH cn fn n Hex 1D 28 6B 03 00 33 43 n Decimal 29 40 107 3 0 51 67 n [Range] ( pL + pH × 256) = 3 ( pL =3, pH =0) cn = 51 fn = 67 TM-P60 , TM-T20 , TM-T88V : 2 ≤ n ≤ 8 [Default] TM-P60 , TM-T20 , TM-T88V : n = 2 [Description] Sets the width of the module for 2-dimensional GS1 DataBar to n dots. [Notes] ■ Settings of this function affect the processing of Functions 381 and 382.
- ■ Settings of this function are effective until ESC @ is executed, the printer is reset, or the power is turned off.

[Model-dependent variations]

TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60

## TM-T90 , TM-T88IV , TM-T70 , TM-L90

This model does not support this function.

## TM-T20

TM-T20 supports this function.

The setting unit is 1 dot. The width is set in units of 0.125 mm {1/203 inch}.

## TM-T88V

TM-T88V supports this function.

The setting unit is 1 dot. The width is set in units of 0.141 mm {1/180 inch}.
