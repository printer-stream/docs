   Line Thermal Printer


  STAR Graphic Mode
Command Specifications


          Rev. 2.31




      Star Micronics Co., Ltd.
     Special Products Division
                                                                                             Rev. 2.31


Notes
  ・ Information in this specifications document may change without notice.


  ・ At Star Micronics Co., Ltd., we have taken all measures in order to provide accurate information,
      but does not assume responsibility for errors or omissions.


  ・ Star Micronics Co., Ltd. does not assume any responsibility for any damage resulting from the
      use of information that is described in this specification.


  ・ No part of this specification may be copied, reproduced, or reprinted without written permission.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications       2
                                                                                                                                                                      Rev. 2.31

Table of Contents
1.   INTERFACE CONFIGURATION ................................................................................................................................6
  1-1) USB Interface..........................................................................................................................................................6
  1-2) Ethernet Interface ...................................................................................................................................................6
  1-3) Wireless LAN Interface ...........................................................................................................................................6
2. COMMAND FUNCTION LIST....................................................................................................................................7
3. COMMAND DETAILS ................................................................................................................................................9
  3-1)     Standard Command Details ..............................................................................................................................9
    3-1-1)         External Device Drive ...............................................................................................................................9
       ESC BEL n1 n2 .......................................................................................................................................................9
       BEL .......................................................................................................................................................................10
       FS .........................................................................................................................................................................10
       SUB ....................................................................................................................................................................... 11
       EM ......................................................................................................................................................................... 11
       ESC GS BEL m n1 n2 ...........................................................................................................................................12
       ESC GS EM DC1 m n1 n2 ....................................................................................................................................13
       ESC GS EM DC2 m n1 n2 ....................................................................................................................................14
    3-1-2)         Print Settings...........................................................................................................................................15
       ESC RS A n ...........................................................................................................................................................15
       ESC RS d n ...........................................................................................................................................................16
       ESC RS r n............................................................................................................................................................16
       ESC GS c h v ........................................................................................................................................................17
    3-1-3) Status .............................................................................................................................................................18
       ESC RS a n ...........................................................................................................................................................18
       ESC ACK SOH ......................................................................................................................................................18
       ETB .......................................................................................................................................................................19
       ESC RS E n ..........................................................................................................................................................19
       ESC GS ETX s n1 n2 ............................................................................................................................................20
    3-1-4) Other ..............................................................................................................................................................22
       ESC GS # m N n1 n2 n3 n4 LF NUL .....................................................................................................................22
       ESC ? LF NUL ......................................................................................................................................................23
       ESC GS L DC1 m n1 n2 ........................................................................................................................................23
       ESC GS L DC2 m n1 n2 ........................................................................................................................................24
  3-2) Raster Graphics Command Details .......................................................................................................................25
       ESC * r R...............................................................................................................................................................25
       ESC * r A ...............................................................................................................................................................26
       ESC * r B ...............................................................................................................................................................26
       ESC * r C...............................................................................................................................................................26
       ESC * r D n NUL ...................................................................................................................................................27
       ESC * r E n NUL ....................................................................................................................................................27
       ESC * r F n NUL ....................................................................................................................................................28
       ESC * r P n NUL ....................................................................................................................................................29
       ESC * r Q n NUL ...................................................................................................................................................29
       ESC * r m l n NUL .................................................................................................................................................30
       ESC * r m r n NUL .................................................................................................................................................30
       ESC * r t n NUL .....................................................................................................................................................31
       ESC * r K n NUL ....................................................................................................................................................31
       b n1 n2 data ..........................................................................................................................................................32
       k n1 n2 data ..........................................................................................................................................................33
       ESC * r Y n NUL ....................................................................................................................................................34
       ESC FF NUL .........................................................................................................................................................34
       ESC FF EOT .........................................................................................................................................................34
       ESC * r a ...............................................................................................................................................................35
       ESC * r b ...............................................................................................................................................................35
       ESC * r e n NUL ....................................................................................................................................................36
       ESC FF EM ...........................................................................................................................................................37
       ESC FF LF ............................................................................................................................................................37
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications                                        3
                                                                                                                                                               Rev. 2.31
  3-3) USB Interface Related Command Details .............................................................................................................38
       ESC # # W n , d1 d2．．． dk LF NUL....................................................................................................................38
  3-4) Print Mode Command Details ...............................................................................................................................39
       ESC RS C n ..........................................................................................................................................................39
       ESC RS S n ..........................................................................................................................................................42
  3-5) Printer Information Related Commands Details ....................................................................................................43
       ESC GS ( S n m [d1...dm] .....................................................................................................................................43
       ESC GS ) I pL pH fn ..............................................................................................................................................44
       ESC # * LF NUL ....................................................................................................................................................45
  3-6) Customer display Commands ...............................................................................................................................46
       ESC GS B @.........................................................................................................................................................46
       ESC RS B A ..........................................................................................................................................................46
       ESC GS B B ..........................................................................................................................................................47
       ESC GS B C..........................................................................................................................................................47
4. APPENDIX ..............................................................................................................................................................48
  4-1) Appendix-1 Standard Status .................................................................................................................................48
  4-2) Appendix-2 Printer Status Transmission Specification for Wireless Ethernet I/F and LAN I/F ..............................53
  4-3) Appendix-3 Device Status Specification (USB Interface Only) ..............................................................................55
  4-4) Appendix-6 Supported Command List by Models .................................................................................................56




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications                                    4
                                                                                                          Rev. 2.31

This specifications document describes the command specifications for the STAR Graphic Mode on line thermal printers.
Information contained herein applies to models with the following conditions.

  ・ Line thermal printers
  ・ Interface
       ・ USB
       ・ Ethernet
       ・ Wireless LAN
       ・ Bluetooth

  <Name of applicable models>
  ・ TSP100U
  ・ TSP100PU
  ・ TSP100GT
  ・ TSP100LAN
  ・ TSP100IIU
  ・ TSP100IIIW
  ・ TSP100IIILAN
  ・ TSP100IIIBI
  ・ TSP100IIIU




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications           5
                                                                                              Rev. 2.31


1. INTERFACE CONFIGURATION
1-1) USB Interface


Specifications:   Conforms to USB2.0 Full Speed
                  Supports Printer class and vendor class
Connector:        Type A (TSP100IIIU)
                  Type B (TSP100U, TSP100PU, TSP100IIU, TSP100GT、TSP100IIIU)
                  PoweredUSB (TSP100PU)



1-2) Ethernet Interface


Specifications:   Physical layer, MAC layer：     10Base-T/100Base-TX (IEEE802.3/IEEE802.3u)
                  Protocol:                      TCP/IP v4
Connector:        RJ45 (TSP100LAN)


1-3) Wireless LAN Interface


Specifications:   Conforms to IEEE 802.11b/g/n




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications          6
                                                                                              Rev. 2.31


2. COMMAND FUNCTION LIST
● Standard Commands
                                                                                       Line    Raster
   Classification           Command                             Name
                                                                                       mode    mode
 External device    ESC BEL                Set pulse width for external device drive    OK      OK
 drive              BEL                    External device 1 drive instruction          OK      OK
                    FS                     External device 1 drive instruction          OK      OK
                    SUB                    External device 2 drive instruction          OK      OK
                    EM                     External device 2 drive instruction          OK      OK
                    ESC GS BEL             Ring buzzer                                  OK      OK
                    ESC GS EM DC1          Set external buzzer drive pulse condition    OK      OK
                    ESC GS EM DC2          Output External buzzer drive pulse           OK      OK
 Print settings     ESC RS A               Set print area                               OK      OK
                    ESC RS d               Set print density                            OK      OK
                    ESC RS r               Set printing speed                           OK      OK
                    ESC GS c               Set reduced printing                         OK      OK
 Status             ESC RS a               Set status transmission conditions           OK      OK
                    ESC ACK SOH            Real-time printer status (ASB status)        OK      OK
                    ETB                    Update ETB status                            OK      OK
                    ESC RS E               Clear ETB counter, ETB status                OK      OK
                    ESC GS ETX             Document start, Document end                 OK      OK
 Other              ESC GS #               Set memory switch                            OK      OK
                    ESC ?                  Reset printer                                OK      OK
                    ESC GS L DC1           Set LED blink condition                      OK      OK
                    ESC GS L DC2           LED blink                                    OK      OK


● Raster related commands
                                                                                       Line    Raster
   Classification           Command                             Name
                                                                                       mode    mode
 Raster             ESC * r R              Initialize raster mode                       OK      OK
                    ESC * r A              Enter raster mode                            OK      OK
                    ESC * r B              Quit raster mode                             No      OK
                    ESC * r C              Clear raster data                            No      OK
                    ESC * r D              Drive drawer                                 No      OK
                    ESC * r E              Set EOT mode                                 No      OK
                    ESC * r F              Set FF mode                                  No      OK
                    ESC * r P              Set page length                              No      OK
                    ESC * r Q              Set print quality                            No      OK
                    ESC * r m l            Set left margin                              No      OK
                    ESC * r m r            Set right margin                             No      OK
                    ESC * r t              Set top margin                               No      OK
                    ESC * r K              Set print color                              No      OK
                    b n1 n2 d1．．． dk       Transfer raster data (auto line feed)        No      OK
                    k n1 n2 d1．．． dk       Transfer raster data                         No      OK
                    ESC * r Y              Position movement in vertical direction      No      OK
                    ESC FF NUL             Execute FF mode                              No      OK
                    ESC FF EOT             Execute EOT mode                             No      OK
 Raster extension   ESC * r a              Start block                                  OK      OK
                    ESC * r b              End block                                    No      OK
                    ESC * r e              Set EM mode                                  No      OK
                    ESC FF EM              Execute EM mode                              No      OK
                    ESC FF LF              Execute LF mode                              No      OK


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications        7
                                                                                              Rev. 2.31



● USB-I/F related commands
                                                                                       Line    Raster
   Classification          Command                                    Name
                                                                                       mode    mode
 USB-I/F             ESC # # W                Register/Initialize USB serial number     OK      OK



● Print mode related commands
                                                                                      Line    Raster
  Classification        Command                                      Name
                                                                                      mode    mode
 Select print       ESC RS C               Select print mode                           OK      OK
 mode
                    ESC RS S               Select print startup setting               OK       OK



● Printer information related commands
                                                                                      Line    Raster
  Classification        Command                                      Name
                                                                                      mode    mode
 Register printer   ESC GS ( S             Register/Clear printer information          OK      OK
 information
 Send printer       ESC GS ) I             Send printer information                   OK       OK
 information
                    ESC # *                Inquire printer version                    OK       OK


● Customer Display commands
                                                                                      Line    Raster
  Classification        Command                                      Name
                                                                                      mode    mode
 Select print       ESC GS B @             Send data to a customer display             OK      OK
 mode               ESC RS B A             Status request                              OK      OK
                    ESC GS B B             Customer display data request               OK      OK
                    ESC GS B C             Buffer clear                                OK      OK




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            8
                                                                                                Rev. 2.31


3. COMMAND DETAILS
3-1) Standard Command Details

3-1-1) External Device Drive


 ESC BEL n1 n2
[Name]         Set external drive device 1 pulse width
[Code]         ASCII         ESC BEL n1 n2
               Hex             1B 07 n1 n2
               Decimal          27    7 n1 n2

[Defined Area] 1≦n1≦127
                1≦n2≦127
[Initial Value] n1 = 20 (Energizing time: 200 msec)
                n2 = 20 (Delay time: 200 msec)

