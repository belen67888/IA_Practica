dfs = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
visita = []
pila = [2]

while pila:
    node = pila.pop()
    if node not in visita:
        print(node, end=" ")
        visita.append(node)
        pila.extend(dfs[node])
