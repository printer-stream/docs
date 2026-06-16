## C O N F I D E N T I A L

| Command   | Classification      | Name                                               | Function type              |
|-----------|---------------------|----------------------------------------------------|----------------------------|
| ESC \     | EXECUTING COMMAND   | Set relative print position                        | PRINT POSITION COMMANDS    |
| ESC a     | SETTING COMMAND     | Select justification                               | PRINT POSITION COMMANDS    |
| ESC c 3   | SETTING COMMAND     | Select paper sensor(s) to output paper-end signals | PAPER SENSOR COMMANDS      |
| ESC c 4   | SETTING COMMAND     | Select paper sensor(s) to stop printing            | PAPER SENSOR COMMANDS      |
| ESC c 5   | SETTING COMMAND     | Enable/disable panel buttons                       | PANEL BUTTON COMMAND       |
| ESC d     | EXECUTING COMMAND   | Print and feed n lines                             | PRINT COMMANDS             |
| ESC i     | EXECUTING COMMAND   | Partial cut (one point left uncut)                 | MECHANISM CONTROL COMMANDS |
| ESC m     | EXECUTING COMMAND   | Partial cut (three points left uncut)              | MECHANISM CONTROL COMMANDS |
| ESC p     | EXECUTING COMMAND   | Generate pulse                                     | MISCELLANEOUS COMMANDS     |
| ESC u     | SETTING COMMAND     | Transmit peripheral device status                  | STATUS COMMANDS            |
| ESC v     | SETTING COMMAND     | Transmit paper sensor status                       | STATUS COMMANDS            |
| ESC t     | SETTING COMMAND     | Select character code table                        | CHARACTER COMMANDS         |
| ESC {     | SETTING COMMAND     | Turn upside-down printing mode on/off              | CHARACTER COMMANDS         |
| FS g 1    | SETTING COMMAND     | Write to NV user memory                            | CUSTOMIZE COMMANDS         |
| FS g 2    | EXECUTING COMMAND   | Read from NV user memory                           | CUSTOMIZE COMMANDS         |
| FS p      | EXECUTING COMMAND   | Print NV bit image                                 | BIT-IMAGE COMMANDS         |
| FS q      | EXECUTING + SETTING | Define NV bit image                                | BIT-IMAGE COMMANDS         |
