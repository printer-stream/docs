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

**Hewlett Packard 7475A Graphics Plotter** 

**OSE** 

## **Pen up/down does not work:** 

1. Check fuse A1F2 and pen supply voltage. 

2. Check solenoid continuity. 

## **Diagonal lines are not straight:** 

1. Check for defective pen drive motor/encoder assembly (especially if diagonals askew near horizontal lines). 

2. Check for defective paper drive motor/encoder assembly (especially if diagonals askew near vertical lines). 

3. Check for deposits on grit wheels, pinchrollers and slider rod. Clean slider rod and pinchrollers with a dry wipe. 

## **Critical Adjustments** 

**Note:** Before performing any of the following procedures, remove top cover (see "Cover Removal" below). 

**Adjusting pen height** - Perform the following procedure if pen carriage assembly is disassembled or replaced. 

1. Position pen holder at center of platen. 

2. Use a 100mm ruler to measure distance from platen to bottom of pen holder. It should be 10.5mm. 

3. Insert a 0.050 inch Allen wrench through hole at rear of pen carriage. Turn clockwise to decrease pen height or counter-clockwise to increase pen height. 

## **Removing pen carousel housing:** 

1. Disconnect pen carousel cable from J8 on main printed circuit board. 

2. Remove screw that secures pen carousel housing to chassis assembly. 

3. Tip pen carousel housing forward and lift it straight up. 

## **Cover Removal** 

1. Turn plotter off and disconnect power cord and interface cable. 

2. Remove 3 screws at rear of plotter. 

3. Lift rear of top cover so that the front releases from base. 

## **Field Replaceable Units** 

|**Field Replaceable Units**||
|---|---|
|**DESCRIPTION**|**OEM P/N**|
|Damper, silicone rubber|07475-4000|
|Paper drive motor assembly|07470-6017|
|PCA-Main HP-IB|07475-6010|
|PCA-Main RS-232C|0747506010|
|Pen carriage|5040-8650|
|Pen drive motor assembly|07470-6018|
|Pen carousel motor|3140-0687|
|Pen carousel assembly|5061-5080|
|Pen holder|07475-6002|
|Solenoid|07475-6001|
|Spring, pen down|1460-1950|



**Note:** Be sure to print a menu/configuration list before replacing a PCS or logic containing configuration settings. 

## **Removing paper drive motor assembly:** 

1. Disconnect paper drive motor cable {twisted pair) from J3 and flat encoder cable from J1 on main printed circuit assembly. 

2. Remove pen drop shield. 

3. Loosen motor clamp and remove motor from its mounting. 

## **Removing pen solenoid:** 

1. Loosen paper drive motor clamp enough to slide motor right about 3/4 inch. Lift right end of motor slightly to release motor from chassis. 

2. Disconnect solenoid cable from J2 on printed circuit assembly. 

3. Loosen solenoid mounting screw enough to allow solenoid removal. 

## **Removing pen drive motor and belt:** 

1. Disconnect pen drive motor cable (twisted pair) from J5 and flat encoder cable from J6 on main printed circuit assembly. 

2. Remove belt tensioner by pressing down on tensioner and sliding the tang at bottom out of chassis slot. 

3. Loosen pen drive motor clamp and remove motor. 

4. Slide belt from pen carriage to remove it. 

5. Loosen pen solenoid mounting screw and slide solenoid to the right. Remove armature and spring. 

6. Slide pen lift bar just far enough right to allow belt removal. 

## **Removing pen carriage, pen holder, and damper:** 

1. Remove paper drive motor (see above). 

2. Remove pen solenoid (see above). 

3. Remove pen drive motor (see above) 

4. Slide belt from pen carriage and move carriage to the left. 

5. Remove end bearing cap while sliding pen lift bar to the right and out of carriage assembly. 

IBM P/N: 55X3584 IBM machine type: 1538-B01, 1516-H20 **Tech Support 800-877-7764** 

6. Move slider rod to the right just far enough to release left end of rod from its mounting. Slide rod to the left and out of carriage/pen holder assembly. 

7. Carefully remove plastic damper from carriage and pen holder. 

**Note:** After reassembling the above, measure the pen down force with a gram gauge before replacing the top cover. Turn plotter on. Lower a pen onto platen. Place tip of gauge under lip of pen body and make sure that pen just starts to lift with 19 +/ 10 grams. If it does not, replace the pen down spring. 

