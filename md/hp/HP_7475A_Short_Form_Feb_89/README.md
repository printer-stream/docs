OSE                                                Hewlett Packard 7475A Graphics Plotter

                                                                                                 Plotting method             Multi-pen plotter

                                                                                                 Plotting speed              Pendown 38.1 cm/s; pen up 50.8 cm/s

                                                                                                 Resolution                  Smallest addressable move 0.025mm

                                                                                                 Paper Handling              A3- and A4-size paper and transparency film.

                                                                                                 Interfaces                  S-232C or HP Interface Bus (HP-IB) (IEE-488)

                                                                                                 Emulations                  HP Graphics Language (HP-GL)



Control Panel
                                                                                                 ERROR light: Indicates plotter error condition
                                                                                                 B/A3, A/A4 lights: indicate current selected paper size.
                                                                                                 P1, P2 keys: On power-up, raises pen and moves it to default position (lower
                                                                                                 left) of A/A4 paper size, or raises pen and moves it to default position (lower left) of
                                                                                                 B/A3 paper size. When either one is pressed together with Enter key, will establish
                                                                                                 new location of scaling point P1 or P2.
                                                                                                 PEN U/D key: Reverses the current pen state (up or down).
                                                                                                 SIZE key: When pushed simultaneously with Enter key, selects paper size as
                                                                                                 indicated by size lights.
                                                                                                 PEN keys: Causes plotter to retrieve same pen number from carousel.
                                                                                                 ENTER key: Multi-use key for changing paper size and location of scaling points
                                                                                                 P1 and P2.
                                                                                                 Cursor keys: Move pen in the direction of the arrow. Using adjacent keys will
                                                                                                 move the pen at a 45 degree angle.
                                                                                                 FAST key: When used with any cursor key, will increase pen speed 4X.
                                                                                                 VIEW key: Turns Error light on, suspends the pen plotting, raises pen to manu-
                                                                                                 ally change pen and view paper. When pressed again, error light will turn off, return
                                                                                                 to last coordinates and up or down status, and resume printing.



Self-test
Basic test:                                                                                      D/Y - In the Y position, received data is retransmitted and plotter does not respond
 1.   Make sure six pens are installed in carousel and plotter is on.                            unless it receives a "Plotter On" command. In the D position, plotter responds to all
                                                                                                 commands.
 2.   With paper loaded, lower PAPER LOAD lever to PAPER HOLD position.
                                                                                                 DIP Switches - HP-IB
 3.   Press a PEN key to select a pen and then use Cursor keys to test selected
      pen.                                                                                       Switch Label - Description
Demonstration plot - Perform the following procedure to draw a bar, pie and line                 ADDRESS - Five of the seven DIP switches set the HP-IB address in binary coded
chart.                                                                                           decimal.
 1.   Make sure six pens are installed in carousel and plotter is off.
                                                                                                 A3/A4 - Selects B/A3-size or A/A4-size paper.
 2.   With A/M-size paper loaded, lower PAPER LOAD lever to PAPER HOLD posi-
      tion.                                                                                      MET/US - Selects maximum plotting area. If B/A3-size paper is selected, MET
                                                                                                 selects 275x402mm and US 1 0.2x16.3 in. If A/M-size paper is selected, MET
 3.   While holding the P1 and P2 keys, turn plotter on.
                                                                                                 selects 192x275mm and US 7.5x10.2 in.
Troubleshooting test - The following procedure exercises both motor drive circuits,
                                                                                                 Baud Rate Selection * - RS-232C
motors and encoders, the servo chips, error light circuit, gate arrays, microprocessor
and ROM.                                                                                                         One                                         Two
 1.   Make sure paper is loaded and plotter is on.                                                               Stop Bit                                    Stop Bits
 2.   Manually move pen carriage near center of its travel.                                      Baud Rate       B4            B3       B2       B1   B4     B3             B2     B1
 3.   Hold ENTER key while turning plotter on. The ERROR light should remain on.                 External        -             -        -        -    0      0              0      0
 4.   Press <-- key.
                                                                                                 75              -             -        -        -    0      0              0      1
 5.   If successful, the ERROR light should turn on and off continuously, and pen
      carriage and paper should move left and right about 6.4mm continuously.                    110             -             -        -        -    0      0              1      0

 6.   Press ENTER key to pause test and <-- key to resume test. To terminate test,               150             0             0        1        1    -      -              -      -
      turn plotter off and back on.                                                              200             0             1        0        0    -      -              -      -
                                                                                                 300             0             1        0        1    1      0              1      1