[Function]     Sets the energizing and delay times for driving the external device.
               ・ Energizing time = 10 x n1 (ms)
               ・ Delay time = 10 x n2 (ms)
               This setting value is not initialized with a soft reset.



                                   ON
                   Drive pulse
                                   OFF
                                                           10×n1(msec)         10×n2(msec)

                                                          (Charging time)       (Delay time)


                 Printing operation                        Printing, paper feeding prohibited




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications              9
                                                                                                         Rev. 2.31


 BEL
[Name]         External device 1 drive instruction
[Code]         ASCII       BEL
               Hex           07
               Decimal        7

[Defined Area] ---
[Initial Value] ---
[Function]      Executes the external device drive conditions set according to the command to set the external drive
                device pulse width (ESC BEL n1 n2).
                External device 1 and external device 2 cannot be executed simultaneously.
                If unprinted data exists, the unprinted data is printed out and then the command is executed.




 FS
[Name]         External device 1 drive instruction
[Code]         ASCII         FS
               Hex           1C
               Decimal       28

[Defined Area] ---
[Initial Value] ---
[Function]      Executes the external device drive conditions set according to the command to set the external drive
                device pulse width (ESC BEL n1 n2).
                External device 1 and external device 2 cannot be executed simultaneously.
                If unprinted data exists, the unprinted data is printed out and then the command is executed.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             10
                                                                                                                Rev. 2.31


 SUB
[Name]          External device 2 drive instruction
[Code]          ASCII        SUB
                Hex            1A
                Decimal        26

[Defined Area] ---
[Initial Value] ---
[Function]      Drives external device 2.
                The energizing time and delay time for external device 2 are fixed at 200 ms each.
                External device 1 and external device 2 cannot be executed simultaneously.
                If unprinted data exists, the unprinted data is printed out and then the command is executed.




 EM
[Name]          External device 2 drive instruction
[Code]          ASCII         EM
                Hex            19
                Decimal        25

[Defined Area] ---
[Initial Value] ---
[Function]      Drives external device 2.
                The energizing time and delay time for external device 2 are fixed at 200 ms each.
                External device 1 and external device 2 cannot be executed simultaneously.
                If unprinted data exists, the unprinted data is printed out and then the command is executed.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications              11
                                                                                                             Rev. 2.31


 ESC GS BEL m n1 n2
[Name]          Ring buzzer
[Code]          ASCII       ESC GS BEL           m       n1     n2
                Hex          1B 1D 07            m       n1     n2
                Decimal      27 29   7           m       n1     n2

[Defined Area] 1≦m≦2
                1≦n1≦255
                1≦n2≦255
[Initial Value] ---
[Function]      Rings the buzzer.
                m specifies the buzzer drive terminal.
                    m        Buzzer Drive Terminal
                   1, 49    Buzzer Drive Terminal 1
                   2, 50    Buzzer Drive Terminal 2

                n1 specifies energizing time; n2 specifies the delay time.
                ・ Energizing time = 20 x n1 (ms)
                ・ Delay time = 20 x n2 (ms)

                The buzzer will not ring while printing.
                Use of this command other than for ringing the buzzer is prohibited.
                (There is the possibility of damage if using this command for driving the drawer on models that support
                external device terminals.)




                                     ON
                    Drive pulse
                                     OFF
                                                          20×n1(msec)             20×n2(msec)

                                                         (Charging time)           (Delay time)


                       Printing operation                     Printing, paper feeding prohibited




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             12
                                                                                                       Rev. 2.31


 ESC GS EM DC1 m n1 n2
[Name]        Set external buzzer drive pulse condition
[Code]        ASCII         ESC GS EM DC1             m      n1   n2
              Hex            1B 1D 19           11    m      n1   n2
              Decimal         27 29 25          17    m      n1   n2

[Defined Area] 1≦m≦2, 49≦m≦50
                0≦n1≦255
                0≦n2≦255
[Initial Value] n1 = 0, n2 = 0

[Function]    Set external buzzer drive pulse condition
              m specifies the buzzer drive terminal to perform the condition settings.
                   m       Buzzer Drive Terminal
                 1, 49      Buzzer Drive Terminal 1
                 2, 50      Buzzer Drive Terminal 2
              n1 specifies energizing time; n2 specifies the delay time.
              ・ Energizing time = 20 x n1 (ms)
              ・ Delay time = 20 x n2 (ms)
              Drives for external buzzers set using this command is performed by <ESC> <GS> <EM> <DC2> m n1 n2.
              When n1 = 0, regardless of the value of n2, the external buzzer drive command
              <ESC><GS><EM><DC2> is ignored.
              This setting value is not initialized with a soft reset.


                                   ON
                  Drive pulse
                                   OFF
                                                         20×n1(msec)          20×n2(msec)

                                                        (Charging time)        (Delay time)


                     Printing operation                  Printing, paper feeding prohibited




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications           13
                                                                                                                      Rev. 2.31


 ESC GS EM DC2 m n1 n2
[Name]         Output External buzzer drive pulse
[Code]         ASCII        ESC GS EM DC2                   m   n1    n2
               Hex            1B 1D 19          12          m   n1    n2
               Decimal        27 29 25          18          m   n1    n2

[Defined Area] 1≦m≦2, 49≦m≦50
                1≦n1≦20
                n2 = 0
[Initial Value] ---
[Function]      Repeatedly drives the buzzer according to the ON/OFF conditions set by the external buzzer drivepulse
                conditions command <ESC> <GS> <EM> <DC1> m t1 t2.
                m specifies the buzzer drive terminal to drive.

               m specifies the buzzer drive terminal to drive.
                   m        Buzzer Drive Terminal
                    1, 49   Buzzer Drive Terminal 1
                    2, 50   Buzzer Drive Terminal 2
               Specifies the number of repetitions of the buzzer drive with (n2 x 256 + n1).
               The buzzer will not ring while printing.
               Use of this command other than for ringing the buzzer is prohibited.
               (If this command is used to drive the cash drawer on models that have an external device terminal, the
               system will be damaged. Absolutely never use it for other purposes.)
               The buzzer can be stopped by pressing the paper feed switch when it is ringing.

               <Example>


                                                                              n1 = 8



                             ON
               Drive pulse
                             OFF


                                              on off



                Printing operation                              Printing, paper feeding prohibited

                                     (Special Note) If off time=0, it is only possible to continuously sound it n1 times.
                                                    For example, if on=5 seconds, off=0 and n1=20 times, it will sound
                                                    for 100 seconds.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications               14
                                                                                                           Rev. 2.31


3-1-2) Print Settings


 ESC RS A n
[Name]         Set print area
[Code]         ASCII          ESC   RS     A    n
               Hex             1B   1E    41    n
               Decimal         27   30    65    n

[Defined Area] 0≦n≦1
[Initial Value] Memory SW setting
[Function]      Sets the print area according to n.
                Set n to be the same as the print area setting of MSW. (See MSW setting of each model for details)
                If unprinted data exists when processing this command, the data is printed out and then the command is
                executed.
                (Cutting and feeding operations are not performed.)
                This command is executed after the print operation is stopped.
                The raster left and right margin settings are initialized.
                This setting value is initialized with a soft reset.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            15
                                                                                                             Rev. 2.31


 ESC RS d n
[Name]         Set print density
[Code]         ASCII         ESC     RS   d     n
               Hex             1B    1E 64      n
               Decimal          27   30 100     n

[Defined Area] 0≦n≦6
                48≦n≦57 (”0”≦n≦”6”)
[Initial Value] Memory SW setting
[Function]      Sets print density.
                If unprinted data exists when processing this command, the data is printed out and then the command is
                executed.
                This command is executed after the print operation is stopped.
                When in two-color printing mode, only print density for red printing can be set by this command.
                   n                                          Print Density
                            Single Color       Two-Color Printing Mode      Energy saving         Energy saving
                           Printing Mode       Red Print Density Double        mode 1               mode 2
                                                  Resolution Mode
                 0, 48    Print density +3        Red print density +        Print density +3    Print density +3
                 1, 49    Print density +2        Red print density +        Print density +2    Print density +2
                 2, 50    Print density +1    Red print density (Standard)   Print density +1    Print density +1
                 3, 51     Print density      Red print density (Standard)    Print density       Print density
                            (Standard)                                         (Standard)          (Standard)
                 4, 52    Print density -1    Red print density (Standard)   Print density -1    Print density -1
                 5, 53    Print density -2        Red print density -        Print density -2    Print density -2
                 6, 54    Print density -3        Red print density -        Print density -3    Print density -3




 ESC RS r n
[Name]         Set print speed
[Code]         ASCII         ESC     RS   r     n
               Hex             1B    1E 72      n
               Decimal         27    30 114     n

[Defined Area] 0≦n≦2
                48≦n≦50 (”0”≦n≦”2”)
[Initial Value] Memory SW setting
[Function]      Sets print speed.
                If unprinted data exists when processing this command, the data is printed out and then the command is
                executed.
                This command is executed after the print operation is stopped.
                Since the printing speed in two-color printing mode and energy saving mode 1 are fixed, the speed
                settings with this command are invalid. However, the settings of this command become valid when
                returning from two-color printing mode or energy saving mode 1 to single color printing mode.
                   n                                          Print Speed
                             Single Color       Two-color Printing      Energy saving           Energy saving
                            Printing Mode            Mode                 mode 1                  mode 2
                 0, 48       High speed                  Invalid             Invalid               Invalid
                 1, 49       Mid-speed                   Invalid             Invalid               Invalid
                 2, 50       Slow speed                  Invalid             Invalid               Invalid



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            16
                                                                                                                Rev. 2.31


 ESC GS c h v
[Name]          Set reduced printing
[Code]          ASCII        ESC GS         c     h        v
                Hex            1B 1D       63     h        v
                Decimal        27 29       99     h        v

[Defined Area] 0≦h≦255
                0≦v≦255
[Initial Value] h = 0 (Always 0)
                v = 0 (When not set) or previously set value
[Function]      Sets reduced printing.
                If unprinted data exists, the unprinted data is printed out and then the command is executed.
                 h              Set horizontal direction of reduced printing                   Remarks
                 0              Always 0

                 v               Set vertical direction of reduced printing                    Remarks
                 0              Invalid (100%)                                 Setting is stored to non-volatile memory
                 1              Valid (50%)                                    Setting is stored to non-volatile memory
                 2              Valid (75%)                                    Setting is stored to non-volatile memory

                ・The reduced printing setting can be changed or disabled for a receipt. However, intermittent printing will
                 occur when it is switched (Print quality is no guaranteed).
                ・If the correct setting value is specified, it is stored to non-volatile memory.
                ・The print quality is not guaranteed for reduced printing (barcodes and 2D barcodes may not be read
                 correctly at times).




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications              17
                                                                                                              Rev. 2.31


3-1-3) Status


  ESC RS a n
 [Name]    Set status transmission conditions
 [Code]    ASCII       ESC RS       a     n
           Hex.          1B 1E 61         n
           Decimal       27 30 97         n

[Defined Area] 0≤n≤3, 48≤n≤51(”0”≤n≤”3”)
                n=16,n=255
[Initial Value] Set by memory switches.
[Function]      Sets the status transmission conditions.
                See Appendix 1 for details regarding ASB status.
                See each printer's product specifications manual for details on the memory switch settings.

                     n       Status transmission conditions
                   0, 48     ASB Invalid , NSB Invalid
                   1, 49     ASB Valid , NSB Invalid
                   2, 50     ASB Invalid , NSB Valid
                   3, 51     ASB Valid , NSB Valid
                     16      Returns the ASB and NSB settings to the initial state previously set by the MSW.
                    255      Sends the ASB status information.




  ESC ACK SOH
 [Name]         Real-time printer status (ASB status)
 [Code]         ASCII        ESC ACK SOH
                Hex.           1B      06    01
                Decimal        27       6     1

