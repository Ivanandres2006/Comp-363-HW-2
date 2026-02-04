# Task 1: Reachability
def reachability(s, G):
    r = []        
    S = [s]       

    while S:
        u = S.pop()

        if u not in r:
            r.append(u)

            for v in range(len(G)):
                if G[u][v] == 1 and v not in r:
                    S.append(v)

    return r


# Task 2: Counting components
def count_components(G):
    visited = []
    components = 0

    for i in range(len(G)):

        if i not in visited:
            components += 1

            S = [i]

            while S:
                u = S.pop()

                if u not in visited:
                    visited.append(u)

                    for v in range(len(G)):
                        if G[u][v] == 1 and v not in visited:
                            S.append(v)

    return components


#--------------------------TESTS--------------------------------
graph = [
   # 0 1 2 3 4 5 6 7
    [0,0,0,1,0,0,1,0],  # 0
    [0,0,0,0,0,1,0,0],  # 1
    [0,0,0,0,1,0,0,0],  # 2
    [1,0,0,0,0,1,0,0],  # 3
    [0,0,1,0,0,0,0,0],  # 4
    [0,1,0,1,0,0,0,0],  # 5
    [1,0,0,0,0,0,0,0],  # 6
    [0,0,0,0,0,0,0,0]   # 7
]


print(reachability(3, graph)) 
print()  
print(count_components(graph)) 
