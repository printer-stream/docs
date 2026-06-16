## C O N F I D E N T I A L

## [Recommended Functions]

This command is supported by some printer models and will not be supported by future models. Future models will not support counter value.

## [Notes]

- ■ The internal counter value which counts the repetition number of printing by processing this command is '0.'
- ■ The value of the counter is updated when executing GS c by following the counter mode set by this command.
- ■ In count-up mode, the counter value exceeds the maximum counter value ( sb ), the printer restart counting from the minimum counter value ( sa ).
- ■ In count-down mode, the counter value is below the minimum counter value ( sb ), the printer restart counting from the maximum counter value ( sa ).
- ■ counter value and sa is the maximum counter value.
- ■ In count-stop mode, the counter value is not changed by GS c .
- ■ The settings of a counter mode set by GS C 1 and the counter value set by GS C 2 are disabled by processing this command.
- ■ sa, sb, sn, sr , and sc specify a value using a decimal character string, respectively.
- ■ sa, sb, sn, sr, and sc can be omitted (';' which separates an argument, cannot be omitted). Setting value for the omitted argument is not changed.

## Example:

- When changing only a stepping amount for a count-up or count-down and a counter value, the setting value is [ GS C ; ; ; 5 ; ; 100 ; ].
- ■ The counter value range (maximum value and minimum value), stepping amount of incrementing or decrementing of a counter value, and repetition number of printing are effective until GS C 1 is executed, ESC @ is executed, the printer is reset, or the power is turned off.
- ■ The value of the serial number counter set by this command is effective until GS C 2 is executed, ESC @ is executed, the printer is reset, or the power is turned off.
