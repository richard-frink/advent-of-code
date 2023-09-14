import pandas as pd


def read_exact_puzzle_input_to_dataframe(puzzle_num, extra_suffix=''):
    puzzle_input_file = '../inputs/input' + str(puzzle_num) + extra_suffix + '.txt'
    return pd.read_csv(puzzle_input_file, delim_whitespace=True, header=None, skip_blank_lines=False)


def read_puzzle_input_as_string(puzzle_num, extra_suffix=''):
    puzzle_input_file = '../inputs/input' + str(puzzle_num) + extra_suffix + '.txt'
    with open(puzzle_input_file) as file:
        for line in file:
            line = line.rstrip().lstrip().replace("\n", "").replace("  ", " ")
            return line


# looks like this
#####
# 123
# 234
# 456
#
# 153
# 624
#
# 624
# 918
# 452
# 701
def read_puzzle_input_as_list_of_lists_clustered_lines_blank_separators(puzzle_num, extra_suffix=''):
    puzzle_input_file = '../inputs/input' + str(puzzle_num) + extra_suffix + '.txt'
    final_input = []
    lines = []
    with open(puzzle_input_file) as file:
        for line in file:
            line = line.rstrip().lstrip().replace("\n", "").replace("  ", " ")
            if line == "":
                final_input.append(lines)
                lines = []
                continue
            lines.append(line)
    return final_input


# looks like this
#####
# r,234,456
# n,624
# k,918,452,701
def read_puzzle_input_as_list_of_lists_per_line(puzzle_num, separator, extra_suffix=''):
    puzzle_input_file = '../inputs/input' + str(puzzle_num) + extra_suffix + '.txt'
    final_input = []
    with open(puzzle_input_file) as file:
        for line in file:
            line = line.rstrip().lstrip().replace("\n", "").replace("  ", " ")
            if line == "":
                continue
            final_input.append(line.split(separator))
    return final_input


# looks like this
#####
# r,234,456
# n,624
# k,918,452,701
def read_puzzle_input_as_numerical_list_of_lists_per_line_no_separator(puzzle_num, extra_suffix=''):
    puzzle_input_file = '../inputs/input' + str(puzzle_num) + extra_suffix + '.txt'
    final_input = []
    with open(puzzle_input_file) as file:
        for line in file:
            line = line.rstrip().lstrip().replace("\n", "").replace("  ", " ")
            if line == "":
                continue
            row = []
            for c in line:
                row.append(int(c))
            final_input.append(row)
    return final_input


# looks like this
#####
# 56rth651h
# 651sdf6g54sdf
# 984eg3afr4e8
def read_puzzle_input_as_list(puzzle_num, extra_suffix=''):
    puzzle_input_file = '../inputs/input' + str(puzzle_num) + extra_suffix + '.txt'
    final_input = []
    with open(puzzle_input_file) as file:
        for line in file:
            line = line.rstrip().lstrip().replace("\n", "").replace("  ", " ")
            if line == "":
                continue
            final_input.append(line)
    return final_input
