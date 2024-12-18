import heapq

def dijkstra(graph, start):
    # Initialize distances to infinity and set start node's distance to 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Min heap to store nodes and their distances (priority queue)
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)

        # If the distance is already greater than the recorded one, skip it
        if current_distance > distances[current_node]:
            continue

        # Explore the neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If the newly calculated distance is smaller, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example of applying Dijkstra's algorithm
graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('A', 1), ('C', 2), ('E', 3)],
    'C': [('B', 2), ('E', 1)],
    'D': [('A', 4), ('E', 5)],
    'E': [('B', 3), ('C', 1), ('D', 5)]
}
print(dijkstra(graph, 'A'))


def bellman_ford(graph, start, V):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    for _ in range(V - 1):  # Relax all edges V-1 times
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                print("Graph contains negative weight cycle")
                return None
    
    return distances
# Graph representation using an adjacency list
graph = {
    'A': {'B': 1, 'C': 10},
    'B': {'C': 3},
    'C': {'D': 2},
    'D': {'B': -6}
}

start_node = 'A'
V = 4  # Number of vertices

# Call the Bellman-Ford function
result = bellman_ford(graph, start_node, V)

# Print the results
if result:
    print("Shortest distances from start node:")
    for node, distance in result.items():
        print(f"{node}: {distance}")