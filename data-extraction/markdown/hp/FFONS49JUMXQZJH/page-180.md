The following parameters are established:

turnaround delay = 500, no output trigger character, no echo terminate character, output terminator = default value, carriage return, intercharacter delay = 5, no immediate response string, block size = 80, enquiry character = bell (decimal equivalent 7), and 9

acknowledgment string = ! carriage return (decimal equivalent 33, 13)

Now the computer sends the Bell character as the enquiry character. The plotter waits approximately 505 milliseconds, the total of the turnaround delay and the intercharacter delay, before sending its response. During that time, the computer will send the ? due to the INPUT statement, but the plotter ignores it. The plotter response to the enquiry character is now two characters, I followed by a carriage return. The carriage return to terminate INPUT is now part of the acknowledgment string. No output terminator, now defaulted to carriage return, is sent because handshake mode 2 is set here by ESC . I. The output terminator, carriage return, will still follow all responses to HP­ GLoutput commands.

## The Output Extended Status Instruction,

## ESC . 0

DESCRIPTIONThe output extended status instruction, ESC . O, outputs the plotter's extended status, giving information about the state of the buffer, pinch wheels, and VIEW button.

USES The instruction can be used to determine, from a remote location, if the plotter is ready to plot.

## SYNTAX , ()

EXPLANATIONNo parameters are used. Unlike the HP-GL output status instruction, OS, the ESC . O instruction does not enter the buffer but is executedimmediately, subject to any turnaround or intercharacter delays specified by ESC . M and ESC . N.
