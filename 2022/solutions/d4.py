import common.input_parsers as common_input


def solve1():
    puzzle_input = common_input.read_puzzle_input_as_list_of_lists_per_line(4, ',')
    fully_overlapping = 0
    for pairs in puzzle_input:
        range1 = pairs[0].split('-')
        range2 = pairs[1].split('-')
        assignment1 = range(int(range1[0]), int(range1[1]) + 1)
        assignment2 = range(int(range2[0]), int(range2[1]) + 1)
        common_sections = list(set(assignment1).intersection(assignment2))
        if set(common_sections) == set(assignment1) or set(common_sections) == set(assignment2):
            fully_overlapping += 1
    print(fully_overlapping)

def solve2():
    puzzle_input = common_input.read_puzzle_input_as_list_of_lists_per_line(4, ',')
    overlapping = 0
    for pairs in puzzle_input:
        range1 = pairs[0].split('-')
        range2 = pairs[1].split('-')
        assignment1 = range(int(range1[0]), int(range1[1]) + 1)
        assignment2 = range(int(range2[0]), int(range2[1]) + 1)
        common_sections = list(set(assignment1).intersection(assignment2))
        if len(common_sections) > 0:
            overlapping += 1
    print(overlapping)

def main():
    solve1()
    solve2()


main()
