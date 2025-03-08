graph = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Oradea', 'Arad'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Lasi'],
    'Lasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Lasi']
}

def bfs_search(graph, kota_awal, kota_tujuan):
    queue = [kota_awal]
    visited = []
    came_from = {}
    came_from[kota_awal] = None
    
    while len(queue) > 0:
        current = queue[0] 
        queue = queue[1:]  
        
        if current == kota_tujuan:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        if current not in visited:
            visited.append(current)
            for neighbor in graph[current]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    came_from[neighbor] = current
    
    return None

kota_awal = input("Masukkan kota asal: ")
kota_tujuan = input("Masukkan kota tujuan: ")
path = bfs_search(graph, kota_awal, kota_tujuan)
if path:
    print("Jalur dari", kota_awal, "ke", kota_tujuan, ":", path)
else:
    print("Tidak ada jalur dari", kota_awal, "ke", kota_tujuan)
