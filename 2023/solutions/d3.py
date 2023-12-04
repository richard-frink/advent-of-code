import common.input_parsers as common_input


# number_locations and special char locations will be like { (r,c): number / or special_char}
def find_all_positions(schematic, special_char_list):
    number_locations, true_num_loactions, special_char_locations = {}, {}, {}
    nums = "1234567890"
    for row, line in enumerate(schematic):
        working_num = ""
        for col, c in enumerate(line):
            if c in nums:
                working_num += c
            if c not in nums or col == len(line) - 1:
                temp_key = working_num + str(row) + str(col) + str(c)
                for i in range(len(working_num)):
                    number_locations[(row, ((col - 1) - i))] = temp_key
                if working_num != "":
                    true_num_loactions[temp_key] = int(working_num)
                working_num = ""
            if c not in nums and c != ".":
                if special_char_list is None:
                    special_char_locations[(row, col)] = c
                else:
                    if c in special_char_list:
                        special_char_locations[(row, col)] = c
    return number_locations, true_num_loactions, special_char_locations

# wrong p1 answers
# 684261 too high
# 571728 too high
# 553825 last try - that was it
# 553816 didn't say
# 447651 too low


def solve1():
    puzzle_input = common_input.read_puzzle_input_as_list(3)
    num_locs, true_num_locs, spec_char_locs = find_all_positions(puzzle_input, None)
    total = 0
    adjacents = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
    for key in spec_char_locs.keys():
        for a in adjacents:
            check_me = (key[0] + a[0], key[1] + a[1])
            if check_me in num_locs:
                total += true_num_locs[num_locs[check_me]]
                true_num_locs[num_locs[check_me]] = 0
    print(total)


# 34408256 - too low
# 93994191


def solve2():
    puzzle_input = common_input.read_puzzle_input_as_list(3)
    num_locs, true_num_locs, spec_char_locs = find_all_positions(puzzle_input, ["*"])
    total = 0
    adjacents = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
    for key in spec_char_locs.keys():
        possible = []
        keys_observed = []
        for a in adjacents:
            check_me = (key[0] + a[0], key[1] + a[1])
            if check_me in num_locs and num_locs[check_me] not in keys_observed:
                possible.append(true_num_locs[num_locs[check_me]])
                keys_observed.append(num_locs[check_me])
        if len(possible) == 2:
            total += possible[0]*possible[1]
    print(total)


def main():
    solve1()
    solve2()


main()
