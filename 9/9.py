from pprint import pprint
import math
from re import L


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


direction_to_step = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}


def tuple_add(A, B):
    return tuple(a + b for a, b in zip(A, B))


def tuple_sub(A, B):
    return tuple(a - b for a, b in zip(A, B))

# def manhatan_distance(A):
#     return sum(abs(a) for a in A)

def part_1():
    positions = set([(0,0)])
    t = h = 0, 0
    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            d, _c = l.split(" ")
            step, count = direction_to_step[d], int(_c)
            for i in range(count):
                h = tuple_add(h, step)
                diff = tuple_sub(h, t)
                distance = max(abs(a) for a in diff)
                t_add = tuple(1 if a > 0 else -1 if a < 0 else 0 for a in diff)
                if distance >= 2:
                    t = tuple_add(t, t_add)
                    positions.add(t)
                # print(t, h, diff, t_add, distance)
        # print(positions)
        print(len(positions))


def part_2():
    positions = set([(0,0)])
    t = h = 0, 0

    rope_length = 10
    rope = [(0,0) for i in range(rope_length)]
    
    with open("9.txt", "r") as f:
        for l in f_iter(f):
            d, _c = l.split(" ")
            step, count = direction_to_step[d], int(_c)
            for _ in range(count):
                rope[rope_length - 1] = tuple_add(rope[rope_length - 1], step)
                for i in range(rope_length - 1, 0, -1):
                    diff = tuple_sub(rope[i], rope[i-1])
                    distance = max(abs(a) for a in diff)
                    t_add = tuple(1 if a > 0 else -1 if a < 0 else 0 for a in diff)
                    if distance >= 2:
                        rope[i-1] = tuple_add(rope[i-1], t_add)
                # print(rope)
                positions.add(rope[0])
        print(len(positions))

# part_1()
part_2()
