
def part1():
    file1 = open("part6.txt","r")
    tot = 0
    d = []
    for line in file1.readlines():
        line = line.replace("\n","")

        if (line == ""):
            d = []
        for char in line:
            if char not in d:
                d.append(char)
                tot += 1
    print(tot)
    file1.close()

def part2():
    file1 = open("test.txt","r")
    tot = 0
    d = {}
    p = 0
    for line in file1.readlines():
        line = line.replace("\n","")
        print(line)
        if (line == ""):
            for key in d:
                print(d[key],p-1)
                if d[key] == p:
                    tot += 1
            print("tot",tot)
            d = {}
            p = 0
        else:
            p += 1
        for char in line:
            if char not in d:
                d[char] = 1
            elif char in d:
                d[char] += 1



    print("tot",tot)


if __name__ == "__main__":
    part1()
    part2()