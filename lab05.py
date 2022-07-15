def lower(endereço):
    """Determina o número de caracteres minúsculos no endereço"""
    lower = 0
    for i in endereço:
        if i.islower():
            lower += 1
    return lower


def upper(endereço):
    """Determina o número de caracteres maiúsculos no endereço"""
    upper = 0
    for i in endereço:
        if i.isupper():
            upper += 1
    return upper


def alpha(endereço):
    """Determina o número de letras no endereço"""
    alpha = 0
    for i in endereço:
        if i.isalpha():
            alpha += 1
    return alpha


def palavras(endereço):
    """Determina o número de palavras no endereço"""
    palavras = 0
    for i in endereço.split(" "):
        palavras += 1
    return palavras


def ascii(endereço):
    """Determina a soma dos valores ascii no endereço"""
    ascii = 0
    for i in endereço:
        ascii += ord(i)
    return ascii


entrada = input()

lista1 = entrada.split(" ")

dia = lista1[0]
n = int(lista1[1])

p = 0
endereços = []

while p < n:
    a = input()
    endereços.append(a)

    p += 1

if dia == "Segunda":
    f = lower
    condicao = False

if dia == "Terca":
    f = upper
    condicao = True

if dia == "Quarta":
    f = alpha
    condicao = False

if dia == "Quinta":
    f = palavras
    condicao = False

if dia == "Sexta":
    f = ascii
    condicao = True


for i in sorted(endereços, reverse=condicao, key=f):
    print(i)





