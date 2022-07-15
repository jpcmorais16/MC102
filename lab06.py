# tava difícil esse aqui né prof

def numero(lista):
    return(lista[1])

def letra(lista):
    if lista[0][0] == "T":
        return 0

    if lista[0][0] == "E":
        return 1

    if lista[0][0] == "D":
        return 2

    if lista[0][0] == "P":
        return 3

class Medalutador:
    def __init__(self, ID, bonus_A, bonus_D, H, K, M, torneio):

        self.ID = ID
        self.A = 0
        self.D = 0
        self.pecas = []
        self.M = M
        self.H = H
        self.K = K
        self.bonus_A = bonus_A
        self.bonus_D = bonus_D
        self.torneio = torneio
        self.H_inicial = H

    def __str__(self):
        return str(self.pecas) + " " + str(self.A) + " " + str(self.D)

    def escolhe_peca(self, adversario):
        lista = []

        for i in adversario.pecas_utilizadas:
                for j in self.pecas_utilizadas:
                    if i[0] == j[0]:
                        lista.append([i, i[1] - j[1]])
        
        lista = sorted(lista, reverse=True, key=numero)


        if lista[0][1] == lista[1][1] and lista[0][1] != lista[2][1]:

            lista = sorted([lista[0], lista[1]], key=letra)


        elif lista[0][1] == lista[2][1] and lista[0][1] != lista[3][1]:

            lista = sorted([lista[0], lista[1], lista[2]], key=letra)
            
        elif lista[0][1] == lista[3][1]:

            lista = sorted(lista, key=letra)

        return(lista[0][0])


    def add_peca(self, i):
        self.pecas.append(i)

    def lose_peca(self, i):
        if i in self.pecas:
            self.pecas.remove(i)



    def atualizacao(self, ganhou, perdeu, peca, H_change):
        p = 0

        if ganhou:
            self.add_peca(peca)
            self.M += 1
            self.H = self.H - H_change

            if self.H < 0:
                self.H = 0

            self.H = self.H + self.K

            if self.H > self.H_inicial:
                self.H = self.H_inicial



            print("Medalutador {} venceu e recebeu a {}{}\n".format(self.ID, peca[0], peca[1]))


        elif perdeu:
            if self.torneio == "principal":
                self.lose_peca(peca)
                self.M -= 1
                self.torneio = "repescagem"
                self.H = (self.H // 2) + self.K

                if self.H > self.H_inicial:
                    self.H = self.H_inicial

                if self.H < 0:
                    self.H = 0


            elif self.torneio == "repescagem":
                self.torneio = "eliminado"






        valor_Direito = []
        valor_Esquerdo = []
        valor_Torso = []
        valor_Pena = []
        Direito = []
        Esquerdo = []
        Torso = []
        Pena = []

        while p < self.M:

            for i in self.pecas:
                if i[0] == "D":
                    Direito.append(i)
                    valor_Direito.append(int(i[1]))

                elif i[0] == "E":
                    Esquerdo.append(i)
                    valor_Esquerdo.append(int(i[1]))

                elif i[0] == "T":
                    Torso.append(i)
                    valor_Torso.append(int(i[1]))

                elif i[0] == "P":
                    Pena.append(i)
                    valor_Pena.append(int(i[1]))

                p += 1

        self.pecas_utilizadas = ["k"] * 4

        self.pecas_utilizadas[0] = Direito[valor_Direito.index(max(valor_Direito))]

        self.pecas_utilizadas[1] = Esquerdo[valor_Esquerdo.index(max(valor_Esquerdo))]

        self.pecas_utilizadas[2] = Torso[valor_Torso.index(max(valor_Torso))]

        self.pecas_utilizadas[3] = Pena[valor_Pena.index(max(valor_Pena))]



        self.A = max(valor_Direito) + max(valor_Esquerdo) + self.bonus_A
        self.D = max(valor_Torso) + max(valor_Pena) + self.bonus_D

def batalha(meda_i, meda_j, final):
    if meda_i.ID > meda_j.ID and not final:
        batalha(meda_j, meda_i, final)
    else:
    
        dif_i = meda_i.A - meda_j.D
        dif_j = meda_j.A - meda_i.D

        print("Medalutadores: {} vs {}".format(meda_i.ID, meda_j.ID))

        for k in (meda_i, meda_j):
            print("\tA{} = {}{} + {}{} + {} = {}".format(k.ID, k.pecas_utilizadas[1][0], k.pecas_utilizadas[1][1],
                                                       k.pecas_utilizadas[0][0], k.pecas_utilizadas[0][1],
                                                       k.bonus_A, k.pecas_utilizadas[1][1] + k.pecas_utilizadas[0][1]
                                                       + k.bonus_A))

            print("\tD{} = {}{} + {}{} + {} = {}".format(k.ID, k.pecas_utilizadas[2][0], k.pecas_utilizadas[2][1],
                                                       k.pecas_utilizadas[3][0], k.pecas_utilizadas[3][1],
                                                       k.bonus_D, k.pecas_utilizadas[2][1] + k.pecas_utilizadas[3][1]
                                                       + k.bonus_D))

            print("\tH{} = {}".format(k.ID, k.H))


        if ((meda_i.A > meda_j.D or meda_j.A > meda_i.D)
        and dif_i != dif_j):
            if dif_i > dif_j:
                if final:
                    print("Campeao: medalutador {}".format(meda_i.ID))

                else:
                    escolhida = meda_i.escolhe_peca(meda_j)
                    meda_i.atualizacao(True, False, escolhida, meda_j.H)
                    meda_j.atualizacao(False, True, escolhida, 0)

            else:
                if final:
                    print("Campeao: medalutador {}".format(meda_j.ID))

                else:
                    escolhida = meda_j.escolhe_peca(meda_i)
                    meda_j.atualizacao(True, False, escolhida, meda_i.H)
                    meda_i.atualizacao(False, True, escolhida, 0)

        elif meda_i.H != meda_j.H:
            if meda_i.H > meda_j.H:
                if final:
                    print("Campeao: medalutador {}".format(meda_i.ID))

                else:
                    escolhida = meda_i.escolhe_peca(meda_j)
                    meda_i.atualizacao(True, False, escolhida, meda_j.H)
                    meda_j.atualizacao(False, True, escolhida, 0)

            else:
                if final:
                    print("Campeao: medalutador {}".format(meda_j.ID))

                else:
                    escolhida = meda_j.escolhe_peca(meda_i)
                    meda_j.atualizacao(True, False, escolhida, meda_i.H)
                    meda_i.atualizacao(False, True, escolhida, 0)

        else:
            if meda_i.ID < meda_j.ID:
                if final:
                    print("Campeao: medalutador {}".format(meda_i.ID))

                else:
                    escolhida = meda_i.escolhe_peca(meda_j)
                    meda_i.atualizacao(True, False, escolhida, meda_j.H)
                    meda_j.atualizacao(False, True, escolhida, 0)

            else:
                if final:
                    print("Campeao: medalutador {}".format(meda_j.ID))

                else:
                    escolhida = meda_i.escolhe_peca(meda_j)
                    meda_j.atualizacao(True, False, escolhida, meda_i.H)
                    meda_i.atualizacao(False, True, escolhida, 0)



N = int(input())

participantes = ["k"] * N


w = 1
while w <= N:
    principal = []
    a = input()
    b = input()

    stats = a.split(" ")
    bonuses = b.split(" ")

    participantes[w - 1] = Medalutador(w, int(bonuses[0]), int(bonuses[1]), int(stats[0]),
                                       int(stats[1]), int(stats[2]), "principal")

    q = 0
    while q < int(stats[2]):
        x = input()
        peca = x.split(" ")


        participantes[w - 1].add_peca([peca[0], int(peca[1])])


        q += 1

    participantes[w - 1].atualizacao(False, False, 0, 0)


    w += 1

# torneio
principal = []
for i in participantes:
    principal.append(i)
repescagem = []

while True:


    if len(principal) == 1 and len(repescagem) == 1:
        print("Cyberluta Final")

        batalha(principal[0], repescagem[0], True)
        break



    for i in range(0, len(repescagem), 1):
        for j in range(0, len(repescagem)):

            if j == i + 1:
                print("Cyberluta da Repescagem")
                batalha(repescagem[i], repescagem[j], False)

                if repescagem[i].torneio == "eliminado":
                    repescagem.remove(repescagem[i])

                elif repescagem[j].torneio == "eliminado":
                    repescagem.remove(repescagem[j])




    for i in range(0, len(principal), 1):
        for j in range(0, len(principal)):

            if j == i + 1:
                    print("Cyberluta do Torneio Principal")
                    batalha(principal[i], principal[j], False)


                    if principal[i].torneio == "repescagem":
                         repescagem.append(principal[i])
                         principal.remove(principal[i])

                    elif principal[j].torneio == "repescagem":
                        repescagem.append(principal[j])
                        principal.remove(principal[j])









