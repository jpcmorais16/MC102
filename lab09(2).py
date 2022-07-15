class Matriz:
    def __init__(self, linhas, colunas, auxiliar):
        self.linhas = linhas
        self.colunas = colunas
        self.elementos = [[]] * self.linhas

    def __str__(self):
        return str(self.elementos)

    def add_linha(self, linha, N_linha):
        """adiciona uma linha na matriz"""
        self.elementos[N_linha - 1] = linha

    def elemento_comum(self, matriz, i0, i, j0, j):
        """encontra um único elemento comum entre as matrizes"""

        x1 = i - i0
        x2 = matriz.linhas - self.linhas + i0 - i
        x3 = j - j0
        x4 = matriz.linhas - self.linhas + j0 - j
        y = 0
        z = 0
        for r in (x1, x2):
            if r > 0:
                y += r
        for s in (x3, x4):
            if s > 0:
                z += s
        return [self.linhas + y, self.colunas + z]



def intersec(lista1,lista2):
    for i in range(len(lista2)):
        for j in range(len(lista1)):
            if lista2[i] == lista1[j]:
                return [i + 1, j + 1]
    return 0

def g(m, n):
    matriz1 = Matriz(m, m, False)
    matriz2 = Matriz(n, n, False)

    linhas = []
    p = 0
    while p < m:
        p += 1
        w = input().split(" ")


        for q in w:
            linhas.append(q)
        matriz1.add_linha(w, p)



    condicao = True
    while p < m + n:

        p += 1
        w = input().split(" ")
        intersect = intersec(linhas, w)

        if condicao:
            if intersect == 0:
                for q in w:
                    linhas.append(q)
                matriz2.add_linha(w, p - m)

            elif intersect != 0:
                i = p - m
                j = intersect[0]
                i0 = 1 + intersect[1] // matriz1.linhas
                j0 = intersect[1] % matriz1.linhas
                u = matriz1.elemento_comum(matriz2, i0, i, j0, j)
                condicao = False

    if not condicao:

        string = (str(u[0]) + " " + "x" + " " + str(u[1]))
        return string

lista = []
while True:

    a = input()
    m = int(a.split(" ")[0])
    n = int(a.split(" ")[1])

    if m == 0 and n == 0:
        break
    u = g(m, n)

    lista.append(u)


for i in lista:
    print(i)