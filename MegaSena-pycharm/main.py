import random

# Quantidade de jogos a ser gerado
print(50 * "*")
print(13 * '*' + ' Mega da Virada Gerador ' + 13 * '*')
nr_jogos = int(input('Quantos Jogos?  '))
print(50 * "*")
numeros = int(input('Quantos Número por jogo? '))

print(50 * "*")

count = 0
while (count < nr_jogos):

    a = [1, 2, 11, 12]
    b = [3, 4, 13, 14]
    c = [5, 6, 15, 16]
    d = [7, 8, 17, 18]
    e = [9, 10, 19, 20]
    f = [21, 22, 31, 32]
    g = [23, 24, 33, 34]
    h = [25, 26, 35, 36]
    i = [27, 28, 37, 38]
    j = [29, 30, 39, 40]
    k = [41, 42, 51, 52]
    l = [43, 44, 53, 54]
    m = [45, 46, 55, 56]
    n = [47, 48, 57, 58]
    o = [49, 50, 59, 60]

    lista1 = list(range(1, 11))
    lista2 = list(range(11, 21))
    lista3 = list(range(21, 31))
    lista4 = list(range(31, 41))
    lista5 = list(range(41, 51))
    lista6 = list(range(51, 61))

    Aposta = []

    A = list(range(1, 61))
    # Embaralha as dezenas de 1 a 10
    random.shuffle(A)
    # Adiciona 5 dezenas a lista a posta
    lista_A = A
    valor = random.sample(lista_A, k=numeros)
    valor.sort()
    Aposta.append(valor)
    # Organiza as dezenas em ordem crescente
    a1 = len(list(filter(lambda x: x in valor, a)))
    b1 = len(list(filter(lambda x: x in valor, b)))
    c1 = len(list(filter(lambda x: x in valor, c)))
    d1 = len(list(filter(lambda x: x in valor, b)))
    e1 = len(list(filter(lambda x: x in valor, b)))
    f1 = len(list(filter(lambda x: x in valor, b)))
    g1 = len(list(filter(lambda x: x in valor, b)))
    h1 = len(list(filter(lambda x: x in valor, b)))
    i1 = len(list(filter(lambda x: x in valor, b)))
    j1 = len(list(filter(lambda x: x in valor, b)))
    k1 = len(list(filter(lambda x: x in valor, b)))
    l1 = len(list(filter(lambda x: x in valor, b)))
    m1 = len(list(filter(lambda x: x in valor, b)))
    n1 = len(list(filter(lambda x: x in valor, b)))
    o1 = len(list(filter(lambda x: x in valor, b)))

    lista_1 = len(list(filter(lambda x: x in valor, lista1)))
    lista_2 = len(list(filter(lambda x: x in valor, lista2)))
    lista_3 = len(list(filter(lambda x: x in valor, lista3)))
    lista_4 = len(list(filter(lambda x: x in valor, lista4)))
    lista_5 = len(list(filter(lambda x: x in valor, lista5)))
    lista_6 = len(list(filter(lambda x: x in valor, lista6)))

    if a1 > 1:
        print('Não atende aos parametros do {a}')
    elif b1 > 1:
        print('Não atende aos parametros do {b}')
    elif c1 > 1:
        print('Não atende aos parametros do {c}')
    elif d1 > 1:
        print('Não atende aos parametros do {d}')
    elif e1 > 1:
        print('Não atende aos parametros do {e}')
    elif f1 > 1:
        print('Não atende aos parametros do {f}')
    elif g1 > 1:
        print('Não atende aos parametros do {g}')
    elif h1 > 1:
        print('Não atende aos parametros do {h}')
    elif i1 > 1:
        print('Não atende aos parametros do {i}')
    elif j1 > 1:
        print('Não atende aos parametros do {j}')
    elif k1 > 1:
        print('Não atende aos parametros do {k}')
    elif l1 > 1:
        print('Não atende aos parametros do {l}')
    elif m1 > 1:
        print('Não atende aos parametros do {m}')
    elif n1 > 1:
        print('Não atende aos parametros do {n}')
    elif o1 > 1:
        print('Não atende aos parametros do {o}')
    elif lista_1 > 1:
        print('Não atende aos parametros do lista_1')
    elif lista_2 > 1:
        print('Não atende aos parametros do lista_2')
    elif lista_3 > 3:
        print('Não atende aos parametros do lista_3')
    elif lista_4 > 3:
        print('Não atende aos parametros do lista_4')
    elif lista_5 > 3:
        print('Não atende aos parametros do lista_5')
    elif lista_6 > 3:
        print('Não atende aos parametros do lista_6')

    else:
        print(*Aposta, sep=",")
    count = count + 1
print(50 * "*")


