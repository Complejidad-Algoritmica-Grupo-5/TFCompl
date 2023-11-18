import heapq
from data_processing import load_graph_data
from calculate_traffic import calculate_traffic

def dijkstra(graph, start, end, hour):
    distances = {node: float('inf') for node in graph['nodes']}
    distances[start] = 0
    queue = [(0, start)]
    predecessors = {node: None for node in graph['nodes']}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        if current_node in graph['nodes'] and current_node in distances:
            for neighbor, edge_data in graph['nodes'][current_node]['neighbors'].items():
                if isinstance(edge_data, dict):
                    # Verifica si edge_data es un diccionario
                    weight = edge_data.get('weight', float('inf'))
                else:
                    # Si no es un diccionario, asume que es el peso directamente
                    weight = edge_data

                updated_weight = calculate_traffic(weight, hour)
                distance = current_distance + updated_weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
                    predecessors[neighbor] = current_node

    return distances, predecessors

def get_shortest_path(start, end, predecessors):
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    return path

# Test
if __name__ == '__main__':
    graph_data = load_graph_data()
    graph = {'nodes': graph_data[0], 'edges': graph_data[1]}

    start_node = 11
    end_node = 5985
    hour = 8
    distances, predecessors = dijkstra(graph, start_node, end_node, hour)
    shortest_path = get_shortest_path(start_node, end_node, predecessors)
    print(f"El camino más corto del punto {start_node} al punto {end_node} es el siguiente:")
    print(shortest_path)
    print(f"La distancia recorrida total es: {distances[end_node]}")