if __name__ == '__main__':
    z = 0
    lista = []
    while z != 56:
        x = int(input("Skriv in ett nummer:"))
        z = x
        lista.append(x)
        if x > 10:
            print("Du har skrivit in ett nummer större än 10")
        elif x < 10:
            print("Du har skrivit in ett nummer mindre än 10")
        else:
            print("Du skrev in nummret 10")
    for i in lista:
        print(i)