def calcularTempo(distancia, velocidade):
    segundos = distancia / velocidade

    dias = segundos // 86400
    segundos_restantes = segundos % 86400

    horas = segundos_restantes // 3600
    segundos_restantes = segundos_restantes % 3600

    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60

    print("Tempo para percorrer a distância é de: {0:.0f} dias".format(dias))
    print("Mais precisamente de {0:.0f} dias, {1:.0f} horas, {2:.0f} \
minutos e {3:.0f} segundos".format(dias, horas, minutos, segundos))


def main():
    distancia = 149600000
    # Converte a velocidade de km/h por km/S
    velocidade = 28440 / 3600
    calcularTempo(distancia, velocidade)


if __name__ == '__main__':
    main()
