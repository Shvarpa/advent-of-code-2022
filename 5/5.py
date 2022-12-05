def f_iter(f):
    while True:
        l: "str" = f.readline()
        if l == "":
            return
        if l[-1] == "\n":
            yield l[:-1]
        else:
            yield l


def f_iter_count(f, count=1):
    group = []
    while True:
        l: "str" = f.readline()
        if l == "":
            if len(group) > 0:
                yield group
            return
        group.append(l.strip())
        if len(group) >= count:
            yield group
            group.clear()


import math


def calc_priority(letter: "str"):
    ol = ord(letter)
    oa = ord("a")
    oA = ord("A")
    return ol - oa + 1 if ol >= oa else ol - oA + 27


def get_proirities(sack: "list[str]"):
    return [calc_priority(item) for item in sack]


def get_stats(sack: "list[str]"):
    result = {}
    for letter in sack:
        result[letter] = result.get(letter, 0) + 1
    return result


def get_priority_stats(sack: "list[int]"):
    appears = [0] * 52
    for priority in sack:
        appears[priority] += 1
    return appears

# def find_collisions(A: "dict", B: "dict"):
#     return set(A.keys()).intersection(B.keys())


def list_add(l):
    if len(l) <= 0:
        return None
    result = l[0]
    for i in l[1:]:
        result += i
    return result

# results = []


def contains(A, B):
    a0, a1 = A
    b0, b1 = B
    return a0 <= b0 and a1 >= b1


def intersects(A, B):
    a0, a1 = A
    b0, b1 = B
    return (a0 <= b0 and b0 <= a1) or (a0 <= b1 and b1 <= a1)


def to_int(arr):
    return [int(a) for a in arr]

def read_line(line: "str"):
    result = []
    while True:
        if len(line) <= 0:
            break
        result.append(line[:3])
        line = line[4:]
    return result

import re

def split(lst: "list", index):
    return lst[:index], lst[index:]


def part_1():
    result = 0
    with open("sample.txt", "r") as f:
        state = []
        for l in f_iter(f):
            if l == "":
                break
            state.append(l)
        state.reverse()
        stack_index = state[0].split("   ")
        stacks = [[] for i in range(len(stack_index))]
        for l in state[1:]:
            l = read_line(l)
            # print(len(stack_index), len(l), l)
            for i, item in enumerate(l):
                item: "str" = item.strip()
                if item != "":
                    stacks[i].append(item)
        # op = 0
        # print(f"op {op}:")
        # for stack in stacks:
        #     print(stack)
        # op += 1
        for l in f_iter(f):
            amount, _from, _to = to_int(re.compile("move (\d+) from (\d+) to (\d)").match(l).groups())
            _from -= 1
            _to -= 1
            stacks[_from], temp = split(stacks[_from], len(stacks[_from]) - amount)
            # temp.reverse() # part2
            stacks[_to] = stacks[_to] + temp
            # print(f"op {op}: {l}")
            # for stack in stacks:
            #     print(stack)
            # op += 1
        print([stack[-1] for stack in stacks if len(stack) > 0])


# def part_2():
#     result = 0
#     with open("sample.txt", "r") as f:
#         for l in f_iter(f):
#             A, B = l.split(",")
#             A, B = to_int(A.split("-")), to_int(B.split("-"))
#             # print(A,B,intersects(A,B), intersects(B,A))
#             if intersects(A, B) or intersects(B, A):
#                 result += 1
#     print(result)


part_1()
# part_2()
