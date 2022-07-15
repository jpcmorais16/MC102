a = input()
b = a.split(" ")

M = int(b[0])
E = int(b[1])
L = int(b[2])






def cod(mensagem, q, m, e):
    if m == 1:


        msgcod = ""

        if q % 2 == 0:
            mensagem = mensagem[::-1]

            for i in mensagem:
                x = ord(i)
                y = oct(x)
                z = ""
                for j in range(2, len(y)):
                    z += y[j]

                z= z.zfill(e)


                msgcod += z

        else:
            for i in mensagem:
                x = ord(i)
                y = hex(x)
                y_1 = ""
                z = ""

                for j in range(2, len(y)):
                    if ord(y[j]) in range(97, 103):
                        l = ord(y[j]) - 32

                        y_1 += chr(l)
                    else:
                        y_1 += y[j]

                    z += y_1[j-2]
                    z = z.zfill(e - 1)

                msgcod += z

        return msgcod

    elif m == 2:
        msgdecod = ""
        if q % 2 == 0:

            for i in range(0, len(mensagem), e):
                x = int("0o" + (mensagem[i + e - 3]) +
                        (mensagem[i + e - 2]) + (mensagem[i + e - 1]), 8)

                msgdecod += chr(x)
            msgdecod = msgdecod[::-1]


        else:
            z = ""
            for i in mensagem:
                if i.isupper():
                    z += i.lower()
                else:
                    z += i

            for i in range(0, len(mensagem), e):
                x = int("0x"
                        + mensagem[i + e - 2] + mensagem[i + e - 1], 16)

                msgdecod += chr(x)

        return msgdecod

mensagens = []
p = 1
while p <= L:
    msg = input()
    mensagens.append(msg)

    p += 1


q = 1

for i in mensagens:
    print(cod(i, q, M, E))
    q += 1