## **Removing printed circuit assembly:** 

1. Disconnect all cables from printed circuit board. 

2. Remove pen carousel housing (see above). 

3. Remove screw holding control panel and remove panel. 

4. Remove recessed screw between pen solenoid and pen drive motor. 

5. Lift right side of chassis assembly. Tabs on left side will release from base plate. 

6. Remove screws or studs holding rear panel interface connector. 

7. Lift front end of printed circuit assembly and remove it from base plate. 

IBM/TSS Internal Use Only 

**2** 

HP-37 

HEWLETT PACKARD 

## HP 7475A Color Desktop Plotter 

## Technical Data 

## Features 

- Two small-fonnat media sizes 

- Full range of pen/media combinations 

- High-quality output 

- Strong software support 

- Hardware compatibility 

- Built-in intelligence 

The HP 74 75A color desktop plotter produces high-quality A4/A- and A3/B-size color graphics for business and PC CAD applications. The HP 7475A is ideal for professionals who need the larger drawings for PERT charts, flow charts, pro­ ject schedules, and design applications. It also produces professional-quality color overheads for presentations and colorful summary charts for handouts and reports. 

## Full Bange of Pen/Media Combinations 

HP 7475A users can select from paper (regular and glossy), over­ head transparency film, and durable double-matte polyester film. Fiber-tip pens for paper and transparencies come in 10 bright colors and two tip widths. Refillable liquid-ink pens are available for final-quality draw­ ings on polyester film. 

## High-quality Output 

The HP 74 75A color desktop plotter combines high resolu­ tion and excellent repeatability to ensure professional-quality output. It has an addressable resolution of 0.025 mm 

- (0.001 in.), so it can plot up to 1000 points in a one-inch line. 

## The one plotter for both CAD and color business graphics 

When commanded to return to the same point with no pen change, it does so within 0.1 mm (0.004 in.). This preci­ sion means your drawings have straight lines, crisp characters, circles that close, and corners that meet. 

Strong Software Support One of the most widely­ supported plotters in the world, the HP 7475A works with major software packages from the entire spectrum of graphics applications-integrated soft­ ware, business graphics/presen­ tations, computer-aided-design/ drafting, scientific and statis­ tical analysis, project scheduling, and more. 

## Hardware Compatibility 

A choice of two interfaces makes it easy to add an HP 74 75A to almost any system-personal computers, mainframes, even smart instru­ ments. The HP 74 75A comes with RS-232-C/CCI'IT V.24 and HP-m (IEEE 488-1978) inter­ face options. And with an additional eavesdrop cable, the RS-232-C plotter can be con­ nected in series between a computer and a tenninal. 

## Built-in Intelligence 

The HP 7475A's control-panel keys can alter the size of the drawing area when switching media sizes or rotate the plot 90 degrees. Control-panel keys can also be used in conjunction with a digitizing sight. 

Programmers will appreciate the intelligence features which eliminate the need for software­ generated characters and func­ tions. Hewlett-Packard Graphics Language (HP-GL) instructions (more than 50) govern such tasks QS labeling, pen move­ ment, and drawing arcs and circles. 

## Thchnical Information 

## Media Sizes 

210 x 297 mm (ISO A4) 8I/.! x 11 in. (ANSI A) 297 x 420 mm (ISO A3) 11 x 17 in. (ANSI B) 

## Pens 

Number: 6 in carousel 

Type: Fiber-tip (paper and transparency), refillable short­ body liquid-ink 

## Media 

Paper (regular and glossy), transparency film, double-matte polyester film 

## Character Sets 

French/German, HP 9825, Scandinavian, Spanish/Latin American, Roman Extensions , and these ISO registered sets: ANSI ASCII (006), French (025), German (021), International Reference Version (002), Italian (015), JIS ASCII (014), Katakana (013), Norwegian I (060), Norwegian 11 (016), Portuguese (016), Spanish (017), Swedish (010), Swedish for Names (011), United Kingdom (004) 

## Acceleration 

Approximately 2 g 

## Maximum Plotting Area 

Pen axis: 258.0 mm (10.2 in.) for A/B; 275.0 mm (10.8 in.) for A4/A3 

Paper axis: 198.0 mm (7.80 in.) for A; 192.0 mm (7.56 in.) for A4; 414.0 mm (16.3 in.) for B; 402.0 mm (15.8 in.) for A3 

