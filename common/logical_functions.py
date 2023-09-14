def halve_and_find_common_elements(list_to_split):
    midpoint = int(len(list_to_split) / 2)
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