Plotter Configuration
                                                                                                 600             0             1        1        0    1      1              0      0
The plotter's interface is configured through a bank of DIP switches located on the
rear panel. The DIP switches will vary according to which interface (RS-232C or                  1200            0             1        1        1    1      1              0      1
HP-IB) is installed.                                                                             2400            1             0        0        0    1      1              1      0
DIP Switches - RS-232C                                                                           4800            1             0        0        1    1      1              1      1
Switch Label - Description                                                                       9600            1             0        1        0    -      -              -      -
A3/A4 - Selects B/A3-size or A/M-size paper.
                                                                                                 *1 = switch open; 0 = switch closed.
BAUD RATE
S1/PARITY - Toggles PARITY on and off.                                                           Common Problems and Fixes
S2/PARITY - If switch S1/PARITY is set to 1 (switch open), selects odd or even                   Plotter does not respond to control panel, ERROR lights is off, and the PAPER
parity.                                                                                          lever is In the load position:
MET/US - Selects maximum plotting area. If B/A3-size paper is selected, MET                       1.    Check rear-panel line fuse, voltages and power supply fuses on PCA.
selects 275x402mm and US 1 0.2x16.3 in. If A/M-size paper is selected, MET                        2.    Check 4 MHz clock and Gate Array B.
selects 192x275mm and US 7.5x1 0.2 in.
                                                                                                 Plotter responds to control panel but not to host:
                                                                                                  1.    Make sure interface connection is properly seated at both ends.
                                                                                                  2.    Test the I/O circuits by sending "SP1;SP2" from host.



September 1995       Copyright IBM Corporation 1995.
All rights reserved.                                                                     HP-37                                                                                          1
Hewlett Packard 7475A Graphics Plotter                                                                                                                                   OSE

Pen up/down does not work:
 1.   Check fuse A1F2 and pen supply voltage.                                                    Cover Removal
 2.   Check solenoid continuity.                                                                  1.   Turn plotter off and disconnect power cord and interface cable.
Diagonal lines are not straight:                                                                  2.   Remove 3 screws at rear of plotter.
 1.   Check for defective pen drive motor/encoder assembly (especially if diagonals               3.   Lift rear of top cover so that the front releases from base.
      askew near horizontal lines).
 2.   Check for defective paper drive motor/encoder assembly (especially if diag-                Field Replaceable Units
      onals askew near vertical lines).
 3.   Check for deposits on grit wheels, pinchrollers and slider rod. Clean slider rod           DESCRIPTION                                                OEM P/N
      and pinchrollers with a dry wipe.                                                          Damper, silicone rubber                                    07475-4000
                                                                                                 Paper drive motor assembly                                 07470-6017
Critical Adjustments
                                                                                                 PCA-Main HP-IB                                             07475-6010
Note: Before performing any of the following procedures, remove top cover (see
"Cover Removal" below).                                                                          PCA-Main RS-232C                                           0747506010
Adjusting pen height - Perform the following procedure if pen carriage assembly is               Pen carriage                                               5040-8650
disassembled or replaced.
                                                                                                 Pen drive motor assembly                                   07470-6018
 1.   Position pen holder at center of platen.
 2.   Use a 100mm ruler to measure distance from platen to bottom of pen holder.                 Pen carousel motor                                         3140-0687
      It should be 10.5mm.                                                                       Pen carousel assembly                                      5061-5080
 3.   Insert a 0.050 inch Allen wrench through hole at rear of pen carriage. Turn                Pen holder                                                 07475-6002
      clockwise to decrease pen height or counter-clockwise to increase pen height.
                                                                                                 Solenoid                                                   07475-6001