[Defined Area] - - -
[Initial Value] - - -
[Function]      Sends ASB status information to the host.
                This command is not used when ASB is valid.
                See Appendix 1, Automatic Status for details regarding ASB status.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            18
                                                                                                           Rev. 2.31


ETB
[Name]          Update ETB status of normal status
[Code]          ASCII          ETB
                Hex              17
                Decimal          23

[Defined Area] ---
[Initial Value] ---
[Function]      Sets the ETB status of the normal status and updates the ETB counter.
                If unprinted data exists when processing this command, the data is printed out and then the command is
                executed.
                (Cutting and feeding operations are not performed.)
                This command is executed after the print operation is stopped.
                For information on the normal status, see Appendix-1.




 ESC RS E n
[Name]         Initialize normal status ETB counter and ETB status
[Code]         ASCII          ESC RS        E    n
               Hex              1B 1E 45         n
               Decimal          27 30 69         n

[Defined Area] n = 0
                n = 48 (“0”)
[Initial Value] Normal status ETB counter = 0
[Function]      Clears the normal status ETB counter to zero and ETB status.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             19
                                                                                                                 Rev. 2.31


 ESC GS ETX s n1 n2
[Name]       Document start , end
[Code]       ASCII        ESC GS ETX            s    n1     n2
             Hexadecimal 1B 1D 03               s    n1     n2
             Decimal         27 30 3            s    n1     n2

[Defined Area]        3≤s≤5
                      Refer to the table below for the n1 and n2 defined area of n1 and n2.

[Function]            This command is run when reading from the reception buffer. Processes the print end counter
                      according to the s parameter.

                     s     Name                       Function
                           Start document             (1) Sets data intake mode
                     3
                           n1, n2 = 0                 (2) Initialize
                                                      (1) Prints data in line buffer, if data exists.
                           End document
                     4                                (2) Waits until printing ends (motor stops).
                           n1, n2 = 0
                                                      (3) Cancels data intake mode
                                                      n1=0 : Initializes to the content of MSW. (n2=0)
                                                      n1=1 : Data timeout setting
                     5     Data timeout setting       n2=0 : Timeout disabled
                                                      Others: n2 = Data timeout time (units: seconds 1 to 255 seconds)
                                                      n1=2: Sends the current timeout setting to the host. (n2=0)

               When s = 3, and s = 4 (Document start command + document end command), printer operates as though
               in data cancel mode. If there is an error after receiving the document start command, reception data is
               received and discarded until the document end command is received when the printer is recovered from
               the error. If the document end command cannot be recognized, all reception data is destroyed. Timeouts
               are 10 seconds. Automatically cancels the data intake mode.

               Restrictions
               1) Sleep mode decrease
               2) Erroneous printing occurs if the same data as the End command is contained in the raster data.
               3) If the interval of data transmission is longer than the timeout time for some reason, it will be judged as
                  an error even though the transmission is not actually disconnected. In case of data cancellation, data
                  up to the document end command will be cancelled. Be sure to check by ETB to control.

             When s = 3, initialize the following settings using the initializing process.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications               20
                                                                                                             Rev. 2.31

           The interface disconnection detection function through data reception timeout is controlled when s=5 is
           specified.

           When this function is enabled, the interface is determined to have been disconnected when no data is
           received
           for a specified period of time at the data read section of the printer.
           When a disconnection is detected during a command execution, the command parsing is stopped.
           When data cancel is enabled, the print start function using the timer (ESC GS g 1) is disabled, and data is
           canceled.

           n1=0 and n2=0: Initializes the interface disconnection detection function through data reception timeout.
                          (Returns to the MSW settings. The initial value for the timeout time is 3 seconds.)
           n1=1 :         Set enable/disable and the timeout time for data reception timeouts.
                          When n2 is 0, the disconnection detection function is disabled due to data reception
                          timeouts.
                          When n2 is anything except for 0, the data reception timeout is set. (Units: seconds, 1 to
                          255 seconds)
           n1=2 and n2=0: Sends the current setting to the host.
                          The data format returned to the host is as shown below.

           <Returned Data Formats>
           [Code] ASCII       ESC GS ETX s n1 n2 [timeout setting] NUL
                   Hex.       1B 1D 03 s n1 n2 [timeout setting] 00
                   Decimal    27 29 3 s n1 n2 [timeout setting] 0

           * Echoes back the specified contents from the host as is until ESC GS ETX s n1 n2, and then sends the
           print end counter value and NUL.

           This function is invalid at the time of program rewriting.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             21
                                                                                                                    Rev. 2.31


3-1-4) Other


 ESC GS # m N n1 n2 n3 n4 LF NUL
[Name]         Set memory SW
[Code]         ASCII       ESC GS           #    m     N    n1    n2    n3    n4       LF    NUL
               Hex          1B 1D          23    m     N    n1    n2    n3    n4       0A     00
               Decimal      27 29          35    m     N    n1    n2    n3    n4       10      0

[Defined Area] m = 87, 84, 44, 43, 45, 64 ( m = “W”, “T”, “,”, “+”, “-”, “@” )
                48≦N≦57 (“0”≦N≦“9”), 65≦N≦70 (“A”≦N≦“F”), 97≦N≦102 (“a”≦N≦“f”)
                48≦n1≦57 (“0”≦n1≦“9”), 65≦n1≦70 (“A”≦n1≦“F”), 97≦n1≦102 (“a”≦n1≦“f”)
                48≦n2≦57 (“0”≦n2≦“9”), 65≦n2≦70 (“A”≦n2≦“F”), 97≦n2≦102 (“a”≦n2≦“f”)
                48≦n3≦57 (“0”≦n3≦“9”), 65≦n3≦70 (“A”≦n3≦“F”), 97≦n3≦102 (“a”≦n3≦“f”)
                48≦n4≦57 (“0”≦n4≦“9”), 65≦n4≦70 (“A”≦n4≦“F”), 97≦n4≦102 (“a”≦n4≦“f”)
[Initial Value] ---
[Function]      Sends command to write after defining memory switch using the definition command specified by the
                following classes.
                Memory switch information defined by the command to write is written to the volatile memory.
                When writing to the volatile memory by the command to write, the printer executes a reset.
                For information on the memory switch, see the product specifications document for each model.

               Function                                            Class           m             N          n1 n2 n3 n4
               Definition data write and reset                       Write     “W”          Fixed at “0”   Fixed at “0000”
               Definition data write and reset and self print        Write      “T”         Fixed at “0”   Fixed at “0000”
               Data definition (data specification)               Definition    “, ”             N          n1 n2 n3 n4
               Data definition (specify bit and set)              Definition    “+”              N          n1 n2 n3 n4
               Data definition (specify bit and clear)            Definition    “-”              N          n1 n2 n3 n4
               Definition data (all data initialized)             Definition   “@”          Fixed at “0”   Fixed at “0000”
               Data definition (load factory setting )            Definition    “*”         Fixed at “0”   Fixed at “0000”
               ・ m              : Mode selection
               ・ N              : Memory switch number to specify
               ・ n1 n2 n3 n4 : Specified data          m=“,” -> Specified data
                                                       m=”+” -> Bit number to set
                                                       m=”-“ -> Bit number cleared




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             22
                                                                                                        Rev. 2.31



 ESC ? LF NUL
[Name]            Reset printer (execute self print)
[Code]            ASCII         ESC     ? LF NUL
                  Hex             1B 3F 0A           00
                  Decimal         27 63 10            0

[Defined Area] ---
[Initial Value] ---
[Function]      After executing a software reset, executes self print once.




 ESC GS L DC1 m n1 n2
[Name]             Set LED blink condition
[Code]             ASCII        ESC GS         L   DC1      m   n1    n2
                   Hex            1B 1D       4C    11      m   n1    n2
                   Decimal        27 29       76    17      m   n1    n2

[Defined Area]     1≦m≦2, 49≦m≦50
                   0≦n1≦255
                   0≦n2≦255
[Initial Value]    n1 = 0, n2 = 0
[Function]         Sets LED flashing conditions.
                   m specifies the LED applicable to the condition settings.
                       m        LED
                      1, 49     ERROR LED (Red)
                      2, 50     READY LED (Blue)
                   n1 specifies lit time; n2 specifies the time the LED turns off.
                   ・ Lit time = 20 x n1 (ms)
                   ・ Turn off time = 20 x n1 (ms)
                   Perform LED flashing set with this command using <ESC><GS>”L”<DC2> m n1 n2.
                   When n1 = 0, regardless of the value of n2, the LED flash command <ESC><GS>”L”<DC2> is ignored.
                   This setting value is not initialized with a soft reset.




                                     ON
                          LED
                                     OFF
                                                           20×n1(msec)         20×n2(msec)

                                                          (Lit (LED ON)        (Not-lit (LED
                                                                time）           OFF) time)




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications              23
                                                                                                                        Rev. 2.31


 ESC GS L DC2 m n1 n2
[Name]         LED blink
[Code]         ASCII         ESC GS         L    DC2        m   n1     n2
               Hex            1B 1D        4C     12        m   n1     n2
               Decimal        27 29        76     18        m   n1     n2

[Defined Area] 1≦m≦3, 49≦m≦51
                1≦n1≦20
                n2 = 0
[Initial Value] ---
[Function]      Repeatedly flashes the LED according to the ON/OFF conditions set by the LED flashing condition
                setting command <ESC><GS>”L”<DC1> m t1 t2.
                m specifies the LED to flash.
                     m       LED
                   1, 49    ERROR LED (Red)
                   2, 50    READY LED (Blue)
                   3, 51    ERROR LED (Red), READY LED (Blue)
               Specifies the number of repetitions of the LED flash with (n2 x 256 + n1).
               After the command is executed, the LED display pattern occurs after according to the status of the
               printer.

               <Example>


                                                                        n1 = 8



                ON
         LED
                OFF


                                       on off




                           (Special note) If off time=0, it can be set to continously lit only for n1 number of times
                                          For example, if on=5 seconds, off=0 and n1=20 times, it will be lit for
                                          100 seconds.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications               24
                                                                                                            Rev. 2.31

3-2) Raster Graphics Command Details


During line mode, these commands are prohibited from being used because they will not be processed be correctly.
(Excluding ESC * r R command, ESC * r A command and ESC * r a command.)



 ESC * r R
[Name]         Initialize raster mode
[Code]         ASCII           ESC    *  r      R
               Hex               1B 2A 72      52
               Decimal           27 42 114     82

[Defined Area] ---
[Initial Value] ---
[Function]      Executes the initialization of raster mode.
                This command is valid for other modes besides raster mode.
                The raster mode initialization performed by this command is executed when entering raster mode.
                This command initializes the following setting contents.
                ・ Raster page length setting (ESC * r P n NUL)
                ・ Raster print color setting (ESC * r K n NUL)
                ・ Raster top margin setting (ESC * r T n NUL)
                ・ Raster left margin setting (ESC * r T n NUL)
                ・ Raster right margin setting (ESC * r T n NUL)
                ・ Raster EOT mode setting (ESC FF EOT)
                ・ Raster FF mode setting (ESC FF NUL)
                ・ Clear raster image buffer
                When entering raster mode, the command executes a process identical to initializing raster mode.
                As the following setting is not initialized when entering raster mode, send this initialization command
                when initializing the contents below,
                ・ Raster data print color setting (ESC * r K n NUL)
                (*) Raster print quality setting (ESC * Q n NUL)




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            25
                                                                                                               Rev. 2.31


 ESC * r A
