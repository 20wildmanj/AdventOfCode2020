
def part1():
    file1 = open("part5.txt","r")
    seats = []
    maxID = 0

    for line in file1.readlines():
        row = [0,127]
        col = [0,7]
        line = line.replace("\n","")
        for i in range(7):
            if line[i] == "F":
                row[1] = (row[0] + row[1]) // 2
            elif line[i] == "B":
                row[0] = (row[0]+row[1]+1)//2
        for i in range(7,10):
            if line[i] == "L":
                col[1] = (col[0] + col[1]) // 2
            elif line[i] == "R":
                col[0] = (col[0] + col[1] + 1) // 2
        id = row[0]*8 +col[0]
        if id > maxID:
            maxID = id
        seats.append(id)
    print(maxID)
    seats.sort()

    for x in range(1,len(seats)-1):
        prev = seats[x-1]
        curr = seats[x]
        if (curr-prev > 1):
            print(prev,curr)

    print(seats)

if __name__ == "__main__":
    part1()