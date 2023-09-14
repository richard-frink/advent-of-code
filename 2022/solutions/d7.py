
import common.input_parsers as common_input
import common.logical_functions as common_logic


def solve1():
    command_lines = common_input.read_puzzle_input_as_list(7)
    tree = common_logic.convert_directory_comands_to_tree(command_lines)
    total_across_directories = 0
    directories_with_totals = {}

    # for every directory, if we don't have disk sizes for every item then we aren't done
    while not all([all([' ' in x for x in v]) for k,v in tree.items()]):
        for k,v in tree.items():
            # if every item in the given directory has disk sizes then we can count it
            if all([' ' in x for x in v]):
                total = sum([int(x.split(' ')[0]) for x in v])
                directories_with_totals[k] = total
                # since we have the total, lets put that number everywhere this directory is referenced
                for k2, v2 in tree.items():
                    for item in v2:
                        if item == k: # if the directory we got a total for is in they keys list, swap it
                            v2[v2.index(item)] = str(total) + ' ' + item
                            tree[k2] = v2
    print(tree)

def solve2():
    command_lines = common_input.read_puzzle_input_as_list(7)


def main():
    solve1()
    solve2()


main()
