# TM-T88II_TechnicalRefGuide


<!-- page 1 -->

## TM-T88II/T88III Technical reference guide

## English

405227700

<!-- page 2 -->



<!-- page 3 -->

## Cautions

- ❏ No part of this document may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, recabling, or otherwise, without the prior written permission of Seiko Epson Corporation.

- ❏ The contents of this document are subject to change without notice. Please contact us for the latest information.

- ❏ While every precaution has been taken in the preparation of this document, Seiko Epson Corporation assumes no responsibility for errors or omissions.

- ❏ Neither is any liability assumed for damages resulting from the use of the information contained herein.

- ❏ Neither Seiko Epson Corporation nor its affiliates shall be liable to the purchaser of this product or third parties for damages, losses, costs, or expenses incurred by the purchaser or third parties as a result of: accident, misuse, or abuse of this product or unauthorized modifications, repairs, or alterations to this product, or (excluding the U.S.) failure to strictly comply with Seiko Epson Corporation's operating and maintenance instructions.

- ❏ Seiko Epson Corporation shall not be liable against any damages or problems arising from the use of any options or any consumable products other than those designated as Original EPSON Products or EPSON Approved Products by Seiko Epson Corporation.

## Trademarks

EPSON  and ESC/POS  are registered trademarks of Seiko Epson Corporation.

## ESC/POS '  Command System

EPSON has been taking industry's initiatives with its own POS printer command system (ESC/POS). ESC/POS has a large number of commands including patented ones. Its high scalability enables users to build versatile POS systems. The system is compatible with all types of EPSON POS printers and displays. Moreover, its flexibility make it easy to upgrade in the future. The functionality and the user-friendliness is valued from around the world.

## Revision History

| Rev.   | Page      | Details of Change   |
|--------|-----------|---------------------|
| Rev. A | All pages | Newly authorized    |

<!-- page 4 -->

## For Safety

## Key to Symbols

The symbols in this manual are identified by their level of importance, as defined below. Read the following carefully before handling the product.

<!-- image -->

You must follow warnings carefully to avoid serious bodily injury.

<!-- image -->

## CAUTION:

Provides information that must be observed to prevent damage to the equipment or loss of data.

- ❏ Possibility of sustaining physical injuries.
- ❏ Possibility of causing physical damages.
- ❏ Possibility of causing information loss.

<!-- image -->

## Note:

Provides important information and useful tips on handling the equipment.

<!-- page 5 -->

## Warnings

<!-- image -->

- ❏ Shut down your equipment immediately if it produces smoke, a strange odor, or unusual noise. Continued use may lead to fire or electric shock. Immediately unplug the equipment.
- ❏ Only disassemble this product as described in this manual. Do not make modifications to the unit. Tampering with this product may result in injury, fire, or electric shock.
- ❏ To avoid risk of electric shock, do not set up this product or handle cables during a thunderstorm in order.
- ❏ Be sure to use the specified power source. Connection to an improper power source may cause fire or shock.
- ❏ Never insert or disconnect the power plug with wet hands. Doing so may result in severe shock.
- ❏ Do not allow foreign matter to fall into the equipment. Penetration by foreign objects may lead to fire or electric shock.
- ❏ If water or other liquid spills into this equipment, turn off the power supply switch and unplug the power cable immediately. Continued usage may lead to fire or electric shock.
- ❏ Do not place multiple loads on power outlet. Overloading the outlet may lead to fire. Always supply power directly from a standard 100 VAC domestic power outlet.
- ❏ Handle the power cable with care. Improper handling may lead to fire or electric shock.
- Do not modify or attempt to repair the cable.
- Do not place any heavy object on top of the cable.
- Avoid excessive bending, twisting and pulling.
- Do not place the cable near heating equipment.
- Check that the plug is clean before plugging it in.
- Be sure to push the plug all the way in.

## Cautions

<!-- image -->

- ❏ Be sure to set this equipment on a firm, stable horizontal surface. Product may break or cause injury if it falls.
- ❏ Do not use in locations subject to high humidity or dust levels. Excessive humidity and dust may cause equipment damage, fire or shock.

<!-- page 6 -->

- ❏ Do not place heavy objects on top of this equipment. Never stand or lean on this equipment. Equipment may fall or collapse, causing breakage and possible injury.
- ❏ To ensure safety, unplug this equipment prior to leaving it unused for an extended period.
- ❏ Parts on the circuit board may become hot during operation. Wait approximately 10 minutes after turning the power off before touching them.
- ❏ To avoid injury, take care not to insert fingers or any part of the hand in the roll paper opening where the manual cutter is installed.
- ❏ Do not open the roll paper cover without taking the necessary precautions, as this can result in injury from the autocutter fixed blade.
- ❏ A needle for supplying ink to the printer is located inside the ink cartridge holder. Inserting your fingers inside the ink cartridge holder may cause an injury.

## Modular Connectors

The printer uses the modular connectors specifically designed for the cash drawer or customer display. Do not connect these connectors to an ordinary telephone line.

<!-- page 7 -->

## About this Manual

This manual describes the TM-T88III, a current EPSON thermal printer product.

This manual also describes the TM-T88II, an obsolete product, for the purpose of supporting legacy systems. The TM-T88II has been replaced by the newer TM-T88III. However, even though the TM-T88II is no longer being sold, it is still in use by customers.

In addition, the power supply that was originally available for the TM-T88II printer, the PS-170, is obsolete and no longer available. It is described only for legacy support. The currently available power supply, the PS-180, works with either printer model.

## Aim of the Manual

This manual was created to provide all the information necessary for system planning, design, installation, and application of the printer for designers and developers of POS system.

## Manual Content

| The manual is made up of the following sections:   | The manual is made up of the following sections:   |
|----------------------------------------------------|----------------------------------------------------|
| Chapter 1                                          | Product Overview                                   |
| Chapter 2                                          | Setup                                              |
| Chapter 3                                          | Application Development Information                |
| Chapter 4                                          | ESC/POS Command-related Information                |
| Chapter 5                                          | Product Specifications                             |
| Appendix A                                         | Interfaces and Connectors                          |
| Appendix B                                         | Options and Consumables                            |
| Appendix C                                         | Character Code Tables                              |
| Appendix D                                         | TM-T88II/TM-88III Comparison Table                 |

## Related Software and Documents

Documents relating to the TM-T88II/TM-T88III are listed below.

| Name of document                               | Description                                                                                                                                          |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| TM-T88II User's Manual TM-T88III User's Manual | Provides information to enable POS operators to use the TM-T88II/TM-T88III safely and correctly. This manual is packed in the box with the printer.* |
| ESC/POS Application Programming Guide          | Provides detailed ESC/POS command information. Contact us to obtain this guide.                                                                      |
| TM-T88II/T88III Technical Reference Guide      | This guide.*                                                                                                                                         |
| EPSON OPOS ADK                                 | This is an OCX driver.*                                                                                                                              |

<!-- page 8 -->

| Name of document                     | Description                                                                                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| EPSON OPOS ADK Manual                | Provides information for anyone who is programming using OPOS. This is included in the EPSON OPOS ADK.*                                                   |
| EPSON Advanced Printer Driver        | This is a Windows driver.*                                                                                                                                |
| EPSON Advanced Printer Driver Manual | Provides information for anyone who is programming using the APD (EPSON Advanced Printer Driver). This is included in the EPSON Advanced Printer Driver.* |

For customers from North America: http://pos.epson.com/

For customers from other countries: http://epson-pos.com/

Select the product from the 'Select any product' pull-down menu.

<!-- page 9 -->

## Contents

| Revision History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                    | . i     |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| For Safety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                              | . ii    |
| . . . . . . . . Key to Symbols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                            | . ii    |
| Warnings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                      | . iii   |
| Cautions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | . iii   |
| . . . . . Modular Connectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              | . iv    |
| About this Manual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                         | . v     |
| . . Aim of the Manual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                         | . v     |
| Manual Content . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                        | . v     |
| . . . . . . . . . . . . . . Related Software and Documents . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              | . v     |
| Chapter 1 Product Overview                                                                                                                      |         |
| Product Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                   | . 1-1   |
| Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                   | . 1-1   |
| Accessories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                       | . 1-1   |
| Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     | . 1-1   |
| Consumable products . . . . . . . . . . . . . . . . . . . . . . . .                                                                             | . 1-1   |
| . . . . . . . . . . . . . . TM-T88II/TM-88III Comparison Table . . . . . . . . . . . . . . . . . . . . . . .                                    | . 1-2   |
| Part Names and Basic Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                  | . 1-3   |
| Part Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          | . 1-3   |
| . Control Panel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                       | . 1-3   |
| Power Switch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          | . 1-4   |
| Connectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                        | 1-5     |
| Handling the Printer . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                        | . . 1-5 |
| . . . . . . . . . . . . . . . . . Installing and Replacing Roll Paper . . . . . . . . . . . . . . . . . . . . . . . . . .                       | . 1-6   |
| Power Switch Cover . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | . 1-7   |
| Shipping Procedures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                               | . 1-8   |
| Chapter 2 Setup                                                                                                                                 |         |
| Installing the Printer . . . . . . . . . . . . . . . . . . . . . . . .                                                                          | . 2-2   |
| . . . . . . . . . . . . . . . . . . . Precautions for Horizontal Installation . . . . . . . . . . . . . . . . . . . . . . .                     | . 2-2   |
| Precautions for Wall Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                     | . 2-2   |
| Setting the DIP Switches                                                                                                                        | . 2-2   |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DIP Switch Positions and Steps for Changing DIP Switch Settings | . 2-2   |
| DIP Switch Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | . 2-3   |
| Adjusting the Roll Paper Near-End Detector . . . . . . . . . . . . . . . . . . . . . .                                                          | . 2-7   |
| Connecting the Printer to the Host Computer . . . . . . . . . . . . . . . . . . . . .                                                           | . 2-8   |
| Serial Interface Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                   | . 2-8   |
| Parallel Interface Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                   | . 2-11  |
| USB Interface Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                      | . 2-11  |
| . . Ethernet Interface Connection . . . . . . . . . . . . . . . . .                                                                             | . 2-13  |
| . . . . . . . . . . . . . . Connecting Power Supply Unit and Cash Drawer . . . . . . . . . . . . . . . . . .                                    | . 2-15  |
| Connecting the Power Supply Unit . . . . . . . . . . . . . . . . . . . . . . . . . .                                                            | . 2-15  |
| Connecting the Drawer Kick-out Cable . . . . . . . . . . . . . . . . . . . . . . .                                                              | . 2-16  |
| Installing the Driver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     | . 2-16  |
| Chapter 3 Application Development Information                                                                                                   |         |
| Introducing the Control Methods . . . . . . . . . . . .                                                                                         | 3-1     |
| . . . . . . . . . . . . . . . . . . . . Windows Driver (EPSON Advanced Printer Driver) . . . . . . . . . . .                                    | . . 3-1 |
| EPSON OPOSADK . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                   | . 3-3   |

<!-- page 10 -->

| ESC/POS Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                            | . . 3-5   |
|---------------------------------------------------------------------------------------------------------|-----------|
| Various Utilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | . . 3-6   |
| Switches and Buttons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . . 3-6   |
| . . Paper FEED Button . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                       | . . 3-6   |
| . . Panel LEDs and Error Status . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | . . 3-7   |
| Power LED . . . . . . . . . . . . . . . . . . . . .                                                     | . 3-7     |
| . . . . . . . . . . . . . . . . . . No Roll Paper (PAPER OUT) LED . . . . . . . . . . . . . . . . . . . | . . . 3-7 |
| Error LED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . . 3-7   |
| Sensors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . . 3-10  |
| Paper Sensors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | . . 3-10  |
| . . . . . Printer Cover Sensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . . 3-10  |
| Offline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . . 3-11  |
| . Busy State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . . 3-11  |
| NVRAM(Non-volatile Memory) . . . . . . . . . . . . . . . . . . . . . . . . .                            | . . 3-12  |
| Bar Code Printing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . . 3-12  |
| Operating Mode (Switch Panel Operation) . . . . . . . . . . . . . . . .                                 | . . 3-13  |
| Self-test Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | . . 3-13  |
| FAQ List . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    | . . 3-14  |
| Q: Why has my print data dropped out? . . . . . . . . . . . . . .                                       | . . 3-14  |
| Q: Why does the drawer kick-out not operate properly?                                                   | . . 3-15  |
| Q: I cannot print part of Page 0 in Visual Basic. Why? . . .                                            | . . 3-15  |
| Chapter 4 ESC/POS Command-related Information                                                           |           |
| NVMemory (Non-volatile Memory) . . . . . . . . . . . . . . . . . . . . .                                | . . 4-1   |
| Using NVMemory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        | . . 4-1   |
| Printer Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . 4-2   |
| Precautions When the Printer Is Offline . . . . . . . . . . . . . . . . . . .                           | . . 4-2   |
| Outputting Hex Dumps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . . 4-2   |
| Chapter 5 Product Specifications                                                                        |           |
| Product Specifications (TM-T88II/TM-T88III) . . . . . . . . . . . . . .                                 | . . 5-1   |
| Print Specifications (TM-T88II/TM-T88III) . . . . . . . . . . . . . . . .                               | . . 5-2   |
| Character Specifications (TM-T88II/TM-T88III) . . . . . . . . . . .                                     | . . 5-3   |
| Paper Specifications (TM-T88II/TM-T88III) . . . . . . . . . . . . . . .                                 | . . 5-3   |
| Printable Area (TM-T88II/TM-T88III) . . . . . . . . . . . . . . . . . . . .                             | . . 5-4   |
| Print Position versus Cutter Position (TM-88II/TM88III) . . .                                           | . . 5-5   |
| . Overview of External Dimensions (TM-T88II/TM-T88III) . . .                                            | . . 5-6   |
| External Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                       | . . 5-6   |
| Operating Specifications (TM-T88II/TM-T88III) . . . . . . . . . . . .                                   | . . 5-7   |
| Appendix A Interfaces and Connectors                                                                    |           |
| RS-232 Serial Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . . A-1   |
| Interface Board Specifications (RS-232-compliant) . . . . . .                                           | . . A-1   |
| Functions of each Connector Pin . . . . . . . . . . . . . . . . . . . . .                               | . . A-2   |
| XON/XOFF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . . A-2   |
| Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . A-3   |
| IEEE 1284 Parallel Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . . A-3   |
| Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                         | . . A-3   |
| . . . . . . . Interface Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . . A-5   |
| Appendix B Options and Consumables                                                                      |           |
| Roll Paper . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . B-1   |
| Power Supply . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . B-1   |
| PS-170 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . B-1   |
| PS-180 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . B-2   |

<!-- page 11 -->

## Appendix C Character Code Tables

