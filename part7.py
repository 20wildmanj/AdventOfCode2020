def dfs_helper(graph, mark, start, target):
    mark[start] = True

    if (target == start):
        return True
    nbors = graph[start]
    for i in range(0, len(nbors)):
        vert = nbors[i]
        if vert not in mark and dfs_helper(graph,mark,vert,target):
            return True
    return False

def count(graph, start):

    if (len(graph[start]) == 0):
        return 1
    nbors = graph[start]
    print("nbors: ", nbors)
    tot = 0
    for i in range(0, len(nbors)):
        vert = nbors[i][0]

        tot += nbors[i][1]*count(graph,vert)

        print(tot)
    tot += 1
    return tot

def dfs(graph,start,target):
    mark = {}
    return dfs_helper(graph,mark,start,target)

def counter(graph,start):
    return count(graph,start)-1
def part1():
    graph = {}
    line1 = open("part7.txt","r")
    for line in line1.readlines():
        line = line.replace("\n","").split(" ")
        name = ""
        i = 0
        while i < len(line):
            if (i == 0):
                name = line[0] + line[1]
                graph[name] = []
                i += 5
            elif (line[4] != "no"):
                nbor = line[i] + line[i+1]
                graph[name].append(nbor)
                i += 4
            else:
                i = len(line)

    count = 0
    for key in graph:
        if dfs(graph, key, "shinygold") and key != "shinygold":
            print(key)
            count += 1
    print("tot: ", count)

def part2():
    graph = {}
    line1 = open("part7.txt","r")
    for line in line1.readlines():
        line = line.replace("\n","").split(" ")
        name = ""
        i = 0
        while i < len(line):
            if (i == 0):
                name = line[0] + line[1]
                graph[name] = []
                i += 5
            elif (line[4] != "no"):
                nbor = []
                nbor.append(line[i] + line[i+1])
                nbor.append(int(line[i-1]))
                graph[name].append(nbor)
                i += 4

            else:
                i = len(line)


    count = counter(graph, "shinygold")

    print("tot: ", count)


if __name__ == "__main__":
    part1()
    part2()