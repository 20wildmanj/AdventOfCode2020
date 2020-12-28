

def cleanInp(line):
    firstPass = ""
    print(line)
    for x in range(0,len(line)):
        if (line[x] == ":"):
            firstPass = line[x+2:]
            break
    #print(firstPass)
    intRanges = []
    
    upos = -1
    for x in range(0,len(firstPass)):
        if (firstPass[x] == "-"):
            intRanges.append(int(firstPass[0:x]))
            upos = x+1
        elif (firstPass[x] == " "):
            intRanges.append(int(firstPass[upos:x]))
            firstPass = firstPass[x+4:]
            break

    upos = -1
    #print(firstPass)
    for x in range(0,len(firstPass)):
        if (firstPass[x] == "-"):
            intRanges.append(int(firstPass[0:x]))
            intRanges.append(int(firstPass[x+1:]))
            upos = x
            break
    return intRanges
  



def part1():
    file1 = open("part16.txt","r")
    i = 0
    params = []
    ticketSum = 0
    for line in file1.readlines():
        line = line.replace("\n","")
        if line != "":
            if i < 20:#20:
                line = cleanInp(line)
                for x in line:
                    params.append(x)
                
            elif i >= 25: #25
                check = list(map(int,line.split(",")))
                #print(check, i )
                for x in range(0, len(check)):
                    checkArray = [None]*(len(params)//2)
                    #print("checking ", check[x])
                    for k in range((len(params)//2)):
                        if not (params[2*k] <= check[x] <= params[2*k+1]):
                            #print(params[2*k], check[x], params[2*k + 1])
                            checkArray[k] = True
                    if not (None in checkArray):
                        #print(check[x])
                        ticketSum += check[x]
        i += 1
    print(params)
    print(ticketSum)

def part2():
    file1 = open("part16.txt","r")
    i = 0
    params = []
    ticketSum = 0
    cleanGrid = []
    tickVals = []
    params2 = []
    for line in file1.readlines():
        line = line.replace("\n","")
        if line != "":
            if i < 20:#20:
                line = cleanInp(line)
                for x in line:
                    params.append(x)
                params2.append(line)
            elif i == 22:#22
                tickVals = list(map(int,line.split(",")))
            elif i >= 25: #25
                check = list(map(int,line.split(",")))
                isValid = True
                for x in range(0, len(check)):
                    checkArray = [None]*(len(params)//2)
                    #print("checking ", check[x])
                    for k in range((len(params)//2)):
                        if not (params[2*k] <= check[x] <= params[2*k+1]):
                            #print(params[2*k], check[x], params[2*k + 1])
                            checkArray[k] = True
                    if not (None in checkArray):
                        #print(check[x])
                        isValid = False
                        break
                
                if (isValid):
                    cleanGrid.append(check)
                
        i += 1
    maps = [None]*len(params2)
    print(params2)
    print(cleanGrid)
    taken = [None]*len(params2)
    for x in range(0, len(params2)):
            for col in range(0,len(cleanGrid[0])):
                isRange = True
                for row in range(0,len(cleanGrid)):
                    
                    if not ((params2[x][0] <= cleanGrid[row][col] <= params2[x][1]) or (params2[x][2] <= cleanGrid[row][col] <= params2[x][3])):
                        print(x,col,params2[x],cleanGrid[row][col])
                        isRange = False
                        #break
                if isRange:
                    maps[x] = col
                    if (taken[x] == None): #find all possible choices
                        taken[x] = []
                    taken[x].append(col)
                       
           



    for row in range(0,len(taken)):
        taken[row].append(row) #track original position
    taken.sort(key=len) #sort by length of possible choices
 
    for row in range(0,len(taken)): #remove the only choice possible for row out of the other rows
        for row2 in range(row+1,len(taken)): 
            taken[row2].remove(taken[row][0])
    prod = 1
    for row in taken:
        if row[1] < 6:
            prod *= tickVals[row[0]]
    print(prod)

if __name__ == "__main__":
    part1()
    part2()