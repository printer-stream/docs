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
