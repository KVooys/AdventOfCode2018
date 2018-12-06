"""
Day 5:
Opposite characters (char.lower and char.upper) 'react', which means they are filtered away from the input.
Part 1: How long is the output after reacting exhaustively?
Part 2: Figuring out and removing the most impactful char, how short can you get the output?
"""


from string import ascii_lowercase


with open("inputs/day5.txt", "r") as file:
    line = file.readlines()[0].strip()

# line = "dabAcCaCBAcCcaDA"


def reacting(char):
    if char == char.lower():
        return char.upper()
    else:
        return char.lower()

# stack based solution


def react(removed_char, current_line):
    stack = []

    if removed_char:
        current_line = current_line.replace(removed_char, "")
        current_line = current_line.replace(removed_char.upper(), "")
    print(current_line)

    for c in current_line:
        # print(c, reacting(c))
        if stack and reacting(c) == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    print(removed_char, len(stack))


# part 1
react(line)

# part 2
for alph in ascii_lowercase:
    react(alph, line)