[Name]          Enter raster mode
[Code]          ASCII         ESC     *   r       A
                Hex            1B    2A 72       41
                Decimal        27    42 114      65

[Defined Area] ---
[Initial Value] ---
[Function]      Enters raster mode.
                This command is ignored during raster mode.
                When entering raster mode, raster mode is initialized.
                The corresponding initialization contents are listed below.
                ・ Raster page length setting (ESC * r P n NUL)
                ・ Raster top margin setting (ESC * r T n NUL)
                ・ Raster left margin setting (ESC * r T n NUL)
                ・ Raster right margin setting (ESC * r T n NUL)
                ・ Raster EOT mode setting (ESC FF EOT)
                ・ Raster FF mode setting (ESC FF NUL)
                (*) Raster print color setting(ESC * r K n NUL)is not initialized when entering raster mode.
                (*) Raster print quality setting (ESC * Q n NUL)is not initialized when entering raster mode.
                If the printer is in command emulator mode and there is unprinted data, this command is processed after
                the unprinted data is printed. (Cutting and feeding operations are not performed.)




 ESC * r B
[Name]          Quit raster mode
[Code]          ASCII        ESC      *   r       B
                Hex            1B    2A 72       42
                Decimal        27    42 114      66

[Defined Area] ---
[Initial Value] ---
[Function]      Ends raster mode.
                When raster mode ends, and if raster data still remains in the image buffer of the raster mode, after
                executing raster EOT mode, terminate the raster mode.




 ESC * r C
[Name]          Clear raster data
[Code]          ASCII         ESC     *   r       C
                Hex             1B   2A 72       43
                Decimal         27   42 114      67

[Defined Area] ---
[Initial Value] ---
[Function]      Clears the image buffer data of raster mode.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications              26
                                                                                                             Rev. 2.31


 ESC * r D n NUL
[Name]          Drive drawer
[Code]          ASCII        ESC       *   r          D        n   NUL
                Hex           1B      2A 72          44        n    00
                Decimal       27      42 114         68        n     0

[Defined Area] 0≦n≦3
[Initial Value] n = 0
[Function]      Executes the drawer drive during raster mode.
                Drawer driving conditions is equivalent to the conditions set by the line mode.
                nI is a decimal notation using ASCII characters (up to 255 digits)
                If raster data exists in the image buffer of raster mode, this command is ignored.

                    n      Drive circuit
                    0      None
                    1      Drive external device drive 1
                    2      Drive external device drive 2
                    3      Drive external device drive 1 + Drive external device drive 2




 ESC * r E n NUL
[Name]          Set raster EOT mode
[Code]          ASCII        ESC    *  r              E        n   NUL
                Hex            1B 2A 72              45        n    00
                Decimal        27 42 114             69        n     0

[Defined Area] n = 0, 1, 2, 3, 8, 9, 12, 13, 32, 33, 36, 37
[Initial Value] Cutter model n = 13
                TearBar model n = 3
[Function]      Sets the raster EOT mode.
                The EOT mode is an operation to be performed by the raster document end command (ESC FF EOT).
                nI is a decimal notation using ASCII characters (up to 255 digits)
                If raster data exists in the image buffer of raster mode, this command is ignored.

                <EOT mode setting format>
                   n            Model                                        Function
                         Cutter      TearBar               FormFeed          Cut Feed          Cutter
                    0        Valid          Valid         Set To Default   Set To Default   Set To Default
                    1        Valid          Valid              OK               －－               －－
                    2        Valid         Invalid             OK               OK               －－
                    3       Invalid         Valid              OK             TearBar            －－
                    8        Valid         Invalid             OK               －－             Full Cut
                    9        Valid         Invalid             OK               OK             Full Cut
                   12        Valid         Invalid             OK               －－           Partial Cut
                   13        Valid         Invalid             OK               OK           Partial Cut
                   32       Invalid        Invalid
                   33       Invalid        Invalid
                   36       Invalid        Invalid
                   37       Invalid        Invalid




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications                  27
                                                                                                     Rev. 2.31


 ESC * r F n NUL
[Name]        Set raster FF mode
[Code]        ASCII         ESC  *   r         F        n   NUL
              Hex            1B 2A 72         46        n    00
              Decimal        27 42 114        70        n     0

[Defined Area] n = 0, 1, 2, 3, 8, 9, 12, 13, 32, 33, 36, 37
[Initial Value] Cutter model n = 13
                TearBar model n = 3
[Function]      Sets the raster FF mode.
                The FF mode is an operation to be performed by the raster document end command (ESC FF NUL).
                nI is a decimal notation using ASCII characters (up to 255 digits)
                If raster data exists in the image buffer of raster mode, this command is ignored.

              <FF mode stetting format>
                 n             Model                                Function
                       Cutter      TearBar         FormFeed         Cut Feed          Cutter
                  0       Valid      Valid     Set To Default     Set To Default   Set To Default
                  1       Valid      Valid          OK                 －－               －－
                  2       Valid     Invalid         OK                 OK               －－
                  3      Invalid     Valid          OK               TearBar            －－
                  8       Valid     Invalid         OK                 －－             Full Cut
                  9       Valid     Invalid         OK                 OK             Full Cut
                 12       Valid     Invalid         OK                 －－           Partial Cut
                 13       Valid     Invalid         OK                 OK           Partial Cut
                 32      Invalid    Invalid
                 33      Invalid    Invalid
                 36      Invalid    Invalid
                 37      Invalid    Invalid




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications           28
                                                                                                             Rev. 2.31


 ESC * r P n NUL
[Name]          Set raster page length
[Code]          ASCII         ESC      * r          P        n   NUL
                Hex            1B 2A 72            50        n    00
                Decimal         27 42 114          80        n     0

[Defined Area] 0, 200≦n≦64000 (Other than TSP100IIU) 0, 200≦n≦32000 (TSP100IIU)
[Initial Value] ---
[Function]      Sets the raster page length.
                nI is a decimal notation using ASCII characters (up to 255 digits)
                If raster data exists in the image buffer of raster mode, this command is ignored.

                TSP100U, TSP100PU, TSP100GT, TSP100LAN, TSP100IIIW, TSP100IIILAN, TSP100IIIBI、TSP100IIIU
                      n
                         0             Continuous printing mode
                                       (page length without setting, but maximum page length is 64000 dot)
                 200≦n≦64000           Specified page length

                TSP100IIU
                       n
                         0             Continuous printing mode
                                       (page length without setting, but maximum page length is 32000 dot)
                 200≦n≦32000           Specified page length




 ESC * r Q n NUL
[Name]          Set raster print quality
[Code]          ASCII          ESC       * r        Q        n   NUL
                Hex              1B 2A 72          51        n    00
                Decimal          27 42 114         81        n     0

[Defined Area] 0≦n≦2
[Initial Value] n = 0
[Function]      Sets the raster print quality.
                nI is a decimal notation using ASCII characters (up to 255 digits)
                If raster data exists in the image buffer of raster mode, this command is ignored.

                   n         Print quality
                   0         High-speed printing specified
                   1         Normal print quality
                   2         High print quality




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications                29
                                                                                                                   Rev. 2.31


 ESC * r m l n NUL
[Name]          Set the left margin of raster
[Code]          ASCII         ESC        *    r m l            n   NUL
                Hex             1B 2A 72 6D 6C                 n    00
                Decimal         27 42 114 109 108              n     0

[Defined Area] Print width: 72 mm mode 0≦n≦71
                Print width 51 mm mode 0≦n≦50
[Initial Value] n = 0
[Function]      Sets the left margin of the raster.
                By this command set the left margin to (nx 8) dots.
                If the left margin exceeds the printable area, or if there is no print area by the left margin specified
                ((printable area - right margin) ≧ left margin specified value), it ignores this command.
                nI is a decimal notation using ASCII characters (up to 255 digits)
                If raster data exists in the image buffer of raster mode, this command is ignored.




 ESC * r m r n NUL
[Name]          Set the right margin of raster
[Code]          ASCII         ESC       *     r m r            n   NUL
                Hex             1B 2A 72 6D 72                 n    00
                Decimal         27 42 114 109 114              n     0

[Defined Area] Print width: 72 mm mode 0≦n≦71
                Print width 51 mm mode 0≦n≦50
[Initial Value] n = 0
[Function]      Sets the right margin of the raster.
                By this command set the right margin to (nx 8) dots.
                If the right margin exceeds the printable area,
                or if there is no print area by the right margin specified ((printable area - left margin) ≧ right margin
                specified value),
                this command is ignored.
                nI is a decimal notation using ASCII characters (up to 255 digits)
                If raster data exists in the image buffer of raster mode, this command is ignored.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications               30
                                                                                                              Rev. 2.31


 ESC * r t n NUL
[Name]          Set the top margin of raster
[Code]          ASCII        ESC       *     r t           n   NUL
                Hex            1B 2A 72 74                 n    00
                Decimal        27 42 114 116               n     0

[Defined Area] 0≦n≦11
[Initial Value] n = 0
[Function]      Sets the top margin of the raster.
                nI is a decimal notation using ASCII characters (up to 255 digits)

                        n                        Top margin                                  Remarks
                       0             Set To Default                          Default top margin differs with the model
                  Other than 0       When n value is for that model,         Enabled setting differs with the model
                                     enabled setting: set top margin
                                     disabled setting: Ignore the command
                (*) Support of this command varies according to the model.

                TSP100IIU
                      n                          Top margin                                  Remarks
                        0         Set To Default (3mm)                      Setting is stored to non-volatile memory
                     3 to 11      Set top margin (3～11mm)                   Setting is stored to non-volatile memory
                 Other than the   Ignore the command
                     above
                (*) When the top margin setting is 3 ~ 10mm, back feed is performed before printing starts.

                Back feed operation by the top margin setting is performed only with the following timing.
                ・After the cutting operation (including error recovery operation)




 ESC * r K n NUL
[Name]          Set raster print color
[Code]          ASCII          ESC     * r        K        n   NUL
                Hex              1B 2A 72        4B        n    00
                Decimal          27 42 114       75        n     0

[Defined Area] 0≦n≦3
[Initial Value] n = 0
[Function]      Sets the raster print color.
                This command is valid only if it is designated a two-color printing mode by the line mode.
                If not the two-color printing mode, ignore the command.
                nI is a decimal notation using ASCII characters (up to 255 digits)

                   n        Print color
                    0     Black
                    1     Cyan
                    2     Magenta
                    3     Yellow
                (*) This command is valid only for two-color printing compatible models.
                    Non-compatible models command ignored




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications              31
                                                                                                          Rev. 2.31


 b n1 n2 data
[Name]         Transfer of raster data (automatic line feed)
[Code]         ASCII           b n1 n2 d1 d2               ...   dk
               Hex            62 n1 n2 d1 d2               ...   dk
               Decimal        98 n1 n2 d1 d2               ...   dk

[Defined Area] 0≦n1≦255
                0≦n2≦255
                0≦d≦255
                k = n1＋n2 x 256
                1≦k
