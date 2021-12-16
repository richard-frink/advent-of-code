import pandas as pd


def read_input():
    return pd.read_csv('../inputs/input##.txt', delim_whitespace=True, header=None)

def solve1(input):
    print(input)

def solve2(input):
    print(input)

def main():
    input = read_input()
    solve1(input)
    solve2(input)

main()