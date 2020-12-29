
class Rule:
    def __init__(self,num,data):
        self.count = num
        self.rules = data


def process(line,rule,currRules,count):
    pos = 0
    #print("nfi",line,currRules,pos,count)
    if type(currRules[0]) == str:
        if currRules[0] == line[count]:
            #print("returning")
            return True, count+1
        else:
            #print("gone")
            return False, 0
    
    if (len(currRules) == 2):
        rule1 = currRules[0:1]
        rule2 = currRules[1:]
        
        passes1 = False
        passes2 = False
        tempC1 = -1
        tempC2 = -1
        passes1, tempC1 = process(line,rule,rule1,count)
        passes2, tempC2 = process(line,rule,rule2,count) 
        #print("split",rule1,rule2)
        #print("split state", passes1,passes2)         
        if (passes1):
            #print("split out 1", currRules,tempC1)
            return True, tempC1
        elif (passes2):
            #print("split out 2", currRules,tempC1)
            return True, tempC2
        else:
            return False, -1   
    while (pos < len(currRules[0])):
        #print(line,currRules,pos,count)
        #print(currRules[0][pos])
        newcurrRules = rule.rules[currRules[0][pos]]
        #print("new: ", newcurrRules)
        passes, tempCount = process(line,rule,newcurrRules,count)
        if (passes):
            count = tempCount
        else:
            return False, 0 
        if count == len(line):
            return True, count
        pos += 1
    #print("out",line,currRules,pos,count)
    return True, count
    
def process2(line,rule,currRules,count):
    pos = 0
    """if (line == "aaaabbaaaabbaaa"):
        print("nfi",line,currRules,pos,count)"""
    if count == len(line):
        return True, count
    elif count > len(line):
        return False,0

    if type(currRules[0]) == str:
        if currRules[0] == line[count]:
            if (line == "aaaabbaaaabbaaa"):
                print("returning",currRules[0],line[count])
            return True, count+1
        else:
            if (line == "aaaabbaaaabbaaa"):
                print("gone",currRules[0],line[count])
            return False, 0
    
    if (len(currRules) == 2):
        rule1 = currRules[0:1]
        rule2 = currRules[1:]
        
        passes1 = False
        passes2 = False
        tempC1 = -1
        tempC2 = -1
        passes1, tempC1 = process2(line,rule,rule1,count)
        passes2, tempC2 = process2(line,rule,rule2,count) 
        if (line == "aaaabbaaaabbaaa"):
            print("split",rule1,rule2)
            print("split state", passes1,passes2)      
        if (passes1):
            if (line == "aaaabbaaaabbaaa"):
                print("split out 1", currRules,tempC1)
            return True, tempC1
        elif (passes2):
            if (line == "aaaabbaaaabbaaa"):
                print("split out 2", currRules,tempC1)
            return True, tempC2
        else:
            return False, -1   
    while (pos < len(currRules[0])):
      
           

        newcurrRules = rule.rules[currRules[0][pos]]
        if (line == "aaaabbaaaabbaaa"):
             print(line,currRules,pos,count,"rule: ",currRules[0][pos],"new: ", newcurrRules)
        passes, tempCount = process2(line,rule,newcurrRules,count)
        if (passes):
            count = tempCount
        else:
            return False, 0 
       
        pos += 1
        """if count == len(line):
            if (line == "aaaabbaaaabbaaa"):
                print(line, pos == len(currRules[0]))
                print("out here",line,currRules,pos,count)
            return True, count"""
    if (line == "aaaabbaaaabbaaa"):
        print("out",line,currRules,pos,count)
    return True, count           
        
          
    
def part1():
    file1 = open("part19.txt","r")
    rules = []
    for x in range(131):
        rules.append([])
    i = 0

    tot = 0
    for line in file1.readlines():
        line = line.replace("\n","")
        if i < 131:
            
            num = int(line[0:line.index(":")])
            #print(num)
            if ("\"" in line):
                quotePos = line.index("\"")+1
                rules[num].append(line[quotePos:quotePos+1])
            elif ("|" in line):
                #print(line.index(":")+2)
                ruleArr = line[line.index(":")+2:].split(" ")
                arr1 = []
                arr2 = []
                past = False
                for rule in ruleArr:
                    if rule == "|":
                        past = True
                    elif past:
                        arr2.append(int(rule))
                    else:
                        arr1.append(int(rule))
                
                rules[num].append(arr1)
                rules[num].append(arr2)
            else:
                ruleArr = list(map(int,line[line.index(":")+2:].split(" ")))
                rules[num].append(ruleArr)
        elif i >= 132:
            
            count = 0
            rule = Rule(0,rules)
            currRules = [rules[0][0]]
            check, finCount = process(line,rule,currRules,count)
            if (check and finCount == len(line)):
                tot += 1
            #print(check)
        #print(rules)
            
        i += 1
            

    print("tot:",tot)
#partially solved, doesn't give the right answer (a bit higher, can't figure out why)
def part2():
    file1 = open("test.txt","r")
    rules = []
    for x in range(43):
        rules.append([])
    i = 0

    tot = 0
    for line in file1.readlines():
        line = line.replace("\n","")
        if i < 31: #131
            
            num = int(line[0:line.index(":")])
            #print(num)
            if ("\"" in line):
                quotePos = line.index("\"")+1
                rules[num].append(line[quotePos:quotePos+1])
            elif ("|" in line):
                #print(line.index(":")+2)
                ruleArr = line[line.index(":")+2:].split(" ")
                arr1 = []
                arr2 = []
                past = False
                for rule in ruleArr:
                    if rule == "|":
                        past = True
                    elif past:
                        arr2.append(int(rule))
                    else:
                        arr1.append(int(rule))
                
                rules[num].append(arr1)
                rules[num].append(arr2)
            else:
                ruleArr = list(map(int,line[line.index(":")+2:].split(" ")))
                rules[num].append(ruleArr)
        elif i >= 32:
            
            count = 0
            rule = Rule(0,rules)
            currRules = [rules[0][0]]
            check, finCount = process2(line,rule,currRules,count)
            if (check and finCount == len(line)):
                print(line)
                tot += 1
            #print(check)
        #print(rules)
            
        i += 1
            
    print(rules)
    print("tot:",tot)


if __name__ == "__main__":
    part1()
    part2()