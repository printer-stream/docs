<!-- image -->

The method of sending data in standard raster graphics compressed mode is slightly more complicated. However, the amount of data necessary to print graphics may be greatly reduced. When possible, you should use one of the available compressed modes. For information on extended raster graphics compressed modes, see 'Extended raster graphics (ESC . 2).'

Data is organized as counter bytes followed by data bytes. Two types of counters can be used: repeat counters and data-length counters.

Repeat counters specify the number of times (minus 1) to repeat the following single byte of data.

Data-length counters specify the number of bytes (minus 1) of print data following the counter. This data is printed only once.

If the counter is positive, it is treated as a data-length counter.

```
0 ≤ (data-length counter) ≤ 127
```

The data-length counter is calculated as follows:

(data-length counter) = (number of data bytes to follow) - 1

If the counter is negative (as determined by two's complement), it is treated as a repeat counter.

```
-1 ≤ (repeat counter) ≤ -127
```

The repeat counter is calculated as follows:

```
(repeat counter) = 256 - (number of times to repeat data) + 1
```

During compressed mode, the first byte of data must be a counter. After receiving a counter, the printer handles data as follows:

If a repeat counter is received, the printer repeats the following byte of data the specified number of times. The byte following the data byte is treated as a counter.

Repeats this one byte of data 11 times

↓

129

ESC

.

10

8

48

0

-10

↑

15

↑

First counter byte Second counter byte

. . .
