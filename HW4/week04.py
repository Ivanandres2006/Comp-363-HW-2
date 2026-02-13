def sssp(s, G):
    n = len(G)
    no_edge = G[0][0]
    d = [float("inf")] * n
    d[s] = 0
    bag = [s]

    while bag:
        u = bag.pop()
        for v in range(n):
            if G[u][v] != no_edge:
                if d[v] > d[u] + G[u][v]:
                    d[v] = d[u] + G[u][v]
                    bag.append(v)

    return d


def reconstruct(d, s, graph):
    n = len(graph)
    no_edge = graph[0][0]
    p = [None] * n

    for v in range(n):
        if v != s:
            for u in range(n):
                if graph[u][v] != no_edge:
                    if d[u] + graph[u][v] == d[v]:
                        p[v] = u
                        break

    return p


def report_sssp(p, d, s):
    n = len(d)

    for v in range(n):
        if d[v] == float("inf"):
            print("No path to", v)
        else:
            path = []
            current = v

            while current is not None:
                path.append(current)
                current = p[current]

            path.reverse()

            for i in range(len(path)):
                if i != len(path) - 1:
                    print(path[i], end="-> ")
                else:
                    print(path[i], end="")

            print("  distance:", d[v])


graph = [
    [0, 5, 1, 5, 10, 0, 0, 0],
    [0, 0, 12, 5, 6, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 1, 5, 0],
    [0, 0, 0, 6, 0, 5, 0, 5],
    [0, 0, 0, 0, 0, 0, 1, 5],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

if __name__ == "__main__":
    s = 0
    d = sssp(s, graph)
    p = reconstruct(d, s, graph)

    print("Distances:", d)
    print("Predecessors:", p)
    print()
    report_sssp(p, d, s)
