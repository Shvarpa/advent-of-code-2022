from pathlib import Path 
from pprint import pprint
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

def part_1():
    current_folder = Path("/")
    files = {}
    folders = {}
    folders[str(Path("/").resolve())] = 0
    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            sections = l.split(" ")
            try:
                files[str(current_folder / sections[1])] = int(sections[0])
            except:
                pass
            if sections[0] == "$":
                command = sections[1:]
                if command[0] == "cd":
                    current_folder = (current_folder / command[1]).resolve()
            elif sections[0] == "dir":
                # files[str(current_folder / sections[1])] = 0
                folders[str(current_folder / sections[1])] = 0
        pprint(files)
        for file, size in files.items():
            p = Path(file)
            while p.parent != p:
                p = p.parent
                folders[str(p)] += size
        pprint(folders)
        total_size = 0
        for folder, size in folders.items():
            if size < 100000:
                total_size += size
        print(total_size)



def part_2():
    current_folder = Path("/")
    files = {}
    folders = {}
    folders[str(Path("/").resolve())] = 0
    with open("sample.txt", "r") as f:
        for l in f_iter(f):
            sections = l.split(" ")
            try:
                files[str(current_folder / sections[1])] = int(sections[0])
            except:
                pass
            if sections[0] == "$":
                command = sections[1:]
                if command[0] == "cd":
                    current_folder = (current_folder / command[1]).resolve()
            elif sections[0] == "dir":
                # files[str(current_folder / sections[1])] = 0
                folders[str(current_folder / sections[1])] = 0
        pprint(files)
        free_space = 70000000
        for file, size in files.items():
            p = Path(file)
            while p.parent != p:
                p = p.parent
                folders[str(p)] += size
            free_space -= size
        pprint(folders)
        print(f"free_space = {free_space}")
        _folders = list(folders.items())
        _folders.sort(key=lambda i:i[1])
        for folder, size in _folders:
            if (free_space + size) > 30000000:
                print(folder, size)
                break
                  
part_1()
part_2()
