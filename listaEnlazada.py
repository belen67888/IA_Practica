containerEnlazada=[10, [20, [30, None]]]

current_node = containerEnlazada
while current_node is not None:
    print(current_node[0])
    current_node = current_node [1]
    print("Hola")