[Initial Value] ---
[Function]      Transfers the raster data.
                Raster data is send at (n1 + n2 x 256) bytes binary data.
                Raster data beyond the print area that is currently set is cut off.
                The deployed position of the image buffer, after deploying the data to one dot column image buffer by
                this command, will one dot column automatic line feed, and move to the left margin of the next line
                position.
                If it goes over page due to automatic line feed
                ・ Page length settings are in continuous print mode, if it exceeds the maximum page length
                   (see ESC * r P n NUL command)
                ・ Page length set in the specified page length mode, and if it exceeds the specified page length, and
                   print the data up to the end page, to process as the first line of data for the next page.
                In addition, data expansion is performed by overwriting processing (OR processing) the current image
                buffer data.
                For the set raster print color, the deployment image buffer is described below.

                Print color                Deployment image buffer
                Black                      Black image buffer
                Cyan                       Colored image buffer
                Magenta                    Colored image buffer
                Yellow                     Colored image buffer




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             32
                                                                                                              Rev. 2.31


 k n1 n2 data
[Name]          Transfer raster data
[Code]          ASCII           k n1     n2    d1   d2    ...   dk
                Hex           6B n1      n2    d1   d2    ...   dk
                Decimal      107 n1      n2    d1   d2    ...   dk

[Defined Area] 0≦n1≦255
                0≦n2≦255
                0≦d≦255
                k= n1＋n2 x 256
                1≦k
[Initial Value] ---
[Function]      Transfers the raster data.
                Raster data is send at (n1 + n2 x 256) bytes binary data.
                Raster data beyond the print area that is currently set is cut off.
                The deployed position of the image buffer, after deploying the data to one dot column image buffer by
                this command, will not automatically line feed, and move to the left margin of the current line position.
                In addition, data expansion is performed by overwriting processing (OR processing) the current image
                buffer data.
                For the set raster print color, the deployment image buffer is described below.

                 Print color            Deployment image buffer
                 Black                  Black image buffer
                 Cyan                   Colored image buffer
                 Magenta                Colored image buffer
                 Yellow                 Colored image buffer




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            33
                                                                                                                Rev. 2.31


 ESC * r Y n NUL
[Name]          Moving position in the vertical direction (line break of a specified dot)
[Code]          ASCII        ESC       *     r     Y     n NUL
                Hex            1B 2A 72 59               n      00
                Decimal        27 42 114 89              n       0

[Defined Area] ---
[Initial Value] ---
[Function]      Performs position movement of the raster vertical direction.
                With this command it will move the position of n dot.
                If the specified movement makes you go over the page
                  ・ If the page length settings are in continuous print mode, and the n dot is the maximum page length
                     (see ESC * r P n NUL command)
                  ・ Page length set at the specified page length mode, and the n dot exceeds the specified page length
                to do this, you print the data up to the end page, and the section that is overflow will be treated as data
                from the beginning of the next page.
                nI is a decimal notation using ASCII characters (up to 255 digits)




 ESC FF NUL
[Name]          Execute FF mode
[Code]          ASCII       ESC       FF    NUL
                Hex          1B       0C     00
                Decimal      27       12      0

[Defined Area] ---
[Initial Value] ---
[Function]      Executes FF mode.
                It runs the operation specified in FF mode setting command (ESC * r F n NUL).
                If raster data exists in the image buffer for raster mode, FF mode is implemented after printing.
                If raster data does not exist in the image buffer for raster mode, this command is ignored.
                (TSP100IIU) if the print paper length to be cut is less than 24mm, then empty feed is automatically added
                before cutting so that the printing paper length is 24mm.




 ESC FF EOT
[Name]          Execute EOT mode
[Code]          ASCII      ESC FF EOT
                Hex          1B 0C 04
                Decimal      27 12  4

[Defined Area] ---
[Initial Value] ---
[Function]      Executes EOT mode.
                It runs the operation specified in EOT mode setting command (ESC * r E n NUL).
                If raster data exists in the image buffer for raster mode, EOT mode is implemented after printing.
                If raster data does not exist in the image buffer for raster mode, this command is ignored.
                (TSP100IIU) if the print paper length to be cut is less than 24mm, then empty feed is automatically added
                before cutting so that the printing paper length is 24mm.


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications              34
                                                                                                                Rev. 2.31


 ESC * r a
[Name]          Start block
[Code]          ASCII         ESC     *   r       a
                Hex            1B    2A 72       61
                Decimal        27    42 114      97

[Defined Area] ---
[Initial Value] ---
[Function]      Starts the block
                Enters the command emulator mode.
                This command is ignored during command simulator mode.
                When it enters the command emulator mode, initialize the command emulator mode.
                The corresponding initialization contents are listed below.
                ・ Raster page length setting (ESC * r P n NUL)
                ・ Raster top margin setting (ESC * r T n NUL)
                ・ Raster left margin setting (ESC * r T n NUL)
                ・ Raster right margin setting (ESC * r T n NUL)
                ・ Raster EOT mode setting (ESC FF EOT)
                ・ Raster FF mode setting (ESC FF NUL)
                ・ Clear raster image buffer
                (*) Raster page length setting (ESC * r P n NUL), is initialized to 0.
                (*) Raster print color setting (ESC * r K n NUL)is not initialized when entering raster mode.
                (*) Raster print quality setting (ESC * Q n NUL)is not initialized when entering raster mode.




 ESC * r b
[Name]          End the block
[Code]          ASCII        ESC      *   r       b
                Hex           1B     2A 72       62
                Decimal       27     42 114      98

[Defined Area] ---
[Initial Value] ---
[Function]      Ends the block
                Maintains a command emulator.
                If raster data remains in the image buffer of the raster mode, command emulator is maintained when
                raster EM mode is executed.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications              35
                                                                                                           Rev. 2.31


 ESC * r e n NUL
[Name]        Set raster EM mode
[Code]        ASCII        ESC   *   r   e              n   NUL
              Hex            1B 2A 72 65                n    00
              Decimal        27 42 114 101              n     0

[Defined Area] n = 0, 1, 2, 3, 8, 9, 12, 13, 32, 33, 36, 37
[Initial Value] Cutter model n = 13
                TearBar model n = 3
[Function]      Sets the raster EM mode.
                The EM mode, is an operation to be performed by the raster document end command (ESC FF EM).
                nI is a decimal notation using ASCII characters (up to 255 digits)

              <EM mode setting format>
                 n                 Model                                  Function
                          Cutter       TearBar       FormFeed            Cut Feed             Cutter
                  0        Valid        Valid      Set To Default      Set To Default     Set To Default
                  1        Valid        Valid            x                   x                  x
                  2        Valid        Valid            x               Cut Feed               x
                  3        Valid        Valid            x             Tear Bar Feed            x
                  8        Valid        Valid            x                   x               Full Cut
                  9        Valid        Valid            x               Cut Feed            Full Cut
                 12        Valid        Valid            x                   x             Partial Cut
                 13        Valid        Valid            x               Cut Feed          Partial Cut
                 32       Invalid      Invalid
                 33       Invalid      Invalid
                 36       Invalid      Invalid
                 37       Invalid      Invalid
              (*) If an unsupported function is specified, it operates with supported features.
                 Cutter only mode: TearBar Feed -> Cut Feed
                 TearBar only model: Cut Feed -> TearBar Feed
                 Full cut only model: Partial Cut -> Full Cut
                 Partial Cut only model: Full Cut -> Partial Cut




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications           36
                                                                                                              Rev. 2.31


 ESC FF EM
[Name]          Execute EM mode
[Code]          ASCII      ESC       FF EM
                Hex          1B      0C 19
                Decimal      27      12 25

[Defined Area] ---
[Initial Value] ---
[Function]      Executes EM mode.
                It runs the operation specified in EM mode setting command (ESC * r e n NUL).
                If raster data exists in the image buffer for raster mode, EM mode is implemented after printing.
                If raster data does not exist in the image buffer of raster mode, this command is executed.
                (TSP100IIU) if the print paper length to be cut is less than 24mm, then empty feed is automatically added
                before cutting so that the printing paper length is 24mm.




 ESC FF LF
[Name]          Execute LF mode
[Code]          ASCII       ESC      FF   LF
                Hex          1B      0C   0A
                Decimal      27      12   10

[Defined Area] ---
[Initial Value] ---
[Function]      Executes LF mode.
                Nothing operates at the time when this command is processed.
                Then, when a certain period of time elapses without any data being received, it starts printing.
                However, if there is no non-printed data in the printer, it will not execute a line break or operate
                FormFeed even if this command is received.
                If the printer is command emulator mode, print out unprinted data and perform a line break.
                If the printer is raster mode, printing will perform a FormFeed operation by the page length setting.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            37
                                                                                                                   Rev. 2.31

3-3) USB Interface Related Command Details


The following command is a command to control the function of the USB interface.

--- Specification(1) ---


 ESC # # W n , d1 d2．．． dk LF NUL
[Name]          Register USB serial number
[Code]          ASCII       ESC       #   #       W         n     ,   d1   d2 ．．．    dk   LF    NUL
                Hex           1B 23 23            57        n   2C    d1   d2 ．．．    dk   LF    NUL
                Decimal       27 35 35            87        n   44    d1   d2 ．．．    dk   LF    NUL

[Defined Area] n = 56 ( “8”)
                When registering serial number        : 48≦d≦57 (“0” ≦d≦”9”), 65≦d≦90 (”A” ≦d≦”Z”)
                When clearing serial number           : d = 63 (“?“)            k=n
[Initial Value] ---
[Function]      Executes USB serial number registration.
                After registration, the printer executes a soft reset, but at this time disconnect/reconnect of the USB-I/F is
                not performed, and the serial number before the value is changed is maintained.
                In order to enable the registered serial number, it is necessary to power on again.
                When initializing the serial number, insert "?" for all serial number data.




--- Specification(2) ---


ESC # # W n , d1 d2．．．dk LF NUL
【Name】 Register USB serial number
【Code】 ASCII       ESC       #   #          W      n      ,     d1    d2 ．．．   dk    LF NUL
       Hex           1B 23 23               57     n    2C      d1    d2 ．．．   dk    LF NUL
       Decimal       27 35 35               87     n    44      d1    d2 ．．．   dk    LF NUL

