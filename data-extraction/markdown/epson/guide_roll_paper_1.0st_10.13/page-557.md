## C O N F I D E N T I A L

## &lt;Function 62&gt; FS ( E pL pH fn m kc1 kc2 a n ( fn =62)

```
[Name] Set top logo printing [Format] ASCII FS ( E pL pH fn m kc1  kc2 a n Hex 1C 28 45 pL pH fn m kc1  kc2 a n Decimal 28 40 69 pL pH fn m kc1  kc2 a n [Range] ( pL + pH × 256) = 6  ( pL = 6, pH = 0) fn = 62 m = 2 32 ≤ kc1 ≤ 126 32 ≤ kc2 ≤ 126 48 ≤ a ≤ 50 0 ≤ n ≤ 255
```

## [Description]

## [Notes]

Sets top logo key code, justification, and number of lines to be removed after top logo printing.

- ■ Associates key codes ( kc1 , kc2 ) of NV graphics to be printed as a top logo.
- ■ a specifies justification for top logo printing.
- ■ n specifies the number of lines to be removed after top logo printing.
- ■ NV memory is used as the storage area for set values of top logo printing.

- a Function

- 48 Specifies left justification.

- 49 Specifies centering.

- 50 Specifies right justification.

SETTING COMMAND
