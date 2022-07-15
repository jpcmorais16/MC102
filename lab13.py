"""recebe uma malha MxN
se M e N são pares:
    se M > N: cria uma nova malha (M-N)xN
    se M < N: cria uma nova malha (N-M)xM

se M ou N é ímpar:
    subtrai 1 do(s) impar(es) para o(s) transformar em par(es)"""


def log2_r(n, p):
    if n == 1:
        return p

    elif n % 2 != 0:
        return -1

    else:
        p += 1
        log2_r(n / 2, p)

def log2(x):
    p = 0
    if x % 2 != 0:
        return -1
    log2_r(x, p)




def malha_r(M, N, p, q):
    if M % 2 == 0 and N % 2 == 0:
        if M == N:
            p += 1
            print(p)
            print(q)

        else:
            if M > N:
                p += 1
                q += log2(N)

                malha_r(M-N, N, p, q)
                #print("a",p)


            else:
                p += 1
                malha_r(N-M, M, p, q)
                #print("b",p)

    elif M % 2 == 0:
        p += M
        q += M
        malha_r(M, N - 1, p, q)

    elif N % 2 == 0:
        p += N
        q += N
        malha_r(M - 1, N, p, q)

    else:
        p += M + N - 1
        q += M + N - 1
        malha_r(M - 1, N - 1, p, q)


def malha(M, N):
    num_tot = 0
    PM = 0

    malha_r(M, N, num_tot, PM)


malha(64, 8)