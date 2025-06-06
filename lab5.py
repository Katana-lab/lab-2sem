def read_graph(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        graph = [[] for _ in range(n)]
        for i in range(n):
            line = f.readline().strip()
            if line:
                neighbors = list(map(int, line.split()))
                graph[i] = neighbors
    return graph

def dfs(graph, start, visited):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def find_root_vertex(graph):
    n = len(graph)
    for v in range(n):
        visited = [False] * n
        dfs(graph, v, visited)
        if all(visited):
            return v
    return -1

def main():
    graph = read_graph("input.txt")
    root = find_root_vertex(graph)
    with open("output.txt", "w") as f:
        f.write(str(root))

if __name__ == "__main__":
    main()