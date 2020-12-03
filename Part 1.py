# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    file1 = open("Part 1.txt", "r")
    numDict = {}
    for line in file1.readlines():
        numDict[int(line)] = int(line)
    for key in numDict:
        if (2020-key) in numDict:
            print(key, 2020-key)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
