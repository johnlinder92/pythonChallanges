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

if __name__ == '__main__':

 mylist = ["apple", "banana", "cherry"]
 test2(mylist)

