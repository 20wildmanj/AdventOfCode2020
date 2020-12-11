

def isOpen(map,row,pos,seatLen):
    check = [pos - 1, pos, pos + 1]
    checkMid = [pos - 1, pos + 1]
    if (row > 0):
        for i in check:
            if i >= 0 and i < seatLen and map[row - 1][i] == "#":
                return False
    for i in checkMid:
        if i >= 0 and i < seatLen and map[row][i] == "#":
            return False
    if (row < len(map) - 1):
        for i in check:
            if i >= 0 and i < seatLen and map[row + 1][i] == "#":
                return False
    return True


def fourOrMore(map,row,pos,seatLen):
    count = 0
    check = [pos-1,pos,pos+1]
    checkMid = [pos-1,pos+1]
    if (row > 0):
        for i in check:
            if i >= 0 and i < seatLen and map[row-1][i] == "#":
                count += 1
    for i in checkMid:
        if i >= 0 and i < seatLen and map[row][i] == "#":
            count += 1
    if (row < len(map)-1):
        for i in check:
            if i >= 0 and i < seatLen and map[row+1][i] == "#":
                count += 1
    #print("four",row,pos,count)
    return count >= 4
def isCrowd(map,row,pos,seatLen):
    count = 0
    check = [pos-1,pos,pos+1]
    checkMid = [pos-1,pos+1]
    r = row+1
    r2 = row-1
    sight = [True]*6

    for r3 in range(row+1,len(map)):
        if map[r3][pos] == "L":
            break
        elif map[r3][pos] == "#":
            count += 1
            break
    for r3 in range(row-1, -1,-1):
        if map[r3][pos] == "L":
            break
        elif map[r3][pos] == "#":
            count += 1
            break

    for i in range(pos+1,seatLen):
        if (r2 >= 0):
            if map[r2][i] == "#" and sight[0]:
                count += 1
            if sight[0] and map[r2][i] != ".":
                sight[0] = False
        if (map[row][i] == "#" and sight[1]):
            count += 1
        if sight[1] and map[row][i] != ".":
            sight[1] = False
        if (r < len(map)):
            if map[r][i] == "#" and sight[2]:
                count += 1
            if sight[2] and map[r][i] != ".":
                sight[2] = False
        r += 1
        r2 -= 1
    r = row + 1
    r2 = row - 1
    for i in range(pos-1,-1,-1):
        if (r2 >= 0):
            if map[r2][i] == "#" and sight[3]:
                count += 1
            if sight[3] and map[r2][i] != ".":
                sight[3] = False
        if (map[row][i] == "#" and sight[4]):
            count += 1
        if sight[4] and map[row][i] != ".":
            sight[4] = False
        if (r < len(map)):
            if map[r][i] == "#" and sight[5]:
                count += 1
            if sight[5] and map[r][i] != ".":
                sight[5] = False
        r += 1
        r2 -= 1
    #print("four", row, pos, count,sight)

    return count >= 5
def isOpen2(map,row,pos,seatLen):
    count = 0

    r = row+1
    r2 = row-1
    sight = [True]*6

    for r3 in range(row+1,len(map)):
        if map[r3][pos] == "L":
            break
        elif map[r3][pos] == "#":
            return False

    for r3 in range(row-1, -1,-1):
        if map[r3][pos] == "L":
            break
        elif map[r3][pos] == "#":
            return False

    for i in range(pos+1,seatLen):
        if (r2 >= 0):
            if map[r2][i] == "#" and sight[0]:
                return False
            if sight[0] and map[r2][i] != ".":
                sight[0] = False
        if (map[row][i] == "#" and sight[1]):
            return False
        if sight[1] and map[row][i] != ".":
            sight[1] = False
        if (r < len(map)):
            if map[r][i] == "#" and sight[2]:
                return False
            if sight[2] and map[r][i] != ".":
                sight[2] = False
        r += 1
        r2 -= 1
    r = row + 1
    r2 = row - 1
    for i in range(pos-1,-1,-1):
        if (r2 >= 0):
            if map[r2][i] == "#" and sight[3]:
                return False
            if sight[3] and map[r2][i] != ".":
                sight[3] = False
        if (map[row][i] == "#" and sight[4]):
            return False
        if sight[4] and map[row][i] != ".":
            sight[4] = False
        if (r < len(map)):
            if map[r][i] == "#" and sight[5]:
                return False
            if sight[5] and map[r][i] != ".":
                sight[5] = False
        r += 1
        r2 -= 1
    #print("checxk", row, pos, count,sight)

    return True
def part1():
    file1 = open("part11.txt","r")
    map = []
    for line in file1.readlines():
        map.append(list(line.replace("\n","")))
    changed = True
    seatLen = len(map[0])
    while changed:
        newMap = []
        for row in range(len(map)):
            newMap.append([None]*seatLen)
            for pos in range(seatLen):
                if (map[row][pos] != "."):
                    if (map[row][pos] == "L" and isOpen(map,row,pos,seatLen)):
                        newMap[row][pos] = "#"
                    elif (map[row][pos] == "#" and fourOrMore(map,row,pos,seatLen)):
                        newMap[row][pos] = "L"
                    else:
                        newMap[row][pos] = map[row][pos];
                else:
                    newMap[row][pos] = "."

        if newMap == map:
            changed = False
        else:
            map = newMap
    count = 0
    for line in map:
        for pos in line:
            if pos == "#":
                count += 1
        print(line)
    print(count)

def part2():
    file1 = open("part11.txt","r")
    map = []
    for line in file1.readlines():
        map.append(list(line.replace("\n","")))
    changed = True
    seatLen = len(map[0])
    while changed:
        newMap = []
        for row in range(len(map)):
            newMap.append([None]*seatLen)
            for pos in range(seatLen):
                if (map[row][pos] != "."):
                    if (map[row][pos] == "L" and isOpen2(map,row,pos,seatLen)):
                        newMap[row][pos] = "#"
                    elif (map[row][pos] == "#" and isCrowd(map,row,pos,seatLen)):
                        newMap[row][pos] = "L"
                    else:
                        newMap[row][pos] = map[row][pos];
                else:
                    newMap[row][pos] = "."


        if newMap == map:
            changed = False
        else:
            map = newMap
    count = 0
    for line in map:
        for pos in line:
            if pos == "#":
                count += 1
        print(line)
    print(count)

if __name__ == "__main__":
    #part1()
    part2()