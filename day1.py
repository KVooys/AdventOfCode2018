
"""
Machine is locked by frequency drift.
A file contains +X and -X commands, which means the frequency needs to change by that much.
Part 1: Find the final frequency after all changes, solved by splitting the commands on the first char.
Part 2: Find the frequency that's reached twice first; solved by making the function recursive and storing a set of
already reached frequencies.
"""


def run_through_list(start, reached):
    frequency = start
    with open("inputs/day1.txt", "r") as file:
        for line in file:
            op, change = line[0], int(line[1:])
            if op == "+":
                frequency += change
            else:
                frequency -= change
            if frequency in reached:
                print(frequency)
                exit()
            else:
                reached.add(frequency)
            print(op, change, frequency)
    run_through_list(frequency, reached)


run_through_list(0, {0})