## Buffer Size 

1024 bytes 

## Environmental Ranges 

## Thmperature 

Operating: 0 to 55 degrees C (32 to 131 degrees F) 

Storage: -40 to 75 degrees C (-40 to 167 degrees F) 

## Humidity 

Operating: 5 to 95% (at 40 degrees C) 

## Power Requirements 

Source: 100, 120,220, 240 V, -10%, +5% 

Frequency: 48-66 Hz 

Consumption: 35 W maximum 

## Physical Specifications 

## Resolution 

Addressable: 0.025 mm (0.001 in.) 

Mechanical: 0.025 mm (0.001 in.) 

## Repeatability 

With a given pen: 0.1 mm (0.004 in.) 

Pen to pen: 0.2 mm (0.008 in.) 

## Pen Velocity 

Pen down, maximum: 38.1 cm/s (15.0 in./s) 

Pen up: 50.8 cm/s (20.0 in'/s) Programmable: approximately 0.4 to 38.1 cmls (0.2 to 15.0 in'/s) in increments of 0.4 cm/s 

Height: 127.0 mm (5.0 in.) Width: 568.0 mm (22.4 in.) Depth: 367.0 mm (14.5 in.) Net weight: 7.0 kg (16.0 lb) Shipping weight: approx. 11.0 kg (25.0 lb) 

## Product Certifications 

FCC certified to conform to limits set for radio frequency when used with a Cla B com­ puting device; meets or exceeds IEC-380, IEC-435, IEC-478, and CSA C22.2 No. 154. 

## Ordering Information 

Interface and Ordering Information Cable Requirements Standard Unit System Cable 7475A HP Vectra PC with HP 24540AlB HP 24542G Color desktop plotter seriaVparaliel interface card or HP 24541 AlB dual serial interface card using 9-pin connector Option numbers: HP Vactra PC with HP 24541 AlB HP 17255M 001 RS-232-C/CCI'IT V.24 dual serial interface card using interface 25-pin connector 002 HP-IB (IEEE 488-1978) HP Touchscreen PC using serial HP 17255M interface interface HP Touchscreen PC using HP-IB HP 10833A (1.0 mJ Note: Interface cables must be interface HP 10833B 12.0 ml ordered separately HP 10833C 13.0 m) HP 10833D 10.5 mJ Accessories Included HP 3000 or DEC VAX in eavesdrop HP 17455A Operation and Interconnection configuration Manual (language appropriate IBM PS/2,['] PC, PC-Xl, and HP 17255D compatibles to plotter destination) IBM AT and compatibles HP 24542G Reference Card Apple Macintosh 128K and 512K HP 92219M Power cord (appropriate to Apple Macintosh SE, Macintosh HP 17302A plotter destination) Plus, and Macintosh 11 Apple lie HP 17355M Plotter paper 50 sheets, A4/A size (paper sizes determined by plotter destination) Transparency film sampler, A4/A size (film sizes deter­ ! mined by plotter destination) Six-pen carousel for fiber-tip pens Assorted fiber-tip paper and transparency pens HP Plotter Supplies Catalog 

## Accessories Av ble 

07475·90000 Hardware Suppan Manual 07475·90001 Interfacing/Programming Manual 5061·5080 Additional fiber ·tip pen carousel 07475-60030 

For a complete list of available supplies, check the current ver­ sion of the HP Plotter Supplies Catalog or the Hewlett-Packard PC Peripherals Price Guide. 

HEWLETT PACKARD 

## United States: 

Hewlett-Pa.ckard Company 4 Choke Cherry Road Rockville, MD 20850 301 670 4300 

Hewlett-Packard Company 5201 Tollview Drive Rolling Meadows, IL 60 8 312 255 9800 

Hewlett-Packard Company 5161 Lankershim Blvd. No. Hollywood, CA 91601 818 505 5600 

Hewlett Packard Company 2015 South Park Place Atlanta, GA 30339 404 955 1500 

Europel AfricalM.lddle East: Hewlett-Packard S.A. 

Central Mailing Department P.O. Box 529 1180 AM Amstelveen The Netherlands 31 20/547 9999 

## Far East: 

Hewlett-Packard Asia Ltd. 221F Bond Centre West Tower 89 Queensway Central, Hong Kong 5 848 7777 

## Japan: 

