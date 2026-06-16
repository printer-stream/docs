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
