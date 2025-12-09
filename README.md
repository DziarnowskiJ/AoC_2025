# Advent Of Code 2025
This is my repository for the annual [**Advent of Code**](https://adventofcode.com/).

- [Day 1: Secret Entrance](#day-1)
- [Day 2: Gift Shop](#day-2)
- [Day 3: Lobby](#day-3)
- [Day 4: Printing Department](#day-4)
- [Day 5: Cafeteria](#day-5)
- [Day 6: Trash Compactor](#day-6)
- [Day 7: Laboratories](#day-7)
- [Day 8: Playground](#day-8)
- [Day 9: Movie Theater](#day-9)

# Notes on each day's challenge

## [Day 1: Secret Entrance](https://adventofcode.com/2025/day/1)<span id="day-1"><span>
Sequential list processing requiring modulo function

The puzzle involves tracking the position of a **safe dial numbered 0 to 99** as 
it undergoes a sequence of left (**L**) and right (**R**) rotations. 
The movement is modular, meaning a move from 99 right lands on 0, 
and a move from 0 left lands on 99. The dial starts at 50.

The first part requires calculating the final position after each 
rotation and counting how many times the dial lands on 0.
# Hello: dupa
The second part is a variation on counting. 
Instead of only counting when the dial lands exactly on 0, 
you must count every time the dial points at 0 - even if it doesn't stop on it.

```
Start position: 50

Part 1 - Counting final position 0s:
Rotation │ Start │ Clicks │ End │ At 0?
─────────┼───────┼────────┼─────┼────────
L68      │ 50    │ -68    │ 82  │ 0 
L30      │ 82    │ -30    │ 52  │ 0
R48      │ 52    │ +48    │ 0   │ 1
L5       │ 0     │ -5     │ 95  │ 0
R60      │ 95    │ +60    │ 55  │ 0
L55      │ 55    │ -55    │ 0   │ 1
L1       │ 0     │ -1     │ 99  │ 0
L99      │ 99    │ -99    │ 0   │ 1
R14      │ 0     │ +14    │ 14  │ 0
L82      │ 14    │ -82    │ 32  │ 0
                                ├────────
                                │Total: 3

Part 2 - Counting all 0s (during and after rotation):
Rotation │ Start │ Clicks │ End │ 0s during rotation │ At 0s │ Total 0s
─────────┼───────┼────────┼─────┼────────────────────┼───────┼───────────
L68      │ 50    │ -68    │ 82  │ 1 (at click 50)    │ 0     │ 1
L30      │ 82    │ -30    │ 52  │ 0                  │ 0     │ 0
R48      │ 52    │ +48    │ 0   │ 0                  │ 1     │ 1
L5       │ 0     │ -5     │ 95  │ 0                  │ 0     │ 0
R60      │ 95    │ +60    │ 55  │ 1 (at click 5)     │ 0     │ 1
L55      │ 55    │ -55    │ 0   │ 0                  │ 1     │ 1
L1       │ 0     │ -1     │ 99  │ 0                  │ 0     │ 0
L99      │ 99    │ -99    │ 0   │ 0                  │ 1     │ 1
R14      │ 0     │ +14    │ 14  │ 0                  │ 0     │ 0
L82      │ 14    │ -82    │ 32  │ 1 (at click 14)    │ 0     │ 1
                                                             ├──────────
                                                             │Total: 6
```

## [Day 2: Gift Shop](https://adventofcode.com/2025/day/2)<span id="day-2"><span>
Searching for numbers with repeating digit patterns within given ranges

The challenge involves parsing a list of ID ranges (e.g., _11-22,95-115,1010-1012_) 
and identifying invalid IDs that fall within these ranges. 
An ID is invalid if it consists of a repeating sequence of digits.

The first part defines an invalid ID as one made of a digit sequence repeated **exactly twice**.
The second part broadens the definition: an ID is invalid if it is made of a digit sequence repeated at **least twice**.

The final goal for both parts is to find all invalid IDs within the given ranges and calculate their sum.

```
Part 1 - Sequence repeated exactly twice (DD):
Range    │ Invalid IDs │ Sum for range
─────────┼─────────────┼───────────────
11-22    │ 11, 22      │ 33
95-115   │ 99          │ 99
998-1012 │ 1010        │ 1010
                       ├──────────
                       │Total: 1142
                       
Part 2 - Sequence repeated at least twice (D, DD, DDD...)::
Range    │ Invalid IDs │ Sum for range
─────────┼─────────────┼───────────────
11-22    │ 11, 22      │ 33
95-115   │ 99, 111     │ 210
998-1012 │ 999, 1010   │ 2009
                       ├──────────
                       │Total: 2252
```

## [Day 3: Lobby](https://adventofcode.com/2025/day/3)<span id="day-3"><span>
Finding the maximum number that can be formed by selecting digits from a string.

The problem presents a series of battery banks, 
where each bank is represented by a long string of single-digit _joltage_ ratings (1-9). 
The goal is to select a **fixed number** of batteries from the bank to form the 
**largest possible number** (_joltage rating_), 
while maintaining the original relative order of the digits.

The first part requires turning on exactly **two batteries**.
The second part increased the complexity by requiring the selection of 
exactly **twelve batteries**.

```
Part 1 - Selecting exactly two digits (2-digit joltage):
Bank: 987654321111111 (Length 15)
1. Find largest first digit: '9' at index 0.
2. Find largest second digit after '9': '8' at index 1.
Joltage: 98

Bank: 818181911112111 (Length 15)
1. Find largest first digit: '9' at index 6.
2. Find largest second digit after '9': '2' at index 11.
Joltage: 92

Part 2 - Selecting exactly twelve digits (12-digit joltage):
Bank: 987654321111111
1. Select '9' (1st digit). 11 digits remain to be selected from 87654321111111.
2. Select '8' (2nd digit). 10 digits remain from 7654321111111.
...and so on, greedily picking the largest available digit for each position.
Joltage: 987654321111

Bank: 818181911112111
1. '8' is the largest starting digit available. The first digit '9' is too far (only 8 digits remain after it).
2. The largest possible prefix comes from the '8889...' sequence, resulting in 888911112111.
Joltage: 888911112111

```

## [Day 4: Printing Department](https://adventofcode.com/2025/day/4)<span id="day-4"><span>
Analyzing adjacency in a 2D grid with iterative removal process.

The puzzle's input is a large 2D grid containing rolls of paper (**@**) and empty spaces (**.**)

The first part defines the accessibility rule: 
a roll of paper can be accessed and removed if it has fewer than 
four rolls of paper in its eight adjacent positions _(horizontal, vertical, and diagonal neighbors)_.
The task is to count how many rolls in the initial grid meet this criterion to be removed.

The second part introduces an **iterative process or paper removal**. 
Once an accessible roll is identified, it is considered removed 
(**turning its position into an empty space**). 
This changes the adjacency counts for its neighbors, 
potentially making new rolls accessible. 
The process must be repeated until no more rolls can be removed, 
and the goal is to find the **total number of removed rolls**.

```
Part 1 - Initial removal:
..@@.@@@@.                         ..●●.●●@●.
@@@.@.@.@@                         ●@@.@.@.@@
@@@@@.@.@@                         @@@@@.●.@@
@.@@@@..@.   Possible to remove    @.@@@@..@.
@@.@@@@.@@  ────────────────────>  ●@.@@@@.@●
.@@@@@@@.@                         .@@@@@@@.@
.@.@.@.@@@                         .@.@.@.@@@
@.@@@.@@@@                         ●.@@@.@@@@
.@@@@@@@@.                         .@@@@@@@@.
@.@.@@@.@.                         ●.●.@@@.●.

Part 2 - Iterative removal
..@@.@@@@.           ..●●.●●@●.           .......●..              ..........
@@@.@.@.@@           ●@@.@.@.@@           .@@.●.●.@●              ..........
@@@@@.@.@@           @@@@@.●.@@           ●@@@@...@@              ..........
@.@@@@..@.  Remove   @.@@@@..@.  Remove   ●.@@@@..●.  Remove x8   ....@@....
@@.@@@@.@@ ────────> ●@.@@@@.@● ────────> .@.@@@@.●. ───────────> ...@@@@...
.@@@@@@@.@           .@@@@@@@.@           .●@@@@@@.●              ...@@@@@..
.@.@.@.@@@           .@.@.@.@@@           .●.@.@.@@@              ...@.@.@@.
@.@@@.@@@@           ●.@@@.@@@@           ..@@@.@@@@              ...@@.@@@.
.@@@@@@@@.           .@@@@@@@@.           .●@@@@@@@.              ...@@@@@..
@.@.@@@.@.           ●.●.@@@.●.           ....@@@...              ....@@@...
```

## [Day 5: Cafeteria](https://adventofcode.com/2025/day/5)<span id="day-5"><span>
Overlapping numerical ranges and set membership

This puzzle involves an inventory system where _fresh ingredient IDs_ 
are defined by a list of **potentially overlapping numerical ranges** _(e.g., 3-5 means 3, 4, and 5 are fresh)_. 
The input is separated into two sections: a list of _fresh ID ranges_ and a list of _available ingredient IDs_.

The first part requires checking each available ingredient ID to see if it falls within any of the defined fresh ranges
The second part ignores the list of available IDs and focuses only on the fresh ID ranges. The task is to find the total count of unique, fresh ingredient IDs defined by the ranges. Because the ranges can overlap, simply summing the lengths of the individual ranges will lead to an overcount.

To correctly find the total count, the overlapping ranges must first be merged into a minimal set of non-overlapping intervals. The total count is then the sum of the lengths of these merged intervals.


```
Part 1 - Counting Available Fresh IDs:
Fresh Ranges: [3, 5], [10, 14], [16, 20], [12, 18]
Available IDs: 1, 5, 8, 11, 17, 32

ID │ Check against ranges        │ Fresh?
───┼─────────────────────────────┼──────────
1  │ Not in any range            │ 0
5  │ Is in [3, 5]                │ 1
8  │ Not in any range            │ 0
11 │ Is in [10, 14]              │ 1
17 │ Is in [16, 20] & [12, 18]   │ 1
32 │ Not in any range            │ 0
                                 ├─────────
                                 │Total: 3
                                 
Part 2 - Merging Overlapping Ranges:
0. Initial Ranges: [3, 5], [10, 14], [16, 20], [12, 18]
1. Sort the ranges: [3, 5], [10, 14], [12, 18], [16, 20]
2. Merge Ranges: [3, 5], [10, 20]

Range    │ Length
─────────┼─────────
[3, 5]   │ 3
[10, 20] │ 11           
         ├─────────
         │Total: 14                   
```

## [Day 6: Trash Compactor](https://adventofcode.com/2025/day/6)<span id="day-6"><span>
Solving math problems presented in a transposed format

The input included set of additions and multiplications written in the _long format_
meaning that numbers within each operation where listed below each other.
Each operation was presented next ot each other, making the paring of the input tricky.

Part one required **solving each equitation and returning sum of all results**.
Part two explained that numbers are not written horizontally but **vertically 
and should be read from right to left**. 
```
Example input:
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

Part 1 - Horizontal numbers:
Equasion       │ Result
───────────────┼────────
123 * 45 * 6   │ 33210
328 + 64 + 98  │ 490
51 * 387 * 215 │ 4243455
64 + 23 + 314  │ 401
               ├─────────
               │Total: 4277556         

Part 2 - Vertical numbers:
Equasion       │ Result
───────────────┼────────
356 * 24 * 1   │ 8544
8 + 248 + 369  │ 625
175 * 581 * 32 │ 3253600
4 + 431 + 623  │ 1058
               ├─────────
               │Total: 3263827         
```

## [Day 7: Laboratories](https://adventofcode.com/2025/day/7)<span id="day-7"><span>
Simulating beam propagation and calculating path multiplicity in a recursive grid structure.

This puzzle involves simulating the behavior of a tachyon beam as it travels 
downward through a grid. The grid consists of empty **space** (**.**) and **splitters** (**^**).

In a part one, when a beam runs into a splitter it is being divided into two beams.
Those beams then run parallel to each other on both sides of the splitter. The goal
is to calculate the number of splits that happen before the beams reach bottom of the grid.

The second part switches to a **_quantum model_**. 
When a single beam reaches a splitter, it takes only one path (left or right), 
but splits the _timeline_ into two branches - one in which it went left and second in which it went right.
The goal is to determine number of timelines created once the beam reaches the bottom. 
This means that it required calculating number of all possible paths for the beam. 


```
Part 1 - Beam splitting
.......S.......                        .......S.......
...............                        .......|.......
.......^.......                        ......|^|...... - 1 split
...............                        ......|.|......
......^.^......  Traveling downwards   .....|^|^|..... - 2 splits
............... ─────────────────────> .....|.|.|.....
.....^.^.^.....                        ....|^|^|^|.... - 3 splits
...............                        ....|.|.|.|....
....^.^...^....                        ...|^|^|||^|... - 3 splits
...............                        ...|.|.|||.|...
...^.^...^.^...                        ..|^|^|||^|^|.. - 4 splits
...............                        ..|.|.|||.|.|..
..^...^.....^..                        .|^|||^||.||^|. - 3 splits
...............                        .|.|||.||.||.|.
.^.^.^.^.^...^.                        |^|^|^|^|^|||^| - 5 splits
...............                        |.|.|.|.|.|||.| ┌─────────────────
                                                       │Total: 21 splits  

Part 2 - Timeline splitting

Always           │  Alternating      │   Other example
going left       │  left and right   │                    
─────────────────┼───────────────────┼────────────────────
.......S.......  │  .......S.......  │   .......S.......
.......|.......  │  .......|.......  │   .......|.......
......|^.......  │  ......|^.......  │   ......|^.......
......|........  │  ......|........  │   ......|........
.....|^.^......  │  ......^|^......  │   .....|^.^......
.....|.........  │  .......|.......  │   .....|.........
....|^.^.^.....  │  .....^|^.^.....  │   ....|^.^.^.....
....|..........  │  ......|........  │   ....|..........
...|^.^...^....  │  ....^.^|..^....  │   ....^|^...^....
...|...........  │  .......|.......  │   .....|.........
..|^.^...^.^...  │  ...^.^.|.^.^...  │   ...^.^|..^.^...
..|............  │  .......|.......  │   ......|........
.|^...^.....^..  │  ..^...^|....^..  │   ..^..|^.....^..
.|.............  │  .......|.......  │   .....|.........
|^.^.^.^.^...^.  │  .^.^.^|^.^...^.  │   .^.^.^|^.^...^.
|..............  │  ......|........  │   ......|........

Number of unique paths: 40
```

## [Day 8: Playground](https://adventofcode.com/2025/day/8)<span id="day-8"><span>
Connecting points in 3D space and analysing the shortest distances between them

Challenge presented a list of **points in a three-dimensional space** and required
calculating **straight-line distance** between each of them. Then, starting with 
the shortest distance, actually connecting them into _circuits_. 

Part one required setting up 1000 connections and finding 3 largest
circuits. Part two asked for the first connection that would combine all points into
a single circuit.

```
Example input:
1,5,2
2,7,3
15,20,10
15,18,16
20,20,20
5,5,5

Possible connections:
ID │ Point 1 (Name)       │ Point 2 (Name)       │ Distance (Rounded)
───┼──────────────────────┼──────────────────────┼────────────────────
1  │ Point 1 5 2      (A) │ Point 2 7 3      (B) │ 2.4
2  │ Point 2 7 3      (B) │ Point 5 5 5      (F) │ 4.1
3  │ Point 1 5 2      (A) │ Point 5 5 5      (F) │ 5.0
4  │ Point 15 20 10   (C) │ Point 15 18 16   (D) │ 6.3
5  │ Point 15 18 16   (D) │ Point 20 20 20   (E) │ 6.7
6  │ Point 15 20 10   (C) │ Point 20 20 20   (E) │ 11.2
7  │ Point 15 20 10   (C) │ Point 5 5 5      (F) │ 18.7
8  │ Point 2 7 3      (B) │ Point 15 20 10   (C) │ 19.7
9  │ Point 15 18 16   (D) │ Point 5 5 5      (F) │ 19.7
10 │ Point 2 7 3      (B) │ Point 15 18 16   (D) │ 21.4
11 │ Point 1 5 2      (A) │ Point 15 20 10   (C) │ 22.0
12 │ Point 1 5 2      (A) │ Point 15 18 16   (D) │ 23.7
13 │ Point 20 20 20   (E) │ Point 5 5 5      (F) │ 26.0
14 │ Point 2 7 3      (B) │ Point 20 20 20   (E) │ 28.0
15 │ Point 1 5 2      (A) │ Point 20 20 20   (E) │ 30.2

Part 1 - iterative setting up connections: 
Connection  │ Circuits
────────────┼─────────────────────
A-B         │ {A,B}
B-F         │ {A,B,F}
A-F         │ {A,B,F}
C-D         │ {A,B,F}, {C,D}      <── Part 1: Largest circuit after 4 connections has 3 points  
D-E         │ {A,B,F}, {C,D,E}
C-E         │ {A,B,F}, {C,D,E}
C-F         │ {A,B,C,D,E,F}       <── Part 2: All points connected after 7 connections
...         │ ...

```

## [Day 9: Movie Theater](https://adventofcode.com/2025/day/9)<span id="day-9"><span>
Finding the largest possible rectangle area defined by two points in a grid

The puzzle involves a large 2D grid of tiles. 
The input provides the coordinates of several red tiles (**■**). 
The goal of the first part is to select any two red tiles and use them 
as opposite corners of a rectangle, then find the one with the maximum area.

The second part introduced new green tiles (**□**) and a color constraint.
The red tiles in the input list form a closed loop and are connected between each other with straight lines. 
Those connections are made out of the green tiles. Additionally, all tiles inside this loop are also green.
Similarly as before, the challenge required finding the largest area bounded by 2 red tiles, 
with the exception that all tiles within it had to be green or red
```
Part 1 - Largest area

Initial grid   │ Largest area
───────────────┼────────────────
.............. │ ..............
.......■...■.. │ ..#########■..
.............. │ ..##########..
..■....■...... │ ..■####■####..
.............. │ ..##########..
..■......■.... │ ..■######■##..
.............. │ ..............
.........■.■.. │ .........■.■..
.............. │ ..............

Part 2 - Largest area of only green and red tiles

Initial grid   │ Largest area
───────────────┼────────────────
.............. │ ..............
.......■□□□■.. │ .......■□□□■..
.......□□□□□.. │ .......□□□□□..
..■□□□□■□□□□.. │ ..■#######□□..
..□□□□□□□□□□.. │ ..########□□..
..■□□□□□□■□□.. │ ..■######■□□..
.........□□□.. │ .........□□□..
.........■□■.. │ .........■□■..
.............. │ ..............
```