Yokogawa Hewlett-Packard Ltd. 29-21, Takaido-Higashi 3-chome Suginami-ku, Tokyo 168 03 331 6111 

## Canada: 

Hewlett-Packard Ltd. 6877 Goreway Drive Miuga, Ontario L4VIM8 416 678 9430 

AustralialNew Zealand: Hewlett-Packard Australia Ltd. 31-41 Joseph Street Blackburn, Victoria 3130 Melbourne, Australia 03 895 2895 

## Latin America: 

Latin American Region Headquarters Monte Pelvoux Nbr. 111 Lomas de Chapultepec 110 Mexico D.F., Mexico 905 596 79 33 

Te information in tbis doclUnt is subject to change without notice. 

Copyright © 1989 Hewlett-Packard Company 

Printed in USA 2/89 5954·7091 

## COMPUTER PERIPHERALS Graphics Plotters Models 7470A and 7475A 

- Low cost, high performance 

- Choice of six- or two-pen models 

Hewlett-Packard's HP 7470A and 7475A graphics plotters provide the kind of graphics excellence you would expect to find only in much more expensive plotters. They feature the same high-quality compo­ nents and innovative paper-moving technology which were intro­ duced in HP's drafting plotters and which make it possible to offer high performance plotters at affordable prices. Refer to the table be­ low for a quick comparison of the main features available in each plotter. 

|plotter.|||
|---|---|---|
|Features|HP 7475A|HP 7470A|
|Media sizes|Two ANSI sizes:A(8.5 x 11 in.)<br>andB(11x17 in.)<br>Two ISO sizes:A4(210 x 297 mm)<br>andA3(297 x 420 mm)|One ANSI size:A(8.5x11 in.)<br>One ISO size:A4(210 x 297 mm)|
|Pans|Six fiber·tip; programmable pen<br>selection; automatic capping|Two fiber·tip; programmable pen<br>selection; automatic capping|
|HP-Cl<br>Instructions|More than 50 instructions|More than40instructions|
|Character<br>sets|19 sets. including ISO European<br>standards and Katakana|Five sets|
|Standard<br>Interfaces|HP·IB (IEEE 488-1978)or<br>RS-232.c(CCITTV.24)|HP-IB (IEEE 488-1978)or<br>RS-232.c(CCITTV.24) orHP-IL|
||Eachplotter incorporatesonepermanent interface option.||
|Technology|Both plotters use the same micro-grip drive for paper movement and<br>have the same high resolution. repeatability, and velocity.||



## computer Applications 

The HP 7470A and 7475A provide hardcopy computer graphics for technical, scientific, and business applications. Colorful A4/ A-size charts and graphs are ideal for reports and overhead trans­ parencies. Use them for summarizing data, identifying trends, com­ paring results, and focusing on exceptions. The larger A3/B-size plots that can be drawn on the HP 7475A are particularly useful for time lines, PERT charts, schematics, engineering drawings, and other ap­ plications where you need to show visual detail. 

- Plot on paper 

- Plot on HP overhead transparency film 

## Measurement Applications 

The HP 7470A and 7475A add hard copy graphics capability to intelligent instruments and instrument systems with HP-IB (IEEE 488-1978). For most applications that use a display screen and an oscilloscope camera, these plotters can produce high-quality hard­ copy of the screen for a cost that is substantially lower than camera film. Because they plot directly from measured data, they eliminate problems created by distortion from the screen. And plotter output provides better visual resolution than photographs. Many systems without screen displays can also have the benefits of HP 7470A or 7475A hardcopy graphics at very little additional cost. 

## Easy to Use 

When the HP 7475A or 7470A plotters are turned on, default con­ ditions are automatically established for most plotting parameters. In many cases, it is only necessary to load the pens and plotting medium in order to start plotting. 

Media and pen loading are also easy. A guide control lever makes media alignment perfect every time. The front panel can be used to select pens, to halt the program for exchanging pen colors, or to move the plot forward to "view" what you have plotted. 

The front panel also allows easy access to the plotter's digitizing capability and scaling points. And, on the HP 7475A, push buttons can rotate plots 90 degrees or run a demonstration plot directly from the plotter. 

## Intelligence Features 

Intelligence features are built directly into these plotters to save you time by eliminating the need for software-generated characters and functions. Many HP-GL instructions (more than 50 in the HP 7475A; more than 40 in the HP 7470A) govern such tasks as labeling, pen movement, drawing arcs and circles, and selecting from a large variety of character sets. The HP 7475A has 19 character sets in- 

