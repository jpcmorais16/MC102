def dist(x1, y1, x2, y2):
    """devolve a distancia quadrada entre dois pontos"""

    return (x1 - x2) ** 2 + (y1 - y2) ** 2


class Objeto():
    def __init__(self, tipo, Xcentro, Ycentro, parametro):
        self.X = Xcentro
        self.Y = Ycentro
        self.tipo = tipo
        self.parametro = parametro

    def pertence(self, x, y):
        """define se um ponto especifico pertence ao objeto"""

        if self.tipo == "circulo":
            if dist(self.X, self.Y, x, y) <= self.parametro ** 2:
                return True
            else:
                return False

        elif self.tipo == "quadrado":
            menor_X = self.X - self.parametro // 2
            maior_X = self.X + self.parametro // 2
            menor_Y = self.Y - self.parametro // 2
            maior_Y = self.Y + self.parametro // 2

            if menor_X <= x <= maior_X and menor_Y <= y <= maior_Y:
                return True
            else:
                return False


def cria_linha(n, y, lista, condition):
    """cria cada uma das linhas:
    recebe a quantidade de termos da linha,
    o y dessa linha, uma lista de objetos e uma condicao.
    Para cada ponto da linha, o programa analisa se ele pertence a
    algum dos objetos da lista"""

    """condition: condicao para deterctar se o fim da linha ja chegou.
    Se sim, o end="" nao eh inserido para que o codigo passe para a proxima linha"""

    if n == 1:
        condicao1 = False
        """condicao1: condicao para detectar se ja foi encontrado
        algum objeto ao qual aquele ponto pertence"""

        for objeto in lista:
            if objeto.pertence(1, y):
                print("x", end=" ")
                condicao1 = True
                break

        if not condicao1:
            print("-", end=" ")

    else:
        list = lista
        condicao1 = False

        cria_linha(n-1, y, list, False)

        for objeto in lista:
            if objeto.pertence(n, y):

                if condition:
                    print("x")
                    condicao1 = True
                    break

                else:
                    print("x", end=" ")
                    condicao1 = True
                    break

        if not condicao1:

            if condition:
                print("-")
            else:
                print("-", end=" ")


def cria_matriz(N, colunas, lista_de_objetos):
    """cria uma matriz.
    Recebe o numero de linhas, o numero de colunas
    e uma lista de objetos"""


    if N == 1:
        cria_linha(colunas, 1, lista_de_objetos, True)

    else:
        aux = lista_de_objetos
        cria_matriz(N - 1, colunas, aux)
        cria_linha(colunas, N, lista_de_objetos, True)


a = input().split(" ")

M = int(a[0])
N = int(a[1])

Q = int(input())


P = 0


lista = []
"""essa lista ira conter todos os objetos"""

while P < Q:

    valores = input().split(" ")

    lista.append(Objeto(valores[0], int(valores[2]) + 1, int(valores[1]) + 1, int(valores[3])))

    P += 1


cria_matriz(M, N, lista)