【Defined Area】
             When registering serial number(8 digits)                ： n = 56 ( “8”）
            When registering serial number(16 digits)                ： n = 16
             When registering serial number(8, 16 digits)            ：48≦d≦57 (“0”≦d≦”9”)、 65≦d≦90 （”A”≦d≦”Z”）
             When initializing the serial number                     ： d = 63 (“?“）         k=n
[Initial Value] ---
【Function】 Executes registration of 8 digits USB serial number or 16 digits one
             After registration, the printer executes a soft reset, but at this time disconnect/reconnect of the USB-I/F is
             not performed, and the serial number before the value is changed is maintained.
             In order to enable the registered serial number, it is necessary to power on again.

           When initializing the serial number, insert "?" for all serial number data.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications               38
                                                                                                             Rev. 2.31

3-4) Print Mode Command Details


The following command is a command to control the printing mode.



--- Specification (1) power saving mode not compatible models ---


 ESC RS C n
[Name]           Select/Cancel two-color print mode
[Code]           ASCII       ESC RS          C    n
                 Hex            1B 1E 43          n
                 Decimal        27 30 67          n

[Defined Area] 0≦n≦1, 48≦n≦49 (”0” ≦n≦”1”)
[Initial Value] n = 0, 48
[Function]      Selects/Cancels two-color print mode
                This setting value is initialized with a soft reset.

                      n      Selects/Cancels two-color print mode
                    0, 48    Release two-color printing mode (setting of monochromatic print mode)
                             When in two-color printing mode, delete the two-color mode with this command.
                             If you already have deleted two-color printing mode, this command is ignored.
                             When the two-color printing mode is released with this command, the following process is
                             executed
                                 ・If there is a non-printed data, print the non-printed data in a two-color mode.
                                ・Initialize the print color (two-color printing mode set to black)
                                ・Set the print density setting in the monochromatic print mode
                                ・Set the print speed setting in the monochromatic print mode
                    1, 49    Select two-color print mode
                             When in monochromatic printing mode, select two-color printing mode with this command
                             If the two-color printing mode is already selected, the command is ignored
                             When the two-color printing mode is selected by this command, the following process is
                             executed
                                ・If there is unprinted data, and prints the unprinted data in the monochrome mode
                                ・Initialize the print color (two-color printing mode is set to black)
                                ・And set the print density setting in the two-color printing mode




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications                39
                                                                                                              Rev. 2.31



--- Specification (2) power saving mode compatible model ---


 ESC RS C n
[Name]         Select print mode
[Code]         ASCII         ESC    RS      C   n
               Hex            1B    1E     43   n
               Decimal         27   30     67   n

[Defined Area] 0≦n≦1, 48≦n≦49 (”0”≦n≦”1”)
[Initial Value] n = 0, 48
[Function]      Selects the print mode.

                       DIPSW setting                      n           Printing Mode
                    Enable energy-saving                 0, 48        Invalid
                                                         1, 49        Invalid
                   Disable energy-saving                 0, 48        Selection of standard print mode
                                                         1, 49        Selection of two-color printing mode

               Setting details when selecting and canceling two-color print mode are as follows.
                  Selects/Cancels two-color     Configuration details
                          print mode
                 When disengaged                When the two-color printing mode is released with this command, the
                   When the standard print      following process is executed
                   mode is selected               ・If there is a non-printed data, print the non-printed data in a
                                                    two-color mode.
                                                   ・Initialize the print color (two-color printing mode is set to black)
                                                  ・Set the print density setting in the monochromatic print mode
                                                  ・Set the print speed setting in the monochromatic print mode
                 When selected                  When the two-color printing mode is selected by this command, the
                   When two-color printing      following process is executed
                   mode is selected               ・If there is unprinted data, and prints the unprinted data in the
                                                    monochrome mode
                                                  ・Initialize the print color (two-color printing mode is set to black)
                                                  ・And set the print density setting in the two-color printing mode




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            40
                                                                                                              Rev. 2.31



--- Specification (3) tone print mode compatible models compatible ---


 ESC RS C n
[Name]          Select print mode
[Code]          ASCII         ESC    RS     C    n
                Hex            1B    1E    43    n
                Decimal         27   30    67    n

[Defined Area] 0≦n≦1, 48≦n≦49 (”0”≦n≦”1”), 8≦n≦8
[Initial Value] n = 0, 48
[Function]      Selects the print mode.

                    n      Select print mode
                  0, 48    Selection of monochromatic print mode
                           When in two-color printing mode/gradation printing mode, select monochromatic
                           printing mode with this command
                           If the monochromatic printing mode is already selected, the command is ignored
                           When the monochromatic printing mode is selected with this command, the following
                           process is executed
                              ・ If there is non-printed data, print the non-printed data with the current print mode
                                 (two-color printing mode/gradation print mode)
                               ・Initialize the print color (two-color printing mode is set to black)
                              ・Set the print density setting in the monochromatic print mode
                              ・Set the print speed setting in the monochromatic print mode
                  1, 49    Selection of two-color printing mode
                           When in monochromatic printing mode/monochromatic print mode, select two-color
                           printing mode with this command
                           If the two-color printing mode is already selected, this command is ignored
                           When the two-color printing mode is selected by this command, the following process is
                           executed
                              ・ If there is non-printed data, print the non-printed data with the current print mode
                                 (monochromatic print mode/gradation print mode)
                              ・Initialize the print color (two-color printing mode is set to black)
                              ・And set the print density setting in the two-color printing mode
                              (Printing speed fixed in the two-color printing mode)
                  8, 56    Selection of tone print mode
                           When in monochromatic printing mode/two-color print mode, select gradation printing
                           mode with this command
                           If the gradation printing mode is already selected, this command is ignored
                           When the gradation printing mode is selected with this command, the following process
                           is executed
                              ・ If there is non-printed data, print the non-printed data with the current print mode
                                 (monochromatic print mode/two-color print mode)
                              ・ Initialize the printing gradation (set to the tone mode gradation 1)
                              ・Set the print density setting in the monochromatic print mode
                              (Printing speed fixed in the gradation printing mode)




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             41
                                                                                                           Rev. 2.31


 ESC RS S n
[Name]         Select print startup setting
[Code]         ASCII          ESC RS        S   n
               Hex              1B 1E 53        n
               Decimal          27 30 83        n

[Defined Area] 0≦n≦1
                48≦n≦49
[Initial Value] Memory Switch Settings
[Function]      Selects the print startup setting.
                If the settings will not change when processing this command, the command is not executed.
                If unprinted data exists when processing this command, the data is printed out and then the command is
                executed.
                If printing when processing this command, the command waits for printing to stop and changes the print
                startup setting.
                This command setting is initialized by a printer reset.

               Parameter details
                    n        print startup setting
                    0, 48      Page
                    1, 49      Line




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             42
                                                                                                                Rev. 2.31

3-5) Printer Information Related Commands Details


 ESC GS ( S n m [d1...dm]
[Name]        Register/Clear printer information
[Code]        ASCII       ESC GS         (    S     n    m [d1     ．．    dm]
              Hex          1B 1D 28 53              n    m [d1     ．．    dm]
              Decimal      27 29 40 83              n    m [d1     ．．    dm]

[Defined Area] n = 5
                When registering information:
                Defined region of m is as in the following table
                48≦d≦57 (“0”≦d≦”9”), 65≦d≦90 (”A”≦d≦”Z”), 97≦d≦122 (”a”≦d≦”z”)
                When clearing information:
                m=0
[Initial Value] ---
[Function]      Parameter details
                ・ n : Register information
                ・ m            : Registered number of data against information
                ・ d : Registration data

              This command is, in addition to the printer information that is set at the factory, is a command for the user
              to arbitrarily register and clear the printer information.
              This command can be specified at the beginning of a line.
              However, if there is unprinted data in the line buffer, print the data in the line buffer and execute this
              command.
              If it is determined that there are no problems with the parameter n and m, start processing this
              command.
              If n or m was outside the definition, abort the command analysis.
              After the registration is finished or the enforced termination of registration process, execute the printer
              set.
              During the registration process (between the first parameter which is judged OK to when the initialization
              of the printer is completed after registration), error processing, mechanical operation, status processing
              and such are not executed.
              When clearing registration information, specify m = 0.



                n          m         Register information               Usage example
                0                    Reserved
                1                    Reserved
                2                    Reserved
                3                    Reserved
                4                    Reserved
                5      1≦m≦16        Product serial number              2284210080600197
                6                    Reserved
                7                    Reserved




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            43
                                                                                                                  Rev. 2.31


 ESC GS ) I pL pH fn
[Name]               Send printer information
[Code]               ASCII         ESC GS        )       I   pL   pH     fn
                     Hex             1B 1D      29      49   pL   pH     fn
                     Decimal         27 29      41      73   pL   pH     fn

[Defined Area]     pL = 1, pH = 0
                   fn = 49
[Function]         Send information of the printer that has been set by ”Command ESC GS ( S".
                   However, when the printer information is not registered by ESC GS (S, or printer information is
                   cleared, the printer information that was set at the factory is sent.
[More information] Send in the following format.
                   ESC GS) I pL pH fn [Tag name=Parameter, Tag name=Parameter, ... ] LF NUL

                     There is a tag name associated to the beginning of each parameter, and a parameter corresponding
                     to each tag name is sent.
                     The tag name is up to the equal sign ("="), and after that is the parameter.
                     Each set of tags and parameters are separated with a delimiter "," and (2CH).
                     Printer information that is sent by this command is different depending on the model.
                     Information is transmitted from the top of the list shown below.
                     Only the information supported by the printer of the transmission source (a set of tags and
                     parameters) is transmitted.
                     <LF> <NUL> represents the terminal, the tag and its parameters after that are not transmitted.

                     Parameters are sent as a string.

                     If the information can not be obtained, transmits the following data.
                     ESC GS ) I pL pH fn LF NUL

                 --- Specification(1) ---


                  transmission     Tag                                 Parameter information
                            ↓    PrHwV      Printer main body HW version
                            ↓    PrSrN      Product serial number             up to 16 digits
                                                                              (Information less than 16 digits is NUL.)
                            ↓    BtDvN      Bluetooth device name             Fixed 16 digits
                                                                              (Information less than 16 digits is NUL.)
                            ↓    BtAtC      Bluetooth auto connection         Auto connection
                                                                              Invalid: BtAtC=00 Valid:BtAtC=01
                            ↓    BtIpN      Bluetooth iOS port name           Fixed 16 digits
                                                                              (Information less than 16 digits is NUL.)
                            ↓    BtDsC      Bluetooth Search Permitted        Search Prohibited: BtDsC=00
                                                      Setting                 Search Permitted: BtDsC=01




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             44
                                                                                                               Rev. 2.31



              --- Specification(2) ---


               transmission     Tag                                   Parameter information
                          ↓    PrHwV      Printer main body HW version
                          ↓    PrSrN      Product serial number              up to 16 digits
                                                                             (Information less than 16 digits is NUL.)
                          ↓    UsSrN      USB serial number
                          ↓    BtDvN      Bluetooth device name              Fixed 16 digits
                                                                             (Information less than 16 digits is NUL.)
                          ↓    BtAtC      Bluetooth auto connection          Auto connection
                                                                             Invalid: BtAtC=00 Valid:BtAtC=01
                          ↓    BtIpN      Bluetooth iOS port name            Fixed 16 digits
                                                                             (Information less than 16 digits is NUL.)
                          ↓    BtDsC      Bluetooth Search Permitted         Search Prohibited: BtDsC=00
                                                    Setting                  Search Permitted: BtDsC=01




 ESC # * LF NUL
[Name]        Inquire printer version
[Code]        ASCII          ESC      #    *    LF   NUL
              Hex              1B 23      2A    0A    00
              Decimal          27 35      42    10     0

[Defined Area] ---
[Initial Value] ---
[Function]      Sends the printer version.
                    ESC # * , print version LF NUL
                        <Example TSP100IIIW Ver1.0： ESC # * , TSP100IIIWVer1.0 LF NUL >




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             45
                                                                                        Rev. 2.31

3-6) Customer display Commands

Applicable Customer display
  Refer to the printer’s specification manuals.



 ESC GS B @
[Name]     Send data to a customer display
[Code]     ASCII        ESC GS B           @       n1    n2   d1   ・・・   dk
           Hex.         1B     1D    42    40      n1    n2   d1   ・・・   dk
           Decimal      27     29 66 64            n1    n2   d1   ・・・   dk

[Defined Area]       n1+n2x256 : BYTE count (1≤d≤65535)
                     k          : n1+ n2x256
[Initial Value]      ---
[Function]           The customer display command is sent to a customer display.




 ESC RS B A
[Name]     Status request
[Code]     ASCII        ESC     RS    B    A
           Hex.         1B      1E    42   41
           Decimal      27      30    66   65

[Defined Area]       ---
[Initial Value]      ---
[Function]           Receives the printer status

                     The customer display status transmission format from the printer
                     <ESC> <RS> B A n

                          Bit (n)    Status
                             0       No data in customer display buffer
                                     Data exists in customer display buffer
                            1        No connection of customer display
                                     Customer display is connected to the printer
                          2–7        Reserved




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications                46
                                                                                     Rev. 2.31


 ESC GS B B