| Page 0 (PC437: USA, Standard Europe) . . . . .                            | . C-1   |
|---------------------------------------------------------------------------|---------|
| Page 1 (Katakana) . . . . . . . . . . . . . . . . . . . . . . . .         | . C-2   |
| Page 2 (PC850: Multilingual) . . . . . . . . . . . . . . .                | . C-3   |
| Page 3 (PC860: Portuguese) . . . . . . . . . . . . . . . .                | . C-4   |
| Page 4 (PC863: Canadian-French) . . . . . . . . . . .                     | . C-5   |
| Page 5 (PC865: Nordic) . . . . . . . . . . . . . . . . . . . .            | . C-6   |
| Page 16 (WPC1252) (TM-T88III only) . . . . . . . .                        | . C-7   |
| Page 17 (PC866: Cyrillic #2) (TM-T88III only) .                           | . C-8   |
| Page 18 (PC852: Latin2) (TM-T88III only) . . . .                          | . C-9   |
| Page 19 (PC858: Euro) . . . . . . . . . . . . . . . . . . . . .           | . C-10  |
| Page 255 (Blank Page) . . . . . . . . . . . . . . .                       | . C-11  |
| . . . . . . International Character Set . . . . . . . . . . . . . . . . . | . C-12  |

Appendix D TM-T88II/TM-88III Comparison Table

<!-- page 12 -->



<!-- page 13 -->

## Product Overview

The TM-T88III thermal printer product is currently available from EPSON. The TM-T88II is an obsolete product, which is described here for the purpose of supporting legacy systems. In addition, the PS-170, the power supply for the TM-T88II printer, also is obsolete and no longer available. It is described only for legacy support. The currently available power supply, the PS-180, works with either printer model.

## 1.1  Product Structure

## 1.1.1  Model

- ❏ Product Name TM-T88III (current product)/TM-T88II (legacy product)
- Print method:

Thermal line printing

- Interface specifications: Serial interface specifications (RS-232C) Parallel interface specifications (IEEE 1284-compliant) USB interface specifications Ethernet interface specifications
- ·
- Paper width specifications: 80 mm {3.15"} width specifications 58 mm {2.28"} width specifications

## 1.1.2  Accessories

- ❏ Printer (body)
- ❏ Roll paper (outer diameter 50 mm {2"}) × 1
- ❏ User's manual × 1
- ❏ Power switch cover × 1
- ❏ External power supply unit model: PS-180 (TM-T88III: packaged power supply)
- ❏ Power cable model: AC-170 for PS-170. (The PS-170 and TM-T88II are no longer being sold.)

## 1.1.3  Options

- ❏ External power supply unit
- Model PS-170 (This option has been replaced by the PS-180, which works for both printers.)
- Model PS-180 (*1) (PS-180 supports the power-saving feature.)

<!-- page 14 -->

- ❏ Power cable (model: AC-170) (*1)
- (*1) The power supply unit and power cable may not come packaged with the TM-T88III. Purchase these separately, if necessary. (The PS-170 power supply has been replaced by the PS-180 and is no longer being sold.)

## 1.1.4  Consumable products

- ❏ Specified paper: Thermal paper

## 1.1.5  TM-T88II/TM-88III Comparison Table

Table 1-1  Differences between the TM-T88II and TM-T88III

|                                                         | TM-T88III (current model)                                                                                                                                                                                                                                                                                                                                                 | TM-T88II (legacy model)          |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1. High-speed print mode                                | Approx. 150 mm/s (4.72") maximum                                                                                                                                                                                                                                                                                                                                          | Approx. 120 mm/s (4.72") maximum |
| 2. High-speed power consumption mode                    | Average approx. 1.8 A                                                                                                                                                                                                                                                                                                                                                     | Average approx. 1.7 A            |
| 3. Serial interface selectable baud rates               | 4800, 9600, 19200, 38400, (2400 discontinued, 38400 added). 38400 is selected by setting DIP SW1-7 and 1-8 to ON. (See 'DIP Switch Functions' (page 2-3).)                                                                                                                                                                                                                | 2400, 4800, 9600, 19200          |
| 4. Conditions for canceling receive buffer BUSY state * | Set with DIP SW2-5 *                                                                                                                                                                                                                                                                                                                                                      | Cannot be changed.               |
| 5. Supported character sets (extended graphics)         | 11 pages including WPC 1252, PC866 [Cyrillic #2], PC852 [Latin2])                                                                                                                                                                                                                                                                                                         | 8 pages                          |
| 6. Driver (EPSON OPOS ADK, Advanced Printer Driver)     | Also can be operated by the driver for the TM-T88II. Functions, however, are restricted as follows: • Some baud rates cannot be used in serial communications (38400 bps, 2400 bps). Note: The driver cannot set a 38400 bps baud rate. Selecting a 2400 bps baud rate with the driver will cause garbled characters (the printer does not support a 2400 bps baud rate). | -                                |

* For details on the conditions for canceling the receive buffer BUSY state, refer to 'DIP Switch Functions' (page 2-3).

<!-- page 15 -->

## 1.2  Part Names and Basic Operation

## 1.2.1  Part Names

Figure 1-1 Printer part names

<!-- image -->

* For details on DIP switch settings, refer to 'DIP Switch Positions and Steps for Changing DIP Switch Settings' (page 2-2).

## 1.2.2  Control Panel

Figure 1-2 Control panels for the TM-T88II (legacy model) and TM-T88III (current model)

<!-- image -->

<!-- page 16 -->

## 1.2.2.1  LED

## POWER LED (green)

- ❏ Lights when the power supply is on.
- ❏ Goes out when the power supply is turned off.

## ERROR LED

Lights or flashes when the printer is offline.

- Lights after the power is turned on or after a reset (offline). Automatically goes out after a
- ❏ while to indicate that the printer is ready.

Lights when the end of the roll paper is detected, and when printing has stopped (offline). If this happens, replace with new roll paper.

- ❏ Flashes when an error occurs. (For details about the flash codes, refer to 'Error Codes' (page 3-8).)
- ❏ Goes out during regular operation (online).

## PAPER OUT LED

- ❏ Lights when there is no more roll paper or there is little remaining.
- ❏ Goes out when there is a sufficient amount of roll paper remaining.
- ❏ Flashes when a self-test is in progress or when the printer waits for a macro execution.

## 1.2.2.2  Buttons

## PAPER FEED button

Pressing this button once feeds the roll paper by one line. Holding this button down feeds the roll paper continuously.

## 1.2.3  Power Switch

The power switch is located at the bottom right front of the printer. (Refer to 'Printer part names' (page 1-3).)

Turn the printer on or off. The marks on the switch (0 = on / 1 = off) indicate the printer switch position.

## CAUTION:

Before turning on the printer be sure to check that the AC adapter is connected to the power supply.

<!-- page 17 -->

## 1.2.4  Connectors

All cables are connected to the connector panel on the lower rear of the printer.

Figure 1-3 Connector panel

<!-- image -->

- ❏ Drawer kick-out connector for connecting the cash drawer
- ❏ Power supply connector for connecting the power supply unit
- ❏ Interface connector to connect the printer to the host computer interface (serial, parallel, etc.)

<!-- image -->

## Note:

The picture above shows a serial interface model. For details on the various interfaces and how to connect the power supply connector and cash drawer, see 'Connecting Power Supply Unit and Cash Drawer' (page 2-15) and 'Connecting the Printer to the Host Computer' (page 2-8).

## 1.3  Handling the Printer

<!-- image -->

Do not open the printer cover during printing. Doing so may damage the printer.

Do not touch the manual cutter with your hands when installing or replacing roll paper. The manual cutter is sharp and may cause an injury.

## 1.3.1  Selecting Paper Width

The customer can select either 58 mm {2.28"} or 80 mm {3.15"} paper. This option is performed at the factory by installation of a spacer, as shown below.

Figure 1-4 Paper spacer

<!-- image -->

<!-- page 18 -->

## 1.3.2  Installing and Replacing Roll Paper

<!-- image -->

## Note:

Be sure to use roll paper that meets printer specifications. See Appendix B for details on the paper specifications.

Do not use roll paper whose trailing end is glued to the roll paper core.

## 1.3.2.1  Installing Roll Paper

1. Make sure the host has not sent a printing command to the printer, and press the cover open button to open the printer cover. If the printer cover does not open, a probable cause is that the autocutter is locked. If this happens, refer to 'Paper jam.'
2. Load the roll paper.

Figure 1-5 Cover open button

<!-- image -->

Figure 1-6 Loading paper

<!-- image -->

<!-- image -->

When loading the roll paper, pay attention to the direction that the roll paper is fed out of the printer.

Figure 1-7 Paper direction

<!-- image -->

<!-- page 19 -->

3. Pull out the roll paper toward you.
4. Close the printer cover.
5. Tear off the leading edge of the roll paper using the manual cutter.

Figure 1-8 Closing the printer cover

<!-- image -->

Figure 1-9 Tear off paper

<!-- image -->

## 1.3.2.2  Replacing Paper

Follow the procedure below to replace roll paper.

1. Open the printer cover, and remove the core of the previously used roll paper.
2. Insert the new roll paper following the procedure in 'Installing Roll Paper' (page 1-6).

## 1.3.3  Power Switch Cover

Install the power switch cover that comes with the TM-T88II/TM-T88III onto the printer to prevent inadvertent changing of the power switch, to prevent tampering, and to improve the appearance of the printer.

To reset the TM printer when the power switch cover is installed, insert a long, thin object (such as the end of a paper clip) into the hole in the power switch cover and press the power switch.

<!-- page 20 -->

## 1.3.4  Shipping Procedures

Do the following before shipping the printer.

1. Press the power switch to turn the power off.
2. Make sure the POWER LED is out.
3. Remove the power supply connector.
4. Pack the printer, keeping the top and bottom correctly oriented.

<!-- page 21 -->

## Setup

Before using the printer, you need to make various settings to increase the printer's functionality. Configure the printer appropriately depending on the environment.

Figure 2-1  Setup flowchart

<!-- image -->

<!-- page 22 -->

## 2.1  Installing the Printer

In addition to regular horizontal installation, the printer can be hung on a wall using the optional WH-10 Wall Hanging Bracket Set.

## 2.1.1  Precautions for Horizontal Installation

- ❏ Install the printer in a flat, horizontal position.
- ❏ Avoid locations susceptible to dust and other foreign matter.
- ❏ Be sure to avoid bumping so that the printer is not exposed to strong impact during operation.
- ❏ Avoid placing the printer on top of the power supply or other cables or other objects.

## 2.1.2  Precautions for Wall Installation

- ❏ Make the following settings on the printer when you hang it on a wall. For details, refer to the installation manual provided with the optional WH-10 Wall Hanging Bracket Set.
- Install the roll paper stopper
- Adjust of near-end detector
- Install the WH-10
- ❏ For other details, refer to the installation manual provided with the optional WH-10 Wall Hanging Bracket Set option.

## 2.2  Setting the DIP Switches

On this printer, you can make various settings with DIP switches.

<!-- image -->

Serial interface communication conditions must be set on serial interface model printers.

## 2.2.1  DIP Switch Positions and Steps for Changing DIP Switch Settings

Follow the steps below to change the DIP switch settings.

## CAUTION:

Before you remove the DIP switch cover, turn the printer off. Otherwise, a short-circuit may cause the printer to malfunction.

1. Make sure the power supply for the printer is turned off.

<!-- page 23 -->

2. Unscrew the screw to remove the DIP switch cover from the base of the printer.
3. Set the DIP switches as desired, using the tip of a tool, such as a small screwdriver.
4. Attach the DIP switch cover, and screw in place.

Figure 2-2  Removing the DIP switch cover

<!-- image -->

<!-- image -->

New DIP switch settings are enabled after the printer is turned on.

## 2.2.2  DIP Switch Functions

The DIP switch functions depend on your printer's interface specifications.

## 2.2.2.1  DIP switch settings for serial interface specifications

Note that the functions of DIP SW1-7, 1-8, and 2-5 differ on the TM-T88II and TM-88III. (The functions of other DIP switch settings are the same.)

<!-- image -->

Table 2-1  Switch bank 1 settings

| SW       | Function                                                                                                                         | ON                                                                                                                               | OFF                                                                                                                              |
|----------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 1-1      | Data receive error                                                                                                               | Ignore                                                                                                                           | ' ? ' is printed *                                                                                                               |
| 1-2      | Receive buffer size                                                                                                              | 45 bytes                                                                                                                         | 4KB *                                                                                                                            |
| 1-3      | Handshake                                                                                                                        | XON/XOFF                                                                                                                         | DTR/DSR *                                                                                                                        |
| 1-4      | Bit length                                                                                                                       | 7 bits                                                                                                                           | 8 bits *                                                                                                                         |
| 1-5      | Parity check                                                                                                                     | Yes                                                                                                                              | No *                                                                                                                             |
| 1-6      | Parity selection                                                                                                                 | Even                                                                                                                             | Odd *                                                                                                                            |
| 1-7, 1-8 | Baud rate selection (See the 'Baud rate selection' tables below. (Note that the settings differ on the TM-T88II and TM-T88III.)) | Baud rate selection (See the 'Baud rate selection' tables below. (Note that the settings differ on the TM-T88II and TM-T88III.)) | Baud rate selection (See the 'Baud rate selection' tables below. (Note that the settings differ on the TM-T88II and TM-T88III.)) |

For details on DIP SW1-2: Receive buffer size, also refer to DIP SW2-5: Cancellation of receive buffer full BUSY state.

<!-- page 24 -->

Table 2-2  Baud rate selection (DIP SW1-7, 1-8)

TM-T88II

| Baud rate (BPS)   | Switch no.   | Switch no.   |
|-------------------|--------------|--------------|
| Baud rate (BPS)   | 1-7          | 1-8          |
| 2400              | ON           | ON           |
| 4800              | OFF          | ON           |
| 9600 *            | ON           | OFF          |
| 19200             | OFF          | OFF          |

Table 2-3  Switch bank 2 settings

| SW       | Function                                           | ON                    | OFF                                      |
|----------|----------------------------------------------------|-----------------------|------------------------------------------|
| 2-1      | Handshake (BUSY) conditions                        | Receive buffer full   | Printer offline or receive buffer full * |
| 2-2      | Reserved (do not change setting)                   | Fixed to OFF          | Fixed to OFF                             |
| 2-3, 2-4 | Print density selection/low-power mode             | (See separate table.) | (See separate table.)                    |
| 2-5      | Conditions for canceling receive buffer BUSY state | (See separate table.) | (See separate table.)                    |
| 2-6      | Reserved (do not change setting)                   | Fixed to OFF          | Fixed to OFF                             |
| 2-7      | Pin # 6 reset signal                               | Used                  | Not used *                               |
| 2-8      | Pin # 25 reset signal                              | Used                  | Not used *                               |

For details on DIP SW2-1: BUSY conditions, also refer to 'Busy State' (page 3-11).

Table 2-4  Print density selection (DIP SW2-3, 2-4)

|       |                         | Switch No.   | Switch No.   |
|-------|-------------------------|--------------|--------------|
| Level | Print density           | 2-3          | 2-4          |
| -     | Low-power mode          | ON           | ON           |
| 1     | Regular print density * | OFF          | OFF          |
| 2     | ↔                       | ON           | OFF          |
| 3     | Heavy print density     | OFF          | ON           |

Table 2-5  Conditions for canceling receive buffer BUSY state (DIP SW2-5)

TM-T88II

| Conditions to cancel receive buffer BUSY state                     | Switch No. 2-5   |
|--------------------------------------------------------------------|------------------|
| BUSY state canceled when 26 bytes or more remain in receive buffer | Fixed to OFF     |

TM-T88III

| Conditions to cancel receive buffer BUSY state (enabled only when DIP SW1-2 is OFF)   | Switch No.   |
|---------------------------------------------------------------------------------------|--------------|
| Conditions to cancel receive buffer BUSY state (enabled only when DIP SW1-2 is OFF)   | 2-5          |
| BUSY state canceled when 138 bytes remain in receive buffer                           | ON           |
| BUSY state canceled when 256 bytes * remain in receive buffer                         | OFF          |

TM-T88III

| Baud rate (BPS)   | Switch no.   | Switch no.   |
|-------------------|--------------|--------------|
|                   | 1-7          | 1-8          |
| 38400             | ON           | ON           |
| 4800              | OFF          | ON           |
| 9600 *            | ON           | OFF          |
| 19200             | OFF          | OFF          |

<!-- page 25 -->

<!-- image -->

## Note:

With the TM-T88III, the DIP SW2-5 setting is enabled only when DIP SW1-2 is set to OFF and the receive buffer is set to 4KB.

With the older TM-T88II model, be sure to set DIP SW2-5 to OFF before use. Otherwise, the printer may no longer function correctly.

When the TM-T88II is used or when the TM-T88III is used with DIP SW1-2 set to ON, the BUSY state is canceled when '26 bytes remaining in receive buffer' are reached, regardless of DIP SW2-5 setting.

Do not change the settings of DIP SW2-2 and SW2-6. Otherwise, the printer may no longer function correctly.

## 2.2.2.2  DIP switch settings for other interface specifications

The following DIP switch functions are for parallel interface/USB/Ethernet model printers.

<!-- image -->

Table 2-6  Parallel/USB/Ethernet DIP switch bank 1

| SW       | Function                                                         | ON                   | OFF                     |
|----------|------------------------------------------------------------------|----------------------|-------------------------|
| 1-1      | Automatic line feed                                              | Enabled at all times | Disabled at all times * |
| 1-2      | Receive buffer size                                              | 45 bytes             | 4KB *                   |
| 1-3, 1-8 | Not defined (Always use printer with these switches set to OFF.) | -                    | -*                      |

Table 2-7  Parallel/USB/Ethernet DIP switch bank 2

| SW       | Function                                           | ON                    | OFF                               |
|----------|----------------------------------------------------|-----------------------|-----------------------------------|
| 2-1      | Handshake (BUSY conditions)                        | • Receive buffer full | • Offline * • Receive buffer full |
| 2-2      | Reserved (do not change setting)                   | Fixed to OFF          |                                   |
| 2-3, 2-4 | Print density selection/low-power mode             | (See separate table.) |                                   |
| 2-5      | Conditions for canceling receive buffer BUSY state | (See separate table.) |                                   |
| 2-6, 2-7 | Reserved (do not change setting)                   | Fixed to OFF          |                                   |
| 2-8      | Pin #31reset signal (do not change setting)        | Fixed to ON           |                                   |

DIP SW2-1: For details on the BUSY condition, also refer to 'Busy State' (page 3-11).

<!-- page 26 -->

Table 2-8  Selection of print density

|       |                         | Switch no.   | Switch no.   |
|-------|-------------------------|--------------|--------------|
| Level | Print density           | 2-3          | 2-4          |
| 1     | Low-power mode          | ON           | ON           |
| 2     | Regular print density * | OFF          | OFF          |
| 3     | ↔                       | ON           | OFF          |
| 4     | Heavy print density     | OFF          | ON           |

Table 2-9  Conditions for canceling receive buffer BUSY state

TM-T88II

Conditions to cancel receive buffer BUSY

state

BUSY state canceled when 26 bytes or

more remain in receive buffer

<!-- image -->

## Note:

With the TM-T88III, the DIP SW2-5 setting is enabled only when DIP SW1-2 is set to OFF and the receive buffer is set to 4KB.

With the TM-T88II, be sure to set DIP SW2-5 to OFF before use. Otherwise, the printer may no longer function correctly.

When the TM-T88II is used or when TM-T88III is used with DIP SW1-2 set to ON, the BUSY state is canceled when '26 bytes remaining in receive buffer' are reached regardless of the setting of DIP SW2-5.

Do not change the settings of DIP SW2-2 and SW2-6. Otherwise, the printer may no longer function correctly.

Switch no.

2-5

Fixed to

OFF

TM-T88III

| Conditions to cancel receive buffer BUSY state (enabled only when DIP SW1-2 OFF)   | Switch no.   |
|------------------------------------------------------------------------------------|--------------|
| Conditions to cancel receive buffer BUSY state (enabled only when DIP SW1-2 OFF)   | 2-5          |
| BUSY state canceled when 138 bytes remain                                          | ON           |
| BUSY state canceled when 256 bytes remain *                                        | OFF          |

<!-- page 27 -->

## 2.3  Adjusting the Roll Paper Near-End Detector

Below are two situations where a roll paper NE detector adjustment is required.

- ❏ To adjust the detection position to suit the diameter of the roll paper core used.
- ❏ To adjust the detection position of remaining amount of paper.

<!-- image -->

Note:

Since roll paper cores vary slightly in shape, depending on paper roll design and manufacturing tolerances, it impossible to detect the remaining paper exactly. Use roll paper with a core inner diameter of 12 mm {0.47"} and outer diameter of 18 mm {0.71"} so that the NE detector can detect the remaining paper as accurately as possible.

Follow the procedure below to adjust the roll paper NE detector position.

1. Open the roll paper cover, and remove the roll paper.
2. Loosen the adjustment screw fastening the detector, and align the upper edge of the positioning plate with the adjustment position. Adjustment positions are as follows:

| Adjustment position   | Remaining amount of roll paper (outer diameter: mm)   |
|-----------------------|-------------------------------------------------------|
| Upper                 | Approx. 27                                            |
| Lower                 | Approx. 23                                            |

<!-- image -->

Figure 2-3  NE detector positions

<!-- image -->

The adjustment screw is set to the lower position before shipment.

3. Tighten the adjustment screw.
4. After adjustment, make sure that the detection lever operates smoothly.
5. Load the roll paper.
6. Close the roll paper cover.

<!-- page 28 -->

## 2.4  Connecting the Printer to the Host Computer

## 2.4.1  Serial Interface Connection

## 2.4.1.1  Cross cable wiring diagrams

The wiring selections for available serial cross cables are as follows:

Figure 2-4  Cross cable diagrams

The cable needed depends on printer control and handshake method. You can operate the TM printer with a Windows driver, OPOS, or ESC/POS commands. XON/XOFF, DTR/DSR, or RTS/CTS are available as handshake controls. For details on available cables for each connection form, refer to 'Section 2.4.1.2, Serial interface connection diagrams.'

## 2.4.1.2  Serial interface connection diagrams

When the TM printer is connected to a host computer by the serial interface, the following two connection forms are possible:

- Stand alone
- Pass-through connection

<!-- page 29 -->

## Stand alone

Both the TM printer and DM-D are connected to the host computer directly via the serial port.

| Application control TM side control setting   |   Application control TM side control setting | XON/XOFF (except OPOS)                 | DTR/DSR (DOS, OPOS, Visual C)   | RTS/CTS (DOS, Windows driver, Visual C, Visual Basic MSComm)   |
|-----------------------------------------------|-----------------------------------------------|----------------------------------------|---------------------------------|----------------------------------------------------------------|
| XON/XOFF                                      |                                             1 | Type A or B                            | -                               | -                                                              |
|                                               |                                             2 | DM-D500: A, B Other DM-D: not possible | -                               | -                                                              |
| DTR/DSR                                       |                                             1 | -                                      | Type A or B                     | Type B                                                         |
|                                               |                                             2 | -                                      | Type A or B                     | Type B                                                         |

Figure 2-5  Configuration of stand-alone connection

<!-- image -->

## Pass-through connection

The host computer is connected to the TM printer over the serial interface via DM-D.

| Application control TM side control setting   | Application control TM side control setting   | XON/XOFF (except OPOS)   | DTR/DSR (DOS, OPOS, Visual C)   | RTS/CTS (DOS, Windows driver, Visual C, Visual Basic MSComm)   |
|-----------------------------------------------|-----------------------------------------------|--------------------------|---------------------------------|----------------------------------------------------------------|
| XON/XOFF                                      | XON/XOFF                                      | Not possible             | -                               | -                                                              |
| DTR/DSR                                       | 1                                             | -                        | Type A or B                     | Type B                                                         |
|                                               | 2                                             | -                        | Type A or B                     | Type A or B                                                    |

Figure 2-6  Configuration of pass-though connection

<!-- image -->

<!-- page 30 -->

## 2.4.1.3  Connecting the serial interface (RS-232) cable

<!-- image -->

Be sure to turn off the power supply for both the printer and host computer before connecting the cables.

1. Insert the interface cable connector firmly into the interface connector on the connector panel.
2. When using connectors equipped with screws, tighten them to secure the connectors firmly.

<!-- image -->

Figure 2-7  Tighten screws

<!-- image -->

The printer comes with hex-head screws with inch-threaded holes installed. When using an interface cable with metric-thread screws, use a hexagonal screwdriver (5 mm) to replace the installed screws with hex-head screws with metric-threaded holes, also supplied.

Figure 2-8  Hex-head screws threaded in inches and millimeters

<!-- image -->

3. When using interface cables equipped with a ground line, attach the ground line to the screw hole marked ' FG ' on the printer.
4. Connect the other end of the interface cable to the host computer.

Figure 2-9  Printer connectors

<!-- image -->

<!-- page 31 -->

## 2.4.2  Parallel Interface Connection

The parallel interface model TM printer is connected to the host computer via the parallel port. When a customer display (DM-D) is to be connected, connect the TM printer to the host computer via the serial port.

## 2.4.2.1  Parallel interface connection diagram

Figure 2-10  Parallel interface connection

<!-- image -->

## 2.4.2.2  Connecting the parallel interface cable

1. Insert the interface cable connector firmly into the interface connector on the connector panel.
2. Press down the clips on either side of the connector to lock it in place.
3. When using interface cables equipped with a ground line, attach the ground line to the screw hole marked ' FG ' on the printer.
4. Connect the other end of the interface cable to the host computer.

## 2.4.3  USB Interface Connection

Connect the TM printer to the host computer with a USB cable. A second TM printer can be connected via a self-powered USB hub from a printer connected to the host computer.

<!-- image -->

## Note:

A customer display (DM-D) can be connected to a USB model TM-T88II/T88III by the exclusive modular cable (RJ-45). When connecting the customer display, connect the modular jack from the customer display to the DM connector (refer to 'Installing the locking wire saddle' (page 2-12)).

When connecting the customer display to a USB model TM-T88II/T88III, set the communication conditions of the customer display as follows:

- Baud rate:

19200 bps

- •

- Bit length: 8-bit

- Parity:

no parity

- Stop bit:

1

<!-- page 32 -->

## 2.4.3.1  USB Interface Connection Diagram

Figure 2-11  USB connection

<!-- image -->

## 2.4.3.2  Connecting the USB interface cable

1. Attach the locking wire saddle at the location shown in the figure below.
2. Put the USB cable through the locking wire saddle as shown in the figure below.

<!-- image -->

Putting the USB cable through the locking wire saddle, as shown in the figure below, prevents the cable from coming unplugged.

Figure 2-12  Installing the locking wire saddle

<!-- image -->

3. Connect the USB cable from the host computer to the USB upstream connector.
4. Up to 2 USB devices can be connected to a USB model TM-T88III/T88III by using 2 USB downstream connectors.

<!-- image -->

The hub installed in a USB model connector panel is a bus-power-supply hub. It is important to note that bus-power-supply hubs (including other USB model TM printers) and bus-power-supply functions with a current consumption of 100 mA or more cannot be connected directly to the printer.

<!-- page 33 -->

To use USB model TM printers, the TM printer driver (EPSON OPOS ADK or advanced printer driver) must be installed on the host computer. Get the latest driver information from one of the following URLs:

For customers from North America, go to the following web site: http://pos.epson.com/

For customers from other countries, go to the following web site:

http://www.epson-pos.com/

Select the product name from the 'Select any product' pull-down menu.

For details on EPSON OPOS ADK or advanced printer driver, refer to 'Introducing the Control Methods' (page 3-1).

## 2.4.4  Ethernet Interface Connection

Connect a TM printer with an Ethernet interface to a network by an Ethernet cable via a hub.

## 2.4.4.1  Ethernet Interface Connection Diagram

Example:

<!-- image -->

When a TM printer is connected to the host computer via a network interface, a customer display (DM-D) cannot be connected to the TM printer. If a customer display must be connected, connect it to the host computer's serial interface.

Figure 2-13  Ethernet connection

<!-- image -->

<!-- page 34 -->

## 2.4.4.2  Connecting the Ethernet Interface Cable

1. Make sure the power supplies for both the printer and host computer have been turned off.
2. For 10Base-T or 100Base-TX Ethernet, connect a 10Base-T or 100Base-TX cable to the 10Base-T/100Base-TX Ethernet connector by pressing firmly until the connector clicks into place.

Figure 2-14  Example Ethernet port interface panel (UB-E02)

<!-- image -->

## CAUTION:

Connecting devices directly to LAN cables installed outdoors exposes them to damage from power surges caused by lightning and other inductive sources. Make sure devices without proper surge protection are cushioned by being connected through devices that do have surge protection. Otherwise, do not connect them to outdoor lines.

Never attempt to connect the customer display cable, drawer kick-out cable, or the standard telephone line cable to the 10Base-T/100Base-TX Ethernet connector.

<!-- image -->

## Note:

To use the Ethernet interface, the separate IP Address Setup Utility for the UB-E02 is required. For details on the various setup methods, refer to 'UB-E02 Technical Reference Guide.' You can obtain the 'IP Address Setup Utility for UB-E02' and the 'UB-E02 Technical Reference Guide' from one of the following URLs:

For customers from North America, go to the following web site: http://pos.epson.com/

For customers from other countries, go to the following web site:

## http://www.epson-pos.com/

Select the product name from the 'Select any product' pull-down menu.

Other compatible Ethernet interface modules may be available for your printer. Contact your EPSON dealer for information on the options available.

<!-- page 35 -->

## 2.5  Connecting Power Supply Unit and Cash Drawer

Always use one of the following power supplies: the EPSON PS-180 (the currently available power supply that can be used with either the TM-T88III or the TM-T88II); the PS-170 (the legacy power supply  used with the TM-T88II printer when that model printer was available); or use an equivalent product as the power supply unit.

Use the cash drawer handled by EPSON or your dealer.

<!-- image -->

Always use the EPSON PS-180,  the preceding model, the PS-170, or an equivalent product as the power supply unit. Using a nonstandard power supply can result in electric shock and even fire.

Should a fault ever occur in the EPSON PS-170, PS-180, or equivalent product, immediately turn off the power to the printer and remove the power supply cable from the wall socket.

## 2.5.1  Connecting the Power Supply Unit

1. Make sure the printer's power supply is turned off and the power supply unit's power cable has been removed from the wall socket.
2. Check the specifications label on the power supply unit to confirm that the wall socket power supply meets the rated voltage requirements.
3. Insert the connector of the power supply cable onto the power supply connector (labeled DC24V ).

Figure 2-15  Connecting the power supply

<!-- image -->

## CAUTION:

Be sure to remove the power supply unit's cable from the wall socket whenever connecting or disconnecting the power supply unit to the printer. Failure to do so may result in damage to the power supply unit or the printer.

Make sure the wall socket power supply satisfies the rated voltage requirements of the power supply unit. Never insert the power supply cable plug into a socket that does not meet the rated voltage requirements of the power supply unit. Doing so may result in damage to both the power supply unit and the printer.

<!-- page 36 -->

<!-- image -->

Before removing the DC cable connector from the EPSON PS-180 (current model power supply) or the PS-170 (legacy model), make sure the power supply cable has been removed from the power supply unit, then grasp the arrow-marked section of the connector and pull straight out.

## 2.5.2  Connecting the Drawer Kick-out Cable

## WARNING:

Prepare a drawer that meets printer specifications. Otherwise, the drawer kick-out solenoid or other parts in the drawer might burn and cause a fire. This may also cause the printer to malfunction at the same time.

Do not insert a telephone line into the drawer kick-out connector. Doing so may damage the telephone line or printer.

Connect the connector of the drawer kick-out cable to the printer.

Figure 2-16  Connecting the drawer-kick cable

<!-- image -->

## 2.6  Installing the Driver

To use the TM printer, either the Advanced Printer Driver (APD) (Windows driver) or the EPSON OPOS ADK (OCX driver) must be installed. For an outline of each driver, refer to 'Introducing the Control Methods' (page 3-1). For details on installation methods, refer to the manual for the respective driver.

<!-- image -->

## Note:

The TM-T88III also can be operated using the driver for TM-88II. Functions, however, are restricted as follows:

- The maximum print speed is restricted to 120 mm/s {4.72"/s} or less.
- Some baud rates (38400, 2400 bps) are not available in serial communications.

ESC/POS commands are also available for directly controlling the printer without the user of a driver. For details on ESC/POS commands, also refer to 'ESC/POS Commands' (page 3-5).

<!-- page 37 -->

## Application Development Information

This chapter describes how to control the printer and gives information useful for printer application development.

## 3.1  Introducing the Control Methods

The TM printer can be controlled and can print using any of the following 3 methods.

1. Windows printer driver (EPSON Advanced Printer Driver or APD)
2. EPSON OPOS ADK
3. ESC/POS commands

Depending on the driver and interface used, the IP setup tool for the Ethernet model, USB device driver, logo printing registration utility (TMFlash logo utility), etc. are available. Get the latest information from one of the following URLs:

For customers from North America, go to the following web site: http://pos.epson.com/

For customers from other countries, go to the following web site: http://www.epson-pos.com/

Select the product name from the 'Select any product' pull-down menu.

## 3.1.1  Windows Driver (EPSON Advanced Printer Driver)

The EPSON Advanced Printer Driver provides the TM printer with satisfactory control as a Windows driver.

## 3.1.1.1  EPSON Advanced Printer Driver overview

EPSON Advanced Printer Driver has the following features:

- ❏ Supplies a Windows printer driver for the TM printer to enable printing from a general Windows application.
- ❏ Can execute POS printer-specific functions, such as cutting paper and opening a drawer.
- ❏ Can print printer-resident fonts by selecting the font type.
- ❏ Can get the printer status using programming languages, such as Visual Basic (VB), via status API. This uses the printer's bidirectional communication capability in the Windows standard printer driver operating environment.

<!-- image -->

Note:

The status API is a printer control API originally supplied by EPSON. This can be used to get the printer status and send ESC/POS commands.

<!-- page 38 -->

## 3.1.1.2  EPSON Advanced Printer Driver contents

The installer automatically evaluates the target PC environment and automatically installs the DLL and software components necessary for operation. You can select the drivers, sample programs, and manuals to be installed.

## ❏ Drivers

You can select the driver, based on its purpose (drivers also can be installed simultaneously), including two-color printing, smoothing, continuous printing, cutting method options, and other functions.

- Receipt: For receipt printing
- Reduce 35: Reduces A4 vertical size 35% to enable printing on 80 mm {3.15"} -wide receipts

## ❏ Sample programs

You can install sample programs in Visual Basic and Visual C++ to use status API.

## ❏ Manuals

The following manuals can be installed:

- User's manual (for developers)
- Engineering data for each status
- Main function control methods (for WordPad and VB)

## 3.1.1.3  EPSON Advanced Printer Driver support environment

- ❏ Supported interfaces
- Serial, parallel, USB, Ethernet
- ❏ Supported operating systems (with confirmation of system operation)
- Windows 95 Standard, OSR 2.5
- Windows 98 Second Edition
- Windows NT Ver. 4.0 SP5, SP6
- Windows 2000 Professional
- Windows XP Professional

Refer to the release note for the driver for the latest information.

- ❏ Supported development languages
- Visual Basic
- Visual C++
- ❏ Supported devices

Refer to the release note for the driver for details on available equipment.

- EPSON receipt printer

<!-- page 39 -->

- EPSON customer display
- EPSON cash drawer

<!-- image -->

## Note:

A separate USB device driver is required for a USB model printer, and a separate IP setup utility is required for an Ethernet model printer. See the manual packed with the APD.

When you use the APD for the TM-T88III serial model or the TM-T88II, using TrueType fonts may slow printing down, due to the speed of communication between the printer and host computer. If this happens, we recommend using printer-resident fonts. For details on how to use resident fonts, see the user's manual for the APD.

Printing with TrueType fonts on other interfaces may have a slight influence on customer applications. In that case, use the printer-resident fonts. Because of the restrictions of some customer applications, when the APD is used with that application, resident fonts sometimes cannot be used, even if they are specified.

When OPOS is used, this problem does not arise because only the printer-resident fonts are available.

## 3.1.1.4  Driver information and download destination

Get the latest driver information from one of the following URLs:

For customers from North America, go to the following web site: http://pos.epson.com/

For customers from other countries, go to the following web site:

http://www.epson-pos.com/

Select the product name from the 'Select any product' pull-down menu.

## 3.1.2  EPSON OPOS ADK

The EPSON OPOS ADK supports the development environment required for OPOS application development using OPOS Control as described by the OLE for Retail POS (simply called 'OPOS' from here on) Technology Association to supply the OPOS-compliant printer driver (OCX). Use this control method to develop OPOS-compliant applications. EPSON's OPOS ADK has the following features:

- ❏ The EPSON OPOS ADK comprehensively supports the development environment required for OPOS application development at customer sites, including not only OPOS Control (CO + SO) proposed by the OPOS Association, but also the contents necessary for development, ranging from the installers and setup utilities to sample programs and manuals, and the function for getting logs for debugging, and silent installation that achieves ease of installation on a target PC.
- ❏ The EPSON OPOS ADK reduces the man-hours for application development, since it handles the following functions that application developers up till now have had to consider. The functions are supported by EPSON-original Direct IO with parameters, power-on notification, offline buffer clear processing, and so on.

<!-- image -->

## Note:

For details on the API functions, refer to the 'Application Programmers Guide Specification' provided by the OLE POS Technology Association.

<!-- page 40 -->

## 3.1.2.1  EPSON OPOS ADK (OPOS Control) overview

OPOS Control included with the EPSON OPOS ADK has the following features:

- ❏ Supplies the CO for each device class and SO for EPSON devices.
- ❏ Direct IO with parameters available:
- Gets the printer maintenance counter value
- Prints NVRAM-stored bit images, etc.
- ❏ Power-on notification function (at power on, this function automatically restores the printer to the state that was active before power off).
- ❏ Offline buffer clear processing (clears the print buffer contents in offline mode).
- ❏ Debugging function (trace function):
- Obtains a log between the application and CO (target: used API and its return value)
- Device status acquisition log (gets the offline and error causes that actually occurred in the devices)

## 3.1.2.2  EPSON OPOS ADK contents

The installer of the EPSON OPOS ADK, Ver. 2.10 or later, has a silent installation function, which can install the OPOS environment without a user interface and facilitate installation. With the installer, the following OPOS-compliant OPOS Control for EPSON devices, manuals, various utilities, and sample programs can be installed.

- ❏ OPOS Control for EPSON devices

Header files for CO, SO, C++, header files for VB, TLB file of CO, device information files, etc., can be installed.

- ❏ Manuals
- User's guide (environment construction manual: installation/uninstallation, usage methods for various utilities)
- Application Development Guide (manual for OPOS-compliant application developer: common manual, manual for each device)
- ❏ Various utilities
- SetUpPOS utility

Facilitates selection of equipment and connection ports and various settings (print wait time, etc.).

- TM Flash logo utility

Saves a bitmap file to the printer or customer display, for example.

- USB device driver

This driver is necessary to connect a USB model printer.

<!-- page 41 -->

- Sample programs

Sample programs for VB, VC++ can be installed.

## 3.1.2.3  EPSON OPOS ADK support environment

- ❏ Supported interfaces
- Serial, parallel, USB, Ethernet
- ❏ Supported OSes (with confirmation of system operation)
- Windows 95 Standard, OSR 2.5
- Windows 98 Second Edition
- Windows NT Ver. 4.0 SP5, SP6
- Windows 2000 Professional
- Windows XP Professional

Refer to the release note of the driver for the latest information.

- ❏ Supported development languages
- Visual Basic
- Visual C++

## 3.1.2.4  Driver information and download destination

Get the latest driver information from one of the following URLs:

For customers from North America, go to the following web site: http://pos.epson.com/

For customers from other countries, go to the following web site:

http://www.epson-pos.com/

Select the product name from the 'Select any product' pull-down menu.

## 3.1.3  ESC/POS Commands

To directly control the TM printer using ESC/POS commands, EPSON proposes printing/ control via ESC/POS commands. The printer can be controlled directly by sending ESC/POS commands from an application to the printer. For detailed information about ESC/POS commands, please contact EPSON or your dealer.

<!-- page 42 -->

## 3.1.4  Various Utilities

We provide the utilities described below for developers of TM printer applications. You can obtain the utilities from one of the following URLs:

For customers from North America, go to the following web site: http://pos.epson.com/

For customers from other countries, go to the following web site:

## http://www.epson-pos.com/

Select the product name from the 'Select any product' pull-down menu.

## 3.1.4.1  IP address setup utility for UB-E02

This utility and its detailed manual for developers allow you to set an IP address for a 10Base-T/ 100Base-TX Ethernet interface installed in the TM printer. Customers who have purchased the Ethernet model TM printer need this utility.

## 3.1.4.2  Electronic logo storage utility for NVRAM

This utility is designed to save logos (bitmaps) to NVRAM (non-volatile RAM). By storing shop logos to NVRAM, the print speed can be increased.

## 3.1.4.3  USB interface ID code rewrite utility

This utility is designed to edit the identification code (ID) of a USB interface.

<!-- image -->

## Note:

Each USB model TM printer has its own ID. So, two TM-88IIIs can be controlled independently from a host computer. Therefore, when replacing a TM printer that has been connected to a host computer with another printer (including same model), you must change the USB port in the printer driver on the host computer. Use of this utility, for example, frees you from changing the USB port in the printer driver.

## 3.2  Switches and Buttons

On this printer, you can disable or enable the paper FEED button. For details on how to switch between disabled or enabled, refer to the documentation for OPOS Advanced Printer Driver and ESC/POS commands, respectively.

## 3.2.1  Paper FEED Button

The printer feeds paper based on the line spacing set by the control method (OPOS, Advanced Printer Driver, ESC/POS commands). However, you cannot feed paper using the paper FEED button under the following conditions:

- When the roll paper cover is open.
- When performing a self-test (Press the FEED button to stop the self-test and press it again to resume it).
- When the paper FEED button has a function defined in a macro definition command (when ESC/POS commands are used).

<!-- page 43 -->

## 3.3  Panel LEDs and Error Status

## 3.3.1  Power LED

Table 3-1  Power LED

| Item       | Item      | Specifications         |
|------------|-----------|------------------------|
| LED color  | LED color | Green                  |
| LED states | Off       | Power is not supplied. |
|            | On        | Power is supplied.     |

## 3.3.2  No Roll Paper (PAPER OUT) LED

Table 3-2  No roll paper (PAPER OUT) LED

| Item       | Item      | Specifications                                                                   |
|------------|-----------|----------------------------------------------------------------------------------|
| LED color  | LED color | Red                                                                              |
| LED states | Off       | Roll paper is loaded.                                                            |
| LED states | On        | A roll paper near end or paper end is detected.                                  |
| LED states | Flashing  | Self-test standby state or standby state when a macro execution command is used. |

<!-- image -->

The macro function is available only when ESC/POS commands are used.

## 3.3.3  Error LED

Table 3-3  Error LED

| Item      | Item      | Specifications                                            |
|-----------|-----------|-----------------------------------------------------------|
| LED color | LED color | Red                                                       |
| On states | Off       | Printer is performing regular operations or is online.    |
| On states | On        | Offline (excluding self-test with the paper FEED button). |
| On states | Flashing  | Error state.                                              |

<!-- page 44 -->

## 3.3.3.1  Error Codes

There are three possible error types: automatically recoverable errors, recoverable errors, and unrecoverable errors.

- ❏ For automatically recoverable errors, the user does not have to take any action. The error recovers automatically when the head temperature returns to normal or the cover is correctly closed.
- ❏ A recoverable error recovers by resetting the printer or sending a command from the driver after the cause of the error is eliminated.
- ❏ For unrecoverable errors, the printer or the power supply may be malfunctioning and must be repaired.

## Automatically recoverable errors

Although normal printer operation is no longer possible when automatically recoverable errors occur, they do not represent printer failure. They can be recovered easily, as described below.

| Error                        | Error description                                                      | Error LED flash code   | Recovery measure                                            |
|------------------------------|------------------------------------------------------------------------|------------------------|-------------------------------------------------------------|
| Roll paper cover open error  | The roll paper cover was opened during printing.                       |                        | Recovers automatically when the roll paper cover is closed. |
| Print head temperature error | Ahigh temperature outside the head drive operating range was detected. |                        | Recovers automatically when the print head cools.           |

Table 3-4  Automatically recoverable errors

<!-- image -->

If the temperature cannot be detected correctly, a drive circuit error occurs.

## Recoverable errors

Although normal printer operation is not possible after a recoverable error occurs, this is not a printer malfunction. These errors can be recovered easily by turning the power on again or sending an error recovery command from the driver after eliminating the cause of the error.

Table 3-5  Recoverable errors

| Error            | Error description                   | Error LED flash code   | Recovery measure                                                                                                                                       |
|------------------|-------------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Autocutter error | Autocutter does not work correctly. |                        | Remove the jammed paper or foreign matter in the printer, close the roll paper cover, send the error recover command, or turn the power on to recover. |

<!-- page 45 -->

<!-- image -->

The error recovery command is valid only if a recoverable error (excluding automatically recoverable errors) occurs. If a recoverable error occurs, the printer recovers from the error upon receipt of an error recovery command from the driver after the cause of the error is eliminated. Turning the printer's power off and on is not required.

## Unrecoverable errors

Normal printer operation is no longer possible when unrecoverable errors occur. The printer must be repaired.

| Error               | Error description                                        | Error LED flash code Approx. 160 ms   | Recovery measure      |
|---------------------|----------------------------------------------------------|---------------------------------------|-----------------------|
| Memory R/W error    | After R/W checking, the printer does not work correctly. |                                       | Impossible to recover |
| High voltage error  | The power supply voltage is extremely high.              |                                       | Impossible to recover |
| Low voltage error   | The power supply voltage is extremely low.               |                                       | Impossible to recover |
| CPU execution error | The CPU is executing an incorrect address.               |                                       | Impossible to recover |
| Drive circuit error | The reaction of the drive circuit is abnormal.           |                                       | Impossible to recover |

Table 3-6  Unrecoverable errors

<!-- image -->

When an unrecoverable error occurs, turn off the power supply immediately.

<!-- page 46 -->

## 3.4  Sensors

## 3.4.1  Paper Sensors

The printer has two paper sensors.

## 3.4.1.1  Roll paper near-end sensor

The roll paper near-end sensor uses the diameter of the roll paper to detect whether the remaining paper is getting low. This sensor is located inside the roll paper supply unit, and you can fine-tune the amount of remaining paper detected by this sensor. (For details on adjustment, see page 2-7.)

Lighting of the PAPER OUT LED in a near-end state does not indicate an error. Regular printing is possible.

<!-- image -->

## Note:

Detection of the near-end status does not necessarily indicate the complete end of the roll paper. Use the sensor as an indication of when to replace the roll paper.

By changing the driver setting, a print job can be canceled automatically during the near-end status.

## 3.4.1.2  Roll Paper End Sensor

The roll paper end sensor detects whether there is paper in the paper path. When there is no paper (paper end status), the PAPER OUT LED and ERROR LED light to indicate an error has occurred. If the sensor detects a roll paper end, the printer stops printing, even in the process of printing. We recommend that you mainly rely on the roll paper near-end sensor and use the roll paper end sensor secondarily.

## 3.4.2  Printer Cover Sensor

## 3.4.2.1  Roll Paper Cover Open Sensor

The cover-open sensor monitors the roll paper cover. When the sensor detects an open cover during printing, the printer stops printing immediately and automatically goes offline.

This status is treated as an automatically recoverable error, and the ERROR LED flashes. When the printer cover is closed, the ERROR LED goes out, and the printer goes online and starts printing at the beginning of the line it was printing when the cover was opened.

When the printer recovers, it feeds paper to take up slack and starts printing from the beginning of the line where the error occurred. In this case, double printing and printing position shift may occur. When a cover open error occurs, we recommend clearing the printer's print buffer by sending the error recovery command from the driver, and resending the print data.

<!-- image -->

## Note:

Whether the cover is open or not does not affect the status reported by the roll paper end sensor.

<!-- page 47 -->

## 3.4.3  Offline

This printer is not equipped with an online/offline switch. The printer automatically goes offline under the following conditions:

- During power on (including resetting with the interface) until the printer is ready
- When the printer is waiting to receive data
- During the self-test
- When the roll paper cover is open
- During paper feeding using the paper FEED button
- When the printer stops printing due to a paper-end (if an empty paper supply is detected by the roll paper end sensor or if the driver has been set to stop printing when a roll paper near-end is detected)
- When an error has occurred
- During macro executing standby status

## 3.4.4  Busy State

## 3.4.4.1  Selecting conditions for invoking a BUSY state

With DIP SW2-1, you can select conditions for invoking a BUSY state as either of the following:

- ❏ When the receive buffer is full
- ❏ When the receive buffer is full or the printer is offline

<!-- image -->

## Note:

In either case above, the printer enters the BUSY state after power is turned on (including resetting with the interface), while the printer is in the standby state waiting for data, and when a self-test is being run.

For details on how to change the DIP switch setting for receive buffer full, see 'Setting the DIP Switches' on page 2-2.

You do not need to change this item when using OPOS or the Advanced Printer Driver.

Table 3-7  Printer BUSY conditions and status of DIP SW2-1

|                                 |                                                                                                                                   | DIP SW2-1 status   | DIP SW2-1 status   |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------|
| Printer status                  | Printer status                                                                                                                    | ON                 | OFF                |
| Offline                         | During the period after power is turned on (including resetting with the interface) to when the printer is ready to receive data. | BUSY               | BUSY               |
|                                 | During the self-test.                                                                                                             | BUSY               | BUSY               |
|                                 | When the cover is open.                                                                                                           | -                  | BUSY               |
|                                 | During paper feed with the paper FEED button.                                                                                     | -                  | BUSY               |
|                                 | When the printer stops printing due to a paper-end (when printer has run out of roll paper).                                      | -                  | BUSY               |
|                                 | When an error has occurred.                                                                                                       | -                  | BUSY               |
| When the receive buffer is full | When the receive buffer is full                                                                                                   | BUSY               | BUSY               |

<!-- page 48 -->

<!-- image -->

When DIP SW2-1 is ON, the printer will not become BUSY even if printer hardware stops operating.

- When an error has occurred
- When the cover is open
- When printing has stopped for a paper out
- When paper is fed by the paper FEED button

## 3.5  NVRAM (Non-volatile Memory)

NVRAM is mounted on this printer, and bitmap images (for example, business logos) or other data are written to it. Pay attention to the following when using NVRAM.

- ❏ The following restriction applies when performing operations (including storing and deleting data) in NVRAM.
- Do not use the paper FEED button.
- ❏ The printer sometimes enters the BUSY state when data is being written to NVRAM. It is important not to send data from the host computer while the printer is in the BUSY state, because the printer cannot process any received data.
- ❏ Frequent use of the functions for writing data to and deleting data from NVRAM may damage the memory. As a rule, in using the various commands to write to NVRAM, avoid writing more than an average of ten times per day.

## 3.6  Bar Code Printing

This printer can print the following types of bar codes:

UPC-A, UPC-E JAN 8 (EAN 8), JAN 13 (EAN 13) CODE 39 ITF (Interleaved 2 of 5) CODABAR (NW-7) CODE 93 CODE 128

To set and print each bar code, refer to the OPOS, Advanced Printer Driver, and ESC/POS command documentation, respectively.

<!-- page 49 -->

## 3.7  Operating Mode (Switch Panel Operation)

The printer has a self-test mode to check printer settings in addition to the regular print mode.

## 3.7.1  Self-test Mode

In the self-test mode, the following items are checked and printed out:

- Control circuit functions
- Printer mechanism functions
- Print quality
- Control software ROM version
- DIP switch settings

Follow the steps below to start a self-test:

1. With the roll paper cover open, press and hold down the paper FEED button and turn on the printer. The printer prints various printer settings.
2. When the printer finishes printing the printer status, check whether the following message is printed:

```
'SELF-TEST printing. Please press PAPER FEED button'
```

The printer is now in the self-test wait mode.

3. To start a test print, press the paper FEED button while the printer is in the self-test wait mode.
4. Check that the following has been printed:

```
'***   completed   ***'
```

This indicates that the printer has been initialized and returned to the normal mode.

<!-- page 50 -->

## 3.8  FAQ List

Listed here are the most-asked questions (Q) and answers (A).

1. Look for information relating to your inquiry or problem in the questions.
2. Then, follow the instructions described in the 'A' sentence below it.

## 3.8.1  Q: Why has my print data dropped out?

- A: Check the handshake process. Data dropout can occur when the handshake between the host computer and printer is not performed correctly. This can result in errors related to print buffer size.

## 3.8.1.1  Corrective procedure

1. Check the serial communication cable, and check the cable connector specifications. (See 'Serial Interface Connection' on page 2-8.)
2. Check the serial communication conditions of the printer and the host.

Serial communication conditions

- Baud rate
- Parity
- Flow control
- Data length

You can check printer settings as follows:

1. Run a self-test to check the printer's serial communication conditions. (See page 3-13.)
2. Setting communication conditions using the DIP switches. Set the baud rate with DIP SW1-7 and SW1-8. (Refer to page 2-4.)

<!-- page 51 -->

## 3.8.2  Q: Why does the drawer kick-out not operate properly?

- A: Drawer specifications differ depending on the manufacturer and the part number. Make sure the specifications of the drawer to be used meet the following conditions before connecting it to the drawer kick-out connector. These conditions also apply to any other devices that use the drawer kick-out connector. Any devices that do not satisfy all the following conditions must not be used.

## Conditions

- A load must be provided across drawer kick-out connector pins 4 and 2 or across pins 4 and 5. (*1)
- When the drawer open/close signal is used, a switch must be provided across drawer kick-out connector pins 3 and 6. (*2)
- The solenoid used for the cash drawer must have a resistance of 24 Ω or higher. (*3)

NOTES

- (*1) Operating the printer with incorrectly installed devices voids the warranty.
- (*2) Connecting devices other than the drawer open/close switch voids the warranty.
- (*3) Using a drawer or a drawer kick-out connector with an input current of 1 A or more may cause an overcurrent, which will cause the device to malfunction.

## 3.8.3  Q: I cannot print part of Page 0 in Visual Basic. Why?

Cannot print a part of Page 0 (for example: ) in Visual Basic.

- A: Try printing using the following procedure:

When programming with Visual Basic, limitations prevent data from 81H through 9FH and from E0H through FEH from being sent as characters. However, you can use the following procedure to send this data:

Dim Send\_ data(0) As Byte Send\_data(0) = &amp;h81 '1 byte of sending data MSComm1.Output = Send\_data

<!-- page 52 -->



<!-- page 53 -->

## ESC/POS Command-related Information

This chapter introduces the printer operation settings, which can be made by using ESC/POS commands, and precautions for those operation settings.

## 4.1  NV Memory (Non-volatile Memory)

The printer's NV memory can be roughly divided into three parts:

- Firmware program area
- NV memory area for product information (This area cannot be edited by the user.)
- NV memory area that the user can access

The following areas are in the NV memory that the user can access:

- NV user memory
- NV graphics memory
- User-defined character code page (page 255 (blank page))
- Area of user-defined command default values

You can customize your printer by changing these values. Note the following when writing to and deleting from NV memory.

- ❏ The following restrictions apply when performing non-volatile memory operations (including data writing and deleting).
- Do not press the paper FEED button.
- Do not execute a real-time command.
- The ASB status is not sent, even when the ASB function in ESC/POS commands is set to Enabled .
- ❏ The printer sometimes enters the BUSY state while data is written to NV memory. It is important not to send data from the host computer while the printer is BUSY, because the printer cannot process any received data.
- ❏ Frequent use of the functions for writing data to and deleting data from NV memory may damage the memory. As a rule in using the various commands to write to NV memory, avoid writing more than an average of ten times per day.

## 4.1.1 Using NV Memory

You can use the free area in NV memory for writing memos, for other character information, for anything you like. Data written to this area is held in the memory even if you turn off the power. For details on how to read and write data, see the 'ESC/POS Application Programming Guide.'

<!-- page 54 -->

<!-- image -->

For details on NV graphics and NV bit images, see the 'ESC/POS Application Programming Guide.'

## 4.2  Printer Status

There are three ways to get the printer status, and each method has the following features. For details, see the 'ESC/POS Application Programming Guide.'

When a status request is processed as a regular command, the printer automatically returns a status message whenever the status changes. Always monitor the value

- Automatic status back (ASB): returned.
- Real-time status:

When the printer receives a real-time status command, it responds with the specified printer status. Returning the printer status takes priority over any regular print data.

- Status:
- The printer transmits a specified printer status in the same way it processes normal print

data.

## 4.3  Precautions When the Printer Is Offline

When printer handshake is set with DIP SW2-1 ON (BUSY = receive buffer full), use the ASB function to check the printer status. Using the ASB lets the printer send status automatically at the time of switching online/offline. When using a real-time command, make sure the receive buffer is not full.

Example: After using the 4KB receive buffer to send data for each line, check the printer status.

## 4.4  Outputting Hex Dumps

TM printers can print data transmitted from the host computer as hexadecimal numbers and their corresponding characters. Called 'hex dump mode,' this allows you to make sure that data has been sent correctly to the TM printer by comparing the printed result with the program. Follow the steps below to output a hex dump:

1. With the roll paper cover open, turn power on while holding down the paper FEED button.
2. Close the roll paper cover.
3. Data received from then on is printed out from the TM printer in hexadecimal numbers and their corresponding characters.

To quit the hex dump mode, turn the printer off after printing ends.

<!-- image -->

## Note:

Do not use this mode when using OPOS or the APD. Doing so will cause unexpected data to be printed, because the driver uses proprietary control to drive the printer.

<!-- page 55 -->

## Product Specifications

## 5.1  Product Specifications (TM-T88II/TM-T88III)

Table 5-1  Specifications

| Print method                                  | Thermal line printing                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Print width                                   | Standard: paper width of80mm- print width of 72 mm{2.84"}, 512 dot positions Factory option (with spacer): paper width of 58 mm{2.28"}- print width of 50.8 mm{2"}, 360 dot positions                                                                                                                                                   |
| Cut type                                      | Partial cut (left-most one point uncut)                                                                                                                                                                                                                                                                                                 |
| Maximum paper thickness for the manual cutter | 100 µ mor less                                                                                                                                                                                                                                                                                                                          |
| Character sets                                | TM-T88III: 95 alphanumeric, 37 international characters, 128 × 11 pages of extended graphics TM-T88II 95 alphanumeric, 32 international characters, 128 × 7 pages of extended graphics                                                                                                                                                  |
| Interface (compatible)                        | RS-232C/bidirectional parallel Dealer option: USB, Ethernet                                                                                                                                                                                                                                                                             |
| Buffer                                        | Receive buffer: 4KB/45 bytes                                                                                                                                                                                                                                                                                                            |
| Buffer                                        | User-defined buffer For both downloaded bitmap images and fonts: Approx. 12KB                                                                                                                                                                                                                                                           |
| Buffer                                        | Macro buffer: 2KB                                                                                                                                                                                                                                                                                                                       |
| Buffer                                        | NV graphics data storage area: 256KB NV user memory: 1KB                                                                                                                                                                                                                                                                                |
| DKD function                                  | 2 drives                                                                                                                                                                                                                                                                                                                                |
| Power supply                                  | Power supplied by optional AC adapter, PS-180 or the previous adapter, the PS-170                                                                                                                                                                                                                                                       |
| Operating voltage                             | 24 VDC ± 7%                                                                                                                                                                                                                                                                                                                             |
| Current consumption                           | High-speed mode Average: TM-T88II: Approx. 1.7 A TM-T88III: Approx. 1.8 A (Font A, α -N, 36 capital letters, rolling pattern, 42-column printing) Peak: Approx. 7.7 A Low-power mode Average: Approx. 1.2 A (Font A, α -N, 36 capital letters, rolling pattern, 42-column printing) Peak: Approx. 6.6 A Standby: Average: Approx. 0.2 A |
| Temperature/humidity                          | Operating: 5 to 45°C (41 to 113°F), 10 to 90% RH Storage: Shipped packed state -10 to +50°C (14 to 122°F), 10 to 90% RH                                                                                                                                                                                                                 |
| Weight                                        | Approx. 1.8 kg {3.968 lb}                                                                                                                                                                                                                                                                                                               |

<!-- page 56 -->

## 5.2  Print Specifications (TM-T88II/TM-T88III)

Table 5-2  Print characteristics

| Characteristics       | Specifications                                                     |
|-----------------------|--------------------------------------------------------------------|
| Print method          | Thermal line printing                                              |
| Paper feed method     | Unidirectional with friction feed                                  |
| Print width           | ❐ 72 mm{2.84"} ❐ 50.8 mm{2.28"} (factory option with paper spacer) |
| Characters per line   | See table titled 'Print width/characters per line,' below.         |
| Print speed           | See table titled 'Print speed,' below.                             |
| Paper feed speed      | TM-T88II: Approx. 120 mm/s {4.72"/s} during continuous paper feed  |
| Paper feed speed      | TM-T88III: Approx. 150 mm/s {5.91"/s} during continuous paper feed |
| Carriage return width | 4.23 mmor 1/6"                                                     |

Table 5-3  Print width/characters per line

| Paper width (mm)                       | Roll paper width (mm)   | Roll paper width (mm)   |
|----------------------------------------|-------------------------|-------------------------|
|                                        | 80 (standard)           | 58 (factory option)     |
| Number of print dots                   | 512                     | 360                     |
| Print width (mm)                       | 72 {2.84"}              | 50.8 {2.28"}            |
| Font A (12 × 24) number of columns     | 42                      | 30                      |
| Font B (9 × 17) number of columns      | 56                      | 40                      |
| Kanji font (24 × 24) number of columns | 21                      | 15                      |

Table 5-4  Print speed

| Print control mode        | Unit   | Setting                           | Print speed (max.)   | Print speed (max.)   |
|---------------------------|--------|-----------------------------------|----------------------|----------------------|
|                           |        |                                   | TM-T88II             | TM-T88III            |
| High-speed mode (*1)      | mm/sec | -                                 | 120 {4.72"/s}        | 150 {5.91"/s}        |
|                           | lps    | Line space setting: 3.18 mm{1/8"} | 38                   | 47.2                 |
|                           | lps    | Line space setting: 4.23 mm{1/6"} | 28.4                 | 35.5                 |
| Low-power mode            | mm/sec | -                                 | 70 {2.76"/s}         | 70 {2.76"/s}         |
|                           | lps    | Line space setting: 4.23 mm{1/6"} | 16.5                 | 16.5                 |
| Printing ladder bar codes | mm/sec | Line space setting: 4.23 mm{1/6"} | 42 {1.65"/s}         | 42 {1.65"/s}         |

lps: lines per second

*1: During printing (at 24 V, 28 ° C {82.4 ° F}, density level 2). Note, however, the print speed automatically changes with the voltage applied to the printer and with the head temperature conditions.

<!-- image -->

## Note:

The print speed sometimes slows down, depending on the data transfer speed and other settings.

A slow baud rate is a probable cause of intermittent printing. We recommend using a faster baud rate.

<!-- page 57 -->

## 5.3  Character Specifications (TM-T88II/TM-T88III)

Table 5-5  Character specifications

| Item                    | Item                    | Specifications                                                                                  | Specifications                                                                                       | Specifications                                                                                       | Specifications                                                                                       |
|-------------------------|-------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Character type          | Alphanumeric            | 95 character sets                                                                               | 95 character sets                                                                                    | 95 character sets                                                                                    | 95 character sets                                                                                    |
| Character type          | International           | TM-T88III:                                                                                      | 37 types                                                                                             | TM-T88II                                                                                             | 32 types                                                                                             |
| Character type          | Extended graphics       | TM-T88III: TM-T88II:                                                                            | 128 characters × 11 pages (including 1 blank page) 128 characters × 7 pages (including 1 blank page) | 128 characters × 11 pages (including 1 blank page) 128 characters × 7 pages (including 1 blank page) | 128 characters × 11 pages (including 1 blank page) 128 characters × 7 pages (including 1 blank page) |
| Character configuration | Character configuration | See table titled 'Character configurations and dimensions,' below. (Default is font A.)         | See table titled 'Character configurations and dimensions,' below. (Default is font A.)              | See table titled 'Character configurations and dimensions,' below. (Default is font A.)              | See table titled 'Character configurations and dimensions,' below. (Default is font A.)              |
| Character dimensions    | Character dimensions    | See 'Character configurations and dimensions,' below. (Spaces between characters not included.) | See 'Character configurations and dimensions,' below. (Spaces between characters not included.)      | See 'Character configurations and dimensions,' below. (Spaces between characters not included.)      | See 'Character configurations and dimensions,' below. (Spaces between characters not included.)      |

Table 5-6  Character configurations and dimensions

|                      | Standard W×H(mm)   | Double-height W×H(mm)   | Double-width W×H(mm)   | Double-width / Double-height W×H(mm)   |
|----------------------|--------------------|-------------------------|------------------------|----------------------------------------|
| Font A (12 × 24)     | 1.41 × 3.39        | 1.41 × 6.77             | 2.82 × 3.39            | 2.82 × 6.77                            |
| Font B (9 × 17)      | 0.99 × 2.40        | 0.99 × 4.80             | 1.98 × 2.40            | 1.98 × 4.80                            |
| Kanji font (24 × 24) | 3.39 × 3.39        | 3.39 × 6.77             | 6.77 × 3.39            | 6.77 × 6.77                            |

Notes:

1. Spaces between characters not included.

2. Characters can be scaled up to 64 times as large as the standard size.

## 5.4  Paper Specifications (TM-T88II/TM-T88III)

See Appendix B.

<!-- page 58 -->

## 5.5  Printable Area (TM-T88II/TM-T88III)

Figure 5-1  Printable area

<!-- image -->

Table 5-7  Dimensions

| a (roll paper width)        |   b (left margin) | c (print width)   |   d (right margin) |
|-----------------------------|-------------------|-------------------|--------------------|
| 79.5 ± 0.5                  |               3.7 | 72.2 ± 0.2        |                3.7 |
| 57.5 ± 0.5 (factory option) |               3.7 | 50.8 ± 0.2        |                3.0 |

* Units: mm

<!-- page 59 -->

## 5.6  Print Position versus Cutter Position (TM-88II/TM88III)

The following illustration shows the relationship between print position and cutter position.

<!-- image -->

Figure 5-2  Print position versus cutter position

<!-- image -->

The values in the figure are center values. The margins vary, due to paper slack or paper variations from piece to piece. Allow a certain margin of error when setting the paper cutter cut position.

<!-- page 60 -->

## 5.7  Overview of External Dimensions (TM-T88II/TM-T88III)

## 5.7.1  External Dimensions

The dimensions in the figure below are common to both the TM-88III and TM-88III.

- ❏ Height 148 mm {5.83"}

- ❏ Width

145 mm {5.71"}

- ❏ Depth

195 mm {7.68"}

- ❏

- Weight

Approx. 1.8 kg {3.97 lb} (without roll paper)

[Units: mm]

<!-- image -->

Figure 5-3  Dimensions

<!-- image -->

<!-- page 61 -->

## 5.8  Operating Specifications (TM-T88II/TM-T88III)

Table 5-8  Temperature and humidity

| Item                  |                                 | Specifications                                                                                                          |
|-----------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Temperature/ Humidity | Operating:                      | 5 to 45°C (41 to 113°F), 10 to 90% RH no condensation allowed. (Refer to ambient operating ranges in the figure below.) |
|                       | Storage: (shipped packed state) | -10 to +50°C (14 to 122°F), 10 to 90% RH (excluding paper)                                                              |

Figure 5-4

<!-- image -->

<!-- page 62 -->



<!-- page 63 -->

## Interfaces and Connectors

## A.1  RS-232 Serial Interface

## A.1.1  Interface Board Specifications (RS-232-compliant)

Table A-1  Serial interface specifications

Item

Specifications

Data transfer method

Serial

Synchronization

Asynchronous

Handshake

Select one of the following with DIP SW1-3:

- [ ] ❏ DTR/DSR

(DIP SW1-3 OFF)

default

- [ ] ❏ XON/XOFF

(DIP SW1-3 ON)

Signal level

MARK

-3 V to -15 V logic '1' /ON

SPACE

+3 V to +15 V logic '0' /OFF

Bit length

Select one of the following with DIP SW1-4:

- [ ] ❏ 7 bit

(DIP SW1-4 ON)

- [ ] ❏ 8 bit

(DIP SW1-4 OFF) default

Baud rate

Select one of the following with DIP SW1-7 and SW1-8:

- [ ] ❏ 19200 bps

(DIP SW1-7 OFF, DIP SW1-8 OFF)

- [ ] ❏ 9600 bps

(DIP SW1-7 ON, DIP SW1-8 OFF)default

- [ ] ❏ 4800 bps

(DIP SW1-7 OFF, DIP SW1-8 ON)

- [ ] ❏ 2400 bps (T88ii) or

38400 bps (T88III)

(DIP SW1-7 ON, DIP SW1-8 ON)

[bps: bits per second]

Parity check

Select one of the following with DIP SW1-5:

- [ ] ❏ Yes

(DIP SW1-5 ON)

- [ ] ❏ No

(DIP SW1-5 OFF)

Parity selection

Select one of the following with DIP SW1-6:

- [ ] ❏ Even

(DIP SW1-6 ON)

- [ ] ❏ Odd

(DIP SW1-6 OFF)

Stop bit

1 or more bits

However, the stop bit for data transfer from the printer is fixed to 1 bit.

Connector

Printer side

DSUB 25-pin (female) connector

<!-- page 64 -->

## A.1.2  Functions of each Connector Pin

Table A-2  Pin assignments

|   Pin no. | Signal name   | Signal direction   | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------|---------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         1 | FG            |                   | Frame ground                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|         2 | TXD           | Output             | Transmission data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|         3 | RXD           | Input              | Reception data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|         4 | RTS           | Output             | Equivalent to DTR signal (pin 20)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|         6 | DSR           | Input              | This signal indicates whether the host computer can receive data. SPACE indicates that the host computer can receive data. MARK indicates that the host computer cannot receive data. When DTR/DSR control is selected, the printer transmits data after confirming this signal (except if transmitted using some ESC/POS commands). When XON/XOFF control is selected, the printer does not check this signal. Changing DIP SW2-7 lets this signal be used as a printer reset signal. When you use this signal as the printer's reset signal, the printer is reset when the signal remains MARK for a pulse width of 1 ms or more.                                                                         |
|         7 | SG            |                   | Signal ground                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|        20 | DTR           | Output             | 1) When DTR/DSR control is selected, this signal indicates whether the printer is Busy. SPACE status -indicates the printer is ready to receive data. MARK status -indicates the printer is Busy. Set Busy conditions with DIP SW2-1. (Refer to 'Busy State' on page 3-11). 2) When XON/XOFF control is selected, the signal indicates that the printer is properly connected and ready to receive data from the host. SPACE status -indicates the printer is properly connected and ready to receive data from the host. The signal is always SPACE, except in the following cases: • During the period from when power is turned on to when the printer is ready to receive data. • During the self-test. |
|        25 | INIT          | Input              | Changing DIP SW2-8 enables this signal to be used as a reset signal for the printer. The printer is reset if the signal remains at SPACE for a pulse width of 1 ms or more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## A.1.3  XON/XOFF

When XON/XOFF control is selected, the printer transmits the XON or XOFF signals as follows. The transmission timing of XON/XOFF differs, depending on the setting of DIP SW2-1.

Table A-3  XON/XOFF transmissions

| Signal   | Printer status                                                                            | DIP SW2-1 status   | DIP SW2-1 status   |
|----------|-------------------------------------------------------------------------------------------|--------------------|--------------------|
|          |                                                                                           | 1 (ON)             | 0 (OFF)            |
| XON      | 1) When the printer goes online after turning on the power (or reset using the interface) | Transmit           | Transmit           |
| XON      | 2) When the receive buffer is released from the buffer full state                         | Transmit           | Transmit           |
| XON      | 3) When the printer switches from offline to online                                       | -                  | Transmit           |
| XON      | 4) When the printer recovers from an error using some ESC/POS commands                    | -                  | Transmit           |
| XOFF     | 5) When the receive buffer becomes full                                                   | Transmit           | Transmit           |
| XOFF     | 6) When the printer switches from online to offline                                       | -                  | Transmit           |

<!-- page 65 -->

## A.1.4  Code

The hexadecimal numbers corresponding to the XON/XOFF codes are shown below.

- ❏ XON code:

11H

- ❏ XOFF code:

13H

<!-- image -->

Note:

When the printer goes from offline to online and the receive buffer is full, XON is not transmitted.

When the printer goes from online to offline and the receive buffer is full, XOFF is not transmitted.

When memory switch MSW 1-3 is off, XON is not transmitted as long as the printer is offline, even if a receive buffer full state has been cleared.

## A.2  IEEE 1284 Parallel Interface

## A.2.1  Modes

The IEEE 1284 parallel interface supports the following two modes.

Table A-4  Parallel modes

| Mode               | Communication direction      | Other information                                    |
|--------------------|------------------------------|------------------------------------------------------|
| Compatibility mode | Host → Printer communication | Centronics-compliant                                 |
| Reverse mode       | Printer → Host communication | Assumes a data transfer from an asynchronous printer |

## Compatibility mode

Compatibility mode allows data transmission from host to printer only: Centronics-compatible.

## Specifications

- Data transmission:

8-bit parallel

- Synchronization:

Externally supplied STROBE* signals

- Handshaking:

ACK* and BUSY signals

- Signal levels:

TTL-compatible connector

- Connector:

ADS-B36BLFDR176 (HONDA) or equivalent product (IEEE 1284 Type B)

- Reverse communication:

Nibble or byte mode

*A rule above a signal name indicates an ' L ' active signal.

<!-- page 66 -->

## Reverse mode

The transfer of status data from the printer to the host proceeds in the nibble or byte mode.

This mode allows data transfer from an asynchronous printer under the control of the host. Data transfers in the nibble mode are made via the existing control lines in units of four bits (a nibble). In the byte mode, data transfer proceeds by making the 8-bit data lines bidirectional. Both modes fail to proceed concurrently in the compatibility mode, thereby causing half-duplex transmission.

<!-- page 67 -->

## A.2.2  Interface Signals

Table A-5  Connector pin assignments

|   Pin | Source   | Compatibility Mode   | Nibble Mode        | Byte Mode   |
|-------|----------|----------------------|--------------------|-------------|
|     1 | Host     | Strobe               | HostClk            | HostClk     |
|     2 | Host/Ptr | Data0(LSB)           | Data0 (LSB)        | Data0 (LSB) |
|     3 | Host/Ptr | Data1                | Data1              | Data1       |
|     4 | Host/Ptr | Data2                | Data2              | Data2       |
|     5 | Host/Ptr | Data3                | Data3              | Data3       |
|     6 | Host/Ptr | Data4                | Data4              | Data4       |
|     7 | Host/Ptr | Data5                | Data5              | Data5       |
|     8 | Host/Ptr | Data6                | Data6              | Data6       |
|     9 | Host/Ptr | Data7 (MSB)          | Data7 (MSB)        | Data7 (MSB) |
|    10 | Printer  | Ack                  | PtrClk             | PtrClk      |
|    11 | Printer  | Busy                 | PtrBusy/Data3, 7   | PtrBusy     |
|    12 | Printer  | Perror               | AckDataReq/Data2,  | AckDataReq  |
|    13 | Printer  | Select               | Xflag/Data1, 5     | Xflag       |
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
|    28 |          | GND                  | GND                | GND         |
|    29 |          | GND                  | GND                | GND         |
|    30 |          | GND                  | GND                | GND         |
|    31 | Host     | Init                 | Init               | Init        |
|    32 | Printer  | Fault                | DataAvail/Data0, 4 | DataAvail   |
|    33 |          | GND                  | ND                 | ND          |
|    34 | Printer  | DK_STATUS            | ND                 | ND          |
|    35 | Printer  | +5V                  | ND                 | ND          |
|    36 | Host     | SelectIn             | 1284-Active        | 1284-Active |

* NC:

Not Connected

ND: Not Defined

<!-- page 68 -->

<!-- image -->

A signal name with a rule above it indicates an 'L' active signal. Bidirectional communications cannot take place, unless all signal names for both sides correspond to each other. Connect all signal lines using a twisted-pair cable. Connect the return side to the signal ground level. Make sure the signals satisfy electrical characteristics. Set the leading edge and trailing edge times to 0.5 µ s or less. Do not ignore Ack or BUSY signals during a data transfer. Ignoring such signals may result in data

corruption.

Make the interface cables as short as possible.

<!-- page 69 -->

## Options and Consumables

## B.1  Roll Paper

The table below shows the roll paper specifications.

| Type of paper                                                                 | Specified thermal paper       | Specified thermal paper   |
|-------------------------------------------------------------------------------|-------------------------------|---------------------------|
| Shape                                                                         | Roll                          | Roll                      |
| Select from the following: ❐ 79.5 mm±0.5 mm(default) ❐ 57.5 mm±0.5 mm(factory | option with                   | Paper width               |
| Internal diameter Outer diameter                                              | 12 mm{0.47"} 18 mm{0.71"}     | Roll core                 |
| External dimensions Outer                                                     | diameter 83 mm{3.27"} or less |                           |

Table B-1  Paper specifications

<!-- image -->

If roll core standards vary from the figures above, it is difficult for the roll paper NE detector to detect the remaining amount of roll paper exactly. Use these figures merely as a guideline.

## B.2  Power Supply

The following describes the specifications for the optional power supplies (PS-170 and PS-180).

## B.2.1  PS-170 (Legacy Model no Longer Available from the Dealer)

## B.2.1.1  Electrical characteristics

- [ ] ❏ Input conditions

Input voltage (rating):

90 to 264 VAC (100 VAC -10% to 230 VAC +15%)

Frequency (rating):

50/60 Hz ± 3 Hz

Power consumption (rating):

100 VA

- [ ] ❏ Output conditions

Output voltage (rating):

24 VDC + 5%

Output current (rating):

2.0 A

Output electric power (rating):48 VA

Output peak current:

4.5 A (within 300 msec)

## B.2.1.2  Case specifications

- ❏ Dimensions:

80 mm (D) × 166 mm (L) × 44 mm (H) (excluding projections).

{3.15 × 6.54 × 1.73"} See the figure on the next page.

- ❏ Weight:

Approx. 0.52 kg {1.15 lb} (excluding the AC cable)

- ❏ Material:

Durability level: V0

- ❏ Color:

Black (matte)

<!-- page 70 -->

Figure B-1  Case specifications

<!-- image -->

## B.2.1.3  Material

No specific brominated flame retardants, such as PBBE and PBB, are used in this product.

## B.2.1.4  AC cable selection

- ❏ Select an AC cable that satisfies the following conditions:
- Safety standard product
- Plug with PE terminal
- ❏ The AC cable is not packed with this printer.

## B.2.2  PS-180 (Current Product for Printers)

## B.2.2.1  Electrical characteristics

- ❏ Input conditions

Input voltage (rating):

90 to 264 VAC (100 VAC -10% to 230 VAC +15%) 50/60 Hz ± 3 Hz

Frequency (rating):

Power consumption (rating):

100 VA

<!-- page 71 -->

- ❏ Output conditions

Output voltage (rating):

24 VDC ± 5%

Output current (rating):

2.0 A

Output electric power (rating):

48 VA

Output peak current:

4.5 A

## B.2.2.2  Case specifications

- ❏ Dimensions:

68 mm (D) × 136 mm (L) × 32 mm (H) (excluding projections) {2.68" × 5.35" × 1.26"} Refer to the figure below.

- ❏ Weight:

Approx. 0.4 kg {14.11 oz} (excluding the AC cable)

- ❏ Material:

Durability level: V0

- ❏ Color:

Black (matte)

Figure B-2  Case specifications

<!-- image -->

## B.2.2.3  Material

No specific brominated flame retardants, such as PBBE and PBB, are used in this product.

## B.2.2.4  AC cable selection

- ❏ Select an AC cable that satisfies the following conditions.
- Safety standard product
- Plug with PE terminal

- ❏ Ground connection: Be sure to ground for safety.

<!-- page 72 -->



<!-- page 73 -->

## Appendix C

## Character Code Tables

## C.1  Page 0 (PC437: USA, Standard Europe)

(International character set: when 'America' is selected)

<!-- image -->

| DC4   |
|-------|

<!-- image -->

Note:

The character code tables show only character configurations.  They do not show the actual print pattern.

<!-- page 74 -->

## C.2  Page 1 (Katakana)

<!-- image -->

|              | HEX,         | 8              | 9 &#124;       | 9 &#124;   |      |              | A)]B)C\),Ds)E&#124;F   | A)]B)C\),Ds)E&#124;F   |              |                |             |             |             |          |      |
|--------------|--------------|----------------|----------------|------------|------|--------------|------------------------|------------------------|--------------|----------------|-------------|-------------|-------------|----------|------|
| HEX          | BIN 1000     | &#124; 1001 +t | &#124; 1001 +t | 1010       | 1010 | &#124; 1011  | &#124; 1011            | &#124; 1100            | &#124; 1100  | &#124; 1101    | &#124; 1101 | &#124; 1110 | &#124; 1110 | &#124; x | 1111 |
| 0            | &#124;o000'— | 128            | 144            |            | sp   | 160          | _- 176                 | y                      | 192          | =              | 208         | =           | 224         |          |  240 |
| 1 0001       | -_           | T 129          | 145            | °          | 161  |              | 7 177                  | F 193                  |              | vA             | 209         | E           | 225         | A        |  241 |
| 2 /0010      | =            | 4 130          | 146            | [          |      | 4 162        | 178                    | 194                    | Yy           | z              | 210         | +           | 226         | aE       |  242 |
| 3            | 0011 ™       | 131            | 147            | Fi         | 163  | 9            | 179                    | &#124;7                | 195          | &#124; &#124;¥ | 211         | 4           | 227         | A        |  243 |
| 4 0100       | 132          |                | 148            | .          |      | + 164        | 180                    | &#124;b                | 196          |                | 212         | &#124;4     | 228         | 4        |  244 |
| 5 /0101      | &#124; 133   | _ &#124;       | 149            |            | 165  | a            | 181                    | F                      | 197          | a              | 213         | » N         | 229         | iF       |  245 |
| 6 /0110      | &#124;] 134  |                | 150            | 7          | 166  | a            | 182                    | =                      | 198          | a              | 214         |             | 230         | 4        |  246 |
| 7 0111       | 135          | &#124;         | 151            | oi7        | 167  | 1%           | 183                    | (x                     | 199          | &#124;F        | 215         | WwW         | 231         | #@       |  247 |
| 8 &#124;1000 | &#124; 136   | r              | 152            | 4          |      | 2 168        | 184                    | cS                     | 200          | y              | 216         | a           | 232         | T        |  248 |
| 9 /1001      | l 137        | 7              | 153            | 9          |      | aT 169       | 185                    |                        | 201          | wv             | 217         | v           | 233         | th       |  249 |
| A /1010      | I 138        | L              | 154            | x          | 170  | a            | 186                    | 2N 202                 |              | Vv             | 218         | +           | 234         | Kk       |  250 |
| Biol         |              | > 139          | 155            | 7          |      |              | Fe 187                 | 203                    |              |                | oe          |             | 235         |          |  251 |
| C &#124;1100 | I            | rn             |                |            | 171  | n>           |                        |                        | en           |                | 219 ee      |             |             | See      |      |
|              | 140          |                | 156            |            |      | 172          | 188                    |                        | 204          |                | 220         |             | 236         | XK       |  252 |
| D /1101      | I 141        | \              | 157            | 2          |      | 173          | 189                    | “                      | 205          | Y              | 221         | e)          |             |          |      |
| E i0         | fl 142       |                | \_&#124;3 158  |            |      | _&#124;* 174 | 190                    | &#124;                 | 206          |                | 222         | 7           |             |          |      |
|              | Fou?”        |                |                | ?          |      |              |                        |                        | y_&#124;y_d’ |                |             | \           |             |          |      |
|              |              | 143            | 159            |            | 175  |              | 191                    |                        | 207          |                | 223         |             |             |          |      |

<!-- page 75 -->

## C.3  Page 2 (PC850: Multilingual)

| [XaH&#124;          | &#124; NIA     |             |             |                  |                  |             |             |             |                           |                           |           |           | TITT &#124; OTTT   | TITT &#124; OTTT   |      |
|---------------------|----------------|-------------|-------------|------------------|------------------|-------------|-------------|-------------|---------------------------|---------------------------|-----------|-----------|--------------------|--------------------|------|
|                     | 0000           | &#124; OOOT | &#124; OOOT | 8-H) &#124; TOOT | 8-H) &#124; TOOT | &#124; OTOT | &#124; OTOT | &#124; TTOT | @ &#124; TOTT &#124; OOTT | @ &#124; TOTT &#124; OOTT | —o &#124; | —o &#124; |                    |                    |      |
| 0                   |                | 8é1 9       |             |                  | vol              |             |             | 361         |                           | 806                       |           | VES       |                    |                    | Ore  |
| T                   | n &#124; 1000; | 621         | 2           | SPT              | Tt               | TOT         |             | 86T —_      | Ga                        | 606                       | g         | ad        |                    | +                  | TVS  |
| O100) @             | cS)            | OeT         | W           | OFT              | 9                | COL         | _           | v6T         | a                         | OTS                       | Qo        | 966       |                    | =                  | Ka44 |
| €                   | eB T100&#124;  | T&T         | Q           | LbT              | n                | 891         | 6LT         | S6T         | a                         | 116                       | Q         | LOS       |                    | %                  | i 44 |
| F                   | e OOTO&#124;   | 6st         | fe)         | 8hI              | u                | POL         | O8T __      | 96T         | a                         | GIG                       | Q         | 866       | b                  |                    | 1444 |
| 8                   | ge fro         | betes &     |             | 6h1 Ng)          |                  | got         | 181 +       | L6T         | to                        | 81d                       | Oo        | 666       |                    | §                  | StS  |
|                     |                | vel         |             | OST              | A                | 99T         | S8T 2       | 86T Se      |                           | ia%4                      |           | 083 ue    |                    |                    | 906  |
| &#124;ITTO&#124;) 2 | §              | géT         | n           | TST              | 5                | LOT         | €8T         | 66T Vv      | I                         | STS                       | d         | T&G       | «                  |                    | Lv]  |
| O0OT) 8             | 2)             | 98T         | &           | @ST              |                  | 891         | PBI         | 006 5       | I                         | 916                       | d         | SES       | °                  |                    | 806  |
| TOOT OOT&#124; 6    | r)             | LET         | Q           | SgT              | ®                | 69T         | SST         | TOS         | &#124;                    | L1@                       | fal       | £83       |                    |                    | 64%  |
| OTOT) V             | 8              | 8st         | Qo          | vot              | L                | OLT         | 98T         | 0G          | &#124;                    | 816                       | no        | VES       |                    |                    | 096  |
| IlOL @              | I              | 68T         | 8           | Sgt              | g                | TLL         | L8T         | £06         | a                         | 613                       | Q         | S8o       |                    | I                  | TSS  |
| OOTT) 0             | It +           | OFT         | Aa          | 9sT              | Pp ‘7            | @LT         | 881         | 06          | =                         | 086                       | 4 >       | 986       |                    | e                  | 6&6  |
|                     |                | ThT         |             | L&T              |                  | eLt         | 68T         | S0Z         |                           | 18S                       |           | LES       |                    |                    | ego  |
| A                   | Vv OLIL&#124;  | GPT         | x           | 8gT              | »                | bLI         | O6T         | 906 —L      | I                         | aaa                       | _         | 88S       |                    | Py                 | iA(4 |
| A                   | Vv TTT)        | ehT         | £           | 6ST              | «                | GLI         | T6T         | L0G re]     | =                         | 86s                       | .         | 686       |                    | ds                 | Sos  |

<!-- page 76 -->

## C.4  Page 3 (PC860: Portuguese)

|                    | &#124; XdH    | 8           | 8           | 6           | 6           | Vv          | Vv          | tsi         | d 0)        | a           |             | A           | A     |
|--------------------|---------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------|
| XaH                | &#124; NIA    | &#124; OOOT | &#124; OOOT | &#124; TOOT | &#124; TOOT | &#124; OTOL | &#124; OTOL | &#124; TTOT | &#124; OOTT | &#124; TOTT | &#124; OTTT | &#124; OTTT | TITT  |
| 0                  | 4 0000,       | 831         | a           |             |             |             |             | S61 _       | 806         |             | 06S =D      |             | Ore   |
|                    |               | 631         |             |             |             |             |             | 86T         | 606         |             | 96S         |             | TvS   |
| 0100 @             |               | Ost         | a9          |             |             |             |             | P6T         | nk          |             | 986         | =           | L444  |
| €                  | e TIOO)       | T&T         | °           | LPT         | n           | e9T         | 6LT         | S6T 4       | aK          | uw          | LOG         | S           | 8%    |
| OOTO&#124; F       | e             | @8L         | fe)         | ias         | u           | v9l L       | O8T         | 96T __      | ai =        | z           | 886         | J           | acd   |
| TOTO)              |               | €&8T ee     |             | 6rI         |             | got LN      | 181         | L61T        | 816         |             | 636 ro      |             | Sho   |
|                    |               | eT          |             | OST         |             | 99T         | 68T         | 86T         | aid         |             | 083         |             | 90%   |
| &#124;ITTO&#124; 2 | §             | SéT         | n           | IST         | re}         | LOT I       | €8T         | 66T         | GTZ         | 1           | 183         | =           | Lv]   |
| OOOT&#124;; 8      | Q             | 9&1         | I           | 6ST         | ?           | 891 LL      | vet         | 00é         | 916         | @           | (S54        | °           | 84%   |
| T00T 6             | g             | LET         |             | 8ST oo      |             | 691         | Sst         | 102         | L16         | 9           | £8          | .           | 64%   |
| O10T Vv            | @             | 8&8T        | _fg>        | VST         |             | OLT         | 98T         | 0G he       | 813         | oD          | VES         |             | 0S¢   |
|                    |               | 68T         |             | SST         |             | TLT         | L8T         | 802         | 616         |             | GSS         |             | TS@   |
| TT 00Il Oo         | Q             | OFT         | >           | 9ST         | :           | GLI         | 88T         | 406         | 0&6 8       |             | 986 0°      |             | GSS   |
| loll a             |               | TL og       |             | L&T         | 1           | SLI         | 681         | 902         | 1% on       |             | LEB         | or          | Lssi4 |
| A                  | Vv OTIT&#124; | das         | ‘1d         | sgt         | >           | bLI =       | O6T         | 903         | (4a4 I      |             | 883         | :           | Lag   |
| A                  | Vv            |             | re)         |             | «           | L           |             | =>          | =           |             |             | dS          | go    |
|                    | ITTT&#124;    | StI         |             | 6ST         |             | GLI         | T6T         | L03         | 836         |             | 683         |             |       |

<!-- page 77 -->

## C.5  Page 4 (PC863: Canadian-French)

|                    | &#124; XdH    | 8                | 6                | 6           | Vv          | Vv           | &#124; tsi   | &#124; tsi   | &#124; da ie)   | a           | a           |             | fc   |
|--------------------|---------------|------------------|------------------|-------------|-------------|--------------|--------------|--------------|-----------------|-------------|-------------|-------------|------|
| XaH                | &#124; NIA    | TOOT &#124; OOOT | TOOT &#124; OOOT | OTOT &#124; | OTOT &#124; | TLTOT &#124; | TLTOT &#124; | OOTT         | &#124; TOTT     | &#124; TOTT | &#124; OTTT | &#124; OTTT | TITT |
| 0                  | 5 &#124;0000) | 861              | a                |             |             |              |              | B61          | 806             |             | VS D        | =           | Ore  |
|                    |               | 681              |                  |             |             |              |              | 86T          | 606             |             | a4          |             | 1544 |
| 0100) 2            | g             | OsT              | aq               |             |             |              |              | v6T          | 14              | I           | 96          | =           | 444  |
| 1100 &             | zg            | T&T              | 9                | LbT         |             | 89T          | 6LT          | S6T          | 113             | au          | Les         | S           | 8ve  |
|                    |               | CsI              |                  | 8rT         |             | vor          | O8t          | 96T          | a4              |             | 866         |             | 1443 |
| T0lo0 ¢            |               | eT               | I,               | 6rL         |             | got LD       | T8T          | L6T          | €16             |             | 666 fo      |             | StG  |
| BOTT 9             |               | vet              |                  | OST         | ©           | 99T          | S8T          | 86T          | iaX4            |             | 08% ad      |             | 90%  |
| &#124;TTTO&#124; 2 | 5             | get              | n                | TST         |             | LOT          | 81           | 66T          | STZ             | 1           | T&S         | ~           | Lv]  |
| 000T&#124; 8       | @             | 98T              | a                | GST         | 891         | >            | P81          | 006          | 916             | CO          | (S574       | .~          | 846  |
| 1001 6             | @             | LET              | O                | €ST         | 7           | 69T          | gst          | 106          | LI@             | 9           | 88S         | .           | 676  |
| O10l Vv            | @             | 8éT              |                  | vat >a)     |             | OLT          | 98T          | 606          | 8IZ 5           |             | ves         |             | ose  |
| TTOT a             | Tt s          | 6&T              | d                | SST         | zw $        | TLT _        | L8T          | £06          | 613 &#124;      | 9           | G&S         |             | TSS  |
| OOTT) DO           | I             | OFT              | ¥                | 9ST         | z           | LT _         | 88T          | 0G           | 066 =           | co          | 986         | a           | 6&6  |
| IOIl a             | =             | THT              | Qu               | LST         | z           | LT i         | 68T          | 906          | 186 &#124;      | @           | LEG         | z           | tsi  |
| a                  | OTTT&#124;    | gas aly          | 8ST              |             | >           | PLT =        | O6T          | 906          | 66S I           |             | 88          | 1           | Ss   |
| a                  | g ttt         |                  |                  |             |             |              |              | L0é          | £66 Ulm         |             | 686         | dg;         | gce  |
|                    |               | €FT              | §                | 6ST         | «           | LT LT        | T6T          |              |                 |             |             |             |      |

