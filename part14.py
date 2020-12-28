
import copy

def part1():
    file1 = open("part14.txt","r")
    maskComp = 0
    mask0 = 0
    mask1 = 0
    dict1 = {}
    for line in file1.readlines():
        if line[0:4] == "mask":
            maskComp = line[7:].replace("\n","")
            mask0 = int(maskComp.replace("X","1"),2)
            mask1 = int(maskComp.replace("X","0"),2)
        else:
            end = 4
            key = -1
            while (line[end] != "]"):
                end += 1
            key = int(line[4:end])
            entry = int(line[end+4:])
            entry = (entry & mask0) |  (mask1)
          
            dict1[key] = entry
    print("sum", sum(dict1.values()))

#recursive function that generates all permutation of a given mask
def maskPerm(store, mask):
    if ("X" not in mask):
        store.append(int(''.join(mask),2))
        return
    for x in range(len(mask)):
        if mask[x] == "X":
            mask[x] = "0"
            mask2 = copy.deepcopy(mask)
            maskPerm(store,mask2)
            mask[x] = "1"
            mask3 = copy.deepcopy(mask)
            maskPerm(store,mask3)
            break
#converts address given the mask
def maskConvert(address,mask):
    address = list(format(int(address),'036b'))
    if (len(address) != 36):
        while (len(address) < 36):
            address.insert(0,"0")
    address = ''.join(address)
    
    resultList = list(mask)
    for x in range(len(resultList)):
        if mask[x] == "0":
            resultList[x] = address[x]
    result = ''.join(resultList)
    
    return result

def part2():
    file1 = open("part14.txt","r")
    maskComp = 0
    mask0 = 0
    mask1 = 0
    dict1 = {}
    for line in file1.readlines():
        if line[0:4] == "mask":
            maskComp = line[7:].replace("\n","")
            mask1 = int(maskComp.replace("X","0"),2)
           
        else:
            store = []
            end = 4
            key = -1
            while (line[end] != "]"):
                end += 1
            key = line[4:end]
            entry = int(line[end+4:])
            result = maskConvert(key,maskComp)
            maskInp = list(result)
            maskPerm(store,maskInp)
        
            for item in store:
                dict1[item] = entry
        
    print("sum", sum(dict1.values()))




if __name__ == "__main__":
    part1()
    part2()