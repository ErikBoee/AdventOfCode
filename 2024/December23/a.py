file = open("input.txt", "r")
lines = file.readlines()
file.close()

separator = ","

computerToOthersMap = {}
for line in lines:
    computer, other = line.strip().split("-")
    if other in computerToOthersMap: 
        computerToOthersMap[other].append(computer)
    else:
        computerToOthersMap[other] = [computer]

    if computer in computerToOthersMap: 
        computerToOthersMap[computer].append(other)
    else:
        computerToOthersMap[computer] = [other]
    

def findClustersOfThree(computerToOthersMap):
    clusters = set()
    for computer in computerToOthersMap:
        originalNeighbors = computerToOthersMap[computer]
        for neighor in originalNeighbors:
            neigborsOfNeighbor = computerToOthersMap[neighor]
            for n in neigborsOfNeighbor:
                if n in originalNeighbors:
                    elements = [computer, neighor, n]
                    elements.sort()
                    clusters.add(elements[0] + separator +  elements[1] + separator + elements[2])
    return clusters

def findClustersWhereAtLeastOneComputerStartsWithT(clusters):
    clustersWithT = set()
    for cluster in clusters:
        clusterValues = cluster.split(separator)
        if len([value for value in clusterValues if value.startswith("t")]) > 0:
            clustersWithT.add(cluster)
    return clustersWithT


clustersOfThree = findClustersOfThree(computerToOthersMap)
clustersWithT = findClustersWhereAtLeastOneComputerStartsWithT(clustersOfThree)
print(len(clustersWithT))