<!-- page 78 -->

## C.6  Page 5 (PC865: Nordic)

<!-- image -->

|    | XadH                | 8       | 6                  | 6                  | Vv          | Vv          | a           | a           | a ie)        | a           |             | a    |
|----|---------------------|---------|--------------------|--------------------|-------------|-------------|-------------|-------------|--------------|-------------|-------------|------|
| XH | &#124; NIA          | OOOT    | &#124; TOOT &#124; | &#124; TOOT &#124; | &#124; OTOT | &#124; OTOT | &#124; TLOT | &#124; TLOT | &#124; OOTT  | &#124; TOTT | &#124; OLTT | TTTT |
| 0  | &#124;0000)         | 821 %   | a                  | PL                 | eB          |             |             | 361 _       | 806 D        | 74          | =           | 0%   |
| T  | n ToOoO)            | 621     | 2                  | pT                 | I           |             |             | 61 __       | 606 g ao     | Efad        | +           | TW   |
| @  | a &#124;0100&#124;  | Ost     | w                  | 9vT                | 0           |             |             | ver         | o1z I        | 98%         | =           | (ar  |
| €  | z T100&#124;        | TeT     | 9                  | LPT                | n           | e9T         | 6LI         | 61 4        | 11Z u        | a4          | s           | 74   |
| &  | B 0010)             | El      |                    | SPI ug)            |             | v9I         | ost         | 961 —       | at <> 4,     | 866         | J           | VG   |
| ¢  | e TIO]              | eer     | 9                  | 651                | N           | 91          | T81         | L6T         | e1z o        | 622         | r           | ove  |
| 9  | B OTTO!             | vel     | n                  | Ost                | B           | 991         | 281         | 861         | v1Z d        | (34         | +           | 99%  |
| 2  | 45 &#124;TTTO&#124; | eT      | n                  | IST                | 5           | LOT         | est         | 66T         | td 1         | its         | =           | LY   |
| 8  | g &#124;O00T&#124;  | ger     | &                  | @gt                | ?           | 891         | ici         | 00%         | 918 ®        | (aad °      |             | Eiz4 |
| 6  | a T00T              | 181     | Pay                | oT                 | 7           | 691         | 81          | 102         | LIB 9        | ez          | .           | Giz4 |
| Vv | 9 OL0T              | sel     |                    | a1 >a)             |             | OLT         | 981         | 20% _       | gIz 5        | ves         |             | 092  |
| a  | ror I               | 68]     | 2                  | oT                 | g           | TLI         | 181         | £02         | 61Z g &#124; | 4           |             | 19%  |
| 9  | y 0OIT              | OFT     | ¥                  | 9gT                | g           | BLT         | 81          | 403         | 086 of       | 98%         | a}          | a4   |
|    | qt T0Il             | ical    | g                  | LST                | '           | ELT         | 681         | 90% 1       | ita o        | 18%         | ;           | 14   |
|    | Vv OTIT&#124;       | aaa     | 1d                 | a1                 | >           | BLT         | O61         | 902         | [444 I       | 88s         | :           | $92  |
| a  |                     | oUs)CUY |                    |                    | on          |             |             |             | Ul om        |             | gg          | 99%  |
|    | rt                  | ery     |                    | 691                |             | LT          | T6T         | 106         | a4           | 68%         |             |      |

