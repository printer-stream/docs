# tm-t88iv_eng_trg_revc_02


<!-- page 1 -->

<!-- image -->

<!-- image -->

## Technical Reference Guide

## Product Overview

Describes features and general specifications for the product.

## Setup

Describes setup and instrallation of the product and peripherals.

## Application Development Information

Describes how to control the printer and necessary information when you develop applications.

## Handling

Describes how to handle the product.

## Replacement of the TM-T88III

Describes precautions for the replacement.

## Appendix

Describes interfaces, connectors and character code tables.

<!-- page 2 -->

## Cautions

- No part of this document may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of Seiko Epson Corporation.
- The contents of this document are subject to change without notice. Please contact us for the latest information.
- While  every  precaution  has  taken  in  the  preparation  of  this  document,  Seiko  Epson  Corporation assumes no responsibility for errors or omissions.
- Neither  is  any  liability  assumed  for  damages  resulting  from  the  use  of  the  information  contained herein.
- Neither Seiko Epson Corporation nor its affiliates shall be liable to the purchaser of this product or third parties for damages, losses, costs, or expenses incurred by the purchaser or third parties as a result of: accident, misuse, or abuse of this product or unauthorized modifications, repairs, or alterations to this product, or (excluding the U.S.) failure to strictly comply with Seiko Epson Corporation's operating and maintenance instructions.
- Seiko Epson Corporation shall not be liable against any damages or problems arising from the use of any options or any consumable products other than those designated as Original EPSON Products or EPSON Approved Products by Seiko Epson Corporation.

## Trademarks

EPSON and ESC/POS are registered trademarks of Seiko Epson Corporation in Japan and other countries/regions.

Microsoft and Windows are registered trademarks of Microsoft Corporation.

## ESC/POS ®  Command System

EPSON has been taking industry's initiatives with its own POS printer command system (ESC/POS). ESC/POS has a large number of commands including patented ones. Its high scalability enables users to build versatile POS systems. The system is compatible with all types of EPSON POS printers (excluding the TM-C100) and displays. Moreover, its flexibility makes it easy to upgrade the future. The functionality and the user-friendliness is valued around the world.

<!-- page 3 -->

## Revision History

| Revision   | page                      | Details of change                                                     |
|------------|---------------------------|-----------------------------------------------------------------------|
| Rev. A     | All pages                 | Newly authorized                                                      |
| Rev. B     | All page                  | All descriptions                                                      |
| Rev. C     | page 49                   | Standalone connection added for the USB interface connection diagram. |
| Rev. C     | page 53, page 62, page 83 | UB-R03 added.                                                         |
| Rev. C     | page 81                   | Note added.                                                           |
| Rev. C     | page 82                   | 'Buzzer' added.                                                       |

<!-- page 4 -->

## For Safety

## Key to Symbols

The symbols in t h i s ma nu al are i de nti f i ed by t he i r level of i mpor t a n ce, as def in ed below. Read t he follow ing caref u lly before ha n dl ing t he prod u c t .

<!-- image -->

<!-- image -->

You must follow warnings carefully to avoid serious bodily injury.

Provides information that must be observed to prevent damage to the equipment or loss of data.

- Possibility of sustaining physical injuries.
- Possibility of causing physical damage.
- Possibility of causing information loss.

Provides information that must be observed to avoid damage to your equipment or a malfunction.

Provides important information and useful tips.

<!-- page 5 -->

## Warnings

<!-- image -->

- To  avoid  risk  of  electric  shock,  do  not  set  up  this  product  or  handle  cables  during  a thunderstorm
- Never insert or disconnect the power plug with wet hands.

Doing so may result in severe shock.

- Handle the power cable with care.

Improper handling may lead to fire or electric shock.

- ∗ Do not modify or attempt to repair the cable.
- ∗ Do not place any heavy object on top of the cable.
- ∗ Avoid excessive bending, twisting, and pulling.
- ∗ Do not place the cable near heating equipment.
- ∗ Check that the plug is clean before plugging it in.
- ∗ Be sure to push the plug all the way in.
- Be sure to use the specified power source.

Connection to an improper power source may cause fire or shock.

- Do not place multiple loads on the power outlet.

Overloading the outlet may lead to fire.

- Shut down your equipment immediately if it produces smoke, a strange odor, or unusual noise .

Continued use may lead to fire. Immediately unplug the equipment and contact your dealer or a Seiko Epson service center for advice.

- Never attempt to repair this product yourself.

Improper repair work can be dangerous.

- Never disassemble or modify this product.

Tampering with this product may result in injury or fire.

- Do not allow foreign matter to fall into the equipment.

Penetration by foreign objects may lead to fire.

- If water or other liquid spills into this equipment, do not continue to use it. Continued use may lead to fire. Unplug the power cord immediately and contact your

dealer or a Seiko Epson service center for advice.

- If you open the DIP switch cover, be sure to close the cover and tighten the screw after adjusting the DIP switch.

Using this product with the cover open may cause fire or electric shock.

<!-- page 6 -->

## Cautions

<!-- image -->

- Do not connect cables in ways other than those mentioned in this manual. Different connections may cause equipment damage or fire.
- Be sure to set this equipment on a firm, stable, horizontal surface. The product may break or cause injury if it falls.
- Do not use this product in locations subject to high humidity or dust levels. Excessive humidity and dust may cause equipment damage or fire.
- Do not place heavy objects on top of this product. Never stand or lean on this product. Equipment may fall or collapse, causing breakage and possible injury.
- To  avoid  injury,  do  not  insert  fingers  or  any  part  of  the  hand  in  the  roll  paper opening where the manual cutter is installed.
- Do not open the roll paper cover without taking the necessary precautions, as this can result in injury from the autocutter fixed blade.
- Do  not  use  aerosol  sprayers  containing  flammable  gas  inside  or  around  this
- product. Doing so may cause fire.
- To ensure safety, unplug this product before leaving it unused for an extended period.

## Restriction of Use

Whe n t h i s prod u c t i s u sed for appl i ca ti o n s req ui r ing h ig h rel i ab i l it y/safe t y s u ch as t ra n spor t a ti o n dev i ces rela t ed t o av i a ti o n , ra i l, mar in e, a ut omo ti ve e t c.; d i sas t er preve nti o n dev i ces; var i o u s safe t y dev i ces e t c.; or f un c ti o n al/prec i s i o n dev i ces e t c., yo u sho u ld u se t h i s prod u c t o n ly af t er gi v ing co n s i dera ti o n t o in cl u d ing fa i l-safes a n d red un da n c i es int o yo u r des ign t o ma int a in safe t y a n d t o t al sys t em rel i ab i l it y. Beca u se t h i s prod u c t was n o t int e n ded for u se in appl i ca ti o n s req ui r ing ex t remely h ig h rel i ab i l it y/safe t y s u ch as aerospace eq ui pme nt , ma in comm uni ca ti o n eq ui pme nt , nu clear power co nt rol eq ui pme nt , or med i cal eq ui pme nt rela t ed t o d i rec t med i cal care e t c., please make yo u r ow n j u d g me nt o n t h i s prod u c t 's s uit ab i l it y af t er a f u ll eval u a ti o n .

<!-- page 7 -->

## About this Manual

## Aim of the Manual

Th i s ma nu al was crea t ed t o prov i de in forma ti o n o n developme nt , des ign , a n d in s t alla ti o n of POS sys t ems a n d developme nt a n d des ign of pr int er appl i ca ti o n s for developers.

## Manual Content

The ma nu al i s made u p of t he follow ing sec ti o n s:

Chapter 1

Product Overview

Chapter 2

Setup

Chapter 3

Application Development Information

Chapter 4

Handling

Chapter 5

Replacement of the TM-T88III

Appendix

Specifications of Interface and Connector

Character Code Tables

<!-- page 8 -->

## Contents

| ■ Revision History.....................................................................................................................                               | 3                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ■ For Safety ..............................................................................................................................                           | 4                                                                                                                                                        |
| Key to Symbols........................................................................................................................................4               |                                                                                                                                                          |
| Warnings..................................................................................................................................................5           |                                                                                                                                                          |
| Cautions                                                                                                                                                              | ..................................................................................................................................................6      |
| ■ Restriction of Use..................................................................................................................                                | 6                                                                                                                                                        |
| ■ About this Manual................................................................................................................                                   | 7                                                                                                                                                        |
| Aim of the Manual .................................................................................................................................7                  |                                                                                                                                                          |
| Manual                                                                                                                                                                | Content.....................................................................................................................................7            |
| ■ Contents................................................................................................................................                            | 8                                                                                                                                                        |
| Product Overview ........................................................................13                                                                           |                                                                                                                                                          |
| ■ Features...............................................................................................................................                             | 13                                                                                                                                                       |
| Product configuration........................................................................................................                                         |                                                                                                                                                          |
| ■                                                                                                                                                                     | 14                                                                                                                                                       |
| Interface................................................................................................................................................14           |                                                                                                                                                          |
| Buzzer.....................................................................................................................................................14         |                                                                                                                                                          |
| Color                                                                                                                                                                 | ......................................................................................................................................................14 |
| Accessories ...........................................................................................................................................14             |                                                                                                                                                          |
| ■ Parts Name and Function..................................................................................................                                           | 16                                                                                                                                                       |
| Power Switch.........................................................................................................................................16               |                                                                                                                                                          |
| Power Switch Cover .............................................................................................................................17                    |                                                                                                                                                          |
| Control Panel ........................................................................................................................................17              |                                                                                                                                                          |
| Connectors ...........................................................................................................................................18              |                                                                                                                                                          |
| Offline.....................................................................................................................................................18        |                                                                                                                                                          |
| ■ Error Status...........................................................................................................................                             | 19                                                                                                                                                       |
| Automatically Recoverable Errors ......................................................................................................19                             |                                                                                                                                                          |
| Recoverable Errors Unrecoverable Errors............................................................................................................................20 | ...............................................................................................................................19                        |
| ■ NV Memory (Non-Volatile Memory)................................................................................                                                     | 21                                                                                                                                                       |
| NV Graphics Memory..........................................................................................................................21                        |                                                                                                                                                          |
| ■ Product Specifications.......................................................................................................                                       | 23                                                                                                                                                       |
| Printing Specifications..........................................................................................................................24                   |                                                                                                                                                          |
| Character Specifications.....................................................................................................................25                       |                                                                                                                                                          |
| Printable Positions..............................................................................................................27                                   | Area.......................................................................................................................................26            |
| Printing and Cutting Paper Specifications                                                                                                                             | ............................................................................................................................27                           |
| Electrical Characteristics.....................................................................................................................28                     |                                                                                                                                                          |
| Environmental Conditions                                                                                                                                              | ...................................................................................................................29                                    |
| External Dimensions and Mass............................................................................................................30                            |                                                                                                                                                          |

<!-- page 9 -->

| ■ Option Specifications.........................................................................................................31                    |                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Power Supply Unit (PS-180)..................................................................................................................          | 31                                                                                                             |
| Setup.............................................................................................33                                                  |                                                                                                                |
| ■ Flow of Setup.......................................................................................................................33              |                                                                                                                |
| ■ Installing the Printer                                                                                                                              | ............................................................................................................34 |
| Important Notes on Horizontal Installation .......................................................................................                    | 34                                                                                                             |
| Important Notes on Wall Hanging.....................................................................................................                  | 34                                                                                                             |
| ■ Setting the DIP Switches.....................................................................................................35                     |                                                                                                                |
| Setting Procedure................................................................................................................................     | 35                                                                                                             |
| For Serial Interface...............................................................................................................................   | 36                                                                                                             |
| For Parallel/LAN/Wireless LAN Interface............................................................................................                   | 38                                                                                                             |
| For USB Interface..................................................................................................................................   | 40                                                                                                             |
| Selecting the Print Density (DIP Switch 2-3/2-4)................................................................................                      | 41                                                                                                             |
| Selecting the BUSY Status....................................................................................................................         | 42                                                                                                             |
| ■ Setting the Memory Switches............................................................................................43                           |                                                                                                                |
| ■ Adjusting the Paper Roll Near-End Sensor .......................................................................45                                  |                                                                                                                |
| ■ Connecting the Printer to the Host Computer .................................................................46                                     |                                                                                                                |
| For Serial Interface...............................................................................................................................   | 46                                                                                                             |
| For Parallel Interface............................................................................................................................    | 48                                                                                                             |
| For USB Interface..................................................................................................................................   | 49                                                                                                             |
| For LAN Interface .................................................................................................................................   | 51                                                                                                             |
| For Wireless LAN Interface...................................................................................................................         | 53                                                                                                             |
| ■ Connecting the Power Supply Unit (PS-180) ....................................................................54                                    |                                                                                                                |
| Connecting the Power Supply Unit....................................................................................................                  | 54                                                                                                             |
| ■ Connecting the Cash Drawer............................................................................................55                            |                                                                                                                |
| Connecting the Drawer Kick-out Cable...........................................................................................                       | 55                                                                                                             |
| Setting the Buzzer.................................................................................................................................   | 56                                                                                                             |
| Application Development Information......................................57                                                                           |                                                                                                                |
| ■ How to Control the Printer ..................................................................................................57                     |                                                                                                                |
| Selecting a Driver.................................................................................................................................   | 57                                                                                                             |
| ESC/POS Command............................................................................................................................           | 58                                                                                                             |
| ■ Software and Manuals                                                                                                                                | .......................................................................................................62      |
| Download............................................................................................................................................. | 63                                                                                                             |
| ■ Setting Check Modes.........................................................................................................64                      |                                                                                                                |
| Self-test Mode......................................................................................................................................  | 64                                                                                                             |
| Hexadecimal Dumping Mode...........................................................................................................                   | 65                                                                                                             |

<!-- page 10 -->

| Handling                                                                                                                                                               | .......................................................................................67                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ■ Installing and Replacing Roll Paper .................................................................................                                                | 67                                                                                                                                                            |
| ■ Attaching/Removing the Connector Cover....................................................................                                                           | 69                                                                                                                                                            |
| Attaching the Connector Cover........................................................................................................69                                |                                                                                                                                                               |
| Removing the Connector Cover........................................................................................................69                                 |                                                                                                                                                               |
| ■ Removing Jammed Paper                                                                                                                                                | ................................................................................................ 70                                                           |
| When the Roll Paper Cover Cannot be Opened.............................................................................70                                              |                                                                                                                                                               |
| ■ Cleaning the Thermal Head..............................................................................................                                              | 72                                                                                                                                                            |
| ■ Preparing for Transport.......................................................................................................                                       | 72                                                                                                                                                            |
| Replacement of the TM-T88III.....................................................73                                                                                    |                                                                                                                                                               |
| ■ Compatibility......................................................................................................................                                  | 73                                                                                                                                                            |
| Printing...................................................................................................................................................73          |                                                                                                                                                               |
| Print Density...........................................................................................................................................73             |                                                                                                                                                               |
| Print Speed............................................................................................................................................73              |                                                                                                                                                               |
| Number of Head Energizing Parts                                                                                                                                        | ......................................................................................................74                                                      |
| Printable Area.......................................................................................................................................74                |                                                                                                                                                               |
| Cutting Method....................................................................................................................................74                   |                                                                                                                                                               |
| Receive Buffer.......................................................................................................................................74                |                                                                                                                                                               |
| Memory Capacity................................................................................................................................74                      |                                                                                                                                                               |
| Electrical Characteristics.....................................................................................................................75                      |                                                                                                                                                               |
| DIP Switches..........................................................................................................................................75               |                                                                                                                                                               |
| Printer Status..........................................................................................................................................75             |                                                                                                                                                               |
| Hexadecimal Dumping                                                                                                                                                    | .......................................................................................................................75                                     |
| Logo Registration..................................................................................................................................75                  |                                                                                                                                                               |
| Driver Compatibility                                                                                                                                                   | .............................................................................................................................76                               |
| Accessories                                                                                                                                                            | ...........................................................................................................................................76                 |
| Overall Dimensions...............................................................................................................................77                    |                                                                                                                                                               |
| ■ Additional Functions and Functional Improvements......................................................                                                               | 79                                                                                                                                                            |
| Print Speed............................................................................................................................................79              |                                                                                                                                                               |
| High-Speed Graphic Printing ..............................................................................................................79                           |                                                                                                                                                               |
| Two-Dimensional                                                                                                                                                        | Code........................................................................................................................79                                |
| Number of Characters.........................................................................................................................79                        |                                                                                                                                                               |
| NV Graphics..........................................................................................................................................80 Page Mode Area | .................................................................................................................................80                           |
| Transmission Speed (For Serial Interface)...........................................................................................80                                 |                                                                                                                                                               |
| Customized Value                                                                                                                                                       | ................................................................................................................................81                            |
| USB Interface.........................................................................................................................................81               |                                                                                                                                                               |
| USB Low Power Consumption Mode..................................................................................................81                                     |                                                                                                                                                               |
| Maintenance Counter.........................................................................................................................81                         |                                                                                                                                                               |
| Supply                                                                                                                                                                 | Buzzer.....................................................................................................................................................82 |
| Power Box..................................................................................................................................82                          |                                                                                                                                                               |

<!-- page 11 -->

