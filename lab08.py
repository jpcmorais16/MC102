def operacao(m, n, op):
    """Operacoes mais basicas do programa"""
    if op == "+":
        return m + n

    elif op == "-":
        return m - n

    elif op == "==":
        return int(m == n)

    elif op == "<":
        return int(m < n)

    elif op == ">":
        return int(m > n)

    elif op == ">=":
        return int(m >= n)

    elif op == "<=":
        return int(m <= n)

    elif op == "!=":
        return int(m != n)

    elif op == "AND":
        return m and n

    elif op == "OR":
        return m or n


def temletra(a):
    """identifica se há alguma letra dentro de a"""
    k = True
    if type(a) == str and len(a) > 0:
        for i in a:
            if i.isalpha():
                k = False
                return True
        if not k:
            return False


def numero(a):
    """identifica se a é um número"""
    if type(a) == int:
        return True

    elif type(a) == str:
        if a.isdigit():
            return True

        elif a[0] == "-":
            return True

        else:
            return False


def atribuir(variavel, valor, condicao):
    """Atribui um valor a uma variavel"""
    for i in variavel:
        if not i.isalpha() and not i.isdigit():
            resultados.append("Erro de sintaxe: {} nao e um nome permitido para uma variavel.".format(variavel))

            return ""

    if not variavel[0].isalpha():
        resultados.append("Erro de sintaxe: {} nao e um nome permitido para uma variavel.".format(variavel))

    else:
        parametro = 0
        if condicao:
            dic = {variavel: condicional(valor, parametro)}
            variaveis.update(dic)

        else:
            dic = {variavel: f(valor, parametro)}
            variaveis.update(dic)


def referencia(lista):
    """Recebe uma equação com variáveis atribuidas
    e as substitui por seus valores"""

    lista1 = lista
    for i in range(0, len(lista)):
        if lista[i] in variaveis:
            lista1[i] = variaveis[lista[i]]

    string = ""
    for j in lista1:
        string += str(j) + " "

    return string[0:-1]


def identifica(lista, parametro):
    """Recebe uma equação e diz se dentro dela
    há quaisquer variaveis, atribuidas ou nao,e substitui
    as atribuidas por seus valores respectivos"""

    a1 = True
    for k in lista:
        if (k not in ("<", ">", "==", ">=", "<=", "!=", "+", "-", "AND", "OR", " ")
                and not numero(k) and k not in variaveis):
            if parametro == 0:
                resultados.append("Erro de referencia: a variavel {} nao foi definida.".format(k))
            a1 = False
            break

    if a1:
        return referencia(lista)
    else:
        return ""


def f(a, parametro):
    """Organiza como as operacoes devem ser chamadas"""
    x = 0
    lista = a
    param = parametro
    y = 0
    op = "+"
    p = 0

    condicao = False

    for m in lista:
        if temletra(m):
            condicao = True
            break

    if a == "AND" or a == "OR":
        return a

    elif not condicao:
        
        if len(lista) == 1:
            x = lista[0]

        else:
            for i in range(0, len(lista)):
                if lista[i] in ("+", "-"):
                    op = lista[i]

                elif lista[i] in ("<", ">", "==", ">=", "<=", "!="):
                    x1 = x
                    x2 = int(f(lista[p + 1:],0))

                    x = operacao(x1, x2, lista[i])
                    break

                elif numero(lista[i]):

                    y = int(lista[i])

                    x = operacao(x, y, op)

                p += 1

    elif condicao:

        lista = identifica(lista, param)

        if lista != "":

            x = f(lista.split(" "), 0)

        else:
            x = ""
    return x


def condicional(string, parametro):
    """Analisa condicoes para determinar se sao verdadeiras"""
    a = string.split(" ")
    b = string.replace("AND", "OR")
    c = b.split(" OR ")
    lista1 = []
    lista2 = []
    lista3 = []
    param = parametro

    for j in c:
        lista1.append(f(j.split(" "), param))
        param = 1

    for k in a:
        if k == "AND" or k == "OR":
            lista2.append(k)

    for j in range(0, len(lista2)):
        lista3.append(lista1[j])
        lista3.append(lista2[j])
    lista3.append(lista1[-1])

    op = "AND"
    x = True

    for i in lista3:
        if i == "AND" or i == "OR":
            op = i

        else:
            x = operacao(x, i, op)

    return x





resultados = []
variaveis = {}
while True:

    try:
        a = input()
        b = a.split(" ")

        if " = " in a:
            c = a.split(" = ")
            d = c[1].split(" ")

            if "AND" in a or "OR" in a:
                parametro = 1
                atribuir(c[0], c[1], True)

            else:
                parametro = 1

                atribuir(c[0], d, False)

        elif "AND" in a or "OR" in a:
            equacao = identifica(b, 0)
            if equacao != "":
                resultados.append(condicional(equacao, 0))

        else:
            equacao = identifica(b, 0)

            if equacao != "":
                resultados.append(f(b, 0))

    except EOFError:

        for i in resultados:
            print(i)
        print("Encerrando... Bye-bye.")
        break

