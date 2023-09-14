import queue
import common.input_parsers as common_input


def solve1():
    comms = common_input.read_puzzle_input_as_string(6)
    window = queue.Queue(maxsize=4)
    count = 0
    for c in comms:
        if window.full():
            window.get()
        window.put(c)
        count += 1
        if len(set(list(window.queue))) == 4:
            print(count)
            print(list(window.queue))
            return

def solve2():
    comms = common_input.read_puzzle_input_as_string(6)
    window = queue.Queue(maxsize=14)
    count = 0
    for c in comms:
        if window.full():
            window.get()
        window.put(c)
        count += 1
        if len(set(list(window.queue))) == 14:
            print(count)
            print(list(window.queue))
            return


def main():
    solve1()
    solve2()


main()
