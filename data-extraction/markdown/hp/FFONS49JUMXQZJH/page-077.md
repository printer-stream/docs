Default control character ETX terminates by perForming end­ oF-text Function.

Printing characters terminate. #but are also printed.#

Control characters terminate and perform their function.

## The Label Instruction, LB

DESCFNPTIUNThe label instruction, LB, provides the means to letter text, expressions, or string variables using the currently defined char­ acter set.

DEE The label instruction can be used to annotate graphs or create text-only overhead transparencies. |

SYNTAX LB c...ct

where t is the label terminator, either the default ETX character (decimal equivalent 3), or another character defined by the DT instruction.

EXPLANATIONAll printing characters following the LB mnemonic are drawn using the currently selected character set. The set used is specified by the commands CA or CS and selected by the commands SA or SS, or the ASCII control characters shift-out or shift-in (decimal equivalent 14and 15respectively). If not specified, the default character set (set 0) is used.

The direction, size, and slant of the characters assume default values if not previously specified by DI, DR, S1,or SR commands.

The label mode can be terminated only by sending a label terminator at the end of the character string. Refer to The Define Terminator In­ struction. (With an HP-IB interface, the bus commands interface clear IFC, device clear DCL, or selected device clear SDC will also terminate label mode. Refer to Bus Commands, Chapter 10.)Unless a label string is terminated, subsequent HP-GL commands will appear as labels in your plot.

The label begins at the current pen position. Before executing the LB command, the pen should be moved to the location where labeling is to begin using one of the plot commands (PA, PR, or a character plot command CP) or by front-panel controls. This establishes the lower-left
