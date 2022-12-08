from pprint import pprint
import math


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


class Info:
    top: "int" = 0
    left: "int" = 0
    bottom: "int" = 0
    right: "int" = 0
    value: "int" = 0
    visible = True

    def __init__(self, value: "int") -> None:
        self.value = value

    def __str__(self) -> str:
        # return f"(({self.left}, {self.top}), ({self.right}, {self.bottom}))"
        return f"{'T' if self.visible else 'F'},{self.value}:{self.top},{self.left},{self.bottom},{self.right}"

    def __repr__(self) -> str:
        return str(self)


def part_1():
    grid = []
    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            grid.append([int(a) for a in l])
    rows = len(grid)
    cols = len(grid[0])
    infos = [[Info(grid[y][x]) for x in range(cols)] for y in range(rows)]

    # circle
    for y in [0, rows - 1]:
        for x in range(cols):
            infos[y][x].top = grid[y][x]
            infos[y][x].left = grid[y][x]
            infos[y][x].bottom = grid[y][x]
            infos[y][x].right = grid[y][x]

    for y in range(rows):
        for x in [0, cols - 1]:
            infos[y][x].top = grid[y][x]
            infos[y][x].left = grid[y][x]
            infos[y][x].bottom = grid[y][x]
            infos[y][x].right = grid[y][x]

    # topleft
    for y in range(1, rows):
        for x in range(1, cols):
            infos[y][x].top = max((infos[y - 1][x].top, grid[y][x]))
            infos[y][x].left = max((infos[y][x - 1].left, grid[y][x]))

    # bottomright
    for y in range(rows - 2, -1, -1):
        for x in range(cols - 2, -1, -1):
            infos[y][x].bottom = max((infos[y + 1][x].bottom, grid[y][x]))
            infos[y][x].right = max((infos[y][x + 1].right, grid[y][x]))

    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            value = grid[y][x]
            top = infos[y - 1][x].top
            left = infos[y][x - 1].left
            bottom = infos[y + 1][x].bottom
            right = infos[y][x + 1].right
            visible = value > top or value > left or value > bottom or value > right
            # print((x, y), value, visible, [top, left, bottom, right])
            infos[y][x].visible = visible

    result = 0
    for y in range(rows):
        for x in range(cols):
            if infos[y][x].visible:
                result += 1
    print(result)

    # pprint(grid)
    # pprint(infos)


def part_2():
    grid = []
    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            grid.append([int(a) for a in l])
    rows = len(grid)
    cols = len(grid[0])

    top_score = 0
    for y in range(cols):
        for x in range(rows):
            # iterate up
            value = grid[y][x]
            def count_break(it):
                c = 0
                for a in it:
                    c += 1
                    if a >= value:
                        break
                return c

            top = (grid[_y][x] for _y in range(y - 1, -1, -1))
            left = (grid[y][_x] for _x in range(x - 1, -1, -1))
            bottom = (grid[_y][x] for _y in range(y + 1, cols, 1))
            right = (grid[y][_x] for _x in range(x + 1, rows, 1))

            # if x == 2 and y == 3:
            #     print("*")

            t = count_break(top)
            l = count_break(left)
            b = count_break(bottom)
            r = count_break(right)
            score = t * l * b * r
            # print((x,y,value, score),[t, l, b, r])
            if score > top_score:
                top_score = score
    print(top_score)

part_1()
part_2()
