## Format

ASCII ESC c nL nH

<!-- formula-not-decoded -->

## Parameter range

0 ≤ nH ≤ 4

```
0 ≤ nL ≤ 255 0 <((nH × 256) + nL)) ≤ 1080 ; HMI ≤ 3.00 inches
```

## Function

Fixes the character width (HMI) according to the following formula:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Default

Depends on panel or DIP-switch setting

## Notes

- This command is available only on printers featuring ESC/P 2.
- This command cancels additional character space set with the ESC SP command.
- The HMI setting made with this command is canceled when the printer receives the following commands: SO, SI, DC2, DC4, ESC W, ESC P, ESC M, ESC g, ESC p, ESC !, ESC SP, and ESC @.
- Use this command to set the pitch if you want to print normal-height 10 or 20-point characters at 15 cpi during multipoint mode. Selecting 15 cpi for 10 or 20-point characters with the ESC X command results in characters being printed at 2/3 their normal height.

## Printers not featuring this command

All non-ESC/P 2 printers

Model-dependent variations

None

## Related topics

ESC X, ESC P, ESC M, ESC g, ESC p, ESC !, Selecting the pitch
