import common.input_parsers as common_input

step1_scoring = {
    "AX": 4,
    "AY": 8,
    "AZ": 3,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6
}
step2_scoring = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 2,
    "CY": 6,
    "CZ": 7
}


def solve1():
    puzzle_input = common_input.read_puzzle_input_as_list_of_lists_per_line(2, " ")
    print(sum([step1_scoring[str(game[0]) + str(game[1])] for game in puzzle_input]))


def solve2():
    puzzle_input = common_input.read_puzzle_input_as_list_of_lists_per_line(2, " ")
    print(sum([step2_scoring[str(game[0]) + str(game[1])] for game in puzzle_input]))


def main():
    solve1()
    solve2()


main()
