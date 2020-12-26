

def part1():
    file1 = open("part12.txt","r")
    coord = [0,0,90]
    for line in file1.readlines():
        line = line.replace("\n","")
        move = int(line[1:])
        if line[0] == "N":
            coord[1] += move
        elif line[0] == "S":
            coord[1] -= move
        elif line[0] == "E":
            coord[0] += move
        elif line[0] == "W":
            coord[0] -= move
        elif line[0] == "L":
            coord[2] -= move
        elif line[0] == "R":
            coord[2] += move
        elif line[0] == "F":
            if coord[2] % 360 == 90:
                coord[0] += move
            elif coord[2] % 360 == 0:
                coord[1] += move
            elif coord[2] % 360 == 180:
                coord[1] -= move
            elif coord[2] % 360 == 270:
                coord[0] -= move
        #print(coord)
def part2():
    file1 = open("part12.txt", "r")
    waypoint = [10,1]
    coord = [0, 0, 90]
    for line in file1.readlines():
        line = line.replace("\n", "")
        move = int(line[1:])
        if line[0] == "N":
            waypoint[1] += move
        elif line[0] == "S":
            waypoint[1] -= move
        elif line[0] == "E":
            waypoint[0] += move
        elif line[0] == "W":
            waypoint[0] -= move
        elif line[0] == "L":
            for x in range(0,move,90):
                temp = waypoint[0]
                waypoint[0] = -1*waypoint[1]
                waypoint[1] = temp
        elif line[0] == "R":
            for x in range(0,move,90):
                temp = waypoint[0]
                waypoint[0] = waypoint[1]
                waypoint[1] = -1*temp
        elif line[0] == "F":
            coord[0] += waypoint[0]*move
            coord[1] += waypoint[1]*move
        print(waypoint)
        print(coord)
    print(abs(coord[0])+abs(coord[1]))

if __name__ == "__main__":
    part1()
    part2()