# HP_7475A_Short_Form_Feb_89


<!-- page 1 -->

<!-- image -->

## Hewlett Packard 7475A Graphics Plotter

<!-- image -->

## Control Panel

<!-- image -->

## Self-test

Basic test:

1. Make sure six pens are installed in carousel and plotter is on.
2. With paper loaded, lower PAPER LOAD lever to PAPER HOLD position.

Plotting method

Multi-pen plotter

Plotting speed

Pendown 38.1 cm/s; pen up 50.8 cm/s

Resolution

Smallest addressable move 0.025mm

Paper Handling

A3- and A4-size paper and transparency film.

Interfaces

S-232C or HP Interface Bus (HP-IB) (IEE-488)

Emulations

HP Graphics Language (HP-GL)

P1, P2 keys: On power-up, raises pen and moves it to default position (lower left) of A/A4 paper size, or raises pen and moves it to default position (lower lef B/A3 paper size. When either one is pressed together with Enter key, will establish new location of scaling point P1 or P2 .

ERROR light: Indicates plotter error condition

B/A3, A/A4 lights:

indicate current selected paper size.

PEN U/D key: Reverses the current pen state (up or down).

SIZE key: When pushed simultaneously with Enter key, selects paper size as indicated by size lights.

PEN keys: Causes plotter to retrieve same pen number from carousel.

ENTER key: Multi-use key for changing paper size and location of scaling points P1 and P2.

Cursor keys: Move pen in the direction of the arrow. Using adjacent keys will move the pen at a 45 degree angle.

FAST key: When used with any cursor key, will increase pen speed 4X.

VIEW key: Turns Error light on, suspends the pen plotting, raises pen to manually change pen and view paper. When pressed again, error light will turn off, retu to last coordinates and up or down status, and resume printing.

D/Y - In the Y position, received data is retransmitted and plotter does not unless it receives a "Plotter On" command. In the D position, plotter responds t commands.

3. Press a PEN key to select a pen and then use Cursor keys to test selected pen.

DIP Switches

- HP-IB

Switch Label

- Description

Demonstration plot - Perform the following procedure to draw a bar, pie and line chart.

ADDRESS - Five of the seven DIP switches set the HP-IB address in binary cod decimal.

1. Make sure six pens are installed in carousel and plotter is off.

A3/A4 - Selects B/A3-size or A/A4-size paper.

2. With A/M-size paper loaded, lower PAPER LOAD lever to PAPER HOLD position.
3. While holding the P1 and P2 keys, turn plotter on.

MET/US - Selects maximum plotting area. If B/A3-size paper is selected, MET selects 275x402mm and US 1 0.2x16.3 in. If A/M-size paper is selected, MET selects 192x275mm and US 7.5x10.2 in.

Baud Rate Selection * - RS-232C

|               | One Stop Bit   |    |    |    |    | Two Stop Bits   |    |    |
|---------------|----------------|----|----|----|----|-----------------|----|----|
| Baud Rate     | B4             | B3 | B2 | B1 | B4 | B3              | B2 | B1 |
| on. External  | -              | -  | -  | -  | 0  | 0               | 0  | 0  |
| 75            | -              | -  | -  | -  | 0  | 0               | 0  | 1  |
| pen 110       | -              | -  | -  | -  | 0  | 0               | 1  | 0  |
| terminate 150 | test, 0        | 0  | 1  | 1  | -  | -               | -  | -  |
| 200           | 0              | 1  | 0  | 0  | -  | -               | -  | -  |
| 300           | 0              | 1  | 0  | 1  | 1  | 0               | 1  | 1  |
| on the 600    | 0              | 1  | 1  | 0  | 1  | 1               | 0  | 0  |
| or 1200       | 0              | 1  | 1  | 1  | 1  | 1               | 0  | 1  |
| 2400          | 1              | 0  | 0  | 0  | 1  | 1               | 1  | 0  |
| 4800          | 1              | 0  | 0  | 1  | 1  | 1               | 1  | 1  |
| 9600          | 1              | 0  | 1  | 0  | -  | -               | -  | -  |

Troubleshooting test - The following procedure exercises both motor drive circuits, motors and encoders, the servo chips, error light circuit, gate arrays, microprocessor and ROM.

1. Make sure paper is loaded and plotter is on.
2. Manually move pen carriage near center of its travel.
3. Hold ENTER key while turning plotter on. The ERROR light should remain on.
4. Press &lt;-- key.
5. If successful, the ERROR light should turn on and off continuously, and pen carriage and paper should move left and right about 6.4mm continuously.
6. Press ENTER key to pause test and &lt;-- key to resume test. To terminate test, turn plotter off and back on.

## Plotter Configuration

The plotter's interface is configured through a bank of DIP switches located on the rear panel. The DIP switches will vary according to which interface (RS-232C or HP-IB) is installed. 1200

DIP Switches

- RS-232C

Switch Label

- Description

A3/A4 - Selects B/A3-size or A/M-size paper.

BAUD RATE

S1/PARITY - Toggles PARITY on and off.

*1 = switch open; 0 = switch closed.

## Common Problems and Fixes

S2/PARITY - If switch S1/PARITY is set to 1 (switch open), selects odd or even parity.

Plotter does not respond to control panel, ERROR lights is off, and the PAPE lever is In the load position:

1. Check rear-panel line fuse, voltages and power supply fuses on PCA.
2. Check 4 MHz clock and Gate Array B.

## Plotter responds to control panel but not to host:

MET/US - Selects maximum plotting area. If B/A3-size paper is selected, MET selects 275x402mm and US 1 0.2x16.3 in. If A/M-size paper is selected, MET selects 192x275mm and US 7.5x1 0.2 in.

1. Make sure interface connection is properly seated at both ends.
2. Test the I/O circuits by sending "SP1;SP2" from host.

<!-- page 2 -->

## Hewlett Packard 7475A Graphics Plotter

## Pen up/down does not work:

1. Check fuse A1F2 and pen supply voltage.
2. Check solenoid continuity.

## Diagonal lines are not straight:

## Cover Removal

1. Turn plotter off and disconnect power cord and interface cable.
2. Remove 3 screws at rear of plotter.
3. Lift rear of top cover so that the front releases from base.
1. Check for defective pen drive motor/encoder assembly (especially if diagonals askew near horizontal lines).

## Field Replaceable Units

2. Check for defective paper drive motor/encoder assembly (especially if diagonals askew near vertical lines).
3. Check for deposits on grit wheels, pinchrollers and slider rod. Clean slider rod and pinchrollers with a dry wipe.

## Critical Adjustments

Note: Before performing any of the following procedures, remove top cover (see "Cover Removal" below).

Adjusting pen height - Perform the following procedure if pen carriage assembly is disassembled or replaced.

1. Position pen holder at center of platen.
2. Use a 100mm ruler to measure distance from platen to bottom of pen holder. It should be 10.5mm.
3. Insert a 0.050 inch Allen wrench through hole at rear of pen carriage. Turn clockwise to decrease pen height or counter-clockwise to increase pen height.

## Removing pen carousel housing:

1. Disconnect pen carousel cable from J8 on main printed circuit board.
2. Remove screw that secures pen carousel housing to chassis assembly.
3. Tip pen carousel housing forward and lift it straight up.

| slider rod DESCRIPTION         | OEM P/N    |
|--------------------------------|------------|
| Damper, silicone rubber        | 07475-4000 |
| Paper drive motor assembly     | 07470-6017 |
| (see PCA-Main HP-IB            | 07475-6010 |
| PCA-Main RS-232C               | 0747506010 |
| is Pen carriage                | 5040-8650  |
| Pen drive motor assembly       | 07470-6018 |
| pen holder. Pen carousel motor | 3140-0687  |
| Pen carousel assembly          | 5061-5080  |
| Turn Pen holder                | 07475-6002 |
| height. Solenoid               | 07475-6001 |
| Spring, pen down               | 1460-1950  |

Note: Be sure to print a menu/configuration list before replacing a PCS or logic containing configuration settings.

## Removing paper drive motor assembly:

1. Disconnect paper drive motor cable {twisted pair) from J3 and flat encoder cable from J1 on main printed circuit assembly.
2. Remove pen drop shield.
3. Loosen motor clamp and remove motor from its mounting.

## Removing pen solenoid:

1. Loosen paper drive motor clamp enough to slide motor right about 3/4 inch. Lift right end of motor slightly to release motor from chassis.
2. Disconnect solenoid cable from J2 on printed circuit assembly.
3. Loosen solenoid mounting screw enough to allow solenoid removal.

## Removing pen drive motor and belt:

1. Disconnect pen drive motor cable (twisted pair) from J5 and flat encoder cable from J6 on main printed circuit assembly.
2. Remove belt tensioner by pressing down on tensioner and sliding the tang at bottom out of chassis slot.
3. Loosen pen drive motor clamp and remove motor.
4. Slide belt from pen carriage to remove it.
5. Loosen pen solenoid mounting screw and slide solenoid to the right. Remove armature and spring.
6. Slide pen lift bar just far enough right to allow belt removal.

## Removing pen carriage, pen holder, and damper:

1. Remove paper drive motor (see above).
2. Remove pen solenoid (see above).
3. Remove pen drive motor (see above)

IBM P/N:

IBM machine type:

55X3584 1538-B01, 1516-H20

4. Slide belt from pen carriage and move carriage to the left.
5. Remove end bearing cap while sliding pen lift bar to the right and out of carriage assembly.

Tech Support 800-877-7764

6. Move slider rod to the right just far enough to release left end of rod from its mounting. Slide rod to the left and out of carriage/pen holder assembly.
7. Carefully remove plastic damper from carriage and pen holder.

Note: After reassembling the above, measure the pen down force with a gram gauge before replacing the top cover. Turn plotter on. Lower a pen onto platen. Place tip of gauge under lip of pen body and make sure that pen just starts to lift with 19 +/ 10 grams. If it does not, replace the pen down spring.

## Removing printed circuit assembly:

1. Disconnect all cables from printed circuit board.
2. Remove pen carousel housing (see above).
3. Remove screw holding control panel and remove panel.
4. Remove recessed screw between pen solenoid and pen drive motor.
5. Lift right side of chassis assembly. Tabs on left side will release from base plate.
6. Remove screws or studs holding rear panel interface connector.
7. Lift front end of printed circuit assembly and remove it from base plate.

<!-- image -->

OSE

<!-- page 3 -->

## HP  7475A Color  Desktop  Plotter

## Technical  Data

## Features

- Two small-fonnat  media sizes
- Full  range  of  pen/media combinations
- High-quality output
- Strong  software support
- Hardware  compatibility
- Built-in  intelligence

The  HP  74  75A  color  desktop plotter  produces  high-quality A4/A- and  A3/B-size  color graphics  for  business  and  PC CAD applications. The HP 7475A is  ideal  for  professionals  who need the larger  drawings  for PERT charts,  flow  charts,  pro­ ject  schedules,  and  design applications. It also  produces professional-quality  color overheads  for  presentations  and colorful  summary  charts  for handouts  and reports.

## Full Bange  of Pen/Media Combinations

HP  7475A  users  can select  from paper  (regular  and  glossy),  over­ head transparency  film,  and durable  double-matte  polyester film.  Fiber-tip  pens  for  paper and transparencies come  in  10 bright colors and two tip widths. Refillable  liquid-ink  pens  are available  for  final-quality  draw­ ings  on  polyester  film.

## High-quality Output

The HP  74  75A  color  desktop plotter  combines  high resolu­ tion and excellent repeatability to ensure professional-quality output. It has  an addressable resolution of  0.025 mm (0.001 in.),  so  it  can  plot  up  to 1000 points in a one-inch line.

<!-- image -->

<!-- image -->

<!-- image -->

The one plotter  for both  CAD and color business  graphics

When commanded to return to the same point  with no  pen change,  it  does  so within 0.1 mm (0.004 in.).  This  preci­ sion  means  your  drawings  have straight  lines,  crisp  characters, circles  that  close,  and  corners that  meet.

## Strong Software Support

One  of  the  most  widely­ supported plotters  in the  world, the HP 7475A works with major  software packages from the entire spectrum  of  graphics applications-integrated soft­ ware,  business  graphics/presen­ tations,  computer-aided-design/ drafting,  scientific  and statis­ tical analysis,  project scheduling,  and  more.

## Hardware Compatibility

A  choice of  two interfaces makes it  easy  to  add  an HP  74  75A  to  almost any system-personal computers, mainframes,  even smart  instru­ ments. The HP 74  75A  comes with RS-232-C/CCI'IT V.24 and HP-m (IEEE 488-1978) inter­ face options. And with  an additional eavesdrop  cable,  the RS-232-C  plotter  can  be  con­ nected in series  between  a computer  and  a  tenninal.

<!-- page 4 -->

## Built-in  Intelligence

The  HP  7475A's  control-panel keys  can  alter  the  size  of  the drawing  area  when  switching media sizes  or  rotate  the  plot 90  degrees.  Control-panel  keys can  also  be  used  in  conjunction with  a  digitizing  sight.

Programmers  will  appreciate the  intelligence  features  which eliminate the  need for  software­ generated  characters  and  func­ tions.  Hewlett-Packard  Graphics Language  (HP-GL)  instructions (more  than  50)  govern  such tasks QS labeling,  pen  move­ ment,  and drawing  arcs  and circles.

## Thchnical Information Media Sizes

210 x 297 mm  (ISO  A4) 8I/.! x 11  in.  (ANSI  A) 297 x 420  mm  (ISO  A3) 11 x 17  in.  (ANSI B)

## Pens

Number:  6  in  carousel

Type:  Fiber-tip (paper  and transparency),  refillable  short­ body  liquid-ink

## Media

Paper  (regular  and  glossy), transparency  fi lm, double-matte polyester  fi lm

## Character  Sets

French/German, HP  9825, Scandinavian,  Spanish/Latin American,  Roman  Extensions and these  ISO  registered  sets: , ANSI  ASCII  (006),  French  (025), German (021),  International Reference  Version (002),  Italian (015),  JIS  ASCII  (014),  Katakana (013),  Norwegian  I  (060), Norwegian 11 (016),  Portuguese (016),  Spanish (017),  Swedish (010),  Swedish  for  Names  (011), United Kingdom  (004)

## Resolution

Addressable:  0.025 mm (0.001  in.) Mechanical:  0.025 mm

(0.001  in.)

## Repeatability

With a  given pen:  0.1  mm (0.004  in.)

Pen  to  pen:  0.2  mm  (0.008  in.)

## Pen Velocity

Pen  down,  maximum:  38.1  cm/s (15.0  in./s)

Pen  up:  50.8  cm/s  (20.0  in'/s)

Programmable:  approximately 0.4 to 38.1 cmls (0.2 to 15.0  in'/s) in  increments  of  0.4  cm/s

## Acceleration

Approximately  2  g

## Maximum  Plotting  Area

Pen axis: 258.0  mm (10.2  in.) for  A/B;  275.0  mm  (10.8  in.)  for A4/A3

Paper axis: 198.0  mm  (7.80  in.) for  A;  192.0  mm  (7.56  in.)  for A4;  414.0  mm  (16.3  in.)  for  B; 402.0  mm  (15.8  in.)  for  A3

## Buffer Size

1024 bytes

## Environmental Ranges

## Thmperature

Operating:  0  to  55  degrees  C (32  to  131  degrees  F)

Storage:  -40  to  75  degrees  C

(-40  to  167  degrees  F)

Humidity Operating:  5  to  95%  (at  40

degrees  C)

## Power  Requirements

Source:  100,  120,220,  240  V, -10%,  +5%

Frequency:  48-66  Hz

Consumption:  35 W maximum

## Physical  Specifications

Height:  127.0  mm  (5.0  in.)

Width:  568.0 mm (22.4 in.)

Depth:  367.0

mm (14.5  in.)

Net  weight:  7.0  kg  (16.0  lb)

Shipping  weight:  approx. 11.0  kg  (25.0  lb)

## Product  Certifications

FCC  certified  to  conform  to limits  set  for  radio  frequency when used  with  a  Class B  com­ puting  device;  meets  or  exceeds IEC-380,  IEC-435,  IEC-478,  and CSA  C22.2  No.  154.

<!-- page 5 -->

## Interface  and Cable  Requirements

|                                                                                                                             | Cable                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| HP Vectra PC with HP 24540AlB seriaVparaliel interface card or HP 24541AlB dual serial interface card using 9-pin connector | HP 24542G                                                               |
| HP Vactra PC with HP 24541AlB dual serial interface card using 25-pin connector                                             | HP 17255M                                                               |
| HP Touchscreen PC using serial interface                                                                                    | HP 17255M                                                               |
| HP Touchscreen PC using HP-IB interface                                                                                     | HP 10833A (1.0 mJ HP 10833B 12.0 ml HP 10833C 13.0 m) HP 10833D 10.5 mJ |
| HP 3000 or DEC VAX in eavesdrop configuration                                                                               | HP 17455A                                                               |
| IBM PS/2, ' PC, PC-Xl, and compatibles                                                                                      | HP 17255D                                                               |
| IBM AT and compatibles                                                                                                      | HP 24542G                                                               |
| Apple Macintosh 128K and 512K                                                                                               | HP 92219M                                                               |
| Apple Macintosh SE, Macintosh Plus, and Macintosh 11                                                                        | HP 17302A                                                               |
| Apple lie                                                                                                                   | HP 17355M                                                               |

## Ordering Information

## Standard Unit

7475A

Color  desktop  plotter

## Option  numbers:

001

RS-232-C/CCI'IT  V.24

interface

HP-IB  (IEEE  488-1978)

002

interface

Note: Interface  cables  must  be ordered  separately

## Accessories Included

Operation and  Interconnection

Manual (language  appropriate

to plotter  destination)

Reference  Card

Power cord (appropriate  to

plotter  destination)

Plotter  paper

50

sheets,  A4/A size (paper

sizes  determined by  plotter

destination)

Transparency  film  sampler, A4/A size  (film  sizes  deter­ mined by plotter  destination)

Six-pen carousel  for  fiber-tip pens

Assorted fiber-tip  paper  and transparency pens

HP  Plotter  Supplies  Catalog

## Accessories Available

07475·90000

07475·90001

5061·5080

07475-60030

Hardware  Suppan  Manual

Interfacing/Programming  Manual

Additional  fiber  ·tip  pen  carousel

liquid�nk drafting  pen  carousel

For  a  complete  list  of  available supplies,  check  the  current  ver­ sion of  the  HP  Plotter  Supplies Catalog or  the  Hewlett-Packard PC Peripherals  Price  Guide.

<!-- page 6 -->

United  States: Hewlett-Pa.ckard Company 4  Choke Cherry Road Rockville,  MD 20850 301 670 4300

Hewlett-Packard Company 5201  Tollview  Drive Rolling Meadows,  IL  60008 312 255 9800

Hewlett-Packard Company 5161 Lankershim Blvd. No. Hollywood, CA 91601 818 505 5600

Hewlett Packard Company 2015 South  Park  Place Atlanta,  GA 30339 404 955 1500

## Canada:

Hewlett-Packard Ltd. 6877  Goreway  Drive Mississauga,  Ontario L4VIM8 416 678 9430

## AustralialNew Zealand:

Hewlett-Packard Australia Ltd. 31-41 Joseph Street Blackburn,  Victoria 3130 Melbourne,  Australia 03 895 2895

<!-- image -->

Europel  AfricalM.lddle East: Hewlett-Packard S.A. Central Mailing Department P.O.  Box 529 1180 AM Amstelveen The  Netherlands 31 20/547  9999

## Far East:

Hewlett-Packard Asia  Ltd. 221F  Bond Centre West Tower 89 Queensway Central,  Hong Kong 5 848 7777

## Japan:

Yokogawa Hewlett-Packard  Ltd. 29-21,  Takaido-Higashi  3-chome Suginami-ku,  Tokyo  168 03 331 6111

## Latin America:

Latin  American Region Headquarters Monte Pelvoux Nbr.  111 Lomas de Chapultepec 11000 Mexico D.F.,  Mexico 905 596 79 33

Technical information in tbis doclUllent is subject to change  without  notice.

Copyright ©  1989 Hewlett-Packard Company

<!-- page 7 -->

- Low cost,  high performance
- Choice of six- or two-pen models
- Plot on  paper
- Plot on  HP overhead transparency film

<!-- image -->

Hewlett-Packard's HP 7470A and 7475A graphics plotters provide the kind of graphics excellence you would expect to find only in much more expensive plotters.  They feature the same high-quality compo­ nents  and  innovative  paper-moving  technology  which  were  intro­ duced in  HP's drafting  plotters and  which  make  it  possible  to  offer high performance plotters at affordable prices. Refer to the table be­ low  for  a  quick  comparison  of  the  main  features  available  in  each plotter.

| Features            | HP 7475A                                                                                                                       | HP 7470A                                                                                                                       |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Media sizes         | Two ANSI sizes: A (8.5 x 11 in.) and B (11 x 17 in.) Two ISO sizes: A4 (210 x 297 mm) and A3 (297 x 420 mm)                    | One ANSI size: A (8.5 x 11 in.) One ISO size: A4 (210 x 297 mm)                                                                |
| Pans                | Six fiber·tip; programmable pen selection; automatic capping                                                                   | Two fiber·tip; programmable pen selection; automatic capping                                                                   |
| HP-Cl Instructions  | More than 50 instructions                                                                                                      | More than 40 instructions                                                                                                      |
| Character sets      | 19 sets. including ISO European standards and Katakana                                                                         | Five sets                                                                                                                      |
| Standard Interfaces | HP·IB (IEEE 488-1978) or RS-232.c (CCITT V.24)                                                                                 | HP-IB (IEEE 488-1978) or RS-232.c (CCITT V.24) or HP-IL                                                                        |
| Standard Interfaces | Each plotter incorporates one permanent interface option.                                                                      | Each plotter incorporates one permanent interface option.                                                                      |
| Technology          | Both plotters use the same micro-grip drive for paper movement and have the same high resolution. repeatability, and velocity. | Both plotters use the same micro-grip drive for paper movement and have the same high resolution. repeatability, and velocity. |

## computer Applications

The  HP  7470A  and  7475A  provide hardcopy computer graphics for  technical,  scientific,  and  business  applications.  Colorful  A4/ A-size  charts  and  graphs  are  ideal  for  reports  and  overhead  trans­ parencies. Use them for summarizing data, identifying trends,  com­ paring results, and focusing on exceptions. The larger A3/B-size plots that can be drawn on the HP 7475A are particularly  useful for time lines,  PERT charts,  schematics,  engineering  drawings,  and other ap­ plications where you need to show visual detail.

## Measurement Applications

The  HP  7470A  and  7475A  add  hard  copy  graphics  capability  to intelligent  instruments  and  instrument  systems  with  HP-IB  (IEEE 488-1978).  For  most  applications  that  use  a  display  screen  and  an oscilloscope  camera,  these  plotters  can  produce  high-quality  hard­ copy of  the screen  for a  cost  that is  substantially  lower  than  camera film.  Because  they  plot directly  from measured data,  they eliminate problems  created  by  distortion  from  the  screen.  And  plotter  output provides  better  visual  resolution  than  photographs.  Many  systems without  screen  displays  can  also  have  the  benefits  of  HP  7470A  or 7475A hardcopy graphics at very little additional cost.

## Easy to Use

When the HP 7475A or 7470A plotters are turned on, default con­ ditions are automatically  established for most plotting parameters. In many cases, it is only necessary to load the pens and plotting medium in order to start plotting.

Media and pen loading are also easy.  A guide control lever makes media  alignment  perfect every  time. The front  panel  can  be used to select pens, to halt the program for exchanging pen colors, or to move the plot forward to "view" what you have plotted.

The front  panel  also  allows  easy  access  to  the  plotter's  digitizing capability  and  scaling  points.  And,  on  the  HP  7475A,  push  buttons can rotate plots 90 degrees or run a demonstration plot directly from the plotter.

## Intelligence Features

Intelligence  features  are  built  directly  into  these  plotters  to  save you  time  by  eliminating  the  need for  software-generated  characters and  functions.  Many  HP-GL  instructions  (more  than  50  in  the  HP 7475A; more than 40 in the HP 7470A) govern such tasks as labeling, pen  movement, drawing arcs and circles,  and selecting  from a  large variety  of  character  sets.  The  HP  7475A  has  19  character  sets  in-

## COMPUTER PERIPHERALS

Graphics Plotters Models 7470A and 7475A

<!-- image -->

<!-- page 8 -->

<!-- image -->

## COMPUTER PERIPHERALS

## Graphics Plotters

Model 7470A and 7475A (cont'd)

cluding ISO European  sets, Katakana,  ASCII, and Roman 8 exten­ sions; the HP 7470A has five internal character sets.

The HP 7475A's extra HP-GL instructions, which are used for fill­ ing rectangles and wedges for pie and bar charts, provide an enhance­ ment especially designed for professional graphics.

## Writing Systems

The  HP  7470A has  two  built-in pen  stalls  which  make two-color plotting easy. For plots with more than two colors, the program can be halted through program or front panel control; new pens can then be installed and plotting resumed. The HP 7475A's six-pen carousel al­ lows you  to  store up  to six  different pen colors  or a variety  of colors and widths.

Several automatic features are included to protect the tip of the pen and increase pen life. When housed in the stall or carousel, the pen is capped to prevent premature drying.  When  a pendown command is given,  the  pen  force  is  damped and the pen  is gently lowered to  the plotting surface.

## High-Quality Output

The HP 7470A and 7475A have an addressable step size of 0.025

## Specifications

mm (0.001 in.). With this resolution, they can plot up to 1000 points in a  I-inch line. When commanded to return to the same point with no pen change, they achieve this repeatability within 0.1 mm (0.004 in.) Because of this outstanding resolution and repeatability, both plotters produce  straight  lines  and  smooth circles  that  have  an  artist-drawn appearance.

## Interface Options

The HP 7475A and 7470A are easy to interface with most HP and non-HP  computers. Both plotters  offer the  RS-232-C/CCITT  V.24 or  HP-IB  (IEEE 488-1978) interface.  With the RS-232-C option, a dual input/output cable is available for connecting the plotters with a terminal and computer.  In addition, the HP 7470A offers a third in­ terface  option,  HP-IL.  This  interface  is  used  to  connect  the  plotter with low-cost,  portable HP systems.

## Graphics Software

HP offers a full line of graphics software packages for use on most HP computer products. And software is also available for many non­ HP computers. These packages make it easy for non-programmers to use the HP 7470A and 7475A plotters.  Details are available from any HP sales and support office.

|                             | HP 7475A                                                                                                                                                                                                                           | HP 7470A                                                                                                                                                                                          |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resolution                  | Smallest addressable step size: 0.025 mm (0.001 in.)                                                                                                                                                                               | Smallest addressable step size: 0.025 mm (0.001 in.)                                                                                                                                              |
| Repeatablllty               | With a given pen: 0.1 mm (0.004 in.) From pen to pen: 0.2 mm (0.008 in.)                                                                                                                                                           | With a given pen: 0.1 mm (0.004 in.) From pen to pen: 0.2 mm (0.008 in.)                                                                                                                          |
| Pen velocity (each axis)    | Pen up,50.8 cmfs (20 in.fs); pen down,maximum -38.1 cmfs (15 in.fs),programmable -Ito 38 cmfs in I cmfs increments                                                                                                                 | Pen up,50.8 cmfs (20 in.fs); pen down,maximum -38.1 cmfs (15 in.fs),programmable -Ito 38 cmfs in I cmfs increments                                                                                |
| Acceleration                | Approximately 2 g's                                                                                                                                                                                                                | Approximately 2 g's                                                                                                                                                                               |
| Envtronmental range         | Operating,O'C to 55'C Non'operating,-4O'C to 75'C                                                                                                                                                                                  | Operating,O'C to 55'C Non'operating,-4O'C to 75'C                                                                                                                                                 |
| Plotting area X·axis Y·axis | 258 mm (10.2 in.), AlB 275 mm(10.8 in.), MfA3 198 mm (7.80 in.),A 192 mm (7.56 in.),M 414 mm (16.3 in.),B 402 mm (15.8 in.),A3                                                                                                     | 191 mm (7.5 in.) A 191 mm (7.5 in.),A4 257 mm (10.2 in.), A 272 mm (10.7 in.), A4                                                                                                                 |
| Interfaces                  | HP-IB (IEEE 488-1978),implements the following HP-IB functions as defined in IEEE 488-1978: SHI, AHI, T2, TEO, LEO, SRI,RLO,DCI, DTO,L2, ppo, (listen only or address less than 7, otherwise PP2)                                  | HP-IB (IEEE 488-1978),implements the following HP-IB functions as defined in IEEE 488-1978: SHI, AHI, T2, TEO, LEO, SRI,RLO,DCI, DTO,L2, ppo, (listen only or address less than 7, otherwise PP2) |
| Interfaces                  | R5-232-GfCCITI,asynchronous serial ASCII with switch selectable baud rates of 75, 1l0,150,200,300,600,1200, 2400, 4800, 9600. External clock input capabilities with intermediate baud rates of up to 9600 baud. 1024 byte buffer. | Same as HP 7475A except 255 byte buffer.                                                                                                                                                          |
| Interfaces                  | R5-232-GfCCITI,asynchronous serial ASCII with switch selectable baud rates of 75, 1l0,150,200,300,600,1200, 2400, 4800, 9600. External clock input capabilities with intermediate baud rates of up to 9600 baud. 1024 byte buffer. | HP-IL,Hewlett-Packard Interface Loop for use with portable systems.                                                                                                                               |
| Power Requirements          | Source: 100, 120, 200,240 v� -10%,+5% Frequency: 48-S6 Hz                                                                                                                                                                          | Source: 100, 120, 200,240 v� -10%,+5% Frequency: 48-S6 Hz                                                                                                                                         |
| Power Requirements          | Consumption: 35 W maximum                                                                                                                                                                                                          | Consumption: 25 W maximum                                                                                                                                                                         |
| Size: Height Width Depth    | 127 mm (5 in.) 568 mm (22.4 in.) 367 mm (14.5 in.)                                                                                                                                                                                 | 127 mm (5 in.) 432 mm (17 in.) 343 mm (13.5 in.)                                                                                                                                                  |
| Weight: Net Shipping        | 7 kg (16.0 Ib) Approx. II kg (25.0 Ib)                                                                                                                                                                                             | 6 kg (13.5 Ib) Approx. 10 kg (22.0 Ib)                                                                                                                                                            |
| FCC                         | FCe certified to conform to limits set for radio frequency interference when used with a Class B computing device.                                                                                                                 | FCe certified to conform to limits set for radio frequency interference when used with a Class B computing device.                                                                                |

## Accessories  Supplied

## HP 7475A

HP 07475-90001 Interfacing and Programming Manual

HP 07475-90002

Operation and Interconnection Manual

HP 07475-90004

## HP 7470A

HP 07470-90001 Interfacing and Programming Manual

HP 07470-90002 Operator's Manual

HP 07470-90003

Interconnection Guide

HP 07470-90004

Reference Card

Power cords and an assortment of pens and drawing media  are also supplied with the plotters. The media size and the appropriate power cord are determined by plotter destination. The HP-IL cable (V2-me­ tre) is  supplied with Option 003 only.

Note: Interface cables  are not  supplied with Option 001 and  Option 002 plotters.

Reference Card

| Ordering Information                                                                                                         | Price   |
|------------------------------------------------------------------------------------------------------------------------------|---------|
| Options                                                                                                                      |         |
| 001 RS-232-C/CCITT V.24 (cable not included)                                                                                 | N/C     |
| 002 HP-IB (IEEE 488-1978) (cable not included)                                                                               | N/C     |
| 003 HP-IL for 7470A only (cable included)                                                                                    | N/C     |
| Note: Option 001, 002, or 003 must be specified when ordering HP 7470A; Option 001 or 002 must be speci­ fied with HP 7475A. |         |
| Interface Cables                                                                                                             |         |
| HP 13242G Male-male, special RS-232-C cable for use with Option 001, HP 150 Personal Computer                                | $69     |
| HP 172550 Male-female, special RS-232-C cable for use with Option 001, IBM Personal Computers                                | $50     |
| HP 17355F Male-male standard cable for use with Op­ tion 001                                                                 | $52.50  |
| HP 17455A Eavesdrop cable for use with Option 001                                                                            | $75     |
| HP 10833A or HP45529A or HP 31389A HP-IB                                                                                     | $81     |
| I-metre cable for use with Option 002 HP 82167A HP-IL Y2-metre cable (included with Op­ tion 003)                            | $6      |
| Plotters                                                                                                                     |         |
| HP 7470A Two-pen Graphics Plotter                                                                                            | $1095   |
| HP 7475A Six-pen Graphics Plotter                                                                                            | $1895   |

<!-- page 9 -->

## Interface Cables for HP Graphics P. and Personal Printers lotters

'TECHNICAL DATA, MARCH 1985

Most HP plotters are not shipped with an interface cable. Hewlett-Packard graphics plotters (HP 7470A, 7475A, 7550A), drafting plotters (HP 7580B, 7585B, 7586B), and personal printers (HP Laserjet, HP Thinkjet) can be used with a variety of HP and non-HP personal computers and computer systems. However, because different configurations often require different interface cables, customers must order the appropriate cable separately.

To find the proper cable to connect your plotter or printer to your personal computer, check the table below. To determine the proper cable for other configurations (such as connecting your plotter or printer to a mainframe computer terminal), consult the tables on Page 2. Cable schematics appear on Page 3. For ordering information, see Page 4.

<!-- image -->

<!-- image -->

## Standalone Configurations:

Ina standalone configuration, the plotter/printer is connected to its own dedicated computer port. This setup is primarily for personal computers in workstation environments, but also includes peripherals on their own computer port in mainframe environments.

Note: Cables from non-HP computer manufacturers are listed for information purposes only. Check with the manufacturer for current model numbers and prices.

| Printer/Plotter to Personal Computer, Standalone (RS-232-C)   | Printer/Plotter to Personal Computer, Standalone (RS-232-C)   | Printer/Plotter to Personal Computer, Standalone (RS-232-C)   | Printer/Plotter to Personal Computer, Standalone (RS-232-C)   |
|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Computer System                                               | HP Laserjet HP Thinkjet                                       | HP 7470A, 7475A, 7580B, 7585B, 7586B                          | HP 7550A                                                      |
| HP Series 150, TI Pro, Wang PC                                | HP 13242G                                                     | HP 13242G                                                     | HP 17255D                                                     |
| The HP PORTABLE                                               | HP 92221P                                                     |                                                               | HP 92221P and HP 17355F*                                      |
| IBM PC and PC/XT, Compaq, AT&T PC 6300                        |                                                               | HP 17255D                                                     | HP 17255F                                                     |
| IBM AT                                                        | HP 17255D and IBM 6450242 Serial Adapter Cable                | HP 17255D and IBM 6450242 Serial Adapter Cable                | HP 17255F and IBM 6450242 Serial Adapter Cable                |
| IBM PCr                                                       | HP 17255D and IBM Serial Device Adapter Cable                 | HP 17255D and IBM Serial Device Adapter Cable                 | HP 17255F and IBM Serial Device Adapter Cable                 |
| Apple Ie, DEC Rainbow, Osborne                                | HP 17355M.                                                    | HP 17355M                                                     | HP 17355D                                                     |
| Apple //I                                                     | HP 17355M"** and Apple A3M0019                                | HP 17355M** and Apple A3M0019                                 | HP 17355D and Apple A3M0019                                   |
| Apple IIc                                                     | Apple A9C0308                                                 | Apple A9C0308                                                 | HP 17355F* and Apple A9C0308                                  |

<!-- page 10 -->

| Printer/Plotter to Personal Computer (HP-IB/IEEE-488)   | Printer/Plotter to Personal Computer (HP-IB/IEEE-488)   | Printer/Plotter to Personal Computer (HP-IB/IEEE-488)   |
|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Computer System                                         | HP 7470A, 7475A, 7550A, 7580B, 7585B, 7586B             |                                                         |
| HP Series 80, HP Series 150, HP 9000 Series 200, 500    | HP 45529A/B or HP 10833A/B or HP 31389A/B               |                                                         |

| Plotter to Mainframe, Standalone (RS-422-A)   | Plotter to Mainframe, Standalone (RS-422-A)   |
|-----------------------------------------------|-----------------------------------------------|
| L Computer System                             | HP 7550A only                                 |
| HP 3000 Series 64, 39, 42, 48                 | HP 17855A                                     |

## Eavesdrop Configurations:

In an eavesdrop configuration, the plotter is situated between a mainframe computer (i.e., HP 3000, IBM 360/370, DEC VAX) and a terminal or a personal computer being used as a terminal. Both the terminal and plotter share the same RS232-C port from the mainframe computer.

To use an HP 7550A, 7580B, 7585B, or 7586B in eavesdrop mode, the only additional cable required in most configura-

| Printer to Mainframe, Standalone (RS-232-C)   | Printer to Mainframe, Standalone (RS-232-C)   |
|-----------------------------------------------|-----------------------------------------------|
| Computer System                               | HP Laserjet only                              |
| HP 3000 Series 37 ATP                         |                                               |

|

| rs Plotter to Calculator/Handheld Computer             | rs Plotter to Calculator/Handheld Computer   |
|--------------------------------------------------------|----------------------------------------------|
|                                                        | HP 7470A only                                |
| HP Series 40 Calculator HP Series 70 Handheld Computer | HP 82167A                                    |

tions is the one from the plotter to the mainframe computer. These plotters have two RS-232-C ports, so the terminal to mainframe computer cable is used with the second RS-232-C port on the plotter.

When connecting an HP 7470A or 7475A in eavesdrop mode, a special eavesdrop cable (HP 17455A) is required in addition to the cable from the plotter to the mainframe computer.

| Eavesdrop Configuration (RS-232-C)   | Eavesdrop Configuration (RS-232-C)   | Eavesdrop Configuration (RS-232-C)   | Eavesdrop Configuration (RS-232-C)   |
|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
| Computer System                      | HP 7470A, 7475A                      | HP 7580B, 7585B, 7586B               |                                      |
| HP Series 150 (in terminal mode)     | HP 17455A and HP 13242N              | HP 17355M or HP 13242N               | HP 17355M or HP 13242N               |
|                                      | HP 17455A and cable from computer    | HP 17355M or HP 13242N               |                                      |

<!-- page 11 -->

## Cable Schematics

<!-- image -->

<!-- image -->

<!-- page 12 -->

| Ordering Information                                                                                                                                                                                                                                                                    | Ordering Information                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RS-232-C/CCITT V.24                                                                                                                                                                                                                                                                     | HP-IB (IEEE-488) Cables                                                                                                                                                                                                                                                                 |
| Cables HP 13242G HP 17355M HP 13242N HP 17455A HP 17255D HP 92218D                                                                                                                                                                                                                      | HP 10833A HP 10833B                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                         | HP 31389A                                                                                                                                                                                                                                                                               |
| HP 17255F HP 92221P                                                                                                                                                                                                                                                                     | HP 31389B                                                                                                                                                                                                                                                                               |
| HP 17355D HP 92222F                                                                                                                                                                                                                                                                     | HP 45529A                                                                                                                                                                                                                                                                               |
| HP 17355F HP 92222M                                                                                                                                                                                                                                                                     | HP 45529B                                                                                                                                                                                                                                                                               |
| RS-422-A Cable                                                                                                                                                                                                                                                                          | HP-IL Cable                                                                                                                                                                                                                                                                             |
| HP 17855A                                                                                                                                                                                                                                                                               | HP 82167A                                                                                                                                                                                                                                                                               |
| Cables are available from your local dealer or HP Sales Representative. To order cables or to obtain a copy of HP’s Computer Users Catalog (5953-2450), which includes a complete listing of Hewlett-Packard supplies and accessories, call one of HP’s Direct Order telephone numbers: | Cables are available from your local dealer or HP Sales Representative. To order cables or to obtain a copy of HP’s Computer Users Catalog (5953-2450), which includes a complete listing of Hewlett-Packard supplies and accessories, call one of HP’s Direct Order telephone numbers: |
| United States California                                                                                                                                                                                                                                                                | 800-538-8787 408-738-4133                                                                                                                                                                                                                                                               |
| United Kingdom France                                                                                                                                                                                                                                                                   | 0734-792868 0734-792959 (6) 928 32 64                                                                                                                                                                                                                                                   |
| Belgium/Luxembourg Switzerland                                                                                                                                                                                                                                                          | (02) 762 32 00 (057) 31 22 54                                                                                                                                                                                                                                                           |
| West Germany                                                                                                                                                                                                                                                                            | or 31 22 59 07031-142829 07031-223133                                                                                                                                                                                                                                                   |
| The Netherlands South Africa                                                                                                                                                                                                                                                            | 020-470639 802-5111                                                                                                                                                                                                                                                                     |
| Canada                                                                                                                                                                                                                                                                                  | 53-7954 28-4178                                                                                                                                                                                                                                                                         |
| Toronto                                                                                                                                                                                                                                                                                 | 416-671-8383 1-800-268-6982 1-800-387-3417                                                                                                                                                                                                                                              |
| Local Ontario Quebec British Columbia Other Provinces Sweden Australia                                                                                                                                                                                                                  | 112-800-387-3154 1-800-387-3154 08-7502027 08-7502028 (03) 895-2645 or 895-2615 (02) 888-7712                                                                                                                                                                                           |

Apple Ile, Ie, and /#! are products of Apple Computer, Inc. AT&amp;T PC 6300 is a product of AT&amp;T Information Systems, Inc. Compaq is a product of Compaq Computer Corp. DEC Rainbow and VAX are products of Digital Equipment Corp. IBM PC, XT, AT, and PGjr are products of International Business Machines Corp. Osborne is a product of Osborne Computer Corp. TI Pro is a product of Texas Instruments. Wang PC is a product of Wang Laboratories, Inc.

For more information, call your local HP sales office listed in the tetephone directory white pages. Ask for a Personal Computer Representative. Or write to Hewlett-Packard: U.S.A. — P.O. Box 10301, Palo Alto, CA 94303-0890. Europe -P.O. Box 999, 1180 AZ Amstelveen, The Netherlands. Canada — 6877 Goreway Drive, Mississauga, L4V 1M8, Ontario. Japan — Yokogawa-Hewlett-Packard Ltd., 2021, Fakaido Higashi), Suginami-ku, Tokyo 168. Elsewhere in the world, write to Hewlett-Packard Intercontinental, 3495 Deer Creek Road, Palo Alto, CA 94304.
