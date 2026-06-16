<!-- image -->

## STAR

&lt;When using GS1 Databar Expanded (m = 78)&gt;

To print GS1 Databar Expanded on this printer, be careful of the following points to send the bar code data.

## The following special characters operate as shown below.

| Special Characters   |      |         |                                                                                                                                                        |
|----------------------|------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Special Characters   | Hex. | Decimal |                                                                                                                                                        |
| (                    | 28   | 40      | ''(' is reflected by the HRI. This is useful when using '(',')' to highlight the AI. It is not included in encoding data.                              |
| )                    | 29   | 41      | The first ')' after d1 is the data division identifier for identifying (AI). The ')' is reflected by the HRI but is not included in the encoding data. |

## Also the following characters are expressed as 2 bytes.

| Special    | Transmission Data   | Transmission Data   | Transmission Data   |
|------------|---------------------|---------------------|---------------------|
| Characters | ASCII               | Hex.                | Decimal             |
| FNC1       | {1                  | 7B, 31              | 123, 49             |
| '('        | {(                  | 7B, 28              | 123, 40             |
| ')'        | {}                  | 7B, 29              | 123, 41             |

- ・ If the double-digit lead for the bar code data line is not a number, or is not '(' and a number, command

processing is stopped at this point and the next data is processed as standard data.

- ・ If the combination of '{' and the character directly behind does not correspond to, command processing is
- stopped at this point and the next data is processed as standard data.
- ・ Although '*' can be used, it is not reflected in the HRI or the encoding data.
- If printing bar codes that require check digits on STAR printers, even if the check digit is sent as a bar code, the check digit that was calculated on the printer is printed.

Reference

GS H, GS f, GS h, GS w, Appendix-6