Removing pen carousel housing:
 1.   Disconnect pen carousel cable from J8 on main printed circuit board.                       Spring, pen down                                           1460-1950

 2.   Remove screw that secures pen carousel housing to chassis assembly.                        Note: Be sure to print a menu/configuration list before replacing a PCS or logic
 3.   Tip pen carousel housing forward and lift it straight up.                                  containing configuration settings.
Removing paper drive motor assembly:
 1.   Disconnect paper drive motor cable {twisted pair) from J3 and flat encoder
      cable from J1 on main printed circuit assembly.
 2.   Remove pen drop shield.
 3.   Loosen motor clamp and remove motor from its mounting.
Removing pen solenoid:
 1.   Loosen paper drive motor clamp enough to slide motor right about 3/4 inch.
      Lift right end of motor slightly to release motor from chassis.
 2.   Disconnect solenoid cable from J2 on printed circuit assembly.
 3.   Loosen solenoid mounting screw enough to allow solenoid removal.
Removing pen drive motor and belt:
 1.   Disconnect pen drive motor cable (twisted pair) from J5 and flat encoder cable
      from J6 on main printed circuit assembly.
 2.   Remove belt tensioner by pressing down on tensioner and sliding the tang at
      bottom out of chassis slot.
 3.   Loosen pen drive motor clamp and remove motor.
 4.   Slide belt from pen carriage to remove it.
 5.   Loosen pen solenoid mounting screw and slide solenoid to the right. Remove
      armature and spring.
 6.   Slide pen lift bar just far enough right to allow belt removal.
Removing pen carriage, pen holder, and damper:
 1.   Remove paper drive motor (see above).
 2.   Remove pen solenoid (see above).                                                                   IBM P/N:                     55X3584
 3.   Remove pen drive motor (see above)                                                                 IBM machine type:            1538-B01, 1516-H20
 4.   Slide belt from pen carriage and move carriage to the left.
 5.   Remove end bearing cap while sliding pen lift bar to the right and out of car-
      riage assembly.                                                                                   Tech Support 800-877-7764
 6.   Move slider rod to the right just far enough to release left end of rod from its
      mounting. Slide rod to the left and out of carriage/pen holder assembly.
 7.   Carefully remove plastic damper from carriage and pen holder.
Note: After reassembling the above, measure the pen down force with a gram
gauge before replacing the top cover. Turn plotter on. Lower a pen onto platen.
Place tip of gauge under lip of pen body and make sure that pen just starts to lift
with 19 +/ 10 grams. If it does not, replace the pen down spring.
Removing printed circuit assembly:
 1.   Disconnect all cables from printed circuit board.
 2.   Remove pen carousel housing (see above).
 3.   Remove screw holding control panel and remove panel.
 4.   Remove recessed screw between pen solenoid and pen drive motor.
 5.   Lift right side of chassis assembly. Tabs on left side will release from base
      plate.
 6.   Remove screws or studs holding rear panel interface connector.
 7.   Lift front end of printed circuit assembly and remove it from base plate.




2                                                                                        HP-37                                          IBM/TSS Internal Use Only
                                                                            HEWLETT
                                                                      FliJa
                                                                      a:� PACKARD




HP 7475A
Color Desktop Plotter



Technical Data                                                        The one plotter for
                                                                      both CAD and color
                                                                      business graphics




Features                          Full Bange of                       When commanded to return to
• Two small-fonnat media sizes    Pen/Media                           the same point with no pen
• Full range of pen/media         Combinations                        change, it does so within
  combinations                    HP 7475A users can select from      0.1 mm (0.004 in.). This preci­
• High-quality output             paper (regular and glossy), over­   sion means your drawings have
                                  head transparency film, and         straight lines, crisp characters,
• Strong software support
                                  durable double-matte polyester      circles that close, and corners
• Hardware compatibility
                                  film. Fiber-tip pens for paper      that meet.
• Built-in intelligence
                                  and transparencies come in 10
                                  bright colors and two tip widths.   Strong Software Support
The HP 74 75A color desktop
                                  Refillable liquid-ink pens are      One of the most widely­
plotter produces high-quality
                                  available for final-quality draw­   supported plotters in the world,
