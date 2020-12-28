
from collections import deque

number = "0123456789"

def process(opq,ops): #process the expression as is (infix), uses a stack and a queue
    while (len(opq) > 0):
        arg = opq.popleft()
        if arg == "+":
            x = ops.pop()
            y = opq.popleft()
            if (y == "("):
                process(opq,ops)
                y = ops.pop()
            else: 
                y = int(y)
            x = x + y
            ops.append(x)
        elif arg == "*":
            x = ops.pop()
            y = opq.popleft()
            if (y == "("):
                process(opq,ops)
                y = ops.pop()
            else:
                y = int(y)
            x = x * y
            ops.append(x)
        elif arg == "(":
            process(opq,ops)
        elif arg == ")":
            return
        elif arg in number:
            ops.append(int(arg))
        #print(ops)


def part1():
    file1 = open("part18.txt","r")
    s = 0
    for line in file1.readlines():
        opq = deque()
        ops = deque()
        line = line.replace("\n","")
        for char in line:
            if char != " ":
                opq.append(char)
        process(opq,ops)
        s += ops.pop()
    print(s)

def process2(opq,ops): #uses a stack and queue but way simpler since everything is postfix
    while (len(opq) > 0):
        arg = opq.popleft()
        if arg == "+":
            x = ops.pop()
            y = ops.pop()
            x = x + y
            ops.append(x)
        elif arg == "*":
            x = ops.pop()
            y = ops.pop()
            x = x * y
            ops.append(x)
        elif arg in number:
            ops.append(int(arg))
       



def infixToPostfix(opq,output): #changes infix to postfix, bit different to account for change in order of operations
    ops = deque()
    while (len(opq) > 0):
        arg = opq.popleft()
        if arg == ")": #returning back to main, add the multiplication signs
            while len(ops) > 0:
                output.append(ops.pop())
            #print("return",output)
            return
        elif arg == "(":
            infixToPostfix(opq,output)
        elif arg == "*":
            ops.append(arg)
        elif arg == "+": #put the addition signs in in advance for proper ooe
            temp = opq.popleft()
            if temp == "(": #recursive case
                infixToPostfix(opq,output)
            else:
                output.append(temp)
            output.append(arg)
        else:
            output.append(arg)
        #print(arg,opq,ops,output)
    while len(ops) > 0:
        output.append(ops.pop())
   

def part2():
    file1 = open("part18.txt","r")
    s = 0
    for line in file1.readlines():
        opq = deque()
        ops = deque()
        output = deque()
        line = line.replace("\n","")
        i = 0
        while i < len(line):
            if line[i] != " ":
                opq.append(line[i])
            i += 1
        infixToPostfix(opq,output)
        ops = deque()
        process2(output,ops)
        s += ops.pop()
        
    print(s)

if __name__ == "__main__":
    part1()
    part2()