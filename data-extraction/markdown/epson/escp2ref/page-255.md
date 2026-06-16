| ESC/P 2   | ESC/P   | 9-Pin ESC/P   |
|-----------|---------|---------------|

You must tell the printer where to find characters: either in the ROM memory (for built-in characters) or in the RAM memory (for user-defined characters). Each time you want to print a user-defined character, you must switch to RAM memory.

You may plan on using many of the standard characters along with your userdefined characters. If so, you can avoid having to switch between ROM and RAM memory each time by copying the characters from the printer's ROM memory to its RAM memory. The ESC : command performs this function.

When you send the ESC : command, the printer copies all the characters from locations 0 to 127 in the currently selected typeface to the same locations in RAM memory. You can then store your user-defined characters and still print all the other characters (except those you redefine) without having to switch back and forth between RAM and ROM memory each time.

Keep the following in mind when copying ROM characters to RAM memory.

- On some printers, you can specify which typeface to copy to RAM memory; see ESC : in the Command Summary and Command Table sections.
- You can only define 10.5-point characters. Even if you select a different point size with the ESC X command, characters in RAM can only be printed as 10.5-point characters (or as 21-point characters if double-height is selected).
- Sending the ESC : command erases any characters that are currently stored in RAM. Always copy ROM characters to RAM before you define user-defined characters. (You cannot copy ROM characters to RAM during multipoint mode.)
- The RAM memory can only store characters of one type at the same time. If you define subscript user-defined characters when normal height characters are stored in RAM memory, for example, the printer erases all previously stored characters. Always set the desired character traits before copying characters (both ROM and user-defined characters).
- Characters copied from ROM to RAM with the ESC : command must have the same traits as the user-defined characters you plan to define. If you define user-defined characters with different traits, the printer erases all previous characters in RAM memory.
- Defining user-defined characters clears any characters previously at that character code location.
- To print characters in RAM, you must first copy characters with the ESC : command or define characters with the ESC &amp; command. The printer ignores commands that would print characters that have not been defined; nothing will be printed.
