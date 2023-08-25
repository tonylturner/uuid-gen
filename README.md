# uuid-gen
Simple python script to generate a specified number of UUIDs. Supports UUId Type 1, 3, 4 and 5. Defaults UUID Type 4, and count of 10. Use -c to specify more or fewer. 

https://en.wikipedia.org/wiki/Universally_unique_identifier


```
usage: uuid-gen.py [-h] [-v {1,3,4,5}] [-c COUNT] [-n NAME]

Generate different versions of UUIDs and print to stdout.

options:
  -h, --help            show this help message and exit
  -v {1,3,4,5}, --version {1,3,4,5}
                        Version of UUID to generate. Options are: 1 (Time-based), 3 (Name-based using MD5), 4
                        (Random), 5 (Name-based using SHA-1). Default is 4 (Random).
  -c COUNT, --count COUNT
                        Count of UUIDs to generate (default is 10).
  -n NAME, --name NAME  Name for the name-based UUID (used with versions 3 and 5). If not provided, will prompt
                        for input.

```
