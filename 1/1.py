results = []
done = False
with open("1.txt", "r") as f:
    while not done:
        elf = []
        while True:
            l = f.readline()
            if l == "":
                done = True
                break
            l = l.strip()
            if l == "":
                break
            elf.append(int(l))
        results.append(sum(elf))

results.sort()
print(results[-1] + results[-2] + results[-3])
