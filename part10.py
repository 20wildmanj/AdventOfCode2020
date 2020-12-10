

def part1():
    file1 = open("part10.txt","r")
    nums = [0]
    for line in file1.readlines():
        nums.append(int(line.replace("\n","")))
    nums.sort()
    nums.append(nums[-1]+3)
    diff = [0,0,0]
    for i in range(0,len(nums)-1):
        elemDiff = nums[i+1]-nums[i]
        diff[elemDiff-1] += 1

    print(diff[0],diff[2],diff[0]*diff[2])

#dp solution from jonathan paulson
#https://www.youtube.com/watch?v=cE88K2kFZn0&feature=youtu.be
def dp(ind,nums,memo):
    if (ind == len(nums) -1):
        return 1

    if (ind in memo):
        return memo[ind]
    res = 0
    for i in range(ind + 1,len(nums)):
        if nums[i] - nums[ind] <= 3:
            res += dp(i,nums,memo)
    memo[ind] = res
    return res

def part2():

    file1 = open("part10.txt", "r")
    nums = [0]
    for line in file1.readlines():
        nums.append(int(line.replace("\n", "")))
    nums.sort()

    diff = [0, 0, 0]
    memo = {}
    x = dp(0,nums,memo)
    print(x)


if __name__ == "__main__":
    part1()
    part2()