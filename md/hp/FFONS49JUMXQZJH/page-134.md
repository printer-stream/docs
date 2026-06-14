## Addressing the 7470 as a Talker or Listener 

In order to communicate effectively with the 7470 plotter, it is important that you completely understand the addressing protocol of your computer. Therefore, you may wish to review this aspect of your computer before proceeding. 

## Computers with No High Level I/O Statements 

On low level computers, addressing devices on the HP-IB bus is accomplished using mnemonics, such as CMD, which serve as the “bus command.” 

When bus commands are necessary, a typical addressing sequence is 

<Unlisten Command> <Talk Address> <Listen Addresses> 

This sequence is made up of three major parts which serve the following purposes: 

1. The unlisten command is the universal bus command with a character code of “?”, It unaddresses all listeners. After the unlisten command is transmitted, no active listeners remain on the bus. 

2. The talk address designates the device that is to talk. A new talk address automatically unaddresses the previous talker. 

3. The listen addresses designate one or more devices that are to listen. A listen address adds the designated device as listener along with other addressed listeners. 

This basic addressing sequence simply states who is to talk to whom. The unlisten command (“?”) plays a vital role in this sequence. It is important that a device receive only the data that is intended for it. 

When a new talk address is transmitted in the addressing sequence, the previous talker is unaddressed. Therefore, only the new talker can send data on the bus and there is no need to routinely use an untalk command in the same manner as the unlisten command. 

## Computers with High Level I/O Statements 

In more powerful computers, higher level input/output (I/O) state ments are used to specify device addresses on the HP-IB bus. In these cases, the addressing protocol (unlisten, talk, listen) is a function of the computer’s internal operating system and need not be of concern to the user. 

9-6 HP-IB INTERFACING 