[Name]    Customer display data request
[Code]    ASCII          ESC GS B           B
          Hex.           1B     1D 42       42
          Decimal        27     29 66       66

[Defined Area]      ---
[Initial Value]     ---
[Function]          Acquire customer display data from a customer display.

                    The customer display data transmission format from the printer
                    <ESC><GS> B B n1 n2 d1・・・dk

                    n1+n2x256 : BYTE count (1≦d≦65535)
                    k         : n1 + n2 x 256




 ESC GS B C
[Name]    Buffer clear
[Code]    ASCII        ESC    GS    B     C
          Hex.         1B     1D    42    43
          Decimal      27     29    66    67

[Defined Area]      ---
[Initial Value]     ---
[Function]          A customer display buffer of a printer is cleared.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            47
                                                                                                                       Rev. 2.31


4. APPENDIX
4-1) Appendix-1 Standard Status


Standard status, is a status group which is returned from the printer to the query from the host. Standard status is
structured with "Header 1" + "Header 2" + "multiple-byte Printer Status", and is returned continuously to the host. Host
will, for every 1 byte received, according to the identification method, execute data identification.
Standard status, is always replying to inquiries from the host.



Header 1
 Header 1 is a 1-byte length information that is sent to the head of a standard status.
  The structure of header 1 is as indicated in the following chart. Header 1, displays the sent bit number for the overall
  status that includes bit 1 to bit 3, and bit 5bit and header 1. Host acquires the sent byte number information and
  always receives the status data for the sent byte number. For reference, the relationship between the transmission bit
 count and header 1 is as shown in the chart below. This data, because the header 1 to indicate it is bit 0 is always 1
 (the second and subsequent bytes always 0), so when detecting the header 1 just confirm that bit 0 = 1 and bit 4 = 0.
 In addition, bit 6 for future expansion, is ignored by host-side processing.

  < Header 1 (the first byte) >
  Bit                                  Condition              TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100

                                        “0”           “1”       U     PU     IIU    GT     LAN    IIIW   IIILAN   IIIBI    IIIU

   7 Fixed at “0”                                      -        0      0      0      0      0      0       0       0       0
   6 Reserved (0 fixed)                                -        0      0      0      0      0      0       0       0       0
   5 Print status number of bytes                               1      1      1      1      1      1       1       1       1
   4 Fixed at “0”                                      -        0      0      0      0      0      0       0       0       0
   3 Print status number of bytes                               0      0      0      0      0      0       0       0       0
   2 Print status number of bytes                               0      0      0      0      0      0       0       0       0
   1 Print status number of bytes                               1      1      1      1      1      1       1       1       1
   0 Fixed at “1”                         -                     1      1      1      1      1      1       1       1       1

          The actual number of bytes sent and the support table for header 1
           Number of bytes sent n (7≦n≦15)                Header 1
                             7                         00001111B (0F Hex)
                             8                         00100001B (21 Hex)
                             9                         00100011B (23 Hex)
                            10                         00100101B (25 Hex)
                            11                         00100111B (27 Hex)
                            12                         00101001B (29 Hex)
                            13                        00101011B (2B Hex)
                            14                        00101101B (2D Hex)
                            15                         00101111B (2F Hex)




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             48
                                                                                                                       Rev. 2.31

Header 2
  Header 2 is a 1-byte length information which is transmitted to the second byte of the standard status. Structure of the
  header 2 in the table below.
  Header 2, for bit 1 to bit 3, and bit 5 is indicating the standard status version (standard status version).
 The relationship of the actual version and header 2 is as shown in the chart below. Standard status version is to up
 new information for the bit position of the printer status that is empty until the addition of new feature in the future.
  If you do not maintain the standard status version on the host side, it is okay to ignore the received header 2.

  < Header 2 (the second byte) >
  Bit                                  Condition              TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100

                                        “0”           “1”       U     PU     IIU    GT     LAN    IIIW   IIILAN   IIIBI    IIIU

   7   Fixed at “0”                                    -        0      0      0      0      0      0       0       0       0
   6   Not used (Fixed at “0”)                         -        0      0      0      0      0      0       0       0       0
   5   Version number                                           0      0      0      0      0      0       0       0       0
   4   Fixed at “0”                                    -        0      0      0      0      0      0       0       0       0
   3   Version number                                           0      0      0      0      0      0       0       0       0
   2   Version number                                           1      1      1      1      1      1       1       1       1
   1   Version number                                           1      1      1      1      1      1       1       1       1
   0   Fixed at “0”                       -                     0      0      0      0      0      0       0       0       0

          Support table between actual standard status version and header 2
          Version number n             Header 2
                   1               00000010B (02 Hex)
                   2               00000100B (04 Hex)
                   3               00000100B (06 Hex)
                   4               00001000B (08 Hex)
                   5               00001010B (0A Hex)
                   6               00001100B (0C Hex)
                   7               00001110B (0E Hex)
                   8               00100000B (20 Hex)
                   9               00100010B (22 Hex)
                                           ・
                   ・                       ・
                   ・                       ・
                  30               01101100B (6C Hex)
                  31               01101110B (CE Hex)




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications             49
                                                                                                                            Rev. 2.31

Printer status
  The printer status is the status itself that is sent for the 3rd byte onwards for the standard status.
  Printer status is (the 2 sent bytes that is attached to header 1) which is returned.
  The printer status will always be updated to the newest information. (History does not exist)
  The configuration of the status body is shown below.



  < Printer Status 1 printer state (third byte) >
  Bit                                         Condition                TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100

                                             “0”                “1”      U      PU     IIU    GT    LAN    IIIW   IIILAN   IIIBI   IIIU

   7   Fixed at “0”                                                -     -      -      -      -      -      -      -        -       -
   6   -                                                                 -      -      -      -      -      -      -        -       -
   5   Cover status                       CLOSE            OPEN         OK     OK     OK     OK     OK     OK     OK       OK      OK
   4   Fixed at “0”                                          -           -      -      -      -      -      -      -        -       -
       ON-LINE／OFF-LINE
   3                                     ON-LINE          OFF-LINE OK          OK     OK     OK     OK     OK     OK       OK      OK
       status
   2   Compulsion SW                       OPEN      CLOSE OK                  OK     OK     OK     OK     OK     OK       OK      OK
                                                     Already
   1   <ETB> command                   Not executed          OK                OK     OK     OK     OK     OK     OK       OK      OK
                                                    executed
   0 Fixed at “0”                                        -    -                 -      -      -      -      -       -       -       -
    ・ <ETB> command
    Cleared to 0 when sent back to the host



  < Printer Status 2 error information (fourth byte) >
  Bit                                    Condition                     TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100

                                           “0”             “1”           U     PU     IIU    GT     LAN    IIIW   IIILAN   IIIBI   IIIU

   7   Fixed at “0”                                         -            -      -      -      -      -      -       -       -       -
       Stopped due to print head         Is not
   6                                                 Is stopped         OK     OK     OK     OK     OK     OK     OK       OK      OK
       high temperature                 stopped
   5   Unrecoverable error              No error    Error occurs OK            OK     OK     OK     OK     OK     OK       OK      OK
   4   Fixed at “0”                                       -       -             -      -      -      -      -      -        -       -
   3   Auto cutter error                no error    Error occurs OK            OK     OK     OK     OK     OK     OK       OK      OK
   2   -                                                          -             -      -      -      -      -      -        -       -
   1   Not used (Fixed at “0”)                                    -             -      -      -      -      -      -        -       -
   0   Fixed at “0”                                       -       -             -      -      -      -      -      -        -       -



  < Printer Status 3 error information (fifth byte) >
  Bit                                    Condition                     TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100

                                             “0”           “1”            U     PU     IIU    GT    LAN    IIIW   IIILAN   IIIBI   IIIU

   7   Fixed at “0”                                            -          -      -      -      -     -      -       -        -      -
   6   -                                                                  -      -      -      -     -      -       -        -      -
   5   -                                                                  -      -      -      -     -      -       -        -      -
   4   Fixed at “0”                                            -          -      -      -      -     -      -       -        -      -
   3   -                                                                  -      -      -      -     -      -       -        -      -
   2   -                                                                  -      -      -      -     -      -       -        -      -
   1   -                                                                  -      -      -      -     -      -       -        -      -
   0   Fixed at “0”                                            -          -      -      -      -     -      -       -        -      -




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications                  50
                                                                                                                    Rev. 2.31



  < Printer Status 4 error information (sixth byte) >
  Bit                                   Condition             TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100

                                           “0”          “1”     U       PU   IIU    GT     LAN    IIIW   IIILAN   IIIBI   IIIU

   7   Fixed at “0”                                 -           -        -    -      -      -      -      -        -       -
   6   Not used (Fixed at “0”)                      -           -        -    -      -      -      -      -        -       -
   5   Not used (Fixed at “0”)                      -           -        -    -      -      -      -      -        -       -
   4   Fixed at “0”                                 -           -        -    -      -      -      -      -        -       -
   3   Paper end                      Has paper No paper       OK       OK   OK     OK     OK     OK     OK       OK      OK
   2   -                                                        -        -    -      -      -      -      -        -       -
   1   -                                                        -        -    -      -      -      -      -        -       -
   0   Fixed at “0”                                      -      -        -    -      -      -      -      -        -       -



  < Printer Status 5 error information (seventh byte) >
  Bit                                   Condition             TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100

                                          “0”         “1”       U       PU   IIU    GT     LAN    IIIW   IIILAN   IIIBI   IIIU

   7   Fixed at “0”                                      -      -       -     -      -      -      -       -       -       -
   6   Not used (Fixed at “0”)                           -      -       -     -      -      -      -       -       -       -
   5   Not used (Fixed at “0”)                           -      -       -     -      -      -      -       -       -       -
   4   Fixed at “0”                                      -      -       -     -      -      -      -       -       -       -
   3   -                                                        -       -     -      -      -      -       -       -       -
   2   -                                                        -       -     -      -      -      -       -       -       -
   1   -                                                        -       -     -      -      -      -       -       -       -
   0   Fixed at “0”                                      -      -       -     -      -      -      -       -       -       -



  < Printer Status 6 ETB counter (eighth) >
  Bit                                 Condition               TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100

                                         “0”            “1”     U       PU   IIU    GT     LAN    IIIW   IIILAN   IIIBI   IIIU

   7 Fixed at “0”                                       -        -      -      -    -    -      -      -      -      -
   6 ETB counter Bit-4                                          OK OK OK OK OK OK OK OK OK
   5 ETB counter Bit-3                                          OK OK OK OK OK OK OK OK OK
   4 Fixed at “0”                                       -        -      -      -    -    -      -      -      -      -
   3 ETB counter Bit-2                                          OK OK OK OK OK OK OK OK OK
   2 ETB counter Bit-1                                          OK OK OK OK OK OK OK OK OK
   1 ETB counter Bit-0                                          OK OK OK OK OK OK OK OK OK
   0 Fixed at “0”                                       -        -      -      -    -    -      -      -      -      -
  (*) ETB counter
          This counter is the ETB counter of 5 bits.
          (0-31 count possible. If the counter overflows, it counts up to 31 -> 0.)
          This counter is incremented by one by the <ETB> command.
          The ETB counter is initialized with the following command. In this case, ETB status for standard status is also
          cleared.

          <ETB counter initialization command >
          ・ <ESC><RS> e n                : ETB counter initialization




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications                51
                                                                                                                              Rev. 2.31



 < Printer Status 7 presenter paper position (9th byte) >
  Bit                                 Condition                 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100 TSP100

                                         “0”          “1”            U      PU         IIU       GT     LAN   IIIW   IIILAN   IIIBI   IIIU

   7   Fixed at “0”                                      -           -          -          -      -      -     -       -       -       -
   6   Not used (Fixed at “0”)                           -           -          -          -      -      -     -       -       -       -
   5   Not used (Fixed at “0”)                           -           -          -          -      -      -     -       -       -       -
   4   Fixed at “0”                                      -           -          -          -      -      -     -       -       -       -
   3   -                                                             -          -          -      -      -     -       -       -       -
   2   -                                                             -          -          -      -      -     -       -       -       -
   1   -                                                             -          -          -      -      -     -       -       -       -
   0   Fixed at “0”                                      -           -          -          -      -      -     -       -       -       -

 Status identification method
           COMMAND                                              Status
           FUNCTION LIST
                                       bit7    bit6   bit5    bit4       bit3       bit2       bit1   bit0
   Normal status (Header 1)               0      *       *        0      *      *      *     1
   Normal status (except header 1)        0      *       *        0      *      *      *     0
  0 = "0" represents fixed bit / 1 = "1" represents fixed bit / * = represents the changing bit




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications              52
                                                                                                              Rev. 2.31

