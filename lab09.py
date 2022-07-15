class Matriz:
    def __init__(self, linhas, colunas, auxiliar):
        self.linhas = linhas
        self.colunas = colunas
        self.elementos = [[]] * self.linhas

        if auxiliar:
            for i in range(self.linhas):
                for j in range(self.colunas):
                    self.elementos[j] = ["k"] * self.colunas


    def __str__(self):
        return str(self.elementos)

    def add_linha(self, linha, N_linha):
        self.elementos[N_linha - 1] = linha

    def muda_elemento(self, linha, coluna, novo_elemento):
        self.elementos[linha - 1][coluna - 1] = novo_elemento

    def pega_elemento(self, linha, coluna):
        return self.elementos[linha - 1][coluna - 1]

    def comparacao(self, matriz):
        posicoes = []
        #print(matriz.linhas)

        for m in range(1, 2*matriz.linhas):
            for n in range(1, 2*matriz.linhas):
                condicao = True
                grau = 0

                for p in range(matriz.linhas):
                    for q in range(matriz.linhas):


                        #print("m",m,"n",n,"p",p,"q",q,"elementos",self.pega_elemento(m + p, n + q),matriz.pega_elemento(p + 1, q + 1))

                        if self.pega_elemento(m + p, n + q) == matriz.pega_elemento(p + 1, q + 1):
                            grau += 1

                        if not (self.pega_elemento(m + p, n + q) == "k"
                                or self.pega_elemento(m + p, n + q) == matriz.pega_elemento(p + 1, q + 1)):

                            condicao = False

                if condicao:
                    posicoes.append([m, n, grau])
        return posicoes


def maior_grau(lista):
    return lista[2]


def f(a, b):

    if a.linhas >= b.linhas:
        m1 = a
        m2 = b

    else:
        m1 = b
        m2 = a

    print(m2.linhas)
    t = m2.linhas - 1
    matriz_auxiliar = Matriz(m1.linhas + 2*t, m1.linhas + 2*t, True)

    for i in range(1, m1.linhas + 1):
        for j in range(1, m1.linhas + 1):
            matriz_auxiliar.muda_elemento(i + t, j + t, m1.pega_elemento(i, j))

    #print(matriz_auxiliar)
    #print("comparacao", matriz_auxiliar.comparacao(m2))

    return [matriz_auxiliar.comparacao(m2), m1, m2]


a = input()
m = int(a.split(" ")[0])
n = int(a.split(" ")[1])

matriz1 = Matriz(m, m, False)
matriz2 = Matriz(n, n, False)

linhas = []
p = 0
while True:
    p += 1
    w = input().split(" ")
    linhas.append(w)


    if w[0] == "0" and w[1] == "0" and len(w) == 2:
        break



for i in range(1, m + 1):
    matriz1.add_linha(linhas[i - 1], i)


for j in range(m + 1, m + n + 1):
    matriz2.add_linha(linhas[j - 1], j - m)

#print(matriz1)
#print(matriz2)

r = f(matriz1, matriz2)

s = sorted(f(matriz1, matriz2)[0], key=maior_grau)[-1]
#print(s)


lin = (r[1].linhas - s[0] + r[2].linhas)
col = (r[1].colunas - s[1] + r[2].colunas)

print(lin, "x", col, sep=" ")