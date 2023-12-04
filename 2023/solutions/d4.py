import math
import common.input_parsers as common_input
from functools import lru_cache


@lru_cache
def get_solved_count(left, right):
    count = 0
    for l in left:
        if l in right:
            count += 1
    return count

def solve1():
    puzzle_input = common_input.read_puzzle_input_as_list(4)
    total = 0
    for line in puzzle_input:
        b_split = line[9:].split("|")
        left = b_split[0].replace("  ", " ").strip().split(" ")
        right = b_split[1].replace("  ", " ").strip().split(" ")
        count = 0
        for l in left:
            if l in right:
                count += 1
        if count > 0:
            total += math.pow(2, count - 1)
    print(total)


# 13261636 too low
# 13261850 correct

def solve2():
    puzzle_input = common_input.read_puzzle_input_as_list(4)
    copies = [1 for x in range(len(puzzle_input))]
    for i, line in enumerate(puzzle_input):
        b_split = line[9:].split("|")
        left = b_split[0].replace("  ", " ").strip().split(" ")
        right = b_split[1].replace("  ", " ").strip().split(" ")
        for t in range(copies[i]):
            count = 0
            count = get_solved_count(tuple(left), tuple(right))
            for c in range(count):
                copies[1 + i + c] += 1
    print(sum(copies))


def main():
    solve1()
    solve2()


main()
