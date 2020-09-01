# Snake Numbering

Fantasy Football Snake Draft Help. Given a draft position, number of teams, and number of rounds, returns a list of the overall pick numbers.
For example:
```bash
./snake_numbering -p 1 -t 10 -r 16
For 10 teams, 16 rounds and draft position 1, you get the following overall picks:
Round 1, Draft Pos 1 ---> Overall Pick #1
Round 2, Draft Pos 1 ---> Overall Pick #20
Round 3, Draft Pos 1 ---> Overall Pick #21
Round 4, Draft Pos 1 ---> Overall Pick #40
Round 5, Draft Pos 1 ---> Overall Pick #41
Round 6, Draft Pos 1 ---> Overall Pick #60
Round 7, Draft Pos 1 ---> Overall Pick #61
Round 8, Draft Pos 1 ---> Overall Pick #80
Round 9, Draft Pos 1 ---> Overall Pick #81
Round 10, Draft Pos 1 ---> Overall Pick #100
Round 11, Draft Pos 1 ---> Overall Pick #101
Round 12, Draft Pos 1 ---> Overall Pick #120
Round 13, Draft Pos 1 ---> Overall Pick #121
Round 14, Draft Pos 1 ---> Overall Pick #140
Round 15, Draft Pos 1 ---> Overall Pick #141
Round 16, Draft Pos 1 ---> Overall Pick #160
```

# Usage

```bash
usage: snake_numbering [-h] [-p POS] [-t NTEAMS] [-r NROUNDS] [-d]

Gives overall number for snake style count

optional arguments:
  -h, --help            show this help message and exit
  -p POS, --pos POS     Draft Position
  -t NTEAMS, --nteams NTEAMS
                        Number of Teams
  -r NROUNDS, --nrounds NROUNDS
                        Number of Rounds
  -d, --debug           Increased verbosity
```

