# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    file1 = open("Part 1.txt", "r")
    numDict = {}
    #part 1
    for line in file1.readlines():
        numDict[int(line)] = int(line)
    for key in numDict:
        if (2020-key) in numDict:
            print(key, 2020-key)
    #part 2
    for key in numDict:
        sum = (2020-key)
        for key2 in numDict:
            if (sum-key2) in numDict:
                print(key, key2, sum-key2)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