| Appendix......................................................................................83                                                |     |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| ■ Specifications of Interface and Connector .....................................................................83                             |     |
| RS-232C Serial Interface......................................................................................................................  |  83 |
| IEEE 1284 Parallel Interface .................................................................................................................  |  86 |
| USB (Universal Serial Bus) Interface ....................................................................................................       |  89 |
| ■ Character Code Tables......................................................................................................90                 |     |
| Common to All Pages.........................................................................................................................    |  90 |
| Page 0 [PC437: USA, Standard Europe]............................................................................................                |  91 |
| Page 1 (Katakana).............................................................................................................................. |  92 |
| Page 2 (PC850: Multilingual) ..............................................................................................................     |  93 |
| Page 3 (PC860: Portuguese)...............................................................................................................       |  94 |
| Page 4 (PC863: Canadian-French)...................................................................................................              |  95 |
| Page 5 (PC865: Nordic) ......................................................................................................................   |  96 |
| Page 16 (WPC1252).............................................................................................................................  |  97 |
| Page 17 (PC866: Cyrillic #2)................................................................................................................    |  98 |
| Page 18 (PC852: Latin2)......................................................................................................................   |  99 |
| Page 19 (PC858: Euro).......................................................................................................................    | 100 |
| Page 255 (User-Defined Page).........................................................................................................           | 101 |
| International Character Sets ............................................................................................................       | 102 |

<!-- page 12 -->



<!-- page 13 -->

## Product Overview

Th i s chap t er descr i bes fea tu res a n d spec i f i ca ti o n s of t he prod u c t .

## Features

## Printing

- Iss uing of ba t ch rece i p t s i s poss i ble. (200 mm/s max i m u m)
- Graph i cs are also pr int ed w it h h ig h-speed pr inting .
- Two-color pr inting i s poss i ble o n t he t wo-color t hermal paper.

## Handling

- Easy dropin paper load ing

## Software

- Comma n d pro t ocol i s based o n t he ESC/POS ®  Propr i e t ary Comma n d Sys t em.
- OPOS ADK a n d W in dows ®  pr int er dr i ver are ava i lable.
- I n add iti o n t o s u ppor ting several k in ds of bar code pr inting , t wo-d i me n s i o n al code (PDF417, QR code) pr inting i s poss i ble.
- Var i o u s layo ut s are poss i ble by u s ing pa g e mode.
- A ma int e n a n ce co unt er f un c ti o n i s s u ppor t ed.

## Interface

Var i o u s int erface boards (EPSON UB ser i es) ca n be u sed.

1

<!-- page 14 -->

## Product configuration

## Interface

- Ser i al int erface model (RS-232C)
- Parallel int erface model (IEEE1284)
- USB int erface model (f u ll-speed)
- E t her n e t int erface model (10/100BASE-T)
- W i reless LAN int erface model (IEEE802.11b)

## Buzzer

- Model w it h t he b u zzer f un c ti o n
- Model w it ho ut t he b u zzer f un c ti o n

## Color

- ECW (Epso n Cool Wh it e)
- EDG (Epso n Dark Gray)

## Accessories

## Attachments

- Roll paper (for opera ti o n check)
- User's ma nu al
- Power sw it ch cover
- Co nn ec t or cover
- Lock ing w i re saddle (o n ly for USB int erface model)

<!-- page 15 -->

## Options

- Ex t er n al power s u pply (Model: PS-180)
- AC cable for t he PS-180.
- Power s u pply box (Model: BX88W/OT-BX88B)
- Aff i x ing t apes for f i x ing t he pr int er (Model: DF-10)
- Wall ha nging bracke t (Model: WH-10)
- I nt erface boards (UB ser i es)

1

<!-- page 16 -->

## Parts Name and Function

<!-- image -->

## Power Switch

T u r n s t he pr int er o n or off. The marks o n t he sw it ch: ( / )

<!-- image -->

Before turning on the printer, be sure to check that the AC adapter is connected to the power supply.

Before turning the printer off, it is recommended to send a power-off command to the printer. If you use the power-off sequence, the latest maintenance counter values are saved. (Maintenance counter values are usually saved every two minutes.) For detailed information about ESC/POS commands, see the ESC/POS Application Programing Guide.

<!-- page 17 -->

## Power Switch Cover

I n s t all t he power sw it ch cover t ha t comes w it h t he TM-T88IV o nt o t he pr int er t o preve nt in adver t e nt cha nging of t he power sw it ch, t o preve nt t amper ing , a n d t o i mprove t he appeara n ce of t he pr int er.

To rese t t he pr int er whe n t he power sw it ch cover i s in s t alled, in ser t a lo ng , t h in objec t (s u ch as t he e n d of a paper cl i p) int o t he hole in t he power sw it ch cover a n d press t he power sw it ch.

<!-- image -->

If an accident occurs with the power switch cover attached, unplug the power cord immediately.

Continued use may cause fire or shock.

## Control Panel

## LED

## POWER LED (green)

- L ig h t s whe n t he power s u pply i s o n .
- Goes o ut whe n t he power s u pply i s tu r n ed off.

## ERROR LED

L ig h t s or flashes whe n t he pr int er i s offl in e.

- L ig h t s  af t er t he power i s tu r n ed o n or  af t er a rese t (offl in e).  A ut oma ti cally g oes o ut af t er a wh i le t o in d i ca t e t ha t t he pr int er i s ready.
- L ig h t s whe n t he e n d of t he roll paper i s de t ec t ed, a n d whe n pr inting has s t opped (offl in e). If t h i s happe n s, replace t he roll paper.
- Flashes whe n a n error occ u rs. (For de t a i ls abo ut t he flash codes, see "Error S t a tu s" o n pa g e 19.)
- Goes o ut d u r ing re gu lar opera ti o n (o n l in e).

<!-- image -->

1

<!-- page 18 -->

## PAPER OUT LED

- L ig h t s whe n t here i s n o more roll paper or t here i s l itt le rema ining .
- Off whe n t here i s a s u ffic i e nt amo unt of roll paper rema ining .
- Flashes whe n a selft es t i s in pro g ress.

## FEED button

Press ing t h i s b utt o n o n ce feeds t he roll paper by o n e l in e. Hold ing t h i s b utt o n dow n feeds t he roll paper co ntinu o u sly.

## Connectors

All cables are co nn ec t ed t o t he co nn ec t or pa n el o n t he lower rear of t he pr int er.

Drawer kick-out connector

<!-- image -->

- Drawer k i ck-o ut co nn ec t or:

Co nn ec t s t he cash drawer.

- Power s u pply co nn ec t or:

Co nn ec t s t he power s u pply unit

- I nt erface co nn ec t or:

Co nn ec t s t he pr int er w it h t he hos t comp ut er int erface.

The picture above shows a serial interface model. For details on the various interfaces and how to connect the power supply connector and cash drawer, see "Connecting the Printer to the Host Computer" on page 46 and "Connecting the Cash Drawer" on page 55.

## Offline

The pr int er a ut oma ti cally g oes offl in e un der t he follow ing co n d iti o n s:

- D u r ing power o n ( in cl u d ing rese tting w it h t he int erface) unti l t he pr int er i s ready
- D u r ing t he selft es t
- Wh i le roll paper i s fed u s ing t he FEED b utt o n .
- Whe n t he pr int er s t ops pr inting d u e t o a paper-e n d ( i f a n emp t y paper s u pply i s de t ec t ed by t he roll paper e n d se n sor or i f t he dr i ver has bee n se t t o s t op pr inting whe n a roll paper n eare n d i s de t ec t ed)
- Whe n a n error has occ u rred

<!-- page 19 -->

## Error Status

There are t hree poss i ble error t ypes: a ut oma ti cally recoverable errors, recoverable errors, a n d un recoverable errors.

## Automatically Recoverable Errors

Pr inting i s n o lo ng er poss i ble whe n a ut oma ti cally recoverable errors occ u r. They ca n be recovered eas i ly, as descr i bed below.

| Error                        | Error description                                                       | Error LED flash code Approx. 160 ms   | Recovery measure                                            |
|------------------------------|-------------------------------------------------------------------------|---------------------------------------|-------------------------------------------------------------|
| Roll paper cover open error  | The roll paper cover was opened during printing.                        |                                       | Recovers automatically when the roll paper cover is closed. |
| Print head temperature error | A high temperature outside the head drive operating range was detected. |                                       | Recovers automatically when the print head cools.           |

## Recoverable Errors

Pr inting i s n o lo ng er poss i ble whe n recoverable errors occ u r. They ca n be recovered eas i ly by tu r ning t he power o n a g a in or se n d ing a n error recovery comma n d from t he dr i ver af t er el i m in a ting t he ca u se of t he error.

| Error            | Error description                   | Error LED flash code Approx. 160 ms   | Recovery measure                                                                                                                                       |
|------------------|-------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Autocutter error | Autocutter does not work correctly. | Approx.2.56 s                         | Remove the jammed paper or foreign matter in the printer, close the roll paper cover, send the error recover command, or turn the power on to recover. |

The error recovery command is valid only if a recoverable error (excluding automatically recoverable errors) occurs.

1

<!-- page 20 -->

## Unrecoverable Errors

Pr inting i s n o lo ng er poss i ble whe n un recoverable errors occ u r. The pr int er m u s t be repa i red.

<!-- image -->

Turn off the power immediately when unrecoverable errors occur.

<!-- image -->

| Error                             | Error description                                        | Error LED flash code Approx. 160 ms   |
|-----------------------------------|----------------------------------------------------------|---------------------------------------|
| Memory R/W error                  | After R/W checking, the printer does not work correctly. |                                       |
| High voltage error                | The power supply voltage is extremely high.              |                                       |
| Low voltage error                 | The power supply voltage is extremely low.               |                                       |
| CPU execution error               | The CPU is executing an incorrect address.               |                                       |
| Internal circuit connection error | Internal circuits are not connected correctly.           | Approx.2.56 s                         |
| UIB error                         | An abnormal operation occurs in UIB.                     |                                       |

<!-- page 21 -->

## NV Memory (Non-Volatile Memory)

The pr int er has NV memory wh i ch in cl u des t he u ser NV memory a n d NV g raph i cs memory t ha t u sers ca n u se.

<!-- image -->

NV memory can be rewritten about 100,000 times. As a guide, NV memory rewriting should be 10 times or less a day when you program applications.

## NV Graphics Memory

Graph i cs s u ch as shop lo g os t o be pr int ed o n rece i p t s ca n be s t ored. Eve n w it h a ser i al int erface model whose comm uni ca ti o n speed i s low, h ig h speed g raph i c pr inting i s poss i ble.

Use t he TM Flash Lo g o Se tu p uti l it y for NVRAM t o re gi s t er g raph i cs.

## NV Graphics Print Mode

I n t h i s mode t he pr int er pr int s t he follow ing :

- Capac it y of t he NV g raph i cs
- Used amo unt of t he NV g raph i cs
- U nu sed capac it y of t he NV g raph i cs
- N u mber of t he NV g raph i cs t ha t are re gi s t ered
- Key code, nu mber of do t s in X d i rec ti o n , nu mber of do t s in Y d i rec ti o n , nu mber of colors t o be def in ed.
- NV g raph i cs da t a

1

<!-- page 22 -->

## Procedure

- 1 Open the roll paper cover.
- 2 While pressing the FEED button, turn the power on.
- 3 Press the FEED button once.
- 4 Close the roll paper cover.
- 5 After instructions are printed, open the roll paper cover.
- 6 Press the FEED button once.
- 7 Close the roll paper cover.

T u r n t he power off a n d o n t o re tu r n t o t he n ormal mode.

<!-- page 23 -->

## Product Specifications

| Printing method                       | Printing method                       | Thermal line printing                                                                                  |
|---------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------|
| Cutting method                        | Cutting method                        | Partial cut (cutting with one point in left edge left uncut)                                           |
| Roll paper (single-ply)               | Roll paper (single-ply)               | Width: 79.5 ± 0.5 mm(3.13 ± 0.02")                                                                     |
| Interface                             | Interface                             | Serial (RS232C), Parallel (IEEE1284), LAN (10/100BASE-T), USB (Full-speed), Wireless LAN (IEEE802.11b) |
| Buffer                                | Receive buffer                        | 4 KB/45 bytes (selectable using the DIP switch 1-2)                                                    |
| Buffer                                | Downloaded buffer                     | 12 KB (both for user-defined characters and downloaded images)                                         |
| Buffer                                | NV graphics data                      | 256 KB                                                                                                 |
| Barcode/two-dimensional code printing | Barcode/two-dimensional code printing | UPC-A, UPC-E JAN 8 (EAN 8), JAN 13 (EAN 13) CODE 39 ITF CODABAR (NW-7) CODE 93 CODE 128 PDF417 QR CODE |
| DKD Function                          | DKD Function                          | 2 drives                                                                                               |
| Supplied voltage                      | Supplied voltage                      | + 24 VDC ± 7%                                                                                          |
| Life                                  | Mechanism                             | 15,000,000 lines                                                                                       |
| Life                                  | Thermal head                          | 100 million pulses Single-color printing: 100 km Two-color printing: 50 km                             |
| Life                                  | Autocutter                            | 1,5000,000 cuts                                                                                        |
| Life                                  | MTBF                                  | 360,000 hours                                                                                          |
| Life                                  | MCBF                                  | 52,000,000 lines                                                                                       |
| Temperature/humidity                  | Temperature/humidity                  | Operating: 5 to 45°C {41 to 113°F}, 10 to 90% RH Storage: -10 to 50°C {14 to 122°F}, 10 to 90% RH      |
| Overall dimensions                    | Overall dimensions                    | 148 × 145 × 195 mm{5.83 × 5.71 × 7.68"} (H × W×D)                                                      |
| Weight (mass)                         | Weight (mass)                         | Approx. 1.8 kg {3.96 lb} (Roll paper excluded)                                                         |

1

<!-- page 24 -->

## Printing Specifications

| Printing method         | Printing method          | Thermal line printing                                              |
|-------------------------|--------------------------|--------------------------------------------------------------------|
| Dot density             | Dot density              | 180 × 180 dpi                                                      |
| Printing direction      | Printing direction       | Unidirectional with friction feed (Reverse feed is not supported.) |
| Maximum printable width | Maximum printable width  | 72.2 mm, 512 dots                                                  |
| Character per line      | Font A (12 × 24)         | 42                                                                 |
| Character per line      | Font B (9 × 17)          | 56                                                                 |
| Maximum print speed* 1  | High speed mode          | 200 mm/s                                                           |
| Maximum print speed* 1  | Lowpowerconsumption mode | 150 mm/s                                                           |
| Line spacing            | Line spacing             | 4.23 mm{1/6"} (Factory setting, programmable by command)           |

dp i

: do t s per in ch

*1: whe n t he pr int er pr int s w it h t he defa u l t pr int de n s it y level a t 24V a n d 25°C {77°F}.

<!-- image -->

- Printing speed may be slower, depending on the such items as the data transmission speed.
- High speed mode/low power consumption mode can be shifted with a DIP switch (2-3/2-4).

<!-- page 25 -->

## Character Specifications

| Number of characters   | Number of characters   | Alphanumeric characters: 95 Extended graphics: 128 × 11 pages (including user-defined page) International characters: 48 GB18030-2000: 28,533 (for Simplified Chinese characters Model) Big 5: 13,535 (for Traditional Chinese characters Model)   |
|------------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Character structure    | Character structure    | Font A (Initial setting): 12 × 24 (including 2-dot spacing in horizontal) Font B: 9 × 17 (including 2-dot spacing in horizontal)                                                                                                                   |
| Character size         | Font A                 | Standard: 1.41 × 3.39mm Double-height: 1.41 × 6.77mm Double-width: 2.82 × 3.39mm Double-width, double-height: 2.82 × 6.77mm                                                                                                                        |
| Character size         | Font B                 | Standard: 0.99 × 2.40mm Double-height: 0.99 × 4.80mm Double-width: 1.98 × 2.40mm Double-width, double-height: 1.98 × 4.80mm                                                                                                                        |

## No t e)

1. Space be t wee n charac t ers i s n o t in cl u ded.
2. Charac t ers ca n be scaled u p t o 64 ti mes as lar g e as t he s t a n dard s i ze.

1

<!-- page 26 -->

## Printable Area

The pr int able area of a paper w it h w i d t h of 79.5 ± 0.5 mm {3.13 ± 0.02"} i s 72.2 ± 0.2 mm {2.84 ± 0.008"} (512 do t s) a n d t he space o n t he r ig h t a n d lef t s i des are approx i ma t ely 3.7 ± 2 mm {0.15 ± 0.079"}.

<!-- image -->

All the numeric values are typical.

<!-- image -->

<!-- page 27 -->

## Printing and Cutting Positions

<!-- image -->

<!-- image -->

The values above may vary slightly as a result of paper slack or variations in the paper. Take the notice into account when setting the cutting position of the autocutter.

## Paper Specifications

| Paper type                | Paper type                | Specified thermal paper                                                                                                                                                                              |
|---------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Form                      | Form                      | Roll paper                                                                                                                                                                                           |
| Size                      | Roll paper diameter       | 83 mm{3.27 " } maximum                                                                                                                                                                               |
| Size                      | Roll paper spool          | Inside: 12 mm{0.47 " }, Outside: 18 mm{0.71 " }                                                                                                                                                      |
| Size                      | Take-up roll paper width  | 80 + 0.5/-1.0mm                                                                                                                                                                                      |
| Size                      | Paper width               | 79.5 ± 0.5mm                                                                                                                                                                                         |
| Specified roll paper type | Specified roll paper type | NTP080-80 In U.S.A.: Nakagawa Mfg. (USA) Inc. In Europe: Nakagawa Mfg. (Europe) GmbH In Southeast Asia: N.A.K. Mfg. (Malaysia) SDN BHD (Original paper: TF50KS-E Nippon Paper Industries Co., Ltd.Åj |

- Paper must not be pasted to the roll paper spool.
- The remaining amount of the roll paper when a roll paper near-end is detected differs depending on the spool type.

1

<!-- page 28 -->

## Electrical Characteristics

|                                                          | High           | speed mode Low current consumption mode                                                                                                                                                                         |
|----------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Supply voltage                                           | Supply voltage | DC24V ± 7%                                                                                                                                                                                                      |
| Current consumption (at 24V, 25°C, normal print density) | Standby        | Mean: Approximately 0.1A Maximum 1A for drawer kick-out driving.                                                                                                                                                |
| Current consumption (at 24V, 25°C, normal print density) | Operating      | Mean: Approximately 1.8A Mean: Approximately 1.2A Note) When print ratio is approximately 18% • Font A • 42 columns • ASCII character continuous printing for 100 lines (repeats 20H-7FH) #$%&' $%&' 42 columns |

<!-- page 29 -->

## Environmental Conditions

<!-- image -->

| Temperature                | Operating                  | 5 to 45°C {41 to 113°F}, 10 to 90% RH (See the operating temperature and humidity range below.)                                                                                                                                                        |
|----------------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature                | Storage (Factory packing)  | -10 to 50°C {14 to 122°F}, 10 to 90% RH (except for paper)                                                                                                                                                                                             |
|                            |                            | Relative humidity Operating environment range 90 65 10 [%RH] 34°C, 90% 40°C, 65% 45°C, 50%                                                                                                                                                             |
| Acoustic noise (Operating) | Acoustic noise (Operating) | Approximately 55 dB (Bystander position) Note) The values above are measured in the Epson evaluation condition. The acoustic noise differs depending on the paper used, printing contents, or the setting values such as print speed or print density. |

1

<!-- page 30 -->

## External Dimensions and Mass

- He ig h t : Approx i ma t ely 148 mm {5.83"}
- W i d t h: Approx i ma t ely 145 mm {5.71"}
- Dep t h: Approx i ma t ely 195 mm {7.68"}
- Mass: Approx i ma t ely 1.8 k g {3.96 lb} (excep t for roll paper)

<!-- image -->

<!-- image -->

<!-- page 31 -->

## Option Specifications

## Power Supply Unit (PS-180)

<!-- image -->

[Unit: mm]

| Electric characteristics   | Input conditions     | input voltage (rating): 90 to 264VAC (100VAC -10% to 230VAC +15%)   |
|----------------------------|----------------------|---------------------------------------------------------------------|
| Electric characteristics   | Input conditions     | Frequency (rating): 50/60 Hz ± 3 Hz                                 |
| Electric characteristics   | Input conditions     | Power consumption (rating): 100VA                                   |
| Electric characteristics   | Output conditions    | Output voltage (rating): 24VDC ± 5%                                 |
| Electric characteristics   | Output conditions    | Output current (rating): 2.0A                                       |
| Electric characteristics   | Output conditions    | Output electric power (rating): 48VA                                |
| Electric characteristics   | Output conditions    | Output peak current: 4.5A                                           |
| Case specifications        | Dimensions (H × W×D) | 68 × 136 × 32 mm{2.68 × 5.35 × 1.26"} (excluding projections)       |
| Case specifications        | Weight               | Approx. 0.4 kg {14.11 oz} (excluding the AC cable)                  |
| Case specifications        | Color                | Black (matte)                                                       |

## Material

No spec i f i c brom in a t ed flame re t arda nt s, s u ch as PBBE a n d PBB, are u sed in t h i s prod u c t .

## AC cable selection

Selec t a n AC cable t ha t sa ti sf i es t he follow ing co n d iti o n s.

- Safe t y s t a n dard prod u c t
- Pl ug w it h PE t erm in al

## Ground connections

Be s u re t o g ro un d for safe t y.

1

<!-- page 32 -->



<!-- page 33 -->

## Setup

Th i s chap t er descr i bes se tu p a n d in s t alla ti o n of t he prod u c t a n d per i pherals.

## Flow of Setup

Th i s chap t er co n s i s t s of t he follow ing sec ti o n s alo ng w it h t he se tu p flow of t he prod u c t a n d per i pherals.

<!-- image -->

<!-- page 34 -->

## Installing the Printer

Yo u ca n in s t all t h i s pr int er hor i zo nt ally. W it h a n op ti o n al ha nging bracke t (WH-10), yo u ca n also a tt ach t he pr int er t o a wall.

## Important Notes on Horizontal Installation

- The pr int er m u s t be in s t alled hor i zo nt ally.
- Do n o t place t he pr int er in d u s t y loca ti o n s.
- Do n o t p ut heavy i mpac t s o n t he pr int er. They may ca u se defec ti ve pr int .
- Do n o t ca t ch cables or fore ign ma tt er un der t he pr int er.

## Important Notes on Wall Hanging

Yo u n eed t o perform t he follow ing t asks t o in s t all t he pr int er o n a wall. For more de t a i ls, see t he in s t alla ti o n ma nu al for t he op ti o n al wall ha nging bracke t (WH-10).

- I n s t all ing t he roll-paper s t oppers
- Cha nging t he loca ti o n of t he roll paper n ear-e n d se n sor
- A tt ach ing t he co nn ec t or cover
- A tt ach ing t he wall ha nging bracke t (WH-10)

For t he o t her n o t es, see t he in s t alla ti o n ma nu al for t he op ti o n al wall ha nging bracke t (WH-10).

<!-- image -->

Be sure to attach the connector cover when you use the printer on a wall using the wall hanging bracket.

<!-- page 35 -->

## Setting the DIP Switches

O n t h i s pr int er, yo u ca n make var i o u s se tting s w it h DIP sw it

F un c ti o n s of t he DIP sw it ches d i ffer depe n d ing o n t he int

ches. erface.

For models with the buzzer function, see also "Setting the Buzzer" on page 56.

## Setting Procedure

Follow t he s t eps below t o cha ng e t he DIP sw it ch se tting s.

<!-- image -->

Before you remove the DIP switch cover, turn the printer off.

Otherwise, a short-circuit may cause the printer to malfunction.

DIP switch settings are enabled only when the power is turned on or the printer is reset via the interface. If the settings are changed after that, the functions will not change.

- 1 Make sure the power supply for the printer is turned off.
- 2 Unscrew the screw to remove the DIP switch cover from the base of the printer.
- 3 Set the DIP switches, using the tip of a tool, such as a small screwdriver.
- 4 Replace the DIP switch cover, and screw it in place.

<!-- image -->

<!-- page 36 -->

## For Serial Interface

## DIP Switch Bank 1

| SW   | Function                      | ON                                          | OFF                                         | Factory setting   |
|------|-------------------------------|---------------------------------------------|---------------------------------------------|-------------------|
| 1-1  | Data reception error          | Ignored                                     | Prints '?'                                  | OFF               |
| 1-2  | Receive buffer capacity       | 45 bytes                                    | 4 KB                                        | OFF               |
| 1-3  | Handshaking                   | XON/XOFF                                    | DTR/DSR                                     | OFF               |
| 1-4  | Word length                   | 7 bits                                      | 8 bits                                      | OFF               |
| 1-5  | Parity check                  | Yes                                         | No                                          | OFF               |
| 1-6  | Parity selection              | Even                                        | Odd                                         | OFF               |
| 1-7  | Transmission speed selections | See the ' Transmission speed (DIP switch 1- | See the ' Transmission speed (DIP switch 1- | ON                |
| 1-8  | Transmission speed selections | 7/1-8)' table below.                        | 7/1-8)' table below.                        | OFF               |

For DIP switch 1-2 (Receive buffer capacity), see also DIP switch 2-5 (Setting the release condition of the receive buffer BUSY state).

Transmission speed (DIP switch 1-7/1-8)

| Transmission speed (bps)                                                                                  | SW 1-7   | SW 1-8   |
|-----------------------------------------------------------------------------------------------------------|----------|----------|
| 38400 (Initial value)                                                                                     |          |          |
| 2400, 4800, 9600, 19200, 38400, 57600, 115200 (When setting with a command/Memory Switch Setting Utility) | ON       | ON       |
| 4800                                                                                                      | OFF      | ON       |
| 9600                                                                                                      | ON       | OFF      |
| 19200                                                                                                     | OFF      | OFF      |

bps: b

it s per seco n d

<!-- page 37 -->

- The transmission speed can be set with a command or the memory switch utility. (Setting values: 2400, 4800, 9600, 19200, 38400, 57600, 115200) The value set with a command or the memory switch utility is enabled only when DIP switches 1-7 and 1-8 are on. For other settings, the value set with the DIP switches is enabled.
- Depending on print conditions such as print duty, print head temperature, and data transmission speed, print speed is automatically adjusted, which can cause white lines due to intermittent print (the motor sometimes stops). To avoid this, set the transmission speed higher or keep the print speed constant by setting it lower. (See "Setting the Memory Switches" on page 43.)

## DIP Switch Bank 2

| SW        | Function                                                                                                                       | ON                                                                                           | OFF                                                                                          | Factory setting   |
|-----------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------|
| 2-1       | Handshaking (BUSY condition)                                                                                                   | Receive buffer full                                                                          | • Offline • Receive buffer full                                                              | OFF               |
| 2-2       | Reserved (Do not change settings)                                                                                              | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-3 ∼ 2-4 | Selects print density/Low power consumption mode                                                                               | See "Selecting the Print Density (DIP Switch 2-3/2-4)" on page 41.                           | See "Selecting the Print Density (DIP Switch 2-3/2-4)" on page 41.                           | OFF               |
| 2-5       | Setting the release condition of the receive buffer BUSY state (This function is effective when DIP switch 1-2 is set to off.) | Releases the BUSY state when the remaining capacity of the receive buffer reaches 138 bytes. | Releases the BUSY state when the remaining capacity of the receive buffer reaches 256 bytes. | OFF               |
| 2-6       | Reserved (Do not change settings)                                                                                              | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-7       | I/F pin 6 reset signal                                                                                                         | Enabled                                                                                      | Disabled                                                                                     | OFF               |
| 2-8       | IF pin 25 reset signal                                                                                                         | Enabled                                                                                      | Disabled                                                                                     | OFF               |

- For DIP switch 2-1 (BUSY condition), see also "Selecting the BUSY Status" on page 42.
- Do not change the setting of DIP switches 2-2 and 2-6. Otherwise, the printer may not operate normally.

<!-- page 38 -->

## For Parallel/LAN/Wireless LAN Interface

## DIP switch bank 1

| SW        | Function                                                                       | ON             | OFF                                                               | Factory setting   |
|-----------|--------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------|-------------------|
| 1-1       | Auto line feed                                                                 | Always enabled | Always disabled                                                   | OFF               |
| 1-2       | Receive buffer capacity                                                        | 45 bytes       | 4 KB                                                              | OFF               |
| 1-3       | Selects paper sensors to output paper-end signals (default value of a command) | Disabled       | Roll paper end sensor enabled, roll paper near-end sensor enabled | OFF               |
| 1-4       | Error signal output                                                            | Disabled       | Enabled                                                           | OFF               |
| 1-5 ∼ 1-8 | Undefined                                                                      | -              | -                                                                 | OFF               |

## DIP switch bank 2

| SW        | Function                                                                                                                       | ON                                                                                           | OFF                                                                                          | Factory setting   |
|-----------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------|
| 2-1       | Handshaking (BUSY condition)                                                                                                   | Receive buffer full                                                                          | • Offline • Receive buffer full                                                              | OFF               |
| 2-2       | Reserved (Do not change setting)                                                                                               | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-3 ∼ 2-4 | Selects print density/Low power consumption mode                                                                               | See "Selecting the Print Density (DIP Switch 2-3/2-4)" on page 41.                           | See "Selecting the Print Density (DIP Switch 2-3/2-4)" on page 41.                           | OFF               |
| 2-5       | Setting the release condition of the receive buffer BUSY state (This function is effective when DIP switch 1-2 is set to off.) | Releases the BUSY state when the remaining capacity of the receive buffer reaches 138 bytes. | Releases the BUSY state when the remaining capacity of the receive buffer reaches 256 bytes. | OFF               |
| 2-6 ∼ 2-7 | Reserved (Do not change settings)                                                                                              | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-8       | IF pin 31 reset signal (Do not change settings)                                                                                | Fixed to ON                                                                                  | Fixed to ON                                                                                  | ON                |

<!-- page 39 -->

- For DIP switch 2-1 (BUSY condition), see also "Selecting the BUSY Status" on page 42.
- Do not change the setting of DIP switches 2-2, 2-6, and 2-7. Otherwise, the printer may not operate normally.

<!-- page 40 -->

## For USB Interface

## DIP switch bank 1

| SW        | Function                             | ON             | OFF             | Factory setting   |
|-----------|--------------------------------------|----------------|-----------------|-------------------|
| 1-1       | Auto line feed                       | Always enabled | Always disabled | OFF               |
| 1-2       | Receive buffer capacity              | 45 bytes       | 4 KB            | OFF               |
| 1-3 ∼ 1-7 | Undefined                            | -              | -               | OFF               |
| 1-8       | Setting of USB power-saving function | Disabled       | Enabled         | OFF               |

## DIP switch bank 2

| SW        | Function                                                                                                                       | ON                                                                                           | OFF                                                                                          | Factory setting   |
|-----------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------|
| 2-1       | Handshaking (BUSY condition)                                                                                                   | Receive buffer full                                                                          | • Offline • Receive buffer full                                                              | OFF               |
| 2-2       | Reserved (Do not change setting)                                                                                               | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-3 ∼ 2-4 | Selects print density/Low power consumption mode                                                                               | See "Selecting the Print Density (DIP Switch 2-3/2-4)" on page 41.                           | See "Selecting the Print Density (DIP Switch 2-3/2-4)" on page 41.                           | OFF               |
| 2-5       | Setting the release condition of the receive buffer BUSY state (This function is effective when DIP switch 1-2 is set to off.) | Releases the BUSY state when the remaining capacity of the receive buffer reaches 138 bytes. | Releases the BUSY state when the remaining capacity of the receive buffer reaches 256 bytes. | OFF               |
| 2-6 ∼ 2-7 | Reserved (Do not change setting)                                                                                               | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-8       | Reserved (Do not change setting)                                                                                               | Fixed to ON                                                                                  | Fixed to ON                                                                                  | ON                |

<!-- image -->

- For DIP switch 2-1 (BUSY condition), see also "Selecting the BUSY Status" on page 42.
- Do not change the setting of DIP switches 2-2, 2-6, and 2-7. Otherwise, the printer may not operate normally.

<!-- page 41 -->

## Selecting the Print Density (DIP Switch 2-3/2-4)

| Function                             | SW 2-3   | SW2-4   |
|--------------------------------------|----------|---------|
| Low power consumption mode           | ON       | ON      |
| Print density (Standard)             | OFF      | OFF     |
| Print density (Darker than standard) | ON       | OFF     |
| Print density (Dark)                 | OFF      | ON      |

- If the print density is set to 'Darker than standard' or 'Dark' level, printing speed may be reduced.
- The print density can be set with DIP switches (2-3/2-4) or to the customized value. (See "Setting the Memory Switches" on page 43.) The initial setting of the customized value is 'Depends on the DIP switch settings.' If the customized value is changed, the value set with the customized value is enabled.

<!-- page 42 -->

## Selecting the BUSY Status

W it h DIP sw it ch 2-1, yo u ca n selec t co n d iti o n s for in vok ing a BUSY s t a t e as e it her of t he follow ing :

- Whe n t he rece i ve b u ffer i s f u ll
- Whe n t he rece i ve b u ffer i s f u ll or t he pr int er i s offl in e

<!-- image -->

In either case above, the printer enters the BUSY state after power is turned on (including resetting with the interface), and when a self-test is being run.

## Printer BUSY condition and status of DIP switch 2-1

| Printer status              | Printer status                                                                                                                    | DIP SW 2-1   | DIP SW 2-1   |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------|--------------|
|                             |                                                                                                                                   | ON           | OFF          |
| Offline                     | During the period after power is turned on (including resetting with the interface) to when the printer is ready to receive data. | BUSY         | BUSY         |
|                             | During the self-test.                                                                                                             | BUSY         | BUSY         |
|                             | When the cover is open.                                                                                                           | -            | BUSY         |
|                             | During paper feed with the FEED button.                                                                                           | -            | BUSY         |
|                             | When the printer stops printing due to a paper- end (when printer has run out of roll paper).                                     | -            | BUSY         |
|                             | When an error has occurred.                                                                                                       | -            | BUSY         |
| When an error has occurred. | When an error has occurred.                                                                                                       | BUSY         | BUSY         |

If DIP switch 2-1 is on, the printer will not become BUSY

- When error has occurred
- When the cover is open
- When printing has stopped for a paper out
- When paper is fed by the FEED button

<!-- page 43 -->

## Setting the Memory Switches

W it h t he 'memory sw it ch (c u s t om i zed val u e,' wh i ch i s a sof t ware sw it ch of t h i s pr int er, yo u ca n se t :

- Pr int de n s it y
- Pr int speed
- N u mber of head e n er gi z ing par t s
- S ing le-color pr inting / t wo-color pr inting
- Black-color de n s it y in t wo-color pr inting

Use t he Memory Sw it ch Se tting U ti l it y or a comma n d t o se t t he memory sw it ches.

<!-- image -->

In power saving mode, all customized value settings are ignored.

<!-- image -->

- For detailed information about the memory switch utility, see the user's manual for the Memory Switch Setting Utility.
- For  detailed  information  about  ESC/POS  commands,  see  the  ESC/POS  Application Programing Guide.

## Selecting the print density

Selec t able from levels 1 t o 13 (l ig h t ∼ dark).

The print density can be set with DIP switches (2-3/2-4) or the customized value. (See "Setting the Memory Switches" on page 43.) The initial setting of the customized value is 'Depends on the DIP switch settings.' If the customized value is changed, the value set with the customized value is enabled.

## Selecting the print speed

Selec t able from levels 1 t o 9 (low ∼ h ig h). (I niti al se tting : level 9)

<!-- image -->

Depending on print conditions such as print duty, print head temperature, or data transmission speed, print speed is automatically adjusted which may cause white lines due to intermittent print (the motor sometimes stops). To avoid this, keep the print speed constant by setting it lower, or set the transmission speed higher in case of the serial interface. (See "Transmission speed (DIP switch 1-7/1-8)" on page 36.)

<!-- page 44 -->

## Selecting the number of head energizing parts

- O n e-par t e n er gi z ing
- Two-par t e n er gi z ing
- Fo u r-par t e n er gi z ing
- A ut o e n er gi z ing (I niti al se tting )
- Usually, the number of head energizing parts does not need to be changed.
- When auto energizing is selected, the printer usually prints in one-part energizing, but it automatically shifts to two-part energizing if print duty is high.

<!-- image -->

## Selecting single-color printing/two-color printing

- S ing le-color pr inting (I niti al se tting )
- Two-color pr inting

## Selecting black-color density in two-color printing

- L ig h t
- S t a n dard (I niti al se tting )

<!-- image -->

This setting affects black-color density only in two-color printing, but not that in single-color printing.

<!-- page 45 -->

## Adjusting the Paper Roll Near-End Sensor

Below are t wo s itu a ti o n s where a roll paper NE se n sor adj u s t me nt i s req ui red.

- To adj u s t t he de t ec ti o n pos iti o n t o s uit t he d i ame t er of t he roll paper core u sed.
- To adj u s t t he de t ec ti o n pos iti o n of rema ining amo unt of paper.
- Since  roll  paper  cores  vary  slightly  in  shape,  depending  on  paper  roll  design  and manufacturing tolerances, it is impossible to detect the remaining paper exactly.
- Use roll paper with a core inner diameter of 12 mm {0.47"} and outer diameter of 18 mm {0.71"} so that the NE sensor can detect the remaining paper as accurately as possible.

Follow t he s t eps below t o adj u s t t he roll paper n ear-e n d de t ec t or.

- 1 Open the roll paper cover, and remove the roll paper.
- 2 Loosen the adjustment screw fastening the sensor, and align the upper edge of the positioning plate with the adjustment position.
- 3 Tighten the adjustment screw.
- 4 After adjustment, make sure that the detection lever operates smoothly.

| Adjustment position     | Remaining amount of paper (outer diameter: mm)   |
|-------------------------|--------------------------------------------------|
| Upper                   | Approx. 27 {1.06"}                               |
| Lower (Initial setting) | Approx. 23 {0.97"}                               |

<!-- image -->

<!-- page 46 -->

## Connecting the Printer to the Host Computer

- Be sure to install the driver before connecting the printer to the host computer.
- The printer uses the modular connectors specifically designed for the cash drawer. Do not connect these connectors to an ordinary telephone line.

## For Serial Interface

## Serial interface connection diagram

Whe n t h i s pr int er i s co nn ec t ed t o a hos t comp ut er by t he ser i al int erface, t wo co nn ec ti o n forms are poss i ble:

- S t a n d alo n e
- Passt hro ug h co nn ec ti o n

## Stand alone

Th i s pr int er i s co nn ec t ed t o t he hos t comp ut er v i a t he ser i al por t . Whe n a c u s t omer d i splay (DM-D) i s t o be co nn ec t ed, co nn ec t it t o t he hos t comp ut er v i a t he ser i al por t .

<!-- image -->

## Pass-through connection

Th i s pr int er i s co nn ec t ed t o t he hos t comp ut er over t he ser i al int erface v i a a c u s t omer d i splay (DM-D).

<!-- image -->

<!-- page 47 -->

## Connecting the serial interface (RS-232C) cable

<!-- image -->

Be sure to turn off the power supply for both the printer and host computer before connecting the cables.

- 1 Insert the interface cable connector firmly into the interface connector on the connector panel.
- 2 When using connectors equipped with screws, tighten them to secure the connectors firmly.
- 3 When using interface cables equipped with a grounding line, attach the ground line to the screw hole marked 'FG' on the printer.
- 4 Connect the other end of the interface cable to the host computer.

<!-- image -->

<!-- image -->

<!-- page 48 -->

## For Parallel Interface

## Parallel interface connection diagram

Th i s pr int er i s co nn ec t ed t o t he hos t comp ut er v i a t he parallel por t . Whe n a c u s t omer d i splay (DM-D) i s t o be co nn ec t ed, co nn ec t it t o t he hos t comp ut er v i a t he ser i al por t .

<!-- image -->

## Connecting the parallel interface cable

- 1 Insert the interface cable connector firmly into the interface connector on the connector panel.
- 2 Press down the clips on either side of the connector to lock it in place.
- 3 When using interface cables equipped with a ground line, attach the ground line to the screw hole marked 'FG' on the printer.
- 4 Connect the other end of the interface cable to the host computer.

<!-- page 49 -->

## For USB Interface

## USB interface connection diagram

Whe n t h i s pr int er i s co nn ec t ed t o t he hos t comp ut er by t he USB int erface, t wo co nn ec ti o n forms are poss i ble:

- S t a n d alo n e
- Y co nn ec ti o n

## Stand alone

Th i s pr int er i s co nn ec t ed t o t he hos t comp ut er v i a t he USB por t . Whe n a c u s t omer d i splay (DM-D) i s t o be co nn ec t ed, co nn ec t it t o t he hos t comp ut er v i a t he ser i al por t .

<!-- image -->

## Y connection (only with the UB-U01III/U02III)

Th i s pr int er i s co nn ec t ed t o t he hos t comp ut er v i a t he USB por t . Whe n a c u s t omer d i splay (DM-D) i s t o be co nn ec t ed, co nn ec t it t o t he pr int er v i a t he mod u lar cable.

<!-- image -->

When connecting a customer display to the printer, connect the modular jack from the customer display to the DM connector.

Also, set the communication conditions of the customer display as follows:

- Baud rate: 19200 bps
- Bit length: 8-bit
- Parity: no parity
- Stop bit: 1

<!-- image -->

<!-- page 50 -->

## Connecting the USB interface cable

- 1 Attach the locking wire saddle at the location shown in the figure below.
- 2 Put the USB cable through the locking wire saddle.
- 3 Connect the USB cable from the host computer to the USB upstream connector.

<!-- image -->

<!-- page 51 -->

## For LAN Interface

Co nn ec t t he pr int er t o a n e t work by a LAN cable v i a a h u b.

## LAN interface connection diagram

<!-- image -->

A customer display (DM-D series) cannot be connected to the printer when the printer is connected to the host computer. To connect the customer display, connect the printer to the host computer via the serial interface.

## Connecting the LAN interface cable

<!-- image -->

- When LAN cables are installed outdoors, make sure devices without proper surge protection are cushioned by being connected through devices that do have surge protection.
- Otherwise, the devices can be damaged by lightning.
- Never attempt to connect the customer display cable, drawer kick-out cable, or the standard telephone line cable to the 10/100BASE-T LAN connector.

<!-- page 52 -->

Co nn ec t a 10/100BASE-T cable t o t he 10/100BASE-T LAN co nn ec t or by press ing f i rmly unti l t he co nn ec t or cl i cks int o place.

<!-- image -->

<!-- image -->

To use the LAN interface, the IP Address Setup Utility for UB-E02 is required. For detailed information about the setup methods, see the UB-E02 Technical Reference Guide. You can obtain the IP Address Setup Utility for UB-E02 and the UB-E02 Technical Reference Guide from one of the following URLs or ask your dealer:

- For customers in North America, go to the following web site: http://www.epsonexpert.com/
- For customers in other countries, go to the following web site: http://www.epson-pos.com/

<!-- page 53 -->

## For Wireless LAN Interface

For de t a i ls o n how t o se t u p a w i reless LAN int erface, see t he UB-R02/R03 Tech ni cal Refere n ce G ui de.

## Wireless LAN interface connection diagram

<!-- image -->

<!-- image -->

TM-T88IV

To use the wireless LAN interface, the IP Address Setup Utility for UB-R02/R03 is required. For detailed information about the setup methods, see the UB-R02/R03 Technical Reference Guide. You can obtain the IP Address Setup Utility for UB-R02/R03 and the UB-R02/R03 Technical Reference Guide from one of the following URLs or ask your dealer:

- For customers in North America, go to the following web site: http://www.epsonexpert.com/
- For customers in other countries, go to the following web site:
- http://www.epson-pos.com/

<!-- page 54 -->

## Connecting the Power Supply Unit (PS-180)

Use t he PS-180 or a n eq ui vale nt prod u c t as t he power s u pply unit .

<!-- image -->

- Always use the EPSON PS-180 or an equivalent product as the power supply unit. Using a nonstandard power supply can result in electric shock and fire.
- Should a fault ever occur in the EPSON PS-180 or equivalent product, immediately turn off the power to the printer and remove the power supply cable from the wall socket.

## Connecting the Power Supply Unit

- 1 Make sure the printer's power supply is turned off and the power supply unit's power cable has been removed from the wall socket.
- 2 Insert the connector of the power supply cable onto the power supply connector (stamped 24V ).
- Be sure to remove the power supply unit's cable from the wall socket whenever connecting or disconnecting the power supply unit to the printer.
- Failure to do so may result in damage to the power supply unit or the printer.
- Make sure the wall socket power supply satisfies the rated voltage requirements of the power supply unit. Never insert the power supply cable plug into a socket that does not meet the rated voltage requirements of the power supply unit. Doing so may result in damage to both the power supply and the printer.

<!-- image -->

<!-- image -->

<!-- image -->

Before removing the DC cable connector from the PS-180, make sure the power supply cable has been removed from the power supply unit, then grasp the arrow-marked section of the connector and pull straight out.

<!-- page 55 -->

## Connecting the Cash Drawer

Use t he cash drawer ha n dled by EPSON or yo u r dealer.

## Connecting the Drawer Kick-out Cable

<!-- image -->

- Specifications of drawers differ depending on makers or models. When you use a drawer other than specified, make sure its specification meets the following conditions.

Otherwise, devices may be damaged.

- ∗ The load, such as a drawer kick-out solenoid, must be connected between pins 4 and 2 or pins 4 and 5 of the drawer kick-out connector.
- ∗ When  the  drawer  open/close  signal  is  used,  a  switch  must  be  provided  between drawer kick-out connector pins 3 and 6.
- ∗ The resistance of the load, such as a drawer kick-out solenoid, must be 24 Ω or more or the input current must be 1A or less.
- ∗ Be sure to use the 24V power output on drawer-kick out connector pin 4 for driving the equipment.
- Use a shield cable for the drawer connector cable.
- Two driver transistors cannot be energized simultaneously.
- Leave  intervals  longer  than  4  times  the  drawer  driving  pulse  when  sending  it continuously.
- Be sure to use the printer power supply (connector pin 4) for the drawer power source.
- Do not insert a telephone line into the drawer kick-out connector. Doing so may damage the telephone line or printer.

Co nn ec t t he co nn ec t or of t he drawer k i ck-o ut cable t o t he pr int er.

<!-- image -->

<!-- page 56 -->

## Drawer Circuitry

<!-- image -->

## Setting the Buzzer

Models w it h t he b u zzer f un c ti o n ca n beep t he b u zzer whe n t he drawer i s ope n ed.

The b u zzer se tting i s performed by se tting t he DIP sw it ches for t he b u zzer a n d spec i fy ing co nn ec t or p in nu mbers t o wh i ch a comma n d o ut p ut s a p u lse s ign al.

|   DIP switch | Specified connector pin         | ON            | OFF                   | Initial setting   |
|--------------|---------------------------------|---------------|-----------------------|-------------------|
|            1 | Drawer kick out connector pin 2 | Buzzer beeps. | Buzzer does not beep. | ON                |
|            2 | Drawer kick out connector pin 5 | Buzzer beeps. | Buzzer does not beep. | OFF               |

<!-- image -->

Since the buzzer drive signal and the cash drawer drive signal are common in the printer, do not use the same connector pin numbers to output the signal for the buzzer and the cash drawer.

For detailed information about ESC/POS commands, see the ESC/POS Application Programing Guide.

<!-- page 57 -->

## Application Development Information

Th i s chap t er descr i bes how t o co nt rol t he pr int er a n d gi ves in forma ti o n u sef u l for pr int er appl i ca ti o n developme nt .

## How to Control the Printer

Use a dr i ver or ESC/POS comma n ds t o co nt rol t he pr int er.

## Selecting a Driver

Choose o n e of t he dr i vers, Adva n ced Pr int er Dr i ver (APD) or OPOS ADK, depe n d ing o n t he appl i ca ti o n opera ting e n v i ro n me nt . Yo u ca nn o t co nt rol t he same pr int er w it h bo t h of t he dr i vers. For in forma ti o n abo ut t he dr i ver opera ting e n v i ro n me nt , see t he in s t alla ti o n ma nu al for each dr i ver.

## When you newly develop an application

- Use APD i f yo u wa nt t o pr int Tr u e Type fo nt s or pr int m u ch g raph i cs.
- OPOS ADK i s recomme n ded for sys t em ex t e n s i b i l it y. A n OPOS dr i ver i s prov i ded for var i o u s per i pherals a n d it i s a POS in d u s t ry s t a n dard n ow. I t e n ables eff i c i e nt POS sys t em es t abl i shme nt , red u c ti o n of developme nt cos t , a n d effec ti ve u se of appl i ca ti o n asse t .

When APD is used for your existing application Use APD.

When OPOS ADK is used for your existing application Use OPOS ADK.

<!-- image -->

You can use all functions including ones not supported by OPOS ADK or APD by using a driver with ESC/POS command. Use the DIRECT I/O function of OPOS ADK, the control A command of APD, or Status API to send ESC/POS command from each driver. (See "ESC/POS command functions" on page 58.)

<!-- page 58 -->

## ESC/POS Command

ESC/POS i s t he Epso n or igin al pr int er comma n d sys t em. W it h ESC/POS comma n ds, yo u ca n d i rec t ly co nt rol all t he TM pr int er f un c ti o n s, b ut de t a i led k n owled g e of pr int er spec i f i ca ti o n s or comb in a ti o n of comma n ds i s req ui red compared t o u s ing a dr i ver.

To u se ESC/POS comma n ds, yo u n eed t o make a n o n d i sclos u re co nt rac t f i rs t a n d g e t t he ESC/POS Appl i ca ti o n Pro g ram ing G ui de. Ask yo u r dealer for de t a i ls.

The ESC/POS comma n d f un c ti o n s are l i s t ed as follows. See t he ESC/POS Appl i ca ti o n Pro g ram ing G ui de for more de t a i ls.

## ESC/POS command functions

| Commands for printing                            |
|--------------------------------------------------|
| Print and line feed                              |
| Print and feed n lines                           |
| Print data in page mode                          |
| Print and return to standard mode (in page mode) |
| Commands for line spacing                        |
| Set line spacing                                 |
| Select default line spacing                      |
| Commands for print character                     |
| Select character code table                      |
| Select an international character set            |
| Set right-side character spacing                 |
| Set all print decoration                         |
| Turn underline mode on/off                       |
| Turn emphasized mode on/off                      |
| Select character font                            |
| Select character size                            |
| Turn smoothing mode on/off                       |
| Turn upside-down print mode on/off               |
| Turn white/black reverse print mode on/off       |
| Set character decoration                         |

<!-- page 59 -->

| Select/cancel user-defined character set                  |
|-----------------------------------------------------------|
| Define user-defined characters                            |
| Cancel print data in page mode                            |
| Commands for panel buttons                                |
| Enable/disable panel buttons                              |
| Commands for paper sensors                                |
| Select paper sensor(s) to stop printing                   |
| Select paper sensor(s) to output paper-end signals        |
| Commands for print positions                              |
| Horizontal tab                                            |
| Set horizontal tab positions                              |
| Set left margin                                           |
| Set print area width                                      |
| Select justification                                      |
| Set absolute print position                               |
| Set relative print position                               |
| Set print area in page mode                               |
| Select print direction in page mode                       |
| Set absolute vertical print position in page mode         |
| Set relative vertical print position in page mode         |
| Commands for bit image                                    |
| Transmit the NV graphic memory capacity                   |
| Print the graphics data in the print buffer               |
| Transmit the remaining capacity of the NV graphics memory |
| Transmit the key code list for defined NV graphics        |
| Delete the specified NV graphics data                     |
| Define the NV graphics data                               |
| Print the specified NV graphics data                      |
| Store the graphics data in the print buffer               |
| Select bit-image mode                                     |

<!-- page 60 -->

| Define downloaded bit image                                                          |
|--------------------------------------------------------------------------------------|
| Print downloaded bit image                                                           |
| Commands for status                                                                  |
| Enable/disable Automatic Status Back (ASB)                                           |
| Transmit status                                                                      |
| Transmit real-time status                                                            |
| Commands for barcode                                                                 |
| Print barcode                                                                        |
| Set barcode height                                                                   |
| Set barcode width                                                                    |
| Select print position of HRI characters                                              |
| Select font for HRI characters                                                       |
| Commands for two-dimensional code                                                    |
| PDF417: Set the number of columns in the data region                                 |
| PDF417: Set the number of rows                                                       |
| PDF417: Set the width of module                                                      |
| PDF417: Set the row height                                                           |
| PDF417: Set the error correction level                                               |
| PDF417: Select the options                                                           |
| PDF417: Store the data in the symbol storage area                                    |
| PDF417: Print the symbol data in the symbol storage area                             |
| PDF417: Transmit the size information of the symbol data in the symbol storage area  |
| QR Code: Select the model                                                            |
| QR Code: Set the size of module                                                      |
| QR Code: Select the error correction level                                           |
| QR Code: Store the data in the symbol storage area                                   |
| QR Code: Print the symbol data in the symbol storage data area                       |
| QR Code: Transmit the size information of the symbol data in the symbol storage area |
| Commands for mechanical control                                                      |
| Select cut mode and cut paper                                                        |

<!-- page 61 -->

| Commands for customization                                   |
|--------------------------------------------------------------|
| Set the customized setting values                            |
| Transmit the customized setting values                       |
| Set the configuration item for the serial interface          |
| Transmit the configuration item for the serial interface     |
| Delete the specified record of NV user memory                |
| Store the data in the specified record of NV user memory     |
| Transmit the data in the specified record of NV user memory  |
| Transmit capacity of the NV user memory currently being used |
| Transmit the remaining capacity of the NV user memory        |
| Transmit the key code list                                   |
| Delete all data in the NV user memory                        |
| Commands for sub-functions                                   |
| Initialize printer                                           |
| Transmit printer ID                                          |
| Set horizontal and vertical motion units                     |
| Select peripheral device                                     |
| Generate pulse to drawer                                     |
| Generate pulse to drawer in real-time                        |
| Execute power-off sequence                                   |
| Clear buffer(s)                                              |
| Enable/disable real-time command                             |
| Send real-time request to printer                            |
| Select page mode                                             |
| Select standard mode                                         |
| Set the process ID response                                  |
| Execute test print                                           |
| Select the print speed                                       |
| Select the number of parts for the thermal head energizing   |
| Initialize maintenance counter                               |
| Transmit maintenance counter                                 |

<!-- page 62 -->

## Software and Manuals

The follow ing sof t ware a n d ma nu als are prov i ded for appl i ca ti o n developme nt .

| Software                                         | Description                                                                                                                                                                                                                                                                               | Manual                                                                                                                                                                        |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Drivers                                          | Drivers                                                                                                                                                                                                                                                                                   | Drivers                                                                                                                                                                       |
| EPSON Advanced Printer Driver (APD)              | In addition to ordinary Windows driver functions, this driver has controls specific to POS such as controls of paper cut, a cash drawer, or customer display. The Status API (Epson original DLL) that monitors printer status and sends ESX/POS command is also attached to this driver. | • APD installation manual • APD TM driver manual • APD Printer driver specification • Status API Reference manual                                                             |
| OPOS ADK (OPOS)                                  | This OCX driver can control POS peripherals using OLE technology* 1 . Because controlling POS peripherals with original commands is not required on application side, efficient system development is possible.                                                                           | • OPOS installation manual • User's guide • Application development guide • OPOS Application Programing Guide* 2 • Sample program guide • TM Flash Logo Utility user's manual |
| Utilities for developers                         | Utilities for developers                                                                                                                                                                                                                                                                  | Utilities for developers                                                                                                                                                      |
| TM Flash LOGO Setup Utility for NVRAM (TM-FLOGO) | Use to register data such as shop logos in the NV memory of the printer.                                                                                                                                                                                                                  | -                                                                                                                                                                             |
| Memory Switch Setting Utility                    | use to change the memory switch and customized value.                                                                                                                                                                                                                                     | User's manual                                                                                                                                                                 |
| TMUSB Identifier Utility                         | Use to edit USB identifying code for the USB interface.                                                                                                                                                                                                                                   | -                                                                                                                                                                             |
| TM Net WinConfig utility for UB-E02              | Use to setup IP address for the LAB interface.                                                                                                                                                                                                                                            | UB-E02 Technical Reference Guide                                                                                                                                              |
| TM Net WinConfig utility for UB-R02/R03          | Use to setup IP address for the wireless interface.                                                                                                                                                                                                                                       | UB-R02/R03 Technical Reference Guide                                                                                                                                          |

*1: OLE t ech n olo g y developed by M i crosof t d i v i des sof t ware int o par t blocks. The OPOS dr i ver i s pres u pposed t o be u sed w it h a develop e n v i ro n me nt s u ch as V i s u al Bas i c, un l i ke ord in ary W in dows dr i vers. I t i s n o t a dr i ver t o be u sed for pr inting from commerc i al appl i ca ti o n s.

*2: Descr i bes n o t Epso n 's spec i f i c f un c ti o n s, b ut g e n eral in forma ti o n o n how t o co nt rol pr int ers u s ing OPOS ADK ( in t he chap t er 'POS Pr int er').

<!-- page 63 -->

O t her t ha n l i s t ed in t he prev i o u s pa g e, UB-E02 Tech ni cal Refere n ce G ui de i s prov i ded t o develop appl i ca ti o n s for t he LAN int erface.

## Download

Dr i vers, uti l iti es, a n d ma nu als ca n be dow n loaded from o n e of t he follow ing URLs.

For c u s t omers in Nor t h Amer i ca, g o t o t he follow ing web s it e:

h tt p://www.epso n exper t .com/ a n d follow t he o n -scree n in s t r u c ti o n s.

For c u s t omers in o t her co unt r i es, g o t o t he follow ing web s it e:

h tt p://www.epso n -pos.com/

Selec t t he prod u c t n ame from t he 'Selec t a n y prod u c t ' p u lldow n me nu .

<!-- page 64 -->

## Setting Check Modes

Bes i des t he ord in ary pr int mode, t he pr int er has a selft es t mode a n d hexadec i mal d u mp ing mode t o check se tting s of t he pr int er.

## Self-test Mode

Yo u ca n co n f i rm t he follow ing pr int er f un c ti o n s by r unning t he selft es t .

- Co nt rol c i rc uit f un c ti o n s
- Pr int er mecha ni sm
- Pr int q u al it y
- ROM vers i o n
- DIP sw it ch se tting s

## Starting Self-test

Follow t he s t eps below t o r un t he selft es t .

- 1 Close the roll paper cover.
- 2 While pressing the FEED button, turn on the printer. (Keep pressing the FEED button until the printer starts printing.)

The pr int er pr int s c u rre nt s t a tu s of t he pr int er o n t he roll paper.

With the LAN interface, before printing starts, it takes 6 seconds if the IP address is fixed and 13 seconds if the IP address is obtained with the automatic setting. (It may takes longer depending on the response time from a host.)

Whe n t he pr int er f ini shes pr inting t he pr int er s t a tu s, t he follow ing messa g e i s pr int ed a n d t he PAPER OUT LED flashes. (The pr int er i s n ow in t he selft es t wa it mode.):

'If yo u wa nt t o co ntinu e SELF-TEST pr inting . Please press FEED b utt o n .'

- 3 To begin the print test again, press the FEED button while the printer is in the self-test wait mode.
- 4 After printing the following message, the printer is initialized and returned to the normal mode.

'*** comple t ed ***'

<!-- page 65 -->

## Hexadecimal Dumping Mode

I n t he hexadec i mal d u mp ing mode, t he pr int er pr int s t he da t a t ra n sm itt ed from a hos t comp ut er in hexadec i mal nu mbers a n d t he i r correspo n d ing charac t ers.

## Starting hexadecimal dumping

Follow t he s t eps below t o perform t he hexadec i mal d u mp ing .

- If there is no character corresponding to print data, '.' is printed.
- If print data is less than one line, press the FEED button to print the line.
- Applications that confirm printer status may not work correctly during the hexadecimal dumping mode. The printer returns only the status for 'Transmit real-time status.'
- 1 Open the roll paper cover.
- 2 While pressing the FEED button, turn on the printer.
- 3 Close the roll paper cover.

Da t a rece i ved from t he n o n i s pr int ed o ut from t he pr int er in hexadec i mal nu mbers a n d t he i r correspo n d ing charac t ers.

- 4 To quit the hexadecimal dumping mode, turn off the printer or press the FEED button three times.

Printing example

<!-- image -->

<!-- page 66 -->



<!-- page 67 -->

## Handling

Th i s chap t er descr i bes bas i c ha n dl ing of t he pr int er.

## Installing and Replacing Roll Paper

<!-- image -->

- Do not open the roll paper cover during printing. The printer may be damaged.
- Do not touch the manual cutter with your hands when installing or replacing the roll paper.

Otherwise, you may be injured because the manual cutter blade is sharp.

- Use roll paper that meets the printer specification. For details about paper specification, see "Paper Specifications" on page 27.
- Paper must not be pasted to the roll paper spool.
- 1 Press the cover open lever to open the roll paper cover.

<!-- image -->

When the roll paper cover cannot be opened, see "When the Roll Paper Cover Cannot be Opened" on page 70.

- 2 Remove the used roll paper core, if any.

<!-- page 68 -->

- 3 In the correct direction of the roll paper, install the roll paper.
- 4 Pull out some roll paper, and close the roll paper cover.
- 5 Tear off the roll paper with the manual cutter.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- page 69 -->

## Attaching/Removing the Connector Cover

## Attaching the Connector Cover

- 1 Connect all the cables. The co nn ec t or cover has t hree poss i ble cable ex it s: o n t he r ig h t , lef t , a n

d back.

- 2 Position  the  two  hooks  on  the  connector  cover  so  that  they  hook  the holes on the printer case. Push the connector cover down until it clicks.

<!-- image -->

## Removing the Connector Cover

Place t he pr int er w it h it s bo tt om u p. Wh i le p u sh ing t he bo t h s i des of t he co nn ec t or cover t oward in s i de, p u sh it dow n t o de t ach t he t wo hooks o n it from t he pr int er case.

<!-- image -->

<!-- page 70 -->

## Removing Jammed Paper

<!-- image -->

Do not touch the thermal head (See"Cleaning the Thermal Head" on page 72.) because it can be very hot after printing.

- 1 Turn off the printer and press the cover open lever to open the roll paper cover.
- 2 Remove the jammed paper, reinstall the roll, and close the roll paper cover.

## When the Roll Paper Cover Cannot be Opened

- 1 Open the cutter cover.
- 2 Turn the knob until you see a triangle in the opening. Th i s re tu r n s t he c utt er blade t o t he n ormal pos iti o n . There i s a label n ear t he c utt er t o ass i s t yo u .

<!-- image -->

<!-- image -->

<!-- page 71 -->

- 3 Close the cutter cover.
- 4 Open the roll paper cover and remove the jammed paper.

4

<!-- page 72 -->

## Cleaning the Thermal Head

Epso n recomme n ds clea ning t he t hermal head per i od i cally ( g e n erally every 3 mo nt hs) t o ma int a in rece i p t pr int q u al it y.

<!-- image -->

After printing, the thermal head can be very hot. Do not touch it and let it cool before you clean it. Do not damage the thermal head by touching it with your fingers or any hard object.

T u r n off t he pr int er, ope n t he roll paper cover, a n d clea n t he t hermal eleme nt s of t he t hermal head w it h a co tt o n swab mo i s t e n ed w it h a n alcohol solve nt (e t ha n ol or IPA).

<!-- image -->

Follow t he s t eps below t o t ra n spor t t he pr int er.

- 1 Turn off the printer.
- 2 Confirm that LED is off.
- 3 Remove the power supply connector.
- 4 Remove the roll paper.
- 5 Pack the printer upright.

<!-- page 73 -->

## Replacement of the TM-T88III

The TM-T88IV i s des ign ed so t ha t it ca n smoo t hly replace t he TM-T88III. Th i s chap t er descr i bes preca uti o n s for t he replaceme nt .

## Compatibility

## Printing

The pr inting a n d charac t er spec i f i ca ti o n s are t he same as t hose of t he TM-T88III excep t some charac t er fo nt des ign s. W it ho ut spec i al co n f igu ra ti o n s, t he TM-T88IV pr int s t he same res u l t s as t he TM-T88III pr int s.

## Font designs

The follow ing fo nt des ign s of t he TM-T88IV have cha ng ed from t hose of t he TM-T88III.

- Fo nt A: 2, 3, 4, 5, 6, 7, 9
- Fo nt B: 2, 6, 9

## Print Density

The pr int de n s it y of t he TM-T88IV ca n be se t w it h DIP sw it ches (2-3/2-4) as ca n t he TM-T88III. Se t t he de n s it y t he same as for t he TM-T88III t o pr int in t he same pr int de n s it y.

The print density can be set also to a customized value. The initial setting of the customized value is 'Depends on the DIP switch settings.' If the customized value is changed, the value set with the customized value is enabled. (See "Setting the Memory Switches" on page 43.)

## Print Speed

The TM-T88IV has speeded it s pr inting u p t o 200 mm/s a t max i m u m. (TM-T88III: 150 mm/s)

Depending on print conditions such as print duty, print head temperature, or data transmission speed, print speed is automatically adjusted which may cause white lines due to intermittent print (the motor sometimes stops). To avoid this, keep the print speed constant by setting it lower (See "Setting the Memory Switches" on page 43.), or set the transmission speed higher in case of the serial interface. (See "Transmission speed (DIP switch 1-7/1-8)" on page 36.)

<!-- page 74 -->

## Number of Head Energizing Parts

For t he TM-T88IV, t he initi al se tting of t he nu mber of head e n er gi z ing par t s i s 'A ut o e n er gi z ing .' Yo u ca n cha ng e t he se tting t o a c u s t om i zed val u e (See "Se tting t he Memory Sw it ches" o n pa g e 43.); however it does n o t u s u ally n eed t o be cha ng ed.

|                                | TM-T88IV                                                                             | TM-T88III                    |
|--------------------------------|--------------------------------------------------------------------------------------|------------------------------|
| Number of head energizing part | • One-part energizing • Two-part energizing • Four-part energizing • Auto energizing | Fixed to two-part energizing |

## Printable Area

The pr int able area (lef t /r ig h t mar gin s, pr int s t ar t pos iti o n from t he a ut oc utting pos iti o n , pr int s t ar t pos iti o n from t he ma nu al c utting pos iti o n ) of t he TM-T88IV i s t he same as t ha t of t he TM-T88III.

## Cutting Method

The TM-T88IV u ses t he par ti al c utting me t hod (c utting w it h o n e po int in lef t ed g e lef t un c ut ) as does t he TM-T88III.

## Receive Buffer

Yo u ca n se t t he rece i ve b u ffer of t he TM-T88IV t o 4KB or 45 by t es w it h DIP sw it ch 1-2 as w it h t he TM-T88III. The b u ffer f u ll co n d iti o n a n d b u ffer f u ll release co n d iti o n of t he TM-T88IV are t he same as t hose of t he TM-T88III.

## Memory Capacity

The s i zes of t he dow n load b u ffer a n d NV g raph i cs da t a of t he TM-T88IV are t he same as t hose of t he TM-T88III. The TM-T88IV does n o t have t he NV u ser memory.

<!-- page 75 -->

## Electrical Characteristics

The opera ting vol t a g e of t he TM-T88IV i s DC24 ± 7%, t he same as t he TM-T88III. The c u rre nt co n s u mp ti o n d i ffers depe n d ing o n t he pr int d ut y.

## DIP Switches

The f un c ti o n al ass ign me nt s of DIP sw it ches are t he same as t hose of t he TM-T88III. W it h t he same se tting s as for t he TM-T88III, t he same f un c ti o n s are e n abled for t he TM-T88IV.

## Printer Status

The TM-T88IV g oes t o t he same s t a tu s un der t he same co n d iti o n s as t he TM-T88III. Yo u ca n replace t he TM-T88IV w it h t he TM-T88III w it ho ut mod i fy ing appl i ca ti o n s.

## Hexadecimal Dumping

## Command operation during hexadecimal dumping

D u r ing hexadec i mal d u mp ing , mos t comma n ds do n o t f un c ti o n .

- TM-T88IV: O n ly DLE EOT f un c ti o n s.
- TM-T88III: O n ly DLE EOT, DLE ENQ, a n d DLE DC4 f un c ti o n .

<!-- image -->

For detailed information about ESC/POS commands, see the ESC/POS Application Programing Guide.

## Ending hexadecimal dumping

Af t er t he hexadec i mal d u mp ing , t he TM-T88IV performs a ut oc utting (par ti al c ut ), b ut t he TM-T88III does n o t .

## Logo Registration

The TM-T88IV ca n re gi s t er lo g os in t he NV memory (NVRAM) w it h t he TM Flash LOGO Se tu p U ti l it y for NVRAM (TM-Flo g o) as ca n t he TM-T88III.

<!-- page 76 -->

## Driver Compatibility

Yo u ca n opera t e t he TM-T88IV w it h a dr i ver for t he TM-T88III.

You cannot operate the TM-T88III with a driver for the TM-T88IV.

## Advanced Printer Driver

Whe n t he TM-T88III i s co nt rolled by a n APD, yo u ca n replace it w it h t he TM-T88IV w it ho ut mod i fy ing t he APD.

## OPOS ADK

Whe n t he TM-T88III i s co nt rolled by a n OPOS ADK, yo u ca n replace it w it h t he TM-T88IV w it ho ut mod i fy ing t he OPOS ADK.

## Accessories

The same co n s u mables a n d op ti o n s are ava i lable for t he TM-T88IV as for t he TM-T88III.

<!-- page 77 -->

## Overall Dimensions

Yo u ca n place t he TM-T88IV in t he same loca ti o n as t he TM-T88III, s in ce it s overall d i me n s i o n s a n d we ig h t are abo ut t he same as t hose of t he TM-T88III. W it h t he wall ha nging bracke t (WH-10), yo u ca n a tt ach t he TM-T88IV t o a wall j u s t as yo u ca n w it h t he TM-T88III.

<!-- image -->

<!-- page 78 -->

## Installation hole position for the wall hanging bracket

If you attach the TM-T88IV without the wall hanging bracket (WH-10), pay attention tho the installation hole position, since it has been changed.

<!-- image -->

<!-- page 79 -->

## Additional Functions and Functional Improvements

## Print Speed

The TM-T88IV pr int s fas t er t ha n t he TM-T88III.

|             | TM-T88IV            | TM-T88III           |
|-------------|---------------------|---------------------|
| Print speed | 200 mm/s at maximum | 150 mm/s at maximum |

No t e) Whe n t he pr int er pr int s w it h t he defa u l t pr int de n s it y level a t 24V a n d 25°C {77°F}.

<!-- image -->

Depending on print conditions such as print duty, print head temperature, and data transmission speed, print speed is automatically adjusted.

## High-Speed Graphic Printing

W it h t he TM-T88IV, h ig h-speed g raph i c pr inting i s poss i ble. (pr int speed: 200 mm/s a t max i m u m)

## Two-Dimensional Code

W it h t he TM-T88IV, t wo-d i me n s i o n al code (PDF417, QR code) pr inting i s poss i ble.

## Number of Characters

For t he TM-T88IV, spec i al charac t ers (845) are added.

<!-- page 80 -->

## NV Graphics

For t he TM-T88IV, in add iti o n t o t he b it i ma g e f un c ti o n (lo g o re gi s t ra ti o n f un c ti o n ), t he NV g raph i cs f un c ti o n i s added.

## What is the NV graphics function?

It enables the following items that are impossible with the NV bit image function.

- You can register/delete logo data one at a time.
- You can register logos without printer reset.
- You can confirm the remaining amount of memory.

<!-- image -->

With the TM Flash LOGO Setup Utility for NVRAM (TM-Flogo), you can use only the NV bit image function. Use ESC/POS commands to use the NV graphics function. For detailed information about ESC/POS commands, see the ESC/POS Application Programing Guide.

## Page Mode Area

For t he TM-T88IV, t he ver ti cal max i m u m pr int able area i s w i der t ha n t ha t of t he TM-T88III.

|                      | TM-T88IV             | TM-T88III           |
|----------------------|----------------------|---------------------|
| Horizontal direction | 512 dots             | 512 dots            |
| Vertical direction   | 1662 dots at maximum | 831 dots at maximum |

## Transmission Speed (For Serial Interface)

The TM-T88IV w it h t he memory se tting has more selec ti o n s of t ra n sm i ss i o n speed t ha n t he TM-T88III.

| TM-T88IV                                          | TM-T88III                    |
|---------------------------------------------------|------------------------------|
| 2400, 4800, 9600, 19200, 38400, 57600, 115200 bps | 4800, 9600, 19200, 38400 bps |

## No t e) bps: b it s per seco n d

<!-- image -->

For detailed information about the transmission speed setting, see "Setting the DIP Switches" on page 35.

<!-- page 81 -->

## Customized Value

For t he TM-T88IV, t he c u s t om i zed val u e f un c ti o n i s added. (See "Se tting t he Memory Sw it ches" o n pa g e 43.) W it h t he c u s t om i zed val u e, yo u ca n perform t he follow ing se tting s:

- Pr int de n s it y
- Pr int speed
- N u mber of head e n er gi z ing par t s
- S ing le-color pr inting / t wo-color pr inting
- Black-color de n s it y in t wo-color pr inting

## USB Interface

I n add iti o n t o t he USB int erface boards t ha t are ava i lable for t he TM-T88III, t he follow ing o n es are ava i lable for t he TM-T88IV.

- UB-U05
- UB-U06
- UB-U19

<!-- image -->

With one of the interface boards above, the USB controller on the main circuit board operates for transmission.

## USB Low Power Consumption Mode

W it h t he TM-T88IV, yo u ca n e n able t he USB low power co n s u mp ti o n mode w it h a DIP sw it ch se tting . (See "For USB I nt erface" o n pa g e 40.)

<!-- image -->

## What is the USB low power consumption mode?

You can reduce the power consumption when the printer is in the standby mode.

## Maintenance Counter

For t he TM-T88IV, a ma int e n a n ce co unt er i s added.

<!-- image -->

## What is the maintenance counter?

With this function, printer information such as a number of lines printed, the number of autocutting, and printer operation time after the printer starts working is automatically saved in the printer memory. You can read the information with the Status API of the APD or OPOS ADK to use it for periodical checks or part replacement.

<!-- page 82 -->

## Buzzer

For t he TM-T88IV, models w it h t he b u zzer f un c ti o n are ava i lable.

Yo u ca n beep t he b u zzer w it h t he p u lse s ign al u s ing a comma n d. (See "Se tting t he B u zzer" o n pa g e 56.)

For detailed information about ESC/POS commands, see the ESC/POS Application Programing Guide.

## Power Supply Box

For t he TM-T88IV, t he op ti o n al power s u pply box (OT-BX88) i s added. Yo u ca n s t ore t he power s u pply unit in t he box a tt ached t o t he pr int er.

<!-- image -->

For detailed information about the power supply box, see the OT-BX88 Installation Manual.

<!-- page 83 -->

## Appendix

## Specifications of Interface and Connector

<!-- image -->

For detailed information about LAN or wireless LAN, see one of the following:

- LAN: UB-E02 Technical Reference Guide
- Wireless LAN: UB-R02/R03 Technical Reference Guide

## RS-232C Serial Interface

## Interface board specifications (RS-232C-compliant)

| Item                                      | Item                                      | Specifications                                                                                                                                                     |
|-------------------------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data transfer method                      | Data transfer method                      | Serial                                                                                                                                                             |
| Synchronization                           | Synchronization                           | Asynchronous                                                                                                                                                       |
| Handshake                                 | Handshake                                 | Select one of the following with DIP switch 1-3: • DTR/DSR • XON/XOFF                                                                                              |
| Signal level                              | MARK                                      | -3V to -15V logic '1'/OFF                                                                                                                                          |
| Signal level                              | SPACE                                     | +3V to +15V logic '0'/ON                                                                                                                                           |
| Bit length                                | Bit length                                | Select one of the following with DIP switch 1-4: • 7 bit • 8 bit                                                                                                   |
| Transmission speed [bps: bits per second] | Transmission speed [bps: bits per second] | • Select one of the following with DIP switch 1-7/1-8: 4800/9600/19200bps • Select one of the following with commands: 2400/4800/9600/19200/38400/57600/115200 bps |
| Parity check                              | Parity check                              | Select one of the following with DIP switch 1-5: • Yes • No                                                                                                        |
| Parity selection                          | Parity selection                          | Select one of the following with DIP switch 1-6: • Even • Odd                                                                                                      |
| Stop bit                                  | Stop bit                                  | 1 or more bits However, the stop bit for data transfer from the printer is fixed to 1 bit.                                                                         |
| Connector                                 | Printer side                              | DSUB 25-pin (female) connector                                                                                                                                     |

<!-- page 84 -->

## Functions of each connector pin

|   Pin no. | Signal name   | Signal direction   | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------|---------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         1 | FG            | -                  | Frame ground                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|         2 | TXD           | Output             | Transmission data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|         3 | RXD           | Input              | Reception data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|         4 | RTS           | Output             | Equivalent to DTR signal (pin 20)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|         6 | DSR           | Input              | This signal indicates whether the host computer can receive data. SPACE indicates that the host computer can receive data. MARK indicates that the host computer cannot receive data. When DTR/DSR control is selected, the printer transmits data after confirming this signal (except if transmitted using some ESC/POS commands). When XON/XOFF control is selected, the printer does not check this signal. Changing DIP switch 2-7 lets this signal be used as a printer reset signal. When you use this signal as the printer's reset signal, the printer is reset when the signal remains MARK for a pulse width of 1 ms or more. |
|         7 | SG            | -                  | Signal ground                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|        20 | DTR           | Output             | 1) When DTR/DSR control is selected, this signal indicates whether the printer is BUSY. • SPACE status Indicates that the printer is ready to receive data. • MARK status Indicates that the printer is BUSY. Set BUSY conditions with DIP switch 2-1. 2) When XON/XOFF control is selected, the signal indicates that the printer is properly connected and ready to receive data from the host. The signal is always SPACE, except in the following cases: • During the period from when power is turned on to when the printer is ready to receive data. • During the self-test.                                                      |
|        25 | INT           | Input              | Changing DIP switch 2-8 enables this signal to be used as a reset signal for the printer. The printer is reset if the signal remains at SPACE for a pulse width of 1 ms or more.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

<!-- page 85 -->

## XON/XOFF

Whe n XON/XOFF co nt rol i s selec t ed, t he pr int er t ra n sm it s t he XON or XOFF s ign als as follows. The t ra n sm i ss i o n ti m ing of XON/XOFF d i ffers, depe n d ing o n t he se tting of DIP sw it ch 2-1.

| Signal   | Printer status                                                                            | DIP switch 2-1   | DIP switch 2-1   |
|----------|-------------------------------------------------------------------------------------------|------------------|------------------|
| Signal   | Printer status                                                                            | 1 (ON)           | 0 (OFF)          |
| XON      | 1) When the printer goes online after turning on the power (or reset using the interface) | Transmit         | Transmit         |
| XON      | 2) When the receive buffer is released from the buffer full state                         | Transmit         | Transmit         |
| XON      | 3) When the printer switches from offline to online                                       | -                | Transmit         |
| XON      | 4) When the printer recovers from an error using some ESC/POS commands                    | -                | Transmit         |
| XOFF     | 5) When the receive buffer becomes full                                                   | Transmit         | Transmit         |
| XOFF     | 6) When the printer switches from online to offline                                       | -                | Transmit         |

## Code

The hexadec i mal nu mbers correspo n d ing t o t he XON/XOFF codes are show n below.

- XON code: 11H

- XOFF code: 13H

<!-- image -->

- When the printer goes from offline to online and the receive buffer is full, XON is not transmitted.
- When the printer goes from online to offline and the receive buffer is full, XOFF is not transmitted.
- When DIP switch 1-3 is off, XON is not transmitted as long as the printer is offline, even if a receive buffer full state has been cleared.

<!-- page 86 -->

## IEEE 1284 Parallel Interface

## Modes

The IEEE 1284 parallel int erface s u ppor t s t he follow ing t wo modes.

| Mode               | Communication direction      | Other information                                    |
|--------------------|------------------------------|------------------------------------------------------|
| Compatibility mode | Host → Printer communication | Centronics-compliant                                 |
| Reverse mode       | Printer → Host communication | Assumes a data transfer from an asynchronous printer |

## Compatibility Mode

Compa ti b i l it y mode allows da t a t ra n sm i ss i o n from hos t t o pr int er o n ly: Ce nt ro ni cs-compa ti ble.

## Specification

| Data transmission     | 8-bit parallel                                |
|-----------------------|-----------------------------------------------|
| Synchronization       | Externally supplied STROBE signals            |
| Handshaking           | ACK and BUSY signals                          |
| Signal levels         | TTL-compatible connector                      |
| Connector             | ADS-B36BLFDR176 (HONDA) or equivalent product |
| Reverse communication | Nibble or byte mode                           |

## Reverse Mode

The t ra n sfer of s t a tu s da t a from t he pr int er t o t he hos t proceeds in t he ni bble or by t e mode. Th i s mode allows da t a t ra n sfer from a n asy n chro n o u s pr int er un der t he co nt rol of t he hos t . Da t a t ra n sfers in t he ni bble mode are made v i a t he ex i s ting co nt rol l in es in unit s of fo u r b it s (a ni bble). I n t he by t e mode, da t a t ra n sfer proceeds by mak ing t he 8-b it da t a l in es b i d i rec ti o n al. Bo t h modes fa i l t o proceed co n c u rre nt ly in t he compa ti b i l it y mode, t hereby ca u s ing half-d u plex t ra n sm i ss i o n .

<!-- page 87 -->

## Interface signals

|   Pin | Source   | Compatibility Mode   | Nibble Mode        | Byte Mode   |
|-------|----------|----------------------|--------------------|-------------|
|     1 | Host     | Strobe               | HostClk            | HostClk     |
|     2 | Host/Ptr | Data0 (LSB)          | Data0 (LSB)        | Data0 (LSB) |
|     3 | Host/Ptr | Data1                | Data1              | Data1       |
|     4 | Host/Ptr | Data2                | Data2              | Data2       |
|     5 | Host/Ptr | Data3                | Data3              | Data3       |
|     6 | Host/Ptr | Data4                | Data4              | Data4       |
|     7 | Host/Ptr | Data5                | Data5              | Data5       |
|     8 | Host/Ptr | Data6                | Data6              | Data6       |
|     9 | Host/Ptr | Data7 (MSB)          | Data7 (MSB)        | Data7 (MSB) |
|    10 | Printer  | Ack                  | PtrClk             | PtrClk      |
|    11 | Printer  | Busy                 | PtrBusy/Data3,7    | PtrBusy     |
|    12 | Printer  | Perror               | AckDataReq/Data2,6 | AckDataReq  |
|    13 | Printer  | Select               | Xflag/Data1,5      | Xflag       |
|    14 | Host     | AutoFd               | HostBusy k         | HostBusy    |
|    15 |          | NC                   | ND                 | ND          |
|    16 |          | GND                  | GND                | GND         |
|    17 |          | FG                   | FG                 | FG          |
|    18 | Printer  | Logic-H              | Logic-H            | Logic-H     |
|    19 |          | GND                  | GND                | GND         |
|    20 |          | GND                  | GND                | GND         |
|    21 |          | GND                  | GND                | GND         |
|    22 |          | GND                  | GND                | GND         |
|    23 |          | GND                  | GND                | GND         |
|    24 |          | GND                  | GND                | GND         |
|    25 |          | GND                  | GND                | GND         |
|    26 |          | GND                  | GND                | GND         |
|    27 |          | GND                  | GND                | GND         |

<!-- page 88 -->

|   Pin | Source   | Compatibility Mode   | Nibble Mode       | Byte Mode   |
|-------|----------|----------------------|-------------------|-------------|
|    28 |          | GND                  | GND               | GND         |
|    29 |          | GND                  | GND               | GND         |
|    30 |          | GND                  | GND               | GND         |
|    31 | Host     | Init                 | Init              | Init        |
|    32 | Printer  | Fault                | DataAvail/Data0,4 | DataAvail   |
|    33 |          | GND                  | ND                | ND          |
|    34 | Printer  | DK_STATUS            | ND                | ND          |
|    35 | Printer  | +5V                  | ND                | ND          |
|    36 | Host     | SelectIn             | 1284-Active       | 1284-Active |

## NC: No n e Co nn ec t

## ND: No t Def in ed

<!-- image -->

- A signal name with a rule above it indicates an 'L' active signal.
- Bidirectional communications cannot take place, unless all signal names for both sides correspond to each other.
- Connect all signal lines using a twisted-pair cable. Connect the return side to the signal ground level.
- Make sure the signals satisfy electrical characteristics.
- Set the leading edge and trailing edge times to 0.5ms or less.
- Do not ignore Ack or BUSY signals during a data transfer. Ignoring such signals may result in data corruption.
- Make the interface cables as short as possible.

<!-- page 89 -->

## USB (Universal Serial Bus) Interface

## Outline

- F u ll-speed t ra n sm i ss i o n a t 12Mbps [bps: b it s per seco n d]
- Pl ug &amp; Play, Ho t I n ser ti o n &amp; Removable

## USB transmission specifications

## USB function

| Overall specifications                       | According to USB 2.0 specifications   |
|----------------------------------------------|---------------------------------------|
| Transmission speed                           | USB Full-Speed (12 Mbps)              |
| Transmission method                          | USB bulk transmission method          |
| Power supply specifications                  | USB self power supply function        |
| Current consumed by USB bus                  | 0 mA                                  |
| USB packet size (with full-speed connection) |                                       |
| USB bulk OUT (TM)                            | 64 bytes                              |
| USB bulk IN (TM)                             | 64 bytes                              |

## Status transmission from printer with USB interface

I n order t o e n s u re t ha t t here i s n o lack of s t a tu s da t a, it i s n ecessary t o per i od i cally re t r i eve s t a tu s da t a a t t he hos t comp ut er.

U n l i ke RS232C t ra n sm i ss i o n , it ca nn o t spo nt a n eo u sly int err u p t da t a t ra n sm i ss i o n t o t he hos t comp ut er.

The pr int er has a 128-by t e s t a tu s da t a b u ffer. S t a tu ses t ha t exceed t he b u ffer capac it y are ca n celled.

<!-- page 90 -->

## Character Code Tables

- The character code tables show only character configurations. They do not show the actual print pattern.
- 'SP' in the table shows a space.

## Common to All Pages

Whe n I nt er n a ti o n al charac t er se t (See "I nt er n a ti o n al Charac t er Se t s" o n pa g e 102.) i s USA:

<!-- image -->

| HEX   | 0     | 1      | 1      | 2    | 2    | 3    | 3    | 4   | 4   | 5   | 5    | 6   | 6   | 7      |   7 |
|-------|-------|--------|--------|------|------|------|------|-----|-----|-----|------|-----|-----|--------|-----|
| 0     | NUL   | NUL    | DLE    | DLE  | SP 0 | SP 0 | @    | @   |     |     | P    | P   | ` p | ` p    |     |
|       | 00    |        | 16     |      | 32   |      | 48   | 64  |     |     | 80   |     | 96  |        | 112 |
| 1     |       | XON    |        | !    |      | 1    | A    |     |     | Q   |      | a   |     | q      |     |
|       |       | 01     | 17     |      | 33   |      | 49   |     | 65  |     | 81   | 97  |     |        | 113 |
| 2     |       | 02     |        | "    |      | 2    | B    |     |     | R   |      | b   |     | r      |     |
|       |       |        | 18     |      | 34   |      | 50   |     | 66  |     | 82   |     | 98  |        | 114 |
| 3     |       | XOFF   |        | #    |      | 3    | C    |     |     | S   |      | c   |     | s      |     |
|       |       | 03     | 19     |      | 35   |      | 51   | 67  |     |     | 83   |     | 99  |        | 115 |
| 4     | EOT   |        | DC4    | $    |      | 4    | D    |     |     | T   | d    |     |     | t      |     |
|       | 04    |        | 20     |      | 36   |      | 52   |     | 68  |     | 84   |     | 100 |        | 116 |
| 5     | ENQ   |        | NAK 21 | %    | 37   | 5    | E    |     |     | U   | 85 e |     | 101 | u      | 117 |
|       |       | 05     |        |      | 38   |      | 53   |     | 69  |     |      |     |     |        |     |
| 6     | ACK   |        |        | &    |      | 6    | F    |     |     | V   | f    |     |     | v      |     |
|       |       | 06     | 22     |      |      |      | 54   |     | 70  |     | 86   |     | 102 |        | 118 |
| 7     |       | 07     | 23     | '    | 39   | 7    | 55 G | 71  | W   |     | 87 g |     | 103 | w      | 119 |
| 8     |       | CAN 08 | 24     | ( 40 |      | 8    | 56 H | 72  |     | X   | 88 h |     | 104 | x      | 120 |
| 9     | HT    |        |        | )    |      | 9    | I    |     |     | Y   |      |     |     | y      |     |
|       |       | 09     | 25     |      | 41   |      | 57   | 73  |     |     | 89   | i   | 105 |        | 121 |
| A     | LF    |        |        | ∗    |      | :    | J    |     |     | Z   | j    |     |     | z      |     |
|       |       | 10     | 26     |      | 42   |      | 58   |     | 74  |     | 90   |     | 106 |        | 122 |
| B     |       | ESC    |        | +    |      | ;    | K    |     |     | [   |      | k   |     | {      |     |
|       |       | 11     | 27     |      | 43   |      | 59   | 75  |     | 91  |      |     | 107 |        | 123 |
| C     | FF 12 | FS     | 28     | ,    | 44   | <    | 60 L | 76  | ¥   |     | 92 l |     | 108 | &#124; | 124 |
| D     |       | GS     | 29     | -    |      |      | M    |     |     |     |      | m   |     |        |     |
|       | CR    |        |        |      |      | =    |      | 77  | ]   |     | 93   |     | 109 | }      |     |
|       | 13    |        |        | 45   |      |      | 61   |     |     |     |      |     |     |        | 125 |
| E     |       | RS     |        | .    |      | >    | 62 N |     |     | ^   |      | n   | 110 | ~      | 126 |
| F     |       | 15     | 31     | /    | 47   | ?    | O    |     |     | 95  | 94 o | 111 |     | SP     |     |
|       |       |        |        |      |      |      | 63   | 79  |     | _   |      |     |     |        | 127 |

<!-- page 91 -->

## Page 0 [PC437: USA, Standard Europe]

<!-- image -->

| HEX   |    | 9       | 9   |     |    | A B   | C     | C   | D   | D   | E     | E   | F   |   F |
|-------|----|---------|-----|-----|----|-------|-------|-----|-----|-----|-------|-----|-----|-----|
| 0     | Ç  | Ç       | É   | É   | á  | á     |       | └   | └   | ╨   | ╨     | α ≡ | α ≡ |     |
|       |    | 128     |     | 144 |    | 160   | 176   | 192 |     | 208 |       | 224 |     | 240 |
| 1     | ü  |         | æ   |     | í  | ▒     | ┴     |     | ╤   |     | β     |     | ±   |     |
|       |    | 129     |     | 145 |    | 161   | 177   | 193 |     | 209 |       | 225 |     | 241 |
| 2     | é  |         | Æ   |     | ó  | ▓     | ┬     |     | ╥   |     | Γ     |     | ≥   |     |
|       |    | 130     |     | 146 |    | 162   | 178   | 194 |     | 210 |       | 226 |     | 242 |
| 3     | â  |         | ô   |     | ú  | │     | ├     |     | ╙   |     | π     |     | ≤   |     |
|       |    | 131     |     | 147 |    | 163   | 179   | 195 |     | 211 |       | 227 |     | 243 |
| 4     | ä  |         | ö   |     | ñ  | ┤     | ─     |     | ╘   |     | Σ     |     | ⌠   |     |
|       |    | 132     |     | 148 |    | 164   | 180   | 196 |     | 212 |       | 228 |     | 244 |
| 5     | à  |         | ò   |     | Ñ  | ╡     | ┼     |     | ╒   |     | σ     |     | ⌡   |     |
|       |    |         |     |     | a  | 166   | 182   | 197 |     | 213 |       | 229 |     |     |
| 6     | å  |         | û   |     |    | ╢     | ╞     |     | ╓   |     | μ     |     | ÷   |     |
|       |    | 134     |     | 150 |    |       |       | 198 |     | 214 |       | 230 |     | 246 |
| 7     | ç  | 135     | ù   | 151 | o  | 167 ╖ | 183 ╟ | 199 | ╫   | 215 | τ 231 |     | ≈   | 247 |
| 8     |    |         | ÿ   | 152 | ¿  | ╕     | 184 ╚ | 200 | ╪   | 216 | Ф     |     | °   |     |
| 9     | ë  |         | Ö   |     | ┌  | 168   | ╔     |     |     |     | 232   |     | •   | 248 |
|       | ê  | 136 137 |     | 153 |    | 169   | 185   | 201 | ┘   | 217 | Θ     | 233 |     | 249 |
| A     | è  |         | Ü   |     | ¬  | ║     | ╩     |     | ┌   |     |       |     | ·   |     |
|       |    | 138     |     | 154 |    | 170   | 186   | 202 |     | 218 | Ω     | 234 |     | 250 |
| B     | ï  |         | ¢   |     | ½  | ╗     | ╦     |     | █   |     |       |     | √   |     |
|       |    | 139     |     | 155 |    | 171   | 187   | 203 |     | 219 | δ     | 235 |     | 251 |
| C     | î  |         | £   |     | ¼  | ╝     | ╠     |     | ▄   | 220 | ∞     |     | n   |     |
|       |    | 140     |     | 156 |    | 172   | 188   | 204 |     |     |       | 236 |     | 252 |
| D     | ì  |         | ¥   |     | ¡  | ╜     | ═     |     | ▌   |     | Φ     |     | ²   |     |
|       |    | 141     |     | 157 |    | 173   | 189   | 205 |     | 221 |       | 237 |     | 253 |
| E     | Ä  |         | Pt  |     | «  | ╛     | ╬     |     | ▐   |     | ε     |     | ■   |     |
|       |    | 142     |     | 158 |    | 174   | 190   | 206 |     | 222 |       | 238 |     | 254 |
| F     | Å  |         | ƒ   |     | »  | ┐     | ╧     |     | ▀   | 223 |       | 239 | SP  | 255 |
|       |    | 143     |     | 159 |    | 175   | 191   | 207 |     |     | ∩     |     |     |     |

<!-- page 92 -->

## Page 1 (Katakana)

<!-- image -->

<!-- page 93 -->

## Page 2 (PC850: Multilingual)

<!-- image -->

| HEX   |    | 9       | 9   |     |    | A B   | C     | C       | D   | D   | E     | E   | F   |   F |
|-------|----|---------|-----|-----|----|-------|-------|---------|-----|-----|-------|-----|-----|-----|
| 0     | Ç  | Ç       | É   | É   | á  | á     |       | └       | └   | ð   | ð     | Ó - | Ó - |     |
|       |    | 128     |     | 144 |    | 160   | 176   | 192     |     | 208 |       | 224 |     | 240 |
| 1     | ü  |         | æ   |     | í  | ▒     | ┴     |         | Ð   |     | β     |     | ±   |     |
|       |    | 129     |     | 145 |    | 161   | 177   | 193     |     | 209 |       | 225 |     | 241 |
| 2     | é  |         | Æ   |     | ó  | ▓     | ┬     |         | Ê   |     | Ô     |     |     |     |
|       |    | 130     |     | 146 |    | 162   | 178   | 194     |     | 210 |       | 226 |     | 242 |
| 3     | â  |         | ô   |     | ú  | │     | ├     |         |     | Ë   | Ò     |     | ¾   |     |
|       |    | 131     |     | 147 |    | 163   | 179   | 195     |     | 211 |       | 227 |     | 243 |
| 4     | ä  |         | ö   |     | ñ  | ┤     | ─     |         | È   |     | õ     |     | ¶   |     |
|       |    | 132     |     | 148 |    | 164   | 180   | 196     |     | 212 |       | 228 |     | 244 |
| 5     | à  |         | ò   |     | Ñ  | Á     | ┼     |         | ı   |     | Õ     |     | §   |     |
|       |    | 133     |     | 149 |    | 165   | 181   | 197     |     | 213 |       | 229 |     | 245 |
| 6     | å  |         | û   |     | a  | Â     | ã     |         | Í   |     | μ     |     | ÷   |     |
|       |    | 134     |     | 150 |    | 166   | 182   | 198     |     | 214 |       | 230 |     | 246 |
| 7     | ç  |         | ù   | 151 | o  | À     | 183 Ã |         | Î   |     | þ 231 |     | ¸   |     |
|       |    | 135     |     |     |    | 167   |       | 199 200 |     | 215 | Þ     |     |     | 247 |
| 8     | ê  |         | ÿ   |     | ¿  | ©     | ╚     |         | Ï   |     |       |     | °   |     |
|       |    | 136     |     | 152 |    | 168   | 184   |         |     | 216 |       | 232 |     | 248 |
| 9     | ë  | 137     | Ö   | 153 | ®  | 169 ╣ | 185 ╔ | 201     | ┘   | 217 | Ú     | 233 | ¨   | 249 |
|       |    | 138     |     | 154 |    | 170   | 186   | 202     |     |     | 234   |     |     | 250 |
| A     | è  |         | Ü   |     | ¬  | ║     | ╩     |         | ┌   | 218 | Û     |     | ·   |     |
| B     | ï  | 139     | ø   | 155 | ½  | 171   | 187 ╦ | 203     | █   | 219 | Ù     | 235 | ¹   | 251 |
| C     | î  |         | £   |     |    | ╝     |       |         | ▄   |     | ý     |     |     |     |
|       |    | 140     |     |     |    | 172   | 188   |         |     |     |       |     |     | 252 |
|       |    |         |     |     | ¼  |       | ╠     | 204     | ¦   | 220 |       |     | ³   |     |
| D     | ì  |         | Ø   | 156 | ¡  |       | 189 ═ | 205     |     |     | 236 Ý |     | ²   |     |
| E     |    |         |     |     |    | ¥     | ╬     |         | Ì   |     | ¯     |     |     | 253 |
|       | Ä  | 141     |     | 157 |    | 173   |       |         |     | 221 |       | 237 |     |     |
|       |    |         | ×   |     | «  |       | 190   |         |     |     |       |     | ■   |     |
|       |    | 142 143 |     | 158 |    | 174   |       | 206     |     | 222 | ´     | 238 |     | 254 |
| F     | Å  |         | ƒ   |     | »  | ┐     | ¤     |         | ▀   | 223 |       |     | SP  |     |
|       |    |         |     | 159 |    | 175   | 191   | 207     |     |     |       | 239 |     | 255 |

<!-- page 94 -->

## Page 3 (PC860: Portuguese)

<!-- image -->

| HEX   |    | 9   | 9   |     |    | A B   | C     | C   | D   | D   | E   | E   |     |    | F   |
|-------|----|-----|-----|-----|----|-------|-------|-----|-----|-----|-----|-----|-----|----|-----|
| 0     | Ç  | Ç   | É   | É   | á  | á     |       | └   | └   | ╨   | ╨   | α   | α   | ≡  | ≡   |
|       |    | 128 |     | 144 |    | 160   | 176   |     | 192 |     | 208 |     | 224 |    | 240 |
| 1     | ü  |     | À   |     | í  | ▒     | ┴     |     |     | ╤   |     | β   |     | ±  |     |
|       |    | 129 |     | 145 |    | 161   | 177   |     | 193 |     | 209 |     | 225 |    | 241 |
| 2     | é  |     | È   |     | ó  |       | ┬     |     |     | ╥   |     | Γ   |     | ≥  |     |
|       |    | 130 |     | 146 |    | 162   | 178   |     | 194 |     | 210 |     | 226 |    | 242 |
| 3     | â  |     | ô   |     | ú  |       | ├     |     |     | ╙   |     | π   |     | ≤  |     |
|       |    | 131 |     | 147 |    | 163   | 179   |     | 195 |     | 211 |     | 227 |    | 243 |
| 4     | ã  |     | õ   |     | ñ  |       | ─     |     |     | ╘   |     | Σ   |     | ⌠  |     |
|       |    | 132 |     | 148 |    | 164   | 180   |     | 196 |     | 212 |     | 228 |    | 244 |
| 5     | à  |     | ò   |     | Ñ  |       | ┼     |     |     | ╒   |     | σ   |     | ⌡  |     |
|       |    | 134 |     | 150 | a  | 166   | 182   |     |     |     |     |     |     |    | 246 |
| 6     | Á  |     | Ú   |     |    |       |       | ╞   |     | ╓   |     | μ   |     | ÷  |     |
|       |    |     |     |     |    |       |       |     | 198 |     | 214 |     | 230 |    |     |
| 7     | ç  | 135 | ù   | 151 | o  | 167   | 183 ╟ |     | 199 | ╫   | 215 | τ   | 231 | ≈  | 247 |
|       |    |     |     |     |    |       |       |     |     |     | 216 |     |     |    |     |
| 8     | ê  |     | Ì   |     | ¿  |       |       | ╚   |     | ╪   |     | Ф   |     | °  |     |
|       |    | 136 |     | 152 |    | 168   | 184   |     | 200 |     |     |     | 232 |    | 248 |
| 9     | Ê  |     | Õ   |     | Ò  |       | ╔     |     |     | ┘   |     | Θ   | 233 | •  |     |
| A     | è  |     |     | 154 | ¬  |       | 186   | ╩   | 202 |     |     | Ω   | 234 |    | 250 |
|       |    | 138 | Ü   |     |    | 170   |       |     |     | ┌   | 218 |     |     | ·  |     |
| B     | Í  | 139 |     |     |    |       |       |     |     | █   | 219 |     |     | √  | 251 |
|       |    |     | ¢   | 155 | ½  | 171   | 187   | ╦   | 203 |     |     | δ   | 235 |    |     |
| C     |    |     |     | 156 |    | 172   |       |     |     | ▄   |     | ∞   |     | n  | 252 |
|       | Ô  | 140 | £   |     | ¼  |       | 188   | ╠   | 204 |     | 220 |     | 236 |    |     |
| D     | ì  |     | Ù   |     | ¡  |       | ═     |     | 205 | ▌   |     | Φ   |     | ²  |     |
|       |    | 141 |     | 157 |    | 173   | 189 ╬ |     |     |     | 221 |     | 237 |    | 253 |
|       |    |     |     | 158 |    | 174   |       |     | 206 |     | 222 |     |     |    | 254 |
| E     | Ã  | 142 | Pt  |     | «  | ╛     | 190   |     |     | ▐   |     | ε   | 238 | ■  |     |
|       |    | 143 |     | 159 |    | 175   |       |     |     |     | 223 |     | 239 |    | 255 |
| F     | Â  |     | Ó   |     | »  | ┐     | ╧     |     |     | ▀   |     | ∩   |     | SP |     |
|       |    |     |     |     |    |       | 191   |     | 207 |     |     |     |     |    |     |

<!-- page 95 -->

## Page 4 (PC863: Canadian-French)

<!-- image -->

| HEX   |    |     |    | 9   | 9   |         | C       | C   | D   | D   | E     | E   |         |     | F       |
|-------|----|-----|----|-----|-----|---------|---------|-----|-----|-----|-------|-----|---------|-----|---------|
| 0     | Ç  | Ç   | É  | É   | ¦   | ░       | ░       | └   | └   | ╨   | ╨     | α   | α       | ≡   | ≡       |
|       |    | 128 |    | 144 |     | 160     | 176     |     | 192 |     | 208   |     | 224     |     | 240     |
| 1     | ü  |     | È  |     | ´   | ▒       | ┴       |     |     | ╤   |       | β   |         | ±   |         |
|       |    | 129 |    | 145 |     | 161     | 177     |     | 193 |     | 209   |     | 225     |     | 241     |
| 2     | é  |     | Ê  |     | ó   | ▓       |         | ┬   |     | ╥   |       | Γ   |         | ≥   |         |
|       |    | 130 |    | 146 |     | 162     | 178     |     | 194 |     | 210   |     | 226     |     | 242     |
| 3     | â  |     | ô  |     | ú   | │       | ├       |     |     | ╙   |       | π   |         | ≤   |         |
|       |    | 131 |    | 147 |     | 163     | 179     |     | 195 |     | 211   |     | 227     |     | 243     |
| 4     | Â  |     | Ë  |     | ¨   | ┤       |         | ─   |     | ╘   |       | Σ   |         | ⌠   |         |
|       |    | 132 |    | 148 |     | 164     | 180     |     | 196 |     | 212   |     | 228     |     | 244     |
| 5     | à  |     | Ï  |     | ¸   | ╡       |         | ┼   |     | ╒   |       | σ   |         | ⌡   |         |
|       |    | 133 |    | 149 |     | 165 ╢   | 181 182 |     | 197 |     | 213   |     | 229 230 |     | 245 246 |
| 6     | ¶  |     | û  |     | ³   |         |         | ╞   |     | ╓   |       | μ   |         | ÷   |         |
|       |    | 134 |    | 150 |     | 166     |         |     | 198 |     | 214   |     |         |     |         |
| 7     | ç  | 135 | ù  | 151 | ¯   | ╖       | 183     | ╟   | 199 | ╫   | 215   | τ   | 231     | ≈   | 247     |
|       |    | 136 |    |     |     |         |         | ╚   |     | ╪   | 216   |     | 232     |     |         |
| 8     | ê  |     | ¤  | 152 | Î   | ╕       |         |     | 200 |     |       | Ф   |         | °   |         |
|       |    |     |    |     |     | 168     | 184     |     |     |     |       |     |         |     | 248     |
| 9     | ë  | 137 | Ô  | 153 | ┌   | 169 ╣ ║ | 185 ╔   | ╩   | 201 | ┘   | 217 Θ |     | 233     | • · | 249     |
| A     | è  | 138 | Ü  | 154 | ¬   | 170     | 186     |     | 202 | ┌   | 218   | Ω   | 234     |     | 250     |
| B     | ï  |     | ¢  |     | ½   | ╗       |         | ╦   |     | █   |       | δ   |         | √   |         |
|       |    | 139 |    | 155 |     | 171     | 187     |     | 203 |     | 219   |     | 235     |     | 251     |
| C     | î  |     | £  |     | ¼   | ╝       |         | ╠   |     | ▄   |       | ∞   |         | n   |         |
|       |    | 140 |    | 156 |     |         | 188     |     | 204 |     | 220   |     | 236     |     | 252     |
| D     |    |     | Ù  |     |     | 172 ╜   |         | ═   |     | ▌   |       | Φ   |         | ²   |         |
|       |    | 141 |    | 157 | ¾   | 173     | 189     |     | 205 |     | 221   |     | 237     |     | 253     |
| E     | À  |     | Û  |     | «   | ╛       | ╬       |     |     | ▐   |       | ε   |         | ■   |         |
|       |    | 142 |    | 158 |     | 174     | 190     |     | 206 |     | 222   |     | 238     |     | 254     |
| F     | §  |     | ƒ  |     | »   | ┐       |         | ╧   |     | ▀   |       | ∩   |         | SP  |         |
|       |    | 143 |    | 159 |     | 175     | 191     |     | 207 |     | 223   |     | 239     |     | 255     |

<!-- page 96 -->

## Page 5 (PC865: Nordic)

<!-- image -->

| HEX   |    | 9   | 9   |     |    | A B   | A B   | C     |   C | D   | D   | E     | E   | F   |   F |
|-------|----|-----|-----|-----|----|-------|-------|-------|-----|-----|-----|-------|-----|-----|-----|
| 0     | Ç  | Ç   | É   | É   | á  | á     | ░ └   | ░ └   |     |     | ╨   | ╨     | α ≡ | α ≡ |     |
|       |    | 128 |     | 144 |    | 160   | 176   |       | 192 |     | 208 |       | 224 |     | 240 |
| 1     | ü  |     | æ   |     | í  | ▒     |       | ┴     |     | ╤   |     | β     |     | ±   |     |
|       |    | 129 |     | 145 |    | 161   |       | 177   | 193 |     | 209 |       | 225 |     | 241 |
| 2     | é  |     | Æ   |     | ó  |       | ▓     | ┬     |     | ╥   |     | Γ     |     | ≥   |     |
|       |    | 130 |     | 146 |    | 162   |       | 178   | 194 |     | 210 |       | 226 |     | 242 |
| 3     | â  |     | ô   |     | ú  |       | │     | ├     |     |     | ╙   | π     |     | ≤   |     |
|       |    | 131 |     | 147 |    | 163   | 179   |       | 195 |     | 211 |       | 227 |     | 243 |
| 4     | ä  |     | ö   |     | ñ  |       | ┤     | ─     |     | ╘   |     | Σ     |     | ⌠   |     |
|       |    | 132 |     | 148 |    | 164   | 180   |       | 196 |     | 212 |       | 228 |     | 244 |
| 5     | à  |     | ò   |     | Ñ  |       | ╡     | ┼     |     | ╒   |     | σ     |     | ⌡   |     |
|       |    |     |     |     |    | 166   | 181   |       | 197 |     | 213 |       | 229 |     | 245 |
| 6     | å  |     | û   |     | a  |       | ╢     | ╞     |     | ╓   |     | μ     |     | ÷   |     |
|       |    | 134 |     | 150 |    |       |       | 182   | 198 |     | 214 |       | 230 |     | 246 |
| 7     | ç  | 135 | ù   | 151 | o  | 167 ╖ |       | 183 ╟ | 199 | ╫   | 215 | τ 231 |     | ≈   | 247 |
|       |    |     | ÿ   |     | ¿  | 168   | ╕     |       | 200 | ╪   | 216 |       |     |     |     |
| 8     | ê  |     |     | 152 |    |       |       | ╚     |     |     |     | Ф     |     | °   |     |
| 9     | ë  | 136 | Ö   |     | ┌  |       | 184 ╣ | ╔     |     |     | ┘   | Θ     | 232 | •   | 248 |
|       | è  | 137 |     | 153 |    | 169   |       | 185 ╩ | 201 | ┌   | 217 | 233   |     | ·   | 249 |
| A     |    |     | Ü   | 154 | ¬  |       | ║     |       | 202 |     | 218 | Ω     | 234 |     |     |
|       |    | 138 | ø   |     | ½  | 170   | ╗     | 186   |     | █   |     |       |     |     | 250 |
| B     | ï  | 139 |     | 155 |    | 171   |       | 187 ╦ | 203 |     | 219 | δ     | 235 | √   | 251 |
| C     |    |     | £   |     |    |       |       | ╠     |     | ▄   |     | ∞     |     | n   |     |
|       |    | 140 |     | 156 |    | 172   | ╝     |       |     |     |     |       |     |     |     |
|       | î  |     |     |     | ¼  |       | 188   | ═     | 204 | ▌   | 220 |       | 236 |     | 252 |
| D     | ì  | 141 | Ø   | 157 | ¡  | 173   | ╜     | 189   | 205 |     | 221 | Φ 237 |     | ²   | 253 |
| E     | Ä  |     | Pt  |     |    |       | ╛     | ╬     |     | ▐   |     | ε     |     | ■   |     |
|       |    | 142 |     | 158 | «  | 174   | 190   |       | 206 |     | 222 |       | 238 |     | 254 |
| F     | Å  |     | ƒ   |     | ¤  |       | ┐     | ╧     |     | ▀   |     | ∩     |     | SP  | 255 |
|       |    | 143 |     | 159 |    | 175   | 191   |       | 207 |     | 223 |       | 239 |     |     |

<!-- page 97 -->

## Page 16 (WPC1252)

<!-- image -->

| HEX   |         | 9       | 9     | A       | A     | B       | B       | C       | C     |         |       | F     |   F |
|-------|---------|---------|-------|---------|-------|---------|---------|---------|-------|---------|-------|-------|-----|
| 0     | €       | €       | SP    | SP      | SP °  | SP °    | À       | À       |       | Ð       | Ð     | E à ð |     |
|       |         | 128     |       | 144     |       | 160     |         | 176 192 |       |         | 224   |       | 240 |
| 1     | SP      | SP      | '     | '       | ¡ ±   | ¡ ±     | Á       | Á       | Ñ     | á       | ñ     | ñ     |     |
|       |         | 129     |       | 145     |       | 161     |         | 177 193 |       |         | 225   |       | 241 |
| 2     | ,       | ,       | '     | '       |       |         | Â       | Â       | Ò     | â       | ò     | ò     |     |
|       |         | 130     |       | 146     |       | 162     |         | 178 194 |       |         | 226   |       | 242 |
| 3     | ƒ       | ƒ       | '     | '       | £ ³   | £ ³     | Ã       | Ã       | Ó     | ã       | ó     | ó     |     |
|       |         | 131     |       | 147     |       | 163     |         | 179 195 |       |         | 227   |       | 243 |
| 4     | '       | '       | '     | '       |       |         | Ä       | Ä       | Ô     | ä       | ô     | ô     |     |
|       |         | 132     |       | 148     |       | 164     |         | 180 196 |       |         | 228   |       | 244 |
| 5     | …       | …       | •     | •       | µ     | µ       | Å       | Å       | Õ     | å       | õ     | õ     |     |
|       |         | 133     |       | 149 150 |       | 165     |         | 181 197 |       |         | 229   |       | 245 |
| 6     | †       | †       | -     | -       |       |         | Æ       | Æ       | Ö     | æ       | ö     | ö     |     |
|       |         | 134     |       |         |       | 166     |         | 182 198 |       |         | 230   |       | 246 |
| 7     | ‡ 135   | ‡ 135   | - 151 | - 151   | § 167 | § 167   | · 183 Ç | · 183 Ç | 199 × | ç       | 231 ÷ | 231 ÷ |     |
|       |         |         |       |         |       |         | È       | È       | Ø     | è       | ø     | ø     |     |
| 8     | ˆ 136   | ˆ 136   | ˜ 152 | ˜ 152   | 168   | 168     | 184     | 184     | 200   | 216     | 216   |       | 248 |
|       |         |         |       |         |       |         |         |         |       |         | 232   |       |     |
| 9     | ‰       | 137     | ™ 153 | ™ 153   |       | 169     | É       | É       | Ù     | é       | ù     | ù     | 249 |
|       |         |         |       |         |       |         |         | Ê       |       |         | 233   | ú     |     |
| A     | Š 138 ‹ | Š 138 ‹ | š 154 | š 154   | 170   | 170     | 186     | 186     | 202 Ú | 202 Ú   | 234   | 234   | 250 |
|       |         | 139     |       | 155     |       | 171     |         | 203     |       |         | 235   |       | 251 |
| B     |         |         | ›     | ›       | «     | «       | 187 Ë Ì | 187 Ë Ì |       | 219 ë   | û     | û     |     |
|       |         | 140     |       |         |       |         |         |         |       |         |       | ü     |     |
| C     | Œ       | Œ       | œ     | 156     |       | 172     | 188     | 188     | 204 Ü | ì       | 236   |       | 252 |
| D     |         | 141     |       |         |       | 173     |         |         |       |         |       |       | 253 |
|       |         |         |       |         |       |         | 189 Í   | 189 Í   | 205 Þ | 221 í î | ý     | ý     |     |
|       |         |         |       | 157     |       |         |         |         |       |         | 237   |       |     |
| E     | Ž 142   | Ž 142   | ž     | ž       | ®     | ®       | ¾ 190 Î | ¾ 190 Î |       |         | þ     | þ     |     |
|       |         |         |       | 158     |       | 174 175 |         | 206     |       |         | 238   |       | 254 |
| F     | SP      | SP      | Ÿ     | Ÿ       |       |         | Ï       | Ï       | β     | ï       | ÿ     | ÿ     | 255 |
|       |         | 143     |       | 159     |       |         |         | 191 207 |       |         | 239   |       |     |

<!-- page 98 -->

## Page 17 (PC866: Cyrillic #2)

<!-- image -->

| HEX   | 8   | 9   | 9   |     |    | A B   | A B   | C     |   C | D   | D   | E     | E   | F   |   F |
|-------|-----|-----|-----|-----|----|-------|-------|-------|-----|-----|-----|-------|-----|-----|-----|
| 0     | А   | А   | Р   | Р   | а  | а     | ░ └   | ░ └   |     |     | ╨   | ╨     | р Ё | р Ё |     |
|       |     | 128 |     | 144 |    | 160   | 176   |       | 192 |     | 208 |       | 224 |     | 240 |
| 1     | Б   |     | С   |     | б  | ▒     |       | ┴     |     | ╤   |     | с     |     | ё   |     |
|       |     | 129 |     | 145 |    | 161   |       | 177   | 193 |     | 209 |       | 225 |     | 241 |
| 2     | В   |     | Т   |     | в  |       | ▓     | ┬     |     | ╥   |     | т     |     | Є   |     |
|       |     | 130 |     | 146 |    | 162   |       | 178   | 194 |     | 210 |       | 226 |     | 242 |
| 3     | Г   |     | У   |     | г  |       | │     | ├     |     |     | ╙   | у     |     | є   |     |
|       |     | 131 |     | 147 |    | 163   | 179   |       | 195 |     | 211 |       | 227 |     | 243 |
| 4     | Д   |     | Ф   |     | д  |       | ┤     | ─     |     | ╘   |     | ф     |     | Ї   |     |
|       |     | 132 |     | 148 |    | 164   | 180   |       | 196 |     | 212 |       | 228 |     | 244 |
| 5     | Е   |     | Х   |     | е  |       | ╡     | ┼     |     | ╒   |     | х     |     | ї   |     |
|       |     |     |     |     |    | 166   | 181   |       | 197 |     | 213 |       | 229 | Ў   |     |
| 6     | Ж   |     | Ц   |     | ж  |       | ╢     | ╞     |     | ╓   |     | ц     |     |     |     |
|       |     | 134 |     | 150 |    |       | 182   |       | 198 |     | 214 |       | 230 |     | 246 |
| 7     | З   | 135 | Ч   | 151 | з  |       | ╖     | 183 ╟ |     | ╫   |     | ч 231 |     | ў   |     |
|       |     |     |     |     |    |       | ╕     |       | 200 |     |     |       |     |     |     |
| 8     | И   |     | Ш   | 152 | и  |       |       | ╚     |     | ╪   |     | ш     |     | °   |     |
|       |     | 136 |     |     |    | 168   | 184   |       |     |     | 216 |       | 232 |     | 248 |
| 9     | Й   | 137 | Щ   | 153 | й  | 169   | ╣     | 185 ╔ | 201 | ┘   | 217 | щ     | 233 | •   |     |
|       |     |     | Ъ   | 154 | к  |       | ║     | ╩     |     | ┌   | 218 | ъ     |     | ·   | 249 |
| A     | К   | 138 |     |     |    | 170   | ╗     | 186 ╦ | 202 |     |     |       |     | 234 | 250 |
| B     | Л   | 139 | Ы   | 155 | л  |       | 187   |       | 203 | █   | 219 | ы     | 235 | √   |     |
| C     |     |     | Ь   |     |    | 171   | ╝     | ╠     |     | ▄   |     | ь     |     | №   | 251 |
|       |     | 140 |     |     | м  |       |       |       | 204 |     |     |       | 236 |     | 252 |
|       | М   |     |     | 156 |    | 172   | 188   | ═     |     | ▌   | 220 |       |     |     |     |
| D     | Н   | 141 | Э   | 157 | н  | 173   | ╜ 189 |       | 205 |     | 221 | э     | 237 | ¤   | 253 |
| E     | О   |     |     |     | о  |       | ╛     | ╬     |     | ▐   |     | ю     |     | ■   |     |
|       |     | 142 |     | 158 |    |       |       | 190   |     |     |     |       |     |     | 254 |
|       |     |     | Ю   |     |    | 174   | ┐     | ╧     | 206 |     |     |       |     | SP  |     |
|       |     | 143 |     | 159 |    | 175   |       |       |     |     | 222 |       | 238 |     | 255 |
| F     | П   |     | Я   |     | п  |       |       |       | 207 | ▀   | 223 | я     |     |     |     |
|       |     |     |     |     |    |       | 191   |       |     |     |     |       | 239 |     |     |

<!-- page 99 -->

## Page 18 (PC852: Latin2)

<!-- image -->

| HEX   | 8   | 9   | 9   | A   | A   | B   | C   | C   | D   | D   | E   | E   | F   |   F |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0     | Ç   | Ç   | É   | É   | á   | á   |     | └   | └   | đ   | đ   | Ó - | Ó - |     |
|       |     | 128 |     | 144 | 160 | ░   | 176 | 192 |     | 208 |     | 224 |     | 240 |
| 1     | ü   |     | Ĺ   |     | í   | ▒   | ┴   |     | Ð   |     | β   |     | ˝   |     |
|       |     | 129 |     | 145 | 161 |     | 177 | 193 |     | 209 |     | 225 |     | 241 |
| 2     | é   |     | ĺ   |     |     | ▓   | ┬   |     | Ď   |     | Ô   |     | ˛   |     |
|       |     | 130 | 146 | ó   | 162 |     | 178 | 194 |     | 210 |     | 226 |     | 242 |
| 3     | â   |     | ô   |     | ú   | │   | ├   |     | Ë   |     | Ń   |     | ˇ   |     |
|       |     | 131 | 147 |     | 163 |     |     | 195 |     | 211 |     | 227 |     | 243 |
| 4     | ä   |     | ö   |     | Ą   | ┤   | ─   |     | d ˇ |     | ń   |     |     |     |
|       |     |     |     |     |     |     | 179 |     |     |     |     |     |     |     |
|       |     | 132 | 148 |     |     | 164 | 180 | 196 |     | 212 |     | 228 | ˘   | 244 |
| 5     | ů   |     | ˇ L | ą   |     | Á   | ┼   |     | Ň   |     | ň   |     | §   |     |
|       |     | 133 |     | 149 |     | 165 | 181 | 197 |     | 213 |     | 229 |     | 245 |
| 6     | ć   |     | ˇ l | Ž   |     | Â   | Ă   |     | Í   |     |     |     |     |     |
|       |     | 134 |     | 150 |     | 166 | 182 |     |     | 214 |     | 230 |     | 246 |
| 7     |     |     | Ś   | ž   |     | Ě   |     | 198 |     |     | Š   |     | ÷ ¸ |     |
|       | ç   | 135 |     | 151 |     | 167 | 183 |     | Î   |     | š   | 231 |     | 247 |
|       |     |     |     |     |     |     | ă   | 199 |     | 215 |     |     | °   |     |
| 8     | ł   |     | ś   | Ę   |     | Ş   | ╚   |     | ě   |     | Ŕ   |     |     |     |
|       |     | 136 |     | 152 |     | 168 | 184 | 200 |     | 216 |     | 232 |     | 248 |
|       | ë   |     | Ö   | ę   |     | ╣   | ╔   |     | ┘   |     | Ú   |     | ¨   |     |
| 9     |     | 137 |     | 153 |     | 169 | 185 | 201 |     | 217 |     | 233 |     | 249 |
| A     | Ő   |     | Ü   |     | SP  | ║   | ╩   |     | ┌   |     | ŕ   |     |     |     |
|       |     | 138 |     | 154 |     | 170 | 186 | 202 |     | 218 |     | 234 | •   | 250 |
| B     | ő   |     | Ť   | ź   |     | ╗   | ╦   |     | █   |     | Ű   |     | ű   |     |
|       |     | 139 |     | 155 |     | 171 | 187 | 203 |     | 219 |     | 235 |     | 251 |
| C     | î   |     | ˇ t | Č   |     | ╝   | ╠   |     | ▄   |     |     |     |     |     |
|       |     | 140 |     |     |     | 172 | 188 |     |     |     |     | 236 |     | 252 |
|       |     |     |     |     |     |     |     | 204 |     |     | ý   |     | Ř   |     |
|       |     |     |     | 156 |     |     |     |     |     | 220 |     |     |     |     |
|       | Ź   |     | Ł   | ş   |     | Ż   | ═   |     | Ţ   |     | Ý   |     | ř   |     |
| D     |     | 141 |     | 157 |     | 173 | 189 | 205 |     | 221 |     | 237 |     | 253 |
| E     | Ä   |     | ×   | «   |     | ż   | ╬   |     | Ů   |     | ţ   |     | ■   |     |
|       |     | 142 |     | 158 |     | 174 | 190 | 206 |     | 222 |     | 238 |     | 254 |
| F     | Ć   |     | č   |     |     | ┐   | ¤   |     | ▀   |     | ´   |     | SP  |     |
|       |     | 143 | 159 | »   | 175 |     | 191 | 207 |     | 223 |     | 239 |     | 255 |

<!-- page 100 -->

## Page 19 (PC858: Euro)

<!-- image -->

| HEX   |    | 9   | 9   |     |    | A B   | A B   | C     | C       | D     | E     | E   | F   | F   |
|-------|----|-----|-----|-----|----|-------|-------|-------|---------|-------|-------|-----|-----|-----|
| 0     | Ç  | Ç   | É   | É   | á  | á     | └     | └     |         | ð     | ð     | Ó - | Ó - | Ó - |
|       |    | 128 |     | 144 |    | 160   | ░ 176 |       | 192     | 208   |       | 224 |     | 240 |
| 1     | ü  |     | æ   |     | í  |       | ▒     | ┴     |         | Ð     | β     |     | ±   |     |
|       |    | 129 |     | 145 |    | 161   |       | 177   | 193     | 209   |       | 225 |     | 241 |
| 2     | é  |     | Æ   |     | ó  |       | ▓     | ┬     |         | Ê     |       |     |     |     |
|       |    | 130 |     | 146 |    | 162   |       | 178   | 194     | 210   | Ô     | 226 |     | 242 |
| 3     | â  |     | ô   |     | ú  |       | │     | ├     |         | Ë     | Ò     |     | ¾   |     |
|       |    | 131 |     | 147 |    | 163   |       | 179   | 195     | 211   |       | 227 |     | 243 |
| 4     | ä  |     | ö   |     | ñ  | ┤     |       | ─     |         | È     | õ     |     | ¶   |     |
|       |    | 132 |     | 148 |    | 164   | 180   |       | 196     | 212   |       | 228 |     | 244 |
| 5     | à  |     | ò   |     | Ñ  |       | Á     | ┼     |         | €     | Õ     |     | §   |     |
|       |    | 133 |     | 149 |    | 165   |       | 181   | 197     | 213   |       | 229 |     | 245 |
| 6     | å  |     | û   |     | a  | Â     |       | ã     |         | Í     | μ     |     | ÷   |     |
|       |    | 134 |     | 150 |    | 166   |       | 182   | 198     | 214   |       | 230 |     | 246 |
| 7     | ç  |     | ù   | 151 | o  |       | À     | Ã     |         | Î     | þ     |     | ¸   |     |
|       |    | 135 |     |     |    | 167   |       | 183   | 199 200 | 215   |       | 231 |     | 247 |
| 8     | ê  |     | ÿ   |     | ¿  |       | ©     | ╚     |         | Ï     | Þ     |     | °   |     |
|       |    | 136 |     | 152 |    | 168   |       | 184   |         | 216   |       | 232 |     | 248 |
| 9     | ë  |     | Ö   | 153 | ®  |       | ╣     | ╔     |         | ┘     | Ú     |     | ¨   |     |
|       |    | 137 |     | 154 |    | 169   |       | 185   | 201     | 217   | Û 234 | 233 |     | 249 |
| A     | è  | 138 | Ü   |     | ¬  | 170   | ║     | 186 ╩ | 202     | ┌ 218 |       |     | ·   | 250 |
| B     | ï  | 139 | ø   | 155 | ½  | 171   | ╗     | 187   | ╦ 203   | █ 219 | Ù     | 235 | ¹   |     |
| C     |    |     |     |     |    |       | ╝     |       |         |       | ý     |     |     | 251 |
|       | î  | 140 |     |     |    |       |       | 188   | 204     | ▄     |       |     |     |     |
|       |    |     | £   |     | ¼  |       |       | ╠     |         | 220   |       |     | ³   |     |
| D     | ì  |     | Ø   | 156 |    | 172   | ¢     |       | ═       | ¦     | 236   |     |     | 252 |
| E     |    | 141 |     | 157 | ¡  | 173   | 189   | ╬     | 205     | 221   |       | 237 |     |     |
|       |    |     |     |     |    |       |       |       |         |       | Ý     |     | ²   | 253 |
|       | Ä  |     | ×   |     | «  |       | ¥     |       |         | Ì     | ¯     |     | ■   |     |
|       |    | 142 |     | 158 |    | 174   | 190   |       | 206     | 222   |       | 238 |     | 254 |
| F     | Å  |     | ƒ   |     | »  |       | ┐     | ¤     | 207     | ▀ 223 | ´     |     | SP  |     |
|       |    | 143 |     | 159 |    | 175   |       | 191   |         |       |       | 239 |     | 255 |

<!-- page 101 -->

## Page 255 (User-Defined Page)

| HEX   |    |     |    | 9   | 9     | A B   |   C | C   | D   | D   | E   | E   |    | F   | F   |
|-------|----|-----|----|-----|-------|-------|-----|-----|-----|-----|-----|-----|----|-----|-----|
| 0     | SP | SP  |    |     | SP SP | SP SP |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 128 |    | 144 |       | 160   | 176 |     | 192 |     | 208 |     |    |     | 240 |
| 1     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 129 |    | 145 |       | 161   | 177 |     | 193 |     | 209 |     |    |     | 241 |
| 2     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 130 |    | 146 |       | 162   | 178 |     | 194 |     | 210 |     |    |     | 242 |
| 3     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 131 |    | 147 |       | 163   | 179 |     | 195 |     | 211 |     |    |     | 243 |
| 4     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 132 |    | 148 |       | 164   | 180 |     | 196 |     | 212 |     |    |     | 244 |
| 5     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 133 |    | 149 |       | 165   | 181 |     | 197 |     | 213 |     |    | SP  | 245 |
| 6     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP |     |     |
|       |    | 134 |    | 150 |       | 166   | 182 |     | 198 |     | 214 |     |    |     | 246 |
| 7     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 135 |    | 151 |       | 167   | 183 |     | 199 |     | 215 |     |    |     | 247 |
| 8     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 136 |    | 152 |       | 168   | 184 |     | 200 |     | 216 |     |    |     | 248 |
| 9     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 137 |    | 153 |       | 169   | 185 |     | 201 |     | 217 |     |    |     | 249 |
| A     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 138 |    | 154 |       | 170   | 186 |     | 202 |     | 218 |     |    |     | 250 |
| B     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 139 |    | 155 |       | 171   | 187 |     | 203 |     | 219 |     |    |     | 251 |
| C     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 140 |    | 156 |       | 172   | 188 |     | 204 |     | 220 |     |    |     | 252 |
| D     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 141 |    | 157 |       | 173   | 189 |     | 205 |     | 221 |     |    |     | 253 |
| E     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 142 |    | 158 |       | 174   | 190 |     | 206 |     | 222 |     |    |     | 254 |
| F     | SP | SP  | SP | SP  | SP    | SP    |     | SP  | SP  | SP  | SP  | SP  | SP | SP  | SP  |
|       |    | 143 |    | 159 |       | 175   | 191 |     | 207 |     | 223 |     |    |     | 255 |

<!-- page 102 -->

## International Character Sets

| Country          | ASCII code (Hex)   | ASCII code (Hex)   | ASCII code (Hex)   | ASCII code (Hex)   | ASCII code (Hex)   | ASCII code (Hex)   | ASCII code (Hex)   | ASCII code (Hex)   | ASCII code (Hex)   | ASCII code (Hex)   | ASCII code (Hex)   | ASCII code (Hex)   |
|------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| Country          | 23                 | 24                 | 40                 | 5B                 | 5C                 | 5D                 | 5E                 | 60                 | 7B                 | 7C                 | 7D                 | 7E                 |
| USA              | #                  | $                  | @                  | [                  | \                  | ]                  | ^                  | `                  | {                  | &#124;             | }                  | ~                  |
| France           | #                  | $                  | à                  | °                  | ç                  | §                  | ^                  | `                  | é                  | ù                  | è                  | ¨                  |
| Germany          | #                  | $                  | §                  | Ä                  | Ö                  | Ü                  | ^                  | `                  | ä                  | ö                  | ü                  | β                  |
| U.K.             | £                  | $                  | @                  | [                  | \                  | ]                  | ^                  | `                  | {                  | &#124;             | }                  | ~                  |
| Denmark I        | #                  | $                  | @                  | Æ                  | Ø                  | Å                  | ^                  | `                  | æ                  | ø                  | å                  | ~                  |
| Sweden           | #                  | ¤                  | É                  | Ä                  | Ö                  | Å                  | Ü                  | é                  | ä                  | ö                  | å                  | ü                  |
| Italy            | #                  | $                  | @                  | °                  | \                  | é                  | ^                  | ù                  | à                  | ò                  | è                  | ì                  |
| Spain I          | Pt                 | $                  | @                  | ¡                  | Ñ                  | ¿                  | ^                  | `                  | ¨                  | ñ                  | }                  | ~                  |
| Japan            | #                  | $                  | @                  | [                  | ¥                  | ]                  | ^                  | `                  | {                  | &#124;             | }                  | ~                  |
| Norway           | #                  | ¤                  | É                  | Æ                  | Ø                  | Å                  | Ü                  | é                  | æ                  | ø                  | å                  | ü                  |
| Denmark II       | #                  | $                  | É                  | Æ                  | Ø                  | Å                  | Ü                  | é                  | æ                  | ø                  | å                  | ü                  |
| Spain II         | #                  | $                  | á                  | ¡                  | Ñ                  | ¿                  | é                  | `                  | í                  | ñ                  | ó                  | ú                  |
| Latin America    | #                  | $                  | á                  | ¡                  | Ñ                  | ¿                  | é                  | ü                  | í                  | ñ                  | ó                  | ú                  |
| Korea            | #                  | $                  | @                  | [                  | W                  | ]                  | ^                  | `                  | {                  | &#124;             | }                  | ~                  |
| Slovenia/Croatia | #                  | $                  | Ž                  | Š                  | Đ                  | Ć                  | Č                  | ž                  | š                  | đ                  | ć                  | č                  |
| China            | #                  | Ұ                  | @                  | [                  | \                  | ]                  | ^                  | `                  | {                  | &#124;             | }                  | ~                  |

<!-- page 103 -->



<!-- page 104 -->
