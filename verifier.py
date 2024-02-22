import sys
import os

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

def buildGraph(n, dependencies, removed):
    graph = {i+1: [] for i in range(n)}
    
    for node, deps in dependencies.items():
        if node not in removed:
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
    with open('./output_verification.txt', 'w') as file:
        if len(sys.argv) < 2:
            print("Please provide the input file name.")
            return
        directory = sys.argv[1]
        for teamOutput in os.listdir(directory):
            n_rem, removed = readInputFile(directory + "/" + teamOutput)
            
            filePath = "input_cycles_10.txt" #TODO #Needs to be updated 
            n, dependencies = readInputFile(filePath)
            graph = buildGraph(n, dependencies, removed)
            topoSort = topologicalSort(graph, n)
            if topoSort == None:
                file.write("F " + teamOutput +"\n")
            else:
                file.write("T " + teamOutput +"\n")
    
main()

