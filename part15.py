



def part1():
    prevmarked = {}
    inp1 = [1,0,18,10,19,6]
    counter = 1

    for i in inp1:
        prevmarked[i] = counter
        counter += 1

    marked = {}
    
    spoken = -1
    prevSpoken = inp1[-1]
    diff = 0
    for x in range(1+len(inp1),2021):
       
        #check if previous spoken word has been seen before
        if (prevSpoken in marked): 
            diff =  marked[prevSpoken] - prevmarked[prevSpoken]
            prevmarked[prevSpoken] = marked[prevSpoken]
            spoken = diff
        else:
            spoken = 0
        #check if spoken word is new (fill in prevmarked entry)
        if (spoken not in prevmarked):
            prevmarked[spoken] = x
        else:
            marked[spoken] = x
        prevSpoken = spoken
    print(spoken)
        

def part2():
    prevmarked = {}
    inp1 = [1,0,18,10,19,6]
    counter = 1

    for i in inp1:
        prevmarked[i] = counter
        counter += 1

    marked = {}
    
    spoken = -1
    prevSpoken = inp1[-1]
    diff = 0
    for x in range(1+len(inp1),30000001):
       
        #check if previous spoken word has been seen before
        if (prevSpoken in marked): 
            diff =  marked[prevSpoken] - prevmarked[prevSpoken]
            prevmarked[prevSpoken] = marked[prevSpoken]
            spoken = diff
        else:
            spoken = 0
        #check if spoken word is new (fill in prevmarked entry)
        if (spoken not in prevmarked):
            prevmarked[spoken] = x
        else:
            marked[spoken] = x
        prevSpoken = spoken
    print(spoken)



if __name__ == "__main__":
    part1()
    part2()