import common.input_parsers as common_input
import common.logical_functions as common_logic


def solve1():
    puzzle_cargo = common_input.read_puzzle_input_as_list(5, '-lists')
    puzzle_moves = common_input.read_puzzle_input_as_list(5, '-moves')
    for raw_move in puzzle_moves:
        move = raw_move.split(' ')  # 0-move 1-[num] 2-from 3-[num] 4-to 5-[num]
        for x in range(int(move[1])):
            l1, l2 = common_logic.move_top_of_one_stack_to_another_stack(list(puzzle_cargo[int(move[3]) - 1]),
                                                                         list(puzzle_cargo[int(move[5]) - 1]))
            puzzle_cargo[int(move[3]) - 1] = ''.join(l1)
            puzzle_cargo[int(move[5]) - 1] = ''.join(l2)
    print(''.join([x[-1] for x in puzzle_cargo]))


def solve2():
    puzzle_cargo = common_input.read_puzzle_input_as_list(5, '-lists')
    puzzle_moves = common_input.read_puzzle_input_as_list(5, '-moves')
    for raw_move in puzzle_moves:
        move = raw_move.split(' ')  # 0-move 1-[num] 2-from 3-[num] 4-to 5-[num]
        l1, l2 = common_logic.move_top_of_one_stack_to_another_stack(list(puzzle_cargo[int(move[3]) - 1]),
                                                                     list(puzzle_cargo[int(move[5]) - 1]),
                                                                     int(move[1]))
        puzzle_cargo[int(move[3]) - 1] = ''.join(l1)
        puzzle_cargo[int(move[5]) - 1] = ''.join(l2)
    print(''.join([x[-1] for x in puzzle_cargo]))


def main():
    solve1()
    solve2()


main()