<!-- page 79 -->

## C.7  Page 16 (WPC1252) (TM-T88III only)

| &#124;   | &#124; XHH   | 8           | 8           |             |             | >ai)qaqso0+44qsvié6   | >ai)qaqso0+44qsvié6   |             |             |                 |             |               |             |             | qd          | qd   |
|----------|--------------|-------------|-------------|-------------|-------------|-----------------------|-----------------------|-------------|-------------|-----------------|-------------|---------------|-------------|-------------|-------------|------|
| XAH      | &#124; NI    | &#124; COOL | &#124; COOL | &#124; TOOT | &#124; TOOT | &#124; OTOT           | &#124; OTOT           | &#124; TIOT | &#124; TIOT | &#124; OOTT     | &#124; OOTT | &#124; TOLL   | &#124; TOLL | &#124; OLTT | &#124; OLTT | IIIT |
| 9        | 000          | 8ar g       | dS          |             | vPT ds;     | O9T                   | °                     | QLT         | Vv          | 61              |             | a             | 802 RB      | VES         | Q           | OVS  |
|          | S000         | 62T         |             | StT         |             |                       | T9T                   | LLT         |             | e6T             |             | 606           |             | SZo ue      |             | Tho  |
| @        | 0100)        | O&sT «      |             | OPT         | $           | COT                   |                       | 8LT         |             | v6T l(uolUvy!C; |             | O13           |             | 926         | ee          | a44  |
| 8        | 00           | T&T £       | 4           | LPT         | fF          | 89T                   |                       | 6LT v¢      |             | G6T             | oO          | TI’           | 8           | LOG         | 9           | ers  |
| *        | 0010)        | 8T «        | “           | Srl         | 4           | Vv9T                  | ©                     | O8T         | v of        | 96T             | ol          | raid          | el -        | 836         | of vv       | 444  |
| G        | TOTO         | 8éT         |             | 67T         | x           | GOT                   | d                     | T8T         | y           | L6T             | Q           | €1Z           | B           | 626         | °           | Gh   |
| 9        | 4/0110       | VET         | _~          | OST         |             | 99T                   | 4b                    | OST         | #&#124;     | 86T             |             | lai #&#124;-o |             | 083         | of          | 946  |
|          | TO)          | SéT jy      |             | TST         | §           | LOT                   |                       | €8T         | 5           | 66T             | x           | GTS           | 5           | T&S         | +           | LVS  |
| 8        | ooor         | 9ST         |             | GST         |             | s9oT                  | .                     | HST         | a           | 002             | el          | 916           | el          | BES         | of          | 8hS  |
| 6        | ong TOOL     | LET         | a           | €cT         |             | 69T                   | ;                     | S8T         |             | 106 ala         |             | LIG           | 9}          |             | $86 al      | 646  |
| ov       | olor         | S&T g       | 5           | VST         | .           | OLT                   | :                     | 98T         |             | 606 ala         |             | 816           |             | VES nel     |             | 0g6  |
| a        | &#124; tor)  | 68T »       | «           | ScT         | »           | TLT                   | «                     | L8T         | a           | £02             | Q           | 616           | Q           | G&o         | n           | 193  |
|          | OTE          | OFT mm      |             | 9ST         |             | GLT                   |                       | 88T         |             | 90% a           |             | 026           |             | Boot        | 986         | CGS  |
|          |              | TvT         |             | L&T         |             | €LT                   |                       | 68T         |             | S06             |             | 16S           |             | LEG         |             | Soo  |
|          | z ot         | aaa         | Zz          | 8ST         | 3           |                       | PLT ve                | O6T         | {           | 90%             | d           |               | BEG ;       | 886         | q           | AA   |
|          |              | isa         |             | 6ST         |             | SLT                   |                       | T6T         |             | L0G             |             | 866           |             | 686         |             | goo  |

<!-- page 80 -->

## C.8  Page 17 (PC866: Cyrillic #2) (TM-T88III only)

<!-- image -->

|     | HEX&#124;   | 8           | 8           | 9           | 9           | A &#124;   | B           | c &#124;                 | c &#124;   | D                         | D                         | E           | E           | F     |    F |
|-----|-------------|-------------|-------------|-------------|-------------|------------|-------------|--------------------------|------------|---------------------------|---------------------------|-------------|-------------|-------|------|
| HEX | BIN &#124;  | 1000 &#124; | 1000 &#124; | 1001 &#124; | 1001 &#124; | 1010       | &#124; 1011 | 1100                     | 1100       | &#124; &#124; 1101 &#124; | &#124; &#124; 1101 &#124; | 1110 &#124; | 1110 &#124; | 1111  | 1111 |
| 0   | oo          | 4 128       | 4 128       | Pa          | Pa          |            |             | &#124;=                  | &#124;=    |                           |                           | }p—lE 224   | }p—lE 224   | 240   |  240 |
| 1   | &#124; 0001 | © 129       | Cc          | 145         | 6           | 161        | =... 177    | 193                      | :          | 209                       | c                         | 225         | e           |       |  241 |
| 2   | oi          | BT 130      |             | 146         | _B          | 162        | 178         | TH 194                   |            | T_T, 210                  |                           | 226         | __6         |       |  242 |
| 3   | om          | PY 131      |             | 147         | oF          | i 163      | ti 179      | 195                      |            | rity 211                  |                           | 227         | 6           |       |  243 |
| 4   | (owo        | AP 132      |             | 148         |             | 164        | 180         | 196                      |            | Rag 212                   |                           | 228         |             |       |  244 |
|     |             | 133         |             | 149         |             | 165        | 181         | 197                      |            | 213                       |                           | 229         |             |       |  245 |
|     |             | 134         |             | 150         |             | 166        | 182         | 198                      |            | 214                       |                           | 230         |             |       |  246 |
| 7   | ou          | 8 — 135     |             | 43 151      |             | 167        | 9 183       | ri 199                   |            | tia 215                   |                           | 231         |             | _y¥   |  247 |
| 8   | 1000 U      | 136         | an          | 152         | u           | 168        | nL 184      | Ld 200                   | wT         | 216                       | ll                        | 232         | °           |       |  248 |
| 9   | 7 101 4     | 137         | Ul          | 153         | i           | ou: 169    | 185         | 201                      | By =&#124; | 217                       | I                         | 233         | ,           |       |  249 |
| A   | 11          | Kb 138      |             | 154         | __*         | 170        | 186         | —&#124; 202              |            | 218                       | [&#124;b                  | 234         |             |       |  250 |
| B   | 101         | 2 139       | BI__        | 155         | a4          | 171        | 187         | _ 203                    |            | Mou 219                   |                           | 235         |             | v     |  251 |
| c   | i009        | 140         | Mb          | 156         | __™M        | 172        | 188         | Jl__&#124;™/_&#124;b 204 |            | 220                       |                           | 236         |             | ™     |  252 |
| p   | uo          | #9 141      |             | _ 157       | 4           | 178        | 189         | 205                      | i          | 221                       | a                         | 237         |             | a     |  253 |
| E   | ino         | 2 142       | 10          | 158         | °           | 174        | = 190       | 206                      |            | a i 222                   | 0                         | 238         |             | 7     |  254 |
|     | Fouu        | MA 148      |             | 159         | om          | 175        | 191         | Ca 207                   |            | 223                       | a                         | 239         |             | __/SP |  255 |

<!-- page 81 -->

## C.9  Page 18 (PC852: Latin2) (TM-T88III only)

|            | XaH        | 8           | 8           | 6           | Vv          | Vv          | ad          | ad          | a @)        |             |             | a           | a           | d    |
|------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|------|
| &#124; XHH | &#124; NIA | &#124; OOOT | &#124; OOOT | &#124; TOOT | &#124; OTOT | &#124; OTOT | &#124; TTOT | &#124; TTOT | &#124; OOTT | &#124; TOTL | &#124; TOTL | &#124; OLTT | &#124; OLTT | TTIT |
| 0          | 0000)      | @           | 8ZT         | vrL         | Bq          | O9T         | QLT         | 661         |             |             | 806 oP      | VES         | 7           | 44   |
| I          | To00       | 62T oe      |             | StT ns      |             | TOT         | LLT         | 86T         | a@          | 602         | g°          | Sto         | “           | Ths  |
|            | TO)        | O&T         |             | 9FT 9       |             | BOT         | BLT         | v6r Gt      |             | Os          |             | 926 ‘Or     |             | GVS  |
| &          | TO)        | T&T ge      | 9           | LPT         | a           | 89T         | 6LT pp      | S6T 4       | @>          | TIé         | N>          | Les         | ~           | 8ho  |
|            | TF         | SET         | eB          | rT          |             | pOT         | O8T         | 96T POE     |             | raid        | UD          | 826         | ~           | 44   |
|            |            | S&T         |             | 6FT         |             | SOT         | T8T         | L6T         |             | 816         |             | 626         |             | StS  |
| 9          | Oro        | pet 2       | TF          | Ost Z       | 99T         | vy          | @8T         | 86T Vo      |             | Ie $I       |             | 0&@         | =           | 906  |
|            |            | SéT         |             | TST         | LOT         |             | €8T         | 66T         |             | GIS         |             | T&%         |             | LV]  |
| 8          | {0001      | 98T         | $           | SST         | 891 a       | g           | vel         | 006 a>      |             | 91%         | UW          | GES         | °           | Bho  |
| TOOT 6     | 2          | LET         | Q           | 3 €ST       | 69T         |             | S8T         | 108 A       | &#124;      | LI@         | Oo;         | 88s         |             | 606  |
| Vv         | OTOT       | S&T O       | a           | VST         | OLT         |             | 98T :       | G06         | ny          | 813         | a           | VES         |             | 0Sd  |
|            |            | 6ET         |             | SST         |             | TLT         | L8T         | 806         |             | 616         |             | G&S         |             | 196  |
| 10)        | OOTT       | OVT I       | 4           | 9ST         | re)         | GLT oo      | 88T         | vOG ;       | =           | 026         | &           | 986         | WU          | 696  |
| or         |            | TPT Eg      |             | LST         |             | SLT 8       | 68T         | S0Z         | GL          | 166         |             | LEG PAD     |             | 896  |
|            | ot         | aan y       | x           | 8gT         | DLT »       | Z           | O6T         | 906 as      |             |             | 6E6 j       | 88S         | =           | VGS  |
| a          | TE         | SPT QQ      |             | 6ST         | SLT CK      |             | T6T         | L106        | mm          | 866         |             | 6&6         | So          | se   |

