

def part1():
    file1 = open("part9.txt","r")
    nums = []
    for line in file1.readlines():
        nums.append(int(line.replace("\n","")))
    prev = {}
    for x in range(0,len(nums)):
        if (x < 25):
            prev[nums[x]] = x
        else:
            mark = False
            for key in prev:
                sum = nums[x] - key
                if (sum in prev):
                    mark = True
            if not mark:
                return nums[x]
            prev[nums[x]] = x
            del prev[nums[x-25]]
    return None
def part2():
    file1 = open("part9.txt","r")
    nums = []
    for line in file1.readlines():
        nums.append(int(line.replace("\n","")))
    target = part1()

    prev = {}
    for x in range(0,len(nums)):
       for i in range(x+2,len(nums)):
           if (sum(nums[x:i]) == target):
               print(max(nums[x:i])+min(nums[x:i]))



if __name__ == "__main__":
    part1()
    part2()