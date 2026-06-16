## Xon-XoffHandshake

With the Xon-Xoffhandshake method, the plotter controls the data exchange sequence by telling the computer when it has room in its buffer for data and when to shut off the flow. The plotter uses buffer threshold indicators (an Xon trigger character and an Xoff trigger character) to prevent buffer overflow.

<!-- image -->

Xon-XoffThreshold Levels

As data is sent to the plotter by the computer, it is stored in the buffer and simultaneously acted on by the plotter. The preceding figure is representative of the way the Xon-Xoffhandshake works; the numbers represent the following:

1. Data enters the buffer faster than it can be acted on by the plotter, and the buffer starts to fill.
2. The plotter begins processing the input data faster than the computer sends it, and the buffer starts to empty.
3. The data enters the buffer at a faster rate than the plotter can process it. The amount of data stored in the buffer reaches the Xoff threshold level, at which point the plotter sends the Xoff trigger character stopping the flow of data from the computer.
4. Due to a finite delay between the time the plotter sends the Xoff trigger character and the time it takes the computer to react, a slight overshoot may occur. For this reason, the Xoffthreshold level should always be specified at least as large as the data block size or the
