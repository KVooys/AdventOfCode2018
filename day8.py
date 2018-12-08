"""
The tree is made up of nodes; a single, outermost node forms the tree's root, and it contains all other nodes in the tree (or contains nodes that contain nodes, and so on).

Specifically, a node consists of:

    A header, which is always exactly two numbers:
        The quantity of child nodes.
        The quantity of metadata entries.
    Zero or more child nodes (as specified in the header).
    One or more metadata entries (as specified in the header).



    2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    A----------------------------------
        B----------- C-----------
                         D-----

In this example, each node of the tree is also marked with an underline starting with a letter for identification.
In it, there are four nodes:

    A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
    B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
    C, which has 1 child node (D) and 1 metadata entry (2).
    D, which has 0 child nodes and 1 metadata entry (99).
"""

from collections import defaultdict, deque
import pprint

sample_line = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
sample_line2 = "2 3 1 3 0 1 5 10 11 12 1 1 0 1 99 2 1 1 2"


with open("inputs/day8.txt", "r") as file:
    line = file.readlines()[0]

# Reading left to right simply won't work; A's metadata is at the very end, AFTER its child node definitions.
# Instead, write separate functions to separate the nodes and then to add their metadata entries.
# Working with a deque to keep track of the remaining numbers


def read_new_node(count):
    # Make sure to add a new dict entry for every node, using the next unused number
    if node_dict.keys():
        count = max(node_dict.keys())+1
    node_name = count
    children = numbers.popleft()
    metadata_count = numbers.popleft()
    metadata_entries = []
    node_dict[node_name] = [children, metadata_count, metadata_entries]

    if children > 0:
        # if the node has children, read every child.
        for c in range(children):
            read_new_node(count)

    # if the node has no children, the metadata are the following numbers
    # But what about the metadata entries when there are children?
    # Those are gonna be the leftmost of the queue after all children are processed.
    for i in range(metadata_count):
        metadata_entries.append(numbers.popleft())
    node_dict[node_name][2] = metadata_entries


# Node A: [[children], int(metadata-count), [metadata-entries]]
node_dict = defaultdict(list)
numbers = deque(map(int, line.split()))
count = 0
count = read_new_node(count)
pprint.pprint(node_dict)

# calculate total function
total = 0
total += sum(sum(v[2]) for v in node_dict.values())
print(total)