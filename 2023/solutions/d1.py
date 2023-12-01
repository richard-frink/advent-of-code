import common.input_parsers as common_input


def solve1():
    puzzle_input = common_input.read_puzzle_input_as_list(1)
    to_sum = []
    for line in puzzle_input:
        first, last = -1,-1
        for c in line:
            if c not in "qwertyuiopasdfghjklzxcvbnm":
                first = c
                break
        for c in line[::-1]:
            if c not in "qwertyuiopasdfghjklzxcvbnm":
                last = c
                break
        to_sum.append(int(str(first)+str(last)))
    print(sum(to_sum))


def solve2():
    puzzle_input = common_input.read_puzzle_input_as_list(1)
    to_sum = []
    d = {"one": "o1e",
         "two": "t2o",
         "three": "t3e",
         "four": "f4r",
         "five": "f5e",
         "six": "s6x",
         "seven": "s7n",
         "eight": "e8t",
         "nine": "n9e"}
    for line in puzzle_input:
        for k in d.keys():
            line = line.replace(k, str(d[k]))
        first, last = -1,-1
        for c in line:
            if c not in "qwertyuiopasdfghjklzxcvbnm":
                first = c
                break
        for c in line[::-1]:
            if c not in "qwertyuiopasdfghjklzxcvbnm":
                last = c
                break
        to_sum.append(int(str(first)+str(last)))
    print(sum(to_sum))


def main():
    solve1()
    solve2()


main()
