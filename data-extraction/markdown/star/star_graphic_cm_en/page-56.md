<!-- image -->

Rev. 2.31

## 4-4) Appendix-6 Supported Command List by Models

## ● Standard Commands

| Class                 | Command       | TSP100 U   | TSP100 PU   | TSP100 IIU   | TSP100 GT   | TSP100 LAN   | TSP100 IIIW     | TSP100 IIILAN   | TSP100 IIIBI    | TSP100 IIIU   |
|-----------------------|---------------|------------|-------------|--------------|-------------|--------------|-----------------|-----------------|-----------------|---------------|
| External device drive | ESC BEL       | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| External device drive | BEL           | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| External device drive | FS            | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| External device drive | SUB           | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| External device drive | EM            | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| External device drive | ESC GS BEL    | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| External device drive | ESC GS EM DC1 | V1.3 ～     | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| External device drive | ESC GS EM DC2 | V1.3 ～     | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| Print settings        | ESC RSA       | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| Print settings        | ESC RS d      | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| Print settings        | ESC RS r      | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| Print settings        | ESC GS c      | No         | No          | OK           | No          | No           | Ver2.0 or later | Ver2.0 or later | Ver2.0 or later | No            |
| Status                | ESC RS a      | No         | No          | No           | No          | No           | Ver1.4 or later | Ver1.3 or later | OK              | OK            |
| Status                | ESCACK SOH    | No         | No          | No           | No          | No           | Ver1.4 or later | Ver1.3 or later | OK              | OK            |
| Status                | ETB           | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| Status                | ESC RS E      | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| Status                | ESC GS ETX    | No         | No          | No           | No          | No           | Ver1.4 or later | Ver1.3 or later | OK              | OK            |
| Other                 | ESC GS #      | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| Other                 | ESC ?         | OK         | OK          | OK           | OK          | OK           | OK              | OK              | OK              | OK            |
| Other                 | ESC GS L DC1  | No         | No          | No           | No          | No           | OK              | OK              | OK              | OK            |
| Other                 | ESC GS L DC2  | No         | No          | No           | No          | No           | OK              | OK              | OK              | OK            |

## ● Raster related commands

| Class            | Command           | TSP100 U   | TSP100 PU   | TSP100 IIU   | TSP100 GT   | TSP100 LAN   | TSP100 IIIW   | TSP100 IIILAN   | TSP100 IIIBI   | TSP100 IIIU   |
|------------------|-------------------|------------|-------------|--------------|-------------|--------------|---------------|-----------------|----------------|---------------|
| Raster           | ESC * r R         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r A         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r B         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r C         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r D         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r E         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r F         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r P         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r Q         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r m l       | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r m r       | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r t         | No         | No          | OK           | No          | No           | No            | No              | No             | No            |
| Raster           | ESC * r K         | OK         | OK          | OK           | OK          | OK           | V1.4 or later | V1.3 or later   | OK             | OK            |
| Raster           | b n1 n2 d1 ．．． dk | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | k n1 n2 d1 ．．． dk | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC * r Y         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC FF NUL        | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster           | ESC FF EOT        | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster extension | ESC * r a         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster extension | ESC * r b         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster extension | ESC * r e         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster extension | ESC FF EM         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |
| Raster extension | ESC FF LF         | OK         | OK          | OK           | OK          | OK           | OK            | OK              | OK             | OK            |

--------------------------------------------------------------------------------------