<!-- page 82 -->

## C.10  Page 19 (PC858: Euro)

<!-- image -->

|               | XadH            | 8               | 8                  | 6                  | 6           | a Vv        | a Vv   | &#124; 0   | &#124; 0    | a           | a           | a           | a           |             | A     |
|---------------|-----------------|-----------------|--------------------|--------------------|-------------|-------------|--------|------------|-------------|-------------|-------------|-------------|-------------|-------------|-------|
| XaH           | OOOT &#124; NIA | OOOT &#124; NIA | &#124; TOOT &#124; | &#124; TOOT &#124; | &#124; OTOT | &#124; OTOT | TTOT   | TTOT       | &#124; OOTT | &#124; OOTT | &#124; TOTT | &#124; TOTT | &#124; OLTT | &#124; OLTT | TIIT  |
| 0             | 0000}           |                 |                    |                    | G           |             |        |            |             | Q           | 806         | fe)         | VES         |             | Ove — |
| T             | n &#124;1000)   |                 |                    |                    |             |             |        |            |             | a           | 606         | g           | SBS         | -           | 4     |
| Z             | OT00&#124;      |                 |                    |                    |             |             |        |            |             | q           | Ole         | oO          | 966         | =           | AKA   |
| TT00} €       |                 |                 |                    |                    |             |             |        |            |             | cl ci       | I1é         | Q           | Les         | e 4         | 8s    |
| F             | e OOO)          | sl              | fe)                | SPT                | u           | POT         | L      | O8T __     | 96T         | a           | rand        | Q           | 866         | b           | VIG   |
|               | eres            | est             |                    | 6¢T Neg            |             | SOT         | yo     | T8L        | L6T +       | BS          | 1d          | 9           | 636         | gs          | SHS   |
| 9             | OTTO            | vel Ug          |                    | OST                | le          | 99T         |        | o8T ely    | 86T         |             | Ie dr       |             | 083         | +/          | 906   |
|               |                 | géT             |                    | TST                |             | LOT         |        | est        | 66T         |             | STS         |             | T&S         |             | Lvs   |
| 8             | g 000T'         | 9&T             |                    | GST                | ?           | B9T         | eo     | PBL        | 006 4       | tT          | 9T@         | dad         | 6ES         | o           | 8hS   |
| 6             | a &#124;TOOT    | LET             |                    | est                | ®@          | 69T         | LL     | Sst        | 106 =&#124; | r           | LIB         | o           | ttrd        |             | 6F%   |
| V             | 8 OTOT)         | 8st             | al                 | VST                | LL          | OLT         |        | 98T        | 606         | &#124;      | 8Ie         | n           | ves         |             | ose   |
|               | IlOl I          | 68T             |                    | ScT                |             | TLT Lg      |        | L8T        | £06 4       | bp          | 616         | a.          | S&o         | ,           | TSé   |
| &#124;OOTT) 0 | t gL            | OFT             | ¥                  | 9cT                | % y         | GLT         | _      | 881        | v0G         | =           | 066         | & 7         | 98%         | &           | 6So   |
| a             | rf TOIT;        | Tel             | @                  | LST                | !           | LT          | >      | 68T        | 806 _       |             | T6s         | &           | LEG         | z           | 893   |
| ©             | Vv OTIT&#124;   | aa5             | x                  | 8ST                | >           | PLT         | &      | O6T        | 906         | I           | 444         | _           | 88S         | 1           | A14   |
|               | It yiltda       | evT             | 5s                 | 6ST                | «           | SLT         |        |            | oo          | m           |             |             | 683         | gS.         | SSS   |
|               |                 |                 |                    |                    |             |             | F      | T6L        | L03         |             | 866         |             |             |             |       |

