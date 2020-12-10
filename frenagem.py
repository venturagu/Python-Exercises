# função retorna a distancia em metros necessario para um veiculo frear totalmente
def frenagem(velocidade, coeficiente):
    distancia = ((velocidade*velocidade) / (250 * coeficiente))
    return distancia


if __name__ == "__main__":
    velocidade = 260
    coeficiente = 1
    distancia = frenagem(velocidade, coeficiente)
    print(
        f"Será necessario {distancia} metros para que o veiculo freie totalmente")