## COMPUTER PERIPHERALS Graphics Plotters Model 7470A and 7475A (cont'd) 

cluding ISO European sets, Katakana, ASCII, and Roman 8 exten­ sions; the HP 7470A has five internal character sets. 

The HP 7475A's extra HP-GL instructions, which are used for fill­ ing rectangles and wedges for pie and bar charts, provide an enhance­ ment especially designed for professional graphics. 

## Writing Systems 

The HP 7470A has two built-in pen stalls which make two-color plotting easy. For plots with more than two colors, the program can be halted through program or front panel control; new pens can then be installed and plotting resumed. The HP 7475A's six-pen carousel al­ lows you to store up to six different pen colors or a variety of colors and widths. 

Several automatic features are included to protect the tip of the pen and increase pen life. When housed in the stall or carousel, the pen is capped to prevent premature drying. When a pendown command is given, the pen force is damped and the pen is gently lowered to the plotting surface. 

## High-Quality Output 

The HP 7470A and 7475A have an addressable step size of 0.025 

mm (0.001 in.). With this resolution, they can plot up to 1000 points in a I-inch line. When commanded to return to the same point with no pen change, they achieve this repeatability within 0.1 mm (0.004 in.) Because of this outstanding resolution and repeatability, both plotters produce straight lines and smooth circles that have an artist-drawn appearance. 

## Interface Options 

The HP 7475A and 7470A are easy to interface with most HP and non-HP computers. Both plotters offer the RS-232-C/CCITT V.24 or HP-IB (IEEE 488-1978) interface. With the RS-232-C option, a dual input/output cable is available for connecting the plotters with a terminal and computer. In addition, the HP 7470A offers a third in­ terface option, HP-IL. This interface is used to connect the plotter with low-cost, portable HP systems. 

## Graphics Software 

HP offers a full line of graphics software packages for use on most HP computer products. And software is also available for many non­ HP computers. These packages make it easy for non-programmers to use the HP 7470A and 7475A plotters. Details are available from any HP sales and support office. 

|Specifications|||
|---|---|---|
|Specifications<br>~~**C**~~|HP7475A<br>HP7470A<br>~~**C**O~~||
|Resolution<br>~~**C**~~|Smallest addressable stepsize: 0.025 mm(0.001 in.)<br>~~**C**O~~<br>~~e~~||
|Repeatab**l**lty|With a given pen: 0.1 mm (0.004 in.)<br>Frompen topen: 0.2 mm(0.008 in.)||
|Penvelocity(each axis)|Pen up, 50.8 cmfs(20 in.fs);pen down, maximum - 38.1 cmfs(15 in.fs),programmable - I to 38 cmfs in I cmfs increments<br>~~a~~||
|A**c**eleration|Approximately2g's<br>~~a~~||
|Envtronmental range|Operating, O'C to 55'C<br>Non'operating, -4O'C to 75'C<br>~~ce~~||
|Plotting area<br>X·axis<br>Y·axis|258mm(10.2 in.), AlB<br>275 mm (10.8 in.), MfA3<br>198 mm (7.80 in.), A<br>192mm(7.56 in.), M<br>414 mm (16.3 in.), B<br>402 mm(15.8 in.), A3|191 mm (7.5 in.) A<br>191 mm (7.5 in.), A4<br>257 mm (10.2 in.), A<br>272 mm (10.7 in.), A4|
|Interfaces<br>~~|~~|HP-IB (IEEE 488-1978), implements the following HP-IB functions as defined in IEEE 488-1978: SHI, AHI, T2, TEO, LEO, SRI, RLO, DCI, DTO, L2,ppo,(listen only or address less<br>than 7, otherwise PP2)<br>~~|~~||
||R5-232-GfCCITI, asynchronous serial ASCII with switch selectable baud rates of 75,<br>Same as HP 7475A except 255 byte buffer.<br>1l0, 150,200,300,6**0**, 1200, 2400,48**0**,9600. External clock input<br>capabilities with intermediate baud rates of upto96**0** baud. 1024 byte buffer.<br>HP-IL, Hewlett-Packard Interface Loop for use with portable systems.<br>~~|~~<br>~~)~~<br>~~!~~<br>~~|~~||
|||HP-IL, Hewlett-Packard Interface Loop for use with portable systems.<br>~~|~~|
|Power Requirements<br>~~|~~|Source:100, 120, 200, 240<br>-10%, +5%Frequency: 48-S6Hz<br>~~|~~<br>Ve<br>|||
||Consumption:35 W maximum<br>Ve|Consumption:25Wmaximum<br>||
|Size:<br>Height<br>127 mm (5 in.)<br>Width<br>568 mm (22.4 in.)<br>Depth<br>367 mm(14.5 in.)<br>~~Po~~||127 mm (5 in.)<br>432 mm (17 in.)<br>343 mm(13.5 in.)<br>||
|Weight:<br>Net<br>7 kg (16.0 Ib)<br>Shipping<br>Approx. II kg (25.0 Ib)<br>~~Po~~||6 kg (13.5 Ib)<br>Approx. 10 kg(22.0 Ib)<br>||
|FCe certified to conform to limits set for radio frequencyinterference when used with a Class B computingdevice.<br>~~Po~~<br>|<br>FCC<br>~~|~~<br>~~|~~|||