4-2) Appendix-2 Printer Status Transmission Specification for Wireless Ethernet I/F and LAN I/F

Describes the printer status transmission specification for the Ethernet I/F and wireless LAN I/F.

1) Transmission format

    ・ If you want to send only STAR ASB
         STAR ASB (2nd byte Bit-7=1) + Length (Length = 0x0000)
    ・ If you want to send printer status transmission other than STAR ASB
         STAR ASB (2nd byte Bit-7=1) + Length + Status Data

          <Length details>
          ・ 2-byte value indicating the number of bytes of status data (0x0000 ≦ Length ≦ 0x0200)
          ・ If Status data is 10 bytes, Length = 0x000a
          ・ If sending only STAR ASB, add Length = 0x0000
          ・ If length is added to STAR ASB second byte Bit-7, then is set to Bit-7 = 1

    Detect whether analysis of status detects all the bytes for ASB for the first byte STAR ASB, and length is added to
    the bit-7 for the 2nd byte for STAR ASB. Furthermore by obtaining the number of bytes of subsequent Status Data
    with the length, analyzed status is possible.

2) Transmission format for     status data

 Status Type    +   delimiter 1   +   Data Type   +   Status Length   +   Printer Status    +   delimiter 2

    (1) Status Type (2byte or 4Byte)
         ・ < Header 1 (the second byte) >
           It indicates the cause of printer status
           For more information refer to 3) status transmission specification list reference
         ・ 3rd and 4th byte
           If the occurrence factors of command, indicating the n parameters of command
           If the n parameter does not exist, third and fourth byte is optional
               <Example> When ESC SYN 3 n command is n = 0x31, the 3rd and 4th byte is “31”

    (2) Delimiter 1 (1 byte)
        Transmit “：”

    (3) Data Type (1byte)
        Indicate the data type of the Printer Status, and send "B" (the binary type)

    (4) Status Length (2byte)
        2-byte value that indicates the number of bytes in the Printer Status

    (5) Printer Status (variable length)
        Status transmitted by the printer
        Status contents are different due to the occurrence factor
        For more information on status content, refer to cause of command, and automatic status

    (6) Delimiter 2 (1 byte)
        Transmit “；”




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications              53
                                                                                                                        Rev. 2.31

3) Status transmission specification list

                                                                                    Status Data
                                                          Status Type
                               STAR              The first and      Third and
      Status causes                   Length                                    Delimiter   Data   Status     Printer
                               ASB               second byte      fourth byte n                                         Delimiter 2
                                                                                    1       Type   Length     Status
                                                 occurrence        parameter
                                                    factor
ASB
                               ASB    0x0000        ――              ――           ――        ――       ――         ――          ――
Automatic status (*1)
ESC ACK SOH
                               ASB    0x0000        ――              ――           ――        ――       ――         ――          ――
Printer Status Request
ESC # *                               Variable                                                     Variable
                               ASB                   “11”        Abridgment       “:”       “B”               Status        “;”
  Request printer version              length                                                       length
ESC GS ETX s5
                               ASB    0x000F         “23”        Abridgment       “:”       “B”    0x0008     Status        “;”
Setting request for time-out
ESC GS ) P fn49
ESC GS ) I fn49                       Variable                                                     Variable   Block
                               ASB                   “A1”        Abridgment       “:”       “B”                             “;”
Request command                        length                                                       length    Data
response
(*1) For automatic status it is delivered to all hosts in the TCP # 9100 port connection.




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications                54
                                                                                                        Rev. 2.31

4-3) Appendix-3 Device Status Specification (USB Interface Only)


Device Status is a 1-byte status which is returned for the GET_PORT_STATUS request from the USB host.



Device status specification
    Bit            Field                 1                      0
  7 .. 6        Reserved                   -
    5         Paper Empty          Paper Empty           Paper Not Empty
    4             Select             Selected              Not Selected
    3           Not Error            Not Error                 Error
  2 .. 0        Reserved                   -




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications         55
                                                                                                                                            Rev. 2.31

4-4) Appendix-6 Supported Command List by Models

● Standard Commands
                                TSP100        TSP100         TSP100          TSP100      TSP100      TSP100        TSP100       TSP100        TSP100
 Class       Command              U             PU             IIU             GT         LAN         IIIW          IIILAN       IIIBI          IIIU

 External    ESC BEL              OK             OK            OK             OK          OK           OK            OK           OK           OK

 device      BEL                  OK             OK            OK             OK          OK           OK            OK           OK           OK

 drive       FS                   OK             OK            OK             OK          OK           OK            OK           OK           OK

             SUB                  OK             OK            OK             OK          OK           OK            OK           OK           OK

             EM                   OK             OK            OK             OK          OK           OK            OK           OK           OK

             ESC GS BEL           OK             OK            OK             OK          OK           OK            OK           OK           OK

             ESC GS EM DC1      V1.3～            OK            OK             OK          OK           OK            OK           OK           OK

             ESC GS EM DC2      V1.3～            OK            OK             OK          OK           OK            OK           OK           OK

 Print       ESC RS A             OK             OK            OK             OK          OK           OK            OK           OK           OK

 settings    ESC RS d             OK             OK            OK             OK          OK           OK            OK           OK           OK

             ESC RS r             OK             OK            OK             OK          OK           OK            OK           OK           OK

             ESC GS c             No             No            OK             No          No
                                                                                                      Ver2.0        Ver2.0      Ver2.0 or
                                                                                                                                                No
                                                                                                      or later      or later      later

 Status      ESC RS a             No             No            No             No          No
                                                                                                     Ver1.4 or     Ver1.3 or
                                                                                                                                  OK           OK
                                                                                                       later         later
             ESC ACK SOH          No             No            No             No          No
                                                                                                     Ver1.4 or     Ver1.3 or
                                                                                                                                  OK           OK
                                                                                                       later         later
             ETB                  OK             OK            OK             OK          OK           OK            OK           OK           OK

             ESC RS E             OK             OK            OK             OK          OK           OK            OK           OK           OK

             ESC GS ETX           No             No            No             No          No
                                                                                                     Ver1.4 or     Ver1.3 or
                                                                                                                                  OK           OK
                                                                                                       later         later

 Other       ESC GS #             OK             OK            OK             OK          OK           OK            OK           OK           OK

             ESC ?                OK             OK            OK             OK          OK           OK            OK           OK           OK

             ESC GS L DC1         No             No            No             No          No           OK            OK           OK           OK

             ESC GS L DC2         No             No            No             No          No           OK            OK           OK           OK




● Raster related commands
                                        TSP100        TSP100        TSP100      TSP100      TSP100      TSP100       TSP100      TSP100       TSP100
 Class           Command                  U             PU            IIU         GT         LAN         IIIW         IIILAN      IIIBI         IIIU

 Raster          ESC * r R               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r A               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r B               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r C               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r D               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r E               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r F               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r P               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r Q               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r m l             OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r m r             OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r t               No            No             OK           No          No           No          No          No          No
                                                                                                         V1.4 or      V1.3 or
                 ESC * r K               OK            OK             OK           OK          OK
                                                                                                          later        later
                                                                                                                                    OK          OK

                 b n1 n2 d1．．． dk        OK            OK             OK           OK          OK          OK           OK          OK          OK

                 k n1 n2 d1．．． dk        OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r Y               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC FF NUL              OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC FF EOT              OK            OK             OK           OK          OK          OK           OK          OK          OK

 Raster          ESC * r a               OK            OK             OK           OK          OK          OK           OK          OK          OK

 extension       ESC * r b               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC * r e               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC FF EM               OK            OK             OK           OK          OK          OK           OK          OK          OK

                 ESC FF LF               OK            OK             OK           OK          OK          OK           OK          OK          OK

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications                56
                                                                                                                             Rev. 2.31


● USB-I/F related commands
                                         TSP100   TSP100   TSP100   TSP100   TSP100   TSP100       TSP100       TSP100         TSP100
 Class              Command                U        PU       IIU      GT      LAN      IIIW         IIILAN       IIIBI           IIIU

 USB-I/F            ESC # # W             (1)      (1)      (1)      (1)      No         No           No           No            (2)




● Print mode related commands
                                         TSP100   TSP100   TSP100   TSP100   TSP100   TSP100       TSP100       TSP100         TSP100
 Class              Command                U        PU       IIU      GT      LAN      IIIW         IIILAN        IIIB           IIIU

 Select print       ESC RS C              (1)      (2)      (1)      (1)      (1)     Ver1.4 or    Ver1.3 or       (1)           (1)
                                                                                       later (1)    later (1)
 mode               ESC RS S              No       No       No       No       No      Ver1.4 or    Ver1.3 or       OK            OK
                                                                                         later        later




● Printer information related commands
                                         TSP100   TSP100   TSP100   TSP100   TSP100   TSP100       TSP100       TSP100         TSP100
 Class              Command                U        PU       IIU      GT      LAN      IIIW         IIILAN       IIIBI           IIIU

 Register printer   ESC GS ( S
                                          No       No       No       No       No         OK           OK           OK            OK
 information
 Send printer       ESC GS ) I                                                         Ver1.5       Ver1.5       Ver1.1          (2)
                                                                                      or earlier   or earlier   or earlier
 information                              No       No       No       No       No
                                                                                         (1)          (1)          (1)
                                                                                       Ver2.0       Ver2.0       Ver2.0
                                                                                       or later     or later     or later
                                                                                         (2)          (2)          (2)
                    ESC # *               No       No       No       No       No         OK           OK           OK            OK




● Customer display related Commands
                                         TSP100   TSP100   TSP100   TSP100   TSP100   TSP100       TSP100       TSP100         TSP100
 Class              Command                U        PU       IIU      GT      LAN      IIIW         IIILAN       IIIBI           IIIU

 Customer           ESC GS B @            No       No       No       No       No         No           No           No            OK

 display            ESC RS B A            No       No       No       No       No         No           No           No            OK

                    ESC GS B B            No       No       No       No       No         No           No           No            OK

                    ESC GS B C            No       No       No       No       No         No           No           No            OK




――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

STAR Graphic Mode Command Specifications            57
URL: http://www.starmicronics.com/support/
