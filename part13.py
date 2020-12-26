



def part1():
    file1 = open("part13.txt","r")
    lines = file1.readlines()
    target = int(lines[0])
    string = lines[1]
    x = 0
    start = -1
    end = -1
    buses = []
    while (x < len(string)):
        if (string[x] != "," and string[x] != "x"):
            start = x
            while (x < len(string) and string[x] != ","):
                x += 1
                end = x
            buses.append(int(string[start:end]))
        x += 1
    comp = [None]*len(buses)
    minimum = 0
    for i in range(len(buses)):
        if (int(target/buses[i])*buses[i] != target):
            comp[i] = int(target/buses[i])*buses[i] + buses[i]
        else: 
            comp[i] = target
        if (comp[minimum] > comp[i]):
            minimum = i
    print(comp[minimum]-target, minimum, (comp[minimum]-target)*buses[minimum])
        
def part2():
    file1 = open("part13.txt","r")
    lines = file1.readlines()
    string = lines[1]
    x = 0
    start = -1
    end = -1
    buses = []
    while (x < len(string)):
        if (string[x] == "x"):
            buses.append(-1)
        elif (string[x] != ","):
            start = x
            while (x < len(string) and string[x] != ","):
                x += 1
                end = x
            buses.append(int(string[start:end]))
        x += 1 
    pos = 0
    found = True
    i = buses[0]
    marked = [None]*len(buses)
    while (None in marked):
        found = True
        for x in range(1,len(buses)):
            if buses[x] != -1 and (pos+x) % buses[x] != 0:
                found = False
                break
            elif (buses[x] != -1 and (pos+x) % buses[x] == 0 and marked[x] == None):
                i *= buses[x]
                marked[x] = 1
        if found:
            print("here",pos)
            break
        pos += i    
        
            
if __name__ == "__main__":
    part1()
    part2()