

def str_compare(e):
    return len(e)

if __name__ == "__main__":
    file1 = open("test.txt","r")
    strlist = []
    for line in file1.readlines():
        line = line.replace("\n","").split()
        for word in line:
            if word not in strlist:
                strlist.append(word)

    strlist.sort(key = str_compare)
    print(strlist)