## Accessories Supplied 

## HP 7475A 

HP 07475-90001 Interfacing and Programming Manual 

HP 07475-90002 Operation and Interconnection Manual HP 07475-90004 Reference Card 

## HP 7470A 

HP 07470-90001 Interfacing and Programming Manual HP 07470-90002 Operator's Manual 

HP 07470-90003 Interconnection Guide 

HP 07470-90004 Reference Card 

Power cords and an assortment of pens and drawing media are also supplied with the plotters. The media size and the appropriate power cord are determined by plotter destination. The HP-IL cable (V2-me­ tre) is supplied with Option 003 only. 

Note: Interface cables are not supplied with Option 001 and Option 002 plotters. 

## Ordering Information Options 

## Price 

001 RS-232-C/CCITT V.24 (cable not included) N/C 002 HP-IB (IEEE 488-1978) (cable not included) N/C 003 HP-IL for 7470A only (cable included) N/C Note: Option 001, 002, or 003 must be specified when ordering HP 7470A; Option 001 or 002 must be speci­ fied with HP 7475A. Interface Cables HP 13242G Male-male, special RS-232-C cable for use with Option 001, HP 150 Personal Computer HP 172550 Male-female, special RS-232-C cable for use with Option 001, IBM Personal Computers HP 17355F Male-male standard cable for use with Op­ tion 001 HP 17455A Eavesdrop cable for use with Option 001 HP 10833A or HP 45529A or HP 31389A HP-IB I-metre cable for use with Option 002 HP 82167A HP-IL Y2-metre cable (included with Op­ $6 tion 003) Plotters HP 7470A Two-pen Graphics Plotter $1095 HP 7475A Six-pen Graphics Plotter $1895 $52.50 $50 $81 $75 $69 

## Interfaceand Personal CablesPrinters for HP Graphicsi Plotters TECHNICAL DATA, MARCH 1985 

**==> picture [92 x 73] intentionally omitted <==**

**----- Start of picture text -----**<br>
a BacarHEWLETT<br>¢»<br>museum<br>**----- End of picture text -----**<br>


