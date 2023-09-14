import common.input_parsers as common_input
import common.logical_functions as common_logic
import common.scoring_techniques as scoring


def solve1():
    puzzle_input = common_input.read_puzzle_input_as_list(3)
    print(sum([scoring.alphabet_lower_upper_1to52.index(common_logic.halve_and_find_common_elements(rucksack)[0]) for rucksack in puzzle_input]))


def solve2():
    puzzle_input = common_input.read_puzzle_input_as_list(3)
    count = 0
    rucksack_group = []
    group_common_types = []
    for rucksack in puzzle_input:
        rucksack_group.append(rucksack)
        count += 1
        if count % 3 == 0:
            group_common_types.append(common_logic.find_common_elements_between_all_list_items(rucksack_group))
            rucksack_group = []
    print(sum([scoring.alphabet_lower_upper_1to52.index(common_type[0]) for common_type in group_common_types]))


def main():
    solve1()
    solve2()


main()
