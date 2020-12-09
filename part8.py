


def part1():
    file1 = open("part8.txt","r")
    lines = file1.readlines()
    mark = [None]*len(lines)
    acc = 0
    looping = False
    iter = 0
    while iter in range(0,len(lines)) and not looping:
        line = lines[iter].replace("\n","").split()
        if mark[iter]:
            looping = True
        elif line[0] == "nop":
            mark[iter] = True
            iter += 1
        elif line[0] == "acc":
            acc += int(line[1])
            mark[iter] = True
            iter += 1
        elif line[0] == "jmp":
            mark[iter] = True
            iter += int(line[1])

    print(acc)
def jmpnop(lines):
    jmpnop = []
    for iter in range(0,len(lines)):
        line = lines[iter].replace("\n","").split()
        if line[0] == "nop" or line[0] == "jmp":
            jmpnop.append(iter)
    return jmpnop



def part2():
    file1 = open("part8.txt","r")
    lines = file1.readlines()
    linesToChange = jmpnop(lines)

    for x in range(0,len(linesToChange)):
        switch = linesToChange[x]
        iter = 0
        mark = [None] * len(lines)
        acc = 0
        looping = False
        while iter in range(0,len(lines)) and not looping:
            line = lines[iter].replace("\n","").split()
            if mark[iter]:
                looping = True
            elif line[0] == "nop" or (line[0] == "jmp" and iter == switch):
                mark[iter] = True
                iter += 1
            elif line[0] == "acc":
                acc += int(line[1])
                mark[iter] = True
                iter += 1
            elif line[0] == "jmp" or (line[0] == "nop" and iter == switch):
                mark[iter] = True
                iter += int(line[1])
        if iter >= len(lines):
            print(acc, switch)






if __name__ == "__main__":
    part1()
    part2()