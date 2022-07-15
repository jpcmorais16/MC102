def comparacao(pessoa):
    """compara as caracteristicas da pessoa(um dicionario)
    com as do suspeito e devolve a quantidade de igualdades"""
    p = 0
    for i in suspeito:
        if i in pessoa and pessoa[i] == suspeito[i]:
            p += 1
    return p




"""pessoas = um dicionario de dicionarios, onde cada um desses
dicionarios interiores representa as caracteristicas de uma pessoa especifica"""
pessoas = {}

suspeito = {}


condicao1 = False
condicao2 = False
condicao3 = True

i = 1
while True:

    """pessoas(1,2,3,4...)"""
    while True:

        dic = {}
        a = input()

        if a == "-":

            i += 1
            condicao3 = True
            break

        elif a == "--":

            condicao1 = True
            break



        b = a.split(": ")


        dic[b[0]] = b[1]

        if condicao3:
            pessoas[i] = dic
            condicao3 = False

        elif not condicao3:
            pessoas[i].update(dic)



    """caracteristicas do suspeito"""
    caracteristicas = 0
    if condicao1:
        while True:
            a = input()

            if a == "---":
                condicao2 = True
                break

            b = a.split(": ")


            suspeito[b[0]] = b[1]
            caracteristicas += 1


    if condicao2:
        break


"""esse bloco chama a funcao comparacao e, se o numero
de semelhancas for maximo, adiciona a pessoa na lista de suspeitos"""
dic = {}
suspeitos = []
for j in range(1, i + 1):
    matches = comparacao(pessoas[j])
    if matches == caracteristicas:
        suspeitos.append(pessoas[j]["Nome"])


"""esse bloco printa o nome de cada uma dos suspeitos
em ordem alfabetica"""

if len(suspeitos) == 0:
    print("Nenhum suspeito(a) com essas caracteristicas foi identificado(a).")


elif len(suspeitos) == 1:
    print("Suspeito(a):")
    print(suspeitos[0])

else:
    print("Suspeitos(as):")
    for i in sorted(suspeitos):
        print(i)
