"""
Puzzle about clothing patterns and claims. The elves are building a suit and all have a certain claim, like so:
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge,
2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric
represented by # (and ignores the square inches of fabric represented by .).
Part 1: How many square inches of fabric are within two or more claims?
Part 2: which claim has no overlap?
"""

from collections import defaultdict


# use coordinates and a dict of {Coordinate:[claims]} to store them
grid = defaultdict(list)
claim_id_set = set()
with open("inputs/day3.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    # some parsing logic first
    cleanline = line.replace(':', '')
    claim_id, _, distances, fills = cleanline.split()
    dx, dy = distances.split(',')
    fillx, filly = fills.split('x')
    fillx, filly, dx, dy = int(fillx), int(filly), int(dx), int(dy)
    # set of claim_ids needed for part 2
    claim_id_set.add(claim_id)

    # two-dimensional loop to get all the needed coordinates
    for x in range(dx, dx+fillx):
        for y in range(dy, dy+filly):
            current_coord = f'({x},{y})'
            grid[current_coord].append(claim_id)

count = 0
for l in grid.values():
    if len(l) > 1:
        count += 1
print(count)


# Solve part 2 by removing all claim_ids that are present on overlaps from a list
for k, v in grid.items():
    if len(v) > 1:
        for claim_id in v:
            if claim_id in claim_id_set:
                claim_id_set.remove(claim_id)
print(claim_id_set)
