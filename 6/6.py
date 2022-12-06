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

import typing
T = typing.TypeVar("T")
class RingBuffer(typing.Generic[T]):
    def __init__(self, size: int) -> None:
        self.size = size
        self.start = 0
        self.end = 0
        self.count = 0
        self.list: "list[T]" = [None] * self.size

    def push(self, item: "T"):
        self.list[self.end] = item
        self.end = (self.end + 1) % self.size
        if self.end == self.start:
            self.start = (self.start + 1) % self.size
        else:
            self.count += 1

    def __iter__(self):
        end = self.end
        # def gen():
        index = self.start
        end = self.end
        while True:
            if index == end:
                break
            yield self.list[index]
            index = (index + 1) % self.size
        # return gen()

    def __del__(self):
        self.clear()

    def clear(self):
        self.start = 0
        self.end = 0
        self.count = 0
        self.list: "list[T]" = [None] * self.size


def part_1():
    size = 4
    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            buffer = RingBuffer(size + 1)
            for i, item in enumerate(l):
                buffer.push(item)
                if len(set(buffer)) == size:
                    print(list(buffer))
                    print(i + 1)
                    break
                    


def part_2():
    size = 14
    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            buffer = RingBuffer(size + 1)
            for i, item in enumerate(l):
                buffer.push(item)
                if len(set(buffer)) == size:
                    print(list(buffer))
                    print(i + 1)
                    break
                    

part_1()
part_2()
