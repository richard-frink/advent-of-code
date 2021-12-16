import pandas as pd


def read_input():
    return pd.read_csv('../inputs/input3.txt', delim_whitespace=True, header=None)

def solve1(input):
    gamma = "000100011001"
    epsilon = "111011100110"
    dec_gamma = int(gamma, 2)
    dec_epsilon = int(epsilon, 2)
    power = dec_gamma * dec_epsilon
    print("power: " + str(power))

def solve2(input):
    for column in input:
        print (input)
        frame= input[column]
        mode = frame.mode()
        # this is for the oxy Logic
        #if mode.shape [0] > 1:
        # mode = 1
        #else:
        # mode=mode.iloc[0]
        # this is for the c02 Logic
        if mode.shape [0] > 1:
            mode = 0
        elif mode.iloc [0] == 1:
            mode = 0
        else:
            mode = 1
        print("mode: " + str(mode))
        print("count: " + str(input.count))
        if input.shape [0] > 1:
            input = input[input[column] == mode]

    oxy = "011010001111"
    c02 = "111001000000"
    dec_oxy = int(oxy, 2)
    dec_c02 = int(c02, 2)
    life = dec_oxy*dec_c02
    print("life: " + str(life))

def main():
    input = read_input()
    solve1(input)
    solve2(input)

main()