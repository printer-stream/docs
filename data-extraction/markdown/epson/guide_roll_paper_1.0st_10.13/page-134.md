## C O N F I D E N T I A L

[Model-dependent variations]

## TM-P60 , TM-U220 , TM-T20 , TM-T88V

## Program Example for all printers

```
FOR n=0 TO 10 PRINT #1, CHR$(&H1B);"R";CHR$(n);
```

```
PRINT #1, "# $ @ [ \ ] ^ ` { - }  ~ "; CHR$(&HA); NEXT n
```

```
Print Sample # $ @ [ \ ] ^ ` { -} ~ ← n=0 (Default setting) # $ ˆ û · ¤ ^ ` Ž · · ¬ ← n=1 # $ ¤ € … † ^ ` Š š Ÿ § ← n=2 £ $ @ [ \ ] ^ ` { -} ~ ← n=3 # $ @ ® ¯ · ^ ` ¾ ¿ Œ ~ ← n=4 # Û ƒ € … · † Ž Š š Œ Ÿ ← n=5 # $ @ û \ Ž ^ · ˆ ˜ · ' ← n=6 t P $ @ Á ' À ^ ` ¬ -} ~ ← n=7 # $ @ [ ´ ] ^ ` { -} ~ ← n=8 # Û ƒ ® ¯ · † Ž ¾ ¿ Œ Ÿ ← n=9 # $ ƒ ® ¯ · † Ž ¾ ¿ Œ Ÿ ← n=10
```

## TM-P60

Settings of this command do not affect special font (24 × 48) printing. Special fonts (24 × 48) print characters when USA is selected, irrespective of the settings of this command.

## TM-U220

The character code table (GB18030 / GB2312) of Simplified Chinese model is selected by using Memory switch {Msw2-3}. See GS ( E &lt;Function 3&gt; for details on the Memory switch.

## TM-T20 , TM-T88V

When the default of the international character set is changed with GS ( E &lt;Function 5&gt; &lt;a = 9&gt;, the default value becomes the one specified by GS ( E.
