## **OSE** 

## **Hewlett Packard 7475A Graphics Plotter** 

**Plotting method Plotting speed Resolution Paper Handling Interfaces Emulations** 

## Multi-pen plotter 

Pendown 38.1 cm/s; pen up 50.8 cm/s Smallest addressable move 0.025mm 

A3- and A4-size paper and transparency film. S-232C or HP Interface Bus (HP-IB) (IEE-488) HP Graphics Language (HP-GL) 

## **Control Panel** 

**ERROR light:** Indicates plotter error condition 

**B/A3, A/A4 lights:** indicate current selected paper size. 

**P1, P2 keys:** On power-up, raises pen and moves it to default position (lower left) of A/A4 paper size, or raises pen and moves it to default position (lower left) of B/A3 paper size. When either one is pressed together with **Enter** key, will establish new location of scaling point **P1** or **P2** . 

**PEN U/D key:** Reverses the current pen state (up or down). 

**SIZE key:** When pushed simultaneously with **Enter** key, selects paper size as indicated by size lights. **PEN keys:** Causes plotter to retrieve same pen number from carousel. **ENTER key:** Multi-use key for changing paper size and location of scaling points P1 and P2. 

**Cursor keys:** Move pen in the direction of the arrow. Using adjacent keys will move the pen at a 45 degree angle. 

**FAST key:** When used with any cursor key, will increase pen speed 4X. **VIEW key:** Turns Error light on, suspends the pen plotting, raises pen to manually change pen and view paper. When pressed again, error light will turn off, return to last coordinates and up or down status, and resume printing. 

## **Self-test** 

## Basic test: 

1. Make sure six pens are installed in carousel and plotter is on. 

2. With paper loaded, lower PAPER LOAD lever to PAPER HOLD position. 

3. Press a **PEN** key to select a pen and then use **Cursor** keys to test selected pen. 

- **Demonstration plot** - Perform the following procedure to draw a bar, pie and line chart. 

1. Make sure six pens are installed in carousel and plotter is off. 

2. With A/M-size paper loaded, lower PAPER LOAD lever to PAPER HOLD position. 

3. While holding the **P1** and **P2** keys, turn plotter on. 

**Troubleshooting test** - The following procedure exercises both motor drive circuits, motors and encoders, the servo chips, error light circuit, gate arrays, microprocessor and ROM. 

1. Make sure paper is loaded and plotter is on. 

2. Manually move pen carriage near center of its travel. 

3. Hold ENTER key while turning plotter on. The ERROR light should remain on. 

4. Press <-- key. 

5. If successful, the ERROR light should turn on and off continuously, and pen carriage and paper should move left and right about 6.4mm continuously. 

6. Press ENTER key to pause test and <-- key to resume test. To terminate test, turn plotter off and back on. 

## **Plotter Configuration** 

The plotter's interface is configured through a bank of DIP switches located on the rear panel. The DIP switches will vary according to which interface (RS-232C or HP-IB) is installed. 

**DIP Switches** - RS-232C 

**Switch Label** - Description 

**A3/A4** - Selects B/A3-size or A/M-size paper. 

**D/Y** - In the Y position, received data is retransmitted and plotter does not respond unless it receives a "Plotter On" command. In the D position, plotter responds to all commands. 

## **DIP Switches** - HP-IB 

**Switch Label** - Description 

**ADDRESS** - Five of the seven DIP switches set the HP-IB address in binary coded decimal. 

**A3/A4** - Selects B/A3-size or A/A4-size paper. 

**MET/US** - Selects maximum plotting area. If B/A3-size paper is selected, MET selects 275x402mm and US 1 0.2x16.3 in. If A/M-size paper is selected, MET selects 192x275mm and US 7.5x10.2 in. 

**Baud Rate Selection *** - RS-232C 

