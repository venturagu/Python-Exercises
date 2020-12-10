def descobrirLinha(ano):
    i = 2
    j = 5
    conjunto = [1]
    count = 2

    print("Linha 1 -> ", end="")
    print(conjunto)
    print()

    while True:
        conjunto = list(range(i, j))
        i = conjunto[-1] + 1
        j += len(conjunto) + 2
        print("Linha " + str(count) + " -> ", end="")
        print(conjunto)
        print()

        if ano in conjunto:
            return count
            break
        else:
            count += 1


if __name__ == "__main__":
    ano = 1969
    resultado = descobrirLinha(ano)
    print("Linha " + str(resultado))
    test = [::7]
    print(test)