Most HP plotters are not shipped with an interface terminal), consult the tables on Page 2. Cable schematics cable. Hewlett-Packard graphics plotters (HP 7470A, 7475A, appear on Page 3. For ordering information, see Page 4. 7550A), drafting plotters (HP 7580B, 7585B, 7586B), and . personal printers (HP Laserjet, HP Thinkjet) can be used Standalone Configurations: with a variety of HP and non-HP personal computers and Ina standalone configuration, the plotter/printer is connected computer systems. However, because different configurations to its own dedicated computer port. This setup is primarily often require different interface cables, customers must order for personal computers in workstation environments, but the appropriate cable separately. also includes peripherals on their own computer port in To find the proper cable to connect your plotter or printer mainframe environments. to your personal computer, check the table below. To deterNote: Cables from non-HP computer manufacturers are mine the proper cable for other configurations (such as conlisted for information purposes only. Check with the manunecting your plotter or printer to a mainframe computer facturer for current model numbers and prices. 

**==> picture [464 x 303] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Printer/Piotter to Personal Computer,|Standalone|(RS-232-C)|
|HP|Laserjet|HP 7470A,|7475A,|
|Computer System|HP Thinkjet|7580B, 7585B,|7586B|HP 7550A|
|HP|Series|150, TI|Pro,|HP|13242G|HP|13242G|HP|17255D|
|Wang PC|
|The|HP PORTABLE|HP|92221P|HP|9222iP|HP|92221P and|
|HP|17355F*|
|IBM PC and PC/XT,|HP|17255D|HP|17255D|HP|17255F|
|Compaq, AT&T PC 6300|
|IBM AT|HP|17255D|and|IBM|HP|17255D|and|IBM|HP|17255F|and|IBM|
|6450242|Serial|6450242|Serial|6450242|Serial|
|Adapter|Cable|Adapter|Cable|Adapter Cable|
|IBM PCr|HP|17255D|and IBM|HP|17255D|and IBM|HP|17255F and IBM|
|Serial|Device|Serial|Device|Serial|Device|
|Adapter|Cable|Adapter|Cable|Adapter|Cable|
|Apple|Ile, DEC|HP|17355M|HP|17355M|-|HP|17355D|
|Rainbow,|Osborne|
|Apple|//!|HP|17355M"**|and|HP|17355M**|and|HP|17355D and|
|Apple A3M0019|Apple A3M0019|Apple A3M0019|
|Apple Ic|Apple A9C0308|Apple A9C0308|HP|17355F*|and|
|Apple A9C0308|

**----- End of picture text -----**<br>


*If the combination of these two cables (over 4 m) is too long, order HP 92222F instead of HP 17355F; second cable is still necessary. **If the combination of these two cables (over 3 m) is too long, order HP 92222M instead of HP 17355M; the Apple A3M0019 is still mecessary. 

Y 

**==> picture [228 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
Printer/Plotter to Personal Computer<br>(HP-IB/IEEE-488)<br>Computer HP HP 7470A, 7475A, 7550A,<br>System Thinkjet| 7580B, 7585B, 7586B<br>HP Series 80, HP 45529A/B or<br>HP Series 150, HP 10833A/B or<br>HP 9000 Series HP 31389A/B<br>200, 500<br>**----- End of picture text -----**<br>


**==> picture [206 x 86] intentionally omitted <==**

**----- Start of picture text -----**<br>
Plotter to Mainframe, Standalone<br>(RS-422-A)<br>Computer<br>System HP 7550A only<br>HP 3000 Series 64, 39, HP 17855A<br>42, 48<br>**----- End of picture text -----**<br>


**==> picture [232 x 237] intentionally omitted <==**

**----- Start of picture text -----**<br>
Printer to Mainframe, Standalone<br>(RS-232-C)<br>Computer<br>System HP Laserjet only<br>HP 3000 Series 37 ATP HP 92218D<br>Plotter to Calculator/Handheld Computer<br>(HP-IL)<br>Computer<br>System HP 7470A only<br>HP Series 40 Calculator HP 82167A<br>HP Series 70 Handheld<br>Computer<br>**----- End of picture text -----**<br>


Eavesdrop Configurations: tions is the one from the plotter to the mainframe computer. In an eavesdrop configuration, the plotter is situated between These plotters have two RS-232-C ports, so the terminal to a mainframe computer (i.e., HP 3000, IBM 360/370, DEC mainframe computer cable is used with the second RS-232-C VAX) and a terminal or a personal computer being used as a port on the plotter. terminal. Both the terminal and plotter share the same RSTo232-C port from the mainframe computer. When connectingan HP 7470A or 74754 in eavesdropmode, use an HP 7550A, 7580B, 7585B, or 7586B in eavesdrop a special eavesdrop cable (HP 17455A) is required in addition mode, the only additional cable required in most configurato the cable from the plotter to the mainframe computer. 

**==> picture [458 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|
|Eavesdrop Configuration (RS-232-C)|
|Computer System|HP 7470A, 7475A|HP 7580B,|7585B, 7586B|HP 7550A|
|HP|Series|150|(in|HP|17455A and|HP|17355M|or|HP|17355M or|
|terminal|mode)|HP|13242N|HP|13242N|HP|13242N|
|HP|3000|HP|17455A and cable|HP|17355M or|Cable from|
|from computer|HP|13242N|computer|

**----- End of picture text -----**<br>

**==> picture [46 x 44] intentionally omitted <==**

**----- Start of picture text -----**<br>
¢2<br>museum<br>**----- End of picture text -----**<br>


## Cable Schematics 

**==> picture [484 x 458] intentionally omitted <==**

**----- Start of picture text -----**<br>
Connector Types Y-Cable for Eavesdrop Connection<br>Part numbers ending in M, F, or D follow this convention: | HP 17455A Computer<br>M= Male to Male Male<br>F = Female to Female 32711} 4] 5] 6| 8 | “ee 25)<br>D = Male to Female |<br>Male 7<br>Plotter i at—_|st— | |<br>(3) 217] 114] 5[6| 8] ov [25]<br>. Female<br>Terminal<br>Pins 4, 5, 6, and 8 through 25 are directly connected between the<br>computer and terminal connectors.<br>Modem Eliminator Type Straight Through<br>HP 17255D/F HP 17355M/F/D*<br>HP 13242G* Length: 1 meter<br>Length: | meter<br>0 Pin Ou<br>Br 4 ol o<br>24 Pp} 17<br>Cen p}-—3,<br>BR Oe 3<br>Pins not shown are not used. Pins 1-25 are directly connected.<br>“Other pins are connected tn this cable but they do not affect plotter *Cables HP 92222F/M are of the same pin configuration as HP<br>usage. (The HP 13242G uses male-to-male connectors. ) 17355F/M, but are only 8 inches long. (There is no HP 92222D.)<br>**----- End of picture text -----**<br>

