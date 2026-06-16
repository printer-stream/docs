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
