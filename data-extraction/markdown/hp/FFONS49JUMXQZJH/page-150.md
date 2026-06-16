## Monitor Mode

After the plotter is in the on-line, programmed-on state, two mutually exclusive monitor modes may be enabled using the set plotter configuration instruction, ESC . @. Depending upon which monitor mode is enabled, either all data (including device control instructions) are re­ transmitted to the terminal CRT or only HP-GLdata are retransmitted as they are parsed from the plotter's buffer. All plotter output responses are sent to both the computer and terminal. Refer to The Set Plotter Configuration Instruction, ESC . @,for complete information.

The plotter monitors for a terminal-generatedBreak signal. Receipt of a Break signal will cause the same results as described under the on-line, programmed-on state. Then, new plotter on and set plotter configuration instructions from the computer are required to resume plotting opera­ tions with monitor mode active. The following diagram shows how the plotter processes data while in monitor mode.

Monitor Mode

<!-- image -->

T
