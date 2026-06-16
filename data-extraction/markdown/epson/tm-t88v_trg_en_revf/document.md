# tm-t88v_trg_en_revf


<!-- page 1 -->

<!-- image -->

<!-- image -->

## Technical Reference Guide

## Product Overview

Describes features of the Product.

## Setup

Describes setup and installation of the product.

## Handling

Describes how to handle the product.

## Advanced Usage

Describes advanced usage methods for the product.

## Application Development Information

Describes how to control the printer and necessary information when you develop applications.

## Replacement of the TM-T88IV

Describes precautions for replacement.

## Appendix

Describes general specifications and character codes.

<!-- page 2 -->

## Cautions

- No part of this document may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of Seiko Epson Corporation.
- The contents of this document are subject to change without notice. Please contact us for the latest information.
- While every precaution has been taken in the preparation of this document, Seiko Epson Corporation assumes no responsibility for errors or omissions.
- Neither  is  any  liability  assumed  for  damages  resulting  from  the  use  of  the  information  contained herein.
- Neither Seiko Epson Corporation nor its affiliates shall be liable to the purchaser of this product or third parties for damages, losses, costs, or expenses incurred by the purchaser or third parties as a result of: accident, misuse, or abuse of this product or unauthorized modifications, repairs, or alterations to this product, or (excluding the U.S.) failure to strictly comply with Seiko Epson Corporation's operating and maintenance instructions.
- Seiko Epson Corporation shall not be liable against any damages or problems arising from the use of any options or any consumable products other than those designated as Original Epson Products or Epson Approved Products by Seiko Epson Corporation.

## Trademarks

EPSON is a registered trademark of Seiko Epson Corporation.

Exceed Your Vision and ESC/POS are registered trademarks or trademarks of Seiko Epson Corporation.

Microsoft ®  and Windows ®  are registered trademarks of Microsoft Corporation in the United States and/or other countries.

The Bluetooth ®  word mark and logos are registered trademarks owned by Bluetooth SIG, Inc. and any use of such marks by Seiko Epson Corporation is under license.

IOS is a trademark or registered trademark of Cisco in the U.S. and other countries and is used under license.

Android and Google Play are trademarks of Google, Inc.

Mac is a trademark of Apple Inc., registered in the U.S. and other countries.

Linux ®  is the registered trademark of Linus Torvalds in the U.S. and other countries.

All other trademarks are the property of their respective owners and used for identification purpose only.

## ESC/POS ®  Command System

Epson ESC/POS is a proprietary POS printer command system that includes patented or patentpending commands. ESC/POS is compatible with most Epson POS printers and displays.

ESC/POS is designed to reduce the processing load on the host computer in POS environments. It comprises a set of highly functional and efficient commands and also offers the flexibility to easily make future upgrades.

© Seiko Epson Corporation 2010-2015. All rights reserved.

<!-- page 3 -->

## For Safety

## Key to Symbols

The symbols in this manual are identified by their level of importance, as defined below. Read the following carefully before handling the product.

<!-- image -->

<!-- image -->

You must follow warnings carefully to avoid serious bodily injury.

Provides information that must be observed to prevent damage to the equipment or loss of data.

- Possibility of sustaining physical injuries.
- Possibility of causing physical damage.
- Possibility of causing information loss.

Provides information that must be observed to avoid damage to your equipment or a malfunction.

Provides important information and useful tips.

<!-- page 4 -->

## Warnings

<!-- image -->

- To avoid risk of electric shock, do not set up this product or handle cables during a thunderstorm
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

- If water or other liquid spills into this equipment, do not continue to use it.

Continued use may lead to fire. Unplug the power cord immediately and contact your

dealer or a Seiko Epson service center for advice.

- If you open the DIP switch cover, be sure to close the cover and tighten the screw after adjusting the DIP switch.

Using this product with the cover open may cause fire or electric shock.

- Do  not  use  aerosol  sprayers  containing  flammable  gas  inside  or  around  this product.

Doing so may cause fire.

<!-- page 5 -->

## Cautions

<!-- image -->

- Do not connect cables in ways other than those mentioned in this manual. Different connections may cause equipment damage or fire.
- Be sure to set this equipment on a firm, stable, horizontal surface. The product may break or cause injury if it falls.
- Do not knock or strike the printer. This may cause defective print.
- Do not use this product in locations subject to high humidity or dust levels. Excessive humidity and dust may cause equipment damage or fire.
- Do not place heavy objects on top of this product. Never stand or lean on this product.

Equipment may fall or collapse, causing breakage and possible injury.

- Take care not to injure your fingers on the manual cutter
- ∗ When you remove printed paper
- ∗ When you perform other operations such as loading/replacing roll paper
- Do not open the roll paper cover without taking the necessary precautions, as this can result in injury from the autocutter fixed blade.
- To ensure safety, unplug this product before leaving it unused for an extended period.
- Using in the presence of silicon gas (silicon adhesive, silicon oil, silicon powder, etc.) including siloxane and of malignant gas (nitric acid, hydrosulfuric, ammonia, chlorine, etc.) may cause contact failure at contact points in a mechanical switch and a DC motor, etc., in a short time because of adhesion or oxidization of the insulation film.

## Restriction of Use

When this product is used for applications requiring high reliability/safety, such as transportation devices related to aviation, rail, marine, automotive, etc.; disaster prevention devices; various safety devices, etc.; or functional/precision devices, etc., you should use this product only after giving consideration to including fail-safes and redundancies into your design to maintain safety and total system reliability. Because this product was not intended for use in applications requiring extremely high reliability/safety, such as aerospace equipment, main communication equipment, nuclear power control equipment, or medical equipment related to direct medical care, etc., please make your own judgment on this product's suitability after a full evaluation.

<!-- page 6 -->

## About this Manual

## Aim of the Manual

This manual provides developers/engineers with all the necessary information for design, development and installation of a POS system, and also design and development of a printer application.

## Manual Content

The manual is made up of the following sections:

| Chapter 1   | Product Overview                             |
|-------------|----------------------------------------------|
| Chapter 2   | Setup                                        |
| Chapter 3   | Handling                                     |
| Chapter 4   | Advanced Usage                               |
| Chapter 5   | Application Development Information          |
| Chapter 6   | Replacement of the TM-T88IV                  |
| Appendix    | Product Specifications Option Specifications |

<!-- page 7 -->

## Contents

| ■ For Safety...............................................................................................................................3                 |                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key to Symbols .......................................................................................................................................       | 3                                                                                                                                                       |
| Warnings .................................................................................................................................................   | 4                                                                                                                                                       |
| Cautions..................................................................................................................................................   | 5                                                                                                                                                       |
| ■ Restriction of Use                                                                                                                                         | ..................................................................................................................5                                     |
| ■ About this Manual                                                                                                                                          | ................................................................................................................6                                       |
| Aim of the Manual.................................................................................................................................           | 6                                                                                                                                                       |
| Manual Content ....................................................................................................................................          | 6                                                                                                                                                       |
| ■ Contents ................................................................................................................................7                 |                                                                                                                                                         |
| Product Overview........................................................................11                                                                   |                                                                                                                                                         |
| ■ Features ...............................................................................................................................11                 |                                                                                                                                                         |
| ■ Product Configurations ......................................................................................................13                            |                                                                                                                                                         |
| Interfaces..............................................................................................................................................     | 13                                                                                                                                                      |
| Buzzer                                                                                                                                                       | .................................................................................................................................................... 13 |
| Accessories...........................................................................................................................................       | 14                                                                                                                                                      |
| ■ Part Names and Functions.................................................................................................15                                |                                                                                                                                                         |
| Power Switch ........................................................................................................................................        | 15                                                                                                                                                      |
| Power Switch Cover.............................................................................................................................              | 16                                                                                                                                                      |
| Roll paper cover/Cover open button...............................................................................................                            | 16                                                                                                                                                      |
| Cutter cover                                                                                                                                                 | ......................................................................................................................................... 16            |
| Control Panel                                                                                                                                                | ....................................................................................................................................... 16              |
| Connectors...........................................................................................................................................        | 18                                                                                                                                                      |
| ■ Online and Offline ..............................................................................................................19                        |                                                                                                                                                         |
| Online....................................................................................................................................................   | 19                                                                                                                                                      |
| Offline .................................................................................................................................................... | 19                                                                                                                                                      |
| ■ Error Status...........................................................................................................................20                  |                                                                                                                                                         |
| Automatically Recoverable Errors .....................................................................................................                       | 20                                                                                                                                                      |
| Recoverable Errors...............................................................................................................................            | 20                                                                                                                                                      |
| Unrecoverable Errors ...........................................................................................................................             | 21                                                                                                                                                      |
| ■ NV Memory.........................................................................................................................22                       |                                                                                                                                                         |
| NV Graphics Memory..........................................................................................................................                 | 22                                                                                                                                                      |
| User NV Memory..................................................................................................................................             | 22                                                                                                                                                      |
| Memory Switches (Customized Value) .............................................................................................                             | 23                                                                                                                                                      |
| R/E (Receipt Enhancement) ..............................................................................................................                     | 23                                                                                                                                                      |
| User-defined Page...............................................................................................................................             | 23                                                                                                                                                      |
| Maintenance Counter........................................................................................................................                  | 23                                                                                                                                                      |

<!-- page 8 -->

| Setup                                                                                                                                                     | .............................................................................................25   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| ■ Flow of Setup.......................................................................................................................                    | 25                                                                                                |
| ■ Installing the Printer............................................................................................................                      | 26                                                                                                |
| Important Notes on Horizontal Installation ........................................................................................26                     |                                                                                                   |
| Important Notes on Wall Hanging......................................................................................................26                   |                                                                                                   |
| ■ Changing the Paper Width................................................................................................                                | 27                                                                                                |
| ■ Adjusting the Paper Roll Near-End Sensor.......................................................................                                         | 29                                                                                                |
| ■ Connecting the AC adapter.............................................................................................                                  | 30                                                                                                |
| Connecting the AC adapter..............................................................................................................30                 |                                                                                                   |
| ■ Connecting the Printer to the Host Computer.................................................................                                            | 32                                                                                                |
| For Serial Interface................................................................................................................................32    |                                                                                                   |
| For Parallel Interface ............................................................................................................................34     |                                                                                                   |
| For USB Interface...................................................................................................................................35    |                                                                                                   |
| For Ethernet Interface ..........................................................................................................................38       |                                                                                                   |
| For Wireless LAN Interface ...................................................................................................................39          |                                                                                                   |
| For Bluetooth Interfaces.......................................................................................................................39         |                                                                                                   |
| ■ Connecting the Cash Drawer ...........................................................................................                                  | 40                                                                                                |
| Connecting the Drawer Kick Cable...................................................................................................40                     |                                                                                                   |
| ■ Setting the Built-in Buzzer (for Model with a Built-in Buzzer)                                                                                          | ...................................................................................... 42         |
| ■ Connecting the Optional External Buzzer........................................................................                                         | 43                                                                                                |
| Installing a Buzzer..................................................................................................................................43   |                                                                                                   |
| Printer Settings.......................................................................................................................................43 |                                                                                                   |
| ■ Attaching the Connector Cover.......................................................................................                                    | 45                                                                                                |
| ■ Arranging the Cables ........................................................................................................                           | 47                                                                                                |
| Handling .......................................................................................49                                                        |                                                                                                   |
| ■ Installing and Replacing Roll Paper .................................................................................                                   | 49                                                                                                |
| ■ Removing Jammed Paper ................................................................................................                                  | 51                                                                                                |
| ■ Cleaning the Printer ...........................................................................................................                        | 53                                                                                                |
| Cleaning the Printer Case...................................................................................................................53            |                                                                                                   |
| Cleaning the Thermal Head/Platen Roller ........................................................................................53                        |                                                                                                   |
| ■ Preparing for Transport.......................................................................................................                          | 54                                                                                                |
| Advanced Usage.........................................................................55                                                                 |                                                                                                   |
| ■ Setting the DIP Switches.....................................................................................................                           | 55                                                                                                |

<!-- page 9 -->

| For Serial Interface...............................................................................................................................           | 56                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| For Parallel Interface............................................................................................................................            | 58                                                                                                                                           |
| For Built-in USB Interface......................................................................................................................              | 59                                                                                                                                           |
| For Ethernet/Wireless LAN/USB Interface...........................................................................................                            | 60                                                                                                                                           |
| Bluetooth Interface..............................................................................................................................             | 61                                                                                                                                           |
| Selecting the Print Density (DIP Switches 2-3/2-4)............................................................................                                | 62                                                                                                                                           |
| Selecting the BUSY Status....................................................................................................................                 | 62                                                                                                                                           |
| ■ Setting the Memory Switches                                                                                                                                 |                                                                                                                                              |
| (Customized Value)............................................................................................................63                              |                                                                                                                                              |
| Functions...............................................................................................................................................      | 64                                                                                                                                           |
| ■ Setting/Checking Modes...................................................................................................68                                 |                                                                                                                                              |
| Self-test Mode......................................................................................................................................          | 69                                                                                                                                           |
| NV Graphics Information Print Mode................................................................................................                            | 70                                                                                                                                           |
| Receipt Enhancement Information Print Mode...............................................................................                                     | 71                                                                                                                                           |
| Memory Switch Setting Mode............................................................................................................                        | 71                                                                                                                                           |
| Hexadecimal Dumping Mode...........................................................................................................                           | 73                                                                                                                                           |
| Application Development Information......................................75                                                                                   |                                                                                                                                              |
| ■ Controlling the Printer.........................................................................................................75                          |                                                                                                                                              |
| ESC/POS................................................................................................................................................       | 75                                                                                                                                           |
| ■ Controlling the Cash Drawer                                                                                                                                 | .............................................................................................76                                              |
| ■ Controlling the Built-in Buzzer............................................................................................77                               |                                                                                                                                              |
| ■ Controlling the Optional External Buzzer..........................................................................78                                        |                                                                                                                                              |
| ■ Software and Manuals                                                                                                                                        | .......................................................................................................79                                    |
| Development Kits.................................................................................................................................             | 79                                                                                                                                           |
| Drivers....................................................................................................................................................   | 80                                                                                                                                           |
| Utilities.................................................................................................................................................... | 81                                                                                                                                           |
| Download.............................................................................................................................................         | 82                                                                                                                                           |
| Replacement of the TM-T88IV                                                                                                                                   | ....................................................83                                                                                       |
| ■ Compatibility                                                                                                                                               | ......................................................................................................................83                     |
| Printing ..................................................................................................................................................   | 83                                                                                                                                           |
| Print Density ..........................................................................................................................................      | 83                                                                                                                                           |
| Two-Color Printing ................................................................................................................................           | 83                                                                                                                                           |
| Number of Head Energizing Parts......................................................................................................                         | 83                                                                                                                                           |
| Printable Area (for 80 mmWidth Paper)...........................................................................................                              | 84                                                                                                                                           |
| Cutting Method ...................................................................................................................................            | 84                                                                                                                                           |
| Manual Paper Feed                                                                                                                                             | ............................................................................................................................ 84              |
| Receive Buffer                                                                                                                                                | ...................................................................................................................................... 84    |
| Memory Capacity...............................................................................................................................                | 84                                                                                                                                           |
| Electrical Characteristics ....................................................................................................................               | 84                                                                                                                                           |
| DIP Switches                                                                                                                                                  | ......................................................................................................................................... 85 |
| Printer Status.........................................................................................................................................       | 85 85                                                                                                                                        |
| Logo Registration.................................................................................................................................            |                                                                                                                                              |

