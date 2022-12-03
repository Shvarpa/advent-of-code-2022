def f_iter(f):
    while True:
        l: "str" = f.readline()
        if l == "":
            return
        yield l.strip()

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

def part_1():
    result = 0
    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            middle = math.floor(len(l) / 2)
            A, B = l[:middle], l[middle:]
            sA, sB = get_stats(A), get_stats(B)
            collisions = set(sA.keys()).intersection(sB.keys())
            for collision in collisions:
                # print(collision, calc_priority(collision))
                result += calc_priority(collision)
            # results.append([A,B])
    print(result)

def part_2():
    result = 0
    with open("sample.txt", "r") as f:
        for lines in f_iter_count(f, 3):
            A,B,C = lines
            sA, sB, sC = get_stats(A), get_stats(B), get_stats(C)
            collisions = set(sA.keys()).intersection(sB.keys()).intersection(sC.keys())
            for collision in collisions:
                # print(collision, calc_priority(collision))
                result += calc_priority(collision)
    print(result)

part_1()
part_2()