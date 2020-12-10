INICIO = "inicio"


class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.meio = None
        self.direita = None

    def __str__(self):
        return str(self.dado)


class Arvore:
    def __init__(self, dado=None, no=None):
        if no:
            self.inicio = no
        elif dado:
            no = No(dado)
            self.inicio = no
        else:
            self.inicio = None

    def emOrdem(self, no=None):
        if no is None:
            no = self.inicio
        if no.esquerda:
            self.emOrdem(no.esquerda)
        print(no, end='')
        if no.direita:
            self.emOrdem(no.direita)

    def percorrer_jogo(self, coins, segundos, dragon_coins, no=None):
        caminho = []
        contador = 0

        if no is None:
            no = self.inicio
        area = no
        caminho.append(area)
        print(area, end="-> ")

        if coins >= 21:
            area = no.esquerda
            caminho.append(area)
            contador += 1
        elif coins >= 9 and coins <= 20:
            area = no.direita
            caminho.append(area)
            contador += 1
        elif coins <= 8:
            area = no.meio
            caminho.append(area)
            contador += 1
        print(caminho[1], end="-> ")

        if segundos >= 250:
            area = caminho[1].esquerda
            caminho.append(area)
            contador += 1
        elif segundos >= 235 and segundos <= 249:
            area = caminho[1].meio
            caminho.append(area)
            contador += 1
        elif segundos < 235:
            area = caminho[1].direita
            caminho.append(area)
            contador += 1
        print(caminho[2], end="-> ")

        if caminho[2].esquerda == None and caminho[2].direita == None:
            area = "saída secreta"
            caminho.append(area)
        else:
            if dragon_coins <= 3:
                area = caminho[2].esquerda
                caminho.append(area)
                contador += 1
            elif dragon_coins >= 4:
                area = caminho[2].direita
                caminho.append(area)
                contador += 1

        print(caminho[3], end=" ")
        print()
        return contador


def cenario():
    arvore = Arvore()

    no0 = No('inicio')

    # Nós da area 2
    no1 = No('A')
    no2 = No('B')
    no3 = No('C')

    # Nós da area 3
    no4 = No('A')
    no5 = No('B')
    no6 = No('C')
    no7 = No('A')
    no8 = No('B')
    no9 = No('C')
    no10 = No('A')
    no11 = No('B')
    no12 = No('C')

    # Nós da area 4
    no13 = No('A')
    no14 = No('B')
    no15 = No('A')
    no16 = No('B')
    no17 = No('A')
    no18 = No('B')
    no19 = No('A')
    no20 = No('B')
    no21 = No('A')
    no22 = No('B')
    no23 = No('A')
    no24 = No('B')

    arvore.inicio = no0
    no0.esquerda = no1
    no0.meio = no2
    no0.direita = no3

    no1.esquerda = no4
    no1.meio = no5
    no1.direita = no6

    no2.esquerda = no7
    no2.meio = no8
    no2.direita = no9

    no3.esquerda = no10
    no3.meio = no11
    no3.direita = no12

    no5.esquerda = no13
    no5.direita = no14

    no6.esquerda = no15
    no6.direita = no16

    no8.esquerda = no17
    no8.direita = no18

    no9.esquerda = no19
    no9.direita = no20

    no11.esquerda = no21
    no11.direita = no22

    no12.esquerda = no23
    no12.direita = no24

    return arvore


def testsuite():
    arvore = cenario()
    variacaoTotal = 0
    # Verificar todas as variações possiveis apartir da variação A da área 2
    coins, segundos, dragon_coins = 21, 250, 3
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 21, 235, 3
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 21, 235, 4
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 21, 234, 3
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 21, 234, 4
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)

    # Verificar todas as variações possiveis apartir da variação B da área 2
    coins, segundos, dragon_coins = 8, 250, 3
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 8, 235, 3
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 8, 235, 4
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 8, 234, 3
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 8, 234, 4
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)

    # Verificar todas as variações possiveis apartir da variação c da área 2
    coins, segundos, dragon_coins = 9, 250, 3
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 9, 235, 3
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 9, 235, 4
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 9, 234, 3
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)
    coins, segundos, dragon_coins = 9, 234, 4
    variacaoTotal += arvore.percorrer_jogo(coins, segundos, dragon_coins)

    return variacaoTotal


if __name__ == "__main__":
    resultado = testsuite()
    print("\nNúmero de variações: ", end="")
    print(resultado)