<!-- page 10 -->

| Driver Compatibility                                                                                                                                          | .............................................................................................................................85       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| USB Low Power Consumption Mode..................................................................................................86                            |                                                                                                                                       |
| Maintenance Counter.........................................................................................................................86                |                                                                                                                                       |
| Buzzer.....................................................................................................................................................86 |                                                                                                                                       |
| Power Supply Box..................................................................................................................................86          |                                                                                                                                       |
| Overall Dimensions...............................................................................................................................87           |                                                                                                                                       |
| ■ Additional Functions and Functional Improvements......................................................                                                      | 88                                                                                                                                    |
| Paper Width..........................................................................................................................................88       |                                                                                                                                       |
| Print Speed............................................................................................................................................88     |                                                                                                                                       |
| Barcodes ...............................................................................................................................................88    |                                                                                                                                       |
| Number of Characters.........................................................................................................................89               |                                                                                                                                       |
| Image Tone Setting ..............................................................................................................................89           |                                                                                                                                       |
| Interface................................................................................................................................................89   |                                                                                                                                       |
| USB Class................................................................................................................................................89   |                                                                                                                                       |
| Coupon Printing                                                                                                                                               | ...................................................................................................................................89 |
| Customized Value                                                                                                                                              | ................................................................................................................................90    |
| R/E Information Printing Mode............................................................................................................90                   |                                                                                                                                       |
| Low Power Load Mode........................................................................................................................91                 |                                                                                                                                       |
| Reliability ...............................................................................................................................................91 |                                                                                                                                       |
| Appendix......................................................................................93                                                              |                                                                                                                                       |
| ■ Product Specifications.......................................................................................................                               | 93                                                                                                                                    |
| Printing Specifications..........................................................................................................................94           |                                                                                                                                       |
| Character Specifications.....................................................................................................................95               |                                                                                                                                       |
| Printable Area.......................................................................................................................................96       |                                                                                                                                       |
| Printing and Cutting Positions..............................................................................................................98                |                                                                                                                                       |
| Paper Specifications ............................................................................................................................99           |                                                                                                                                       |
| Electrical Characteristics...................................................................................................................100              |                                                                                                                                       |
| Environmental Conditions .................................................................................................................101                 |                                                                                                                                       |
| External Dimensions and Mass..........................................................................................................102                     |                                                                                                                                       |
| ■ Option Specifications ......................................................................................................                                | 103                                                                                                                                   |
| AC adapter (PS-180)..........................................................................................................................103              |                                                                                                                                       |
| ■ Specifications of Interfaces and Connectors................................................................                                                 | 104                                                                                                                                   |
| RS-232 Serial Interface........................................................................................................................104            |                                                                                                                                       |
| IEEE 1284 Parallel Interface................................................................................................................107               |                                                                                                                                       |
| USB (Universal Serial Bus) Interface...................................................................................................110                    |                                                                                                                                       |
| ■ Character Code Tables                                                                                                                                       | ................................................................................................... 111                               |

<!-- page 11 -->

## Product Overview

This chapter describes features of the product.

## Features

## Printing

- High speed printing (300 mm/s maximum).
- Shifting from 80 mm width paper printing to 58 mm width paper printing is available.
- Multi-tone graphic printing.
- Coupon print function is supported.

## Handling

- Easy drop-in paper loading

## Software

- Command protocol is based on the ESC/POS Proprietary Command System.
- OPOS ADK, OPOS ADK for .NET, JavaPOS ADK, and Windows printer drivers are available.
- In addition to supporting several kinds of bar code printing, DS1 DataBar printing and twodimensional symbol (PDF417, QR code, MaxiCode, Composite Symbology) printing are possible.
- Various layouts are possible by using page mode.
- A maintenance counter function is supported.
- User-defined font function is supported.
- Paper-saving function is supported.
- Image tone can be changed.
- The remote configuration  tool  allows  you  to  check  the  status  of  and  configure  the  printer connected to a computer on the network.
- The  TM-T88V  is  ENERGY  STAR  qualified.  (Some  configurations  may  be  exempted, depending on their components.)

1

<!-- page 12 -->

## Others

- Various interface boards (Epson UB series * ) can be used.
- Built-in USB interface is also available for all interface models.
- The TM-T88V Software &amp; Documents Disc (drivers, utility, and manuals).
* Except the following interface boards with the buzzer function
- ∗ UB-E02A, UB-R02A, UB-R03A

<!-- page 13 -->

## Product Configurations

<!-- image -->

- Serial UB + built-in USB interface model
- Parallel UB + built-in USB interface model
- USB UB
- Ethernet UB
- Wireless LAN UB

<!-- image -->

For this printer, never use a LAN interface board or a wireless LAN interface board with a buzzer function.

Otherwise, the printer or the interface board may be damaged.

The name of interface boards with a buzzer function has 'A' at the end.

Example) UB-E**A, UB-R**A (*: alphanumeric character)

## Buzzer

- Model with the built-in buzzer
- Optional external buzzer

The optional external buzzer and the built-in buzzer cannot be used together at the same time.

1

<!-- page 14 -->

## Accessories

## Included

- Roll paper (for operation check)
- Power switch cover
- Connector cover
- Roll paper guide for 58 mm width paper*
- Two strips for the roll paper guide*
- Screw for the roll paper guide*
- The TM-T88V Software &amp; Documents Disc (drivers, utilities, and documentation) *
- Warranty certificate*
- Setup Guide or User's manual
* May not be included depending on the model.

## Options

- AC adapter
- AC cable
- Power supply box (Model: OT-BX88V)
- Affixing tape for fixing the printer (Model: DF-10)
- Wall hanging bracket (Model: WH-10)
- Interface boards (UB series)
- Optional external buzzer (Model: OT-BZ20)

<!-- page 15 -->

## Part Names and Functions

<!-- image -->

## Power Switch

Turns the printer on or off. The marks on the switch: ( : OFF/ : ON)

<!-- image -->

Before turning on the printer, be sure to check that the AC adapter is connected to the power supply.

CAUTION

Before turning the printer off, it is recommended to send a power-off command to the printer. If you use the power-off sequence, the latest maintenance counter values are saved. (Maintenance counter values are usually saved every two minutes.) For detailed information about ESC/POS commands, see the ESC/POS Application Programming Guide.

1

<!-- page 16 -->

## Power Switch Cover

Install the power switch cover that comes with the TM-T88V onto the printer to prevent inadvertent changing of the power switch, to prevent tampering, and to improve the appearance of the printer.

To reset the printer when the power switch cover is installed, insert a long, thin object (such as the end of a paper clip) into the hole in the power switch cover and press the power switch.

<!-- image -->

If an accident occurs with the power switch cover attached, unplug the power cord immediately.

Continued use of the printer may cause fire or shock.

## Roll paper cover/Cover open button

- When loading and replacing roll paper, use the cover open button to open the roll paper cover.
- Do not open the cover during printing or while the auto cutter is operating.

## Cutter cover

Houses the autocutter. Open this when you need to move the cutter manually.

## Control Panel

<!-- image -->

<!-- page 17 -->

## LEDs

## Power LED (green)

- Lights when the power supply is on.
- Goes out when the power supply is turned off.

## Error LED

Lights or flashes when the printer is offline.

- Lights after the power is turned on or after a reset (offline). Automatically goes out after a while to indicate that the printer is ready.
- Lights when the end of the roll paper is detected, and when printing has stopped (offline). If this happens, replace the roll paper.
- Flashes when an error occurs. (For details about the flash codes, see "Error Status" on page 20.)
- Goes out during regular operation (online).

## Paper LED

- Lights when there is no more roll paper or there is little remaining.
- Off when there is a sufficient amount of roll paper remaining.
- Flashes when a self-test is in progress.

## Feed button

Pressing this button once feeds the roll paper by one line. Holding this button down feeds the roll paper continuously.

1

<!-- page 18 -->

## Connectors

All cables are connected to the connector panel on the lower rear of the printer.

<!-- image -->

- Drawer kick connector:
- Interface connector:
- Power supply connector:

Connects a cash drawer or the optional external buzzer.

Connects the printer with the host computer interface.

Connects the power supply unit

The picture above shows a serial interface model. For details on the various interfaces and how to connect the power supply connector and cash drawer, see "Connecting the Printer to the Host Computer" on page 32 and "Connecting the Cash Drawer" on page 40.

<!-- page 19 -->

## Online and Offline

## Online

When no events to go offline have occurred, the printer is online and ready for normal printing.

## Offline

The printer automatically goes offline under the following conditions:

- During power on (including resetting with the interface) until the printer is ready.
- During the self-test.
- When the roll paper cover is open.
- While roll paper is fed using the Feed button.
- When printing stops due to end of paper. (When the roll paper end sensor detects the end of paper or the printer is set so that printing stops upon detection of roll paper near-end.)
- Macro execution standby state.
- When an error has occurred.

1

<!-- page 20 -->

## Error Status

There are three possible error types: automatically recoverable errors, recoverable errors, and unrecoverable errors.

## Automatically Recoverable Errors

Printing is no longer possible when automatically recoverable errors occur. They can be recovered easily, as described below.

| Error                        | Error description                                                       | Error LED flash code          | Recovery measure                                            |
|------------------------------|-------------------------------------------------------------------------|-------------------------------|-------------------------------------------------------------|
| Roll paper cover open error  | The roll paper cover was opened during printing.                        | LED ON LED OFF Approx. 160 ms | Recovers automatically when the roll paper cover is closed. |
| Print head temperature error | A high temperature outside the head drive operating range was detected. | LED ON LED OFF Approx. 160 ms | Recovers automatically when the print head cools.           |

## Recoverable Errors

Printing is no longer possible when recoverable errors occur. They can be recovered easily by turning the power on again or sending an error recovery command from the driver after eliminating the cause of the error.

| Error            | Error description                   | Error LED flash code                          | Recovery measure                                                                                                                                        |
|------------------|-------------------------------------|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Autocutter error | Autocutter does not work correctly. | LED ON LED OFF Approx. 160 ms Approx. 2560 ms | Remove the jammed paper or foreign matter in the printer, close the roll paper cover, send the error recovery command, or turn the power on to recover. |

The error recovery command is valid only if a recoverable error (excluding automatically

recoverable errors) occurs.

<!-- page 21 -->

## Unrecoverable Errors

Printing is no longer possible when unrecoverable errors occur. The printer must be repaired.

<!-- image -->

Turn off the power immediately when unrecoverable errors occur.

| Error                             | Error description                                        | Error LED flash code                          |
|-----------------------------------|----------------------------------------------------------|-----------------------------------------------|
| Memory R/W error                  | After R/W checking, the printer does not work correctly. | LED ON LED OFF Approx. 160 ms                 |
| High voltage error                | The power supply voltage is extremely high.              | LED ON LED OFF Approx. 160 ms                 |
| Low voltage error                 | The power supply voltage is extremely low.               | LED ON LED OFF Approx. 160 ms                 |
| CPU execution error               | The CPU is executing an incorrect address.               | LED ON LED OFF Approx. 160 ms                 |
| Internal circuit connection error | Internal circuits are not connected correctly.           | LED ON LED OFF Approx. 160 ms Approx. 2560 ms |

1

<!-- page 22 -->

## NV Memory

The printer's NV memory (Non-Volatile Memory) stores data even after the printer power is turned off. NV memory contains the following memory areas for the user:

- NV graphics memory
- User NV memory
- Memory switches (customized value)
- R/E (Receipt Enhancement)
- User-defined page
- Maintenance counter

<!-- image -->

NV memory can be rewritten about 100,000 times. As a guide, NV memory rewriting should be 10 times or less a day when you program applications.

## NV Graphics Memory

Graphics, such as shop logos to be printed on receipts, can be stored. Even with a serial interface model whose communication speed is low, high speed graphics printing is possible.

Use the TM-T88V Utility to register graphics.

You can also print and confirm the registered graphics in the NV graphics memory print mode.

<!-- image -->

- For  detailed  information  about  the  TM-T88V  Utility,  see  the  TM-T88V  Utility  User's Manual.
- For  information  about  how  to  use  the  NV  graphics  memory  print  mode,  see  "NV Graphics Information Print Mode" on page 70.

## User NV Memory

You can store and read text data for multiple purposes, such as for storing a note including customizing or maintenance information of the printer.

<!-- page 23 -->

## Memory Switches (Customized Value)

With the memory switches (customized value), which are software switches for the printer, you can set paper width, print density, font, USB class, interface mode, power supply unit capacity, automatic paper cut, paper reduction, serial interface transmission speed, and printer model. See "Setting the Memory Switches (Customized Value)" on page 63.

## R/E (Receipt Enhancement)

