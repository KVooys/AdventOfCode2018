"""
Input is a log of guard duty.
Since the input is unsorted, sort it first.
Part 1: Find the guard that sleeps the most, then the minute during which he's asleep the most.
Part 2: Find the guard that is most frequently asleep on the same minute
"""

from datetime import datetime
from collections import defaultdict, OrderedDict, Counter
import pprint
import re

# sort the input by datetime first
def parse_input(input):
    timedict = defaultdict(str)
    for line in input:
        time, event = line.split(']')
        time = time[1:]
        timestamp = datetime.strptime(time, '%Y-%m-%d %H:%M')
        timedict[str(timestamp)] = event
    od = OrderedDict(sorted(timedict.items()))
    return od


# temporary function to make clean output readable
def print_clean_input(cleanlines):
    with open("inputs/day4cleaned.txt", "w") as output:
        for l in cleanlines:
            output.writelines(l)


# logfile is an ordereddict of events
# Need to 'group' events, aka start from one Guard, then read ahead until another Guard log starts.
# For every guard, track during which minutes he sleeps (length of this is total sleeptime)
# Sample: {'3307', [1,2,3,4,5,6,7]
def read_log(logfile):
    guard_dict = defaultdict(list)
    current_guard = ''
    sleep_start, sleep_end = 0, 0
    is_guard = r"Guard \#(\d+)"
    is_asleep = r"asleep"
    is_awoken = r"wakes up"
    longest_sleeper, longest_sleep = '', 0
    for time, event in logfile.items():
        timestamp = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

        # Guard line logic: keep track of which guard it is
        m = re.search(is_guard, event)
        if m:
            current_guard = m.group(1)

        # Asleep line logic: keep track of start minute
        m2 = re.search(is_asleep, event)
        if m2:
            sleep_start = timestamp.minute

        # Awoken logic: calculate total time using end minute, then write away in the guard_dict
        m3 = re.search(is_awoken, event)
        if m3:
            sleep_end = timestamp.minute
            for m in range(sleep_start, sleep_end):
                guard_dict[current_guard].append(m)
            # check if he's the new longest sleeper
            if len(guard_dict[current_guard]) > longest_sleep:
                longest_sleep = len(guard_dict[current_guard])
                longest_sleeper = current_guard

    print(max(set(guard_dict[longest_sleeper]), key=guard_dict[longest_sleeper].count))
    print(longest_sleeper)


def part_2(logfile):
    guard_dict = defaultdict(list)
    current_guard = ''
    sleep_start, sleep_end = 0, 0
    is_guard = r"Guard \#(\d+)"
    is_asleep = r"asleep"
    is_awoken = r"wakes up"
    most_frequent_guard, most_frequent_minute, max_freq = '', 0, 0
    for time, event in logfile.items():
        timestamp = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

        # Guard line logic: keep track of which guard it is
        m = re.search(is_guard, event)
        if m:
            current_guard = m.group(1)
            sleep_list = [0, []]

        # Asleep line logic: keep track of start minute
        m2 = re.search(is_asleep, event)
        if m2:
            sleep_start = timestamp.minute

        # Awoken logic: calculate total time using end minute, then write away in the guard_dict
        m3 = re.search(is_awoken, event)
        if m3:
            sleep_end = timestamp.minute
            for m in range(sleep_start, sleep_end):
                guard_dict[current_guard].append(m)

    # counter logic to find the most frequent minute and corresponding guard
    for guard, mins in guard_dict.items():
        c = Counter(mins)
        print(guard, c.most_common()[0])
        freq_count = c.most_common()[0][1]
        if freq_count > max_freq:
            max_freq = freq_count
            most_frequent_guard = guard
            most_frequent_minute = c.most_common()[0][0]
            print("New record", guard, c.most_common()[0])
    print(int(most_frequent_guard) * most_frequent_minute, max_freq)


with open("inputs/day4.txt", "r") as file:
    lines = file.readlines()
cleaned_log = parse_input(lines)
# print_clean_input(cleaned_log)
read_log(cleaned_log)
part_2(cleaned_log)
