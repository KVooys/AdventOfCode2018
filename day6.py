"""
--- Day 6: Chronal Coordinates ---

The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9

If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.

This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf

Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid.
However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself).
Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?

"""

from collections import defaultdict
import pprint

with open("inputs/day6.txt", "r") as file:
    lines = file.readlines()


coord_map = defaultdict(list)
max_x, max_y = 0, 0
count = 0
for line in lines:
    x, y = map(int, line.strip().split(", "))
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    coord_map[count] = [x, y]
    count += 1

# TODO: find nearest coords (Manhattan distance) for each point in the coord_map
# Pseudo code:
# for every point on the grid (which is size max_x, max_y)
# calculate Manhattan distance to X nearby points (how many? only for points +/- 0.5 * max_x and max_y)
# store shortest dist per point on the grid somehow, like a defaultdict(int)
# use 0 if distance is the same to two or more points

# No need to search for the distance to the points that are farthest outside
# as they will extend infinitely in some way or another
# Optional: Write them to a CSV file to make a nice map view for funsies
# Example:
# # Write csv full of dots
# with open("day6test.csv", "w") as output:
#     for y in range(max_y):
#         base_line = (max_x * ".," + "\n")
#         output.write(base_line)



