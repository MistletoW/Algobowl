import sys

def readInputFile(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()
    
    n = int(lines[0].strip())
    dependencies = {i+1: [] for i in range(n)}
    
    for i, line in enumerate(lines[1:], start=1):
        parts = line.strip().split()
        numDependencies = int(parts[0])
        if numDependencies > 0:
            dependencies[i] = list(map(int, parts[1:]))
    
    return n, dependencies

def buildGraph(n, dependencies):
    graph = {i+1: [] for i in range(n)}
    
    for node, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(node)
    
    return graph

def topologicalSort(graph, n):
    inDegree = {i: 0 for i in range(1, n+1)}
    for deps in graph.values():
        for node in deps:
            inDegree[node] += 1
    
    queue = [node for node, degree in inDegree.items() if degree == 0]
    topOrder = []
    
    while queue:
        node = queue.pop(0)
        topOrder.append(node)
        
        for adj in graph[node]:
            inDegree[adj] -= 1
            if inDegree[adj] == 0:
                queue.append(adj)
                
    if len(topOrder) == n:
        return topOrder
    else:
        return None

def main():
    if len(sys.argv) < 2:
        print("Please provide the input file name.")
        return
    
    filePath = sys.argv[1]
    n, dependencies = readInputFile(filePath)
    graph = buildGraph(n, dependencies)
    topoSort = topologicalSort(graph, n)

    if topoSort == None:
        print("Failed verification " + sys.argv[1])
    else:
        print("Passed Verification " + sys.argv[1])
    
main()

