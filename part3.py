


if __name__ == '__main__':
    file1 = open("part3.txt", "r")
    treeMap = []
    for line in file1.readlines():
        clean = line.replace("\n", "")
        treeMap.append(clean)
    x = 0
    y = 0
    count = 0
    strlen = len(treeMap[0])
    while (y < len(treeMap)):
        if (treeMap[y][x] == "#"):
            count += 1
        x += 3
        if (x >= strlen):
            x -= strlen
        y+=1
    print(count)
    moves = [(1, 1), (3, 1), (5, 1),(7, 1), (1, 2)]

    out = []
    for move in moves:
        count = 0
        x = 0
        y = 0
        while (y < len(treeMap)):
            if (treeMap[y][x] == "#"):
                count += 1
            x += move[0]
            if (x >= strlen):
                x -= strlen
            y += move[1]
        out.append(count)

    count = 1
    for x in out:
        count *= x
    print(out)
    print(count)

