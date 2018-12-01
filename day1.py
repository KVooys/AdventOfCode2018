
"""
Machine is locked by frequency drift.
A file contains +X and -X commands, which means the frequency needs to change by that much.
Part 1: Find the final frequency after all changes, solved by simply looping over the commands.
Part 2: Find the frequency that's reached twice first; solved by making the function recursive and storing a set of
already reached frequencies.
"""


def run_through_list(start, reached, changes):
    frequency = start
    for change in changes:
        frequency += int(change)
        if frequency in reached:
            print(frequency)
            exit()
        else:
            reached.add(frequency)
        print(change, frequency)
    run_through_list(frequency, reached, changes)


with open("inputs/day1.txt", "r") as file:
    lines = file.readlines()
run_through_list(0, {0}, lines)