|~~ee~~|**One**<br>**Stop Bit**<br>~~ee~~|||||**Two**<br>**Stop Bits**|||
|---|---|---|---|---|---|---|---|---|
|**Baud Rate**<br>~~ee~~<br>~~es~~|**B4**<br>~~ee~~|**B3**|**B2**|**B1**|**B4**|**B3**|**B2**|**B1**|
|External<br>~~ee ~~<br>~~es~~<br>~~ee~~|-<br> ~~ee~~|-|-|-|0|0|0|0|
|75<br>~~es~~<br>~~ee~~<br>~~es~~|-<br>~~ee~~|-<br>~~de~~|-<br>~~de~~|-<br>~~de~~|0|0|0|1|
|110<br>~~ee~~<br>~~es~~|-<br>~~ee~~|-<br>~~de~~|-<br>~~de~~|-<br>~~de~~|0|0|1|0|
|150<br>~~es~~<br>~~a~~<br>~~ee~~|0<br>~~ee ~~<br>~~ee~~|0<br> ~~de~~<br>~~ee~~|1<br>~~de~~|1<br>~~de~~|-|-|-|-|
|200<br>~~ee~~|0<br>~~ee~~|1<br>~~ee~~|0|0|-|-|-|-|
|300<br>~~ee ~~<br>~~a ee~~<br>~~ee~~|0<br> ~~ee~~<br>~~ee~~<br>~~ee~~|1<br>~~ee~~<br>~~ee~~<br>~~ee~~|0<br>~~ee~~|1<br>~~ee~~|1<br>~~ee~~|0<br>~~ee~~|1<br>~~ee~~|1<br>~~ee~~|
|600<br>~~ee~~<br>~~es~~|0<br>~~ee~~<br>~~ee~~|1<br>~~ee~~<br>~~ee~~|1<br>~~ee~~|0<br>~~ee~~|1<br>~~ee~~|1|0|0|
|1200<br>~~ee ~~<br>~~es~~<br>~~ee~~|0<br> ~~ee~~<br>~~ee~~|1<br>~~ee~~<br>~~ee~~|1<br>~~ee~~|1<br>~~ee~~|1<br>~~ee~~|1|0|1|
|2400<br>~~es ~~<br>~~ee~~<br>~~es~~|1<br> ~~ee ~~<br>~~ee ee~~|0<br> ~~ee ~~<br>~~ee~~|0<br> ~~ee~~<br>~~ee~~|0<br>~~ee~~<br>~~ee~~|1<br>~~ee~~<br>~~ee~~|1|1|0|
|4800<br>~~ee~~<br>~~es~~<br>~~ee~~|1<br>~~ee ee~~<br>~~ee~~|0<br>~~ee~~<br>~~ee~~|0<br>~~ee~~|1<br>~~ee~~|1<br>~~ee~~|1|1|1|
|9600<br>~~es ~~<br>~~ee~~|1<br> ~~ee ee~~<br>~~ee~~|0<br>~~ee~~<br>~~ee~~|1<br>~~ee ~~|0<br> ~~ee~~|-<br>~~ee~~|-|-|-|



*1 = switch open; 0 = switch closed. 

## **BAUD RATE** 

**S1/PARITY** - Toggles PARITY on and off. 

**S2/PARITY** - If switch S1/PARITY is set to 1 (switch open), selects odd or even parity. 

**MET/US** - Selects maximum plotting area. If B/A3-size paper is selected, MET selects 275x402mm and US 1 0.2x16.3 in. If A/M-size paper is selected, MET selects 192x275mm and US 7.5x1 0.2 in. 

## **Common Problems and Fixes** 

**Plotter does not respond to control panel, ERROR lights is off, and the PAPER lever is In the load position:** 

1. Check rear-panel line fuse, voltages and power supply fuses on PCA. 

2. Check 4 MHz clock and Gate Array B. 

## **Plotter responds to control panel but not to host:** 

1. Make sure interface connection is properly seated at both ends. 

2. Test the I/O circuits by sending "SP1;SP2" from host. 

September 1995 Copyright IBM Corporation 1995. All rights reserved. 

**1** 

HP-37 
