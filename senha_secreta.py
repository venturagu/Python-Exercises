from random import choice
import string
import re


def combinacoes():
    letras = 'ABCDEF'
    digitos = '123456789'
    primeiroDigito = '36'

    senha = ''

    invalid = True
    senha = choice(letras)
    i = 1

    while(invalid):
        senha += choice(letras)
        if(senha[i] == senha[i-1]):
            senha = senha[:-1]
            invalid = True
        else:
            i += 1

        if(len(senha) == 3):
            letraRegex = re.compile(r'(?=.*A).*(?=.*D)')
            mo = letraRegex.findall(senha)

            if not mo:
                senha = senha[:-2]
                i -= 2
            else:
                invalid = False
    i = 2
    invalid = True
    senha += choice(primeiroDigito)
    while(invalid):
        senha += choice(digitos)
        if(len(senha) == 6):
            if((int(senha[3]) + int(senha[4]) + int(senha[5])) != 8):
                senha = senha[:-2]
                i -= 2
            else:
                invalid = False
    print(senha)
    return senha


def listaDeSenha():
    listSenha = []
    toleranciaRepeticao = 0

    senha = combinacoes()
    while(toleranciaRepeticao != 900):
        if senha in listSenha:
            toleranciaRepeticao += 1
        else:
            listSenha.append(senha)
        senha = combinacoes()

    for i in range(len(listSenha)):
        print(listSenha[i], end=" ")
        if(i % 2):
            print()
    return listSenha


def tempoDeCombinacoes(combinacoes):
    tempo = 0
    for i in range(len(combinacoes)):
        tempo += 2

    # converter o tempo de segundo para minutos
    tempo = tempo / 60
    return tempo


if __name__ == "__main__":
    combinacoes = listaDeSenha()
    tempo = tempoDeCombinacoes(combinacoes)
    print()
    if(tempo >= 5):
        print("Alarme disparou!!!")
    else:
        print(
            "Lara desvendou todas as possibilidades em um tempo médio de: {0:.0f} minutos ".format(tempo))
