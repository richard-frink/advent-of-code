import common.input_parsers as common_input
import common.logical_functions as common_logic


def solve1():
    grid = common_input.read_puzzle_input_as_numerical_list_of_lists_per_line_no_separator(8)
    # horizontally
    xi_edge_min = 0
    xi_edge_max = len(grid[0]) - 1

    # vertically
    yi_edge_min = 0
    yi_edge_max = len(grid) - 1


def solve2():
    grid = common_input.read_puzzle_input_as_list(8)


def main():
    solve1()
    solve2()


main()
