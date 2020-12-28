
import copy

def get_neighbors(x,y,z,dictionary):
    count = 0
    for z1 in range(z-1,z+2):
        for y1 in range(y-1,y+2):
            for x1 in range(x-1,x+2):
                if ((x1,y1,z1) in dictionary and (x1,y1,z1) != (x,y,z)):
                    count += 1
    #print("count", x,y,z,count)
    return count


def part1():
    file1 = open("part17.txt","r")
    lines = file1.readlines()
    activeDict = {}
    for y1 in range(len(lines)):
        lines[y1] = lines[y1].replace("\n","")
        for x1 in range(len(lines[y1])):
            if (lines[y1][x1] == "#"):
                coord = (x1-(len(lines[y1])//2),y1-(len(lines)//2),0)
                print(coord)
                activeDict[coord] = 1
    
    zSlice = 1
    xSlice = len(lines[0])
    ySlice = len(lines)
    for iter in range(6):
        currDict = copy.deepcopy(activeDict)
        for z in range(0-(zSlice//2)-1,(zSlice//2)+2,1):
            for y in range(0-(ySlice//2)-1,(ySlice//2)+2,1):
                for x in range(0-(xSlice//2)-1,(xSlice//2)+2,1):
                    if ((x,y,z) in activeDict):
                        if not (get_neighbors(x,y,z,activeDict) == 2 or get_neighbors(x,y,z,activeDict) == 3):
                            currDict.pop((x,y,z))
                    else:
                        if get_neighbors(x,y,z,activeDict) == 3:
                            currDict[(x,y,z)] = 1
        activeDict = currDict
        zSlice += 2
        xSlice += 2
        ySlice += 2
        count = 0
        for vals in activeDict.keys():
            count += 1
        print(count)
        
def get_neighbors4d(x,y,z,w,dictionary):
    count = 0
    for w1 in range(w-1,w+2):
        for z1 in range(z-1,z+2):
            for y1 in range(y-1,y+2):
                for x1 in range(x-1,x+2):
                    if ((x1,y1,z1,w1) in dictionary and (x1,y1,z1,w1) != (x,y,z,w)):
                        count += 1
    return count


def part2():
    file1 = open("part17.txt","r")
    lines = file1.readlines()
    activeDict = {}
    for y1 in range(len(lines)):
        lines[y1] = lines[y1].replace("\n","")
        for x1 in range(len(lines[y1])):
            if (lines[y1][x1] == "#"):
                coord = (x1-(len(lines[y1])//2),y1-(len(lines)//2),0,0)
                print(coord)
                activeDict[coord] = 1
    
    wSlice = 1
    zSlice = 1
    xSlice = len(lines[0])
    ySlice = len(lines)
    for iter in range(6):
        currDict = copy.deepcopy(activeDict)
        for w in range(0-(wSlice//2)-1,(wSlice//2)+2,1):
            for z in range(0-(zSlice//2)-1,(zSlice//2)+2,1):
                for y in range(0-(ySlice//2)-1,(ySlice//2)+2,1):
                    for x in range(0-(xSlice//2)-1,(xSlice//2)+2,1):
                        neighbors = get_neighbors4d(x,y,z,w,activeDict)
                        if ((x,y,z,w) in activeDict):
                            if not (neighbors == 2 or neighbors == 3):
                                currDict.pop((x,y,z,w))
                        else:
                            if neighbors == 3:
                                currDict[(x,y,z,w)] = 1
        activeDict = currDict
        zSlice += 2
        xSlice += 2
        ySlice += 2
        wSlice += 2
        count = 0
        for vals in activeDict.keys():
            count += 1
        print(count)


if __name__ == "__main__":
    part1()
    part2()