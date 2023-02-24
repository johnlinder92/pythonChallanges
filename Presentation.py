if __name__ == '__main__':
    z = 0
    lista = []
    while z != 56:
        x = int(input("Skriv in ett nummer:"))
        z = x
        lista.append(x)
        if x > 10:
            print("A")
        elif x == 11:
            print("B")
        else:
            print("Du skrev in nummret 10")#commented
    for i in lista:
        print(i)