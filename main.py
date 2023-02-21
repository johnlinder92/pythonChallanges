# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#hmm

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def flatten(listoflists):
    result = []
    for i in listoflists:
        for x in i:
            result.append(x)
    return result

def up_down(int):
    mytuple = ((int-1), (int+1))
    return mytuple

def test(x):
    if x == 5:
        print("x is bigger than 5")
    elif x >= 5 and x <= 10:
        print("x is biger than 5 and less than 10")
    else:
        print("x is less than 5")

def test2(y):
    x = 5
    while x == 5:
        for i in y:
            print(i)
        print("listan klarprintad")
        x = 2
def validate(string):
    if string.find("def") == -1:
        return "missing def"
    elif string.find(":")== -1:
        return "missing :"
    elif string.find("(") == -1:
        return "missing paren"
    elif string.find(")") == -1:
        return "missing paren"
    elif string.find("("+")") != -1:
        return "missing param"
    elif string.find("    ") == -1:
        return "missing indent"
    elif string.find("validate") == -1:
        return "wrong name"
    elif string.find("return") == -1:
        return "missing return"
    else:
        return True
def test(string):
    if string.find("def") == -1:
        return "missing def"

def all_equal(list):
    if list.__len__()==1:
     return True
    a = 0
    for i in list:
        a+1
        if (i == list[a]):
            pass
        else:
            return False
    return True

def testlist(list):
    list.append("test")
    return list

def consecutive_zeros(stringofoneandzero):
    count = 0
    highestCount = 0
    for i in stringofoneandzero:
        if(len(stringofoneandzero) == 1):
            if(i=='0'):
                highestCount = 1
                return highestCount
            if(i=='1'):
                highestCount = 0
                return highestCount
        if(i == '0'):
            count += 1
        if(i=='1'):
            if (count>highestCount):
                highestCount = count
            count = 0
    return highestCount


def list_xor(n, list1, list2):
    existsInFirstList = 0
    existInSecondList = 0

    for i in list1:
       if i == n:
           existsInFirstList = 1
    for b in list2:
       if b == n:
           existInSecondList = 1
    if (existsInFirstList == 1 and existInSecondList == 1):
        return False
    if (existsInFirstList == 0 and existInSecondList == 1):
        return True
    if (existsInFirstList == 1 and existInSecondList == 0):
        return True
    if (existsInFirstList == 0 and existInSecondList == 0):
        return False

if __name__ == '__main__':
    print(list_xor(1, [1, 2, 3], [4, 5, 6]))

