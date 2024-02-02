def factorial (n):
    lista = []
    for operar in range(n-1, 1, -1):
        lista.append(operar)
    for i in range(len(lista)):
        n = n * lista[i]
    return n