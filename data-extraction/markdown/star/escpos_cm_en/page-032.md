<!-- image -->

## 4-2 Exception	Processing

## 1. Undefined	codes

Codes from &lt;00&gt;H to &lt;1F&gt;H are targeted.  When codes not defined as commands in this region are re ceived, they are discarded.

- (Ex.) If processing the data string of &lt;30&gt;H&lt;31&gt;H&lt;03&gt;H&lt;32&gt;H&lt;0A&gt;H&lt;33&gt;H, the printer will discard &lt;03&gt;H as an undefined code.

## 2. Undefined	commands

When data continuing the codes of ESC, FS, GS, DLE are codes not defined as commands, ESC, FS,GS, DLE and subsequent codes are discarded.

- (Ex.) If processing the data string of &lt;30&gt;H&lt;1B&gt;H&lt;22&gt;H&lt;31&gt;H&lt;32&gt;H, the printer will read and dis card &lt;1B&gt;H&lt;22&gt;H as an undefined command.

## 3. Settings	outside	of	the	defined	area

Processing values outside of the defined area in commands accompanying arguments, those commands are ignored and the preset values are unchanged.  The processing of commands is terminated at the point values outside of the defined region are processed in arguments having a plurality of commands.

- (Ex.) If processing the data string of &lt;1B&gt;H&lt;52&gt;H&lt;15&gt;H, the printer will discard the data string of &lt;1B&gt;H&lt;52&gt;H&lt;15&gt;H because although &lt;1B&gt;H&lt;52&gt;H is defined as a commands (ESC R), the argument &lt;15&gt;H is outside of the definition.  Therefore, the international character set that is al ready set experiences no change.

## 4. Real-time	Commands

Real-time commands are stored in the reception buffer.
