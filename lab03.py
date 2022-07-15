a = True
dimensoes = []
pecas = []
pecax = []
pecay = []
p_1 = []

def movimentos(peca, x, y, n):
    x = x - 1
    p = x
    q = y
    x_mov = []
    y_mov = []

    # tipos de peca
    if peca == "Torre":

        # movimentos horizontais
        for i in range(0, n + 1):
            if i != x:
                x_mov.append(i)
                y_mov.append(y)
        # print("passo 1: ", x_mov)
        # print("passo 2;", y_mov)
        # movimentos verticais
        for i in range(1, n + 1):
            if i != y:
                x_mov.append(x)
                y_mov.append(i)

    elif peca == "Bispo":
        # up left
        while p > 0 and q <= n + 1:
            p -= 1
            q += 1
            x_mov.append(p)
            y_mov.append(q)

        p = x
        q = y

        # up right
        while p <= n + 1 and q <= n + 1:
            p += 1
            q += 1
            x_mov.append(p)
            y_mov.append(q)

        p = x
        q = y

        # down right
        while p <= n + 1 and q > 1:
            p += 1
            q -= 1
            x_mov.append(p)
            y_mov.append(q)

        p = x
        q = y

        # down left
        while p > 0 and q > 0:
            p -= 1
            q -= 1
            x_mov.append(p)
            y_mov.append(q)

        p = x
        q = y

        # down left
        while p > 1 and q > 1:
            p -= 1
            q -= 1
            x_mov.append(p)
            y_mov.append(q)

    elif peca == "Dama":
        # movimentos horizontais
        for i in range(0, n + 1):
            if i != x:
                x_mov.append(i)
                y_mov.append(y)

        # movimentos verticais
        for i in range(1, n + 1):
            if i != y:
                x_mov.append(x)
                y_mov.append(i)

            # up left
            while p > 0 and q <= n + 1:
                p -= 1
                q += 1
                x_mov.append(p)
                y_mov.append(q)

            p = x
            q = y

            # up right
            while p <= n + 1 and q <= n + 1:
                p += 1
                q += 1
                x_mov.append(p)
                y_mov.append(q)

            p = x
            q = y

            # down right
            while p <= n + 1 and q > 1:
                p += 1
                q -= 1
                x_mov.append(p)
                y_mov.append(q)

            p = x
            q = y

            # down left
            while p > 0 and q > 1:
                p -= 1
                q -= 1
                x_mov.append(p)
                y_mov.append(q)

            p = x
            q = y

    elif peca == "Peao":
        if y != n:
            if y == 2:
                x_mov.append(x)
                y_mov.append(y + 1)
                x_mov.append(x)
                y_mov.append(y + 2)
            else:
                x_mov.append(x)
                y_mov.append(y + 1)

    elif peca == "Cavalo":
        # up left
        if x - 2 >= 0 and y + 1 <= n:
            x_mov.append(x - 2)
            y_mov.append(y + 1)
        if x - 1 >= 0 and y + 2 <= n:
            x_mov.append(x - 1)
            y_mov.append(y + 2)

        # up right
        if x + 1 <= n and y + 2 <= n:
            x_mov.append(x + 1)
            y_mov.append(y + 2)
        if x + 2 <= n and y + 1 <= n:
            x_mov.append(x + 2)
            y_mov.append(y + 1)

        # down right
        if x + 1 <= n and y - 2 >= 0:
            x_mov.append(x + 1)
            y_mov.append(y - 2)
        if x + 2 <= n and y - 1 >= 0:
            x_mov.append(x + 2)
            y_mov.append(y - 1)

        # down left
        if x - 2 >= 0 and y - 1 >= 0:
            x_mov.append(x - 2)
            y_mov.append(y - 1)
        if x - 1 >= 0 and y - 2 >= 0:
            x_mov.append(x - 1)
            y_mov.append(y - 2)

    elif peca == "Rei":
        for i in (y - 1, y + 1):
            x_mov.append(x - 1)
            y_mov.append(i)
            x_mov.append(x)
            y_mov.append(i)
            x_mov.append(x + 1)
            y_mov.append(i)

        x_mov.append(x - 1)
        y_mov.append(y)
        x_mov.append(x + 1)
        y_mov.append(y)
    mov = [x_mov, y_mov]
    return mov


while True:
    N = int(input())

    if N == 0:
        break

    b = input()

    dimensoes.append(N)

    lista = b.split(" ")

    pecas.append(lista[0])
    pecax.append(ord(lista[1]) - 96)
    pecay.append(int(lista[2]))
    p_1.append(lista[1])

s = 0

for i in dimensoes:
    mov = movimentos(pecas[s], pecax[s], pecay[s], i)
    print("Movimentos para a peca {} a partir da casa {}{}.".format(pecas[s], p_1[s], pecay[s]))
    x_mov = mov[0]
    y_mov = mov[1]

    pares = ["k"]*(len(x_mov))

    for k in range(0, len(x_mov)):
        pares[k] = [x_mov[k], y_mov[k]]

    # tabuleiro
    m = i

    while m >= 0:
        j = 0
        linha = []
        while j <= i:
            if j == 0:
                if m != 0:
                    linha.append(m)
                else:
                    linha.append(" ")
            elif j == pecax[s] and m == pecay[s]:
                linha.append("o")

            elif m == 0:
                linha.append(chr(96 + j))
                
            elif [j - 1, m] in pares:
                linha.append("x")

            else:
                linha.append("-")

            j += 1

        for f in linha:
            print(f, end=" ")
        print(" ")

        m -= 1

    print(" ")

    s += 1












