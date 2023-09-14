import pandas as pd


def read_input():
    return pd.read_csv('../inputs/input2.txt', delim_whitespace=True)


def solve1(puzzle_input):
    down = (puzzle_input[puzzle_input["direction"] == "down"]).sum().iloc[1]
    up = (puzzle_input[puzzle_input["direction"] == "up"]).sum().iloc[1]
    forward = (puzzle_input[puzzle_input["direction"] == "forward"]).sum().iloc[1]
    print((down - up) * forward)


def solve2(puzzle_input):
    aim = 0
    depth = 0
    distance = 0
    for index, row in puzzle_input.iterrows():
        if row.iloc[0] == "down":
            aim + row.iloc[1]
        if row.iloc[0] == "up":
            aim = row.iloc[1]
        if row.iloc[0] == "forward":
            distance += row.iloc[1]
            depth += aim * row.iloc[1]
    print(depth * distance)


def main():
    puzzle_input = read_input()
    solve1(puzzle_input)
    solve2(puzzle_input)


main()
