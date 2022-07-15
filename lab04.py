a = input()

b = a.split(" ")

senha = b[0]

T = b[1]

tentativas = 0


while tentativas < int(T):
    tentativa = input()
    acertos = 0

    if len(tentativa) != len(senha):
        acertos = "Erro: quantidade de digitos incongruente"

    if type(acertos) == int:
        for i in range(0, len(senha)):
            if senha[i] == tentativa[i]:
                acertos += 1

    if acertos == len(senha):
        print("Senha reconhecida. Desativando defesas...")
        break

    else:
        print("Senha incorreta")
        print("Semelhanca:", acertos)
        print("Tentativas restantes:", int(T) - tentativas - 1)
        print(" ")

    tentativas += 1

if int(T) - tentativas  == 0:
    print("Tentativas esgotadas. Acionando defesas...")











    tentativas += 1


