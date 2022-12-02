def f_iter(f):
    while True:
        l: "str" = f.readline()
        if l == "":
            return
        yield l.strip()

# def win(rival, choice):
#     return (rival == "A" and choice == "Y") or (rival == "B" and choice == "Z") or (rival == "C" and choice == "X")

# def draw(rival, choice):
#     return (rival == "A" and choice == "X") or (rival == "B" and choice == "Y") or (rival == "C" and choice == "Z")

piece_dict = {
    "A": 0,
    "B": 1,
    "C": 2
}

win_dict = {
    0: 3,
    1: 6,
    2: 0,
}

choice_dict = {
    0: 1,
    1: 2,
    2: 3
}

result_dict = {
    "X": 2,
    "Y": 0,
    "Z": 1,
}


def decide_choice(rival, result):
    return (rival + result) % 3

def calc_result(rival, choice):
    return (choice - rival + 3) % 3

# def calc_score(rival, choice):
#     result = (((ord(choice) - ord('X')) - (ord(rival) - ord('A')) + 3) % 3)
#     # result = (ord(choice) - ord('X')) - (ord(rival) - ord('A'))
#     return win_dict[result] + choice_dict[choice]

def calc_score(result, choice):
    return win_dict[result] + choice_dict[choice]
    
    
results = []
with open("2.txt", "r") as f:
    for l in f_iter(f):
        rival, result = l.split(" ")
        result = result_dict[result]
        rival = piece_dict[rival]
        choice = decide_choice(rival, result)
        _result = calc_result(rival, choice)
        if _result != result:
            print("ERROR")
        results.append(calc_score(_result, choice))
        
print(sum(results))