Graphics, such as shop logos to be printed on top or bottom of receipts can be registered. Use the TM-T88V Utility to register graphics.

## User-defined Page

You can store character data in the user-defined page (character code table: page 255) so that you can also print characters not resident in the printer.

## Maintenance Counter

With this function, printer information, such as the number of lines printed, the number of autocuts, and printer operation time after the printer starts working, is automatically stored in NV memory. You can read the information with the Status API of the APD or OPOS ADK to use it for periodical checks or part replacement.

<!-- image -->

Maintenance Counter can be checked with the TM-T88V Utility or in a self-test.

1

<!-- page 24 -->



<!-- page 25 -->

## Setup

This chapter describes setup and installation of the product and peripherals.

## Flow of Setup

This chapter consists of the following sections along with the setup flow of the product and peripherals.

<!-- image -->

<!-- page 26 -->

## Installing the Printer

You can install this printer horizontally. With an optional hanging bracket (WH-10), you can also attach the printer to a wall.

## Important Notes on Horizontal Installation

- The printer must be installed horizontally on a flat surface (not tilted).
- Do not place the printer in dusty locations.
- Do not catch cables or place foreign matter under the printer.

## Important Notes on Wall Hanging

You need to perform the following tasks to install the printer on a wall. For more details, see the installation manual for the optional wall hanging bracket (WH-10).

- Installing the roll-paper stoppers
- Changing the location of the roll paper near-end sensor
- Attaching the connector cover
- Attaching the wall hanging bracket (WH-10)

For the other notes, see the installation manual for the optional wall hanging bracket (WH-10).

<!-- image -->

Be sure to attach the connector cover when you install the printer on a wall using the wall hanging bracket.

<!-- page 27 -->

## Changing the Paper Width

The printer is initially set to print on 80 mm width paper and you can change the printer to print on 58 mm width paper by installing the roll paper guide and changing the paper width setting with the customized value.

Follow the steps below to install the roll paper guide.

Once you change the paper width from 80 mm to 58 mm, you cannot change it back to 80 mm.

To set the customized value, see "Setting the Memory Switches (Customized Value)" on page 63.

- 1 Open the roll paper cover.
- 2 Install the roll paper guide so that the projection on its bottom is aligned with the hole at the right of the roll paper holder.
- 3 Tighten the enclosed screw to fix the roll paper guide.

<!-- image -->

<!-- page 28 -->

- 4 Paste  the  enclosed  2  small  strips  along  the  roll  paper  guide  on  the bottom of the roll paper holder.

Make sure the space between the top edge of the strip and the line of the groove in the roll paper guide is 0.5 mm or less.

<!-- image -->

<!-- page 29 -->

## Adjusting the Paper Roll Near-End Sensor

Below are two situations where a roll paper NE sensor adjustment is required.

- To adjust the detection position to suit the diameter of the roll paper core used.
- To adjust the detection position of remaining amount of paper.
- Since  roll  paper  cores  vary  slightly  in  shape,  depending  on  paper  roll  design  and manufacturing tolerances, it is impossible to detect the remaining paper exactly.
- Use roll paper with a core inner diameter of 12 mm {0.47"} and outer diameter of 18 mm {0.71"} so that the NE sensor can detect the remaining paper as accurately as possible.

Follow the steps below to adjust the roll paper near-end detector.

- 1 Open the roll paper cover, and remove the roll paper.
- 2 Loosen the adjustment screw fastening the sensor, and align the upper edge of the positioning plate with the adjustment position.
- 3 Tighten the adjustment screw.
- 4 After adjustment, make sure that the detection lever operates smoothly.

