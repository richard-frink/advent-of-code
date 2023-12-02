import common.input_parsers as common_input


def solve1():
    puzzle_input = common_input.read_puzzle_input_as_list(2)
    final = 0
    for index, game in enumerate(puzzle_input):
        possible = True
        rounds = game.split(":")[1].split(";")
        for r in rounds:
            cubes = r.split(",")
            for draw in cubes:
                vals = draw.split(" ")
                if "d" in vals[2]:  # red
                    if int(vals[1]) > 12:
                        possible = False
                        break
                if "g" in vals[2]:  # green
                    if int(vals[1]) > 13:
                        possible = False
                        break
                if "b" in vals[2]:  # blue
                    if int(vals[1]) > 14:
                        possible = False
                        break
                if not possible:
                    break
        if possible:
            final += (index + 1)
    print(final)


def solve2():
    puzzle_input = common_input.read_puzzle_input_as_list(2)
    final = 0
    for index, game in enumerate(puzzle_input):
        m_r, m_g, m_b = 0,0,0
        rounds = game.split(":")[1].split(";")
        for r in rounds:
            cubes = r.split(",")
            for draw in cubes:
                vals = draw.split(" ")
                if "d" in vals[2]:  # red
                    if int(vals[1]) > m_r:
                        m_r = int(vals[1])
                if "g" in vals[2]:  # green
                    if int(vals[1]) > m_g:
                        m_g = int(vals[1])
                if "b" in vals[2]:  # blue
                    if int(vals[1]) > m_b:
                        m_b = int(vals[1])
        final += (m_r*m_g*m_b)
    print(final)


def main():
    solve1()
    solve2()


main()
