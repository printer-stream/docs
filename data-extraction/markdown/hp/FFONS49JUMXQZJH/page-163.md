- 0 Enquiry character (ESC . I or ESC . H command)
- 0 Acknowledgment string (ESC . I or ESC . H command)

In its simplest form, the data exchange looks like this:

ENQ/ACK Handshake Protocol Example 1

<!-- image -->

In a more complex form, the communication might look like the following example, where the two commands . M250;17;10;13: and . H100;5;6: have beensent to specifythe variables as: Gq

turnaround delay = 250 ms

outputtrigger character = ASCII character DC1 (decimal equiva­ lent 17)

echoterminate character = ASCII character LF (decimal equiva­ lent 10)

output terminator = ASCII character CR(decimal equivalent 13)

data block size = 100 bytes

enquiry character = ASCII character ENQ (decimal equivalent 5)

acknowledgment string = ASCII character ACK (decimal equiva­ lent 6)
