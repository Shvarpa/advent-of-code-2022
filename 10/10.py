from pprint import pprint
import math
from re import L
from unittest import result


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

# def manhatan_distance(A):
#     return sum(abs(a) for a in A)

def part_1():
    reg_x = 1
    cycle = 1

    signals = [20, 60, 100, 140, 180, 220]
    signals_index = 0
    results = [None] * len(signals)
    
    with open("10.txt", "r") as f:
        for l in f_iter(f):
            # if l.startswith("addx"):
            command, number = "", 0
            args = l.split(" ")
            if len(args) == 2:
                command, _number = args
                number = int(_number)
            else:
                command = args[0]

            if command == "noop":
                cycle += 1
            
            elif command == "addx":
                cycle += 2
            
            if cycle > signals[signals_index]:
                # print("*", cycle, reg_x)
                results[signals_index] = reg_x
                signals_index += 1
                if signals_index >= len(signals):
                    break


            reg_x += number
            # print(l, ":", cycle, reg_x, command == "noop")
        
        # print(results)

    res = 0
    for result, ampl in zip(results, signals):
        res += result * ampl
    print(res)

def part_2():
    reg_x = 1
    cycle = 0

    signals = [20, 60, 100, 140, 180, 220]
    signals_index = 0
    results = [None] * len(signals)

    w = 40
    h = 6
    grid = [["." for x in range(w)] for y in range(h)]

    def cycle_to_xy(cycle = cycle):
        return cycle % w, math.floor(cycle / w)


    sprite = "###" + "." * (w - 3)
    def get_sprite_i(i, reg_x=reg_x):
        return sprite[(i - reg_x + 1) % w]

    def get_sprite(reg_x=reg_x):
        return "".join(get_sprite_i(i, reg_x) for i in range(w))

    # print(get_sprite(1))
    # print(get_sprite(16))
    # x,y = cycle_to_xy(39)
    # grid[y][x] = "#"

    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            # if l.startswith("addx"):
            command, number = "", 0
            args = l.split(" ")
            if len(args) == 2:
                command, _number = args
                number = int(_number)
            else:
                command = args[0]

            last_cycle = cycle

            if command == "noop":
                cycle += 1
            
            elif command == "addx":
                cycle += 2

            for c in range(last_cycle, cycle):
                x,y = cycle_to_xy(c)
                try:
                    grid[y][x] = get_sprite_i(x, reg_x)
                except:
                    break

            reg_x += number

            if cycle >= (w * h):
                break
        

    pprint(tuple("".join(row) for row in grid))

part_1()
part_2()