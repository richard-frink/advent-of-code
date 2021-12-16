import pandas as pd

direction = 1
distance = 2

def read_input():
    return pd. read_csv('../inputs/input2.txt', delim_whitespace=True)

def solve1(input):
    down = (input[input["direction"] == "down"]).sum().iloc[1]
    up = (input [input["direction"] == "up"]).sum().iloc[1]
    forward = (input[input["direction"] == "forward"]).sum().iloc[1]
    print((down - up)*forward)

def solve2(input):
    aim = 0
    depth = 0
    distance = 0
    for index, row in input.iterrows():
        if row[0] == "down":
            aim + row[1]
        if row[0] == "up":
            aim = row[1]
        if row[0] == "forward":
            distance += row[1]
            depth += aim*row[1]
    print(depth*distance)

def main():
    input = read_input()
    solve1(input)
    solve2(input)

main()