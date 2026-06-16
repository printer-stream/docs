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
