def distancia(p1, p2):
    """calcula a distancia entre dois pontos"""
    dx2 = (p1[0] - p2[0]) ** 2
    dy2 = (p1[1] - p2[1]) ** 2

    return dx2 + dy2


def maior_distancia(ponto):
    """recebe um ponto do eixo Y e devolve
    sua distancia ao esconderijo mais distante"""
    d = 0
    for i in esconderijos:
        l = distancia(ponto, i)

        if l > d:
            d = l

    return d


def busca_binaria():
    """A ideia aqui eh usar uma busca binaria alterada.
    Se plotassemos a distancia ao ponto mais distante de cada ponto
    do eixo Y(uma curva do tipo maior distancia vs Y), obteriamos uma curva
    que necessariamente teria algum ponto tal que sua derivada eh 0 e sua derivada segunda eh maior que 0
    (a demonstração dessa afirmação é muito longa para ser colocada aqui), sendo esse ponto o ponto
    de menor distancia possivel ao seu esconderijo mais distante. Portanto, o que o algoritmo faz eh
    medir uma "derivada" de cada ponto escolhido. Se essa derivada eh maior que 0, significa que o
    ponto de derivada = 0 esta para a esquerda. Se essa derivada eh menor que 0, o ponto de derivada = 0,
    analogamente, esta para a direita. Apos algumas iteraçoes, convergiremos para a regiao do ponto desejado"""

    d = Y - 1
    e = 1

    d1 = maior_distancia([0, 1])
    t = d1

    mf = 0
    while d >= e:
        m = (d + e) // 2

        md = maior_distancia([0, m])
        md1 = maior_distancia([0, m+1])

        if md <= t:
            """esse bloquinho serve para manter controle
            da menor distancia que encontramos.
            Isto eh importante porque o algoritmo converge 
            para a REGIAO do ponto cuja derivada é 0,
            mas nem sempre converge diretamente para ele
            (ate porque estamos trabalhando com inteiros
            e nem sempre o ponto de derivada 0 da curva 
            sera um inteiro)."""

            t = md
            mf = m

        if md1 - md < 0:
            e = m + 1

        elif md1 - md > 0:
            d = m - 1

    return mf


while True:
    a = input().split()
    N = int(a[0])
    Y = int(a[1])

    if a[0] == a[1] == "0":
        break


    esconderijos = []

    p = 0
    for m in range(N):

        b = input().split(" ")
        x = int(b[0])
        y = int(b[1])

        esconderijos.append([x, y])

    print(busca_binaria())