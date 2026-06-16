<!-- image -->

## FS C n

Name

Select Chinese character code type

Code

ASCII

FS C n

Hex.

1C 43 n

Decimal

28 67 n

Defined Region

n = 0, 1, 48, 49

Initial Value

n = 0

Function

Selects the Chinese character code type.

| n     | Selection           |
|-------|---------------------|
| 0, 48 | JIS Code Type       |
| 1, 49 | SHIFT-JIS Code Type |

## Details

STAR

- If using the JIS code type, the Chinese characters codes below are effective.  This command is enabled only when using Japanese language specifications.
- If using the SHIFT-JIS code type, the Chinese characters codes below are effective.
- This command is ignored when the memory switch location of use is specified as SBCS (single byte countries).

First Byte: &lt;21&gt;H to &lt;7E&gt;H

Second Byte: &lt;21&gt;H to &lt;7E&gt;H

First Byte: &lt;81&gt;H to &lt;9F&gt;H and &lt;E0&gt;H to &lt;EF&gt;H

Second Byte: &lt;40&gt;H to &lt;7E&gt;H and &lt;80&gt;H to &lt;FC&gt;H
