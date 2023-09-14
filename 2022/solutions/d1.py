import common.input_parsers as common_input


def solve1():
    puzzle_input = common_input.read_puzzle_input_as_list_of_lists_clustered_lines_blank_separators(1)
    print(max([sum([int(cal) for cal in food]) for food in puzzle_input]))


def solve2():
    puzzle_input = common_input.read_puzzle_input_as_list_of_lists_clustered_lines_blank_separators(1)
    elves_calories = [sum([int(cal) for cal in food]) for food in puzzle_input]
    elves_calories.sort()
    print(sum(elves_calories[-3:]))


def main():
    solve1()
    solve2()


main()
