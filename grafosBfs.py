bfs = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
vist = []
cola = [2]

while cola:
    node = cola.pop(0)
    if node not in vist:
        print(node, end=" ")
        vist.append(node)
        cola.extend(bfs[node])

