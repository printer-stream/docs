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
