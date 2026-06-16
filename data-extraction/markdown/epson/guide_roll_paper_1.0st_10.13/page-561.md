## C O N F I D E N T I A L

## &lt;Function 65&gt; FS ( E pL pH fn m a n ( fn =65)

```
[Name] Enable/disable top/bottom logo printing [Format] ASCII FS ( E pL pH fn m a n Hex 1C 28 45 pL pH fn m a n Decimal 28 40 69 pL pH fn m a n [Range] ( pL + pH × 256) = 4  ( pL = 4, pH = 0) fn = 65 m = 2 a = 48, 49 n = 48, 49 [Default] n = 48 [when a = 48] n = 48 [when a = 49]
```

[Description]

[Notes]

Specifies top/bottom logo printing by a and enables or disables top/bottom logo printing by n .

- ■ Top/bottom logo printing specified by a is as follows:
- ■ Enabling/disabling setting specified by n is as follows:
- ■ Volatile memory is used as the storage area for set values ( n ).
- ■ This command is used when changing the setting of 'Logo printing enabled' set with FS ( E &lt;Function 64&gt; to Disabled temporarily.

- a Function 48 Specifies top logo printing. 49 Specifies bottom logo printing.

```
n Function 48 Enables. 49 Disables.
```

EXECUTING COMMAND
