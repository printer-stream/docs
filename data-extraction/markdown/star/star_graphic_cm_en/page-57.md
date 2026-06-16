<!-- image -->

Rev. 2.31

- USB -I/F related commands

| Class   | Command   | TSP100 U   | TSP100 PU   | TSP100 IIU   | TSP100 GT   | TSP100 LAN   | TSP100 IIIW   | TSP100 IIILAN   | TSP100 IIIBI   | TSP100 IIIU   |
|---------|-----------|------------|-------------|--------------|-------------|--------------|---------------|-----------------|----------------|---------------|
| USB-I/F | ESC##W    | (1)        | (1)         | (1)          | (1)         | No           | No            | No              | No             | (2)           |

● Print mode related comm ands

| Class             | Command   | TSP100 U   | TSP100 PU   | TSP100 IIU   | TSP100 GT   | TSP100 LAN   | TSP100 IIIW         | TSP100 IIILAN       | TSP100 IIIB   | TSP100 IIIU   |
|-------------------|-----------|------------|-------------|--------------|-------------|--------------|---------------------|---------------------|---------------|---------------|
| Select print mode | ESC RS C  | (1)        | (2)         | (1)          | (1)         | (1)          | Ver1.4 or later (1) | Ver1.3 or later (1) | (1)           | (1)           |
| Select print mode | ESC RS S  | No         | No          | No           | No          | No           | Ver1.4 or later     | Ver1.3 or later     | OK            | OK            |

● P rinter information related commands

| Class                        | Command    | TSP100 U   | TSP100 PU   | TSP100 IIU   | TSP100 GT   | TSP100 LAN   | TSP100 IIIW                               | TSP100 IIILAN                             | TSP100 IIIBI                              | TSP100 IIIU   |
|------------------------------|------------|------------|-------------|--------------|-------------|--------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|---------------|
| Register printer information | ESC GS ( S | No         | No          | No           | No          | No           | OK                                        | OK                                        | OK                                        | OK            |
| Send printer information     | ESC GS ) I | No         | No          | No           | No          | No           | Ver1.5 or earlier (1) Ver2.0 or later (2) | Ver1.5 or earlier (1) Ver2.0 or later (2) | Ver1.1 or earlier (1) Ver2.0 or later (2) | (2)           |
| Send printer information     | ESC # *    | No         | No          | No           | No          | No           | OK                                        | OK                                        | OK                                        | OK            |

● Customer display related Commands

| Class            | Command    | TSP100 U   | TSP100 PU   | TSP100 IIU   | TSP100 GT   | TSP100 LAN   | TSP100 IIIW   | TSP100 IIILAN   | TSP100 IIIBI   | TSP100 IIIU   |
|------------------|------------|------------|-------------|--------------|-------------|--------------|---------------|-----------------|----------------|---------------|
| Customer display | ESCGSB@    | No         | No          | No           | No          | No           | No            | No              | No             | OK            |
| Customer display | ESC RS B A | No         | No          | No           | No          | No           | No            | No              | No             | OK            |
| Customer display | ESC GS B B | No         | No          | No           | No          | No           | No            | No              | No             | OK            |
| Customer display | ESC GS B C | No         | No          | No           | No          | No           | No            | No              | No             | OK            |

--------------------------------------------------------------------------------------
