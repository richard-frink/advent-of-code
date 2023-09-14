from collections import defaultdict


def halve_and_find_common_elements(list_to_split):
    midpoint = int(len(list_to_split)/2)
    half1 = list_to_split[:midpoint]
    half2 = list_to_split[midpoint:]
    return list(set(half1).intersection(half2))


# this input
# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# would return 'r'
def find_common_elements_between_all_list_items(list_of_items):
    working_list = list_of_items[0]
    for item in list_of_items:
        working_list = list(set(working_list).intersection(item))
    return working_list


def move_top_of_one_stack_to_another_stack(stack1, stack2, items_to_pick_up_at_once=1):
    temp_stack = []
    for x in range(items_to_pick_up_at_once):
        temp_stack.append(stack1.pop())
    for x in reversed(temp_stack):
        stack2.append(x)
    return stack1, stack2


# possible commands are:
# cd, ls
# ls can result in ->
#   "23453 file.txt" meaning file size and filename
#   or "dir something" meaning directory with a given name
def convert_directory_comands_to_tree(command_lines):
    tree = defaultdict(list)
    active_folder = '/'
    active_ls_command = False
    ls_results = []
    test = 'sdc'
    for line in command_lines:
        if active_ls_command:
            if '$' in line: # we've moved on from our ls
                active_ls_command = False
                for ls_result in ls_results: # handle the ls results
                    if ls_result.startswith('dir'):
                        tree[active_folder].append(ls_result[4:])
                        continue
                    else:
                        tree[active_folder].append(ls_result)
                        continue
                ls_results = []
            else: # add results from ls
                ls_results.append(line)
                continue
        if '$ cd' in line:
            if line == '$ cd ..':
                for k,v in tree.items():
                    if v == active_folder:
                        active_folder = k
            active_folder = line.split(' ')[2]
            continue
        if line == '$ ls':
            active_ls_command = True
            continue
    return tree
