<!-- image -->

## Note:

- You always assign the tables at the beginning of a print job; do not assume what the settings are.
- You can reassign any of the tables at any time, without affecting other table assignments.
- Do not assign a registered table to Table 2 if you plan to use it for userdefined characters. Once you assign a registered table to Table 2, you must reset the printer (with the ESC @ command) before you can use it for userdefined characters.

The following commands assign character tables to active tables 0 to 3.

| ESC ( t 3 0 0 0 0   | Assigns the italic table to active Table 0.                |
|---------------------|------------------------------------------------------------|
| ESC ( t 3 0 1 1 0   | Assigns the PC437 (US) table to active Table 1.            |
| ESC ( t 3 0 2 8 0   | Assigns the PC865 (Canada-French) Table to active Table 2. |
| ESC ( t 3 0 3 3 0   | Assigns the PC850 (Multilingual) table to active Table 3.  |