A4/A- and A3/B-size color
                                  ings on polyester film.             the HP 7475A works with
graphics for business and PC
                                                                      major software packages from
CAD applications. The HP 7475A
                                                                      the entire spectrum of graphics
is ideal for professionals who    High-quality Output
                                                                      applications-integrated soft­
need the larger drawings for      The HP 7475A color desktop
                                                                      ware, business graphics/presen­
PERT charts, flow charts, pro­    plotter combines high resolu­
                                                                      tations, computer-aided-design/
ject schedules, and design        tion and excellent repeatability
                                                                      drafting, scientific and statis­
applications. It also produces    to ensure professional-quality
                                                                      tical analysis, project
professional-quality color        output. It has an addressable
                                                                      scheduling, and more.
overheads for presentations and   resolution of 0.025 mm
colorful summary charts for       (0.001 in.), so it can plot up to
                                  1000 points in a one-inch line.
                                                                      Hardware
handouts and reports.
                                                                      Compatibility
                                                                      A choice of two interfaces
                                                                      makes it easy to add an
                                                                      HP 7475A to almost any
                                                                      system-personal computers,
                                                                      mainframes, even smart instru­
                                                                      ments. The HP 7475A comes
                                                                      with RS-232-C/CCI'IT V.24 and
                                                                      HP-m (IEEE 488-1978) inter­
                                                                      face options. And with an
                                                                      additional eavesdrop cable, the
                                                                      RS-232-C plotter can be con­
                                                                      nected in series between a
                                                                      computer and a tenninal.
                                   Thchnical Information                  Acceleration
                                   Media Sizes                            Approximately 2 g
                                   210 x 297 mm (ISO A4)
                                   8I/.! x 11 in. (ANSI A)                Maximum Plotting Area

                                   297 x 420 mm (ISO A3)                  Pen axis: 258.0 mm (10.2 in.)
                                   11 x 17 in. (ANSI B)                   for A/B; 275.0 mm (10.8 in.) for
                                                                          A4/A3

                                   Pens                                   Paper axis: 198.0 mm (7.80 in.)
                                   Number: 6 in carousel                  for A; 192.0 mm (7.56 in.) for

                                   Type: Fiber-tip (paper and             A4; 414.0 mm (16.3 in.) for B;
                                                                          402.0 mm (15.8 in.) for A3
                                   transparency), refillable short­
                                   body liquid-ink
Built-in Intelligence                                                     Buffer Size
The HP 7475A's control-panel
                                                                          1024 bytes
                                   Media
keys can alter the size of the
                                   Paper (regular and glossy),
drawing area when switching
                                                                          Environmental Ranges
                                   transparency film, double-matte
media sizes or rotate the plot
                                   polyester film
                                                                          Thmperature
90 degrees. Control-panel keys
                                                                          Operating: 0 to 55 degrees C
can also be used in conjunction
                                                                          (32 to 131 degrees F)
                                   Character Sets
with a digitizing sight.
                                   French/German, HP 9825,                Storage: -40 to 75 degrees C
                                   Scandinavian, Spanish/Latin            (-40 to 167 degrees F)
Programmers will appreciate
                                   American,Roman Extensions,
the intelligence features which                                           Humidity
                                   and these ISO registered sets:
eliminate the need for software­                                          Operating: 5 to 95% (at 40
                                   ANSI ASCII (006), French (025),
generated characters and func­                                            degrees C)
                                   German (021),International
tions. Hewlett-Packard Graphics
                                   Reference Version (002), Italian
Language (HP-GL) instructions                                             Power Requirements
                                   (015),JIS ASCII (014),Katakana
(more than 50) govern such                                                Source: 100, 120,220,240 V,
                                   (013),Norwegian I (060),
tasks QS labeling,pen move­                                               -10%, +5%
                                   Norwegian 11 (016), Portuguese
ment, and drawing arcs and
                                                                          Frequency: 48-66 Hz
                                   (016), Spanish (017),Swedish
