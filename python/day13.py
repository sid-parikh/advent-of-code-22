from functools import cmp_to_key
import utils

input_list = utils.get_list(13)
lists = list()
for line in input_list:
    line = line.strip()
    if line:
        lists.append((eval(line)))


def compare(a, b):
    if type(a) is int and type(b) is int:
        if b > a:
            return 1
        if a > b:
            return -1
        return 0
    elif type(a) is list and type(b) is list:
        i = j = 0
        while i < len(a) and j < len(b):
            n = compare(a[i], b[j])
            if n != 0:
                return n
            i += 1
            j += 1
        if i == len(a) and j == len(b):
            return 0
        if i == len(a):
            return 1
        return -1
    elif type(a) is int and type(b) is list:
        return compare([a], b)
    elif type(a) is list and type(b) is int:
        return compare(a, [b])

    raise Exception("Invalid input")


def part1():
    index = 1
    total = 0
    i = 0
    while i + 1 < len(lists):
        n = compare(lists[i], lists[i + 1])
        if n == 0:
            raise Exception("Invalid input")

        if n == 1:
            total += index
        index += 1
        i += 2

    print(total)


def part2():
    lists.append([[2]])
    lists.append([[6]])
    sorted_lists = sorted(lists, key=cmp_to_key(compare), reverse=True)

    a = sorted_lists.index([[2]]) + 1
    b = sorted_lists.index([[6]]) + 1
    print(a * b)


part1()
part2()
