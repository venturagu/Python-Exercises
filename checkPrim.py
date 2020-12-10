# Função retorna o numeros primos entre um intervalo passado como parametro
def numerosPrimos(inicio, fim):
    sequencia = list(range(inicio, fim+1))
    primos = []
    count = 0

    while(len(sequencia) != 0):
        j = 0
        multiplo = 0
        while(j < len(sequencia)):
            if sequencia[0] % sequencia[j] == 0:
                multiplo += 1
            j += 1

        count += 1
        primos.append(sequencia[0])
        if count < 5:
            multiplos = set(
                list(range((sequencia[0]), fim+1, sequencia[0])))
            sequenciaAtual = set(sequencia)
            sequencia = list(sequenciaAtual.difference(multiplos))
        else:
            resultado = list(primos)
            resultado.extend(x for x in sequencia if x not in resultado)
            break
    return resultado


def main():
    inicio = 2
    fim = 120
    resultado = numerosPrimos(inicio, fim)

    for i in range(len(resultado)):
        print(str(resultado[i]), end=" ")
    print()


if __name__ == '__main__':
    main()