circles.
                                   (010), Swedish for Names (011),        Consumption: 35 W maximum
                                   United Kingdom (004)
                                                                          Physical Specifications
                                   Resolution                             Height: 127.0 mm (5.0 in.)
                                   Addressable: 0.025 mm
                                                                          Width: 568.0 mm (22.4 in.)
                                   (0.001 in.)
                                                                          Depth: 367.0 mm (14. 5 in.)
                                   Mechanical: 0.025 mm
                                                                          Net weight: 7.0 kg (16.0 lb)
                                   (0.001 in.)
                                                                          Shipping weight: approx.
                                   Repeatability                          11.0 kg (25.0 lb)
                                   With a given pen: 0.1 mm
                                   (0.004 in.)                            Product Certifications
                                                                          FCC certified to conform to
                                   Pen to pen: 0.2 mm (0.008 in.)
                                                                          limits set for radio frequency
                                                                          when used with a Class B com­
                                   Pen Velocity
                                                                          puting device; meets or exceeds
                                   Pen down, maximum: 38.1 cm/s
                                                                          IEC-380, IEC-435,IEC-478,and
                                   (15.0 in. /s)
                                                                          CSA C22.2 No. 154.
                                   Pen up: 50.8 cm/s (20.0 in'/s)

                                   Programmable: approximately
                                   0.4 to 38.1 cmls (0.2 to 15.0 in'/s)
                                   in increments of 0.4 cm/s
Interface and                                             Ordering Information
Cable Requirements                                        Standard Unit
                                      Cable               7475A
HP Vectra PC with HP 24540AlB         HP 24542G           Color desktop plotter
seriaVparaliel interface card or HP
24541AlB dual serial interface card
using 9-pin connector                                     Option numbers:
                                                          001    RS-232-C/CCI'IT V.24
HP Vactra PC with HP 24541AlB         HP 17255M
dual serial interface card using                                 interface
25-pin connector
                                                          002 HP-IB (IEEE 488-1978)
HP Touchscreen PC using serial        HP 17255M
interface
                                                                 interface

HP Touchscreen PC using HP-IB         HP 10833A (1.0 mJ   Note: Interface cables must be
interface                             HP 10833B 12.0 ml   ordered separately               Accessories Available
                                      HP 10833C 13.0 m)                                    07475·90000   Hardware Suppan Manual
                                      HP 10833D 10.5 mJ                                    07475·90001   Interfacing/Programming Manual
                                                          Accessories Included             5061·5080     Additional fiber·tip pen carousel
HP 3000 or DEC VAX in eavesdrop       HP 17455A
                                                          Operation and Interconnection    07475-60030   liquid�nk drafting pen carousel
configuration
           '                                              Manual (language appropriate
IBM PS/2, PC, PC-Xl, and              HP 17255D                                            For a complete list of available
compatibles                                               to plotter destination)
                                                                                           supplies, check the current ver­
IBM AT and compatibles                HP 24542G           Reference Card                   sion of the HP Plotter Supplies
Apple Macintosh 128K and 512K         HP 92219M                                            Catalog or the Hewlett-Packard
                                                          Power cord (appropriate to
Apple Macintosh SE, Macintosh         HP 17302A           plotter destination)             PC Peripherals Price Guide.
Plus, and Macintosh 11

Apple lie
                                                          Plotter paper
                                      HP 17355M
                                                          50 sheets, A4/A size (paper
                                                          sizes determined by plotter
                                                          destination)

                                                          Transparency film sampler,
                                                          A4/A size (film sizes deter­
                                                          mined by plotter destination)

                                                          Six-pen carousel for fiber-tip
                                                          pens

                                                          Assorted fiber-tip paper and
                                                          transparency pens

                                                          HP Plotter Supplies Catalog
                                  rlipl HEWLETT
                                  �r... PACKARD




United States:                   EuropelAfricalM.lddle East:
Hewlett-Pa.ckard Company         Hewlett-Packard S.A.
4 Choke Cherry Road              Central Mailing Department
Rockville, MD 20850              P.O. Box 529
301 670 4300                     1180 AM Amstelveen
                                 The Netherlands
Hewlett-Packard Company          31 20/547 9999
5201 Tollview Drive
Rolling Meadows, IL 60008        Far East:
312 255 9800                     Hewlett-Packard Asia Ltd.
                                 221F Bond Centre
Hewlett-Packard Company          West Tower
5161 Lankershim Blvd.            89 Queensway
No. Hollywood, CA 91601          Central, Hong Kong
818 505 5600                     5 848 7777

Hewlett Packard Company          Japan:
2015 South Park Place            Yokogawa Hewlett-Packard Ltd.
Atlanta, GA 30339                29-21, Takaido-Higashi 3-chome
404 955 1500                     Suginami-ku, Tokyo 168
                                 03 331 6111
Canada:
Hewlett-Packard Ltd.             Latin America:
6877 Goreway Drive               Latin American Region Headquarters
Missisusa ga, Ontario L4VIM8     Monte Pelvoux Nbr. 111
416 678 9430                     Lomas de Chapultepec
                                 11000 Mexico D.F., Mexico
AustralialNew Zealand:           905 596 79 33
Hewlett-Packard Australia Ltd.
31-41 Joseph Street
Blackburn, Victoria 3130
Melbourne, Australia
03 895 2895




                                 Technical information in tbis doclUllent
                                 is subject to change without notice.

                                 Copyright © 1989
                                 Hewlett-Packard Company

                                 Printed in USA    2/89
                                 5954·7091
                                                                                                 COMPUTER PERIPHERALS
                                                                                                                                     Graphics Plotters
                                                                                                                                 Models 7470A and 7475A


•    Low cost, high performance                                                              •   Plot on paper
•    Choice of six- or two-pen models                                                        •   Plot on HP overhead transparency film




  Hewlett-Packard's HP 7470A and 7475A graphics plotters provide                             Measurement Applications
the kind of graphics excellence you would expect to find only in much                           The HP 7470A and 7475A add hard copy graphics capability to
more expensive plotters. They feature the same high-quality compo­                           intelligent instruments and instrument systems with HP-IB (IEEE
nents and innovative paper-moving technology which were intro­                               488-1978). For most applications that use a display screen and an
duced in HP's drafting plotters and which make it possible to offer                          oscilloscope camera, these plotters can produce high-quality hard­
high performance plotters at affordable prices. Refer to the table be­                       copy of the screen for a cost that is substantially lower than camera
low for a quick comparison of the main features available in each                            film. Because they plot directly from measured data, they eliminate
plotter.                                                                                     problems created by distortion from the screen. And plotter output
                                                                                             provides better visual resolution than photographs. Many systems
         Features               HP 7475A                             HP 7470A                without screen displays can also have the benefits of HP 7470A or
    Media sizes      Two ANSI sizes: A (8.5 x 11 in.)      One ANSI size: A (8.5 x 11 in.)   7475A hardcopy graphics at very little additional cost.
                           and B (11 x 17 in.)
                    Two ISO sizes: A4 (210 x 297 mm)     One ISO size: A4 (210 x 297 mm)
                        and A3 (297 x 420 mm)
                                                                                             Easy to Use
    Pans             Six fiber·tip; programmable pen      Two fiber·tip; programmable pen
                     selection; automatic capping         selection; automatic capping          When the HP 7475A or 7470A plotters are turned on, default con­
                                                                                             ditions are automatically established for most plotting parameters. In
    HP-Cl               More than 50 instructions            More than 40 instructions
    Instructions                                                                             many cases, it is only necessary to load the pens and plotting medium
                                                                                             in order to start plotting.
    Character        19 sets. including ISO European                  Five sets
    sets             standards and Katakana                                                     Media and pen loading are also easy. A guide control lever makes
                                                                                             media alignment perfect every time. The front panel can be used to
    Standard            HP·IB (IEEE 488-1978) or             HP-IB (IEEE 488-1978) or
    Interfaces           RS-232.c (CCITT V.24)            RS-232.c (CCITT V.24) or HP-IL     select pens, to halt the program for exchanging pen colors, or to move
                                                                                             the plot forward to "view" what you have plotted.
                     Each plotter incorporates one permanent interface option.
                                                                                                The front panel also allows easy access to the plotter's digitizing
    Technology       Both plotters use the same micro-grip drive for paper movement and
                     have the same high resolution. repeatability, and velocity.             capability and scaling points. And, on the HP 7475A, push buttons
                                                                                             can rotate plots 90 degrees or run a demonstration plot directly from
                                                                                             the plotter.
computer Applications
   The HP 7470A and 7475A provide hardcopy computer graphics
for technical, scientific, and business applications. Colorful A4/                           Intelligence Features
A-size charts and graphs are ideal for reports and overhead trans­                             Intelligence features are built directly into these plotters to save
parencies. Use them for summarizing data, identifying trends, com­                           you time by eliminating the need for software-generated characters
paring results, and focusing on exceptions. The larger A3/B-size plots                       and functions. Many HP-GL instructions (more than 50 in the HP
that can be drawn on the HP 7475A are particularly useful for time                           7475A; more than 40 in the HP 7470A) govern such tasks as labeling,
lines, PERT charts, schematics, engineering drawings, and other ap­                          pen movement, drawing arcs and circles, and selecting from a large
plications where you need to show visual detail.                                             variety of character sets. The HP 7475A has 19 character sets in-
COMPUTER PERIPHERALS
Graphics Plotters
Model 7470A and 7475A (cont'd)

cluding ISO European sets, Katakana, ASCII, and Roman 8 exten­                                           mm (0.001 in.). With this resolution, they can plot up to 1000 points
sions; the HP 7470A has five internal character sets.                                                    in a I-inch line. When commanded to return to the same point with no
   The HP 7475A's extra HP-GL instructions, which are used for fill­                                     pen change, they achieve this repeatability within 0.1 mm (0.004 in.)
ing rectangles and wedges for pie and bar charts, provide an enhance­                                    Because of this outstanding resolution and repeatability, both plotters
ment especially designed for professional graphics.                                                      produce straight lines and smooth circles that have an artist-drawn
                                                                                                         appearance.
Writing Systems
                                                                                                         Interface Options
   The HP 7470A has two built-in pen stalls which make two-color
                                                                                                            The HP 7475A and 7470A are easy to interface with most HP and
plotting easy. For plots with more than two colors, the program can be
                                                                                                         non-HP computers. Both plotters offer the RS-232-C/CCITT V.24
halted through program or front panel control; new pens can then be
                                                                                                         or HP-IB (IEEE 488-1978) interface. With the RS-232-C option, a
installed and plotting resumed. The HP 7475A's six-pen carousel al­
                                                                                                         dual input/output cable is available for connecting the plotters with a
lows you to store up to six different pen colors or a variety of colors
                                                                                                         terminal and computer. In addition, the HP 7470A offers a third in­
and widths.
                                                                                                         terface option, HP-IL. This interface is used to connect the plotter
   Several automatic features are included to protect the tip of the pen
                                                                                                         with low-cost, portable HP systems.
and increase pen life. When housed in the stall or carousel, the pen is
capped to prevent premature drying. When a pendown command is                                            Graphics Software
given, the pen force is damped and the pen is gently lowered to the                                        HP offers a full line of graphics software packages for use on most
plotting surface.                                                                                        HP computer products. And software is also available for many non­
                                                                                                         HP computers. These packages make it easy for non-programmers to
High-Quality Output                                                                                      use the HP 7470A and 7475A plotters. Details are available from any
  The HP 7470A and 7475A have an addressable step size of 0.025                                          HP sales and support office.

Specifications
                                                                HP 7475A                                                                                 HP 7470A
 Resolution                 Smallest addressable step size: 0.025 mm (0.001 in.)
 Repeatablllty                                                                                    With a given pen: 0.1 mm (0.004 in.)
                                                                                                  From pen to pen: 0.2 mm (0.008 in.)
 Pen velocity (each axis)   Pen up,50.8 cmfs (20 in.fs); pen down,maximum - 38.1 cmfs (15 in.fs), programmable - I to 38 cmfs in I cmfs increments
 Acceleration                                                                                              Approximately 2 g's
 Envtronmental range                                                                                    Operating,O'C to 55'C
                                                                                                    Non'operating, -4O'C to 75'C
 Plotting area
  X·axis                    258 mm (10.2 in.), AlB                                                                   191 mm (7.5 in.) A
                            275 mm (10.8 in.), MfA3                                                                  191 mm (7.5 in.), A4
  Y·axis                    198 mm (7.80 in.),A                                                                      257 mm (10.2 in.), A
                            192 mm (7.56 in.), M                                                                     272 mm (10.7 in.), A4
                            414 mm (16.3 in.), B
                            402 mm (15.8 in.),A3
  Interfaces                HP-IB (IEEE 488-1978),implements the following HP-IB functions as defined in IEEE 488-1978: SHI, AHI, T2, TEO, LEO, SRI,RLO,DCI, DTO, L2,ppo, (listen only or address less
                            than 7, otherwise PP2)
                            R5-232-GfCCITI,asynchronous serial ASCII with switch selectable baud rates of 75,        Same as HP 7475A except 255 byte buffer.
                            1l0,150,200,300,600,1200, 2400, 4800, 9600. External clock input                         HP-IL,Hewlett-Packard Interface Loop for use with portable systems.
                            capabilities with intermediate baud rates of up to 9600 baud. 1024 byte buffer.
  Power Requirements        Source: 100, 120, 200, 240 v� -10%,+5%       Frequency: 48-S6 Hz
                            Consumption: 35 W maximum                                                                Consumption: 25 W maximum
  Size:
  Height                    127 mm (5 in.)                                                                           127 mm (5 in.)
  Width                     568 mm (22.4 in.)                                                                        432 mm (17 in.)
  Depth                     367 mm (14.5 in.)                                                                        343 mm (13.5 in.)
  Weight:
  Net                       7 kg (16.0 Ib)                                                                           6 kg (13.5 Ib)
  Shipping                  Approx. II kg (25.0 Ib)                                                                  Approx. 10 kg (22.0 Ib)
  FCC                       FCe certified to conform to limits set for radio frequency interference when used with a Class B computing device.

                                                                                                         Ordering Information                                                                  Price
                                                                                                         Options
                                                                                                         001 RS-232-C/CCITT V.24 (cable not included)                                            N/C
                                                                                                         002 HP-IB (IEEE 488-1978) (cable not included)                                          N/C
Accessories Supplied                                                                                     003 HP-IL for 7470A only (cable included)                                               N/C
                                                                                                         Note: Option 001, 002, or 003 must be specified when
                                                                                                         ordering HP 7470A; Option 001 or 002 must be speci­
HP 7475A
                                                                                                          fied with HP 7475A.
HP 07475-90001 Interfacing and Programming Manual
                                                                                                          Interface Cables
HP 07475-90002 Operation and Interconnection Manual
                                                                                                          HP 13242G Male-male, special RS-232-C cable for use                                      $69
HP 07475-90004 Reference Card
                                                                                                          with Option 001, HP 150 Personal Computer
                                                                                                          HP 172550 Male-female, special RS-232-C cable for                                        $50
HP 7470A
                                                                                                          use with Option 001, IBM Personal Computers
HP 07470-90001 Interfacing and Programming Manual
                                                                                                          HP 17355F Male-male standard cable for use with Op­                                  $52.50
HP 07470-90002 Operator's Manual
                                                                                                          tion 001
HP 07470-90003 Interconnection Guide
                                                                                                          HP 17455A Eavesdrop cable for use with Option 001                                        $75
HP 07470-90004 Reference Card
                                                                                                          HP 10833A or HP 45529A or HP 31389A HP-IB                                                $81
Power cords and an assortment of pens and drawing media are also
                                                                                                          I-metre cable for use with Option 002
supplied with the plotters. The media size and the appropriate power
                                                                                                          HP 82167A HP-IL Y2-metre cable (included with Op­                                          $6
cord are determined by plotter destination. The HP-IL cable (V2-me­
                                                                                                          tion 003)
tre) is supplied with Option 003 only.
                                                                                                          Plotters
Note: Interface cables are not supplied with Option 001 and Option                                        HP 7470A Two-pen Graphics Plotter                                                     $1095
002 plotters.                                                                                             HP 7475A Six-pen Graphics Plotter                                                     $1895