**==> picture [499 x 530] intentionally omitted <==**

**----- Start of picture text -----**<br>
RS-232-C/CCITT V.24 HP-IB (IEEE-488)<br>Cables Cables<br>HP 13242G HP 17355M HP 10833A<br>HP 13242N HP 17455A HP 10833B<br>HP 17255D HP 92218D HP 31389A<br>HP 17255F HP 92221P HP 31389B<br>HP 17355D HP 92222F HP 455294<br>HP 17355F HP 92222M HP 45529B<br>RS-422-A Cable HP-IL Cable<br>HP 17855A HP 82167A<br>Cables are available from your local dealer or HP<br>Sales Representative. To order cables or to obtain a<br>copy of HP’s Computer Users Catalog (5953-2450),<br>which includes a complete listing of Hewlett-Packard<br>suppliestelephoneand [numbers:]  accessories,call one of HP’s Direct Order<br>United States 800-538-8787<br>California 408-738-4133<br>United Kingdom 0734-792868<br>0734-792959<br>France (6) 928 32 64<br>Belgium/Luxembourg (02) 762 32 00<br>Switzerland (057) 31 22 54<br>or 31 22 59<br>; West Germany 07031-142829<br>07031-223133<br>The Netherlands 020-470639<br>South Africa 802-5111<br>53-7954<br>28-4178<br>Canada<br>Toronto Local 416-671-8383<br>Ontario 1-800-268-6982<br>Quebec 1-800-387-3417<br>British Columbia 112-800-387-3154 ;<br>Other Provinces 1-800-387-3154<br>Sweden 08-7502027<br>08-7502028<br>Australia (03) 895-2645<br>or 895-2615<br>(02) 888-7712<br>or 887-1611<br>Apple IIc, Ie, and /i/ are products of Apple Computer, Inc. AT&T PC 6300 is aproduct of AT&T Information Systems, Inc. Compaq is a<br>product of Compaq Computer Corp. DEC Rainbow and VAX are products of Digital Equipment Corp. IBM PC, XT, AT, and PG are<br>products of International Business Machines Corp. Osborne ‘is a product af Osborne Computer Corp. TI Pro is a product of Texas<br>Instruments. Wang PC is a product ofWang Laboratories, Inc.<br>**----- End of picture text -----**<br>


For more information, call your local HP sales office listed in the tetephone directory white pages. Ask for a Personal Computer Representative. Or write to Hewlett-Packard: U.S.A. — P.O. Box 10301, Palo Alto, CA 94303-0890. Europe - P.O. Box 999, 1180 AZ Amstelveen, The Netherlands. Canada — 6877 Goreway Drive, Mississauga, L4V 1M8, Ontario. Japan — Yokogawa-Hewlett-Packard Ltd., 3-29-21, Takaido-Higashi, Suginami-ku, Tokyo 168. Elsewhere in the world, write to Hewlett-Packard Intercontinental, 3495 Deer Creek Road, Palo Alto, CA 94304. 

(11) 5953-9825 

Data Subject to Change 

Printed in U.S.A. 3/85 
