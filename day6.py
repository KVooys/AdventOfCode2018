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

from collections import defaultdict, Counter
from PIL import Image, ImageFilter
import random
import math


def input_to_vars(lines):
    coord_map = defaultdict(tuple)
    max_x, max_y = 0, 0
    count = 0
    for line in lines:
        x, y = map(int, line.strip().split(", "))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        coord_map[count] = (x, y)
        count += 1
    return coord_map, max_x, max_y


# this is wrong, but was fun to make! Vonoroi diagram (which is not Manhattan unfortunately)
def generate_voronoi_diagram(width, height, coords):
    colours = defaultdict(int)
    image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    for k, v in coords.items():
        nx.append(v[0])
        ny.append(v[1])
        nr.append(random.randrange(1, 256))
        ng.append(random.randrange(1, 256))
        nb.append(random.randrange(1, 256))
    for y in range(imgy):
        for x in range(imgx):
            # mark the initial points in black
            if (x, y) in coords.values():
                putpixel((x, y), (0, 0, 0))
            else:
                dmin = math.hypot(imgx - 1, imgy - 1)
                j = -1
                for i in range(len(coords)):
                    d = math.hypot(nx[i] - x, ny[i] - y)
                    if d < dmin:
                        dmin = d
                        j = i
                putpixel((x, y), (nr[j], ng[j], nb[j]))

    image.save("VoronoiDiagram.png", "PNG")


def generate_manhattan_distances(width, height, coords):
    nearest = {}
    imgx, imgy = width, height

    for y in range(imgy):
        for x in range(imgx):
            xy = (x, y)
            dist = []
            for c in coords.values():
                # calculate mh dist to each coord and append to the dist_dict
                manhattan = abs((c[0] - x) + (c[1] - y))
                dist.append((c, manhattan))
            # check to which coord this pixel has the least mh dist, and whether there's only one of those.
            min_dist = min(d[1] for d in dist)
            found = list(filter(lambda d: d[1] == min_dist, dist))
            # if that's the case, append it to a dict to count with.
            # TODO: Figure out which ones go on infinitely somehow.
            if len(found) == 1:
                nearest[xy] = found[0][0]
            else:
                nearest[xy] = None
    counter = Counter(nearest.values())
    print(counter.most_common())


with open("inputs/day6.txt", "r") as file:
    lines = file.readlines()


coords, width, height = input_to_vars(lines)
# print(coords, width, height)
generate_voronoi_diagram(width, height, coords)
# generate_manhattan_distances(width, height, coords)


# find nearest coords (Manhattan distance) for each point in the coord_map
# Pseudo code:
# for every point on the grid (which is size max_x, max_y)
# calculate Manhattan distance to other points
# store shortest dist per point on the grid somehow, in a counter for instance
# don't count if distance to two or more points is the same

# No need to search for the distance to the points that are farthest outside
# as they will extend infinitely in some way or another
# However, I don't know yet how to determine which ones this involves.
