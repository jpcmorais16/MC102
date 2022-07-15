def log2_r(n, p, condicao):
    if n == 1:
        condicao = True
        return p, condicao

    elif n % 2 != 0:
        condicao = False
        return p, condicao

    else:
        p += 1
        return log2_r(n / 2, p, condicao)


def log2(x):
    """descobre se o numero eh uma potencia de 2 e devolve quantas vezes
    o numero 2 aparece em sua fatoracao"""
    p = 0
    ispot = -13
    if x % 2 != 0:
        return -1
    return log2_r(x, p, ispot)


def pot_prox(numero):
    """devolve a maior potencia de 2 que eh
    menor ou igual ao numero"""
    if (numero % 2 == 0 and log2(numero)[1]) or numero == 1:
        return numero

    else:
        return pot_prox(numero - 1)


def malha_r(m, n, p, q, r):
    """a ideia aqui eh, quando a funcao recebe
    uma malha mxn, ela vai procurar o maior quadrado
    possivel que pode ser inserido nessa malha, e, em seguida,
    criar uma malha separada com as dimensoes do quadrado. Suponha t o lado
     desse quadrado, maior = max(m, n) e menor = min(m,n).
     Apos o quadrado ser retirado da malha original, obtemos uma
     nova malha que pode ser decomposta em dois retangulos:
     um de dimensoes (maior-t)*menor e um de dimensoes (menor-t)*t (observe que,
     em alguns casos, teremos retangulos de area 0, o que significa que na verdade
     se trata de somente 1 retangulo ou nenhum, se a malha original ja era uma potencia de 2).
     Apos isso, repete-se esse processo por recursao com cada uma das matrizes retangulares.
     """
    maior = max(m, n)
    menor = min(m, n)

    if m == 0 or n == 0:
        return 0, 0

    elif menor == 1 and menor != maior:
        """se a matriz eh da forma nx1,
        ja podemos afirmar que a unica divisao
        possivel eh em n quadrados de area 1"""
        p += maior
        q += maior
        r[0] += maior

        return p, q

    elif m == n and pot_prox(m) == m:
        """caso base principal:
        a malha eh uma potencia de 2"""
        p += 1
        q += m
        log = log2(m)[0]
        try:
            r[log] += 1

        except KeyError:
            r[log] = 1

        return p, q

    else:
        t = pot_prox(menor)

        x1 = malha_r(t, menor - t, p, q, r)
        x2 = malha_r(maior - t, menor, p, q, r)
        x3 = malha_r(t, t, p, q, r)

        total = x1[0] + x2[0] + x3[0]

        PM = x1[1] + x2[1] + x3[1]

        return total, PM


niveis = {0: 0}


def malha(m, n, dic):
    num_total = 0
    PM = 0

    return malha_r(m, n, num_total, PM, dic)


a = input().split(" ")
M = int(a[0])
N = int(a[1])
valores = malha(M, N, niveis)


print("---\nGrimorio de Teraf L'are\n---")

for i in niveis.keys():
    if niveis[i] != 0:
        print("{} submagia(s) de nivel {}".format(niveis[i], i))

print("---\nTotal de submagia(s) conjurada(s): {}".format(valores[0]))
print("Total de PM gasto: {}\n---".format(valores[1]))