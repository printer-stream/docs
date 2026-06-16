200 OK,count=1&amp;t\_size=7731371&lt;CRLF&gt;

&lt;CRLF&gt;

0&lt;CRLF&gt;

&lt;CRLF&gt;

0&lt;CRLF&gt;

Interpretation Acquire total number of files and file size. Specify start time and end time, then CHUNKED HTTP response will be returned. The value of count is total number of files. The value of t\_size is file size.

Allowed users admin, operator

## Exporting SD Card Data as a File

## Format

/api/copy?pseudo=off&amp;from.date.start=YYYYMMDDhhmmss&amp;from.date.end=YYYYMMDDhhmmss

Example of response

c&lt;CRLF&gt;

200 OK,(0)&lt;CRLF&gt;

&lt;CRLF&gt;

14&lt;CRLF&gt;

200 OK,(Completed)&lt;CRLF&gt;

&lt;CRLF&gt;

40&lt;CRLF&gt;

Size of main header

## Data structure of header1

| Item                  |   Size | Example         | Note                    |
|-----------------------|--------|-----------------|-------------------------|
| Revision              |     24 | revision=0x0100 | Revision of file format |
| Total number of files |     16 | count=2         | Total number of files   |
| Total size of files   |     24 | t_size=12052495 | Total size of files     |

## 38&lt;CRLF&gt;

Data structure of header1

| Item            |           |   Size | Example       | Note          |
|-----------------|-----------|--------|---------------|---------------|
| Header of file1 | Size      |     16 | size=7731251  | Size of file1 |
| Header of file1 | File name |     40 | name-ckst0000 | Name of file1 |

38&lt;CRLF&gt;

Data structure of header2

| Item            |           |   Size | Example       | Note          |
|-----------------|-----------|--------|---------------|---------------|
| Header of file2 | Size      |     16 | size=4321244  | Size of file2 |
| Header of file2 | File name |     40 | name-ckst0001 | Name of file2 |

C800&lt;CRLF&gt;

Data(1) size of file1

data(1) of file1 (50 kB)

Header size of file2

Header size of file2
