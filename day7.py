"""
--- Day 7: The Sum of Its Parts ---

You find yourself standing on a snow-covered coastline; apparently, you landed a little off course. The region is too hilly to see the North Pole from here, but you do spot some Elves that seem to be trying to unpack something that washed ashore. It's quite cold out, so you decide to risk creating a paradox by asking them for directions.

"Oh, are you the search party?" Somehow, you can understand whatever Elves from the year 1018 speak; you assume it's Ancient Nordic Elvish. Could the device on your wrist also be a translator? "Those clothes don't look very warm; take this." They hand you a heavy coat.

"We do need to find our way back to the North Pole, but we have higher priorities at the moment. You see, believe it or not, this box contains something that will solve all of Santa's transportation problems - at least, that's what it looks like from the pictures in the instructions." It doesn't seem like they can read whatever language it's in, but you can: "Sleigh kit. Some assembly required."

"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at once!" They start excitedly pulling more parts out of the box.

The instructions specify a series of steps and requirements about which steps must be finished before others can begin (your puzzle input). Each step is designated by a single letter. For example, suppose you have the following instructions:

Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.

Visually, these requirements look like this:


  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----

Your first goal is to determine the order in which the steps should be completed. If more than one step is ready, choose the step which is first alphabetically. In this example, the steps would be completed as follows:

    Only C is available, and so it is done first.
    Next, both A and F are available. A is first alphabetically, so it is done next.
    Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically of the three.
    After that, only D and F are available. E is not available because only some of its prerequisites are complete. Therefore, D is completed next.
    F is the only choice, so it is done next.
    Finally, E is completed.

So, in this example, the correct order is CABDFE.

In what order should the steps in your instructions be completed?

"""

    from collections import defaultdict

    with open("inputs/day7.txt", "r") as file:
        lines = file.readlines()

    # small requirements document in dict form:
    # before X can begin: do ABC --> formatted as {X: [A,B,C]}
    # Words[7] is the step, words[1] the requirement of that step
    reqs = defaultdict(list)
    total_steps = set()
    solved_order = ""

    for line in lines:
        words = line.split()
        reqs[words[7]].append(words[1])
        total_steps.add(words[1])
        total_steps.add(words[7])

    # if an item has no dependencies, it will not be in the dict, but it will be in the total_steps
    # That is the starting point (or a list of starting points).
    print("Removing starting points")
    starting_points = []
    for char in total_steps:
        if char not in reqs.keys():
            starting_points += char
    # Remove the starting points in alph order from the total_steps and add them to the solved_order.
    starting_points.sort()
    for s in starting_points:
        total_steps.remove(s)
        solved_order += s
        # since the requirement is solved, remove it from any requirements
        for v in reqs.values():
            if s in v:
                v.remove(s)
    print(starting_points)


    # main loop
    # logic: keep looping over the steps while there are still steps to be set
    points_to_remove = []
    while len(total_steps) > 0:
        print("Looping on ", total_steps)
        print("Requirements: ", reqs.items())
        for k, v in reqs.items():
            # if the requirements are met, the value in the dict will be an empty list
            if len(v) == 0 and k not in points_to_remove:
                points_to_remove.append(k)
        for p in points_to_remove:
            if p in reqs:
                reqs.pop(p)

        # remove the first in alph order from the total_steps and add them to the solved_order
        points_to_remove.sort()
        print("Eligible for removal ", points_to_remove)
        # only remove the alphabetically first letter
        removed_letter = points_to_remove[0]
        print("Removing ", removed_letter)
        total_steps.remove(removed_letter)
        solved_order += removed_letter
        # clean up the other requirements since one has been met
        for k, v in reqs.items():
            if removed_letter in v:
                v.remove(removed_letter)
        points_to_remove.remove(removed_letter)

    print(solved_order)
