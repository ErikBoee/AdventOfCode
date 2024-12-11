import copy

file = open("input.txt", "r")
lines = file.readlines()
file.close()

nodes = set()
edges = set()
for line in lines:
    firstNode = line.strip().split(":")[0]
    nodes.add(firstNode)
    remainingNodes = line.strip().split(": ")[1].split(" ")
    for node in remainingNodes:
        nodes.add(node)
        edges.add((firstNode, node, 1))
    
def mostTightlyConnectedNode(remainingNodes, edges, newNodes):
    selectedNode = None
    remainingNodeToConnections = {}
    for node in remainingNodes:
        remainingNodeToConnections[node] = 0
    for edge in edges:
        if edge[0] in newNodes:
           if edge[1] in remainingNodes:
               remainingNodeToConnections[edge[1]] += 1
        elif edge[1] in newNodes:
            if edge[0] in remainingNodes:
                remainingNodeToConnections[edge[0]] += 1
    mostlyConnected = 0
    for node in remainingNodes:
        if remainingNodeToConnections[node] > mostlyConnected:
            mostlyConnected = remainingNodeToConnections[node]
            selectedNode = node
    return selectedNode

def cutFromLastNode(edges, lastNode):
    totalNumberOfEdges = 0
    for edge in edges:
        if lastNode in edge:
            totalNumberOfEdges += edge[2]
    return totalNumberOfEdges

def mergeNodes(lastTwo, nodes, edges):
    firstNode = lastTwo[0]
    secondNode = lastTwo[1]
    mergedNode = firstNode + "-" + secondNode
    firstNodeEdges = {}
    secondNodeEdges = {}
    newEdges = set()
    for edge in edges:
        if edge[0] == firstNode:
            firstNodeEdges[edge[1]] = edge[2]
        elif edge[1] == firstNode:
            firstNodeEdges[edge[0]] = edge[2]
        elif edge[0] == secondNode:
            secondNodeEdges[edge[1]] = edge[2]
        elif edge[1] == secondNode:
            secondNodeEdges[edge[0]] = edge[2]
        else:
            newEdges.add(edge)
        
    
    for k, v in firstNodeEdges.items():
        if k in secondNodeEdges:
            newEdges.add((mergedNode, k, v + secondNodeEdges[k]))
        elif k != secondNode:
            newEdges.add((mergedNode, k, v))
    
    for k, v in secondNodeEdges.items():
        if k not in firstNodeEdges and k != firstNode:
            newEdges.add((mergedNode, k, v))
    
    nodes.remove(firstNode)
    nodes.remove(secondNode)
    nodes.add(mergedNode)
    return nodes, newEdges

def edgesBetweenPartitions(firstPartition, secondPartition, edges):
    edgesBetween = set()
    for edge in edges:
        if edge[0] in firstPartition and edge[1] in secondPartition:
            edgesBetween.add(edge)
        elif edge[1] in firstPartition and edge[0] in secondPartition:
            edgesBetween.add(edge)
    return edgesBetween
    

def findMinCutPhase(nodes: set, edges):
    node = nodes.pop()
    newNodes = set()
    newNodes.add(node)
    if len(nodes) == 1:
        last = nodes.pop()
        return cutFromLastNode(edges, last), [node, last]
    lastTwo = []
    last = ""
    cutsFromLastNode = 0
    while len(nodes) > 1:
        node = mostTightlyConnectedNode(nodes, edges, newNodes)
        newNodes.add(node)
        nodes.remove(node)
        if len(nodes) == 1:
            last = nodes.pop()
            lastTwo = [node, last]
            cutsFromLastNode = cutFromLastNode(edges, last)
    return cutsFromLastNode, lastTwo


minCut = 100000000
origLength = len(nodes)
lastOnMinCut = ""
nodesOnMinCut = set()
edgesOnMinCut = set()
originalEdges = copy.deepcopy(edges)
while minCut > 3:
    nodesCopy = copy.deepcopy(nodes)
    edgesCopy = copy.deepcopy(edges)
    cut, lastTwo = findMinCutPhase(nodesCopy, edgesCopy)
    if cut < minCut:
        minCut = cut
        lastOnMinCut = lastTwo[1]
        nodesOnMinCut = copy.deepcopy(nodes)
        edgesOnMinCut = copy.deepcopy(edges)

    nodes, edges = mergeNodes(lastTwo, nodes, edges)
    print(len(nodes))

nodesOnMinCut.remove(lastOnMinCut)
secondPartitiononMinCut = set(lastOnMinCut.split("-"))
firstPartitiononMinCut = set()
for node in nodesOnMinCut:
    origNodes = node.split("-")
    for origNode in origNodes:
        firstPartitiononMinCut.add(origNode)

edgesBetween = edgesBetweenPartitions(firstPartitiononMinCut, secondPartitiononMinCut, originalEdges)
print(minCut)
print(len(firstPartitiononMinCut) * len(secondPartitiononMinCut))