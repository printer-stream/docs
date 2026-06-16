<!-- image -->

## HP-IL Interfacing

## What You'llLearn in This Chapter

This chapter is only for 7470 owners with an HP-IL interface. HP 7470s with Option 003have an HP-IL interface.

In this chapter, you will find a brief overview of HP-IL, a list of the HP-IL capabilities implemented on the 7470,and examples of sending and receiving data using a variety of computers.

## An Overview of HP-IL

In an HP-IL system, devices are connected to each other in a closed loop. All devices communicate by sending messages consisting of 11 bits each; these messages travel through the loop in one direction, one bit at a time. Only one message is traveling around the loop at a given time.

There are three categories that describe whether devices can send or receive messages: talkers, listeners, and controllers.

- 0 Talkers are devices that send data over the interface; only one talker can be active at a given time. The controller designates the role of talker with commands that are dependent on the specific controller. The 7470is capable of being a talker.
- 0 Listeners are devices that receive data from a talker or commands from a controller; several listeners can be active simultaneously. As with talkers, listeners are designated by the controller. The 7470 is capable of being a listener.
- 0 Controllers are in charge of all loop operations. For example, the controller assigns the roles of talker and listener, assigns addresses, and initiates data transfer between devices. There can be more than one controller in a loop, but only one can be active at any time, and only one can be the system controller. A controller is typically a portable computer or calculator. The 7470does not have the ability to be a controller.
