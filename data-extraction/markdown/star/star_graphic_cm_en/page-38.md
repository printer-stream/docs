<!-- image -->

Rev. 2.31

## 3-3) USB Interface Related Command Details

The following command is a command to control the function of the USB interface.

- ---Specification(1) ---

## ESC # # W n , d1 d2 ．．． dk LF NUL

## [Name] [Code]

Register USB serial number

ASCII ESC # # W n , d1 d2 ．．． dk LF NUL

Hex 1B 23 23 57 n 2C d1 d2 ．．． dk LF NUL

Decimal 27 35 35 87 n 44 d1 d2 ．．． dk LF NUL

## [Defined Area]  n = 56 ( '8')

When registering serial number

: 48 ≦ d ≦ 57 ('0' ≦ d ≦ '9'), 65 ≦ d ≦ 90 ('A' ≦ d ≦ 'Z')

When clearing serial number

: d = 63 ('?') k = n

## [Initial Value] [Function]

---

Executes USB serial number registration.

After registration, the printer executes a soft reset, but at this time disconnect/reconnect of the USB-I/F is not performed, and the serial number before the value is changed is maintained. In order to enable the registered serial number, it is necessary to power on again. When initializing the serial number, insert "?" for all serial number data.

- ---Specification(2) ---

## ESC # # W n , d1 d2 ．．． dk LF NUL

【 Name 】 Register USB serial number

【 Code 】 ASCII ESC # # W n , d1 d2 ．．． dk LF  NUL

Hex 1B 23 23 57 n 2C d1 d2 ．．． dk LF  NUL

Decimal 27 35 35 87 n 44 d1 d2 ．．． dk LF  NUL

## 【 Defined Area 】

When registering serial number(8 digits) ：

n = 56 ( '8' ）

When registering serial number(16 digits) ：

n = 16

When registering serial number(8, 16 digits)

：

48 ≦ d ≦ 57 ('0' ≦ d ≦ '9') 、 65 ≦ d ≦ 90 （ 'A' ≦ d ≦ 'Z' ）

When initializing the serial number ：

d = 63 ('?' ） k = n

## [Initial Value] ---

【 Function 】 Executes registration of 8 digits USB serial number or 16 digits one

After registration, the printer executes a soft reset, but at this time disconnect/reconnect of the USB-I/F is not performed, and the serial number before the value is changed is maintained. In order to enable the registered serial number, it is necessary to power on again.

When initializing the serial number, insert "?" for all serial number data.

--------------------------------------------------------------------------------------
