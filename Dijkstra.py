dijk = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

start = 0

distances = {0: float('inf'), 1: float('inf'), 2: float('inf'), 3: float('inf')}
distances[start] = 0  

visited = []

while len(visited) < len(dijk):
    min_node = None
    for node in distances:
        if node not in visited:
            if min_node is None:
                min_node = node
            elif distances[node] < distances[min_node]:
                min_node = node
    
    visited.append(min_node)
    for neighbor, weight in dijk[min_node]:
        new_distance = distances[min_node] + weight
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance

print(distances)
