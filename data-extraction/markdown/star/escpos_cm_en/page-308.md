<!-- image -->

## 6-8 Appendix	8 Explanation	of	Print	Startup	Control	Starting	Printing	When	Set	to	Page	Units

When print startup control is set to page units, printing starts when the image buffer length is full or the following commands are run.

If the following commands are not received, start printing after a 1-second timeout.

For details on image buffer length and how to set print startup control, see the product specifications manual.

## Print starting trigger

- Cutter command:

&lt;GS&gt; V n, &lt;GS&gt; V m n

- BM detection command:

&lt;GS&gt; &lt;FF&gt;, &lt;FF&gt; (When BM is valid)

- Print startup command:

&lt;ESC&gt;&lt;GS&gt; g 0 m n
