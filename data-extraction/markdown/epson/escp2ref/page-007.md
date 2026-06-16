Some command parameters may exceed 256, and require two bytes of data. These variables are listed with the subscripts L for low and H for high (for example, nL and nH, or mL and mH).

To determine the value of these two bytes, this manual uses the INT and MOD conventions. INT indicates the integer (or whole number) part of a number, while MOD indicates the remainder of a division operation.

For example, to break the value 520 into two bytes, use the following two equations:

<!-- image -->

INT simply deletes the fraction part of the number, and the value of nH is calculated as shown below.

<!-- image -->

MOD, on the other hand, results in the remainder of the division operation of the fraction part as shown below.

<!-- image -->
