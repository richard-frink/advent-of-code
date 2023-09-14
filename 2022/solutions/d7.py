import common.input_parsers as common_input


# taking this from online
def add_path_to_directories(path, directories):
    if path not in directories.keys():
        directories[path] = 0
    return directories


def get_sized_directories(command_lines):
    directories_size = {}
    current_stack = []
    current_path = ""
    for line in command_lines:
        if line.startswith("$ cd"):
            # maintaining directories list
            if not line.startswith("$ cd ..") and not line.startswith("$ cd /"):
                current_path += f"/{line.split()[-1]}" if current_path != "/" else line.split()[-1]
                current_stack.append(current_path)
                directories_size = add_path_to_directories(current_path, directories_size)
            # maintaining directories list
            elif line.strip() == "$ cd /":
                current_path = "/"
                current_stack = ["/"]
                directories_size = add_path_to_directories(current_path, directories_size)
            # maintaining directories list
            elif line.strip() == "$ cd ..":
                current_path = "/".join(current_path.split("/")[:-1])
                current_stack.pop()
        if line[0].isdigit():
            file_size = int(line.split()[0])
            # this will maintain a running list of all files per every possible directory path
            for directory in current_stack:
                directories_size[directory] += file_size
    return directories_size


def solve1():
    command_lines = common_input.read_puzzle_input_as_list(7)
    directories_size = get_sized_directories(command_lines)
    final_list = [el for el in directories_size.values() if el <= 100000]
    print(sum(final_list))


def solve2():
    command_lines = common_input.read_puzzle_input_as_list(7)
    directories_size = get_sized_directories(command_lines)
    current_root_size = directories_size["/"]
    space_to_free = current_root_size - 40000000
    final_list = sorted([el for el in directories_size.values() if el >= space_to_free])
    print(final_list[0])


def main():
    solve1()
    solve2()


main()
