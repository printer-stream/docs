<!-- image -->

## 4-3-6 STAR	Original	Mark	Commands

This command is specialized for printing mark sheets for lotteries.  This command can print lines.

<!-- image -->

## &lt;Example	of	Command	Transmission&gt;

- Mark Format

Mark Height h = 10 dots, Mark line feed amount v = 20 dots

Mark number 0: Mark Color c = White, Mark horizontal width w = 16 dots

Mark number 1: Mark Color c = Black, Mark horizontal width w = 40 dots

Mark number 2: Mark Color c = White, Mark horizontal width w = 40 dots

<!-- image -->

## ·	Example	Transmission

```
1. Mark height, Line feed amount setting <ESC> <GS> *1 h v (h = '010', v = '020') 2. Color of each mark number, Horizontal width setting
```

```
<ESC> <GS> *2 m c w  (Mark number 0 setting: m = '0', c = '0', w = '016') <ESC> <GS> *2 m c w  (Mark number 0 setting: m = '1', c = '1', w = '040')
```

&lt;ESC&gt; &lt;GS&gt; *2 m c w  (Mark number 0 setting: m = '2', c = '0', w = '040')

3. Register the mark format specified by 1 and 2 in advance in the non-volatile memory (it is possible to print marks that are not registered in the non-volatile memory.)

<!-- formula-not-decoded -->

```
4. Printing Marks <ESC><GS>*0nm1m2m3m4m5m6m7 (n = '007', m1 = '1', m2 = '0', m3 = '1', m4 = '0', m5 = '1', m6 = '0', m7 = '2') <ESC><GS>*0nm1m2m3m4m5m6m7 (n = '007',m1 = '1', m2 = '0', m3 = '2', m4 = '0', m5 = '1', m6 = '0', m7 = '1') <ESC><GS>*0nm1m2m3m4m5m6m7 (n = '007', m1 = '1', m2 = '0', m3 = '1', m4 = '0', m5 = '2', m6 = '0', m7 = '2')
```
