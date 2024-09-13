arbol = [5, [2, None, None], [12, None, None]]

def binario(arbol):
    if arbol:
        binario(arbol[1])
        print(arbol[0], end=" ")
        binario(arbol[2])

binario(arbol)