<!-- page 83 -->

## C.11  Page 255 (Blank Page)

|                  |          | A            |
|------------------|----------|--------------|
| 1000             | 1001     | 1010         |
| &#124; 128&#124; | SP [144] | SP           |
|                  |          | [160 SP [161 |
|                  |          | SP {162      |
|                  |          | 163          |
|                  |          | 164          |
|                  |          | 165          |

UD: undefined

<!-- page 84 -->

## C.12  International Character Set

|               | ASCII codes (base 16)   | ASCII codes (base 16)   | ASCII codes (base 16)   | ASCII codes (base 16)   | ASCII codes (base 16)   | ASCII codes (base 16)   | ASCII codes (base 16)   | ASCII codes (base 16)   | ASCII codes (base 16)   | ASCII codes (base 16)   | ASCII codes (base 16)   | ASCII codes (base 16)   |
|---------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| America       |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| France        |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Germany       |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| UK            |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Denmark I     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Sweden        |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Italy         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Spain I       |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Japan         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Norway        |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Denmark II    |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Spain II      |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Latin America |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
| Korea         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |

<!-- page 85 -->

## Appendix D

## TM-T88II/TM-88III Comparison Table

|                                                         | TM-T88III                                                                                                                                                                                                                                                                                                                                                     | TM-T88II                                   |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| 1. High-speed print mode                                | Approx. 150 mm/s {5.91"/s} (4.72") maximum                                                                                                                                                                                                                                                                                                                    | Approx. 120 mm/s {4.72"/s} (4.72") maximum |
| 2. High-speed power consumption mode                    | Average approx. 1.8 A                                                                                                                                                                                                                                                                                                                                         | Average approx. 1.7 A                      |
| 3. Serial interface selectable baud rates               | 4800, 9600, 19200, 38400, (2400 discontinued; 38400 added). 38400 selected by setting DIP SW1-7 and 1-8 to ON.                                                                                                                                                                                                                                                | 2400, 4800, 9600, 19200                    |
| 4. Conditions for canceling receive buffer BUSY state * | Set on DIP SW2-5 *                                                                                                                                                                                                                                                                                                                                            | Cannot be changed                          |
| 5. Supported character sets (extended graphics) *       | 11 pages including WPC 1252, PC866 [Cyrillic #2], PC852 [Latin2])                                                                                                                                                                                                                                                                                             | 8 pages                                    |
| 6. Driver (EPSON OPOS ADK, Advanced Printer Driver )    | Also can be operated by the TM-T88II driver. Functions, however, are restricted as follows: • Some baud rates cannot be used in serial communications (38400 bps, 2400 bps). Note: The driver cannot set a 38400 bps baud rate. Selecting a 2400 bps baud rate with the driver causes garbled characters (the printer does not support a 2400 bps baud rate). | -                                          |

<!-- page 86 -->



<!-- page 87 -->



<!-- page 88 -->

## EPSON

SEIKO EPSON CORPORATION Printed in Japan
