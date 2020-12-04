
class Passport:
    num = "0123456789"
    char = "abcdef"
    eclList = ["amb","blu","brn","gry","grn","hzl","oth"]
    def __init__(self):
        self.byr = -1
        self.ecl = ""
        self.iyr = -1
        self.eyr = -1
        self.hgt = ""
        self.hcl = ""
        self.pid = ""
    def ecl_valid(self):
        if self.ecl not in self.eclList:
            return False
        return True
    def pid_valid(self):
        if len(self.pid) != 9:
            return False
        for char in self.pid:
            if char not in self.num:
                return False
        return True
    def height_valid(self):
        if (self.hgt == ""):
            return False
        if ("cm" in self.hgt):
            strip = int(self.hgt.replace("cm",""))
            return (strip >= 150 and strip <= 193)
        if ("in" in self.hgt):
            strip = int(self.hgt.replace("in",""))
            return (strip >= 59 and strip <= 76)
        return False
    def hcl_valid(self):
        if (self.hcl == "" or self.hcl[0] != "#"):
            return False
        if (len(self.hcl) != 7):
            return False
        for char in self.hcl[1:]:
            if char not in self.char and char not in self.num:
                return False
        return True

    def is_valid(self):
        return (self.byr >= 1920 and self.byr <= 2002 and
                self.iyr >= 2010 and self.iyr <= 2020 and
                self.eyr >= 2020 and self.eyr <= 2030 and
                self.height_valid() and self.hcl_valid() and self.pid_valid()
                and self.ecl_valid()

                )
    def to_str(self):
        print("NEW OBJECT")
        print(self.byr,(self.byr >= 1920 and self.byr <= 2002))
        print(self.ecl, self.ecl_valid())
        print(self.iyr,(self.iyr >= 2010 and self.iyr <= 2020))
        print(self.eyr, (self.eyr >= 2020 and self.eyr <= 2030))
        print(self.hgt, self.height_valid())
        print(self.hcl, self.hcl_valid())
        print(self.pid, self.pid_valid())
        print(self.is_valid())
        print("-----")

if __name__ == "__main__":
    file1 = open("part4.txt", "r")
    fields = ["byr","eyr","iyr","pid","hcl"]
    totalPass = []
    newPass = Passport()
    for line in file1.readlines():
        if len(line) == 1:
            newPass.to_str()
            if (newPass.is_valid()):
                totalPass.append(newPass)
            newPass = Passport()

        else:
            line = line.split(" ")
            for string in line:
            
                string = string.replace('\n', '')
                if "byr" in string:
                    newPass.byr = int(string[4:])
                elif "eyr" in string:
                    newPass.eyr = int(string[4:])
                elif "iyr" in string:
                    newPass.iyr = int(string[4:])
                elif "pid" in string:
                    newPass.pid = string[4:]
                elif "hcl" in string:
                    newPass.hcl = string[4:]
                elif "hgt" in string:
                    newPass.hgt = string[4:]
                elif "ecl" in string:
                    newPass.ecl = string[4:]
    if (newPass.is_valid()):
        totalPass.append(newPass)
    print(len(totalPass))
