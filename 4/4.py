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

def part_1():
    result = 0
    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            A,B = l.split(",")
            A,B = to_int(A.split("-")), to_int(B.split("-"))
            # print(A,B,contains(A,B), contains(B,A))
            if contains(A,B) or contains(B,A):
                result += 1
    print(result)


def part_2():
    result = 0
    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            A,B = l.split(",")
            A,B = to_int(A.split("-")), to_int(B.split("-"))
            # print(A,B,intersects(A,B), intersects(B,A))
            if intersects(A,B) or intersects(B,A):
                result += 1
    print(result)

part_1()
part_2()