| Adjustment position     | Remaining amount of paper (outer diameter: mm)   |
|-------------------------|--------------------------------------------------|
| Upper                   | Approx. 27 {1.06"}                               |
| Lower (Default setting) | Approx. 23 {0.97"}                               |

<!-- image -->

<!-- page 30 -->

## Connecting the AC adapter

Use the Epson PS-180 or an equivalent product as the AC adapter.

<!-- image -->

If the printer emits smoke, fire, heat, any strange odor, or unusual noise, turn off the power immediately and unplug the equipment.

## Connecting the AC adapter

- 1 Make sure the printer's power is turned off.
- 2 Connect the AC cable to the AC adapter.
- 3 Insert the connector of the power supply cable onto the power supply connector (stamped 24V ).

<!-- image -->

When removing the DC cable for the AC adapter from the printer, check that the AC cable is not connected, and then grasp the arrow marked section of the connector and pull it straight out.

<!-- image -->

<!-- page 31 -->

<!-- image -->

<!-- page 32 -->

## Connecting the Printer to the Host Computer

- Be sure to install the driver before connecting the printer to the host computer.
- The printer uses modular connectors specifically designed for the cash drawer. Do not connect these connectors to an ordinary telephone line.

## For Serial Interface

## Connecting the serial interface (RS-232) cable

<!-- image -->

Be sure to turn off the power for both the printer and host computer before connecting the cables.

- 1 Insert the interface cable connector firmly into the interface connector on the connector panel.
- 2 When using connectors equipped with screws, tighten them to secure the connectors firmly.
- 3 When using interface cables equipped with a grounding line, attach the ground line to the screw hole marked 'FG' on the printer.
- 4 Connect the other end of the interface cable to the host computer.

<!-- image -->

<!-- page 33 -->

## Customer display connection

## Pass-through connection

You can connect a customer display (DM-D) stand type and the printer to a host computer using a pass-through connection. For more details, see Technical Reference Guide of the customer display.

<!-- image -->

<!-- page 34 -->

## For Parallel Interface

## Connecting the parallel interface cable

- 1 Insert the interface cable connector firmly into the interface connector on the connector panel.
- 2 Press down the clips on either side of the connector to lock it in place.
- 3 When using interface cables equipped with a ground line, attach the ground line to the screw hole marked 'FG' on the printer.
- 4 Connect the other end of the interface cable to the host computer.

<!-- page 35 -->

## For USB Interface

If you want to communicate via the built-in USB interface when you use a model with an interface other than the serial/parallel interface, you need to change the interface mode with the memory switch (customized value). To set the memory switch (customized value), see "Setting the Memory Switches (Customized Value)" on page 63.

## Connecting the built-in USB interface cable

- 1 Put the USB cable on the hook as shown in the figure, then connect it firmly to the built-in USB interface connector.
- 2 Connect the other connector of the cable to the host computer.

<!-- image -->

<!-- page 36 -->

## Connecting the USB interface cable

- 1 Attach the locking wire saddle at the location shown in the figure below.
- 2 Put the USB cable through the locking wire saddle.
- 3 Connect the USB cable from the host computer to the USB upstream connector.

<!-- image -->

<!-- page 37 -->

## Customer display connection

## Y connection (only with the UB-U01III/U02III)

This printer is connected to the host computer via the USB port. When a customer display (DM-D) is to be connected, connect it to the printer via the modular cable.

- Make sure to pull out the power cable before connecting cables.
- When connecting a customer display to the printer, connect the modular jack from the customer display to the DM connector.
- Set the communication conditions of the customer display as follows:
- ∗ Baud rate: 19200 bps
- ∗ Bit length: 8-bit
- ∗ Parity: no parity
- ∗ Stop bit: 1

<!-- image -->

<!-- page 38 -->

## For Ethernet Interface

Connect the printer to a network by a LAN cable via a hub.

For the setting of the network parameters such as IP address, see User's Manual or Technical Reference Guide of UB-Exx.

## Connecting the Ethernet interface cable

<!-- image -->

- When LAN cables are installed outdoors, make sure devices without proper surge protection are cushioned by being connected through devices that do have surge protection.
- Otherwise, the devices can be damaged by lightning.
- Never attempt to connect the customer display cable, drawer kick cable, or the standard telephone line cable to the LAN connector.

Connect a 10BASE-T/100BASE-TX cable to the LAN connector by pressing firmly until the connector clicks into place.

<!-- image -->

<!-- page 39 -->

## For Wireless LAN Interface

For details on how to set up a wireless LAN interface, see User's Manual or Technical Reference Guide of UB-Rxx.

## Wireless LAN interface connection diagram

<!-- image -->

## For Bluetooth Interfaces

## Connecting to smart devices

You can connect by using your smart device's Bluetooth connection settings as well as by using the Epson TM Utility "Bluetooth Setup Wizard". See the iOS Bluetooth ®  TM Printer Technical Reference Guide for details on connecting to iOS devices.

## Connecting to Windows PCs

You can connect quickly and easily by using the EPSON TM Bluetooth ®  Connector utility. Start the utility, select the search method, and then click [Search]. Select the printer you want to pair with, and then click [Connect]. If a passkey entry screen is displayed, enter the Passkey, and then click [OK]. Select the port you want to use from the drop-down list, and then click [OK]. The [Connection complete] screen is displayed.

<!-- image -->

- The device name displayed during pairing is TM-T88V\_xxxxxx (where the last six digits are the product serial number).
- The default Passkey is "0000".

<!-- page 40 -->

## Connecting the Cash Drawer

If the optional external buzzer is used, you cannot use a cash drawer.

## Connecting the Drawer Kick Cable

<!-- image -->

- Specifications of drawers differ depending on makers or models. When you use a drawer other than specified, make sure its specification meets the following conditions.

Otherwise, devices may be damaged.

- ∗ The load, such as a drawer kick solenoid, must be connected between pins 4 and 2 or pins 4 and 5 of the drawer kick connector.
- ∗ When  the  drawer  open/close  signal  is  used,  a  switch  must  be  provided  between drawer kick connector pins 3 and 6.
- ∗ The resistance of the load, such as a drawer kick solenoid, must be 24 Ω or more or the input current must be 1A or less.
- ∗ Be sure to use the 24V power output on connector pin 4 for driving the equipment.
- Use a shield cable for the drawer connector cable.
- Two driver transistors cannot be energized simultaneously.
- Leave  intervals  longer  than  4  times  the  drawer  driving  pulse  when  sending  it continuously.
- Be sure to use the printer power supply (connector pin 4) for the drawer power source.
- Do not insert a telephone line into the drawer kick connector. Doing so may damage the telephone line or printer.
- For specifications with a built-in buzzer, use a cash drawer operated by pin 2 of a drawer kick connector.

When using a cash drawer operated by pin 5, you need to make printer settings. For details, see "Setting the Built-in Buzzer  (for Model with a Built-in Buzzer)" on page 42.

Connect the connector of the drawer kick cable to the printer.

<!-- image -->

<!-- page 41 -->

## Drawer Connection Circuitry

<!-- image -->

<!-- page 42 -->

## Setting the Built-in Buzzer (for Model with a Built-in Buzzer)

For specifications with a built-in buzzer, a pulse output is sent to drawer kick connector pin 5 to beep the buzzer.

When using a cash drawer, connect a cash drawer operated by pin 2.

If you have to use a cash drawer operated by pin 5, change the DIP switch settings for the buzzer circuit.

For details, see ' Setting the DIP Switches' - "Setting Procedure" on page 55.

## DIP Switch for Buzzer Circuit

|   DIP switch | Specified connector pin     | ON            | OFF                   | Default setting   |
|--------------|-----------------------------|---------------|-----------------------|-------------------|
|            1 | Drawer kick connector pin 2 | Buzzer beeps. | Buzzer does not beep. | ON                |
|            2 | Drawer kick connector pin 5 | Buzzer beeps. | Buzzer does not beep. | OFF               |

<!-- image -->

Do not set the buzzer to beep for pin numbers used for drawer operations. The buzzer and the cash drawer cannot be operated by one pulse signal.

For details on controlling the built-in buzzer, see "Controlling the Built-in Buzzer" on page 77.

<!-- page 43 -->

## Connecting the Optional External Buzzer

You can use the optional external buzzer (OT-BZ20) by connecting it to the drawer kick connector.

You need to change the printer settings to make sure that it can be used.

- The optional external buzzer and the cash drawer cannot be used together at the same time. Do not connect them both to the printer at the same time by using a branch cable.
- If you enable the optional external buzzer, the cash drawer cannot be operated even if it is connected.
- You  cannot  use  the  built-in  buzzer  and  the  optional  external  buzzer.  When  using  an optional external buzzer on a model with a built-in buzzer, set the DIP switches for the built-in buzzer to "Do not operate" for each drawer kick connector pin 2/pin 5.

## Installing a Buzzer

See the buzzer's user's manual for details on installing the buzzer.

## Printer Settings

The optional external buzzer is disabled by default. Follow the steps below to change the memory switch (custom values) to make sure it is enabled.

## Changing Settings Using the Utility

- 1 Start the APD5 Utility or TM-T88V Utility.

For details, see the "Advanced Printer Driver Ver.5 Printer Manual" or the "TM-T88V Utility User's Manual".

- 2 Click "Option Buzzer" from the menu, and then select "Use Buzzer".
- 3 Set the timing and beep pattern for the optional buzzer as necessary.

<!-- page 44 -->

## Changing Settings Using Memory Switch Setting Mode

- 1 Start the Memory Switch Setting Mode.

For details, see "Memory Switch Setting Mode" on page 71.

- 2 Select Buzzer Control from Other Settings.
- 3 Select Option Buzzer, and then set Enable.
- 4 Set the timing and beep pattern for the optional buzzer as necessary.

<!-- page 45 -->

## Attaching the Connector Cover

When using the connector cover, attach the connector cover. Follow the steps below to attach the connector cover to protect cables.

- 1 Turn over the printer.
- 2 Position the two hooks on both sides of the connector cover so that they hook the printer case.
- 3 Push the connector cover down to click onto the printer case.
- 4 Pass each cable through the cable exits at the bottom of the connector cover.
- 5 Turn over the printer and make sure the cables are not pinched.

<!-- image -->

<!-- page 46 -->

- The serial, USB, or power cables can pass beneath the front of the printer so that the back of the printer looks uncluttered.
- To  remove  the  connector  cover,  turn  the  printer  over,  and  push  the  connector  cover down while pushing both sides of the connector cover inward to detach the hooks from the printer case.

<!-- image -->

<!-- page 47 -->

## Arranging the Cables

Route the cables when using the connector cover.

Pass the cables through cable exits in the connector cover. The connector cover has cable exits on the back and both sides.

You can also route the cables out the front by passing them through the notch in the printer bottom.

<!-- image -->

If you want to pass the USB cable through the cable exit on the back, fit the cable under the hook on the printer to prevent the cable from coming off.

<!-- image -->

After the cable arrangement, turn over the printer, and make sure the cables are not pinched.

<!-- image -->

<!-- page 48 -->



<!-- page 49 -->

## Handling

This chapter describes basic handling of the printer.

## Installing and Replacing Roll Paper

<!-- image -->

- Do not open the roll paper cover during printing. The printer may be damaged.
- Do not touch the manual cutter with your hands when installing or replacing the roll paper.

Otherwise, you may be injured because the manual cutter blade is sharp.

- Use roll paper that meets the printer specification. For details about paper specification, see "Paper Specifications" on page 99.
- Paper must not be pasted to the roll paper spool.
- 1 Press the cover open lever to open the roll paper cover.

<!-- image -->

When the roll paper cover cannot be opened, see "Removing Jammed Paper" on page 51.

- 2 Remove the used roll paper core, if any.

<!-- page 50 -->

- 3 Install the roll paper in the correct direction.
- 4 Pull out some roll paper, and close the roll paper cover.

<!-- image -->

<!-- image -->

5 Tear off the roll paper with the manual cutter.

<!-- image -->

<!-- page 51 -->

## Removing Jammed Paper

When a paper jam occurs, never pull out the paper forcibly. Open the roll paper cover and remove the jammed paper.

When the roll paper cover cannot be opened, follow the steps below to remove the jammed paper.

<!-- image -->

Do not touch the thermal head (See "Cleaning the Thermal Head/Platen Roller" on page 53.) because it can be very hot after printing.

- 1 Turn off the printer.
- 2 Slide the cutter cover toward the front to open it.
- 3 Turn the knob until you see a triangle in the opening. This returns the cutter blade to the normal position. There is a label near the cutter to assist you.

<!-- image -->

<!-- image -->

<!-- page 52 -->

- 4 Close the cutter cover.
- 5 Open the roll paper cover and remove the jammed paper.

<!-- page 53 -->

## Cleaning the Printer

## Cleaning the Printer Case

Be sure to unplug the AC cable from the wall socket, and turn off the printer before cleaning. Wipe the dirt off the printer case with a dry cloth or a damp cloth.

<!-- image -->

Never clean the product with alcohol, benzine, thinner, or other such solvents. Doing so may damage or break the parts made of plastic and rubber.

## Cleaning the Thermal Head/Platen Roller

Epson recommends cleaning the thermal head periodically (generally every 3 months) to maintain receipt print quality.

Depending on the roll paper used, paper dust may stick to the platen roller and cause an irregular paper feed. To remove the paper dust, clean the platen roller with a cotton swab moistened with water. Turn on the printer power only after the water has completely dried.

Turn off the printer, open the roll paper cover, and clean the thermal elements of the thermal head with a cotton swab moistened with an alcohol solvent (ethanol or IPA).

- After printing, the thermal head can be very hot. Do not touch it and let it cool before you clean it.
- Do not damage the thermal head by touching it with your fingers or any hard object.

<!-- image -->

<!-- page 54 -->

## Preparing for Transport

Follow the steps below to transport the printer.

- 1 Turn off the printer.
- 2 Remove the power supply connector.
- 3 Remove the roll paper.
- 4 Pack the printer upright.

<!-- page 55 -->

## Advanced Usage

## Setting the DIP Switches

On this printer, you can make various settings with DIP switches.

The DIP switches are already set for the current interfaces. Change the setting if necessary. Functions of the DIP switches differ depending on the interface.

For models with the buzzer function, see also "Setting the Built-in Buzzer  (for Model with a Built-in Buzzer)" on page 42.

## Setting Procedure

Follow the steps below to change the DIP switch settings.

<!-- image -->

Before you remove the DIP switch cover, turn the printer off.

Otherwise, a short-circuit may cause the printer to malfunction.

- DIP switch settings are enabled only when the power is turned on or the printer is reset via the interface. If the settings are changed after that, the functions will not change.
- Do not change switches that are fixed to ON or OFF. Otherwise, the printer may not operate normally.
- 1 Make sure the power supply for the printer is turned off.
- 2 Unscrew the screw to remove the DIP switch cover from the base of the printer.

<!-- page 56 -->

<!-- image -->

- 3 Set the DIP switches, using the tip of a tool, such as a small screwdriver.
- 4 Replace the DIP switch cover, and screw it in place.

## For Serial Interface

When using the built-in USB interface, it is not necessary to change the DIP switch setting but their function changes. For the details, see "For Built-in USB Interface" on page 59.

## DIP Switch Bank 1

| SW   | Function                      | ON                                         | OFF                                        | Default setting   |
|------|-------------------------------|--------------------------------------------|--------------------------------------------|-------------------|
| 1-1  | Data reception error          | Ignored                                    | Prints '?'                                 | OFF               |
| 1-2  | Receive buffer capacity       | 45 bytes                                   | 4 KB                                       | OFF               |
| 1-3  | Handshaking                   | XON/XOFF                                   | DTR/DSR                                    | OFF               |
| 1-4  | Word length                   | 7 bits                                     | 8 bits                                     | OFF               |
| 1-5  | Parity check                  | Yes                                        | No                                         | OFF               |
| 1-6  | Parity selection              | Even                                       | Odd                                        | OFF               |
| 1-7  | Transmission speed selections | See the ' Transmission Speed (DIP Switches | See the ' Transmission Speed (DIP Switches | ON                |
| 1-8  | Transmission speed selections | 1-7/1-8)' table below.                     | 1-7/1-8)' table below.                     | OFF               |

For DIP switch 1-2 (Receive buffer capacity), see also DIP switch 2-5 (Sets the release condition of the receive buffer BUSY state.)

<!-- page 57 -->

## Transmission Speed (DIP Switches 1-7/1-8)

| Transmission speed (bps: bits per second)                    | SW 1-7   | SW 1-8   |
|--------------------------------------------------------------|----------|----------|
| Depends on the memory switches (customized value) settings.* | ON       | ON       |
| 4800                                                         | OFF      | ON       |
| 9600 (default)                                               | ON       | OFF      |
| 19200                                                        | OFF      | OFF      |

bps: bits per second

* The default value of transmission speed set with memory switches (customized value) is 38400 bps. (See "Setting the Memory Switches (Customized Value)" on page 63.)

<!-- image -->

Depending on print conditions, such as print duty, print head temperature, and data transmission speed, print speed is automatically adjusted, which can cause white lines due to intermittent print (the motor sometimes stops). To avoid this, set the transmission speed higher or keep the print speed constant by setting it lower.

## DIP Switch Bank 2

| SW        | Function                                                                                                                     | ON                                                                                           | OFF                                                                                          | Default setting   |
|-----------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------|
| 2-1       | Handshaking (BUSY condition)                                                                                                 | Receive buffer full                                                                          | • Offline • Receive buffer full                                                              | OFF               |
| 2-2       | Reserved (Do not change setting)                                                                                             | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-3 ∼ 2-4 | Selects print density                                                                                                        | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | OFF               |
| 2-5       | Sets the release condition of the receive buffer BUSY state. (This function is effective when DIP Switch 1-2 is set to off.) | Releases the BUSY state when the remaining capacity of the receive buffer reaches 138 bytes. | Releases the BUSY state when the remaining capacity of the receive buffer reaches 256 bytes. | OFF               |
| 2-6       | Reserved (Do not change setting)                                                                                             | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-7       | I/F pin 6 reset signal                                                                                                       | Enabled                                                                                      | Disabled                                                                                     | OFF               |
| 2-8       | IF pin 25 reset signal                                                                                                       | Enabled                                                                                      | Disabled                                                                                     | OFF               |

<!-- image -->

- For DIP Switch 2-1 (BUSY condition), see also "Selecting the BUSY Status" on page 62.
- When you use the APD, change the setting of DIP switch 2-1 (BUSY condition) to ON.

<!-- page 58 -->

## For Parallel Interface

When using the built-in USB interface, it is not necessary to change the DIP switch setting but their function changes. For the details, see "For Built-in USB Interface" on page 59.

## DIP Switch Bank 1

| SW        | Function                                                                       | ON             | OFF                                                               | Default setting   |
|-----------|--------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------|-------------------|
| 1-1       | Auto line feed                                                                 | Always enabled | Always disabled                                                   | OFF               |
| 1-2       | Receive buffer capacity                                                        | 45 bytes       | 4 KB                                                              | OFF               |
| 1-3       | Selects paper sensors to output paper-end signals (default value of a command) | Disabled       | Roll paper end sensor enabled, roll paper near-end sensor enabled | OFF               |
| 1-4       | Error signal output                                                            | Disabled       | Enabled                                                           | OFF               |
| 1-5 ∼ 1-8 | Undefined                                                                      | -              | -                                                                 | OFF               |

## DIP Switch Bank 2

| SW        | Function                                                                                                                     | ON                                                                                           | OFF                                                                                          | Default setting   |
|-----------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------|
| 2-1       | Handshaking (BUSY condition)                                                                                                 | Receive buffer full                                                                          | • Offline • Receive buffer full                                                              | OFF               |
| 2-2       | Reserved (Do not change setting)                                                                                             | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-3 ∼ 2-4 | Selects print density                                                                                                        | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | OFF               |
| 2-5       | Sets the release condition of the receive buffer BUSY state. (This function is effective when DIP Switch 1-2 is set to off.) | Releases the BUSY state when the remaining capacity of the receive buffer reaches 138 bytes. | Releases the BUSY state when the remaining capacity of the receive buffer reaches 256 bytes. | OFF               |
| 2-6 ∼ 2-7 | Reserved (Do not change settings)                                                                                            | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-8       | IF pin 31 reset signal (Do not change setting)                                                                               | Fixed to ON                                                                                  | Fixed to ON                                                                                  | ON                |

For DIP Switch 2-1 (BUSY condition), see also "Selecting the BUSY Status" on page 62.

<!-- page 59 -->

## For Built-in USB Interface

When using the serial or parallel interface, it is not necessary to change the DIP switch setting but their function changes. For the details, see "For Serial Interface" on page 56 and "For Parallel Interface" on page 58.

## DIP Switch Bank 1

| SW        | Function                             | ON             | OFF             | Default setting   |
|-----------|--------------------------------------|----------------|-----------------|-------------------|
| 1-1       | Auto line feed                       | Always enabled | Always disabled | OFF               |
| 1-2       | Receive buffer capacity              | 45 bytes       | 4 KB            | OFF               |
| 1-3 ∼ 1-6 | Undefined                            | -              | -               | OFF               |
| 1-7       | Undefined                            | -              | -               | *                 |
| 1-8       | Setting of USB power-saving function | Disabled       | Enabled         | OFF               |

## DIP Switch Bank 2

| SW        | Function                                                                                                                     | ON                                                                                           | OFF                                                                                          | Default setting   |
|-----------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------|
| 2-1       | Handshaking (BUSY condition)                                                                                                 | Receive buffer full                                                                          | • Offline • Receive buffer full                                                              | OFF               |
| 2-2       | Reserved (Do not change setting)                                                                                             | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-3 ∼ 2-4 | Selects print density                                                                                                        | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | OFF               |
| 2-5       | Sets the release condition of the receive buffer BUSY state. (This function is effective when DIP Switch 1-2 is set to off.) | Releases the BUSY state when the remaining capacity of the receive buffer reaches 138 bytes. | Releases the BUSY state when the remaining capacity of the receive buffer reaches 256 bytes. | OFF               |
| 2-6 ∼ 2-7 | Reserved (Do not change settings)                                                                                            | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-8       | Reserved                                                                                                                     | -                                                                                            | -                                                                                            | *                 |

For DIP Switch 2-1 (BUSY condition), see also "Selecting the BUSY Status" on page 62.

<!-- page 60 -->

## For Ethernet/Wireless LAN/USB Interface

## DIP Switch Bank 1

| SW        | Function                | ON             | OFF             | Default setting   |
|-----------|-------------------------|----------------|-----------------|-------------------|
| 1-1       | Auto line feed          | Always enabled | Always disabled | OFF               |
| 1-2       | Receive buffer capacity | 45 bytes       | 4 KB            | OFF               |
| 1-3 ∼ 1-8 | Undefined               | -              | -               | OFF               |

## DIP Switch Bank 2

| SW        | Function                                                                                                                     | ON                                                                                           | OFF                                                                                          | Default setting   |
|-----------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------|
| 2-1       | Handshaking (BUSY condition)                                                                                                 | Receive buffer full                                                                          | • Offline • Receive buffer full                                                              | OFF               |
| 2-2       | Reserved (Do not change setting)                                                                                             | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-3 ∼ 2-4 | Selects print density                                                                                                        | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | OFF               |
| 2-5       | Sets the release condition of the receive buffer BUSY state. (This function is effective when DIP Switch 1-2 is set to off.) | Releases the BUSY state when the remaining capacity of the receive buffer reaches 138 bytes. | Releases the BUSY state when the remaining capacity of the receive buffer reaches 256 bytes. | OFF               |
| 2-6 ∼ 2-7 | Reserved (Do not change settings)                                                                                            | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-8       | Reserved (Do not change setting)                                                                                             | Fixed to ON                                                                                  | Fixed to ON                                                                                  | ON                |

<!-- image -->

For DIP Switch 2-1 (BUSY condition), see also "Selecting the BUSY Status" on page 62.

<!-- page 61 -->

## Bluetooth Interface

## DIP Switch Bank 1

| SW        | Function                | ON             | OFF             | Default setting   |
|-----------|-------------------------|----------------|-----------------|-------------------|
| 1-1       | Auto line feed          | Always enabled | Always disabled | OFF               |
| 1-2       | Receive buffer capacity | 45 bytes       | 4 KB            | OFF               |
| 1-3 ∼ 1-8 | Undefined               | -              | -               | OFF               |

## DIP Switch Bank 2

| SW        | Function                                                                                                                     | ON                                                                                           | OFF                                                                                          | Default setting   |
|-----------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------|
| 2-1       | Reserved (Do not change setting)                                                                                             | Fixed to ON                                                                                  | Fixed to ON                                                                                  | ON                |
| 2-2       | Reserved (Do not change setting)                                                                                             | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-3 ∼ 2-4 | Selects print density                                                                                                        | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.                         | OFF               |
| 2-5       | Sets the release condition of the receive buffer BUSY state. (This function is effective when DIP Switch 1-2 is set to off.) | Releases the BUSY state when the remaining capacity of the receive buffer reaches 138 bytes. | Releases the BUSY state when the remaining capacity of the receive buffer reaches 256 bytes. | OFF               |
| 2-6 ∼ 2-7 | Reserved (Do not change settings)                                                                                            | Fixed to OFF                                                                                 | Fixed to OFF                                                                                 | OFF               |
| 2-8       | Reserved (Do not change setting)                                                                                             | Fixed to ON                                                                                  | Fixed to ON                                                                                  | ON                |

<!-- page 62 -->

## Selecting the Print Density (DIP Switches 2-3/2-4)

| Function                             | SW 2-3   | SW 2-4   |
|--------------------------------------|----------|----------|
| Do not set                           | ON       | ON       |
| Print density (standard)             | OFF      | OFF      |
| Print density (darker than standard) | ON       | OFF      |
| Print density (dark)                 | OFF      | ON       |

- If the print density is set to 'Darker than standard' or 'Dark' level, print speed may be reduced.
- The print density can be set with DIP switches (2-3/2-4) or the customized value. (See "Setting the Memory Switches (Customized Value)" on page 63.) The default setting of the customized value is 'Depends on the DIP switch settings.' If the customized value is changed, the value set with the customized value is enabled.

## Selecting the BUSY Status

With DIP switch 2-1, you can select conditions for invoking a BUSY state as either of the following:

- When the receive buffer is full
- When the receive buffer is full or the printer is offline

<!-- image -->

In either case above, the printer enters the BUSY state after power is turned on (including resetting with the interface) and when a self-test is being run.

## Printer BUSY Condition and Status of DIP Switch 2-1

| Printer status                        | Printer status                                                                                                                    | DIP SW 2-1   | DIP SW 2-1   |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------|--------------|
|                                       |                                                                                                                                   | ON           | OFF          |
| Offline                               | During the period after power is turned on (including resetting with the interface) to when the printer is ready to receive data. | BUSY         | BUSY         |
|                                       | During the self-test.                                                                                                             | BUSY         | BUSY         |
|                                       | When the cover is open.                                                                                                           | -            | BUSY         |
|                                       | During paper feed with the Feed button.                                                                                           | -            | BUSY         |
|                                       | When the printer stops printing due to a paper-end (when printer has run out of roll paper).                                      | -            | BUSY         |
|                                       | When waiting for the paper Feed button to be pressed before macro execution.                                                      | -            | BUSY         |
|                                       | When an error has occurred.                                                                                                       | -            | BUSY         |
| When the receive buffer becomes full. | When the receive buffer becomes full.                                                                                             | BUSY         | BUSY         |

<!-- page 63 -->

## Setting the Memory Switches (Customized Value)

With the 'memory switch (customized value),' a software switch for this printer, you can set the functions shown in the table below.

The memory switches (customized value) are already set. Change the setting if necessary.

For an outline of the functions, see the following section.

Use the methods in this table to set the memory switches (customized value).

|                                                                                                                                                        | Memory Switch Setting Mode   | TM-T88V Utility   | ESC/POS Commands   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|-------------------|--------------------|
| Paper width                                                                                                                                            | ✔                            | ✔                 | ✔                  |
| Print density                                                                                                                                          | ✔                            | ✔                 | ✔                  |
| Multi-tone print density                                                                                                                               | ✔                            | ✔                 | ✔                  |
| Print speed                                                                                                                                            | ✔                            | ✔                 | ✔                  |
| Font • Code page • International character set • Font A/B replacement                                                                                  | ✔                            | ✔                 | ✔                  |
| Optional Buzzer                                                                                                                                        | ✔                            | ✔                 | ✔                  |
| USB class                                                                                                                                              | ✔                            | ✔                 | ✔                  |
| Selection of interface mode                                                                                                                            | ✔                            |                   | ✔                  |
| Number of head energizing parts                                                                                                                        | ✔                            |                   | ✔                  |
| Power supply unit capacity                                                                                                                             | ✔                            | ✔                 | ✔                  |
| Automatic paper cut                                                                                                                                    | ✔                            | ✔                 | ✔                  |
| Paper reduction • Upper space reduction • Lower space reduction • Line space reduction rate • Line feed reduction rate • Barcode height reduction rate | ✔                            | ✔                 | ✔                  |
| Transmission speed for serial interface                                                                                                                | ✔                            | ✔                 | ✔                  |
| Printer model* 1                                                                                                                                       | ✔                            |                   | ✔                  |

<!-- page 64 -->

<!-- image -->

- To directly configure the printer in the memory switch setting mode, see "Memory Switch Setting Mode" on page 71.
- For  detailed  information  about  the  TM-T88V  Utility,  see  the  TM-T88V  Utility  User's Manual.
- For  detailed  information  about  ESC/POS  commands,  see  the  ESC/POS  Application Programming Guide.

## Functions

## Setting the paper width

- 80 mm (default setting)
- 58 mm
- Be sure to install the roll paper guide when you select the 58 mm paper width. (See "Changing the Paper Width" on page 27.)
- Once you change the paper width from 80 mm to 58 mm, you cannot change it back to 80 mm.

## Setting the print density

Selectable from levels 1 to 13 (70% ∼ 130%)

<!-- image -->

The print density can be set with DIP switches (2-3/2-4) or the customized value. (See "Selecting the Print Density (DIP Switches 2-3/2-4)" on page 62.) The default setting of the customized value is 'Depends on the DIP switch settings.' If the customized value is changed, the value set with the customized value is enabled.

## Setting the multi-tone print density

Selectable from levels 1 to 13 (70% ∼ 130%)

- First change the print density, and then configure the Multi-tone print density.
- If  you  set  the  density  too  high,  the  contrast  becomes  lower.  Select  the  density  level checking the overall tone balance of your image.

<!-- page 65 -->

## Setting the print speed

Selectable from levels 1 to 13 (Slow ∼ Fast) (default setting: level 13)

<!-- image -->

Depending on print conditions, such as print duty, print head temperature, and data transmission speed, print speed is automatically adjusted, which may cause white lines due to intermittent print (the motor sometimes stops). To avoid this, keep the print speed constant by setting it lower, or set the transmission speed higher for the serial interface. (See "Transmission Speed (DIP Switches 1-7/1-8)" on page 57.)

## Setting font

- Code page: Selectable from 43 pages including user defined page
- International character set: Selectable from 18 sets
- Font A/B replacement

## Optional Buzzer

When to sound the buzzer is selectable from the following occasions.

- When an error occurs
- When automatic paper cut activates
- When specified pulse 1 (2 pin) occurs
- When specified pulse 2 (5 pin) occurs

## USB Class

- Printer Class
- Vendor Class

4

<!-- page 66 -->

## Selecting interface mode

Selectable from: automatic selection, fixed to UB interface, or fixed to built-in USB. Those 3 modes are described in both tables below.

<!-- image -->

The TM-T88V has dual interfaces: a built-in USB interface and another interface selected by the customer. (The selectable interface is referred to as the 'UB' interface.) The table below describes the modes you can set for the printer to control the dual interfaces.

## For models with serial/parallel UB

| Interface mode                        | UB            | Built-in USB   |
|---------------------------------------|---------------|----------------|
| Automatic selection (default setting) | Available     | Available      |
| Fixed to UB                           | Available     | Not available  |
| Fixed to built-in USB                 | Not available | Available      |

## For models with other UB

| Interface mode                        | UB            | Built-in USB   |
|---------------------------------------|---------------|----------------|
| Automatic selection (default setting) | Available     | Not available  |
| Fixed to UB                           | Available     | Not available  |
| Fixed to built-in USB                 | Not available | Available      |

<!-- image -->

## Automatic selection:

The interface of either the UB or built-in USB to which data is transmitted first is selected. Once the interface is selected, the selection is enabled until the power is turned off or the printer is reset.

## Setting the number of head energizing parts

- One-part energizing (default setting)
- Two-part energizing
- Four-part energizing
- Usually, the number of head energizing parts does not need to be changed.
- The maximum print speed (300 mm/s) can be performed only when one-part energizing is selected.

<!-- image -->

<!-- page 67 -->

## Setting the power supply unit capacity

Selectable from levels 1 to 3 (Low ∼ High) (default setting: level 3)

Depending on the print pattern or usage environment and so on, if problems such as a low voltage error or power shutdown occur, you may be able to avoid the problem by setting the power supply unit capacity. If you cannot avoid the problem even after setting the power supply unit capacity to level 1, you may be able to avoid it by reducing the print speed and reviewing the print pattern (reducing the amount of printing).

## Setting the automatic paper cut

- Not use this function (default setting)
- Cut paper when the cover is closed
- Print logo when paper is cut

Printing logo when paper is cut is not available with memory switch setting mode.

## Setting the paper reduction

- Extra upper space reduction: enabled or disabled (default setting)
- Extra lower space reduction: enabled or disabled (default setting)
- Line space reduction rate: not reduced (default setting), 25%, 50%, or 75%
- Line feed reduction rate: not reduced (default setting), 25%, 50%, or 75%
- Barcode height reduction rate: not reduced (default setting), 25%, 50%, or 75%

## Setting the transmission speed for serial interface

When DIP switches 1-7 and 1-8 are set to ON, the memory switch settings (custom values) are enabled.  You can select the communication speed from 2400, 4800, 9600, 19200, 38400, 57600, or 115200 bps. (The default is 38400 bps.) (See "Transmission Speed (DIP Switches 1-7/1-8)" on page 57.)

## Setting the printer model

When you use the TM-T88V with the APD Ver. 4.00 ~ 4.04, you need to change the printer model name to 'TM-T88IV.'

<!-- page 68 -->

## Setting/Checking Modes

As well as print mode, the following modes are also provided for making various printer settings and checking items.

- Self-test mode
- NV graphics information print mode
- R/E (receipt enhancement) information print mode
- Memory switch setting mode
- Hexadecimal dumping mode

The self-test mode or hexadecimal dumping mode is selected depending on the operation performed when the power is turned on.

NV graphic information print mode, R/E (receipt enhancement) information print mode, and the Memory switch setting mode are selected depending on the Feed button operation performed during a self-test.

<!-- image -->

<!-- page 69 -->

In (1) and (2), the following guidances are printed, the Power LED flashes, and instructs the user's operations.

- (1) Continuing self-test guidance

```
Select Modes by pressing Feed Button. Continue SELF-TEST: Less than 1 second
```

```
Mode Selection    : 1 second or more
```

(2) Mode selection guidance

## Mode Selection

## Modes

```
0: Exit and Reboot Printer 1: NV Graphics Information 2: Receipt Enhancement Information 3: Customize Value Settings 4 or more: None
```

Select Modes by executing following procedure.

```
step 1. Press the Feed button less than 1 second as many times as the selected mode number. step 2. Press Feed button for 1 second or more.
```

## Self-test Mode

You can check the following items using the self-test.

- Firmware version
- Interface information
- Buffer capacity
- BUSY condition (depends on the interface)
- Built-in fonts
- Auto line feed setting (parallel interface only)
- Print density
- Maintenance information (head mileage, autocut count)
- Settings of Dip switch 1 and 2

4

<!-- page 70 -->

Follow the steps below.

- 1 Close the roll paper cover.
- 2 While pressing the Feed button, turn on the printer. (Hold down the Feed button until printing starts.)

After printing the current print status, a Continuing self-test guidance is printed, and the Power LED flashes.

- 3 Briefly press the Feed button (less than one second) to continue the selftest.

The printer prints a rolling pattern on the roll paper, using the built-in character set.

After '*** completed ***' is printed, the printer initializes and switches to standard mode.

## NV Graphics Information Print Mode

Prints the following NV graphic information registered to the printer.

- NV graphics capacity
- NV graphics usage capacity
- NV graphics free capacity
- NV graphics registration
- Key code for each data, number of X direction dots, number of Y direction dots
- NV graphics data

For details on NV graphics, see "NV Graphics Memory" on page 22.

Follow the steps below.

- 1 After running a self-test, hold down the Feed button for at least one sec-
- ond, and then select the Mode selection.

The Mode selection guidance is printed, and the Paper LED flashes.

- 2 After briefly (less than one second) pressing the Feed button once, hold it down for at least one second, to print the NV graphics information.
- After information printing, the Mode selection guidance is printed again.
- 3 To finish, turn off the power, or select 'Exit and Reboot Printer'.

<!-- page 71 -->

## Receipt Enhancement Information Print Mode

Prints the following R/E (receipt enhancement) information registered to the printer.

- Automatic top logo setting
- Automatic bottom logo setting
- Extended settings for automatic top/bottom logo

Follow the steps below.

- 1 After running a self-test, hold down the Feed button for at least one second, and then select the Mode selection.

The Mode selection guidance is printed, and the Power LED flashes.

- 2 After briefly pressing the Feed button twice (less than one second), hold it down for at least one second, to print the Receipt enhancement information.
- 3 To finish, turn off the power, or select "Exit and Reboot Printer".

## Memory Switch Setting Mode

You can configure the memory switches (customized values) of the printer.

- Print density
- Communication conditions using a serial interface
- Auto reduction of the amount of paper to use
- Autocutting of paper while the cover is closed
- Paper width
- Default value of character code page/international character set
- Auto replacement of font
- Selection of an interface
- Selection of USB class
- Power supply capacity
- Print speed
- Other settings (optional external buzzer control and so on)

<!-- image -->

For detailed information about memory switches (customized value), see "Setting the Memory Switches (Customized Value)" on page 63.

4

<!-- page 72 -->

Follow the steps below.

- 1 After running a self-test, hold down the Feed button for at least one second, and then select the Mode selection.

The Mode selection guidance is printed, and the Paper LED flashes.

- 2 Briefly press the Feed button three times (less than one second), hold it down for at least one second, and then select the Software settings mode (Customized value setting).

The Software setting mode guidance is printed, and the Paper LED flashes.

<!-- image -->

- 3 After briefly pressing the Feed button (less than one second) for the number of times shown in the print result, hold down the button for more than one second, and then select the setting items.

Options for the selected setting item, the current value and default value are printed. Depending on the setting item, you may need to continue selecting the setting item before the settings are printed.

<!-- page 73 -->

- 4 Select a setting by briefly pressing the Feed button (less than one second) for the number of times applicable to the setting, and then hold down the button for more than one second to confirm your selection. After saving the settings, the Software setting mode guidance is printed, and the Paper LED flashes.
- 5 To  close  Software  setting  mode,  turn  off  the  printer,  or  select  'Exit'  to return to Mode selection guidance, and then select 'Exit and Reboot Printer'.
- To select 0 as the item number, hold down the Feed button until printing starts.
- If the button is pressed a number of times that is not displayed by the Setup guidance, the operation is invalid and the same guidance is printed.

## Hexadecimal Dumping Mode

In hexadecimal dumping mode, data from the host computer is printed in hexadecimal numbers and characters. By comparing the print outs and the program, you can check whether or not data is being sent to the printer correctly.

<!-- image -->

- When there are no characters that correspond to the print data, ' . ' is printed.
- If you press the Feed button when there is less than one line of print data, one line is printed.
- During hexadecimal dumping mode, applications that check the printer status may not operate correctly. The printer only returns the status for the 'Real-time transmission status' command.

Follow the steps below.

- 1 Open the roll paper cover.
- 2 While pressing the Feed button, turn on the printer. (Hold down the Feed button until the Error LED turns on.)
- 3 Close the roll paper cover. From this point, all data received by the printer is printed in the corresponding hexadecimal numbers and ASCII characters.

<!-- page 74 -->

Example of printing in hexadecimal dumping mode

```
Hexadecimal Dump To terminate hexadecimal dump, press FEED button three times. 1B 21 00 1B 26 02 40 40 1B 69  . ! . . & . @ @ . i 1B 25 01 1B 63 34 00 1B 30 31  . % . . c 4 . . 0 1 41 42 43 44 45 46 47 48 49 4A  A B C D E F G H I J ***  completed  ***
```

- 4 To close hexadecimal dumping mode, turn off the printer after printing is complete, or press the Feed button for three times.

<!-- page 75 -->

## Application Development Information

This chapter describes how to control the printer and gives information useful for printer application development.

## Controlling the Printer

The printer supports the following command systems:

- ESC/POS

Users can control the printer by using the aforementioned command, or the following development kits or drivers.

- OPOS ADK
- OPOS ADK for .NET
- JavaPOS ADK
- EPSON Advanced Printer Driver (APD)
- ePOS-Print SDK (for Android/iOS/Windows Store Apps/JavaScript)

## ESC/POS

ESC/POS is the Epson original printer command system for POS printers and customer display. With ESC/POS commands, you can directly control all the printer functions, but detailed knowledge of printer specifications or combination of commands is required, compared to using drivers and applications.

For detailed information about ESC/POS commands, see the ESC/POS Command Reference that can be accessed from the following URL.

https://reference.epson-biz.com/pos/reference/

<!-- page 76 -->

## Controlling the Cash Drawer

A pulse output is sent to drawer kick connector pin 2 or pin 5, and you can open the drawer.

You can also check the open/close status of the drawer by checking the signal level of the drawer kick connector pin 3.

These controls are executed by a driver or by commands.

## ESC/POS Commands

Prepare the output command for the specified pulse and the status transmission command. For details, see the ESC/POS Command Reference.

## For Windows Printer Drivers (APD)

You can set so that the drawer opens at the start/end of printing or start/end of a page. For details, see the manual for drivers.

For details on control, see the manual for Status API of the driver.

## OPOS (OCX Driver)

Register a cash drawer using the SetupPOS Utility, and control using the OpenDrawer method or the DirectIO function.

For details, see the "EPSON OPOS ADK MANUAL APPLICATION DEVELOPMENT GUIDE Cash Drawer" and the "UnifiedPOS Specification".

## OPOS for .NET

Register a cash drawer using the SetupPOS Utility, and control using the OpenDrawer method or the DirectIO function.

For details, see the "EPSON OPOS ADK for .NET MANUAL Application Development Guide Cash Drawer (EPSON Standard)" and the "UnifiedPOS Specification".

## ePOS-Print SDK

The output command for the drawer kick pulse and the status transmission command are provided in each SDK library. For details, see the user's manuals provided with each SDK.

<!-- image -->

- Whether or not pin 2 or pin 5 operates the drawer kick connector depends on the connected cash drawer.
- You can acquire documents regarding the UnifiedPOS from the following link. https://nrf.com/resources/retail-technology-standards/unifiedpos

<!-- page 77 -->

## Controlling the Built-in Buzzer

For specifications with a built-in buzzer, a pulse output is sent to the operating pin for the drawer kick connector, and the built-in buzzer beeps.

You cannot change the volume or the sound emitted, but you can change the buzzing time by changing the signal pulse width.

This is controlled by a driver or by commands.

## ESC/POS Commands

The output command for the specified pulse is used.

For details, see the ESC/POS Command Reference.

## For Windows Printer Drivers (APD)

You can set so that the buzzer beeps at the start/end of printing or start/end of a page. For details, see the manual for drivers.

For API, the API for opening the drawer is used. For details, see the manual for Status API of the driver.

## OPOS (OCX Driver)

Register a POS printer using the SetupPOS Utility and control using the DirectIO function. For details, see the "EPSON OPOS ADK MANUAL APPLICATION DEVELOPMENT GUIDE POSPrinter (TM Series)".

## OPOS for .NET

Register a POS printer using the SetupPOS Utility and control using the DirectIO function. For details, see the "EPSON OPOS ADK for .NET MANUAL Application Development Guide POSPrinter (TM-T88V)".

## ePOS-Print SDK

Use the output command for the drawer kick pulse provided in each SDK library. For details, see the user's manuals provided with each SDK.

<!-- image -->

When using a cash drawer operated by pin 5 with a built-in buzzer, you need to change the DIP switch settings for the buzzer circuit so that the buzzer beeps from a pulse signal for pin 2. For details, see "Setting the Built-in Buzzer  (for Model with a Built-in Buzzer)" on page 42.

<!-- page 78 -->

## Controlling the Optional External Buzzer

You can set the optional external buzzer to buzz when an error occurs and when an automatic cut off occurs.

The buzzer can be buzzed using a driver or a command.

You can also set the timing and the beep pattern for the buzzer.

## ESC/POS Command

Use the buzzer control command or the output command for the specified pulse.

For details, see the ESC/POS Command Reference.

## For Windows Printer Drivers (APD)

You can set so that the buzzer beeps at the start/end of printing or start/end of a page. For details, see the manual for drivers.

For API, use the DirectIO function or the API for opening the drawer. For details, see the manual for Status API of the drivers.

## OPOS (OCX Driver)

Register a POS printer using the SetupPOS Utility and control using the DirectIO function. For details, see the "EPSON OPOS ADK MANUAL APPLICATION DEVELOPMENT GUIDE POSPrinter (TM Series)".

## OPOS for .NET

Register a POS printer using the SetupPOS Utility and control using the DirectIO function. For details, see the "EPSON OPOS ADK for .NET MANUAL Application Development Guide POSPrinter (TM-T88V)".

## ePOS-Print SDK

The command for the buzzer function is provided in each SDK library. For details, see the user's manuals provided with each SDK.

For details on setting the optional external buzzer, see "Connecting the Optional External Buzzer" on page 43.

<!-- page 79 -->

## Software and Manuals

The following software and manuals are provided for application development.

## Development Kits

| Software               | Description                                                                                                                                                              | Target model                             |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| ePOS-Print SDK         | This development kit is for controlling the printer from Web applications and native applications of smart devices. It includes libraries, manuals, and sample programs. |                                          |
| for Android            | This development kit is for controlling the printer from Web applications and native applications of smart devices. It includes libraries, manuals, and sample programs. | Ethernet/ Wireless LAN / Bluetooth / USB |
| for iOS                | This development kit is for controlling the printer from Web applications and native applications of smart devices. It includes libraries, manuals, and sample programs. | Ethernet / Wireless LAN / Bluetooth      |
| for Windows Store Apps | This development kit is for controlling the printer from Web applications and native applications of smart devices. It includes libraries, manuals, and sample programs. | Ethernet / Wireless LAN / Bluetooth      |
| for JavaScript         | This development kit is for controlling the printer from Web applications and native applications of smart devices. It includes libraries, manuals, and sample programs. | Ethernet *1 / Wireless LAN *2            |

- *1: Except for models with the following interface boards. UB-E02, UB-E02A, UB-E03
- *2: Except for models with the following interface boards. UB-R02, UB-R02A, UB-R03, UB-R03A

| Software                | Description                                                                                                                                                                                                                                                                                                             | Operating environment   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| EPSON OPOS ADK          | This OCX driver can control POS peripherals using OLE technology* 1 . Because controlling POS peripherals with original commands is not required on the application side, efficient system development is possible.                                                                                                     | Windows                 |
| EPSON OPOS ADK for .NET | The OPOS ADK for .NET is a POS industry standard printer driver compatible with Microsoft POS for .NET. It allows you to develop applications that are compatible with the UPOS (Unified POS) specification. When developing applications, use a separate development environment such as Microsoft Visual Studio .NET. | Windows                 |

<!-- page 80 -->

| Software    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Operating environment   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| JavaPOS ADK | JavaPOS is the standard specification which defines an architecture and device interface (API) to access various POS devices from a Java based system. Using JavaPOS standard API allows control with Java based applications of functions inherent to each device. A flexible design with Java language and JavaPOS enables many different types of computer systems, such as stand alone or network configuration, to use a same application. You can use JavaPOS to build applications and drivers independently of platforms. This allows flexible configurations using thin clients to meet the system requirements. | Windows, Linux          |

*1: OLE technology developed by Microsoft divides software into part blocks.

The OPOS driver is presupposed to be used with a development environment such as Visual Basic, unlike ordinary Windows printer drivers. It is not a driver to be used for printing from commercial applications.

## Drivers

| Software                            | Description                                                                                                                                                                                                                                                                                                                                                                                             | Operating environment   |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| EPSON Advanced Printer Driver (APD) | In addition to ordinary Windows printer driver functions, this driver has controls specific to POS. The Status API (Epson original DLL) that monitors printer status and sends ESC/POS commands is also attached to this driver.                                                                                                                                                                        | Windows                 |
| EPSON TM Virtual Port Driver        | This is a serial/parallel-USB/LAN conversion driver to make an Epson TM/BA/EU printer connected via USB or LAN accessible from a POS application through a virtual serial or parallel port. It allows you to directly control devices connected via USB or LAN with ESC/ POS commands without making changes in the POS application that controls devices connected via a serial or parallel interface. | Windows                 |

<!-- page 81 -->

| Software                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Operating environment   |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| TM-T88V Mac Printer Driver                | Mac printer driver allows you to control the TM-T88V using Common UNIX Printing System (CUPS) on Mac OS X. This is a full raster printer driver. It is able to print images, text, and vector graphics etc., that an application displays. With this driver many printer controls are possible, such as paper cut timing control, cash drawer control, print speed control, blank line skip, and upside-down printing. It also provides API and dialogues for print setting, sample applications, and logo setting utility . | Mac                     |
| Epson TM/BA Series Thermal Printer Driver | This driver allows you to control the TM-T88V using Common UNIX Printing System (CUPS) on GNU/Linux. This is a full raster printer driver. It is able to print images, text, and vector graphics etc., that an application displays. With this driver many printer control are possible, such as paper cut timing control, cash drawer control, print speed control, blank line skip, and upside-down printing.                                                                                                              | Linux                   |

## Utilities

| Software                              | Description                                                                                                                                                                                                                                                                                                                                       | Operating environment   |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| TM-T88V Utility                       | A utility for checking and changing various printer settings. Use this utility to: • Checking current settings • Operation check • Storing logos • Coupon settings • Paper reduction settings • Automatic paper cut settings • Printing control settings • Font settings • Optional buzzer settings • Communication I/F settings • Backup/restore | Windows                 |
| TM-T88V Printer Model Setting Utility | Use to change the printer model name when you use the TM-T88V with the APD Ver. 4.00 ~ 4.04.                                                                                                                                                                                                                                                      | Windows                 |

<!-- page 82 -->

| Software        | Description                                                                                                                                                                                                                                                                       | Operating environment   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| EpsonNet Config | A network setting tool for Epson network products. In the case of this printer, you can use this tool to check and/or set network parameters by connecting the Wireless LAN model to a computer for setup via the USB interface.                                                  | Windows, Mac            |
| Monitoring Tool | Use to check a list of status for the Epson printers connected to the network.                                                                                                                                                                                                    | Windows                 |
| Deployment Tool | Use to make network and printer settings simultaneously, via USB. Allows you to make settings efficiently at the time of introducing TM printers for the first time, or when configuring multiple TM printers at the same time.                                                   | Windows                 |
| BmpToRaster     | This is a command line and GUI utility that converts Windows BMP files to raster graphics data for ESC/POS commands. You can create a variety of multiple tone or monochrome image print data. You can print graphics by sending the created binary file to the printer as it is. | Windows                 |

## Download

You can obtain software and manuals from one of the following URLs.

For customers in North America, go to the following web site and follow the on-screen instructions.

http://www.epsonexpert.com/

For customers in other countries, go to the following web site:

http://download.epson-biz.com/?service=pos

<!-- page 83 -->

## Replacement of the TM-T88IV

The TM-T88V is designed so that it can smoothly replace the TM-T88IV. This chapter describes precautions for the replacement.

## Compatibility

## Printing

The printing and character specifications are the same as those of the TM-T88IV. Without special configurations, the TM-T88V prints the same results as the TM-T88IV prints.

## Print Density

The print density of the TM-T88V can be set with DIP switches (2-3/2-4) as can the TM-T88IV. Set the density the same as for the TM-T88IV to print in the same print density.

<!-- image -->

The print density can be set also with a customized value. The default setting of the customized value is 'Depends on the DIP switch settings.' If the customized value is changed, the value set with the customized value is enabled. (See "Setting the Memory Switches (Customized Value)" on page 63.)

## Two-Color Printing

You cannot use the paper for two-color printing (P320RB/P320BB) with the TM-T88V, which you can use with the TM-T88IV.

## Number of Head Energizing Parts

For the TM-T88V, the default setting of the number of head energizing parts is 'One-part energizing.' You can change the setting with the customized value (See "Setting the Memory Switches (Customized Value)" on page 63.); however it does not usually need to be changed.

|                                | TM-T88V                                                            | TM-T88IV                                                     |
|--------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------|
| Number of head energizing part | • One-part energizing • Two-part energizing • Four-part energizing | One-part energizing Two-part energizing Four-part energizing |

<!-- page 84 -->

## Printable Area (for 80 mm Width Paper)

The printable area (left/right margins, print start position from the autocutting position, print start position from the manual cutting position) of the TM-T88V is the same as that of the TM-T88IV.

## Cutting Method

The TM-T88V uses the partial cutting method (cutting with one point in left edge left uncut) as does the TM-T88IV.

## Manual Paper Feed

Manual paper feed is not possible with the TM-T88V while it is possible with the TM-T88IV after printing pauses.

## Receive Buffer

You can set the receive buffer of the TM-T88V to 4KB or 45 bytes with DIP switch 1-2 as with the TM-T88IV. The buffer full condition and buffer full release condition of the TM-T88V are the same as those of the TM-T88IV.

## Memory Capacity

The sizes of the download buffer and NV graphics data of the TM-T88V are the same as those of the TM-T88IV.

## Electrical Characteristics

The operating voltage of the TM-T88V is DC24 ± 7%, the same as the TM-T88IV. The current consumption differs, depending on the print duty.

<!-- image -->

The TM-T88V does not have a low power consumption mode, which the TM-T88IV has, so you cannot set DIP switches 2-3 and 2-4 to on. Use the newly added low power load mode instead.

<!-- page 85 -->

## DIP Switches

The functional assignments of DIP switches are the same as those of the TM-T88IV except for DIP switches 2-3 and 2-4.

Since the TM-T88V does not have a low power consumption mode, do not set DIP switches 2-3 and 2-4 both to ON.

## Printer Status

The TM-T88V goes to the same status under the same conditions as the TM-T88IV. You can replace the TM-T88V with the TM-T88IV without modifying applications.

## Logo Registration

The TM-T88V can register logos in the NV memory (NVRAM) with the TM-T88V Utility, while the TM-T88IV can register logos with the TM Flash LOGO Setup Utility for NVRAM (TM-Flogo).

For detailed information about the TM-T88V Utility, see the TM-T88V Utility User's Manual.

## Driver Compatibility

You can operate the TM-T88V with a driver for the TM-T88IV or the TM-T88III.

You cannot operate the TM-T88IV with a driver for the TM-T88V.

## Advanced Printer Driver

When the TM-T88IV was controlled by APD Ver. 4.00 ~ 4.04, you need to change the TM-T88V printer model name to 'TM-T88IV' using the customized value. (See "Setting the Memory Switches (Customized Value)" on page 63.)

When the TM-T88IV was controlled by an APD other than Ver. 4.00 ~ 4.04, you can replace it with the TM-T88V without modifying the APD.

## OPOS ADK

If the TM-T88IV was controlled by an OPOS ADK, you can replace it with the TM-T88V without modifying the OPOS ADK.

<!-- page 86 -->

## USB Low Power Consumption Mode

With the TM-T88V, you can enable the USB low power consumption mode with DIP Switch 1-8, just as you can with the TM-T88IV. (See "For Ethernet/Wireless LAN/USB Interface" on page 60.)

## Maintenance Counter

The TM-T88V has a maintenance counter just as the TM-T88IV has.

## Buzzer

TM-T88V is available with a built-in buzzer or without the buzzer. Even if you purchase the one without the buzzer, you can attach an optional external buzzer. You can beep the buzzer with the pulse signal using a command. (See "Setting the Built-in Buzzer  (for Model with a Built-in Buzzer)" on page 42, "Connecting the Optional External Buzzer" on page 43.)

For detailed information about ESC/POS commands, see the ESC/POS Application Programming Guide.

## Power Supply Box

The optional power supply box (OT-BX88V) is available to be attached under the TM-T88V to hold the power unit, just as the OT-BX88 has been available for the TM-T88IV.

<!-- page 87 -->

## Overall Dimensions

You can place the TM-T88V in the same location as the TM-T88IV, since its overall dimensions and weight are about the same as or smaller than those of the TM-T88IV. With the wall hanging bracket (WH-10), you can attach the TM-T88V to a wall just as you can with the TM-T88IV.

<!-- image -->

<!-- page 88 -->

## Additional Functions and Functional Improvements

## Paper Width

You can change the printer to print on 58 mm width paper by installing the roll paper guide and changing the paper width setting with the customized value.

Once you change the paper width form 80 mm to 58 mm, you cannot change it back to 80 mm.

## Print Speed

The TM-T88V has increased its print speed up to a maximum of 300 mm/s.

|                                        | TM-T88V       | TM-T88IV     |
|----------------------------------------|---------------|--------------|
| Maximum print speed                    | 300 mm/s      | 200 mm/s     |
| Print speed setting (Customized value) | Level 1 to 13 | Level 1 to 9 |

Note: When the printer prints text (built-in fonts) with the default print density level at 24V and 25°C {77°F}.

<!-- image -->

Depending on print conditions such as print duty, print head temperature, and data transmission speed, print speed is automatically adjusted.

## Barcodes

With the TM-T88V, printing the following barcodes, two-dimensional symbols and composite symbology is additionally possible.

- GS1-128
- GS1 DataBar Omnidirectional
- GS1 DataBar Truncated
- GS1 DataBar Stacked
- GS1 DataBar Stacked Ominidirectional
- GS1 DataBar Limited
- GS1 DataBar Expanded
- GS1 DataBar Expanded Stacked
- MaxiCode
- Composite Symbology

<!-- page 89 -->

## Number of Characters

For the TM-T88V, character code tables and international characters are added.

| TM-T88V                                      |                                              | TM-T88IV                 |
|----------------------------------------------|----------------------------------------------|--------------------------|
| 128 × 43 pages (including user-defined page) | 128 × 11 pages (including user-defined page) | Character code tables    |
| 18 sets                                      | 14 sets                                      | International characters |

## Image Tone Setting

The TM-T88V allows you to specify tone of images (2 tones/Grayscale).

## Interface

The USB interface is added to the main unit of the TM-T88V as standard equipment.

## USB Class

When using the built-in USB interface or USB Plus Power, USB printer class can be used beside the USB vendor-defined class. This setting can be done in customized value. (See "Setting the Memory Switches (Customized Value)" on page 63.)

## Coupon Printing

The TM-T88V allows you to print coupons registered and set with the TM-T88V Utility.

<!-- image -->

For detailed information about the TM-T88V Utility, see the TM-T88V Utility User's Manual.

6

<!-- page 90 -->

## Customized Value

For the TM-T88V, the following customized value functions are added.

- Paper width
- Multi-tone print density
- Default value of the character code table
- Default value of the international character set
- Optional buzzer
- USB class
- Interface mode
- Power supply unit capacity
- Automatic paper cut when the cover is closed
- Automatic paper-saving (upper space reduction)
- Automatic paper-saving (lower space reduction)
- Automatic paper-saving (line space reduction rate)
- Automatic paper-saving (line feed reduction rate)
- Automatic paper-saving (barcode height reduction rate)
- Font A replacement
- Font B replacement
- Printer model

For the TM-T88V, the following customized value functions are deleted.

- Single-color printing/two-color printing
- Black-color density in two-color printing

For detailed information about the customized value, see "Setting the Memory Switches (Customized Value)" on page 63.

## R/E Information Printing Mode

The TM-T88V has a Receipt Enhancement (R/E) Information Printing mode that lets you confirm the following information:

- Automatic top logo setting
- Automatic bottom logo setting
- Extended settings for automatic top/bottom logo

<!-- page 91 -->

## Low Power Load Mode

For the TM-T88V, there is a new low power load mode. In this mode, the power supply load is lowered by automatically changing the print speed, depending on the print duty. You can set the mode with the customized value. (See "Setting the Memory Switches (Customized Value)" on page 63.)

## Reliability

The TM-T88V has improved reliability.

|      |                   | TM-T88V                   | TM-T88IV                  |
|------|-------------------|---------------------------|---------------------------|
| Life | Printer mechanism | 20 million lines          | 15 million lines          |
| Life | Print head        | 150 million pulse, 150 km | 100 million pulse, 100 km |
| Life | Autocutter        | 2 million cuts            | 1.5 million cuts          |
| MCBF | MCBF              | 70 million lines          | 52 million lines          |

<!-- page 92 -->



<!-- page 93 -->

## Appendix

## Product Specifications

| Printing method                                           | Printing method                                           | Thermal line printing                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cutting method                                            | Cutting method                                            | Partial cut (cutting with one point in left edge left uncut)                                                                                                                                                                                                                                                                                   |
| Roll paper (single-ply) width                             | Roll paper (single-ply) width                             | 80 mmwidth paper printing: 79.5 ± 0.5 mm(3.13 ± 0.02") 58 mmwidth paper printing: 57.5 ± 0.5 mm(2.26 ± 0.02")                                                                                                                                                                                                                                  |
| Interfaces                                                | Interfaces                                                | Serial (RS-232), Parallel (IEEE1284), Ethernet (10/100BASE-T), USB (Full-speed), Wireless LAN (IEEE802.11b)                                                                                                                                                                                                                                    |
| Buffers                                                   | Receive buffer                                            | 4 KB/45 bytes (selectable using DIP switch 1-2)                                                                                                                                                                                                                                                                                                |
| Buffers                                                   | Downloaded buffer                                         | 12 KB (both for user-defined characters and downloaded images)                                                                                                                                                                                                                                                                                 |
| Buffers                                                   | NV graphics data                                          | 256 KB                                                                                                                                                                                                                                                                                                                                         |
| Barcode/two-dimensional symbol/ composite symbol printing | Barcode/two-dimensional symbol/ composite symbol printing | UPC-A, UPC-E, JAN 8 (EAN 8), JAN 13 (EAN 13), CODE 39, ITF , CODABAR (NW-7), CODE 93, CODE 128, GS1-128, GS1 DataBar Omnidirectional, GS1 DataBar Truncated, GS1 DataBar Stacked, GS1 DataBar Stacked Omnidirectional, GS1 DataBar Limited, GS1 DataBar Expanded, GS1 DataBar Expanded Stacked, PDF417, QR CODE, MaxiCode, Composite Symbology |
| DKD function                                              | DKD function                                              | 2 drives                                                                                                                                                                                                                                                                                                                                       |
| Supplied voltage                                          | Supplied voltage                                          | DC 24 V ± 7%                                                                                                                                                                                                                                                                                                                                   |
| Life                                                      | Mechanism                                                 | 20,000,000 lines                                                                                                                                                                                                                                                                                                                               |
| Life                                                      | Thermal head                                              | 150 million pulses 150 km                                                                                                                                                                                                                                                                                                                      |
| Life                                                      | Autocutter                                                | 2,000,000 cuts (when using the specified original paper types, PD150R or PD160R) 1,500,000 cuts (when using paper types other than the specified original paper types)                                                                                                                                                                         |
| Life                                                      | MTBF                                                      | 360,000 hours                                                                                                                                                                                                                                                                                                                                  |
| Life                                                      | MCBF                                                      | 70,000,000 lines                                                                                                                                                                                                                                                                                                                               |
| Temperature/humidity                                      | Temperature/humidity                                      | Operating: 5 to 45°C {41 to 113°F}, 10 to 90% RH Storage: -10 to 50°C {14 to 122°F}, 10 to 90% RH                                                                                                                                                                                                                                              |

<!-- page 94 -->

| Overall dimensions   | 145 × 195 × 148 mm{5.71 × 7.68 × 5.83"} (W × D × H)   |
|----------------------|-------------------------------------------------------|
| Mass                 | Approx. 1.6 kg {3.5 lb} (roll paper excluded)         |

## Printing Specifications

| Printing method        | Printing method        | Thermal line printing                                                                                  |
|------------------------|------------------------|--------------------------------------------------------------------------------------------------------|
| Dot density            | Dot density            | 180 × 180 dpi                                                                                          |
| Printing direction     | Printing direction     | Unidirectional with friction feed (Reverse feed is not supported.)                                     |
| Printing width         | Printing width         | 80 mmwidth paper printing: 72.0 mm(2.83"), 512 dots 58 mmwidth paper printing: 50.8 mm(2.0"), 360 dots |
| Characters per line    | Font A (12 × 24)       | 80 mmwidth paper printing: 42 58 mmwidth paper printing: 30                                            |
| Characters per line    | Font B (9 × 17)        | 80 mmwidth paper printing: 56 58 mmwidth paper printing: 40                                            |
| Maximum print speed* 1 | Maximum print speed* 1 | 300 mm/s                                                                                               |
| Line spacing           | Line spacing           | 4.23 mm{1/6"} (Default value, programmable by command)                                                 |

dpi: dots per inch

*1: when the printer prints text (built-in fonts) with the default print density level at 24V and 25°C {77°F}.

Print speed may be slower, depending on the such items as the data transmission speed.

<!-- page 95 -->

## Character Specifications

| Number of characters             | Number of characters             | Alphanumeric characters: 95 Extended graphics: 128 × 43 pages (including user-defined page) International characters: 18 sets GB18030-2000: 28,533 (for Simplified Chinese characters model) Big 5: 13,535 (for Traditional Chinese characters model) Korean Kanji (KC C5601): 8,366 (for Korean model) Thai character: 3-pass printing font (for South Asia model) 128 characters x 3 pages (133 character types) Vietnam character (for South Asia model) 128 characters x 2 pages (135 character types)   |
|----------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Character structure (W x H dots) | Character structure (W x H dots) | Font A (default): 12 × 24 (including 2-dot horizontal spacing) Font B: 9 × 17 (including 2-dot horizontal spacing)                                                                                                                                                                                                                                                                                                                                                                                           |
| Character size (W x H)           | Font A                           | Standard: 1.41 × 3.39mm Double-height: 1.41 × 6.77mm Double-width: 2.82 × 3.39mm Double-width, double-height: 2.82 × 6.77mm                                                                                                                                                                                                                                                                                                                                                                                  |
| Character size (W x H)           | Font B                           | Standard: 0.99 × 2.40mm Double-height: 0.99 × 4.80mm Double-width: 1.98 × 2.40mm Double-width, double-height: 1.98 × 4.80mm                                                                                                                                                                                                                                                                                                                                                                                  |

## Note:

1. Space between characters is not included.
2. Characters can be scaled up to 64 times as large as the standard size.

<!-- page 96 -->

## Printable Area

## 80 mm paper width printing

The printable area of paper with a width of 79.5 ± 0.5 mm {3.13 ± 0.02"} is 72.2 ± 0.2 mm {2.84 ± 0.008"} (512 dots), and the space on the right and left sides is approximately 3.7 mm {0.15"}.

All the numeric values are typical.

<!-- image -->

- In  2-divided  energizing,  the  print  position  within  the  printable  area  of  the  thermal elements for dots 1 to 256 and 257 to 512 is shifted approximately 0.07 mm {0.0028"} in the paper feed direction as shown in the figure below.
- In  4-divided  energizing,  the  print  position  within  the  printable  area  of  the  thermal elements for dots 1 to 128, 129 to 256, 257 to 384, and 385 to 512 is shifted approximately 0.04 mm {0.0016"} in the paper feed direction as shown in the figure below.

<!-- image -->

<!-- image -->

<!-- page 97 -->

## 58 mm paper width printing

The printable area of paper with a width of 57.5 ± 0.5 mm {2.26 ± 0.02"} is 50.8 ± 0.2 mm {2.00 ± 0.008"} (360 dots), and the space on the left side is approximately 3.7 mm {0.15"} and the space on the right side is approximately 3.0 mm {0.12"}.

All the numeric values are typical.

<!-- image -->

- In  2-divided  energizing,  the  print  position  within  the  printable  area  of  the  thermal elements for dots 1 to 256 and 257 to 360 is shifted approximately 0.07 mm {0.0028"} in the paper feed direction as shown in the figure below.
- In  4-divided  energizing,  the  print  position  within  the  printable  area  of  the  thermal elements for dots 1 to 128, 129 to 256, and 257 to 360 is shifted approximately 0.04 mm {0.0016"} in the paper feed direction as shown in the figure below.

<!-- image -->

<!-- image -->

<!-- page 98 -->

## Printing and Cutting Positions

<!-- image -->

The values above may vary slightly as a result of paper slack or variations in the paper. Take this into account when setting the cutting position of the autocutter.

<!-- page 99 -->

## Paper Specifications

| Paper types                   | Paper types                   | Specified thermal paper                                                                                                                                                                                      |
|-------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Form                          | Form                          | Roll paper                                                                                                                                                                                                   |
| Size                          | Roll paper diameter           | 83 mm{3.27 " } maximum                                                                                                                                                                                       |
| Size                          | Roll paper spool              | Inside: 12 mm{0.47 " }, Outside: 18 mm{0.71 " }                                                                                                                                                              |
| Size                          | Roll width when taken up      | 80 mmwidth paper printing: 80 + 0.5/-1.0mm 58 mmwidth paper printing: 58 + 0.5/-1.0mm                                                                                                                        |
| Size                          | Paper width                   | 80 mmwidth paper printing: 79.5 ± 0.5mm 58 mmwidth paper printing: 57.5 ± 0.5mm                                                                                                                              |
| Specified roll paper type     | Specified roll paper type     | NTP080-80/NTP058-80 In U.S.A.: Nakagawa Mfg. (USA) Inc. In Europe: Nakagawa Mfg. (Europe) GmbH In Southeast Asia: N.A.K. Mfg. (Malaysia) SDN BHD (Original paper: TF50KS-E Nippon Paper Industries Co., Ltd. |
| Specified original paper type | Specified original paper type | P300, P310, P350 (Kanzaki Specialty Papers) AF50KS-E (Jujo Thermal Oy) F5041 (Mitsubishi HiTec Paper Flensburg GmbH) KT55F20, KT48F20 (Koehler Paper Group)                                                  |

- Paper must not be pasted to the roll paper spool.
- The remaining amount of the roll paper when a roll paper near-end is detected differs depending on the spool type.

<!-- page 100 -->

## Electrical Characteristics

| Supply voltage                                           | Supply voltage   | DC 24V ± 7%                                                                                                                                                                                        |
|----------------------------------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Current consumption (at 24V, 25°C, normal print density) | Standby          | Mean: Approximately 0.015A Maximum 1A for drawer kick driving.                                                                                                                                     |
| Current consumption (at 24V, 25°C, normal print density) | Operating        | Mean: Approximately 1.8A Note: When print ratio is approximately 18% • Continuous printing for 50 lines (repeating 20H-7FH) ∗ Font A ∗ 42 columns ∗ ASCII character • 5 line feeding • Autocutting |

<!-- page 101 -->

## Environmental Conditions

<!-- image -->

| Temperature/ Humidity      | Operating                  | 5 to 45°C {41 to 113°F}, 10 to 90% RH (See the operating temperature and humidity range below.)                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature/ Humidity      | Storage (Factory packing)  | -10 to 50°C {14 to 122°F}, 10 to 90% RH (except for paper)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Acoustic noise (operating) | Acoustic noise (operating) | Approximately 55 dB (bystander position) Note: The values above are measured in the Epson evaluation condition. Acoustic noise differs depending on the paper used, printing contents, and the setting values, such as print speed or print Relative humidity Operating environment range 90 65 10 5 34 40 45 Ambient temperature [%RH] 34°C, 90% 40°C, 65% 45°C, 50% [°C] 31°C, 90% 34°C, 75% 45°C, 43% Specified original paper other than below Specified original paper: P300, P310, P350 |

<!-- page 102 -->

## External Dimensions and Mass

- Width: Approximately 145 mm {5.71"}
- Depth: Approximately 195 mm {7.68"}
- Height: Approximately 148 mm {5.83"}
- Mass: Approximately 1.6 kg {3.53 lb} (except for roll paper)

<!-- image -->

<!-- image -->

[Units: mm]

<!-- page 103 -->

## Option Specifications

| Electric characteristics   | Input conditions       | Input voltage (rating): 90 to 264VAC (100VAC -10% to 230VAC +15%)   |
|----------------------------|------------------------|---------------------------------------------------------------------|
| Electric characteristics   | Input conditions       | Frequency (rating): 50/60 Hz ± 3 Hz                                 |
| Electric characteristics   | Input conditions       | Input current (rating): 1.3A                                        |
| Electric characteristics   | Output conditions      | Output voltage (rating): 24VDC ± 5%                                 |
| Electric characteristics   | Output conditions      | Output current (rating): 2.1A                                       |
| Case specifications        | Dimensions (W × D × H) | 136 × 33 × 68 mm{5.35 × 1.30 × 2.68"} (excluding projections)       |
| Case specifications        | Weight                 | Approx. 0.4 kg {14.11 oz} (excluding the AC cable)                  |
| Case specifications        | Color                  | Black (matte)                                                       |

<!-- image -->

<!-- page 104 -->

## Specifications of Interfaces and Connectors

For detailed information about LAN or wireless LAN, see the Technical Reference Guide for the interface board.

## RS-232 Serial Interface

## Interface board specifications (RS-232-compliant)

| Item                                      | Item                                      | Specifications                                                                                                                                                            |
|-------------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data transfer method                      | Data transfer method                      | Serial                                                                                                                                                                    |
| Synchronization                           | Synchronization                           | Asynchronous                                                                                                                                                              |
| Handshake                                 | Handshake                                 | Select one of the following with DIP switch 1-3: • DTR/DSR • XON/XOFF                                                                                                     |
| Signal level                              | MARK                                      | -3V to -15V logic '1'/OFF                                                                                                                                                 |
| Signal level                              | SPACE                                     | +3V to +15V logic '0'/ON                                                                                                                                                  |
| Bit length                                | Bit length                                | Select one of the following with DIP switch 1-4: • 7 bit • 8 bit                                                                                                          |
| Transmission speed [bps: bits per second] | Transmission speed [bps: bits per second] | • Select one of the following with DIP switch 1-7/1-8: 4800/9600/19200/38400 bps • Select one of the following with commands: 2400/4800/9600/19200/38400/57600/115200 bps |
| Parity check                              | Parity check                              | Select one of the following with DIP switch 1-5: • Yes • No                                                                                                               |
| Parity selection                          | Parity selection                          | Select one of the following with DIP switch 1-6: • Even • Odd                                                                                                             |
| Stop bit                                  | Stop bit                                  | 1 or more bits However, the stop bit for data transfer from the printer is fixed to 1 bit.                                                                                |
| Connector                                 | Printer side                              | DSUB 25-pin (female) connector                                                                                                                                            |

<!-- page 105 -->

## Functions of each connector pin

|   Pin no. | Signal name   | Signal direction   | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         1 | FG            | -                  | Frame ground                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|         2 | TXD           | Output             | Transmission data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|         3 | RXD           | Input              | Reception data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|         4 | RTS           | Output             | Equivalent to DTR signal (pin 20)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|         6 | DSR           | Input              | This signal indicates whether the host computer can receive data. SPACE indicates that the host computer can receive data. MARK indicates that the host computer cannot receive data. When DTR/DSR control is selected, the printer transmits data after confirming this signal (except if transmitted using some ESC/POS commands). When XON/XOFF control is selected, the printer does not check this signal. Changing DIP switch 2-7 lets this signal be used as a printer reset signal. When you use this signal as the printer's reset signal, the printer is reset when the signal remains MARK for |
|         7 | SG            | -                  | Signal ground                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|        20 | DTR           | Output             | 1) When DTR/DSR control is selected, this signal indicates whether the printer is BUSY. • SPACE status Indicates that the printer is ready to receive data. • MARK status Indicates that the printer is BUSY. Set BUSY conditions with DIP switch 2-1. 2) When XON/XOFF control is selected, the signal indicates that the printer is properly connected and ready to receive data from the host. The signal is always SPACE, except in the following cases: • During the period from when power is turned on to when the printer is ready to receive data. • During the self-test.                       |
|        25 | INT           | Input              | Changing DIP switch 2-8 enables this signal to be used as a reset signal for the printer. The printer is reset if the signal remains at SPACE for a pulse width of 1 ms or more.                                                                                                                                                                                                                                                                                                                                                                                                                          |

<!-- page 106 -->

## XON/XOFF

When XON/XOFF control is selected, the printer transmits the XON or XOFF signals as follows. The transmission timing of XON/XOFF differs, depending on the setting of DIP switch 2-1.

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

The hexadecimal numbers corresponding to the XON/XOFF codes are shown below.

- XON code: 11H
- XOFF code: 13H
- When the printer goes from offline to online and the receive buffer is full, XON is not transmitted.
- When the printer goes from online to offline and the receive buffer is full, XOFF is not transmitted.
- When DIP switch 1-3 is off, XON is not transmitted as long as the printer is offline, even if a receive buffer full state has been cleared.

<!-- image -->

<!-- page 107 -->

## IEEE 1284 Parallel Interface

## Modes

The IEEE 1284 parallel interface supports the following two modes.

| Mode               | Communication direction      | Other information                                    |
|--------------------|------------------------------|------------------------------------------------------|
| Compatibility mode | Host → Printer communication | Centronics-compliant                                 |
| Reverse mode       | Printer → Host communication | Assumes a data transfer from an asynchronous printer |

## Compatibility Mode

Compatibility mode allows data transmission from host to printer only: Centronics-compatible.

## Specification

| Data transmission     | 8-bit parallel                                |
|-----------------------|-----------------------------------------------|
| Synchronization       | Externally supplied STROBE signals            |
| Handshaking           | ACK and BUSY signals                          |
| Signal levels         | TTL-compatible connector                      |
| Connector             | ADS-B36BLFDR176 (HONDA) or equivalent product |
| Reverse communication | Nibble or byte mode                           |

## Reverse Mode

The transfer of status data from the printer to the host proceeds in the nibble or byte mode.

This mode allows data transfer from an asynchronous printer under the control of the host. Data transfers in the nibble mode are made via the existing control lines in units of four bits (a nibble). In the byte mode, data transfer proceeds by making the 8-bit data lines bidirectional. Both modes fail to proceed concurrently in the compatibility mode, thereby causing half-duplex transmission.

<!-- page 108 -->

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

<!-- page 109 -->

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

## NC: Not Connected

## ND: Not Defined

<!-- image -->

- A signal name with a rule above it indicates an 'L' active signal.
- Bidirectional communications cannot take place, unless all signal names for both sides correspond to each other.
- Connect all signal lines using a twisted-pair cable. Connect the return side to the signal ground level.
- Make sure the signals satisfy electrical characteristics.
- Set the leading edge and trailing edge times to 0.5ms or less.
- Do not ignore Ack or BUSY signals during a data transfer. Ignoring such signals may result in data corruption.
- Make the interface cables as short as possible.

<!-- page 110 -->

## USB (Universal Serial Bus) Interface

## Outline

- Full-speed transmission at 12 Mbps [bps: bits per second]
- Plug &amp; Play, Hot Insertion &amp; Removal

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

In order to ensure that there is no lack of status data, it is necessary to periodically retrieve status data at the host computer.

Unlike RS 232C transmission, it cannot spontaneously interrupt data transmission to the host computer.

The printer has a 128-byte status data buffer. Statuses that exceed the buffer capacity are canceled.

<!-- page 111 -->

## Character Code Tables

Refer to the following URL regarding the character code table.

http://www.epson-biz.com/pos/reference/charcode/

<!-- page 112 -->
