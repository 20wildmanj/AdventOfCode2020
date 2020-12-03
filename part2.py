


if __name__ == '__main__':
    file1 = open("part2.txt", "r")

    tot = 0
    #part1
    for line in file1.readlines():
        pwdStr = list(line.split(" "))
        bounds = pwdStr[0].split("-")
        charToCheck = pwdStr[1][0]

        pwdStr[2].replace('\n', '')
        count = pwdStr[2].count(charToCheck)

        if count >= int(bounds[0]) and count <= int(bounds[1]):
            tot += 1
    print(tot)
    file1.close()
    file1 = open("part2.txt", "r")
    tot = 0
    for line in file1.readlines():
        pwdStr = list(line.split(" "))
        #print(pwdStr)
        bounds = pwdStr[0].split("-")
        bounds[0] = int(bounds[0])-1
        bounds[1] = int(bounds[1]) - 1
        charToCheck = pwdStr[1][0]
        pwdStr[2].replace('\n', '')
        count = 0

        if charToCheck in pwdStr[2][bounds[0]]:
            count += 1
        if charToCheck in pwdStr[2][bounds[1]]:
            count += 1
        if count == 1:
            tot += 1
    print(tot)
    file1.close()






