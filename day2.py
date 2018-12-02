"""
Input file contains a list of IDs.
Part 1: find how many IDs have exactly 2 of a letter, and exactly 3 of a letter, and multiply those.
Part 2: find the two IDs that match for all except 1 letter, and enter the letters common to both!
"""

from collections import defaultdict
import difflib


def part1(lines):
    twopairs, threepairs = 0, 0
    for l in lines:
        currentline = sorted(l.strip('\n'))
        linedict = defaultdict(int)
        for letter in currentline:
            linedict[letter] += 1
        if 2 in linedict.values():
            twopairs += 1
        if 3 in linedict.values():
            threepairs += 1
    print(twopairs * threepairs)


def part2(lines):
    # run a loop once, removing the current line from the rest of the loop so I don't accidentally compare it to itself
    for l in lines:
        currentline = lines
        currentline.remove(l)
        # the words are 27 letters long, one letter is a ~4% difference, which explains the high cutoff
        # since there's only one pair to find I can simply read the output, no need to parse further
        if difflib.get_close_matches(l, currentline, cutoff=0.96):
            print(l, difflib.get_close_matches(l, currentline, cutoff=0.96)[0])


with open("inputs/day2.txt", "r") as file:
    lines = file.readlines()
# part1(lines)
part2(lines)