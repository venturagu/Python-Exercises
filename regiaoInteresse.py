'''Resolução utilizando teoria dos conjuntos - Venn diagram'''

if __name__ == "__main__":
    # Conjuntos por localidade
    yoshi_island = 450
    chocolate_island = 330
    cookie_mountain = 340

    # intersecção dos conjuntos
    yoshi_and_chocolate = 200
    yoshi_and_cookie = 180
    chocolate_and_cookie = 100

    # Intersecção das três localidades
    tres_locais = 30

    # espaço total
    total = 1000

    # Intersecção com apenas dois conjuntos
    apenas_yoshi_and_chocolate = yoshi_and_chocolate - tres_locais
    apenas_yoshi_and_cookie = yoshi_and_cookie - tres_locais
    apenas_chocolate_and_cookie = chocolate_and_cookie - tres_locais

    # Conjunto de apenas interrese por uma localidade
    somente_yoshi = yoshi_island - \
        (apenas_yoshi_and_chocolate + tres_locais + apenas_yoshi_and_cookie)
    somente_chocolate = chocolate_island - \
        (apenas_yoshi_and_chocolate + tres_locais + apenas_chocolate_and_cookie)
    somente_cookie = cookie_mountain - \
        (apenas_chocolate_and_cookie + tres_locais + apenas_yoshi_and_cookie)

    apenas_uma_localidade = somente_yoshi + somente_cookie + somente_chocolate
    nenhuma_localidade = total - \
        (chocolate_island + somente_yoshi +
         somente_cookie + apenas_yoshi_and_cookie)

    print(str(nenhuma_localidade) +
          " Yoshis não gostam de nenhuma destas localidades")
    print(str(apenas_uma_localidade) +
          " Yoshis gostam apenas de uma única localidade")
