# Supondo movimento retilíneo uniforme,
# com uma velocidade de 80 km/h e um ângulo de 45 graus,
# qual a distância horizontal que a banana percorrerá após 5 segundos.
import math


def alcanceHorizontal(velocidade, angulo, tempo):
    distancia = velocidade * math.cos(angulo)
    distancia = distancia * tempo
    return distancia


def main():
    # Converte velocidade em km/h para m/s
    velocidade = 80 / 3.6
    angulo = 45
    tempo = 5

    distancia = alcanceHorizontal(velocidade, angulo, tempo)

    print("Após {} segundos a banana percorrerá uma distância horizontal de {:.2f} metros"
          .format(tempo, distancia))


if __name__ == '__main__':
    main()
