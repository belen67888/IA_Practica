a = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 5), ('E', 1)],
    'C': [('E', 6)],
    'D': [('F', 2)],
    'E': [('F', 2)],
    'F': []
}

heuristics = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

open_list = [start]  
closed_list = []     

g_costs = {node: float('inf') for node in a}  
g_costs[start] = 0

f_costs = {node: float('inf') for node in a}
f_costs[start] = heuristics[start]


while open_list:

    current_node = min(open_list, key=lambda node: f_costs[node])

    if current_node == goal:
        print(f"El {goal} con un costo total de {g_costs[goal]}")
        break

    open_list.remove(current_node)
    closed_list.append(current_node)

    for neighbor, weight in a[current_node]:
        if neighbor in closed_list:
            continue  

        tentative_g_cost = g_costs[current_node] + weight

        if tentative_g_cost < g_costs[neighbor]:
            g_costs[neighbor] = tentative_g_cost
            f_costs[neighbor] = g_costs[neighbor] + heuristics[neighbor]

            if neighbor not in open_list:
                open_list.append(neighbor)

print("Costos finales:")
print(g_costs)
