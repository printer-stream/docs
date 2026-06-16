## Unit Systems

There are two unit systems which can be used to define points in the plotting area: plotter units and user units. Plotter units are always the same size. The size of a user unit depends on the parameters of the SC instruction and the settings of the scaling points, P1 and P2.

## The Plotter Unit

The plotting area is divided into plotter units; one plotter unit equals 0.025 mm. There are approximately 40 plotter units per millimetre, or approximately 1000 plotter units per inch. One plotter unit is the smallest move the plotter can make. When the paper switch is set to A4, the plotting area contains 10900 plotter units in X and 7650 plotter units in Y. When the paper switch is set to us, the plotting area contains 10300 plotter units in X and 7650in Y.While the pen can only plot in the area mentioned above, parameters of plot commands be­ tween -32 768 and 32 767 plotter units are understood by the plotter. When plotting in plotter units, only integer values are used; parameters are truncated to integers. Refer to The Plot Absolute Instruction, PA,in Chapter 3.

At power on, upon front-panel reset, and whenever an IN command is sent to the plotter, the scaling point P1 is set to 250,279 plotter units and the scaling point P2 is set to 10 250, 7479plotter units. These settings are independent of the setting of the paper switch.

## User Units

The plotting area can also be scaled into user units. This is done with the scale instruction, SC, which assigns values to the scaling points P1 and P2. A user unit may be almost any size. The parameters of the SC instruction are truncated to integers between -32 768 and 32 767. Parameters of plot commands must also be in that range but may be decimal numbers with fractional parts. Decimal fractions are not trun­ cated; as a matter of fact, you can set the scaling points at 0,0 and 1,1 and all your data can be decimal fractions between 0 and 1. You can also use the plot relative instruction to plot to a point which, in user units, is beyond the range i32 768 as long as its location, expressed as plotter units, is in range. Refer to the plot instructions PA and PR in Chapter 3. Youwill probably use the SC instruction and user units for most plots.

## Setting the Scaling Points

Scaling points P1 and P2 can be set programmatically using the input P1 and P2 instruction, IP, as described in a following section. P1 and P2 can be set manually using front panel controls ENTER, P1,and P2.
