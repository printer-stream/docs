## Adescription of the instruction's parameters follows:

- &lt;DEC&gt; delay. Thedelayimplementedis ((parame­

The first parameter is optional. If present, it is the intercharacter ter X 1.1875)mod65 536)/ 1.2milliseconds. The parameter range is 0 to 54 612. If parameters follow, the semicolon must be included, even if this decimal parameter is omitted.

- &lt;ASC&gt; . . . &lt;ASC&gt; This parameter is optional. If present, it is a list of the decimal equivalents of 1 to 10 ASCII characters in the range 0 to 127.For Xon-Xoff handshake mode, it specifies the Xoff trigger character(s). Forenquire/ acknowledge handshake mode, it specifies the imme­ diate response string. Semicolonsmust separate each parameter in the list.

## EXAMPLES

For Xon-XoffHandshake

- . N;19: Sets the Xoff trigger character to DC3. There will be no intercharacter delay, since the first parameter is defaulted to zero by the semicolon. no

## For Enquire/Acknowledge Handshake

The examples given here include all handshaking instructions. In addition to illustrating the use of intercharacter delays and immediate response strings set by ESC . N, they are designed to clarify the difference between handshake mode 1 and'mode 2 and give some insight into why certain values are logical choices for some parameters. Note the CHR$ function is used to send the escape character. I

```
10 DIM DUT$(80) :30 PRINTCHR$(2?);".M0;B3;O;13:";CHR$(2?);".N5:" so PRINT CHR$(2?);".H80;1B;4&3:" so 0UT$="IN;SF'1;PR500,500;" :«-sosus 100 l00 PRINT CHR$(18): INPUT 2: PRINT DUT$: RETURN The following parameters are set in lines 40 and 50: turnaround delay = 0, output trigger character = ? (decimal equivalent 63), no echoterminate character,
```

## 10-36 RS-232-C/CCITT V.24INTERFACING
