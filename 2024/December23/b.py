from a import *


clusters = findClustersOfThree(computerToOthersMap)

print("Clusters of 3:", len(clusters))

i = 4
while len(clusters) > 0:
    currentCluster = set()
    for cluster in clusters:
        clusterValues = cluster.split(separator)
        listOfNeighbors = [computerToOthersMap[clusterValue] for clusterValue in clusterValues]
        for computer in computerToOthersMap.keys():
            computerInAllNeighbors = True
            for neighbors in listOfNeighbors:
                if not computer in neighbors:
                    computerInAllNeighbors = False
                    break
            if computerInAllNeighbors:
                tempClusterValues = clusterValues.copy()
                tempClusterValues.append(computer)
                tempClusterValues.sort()
                key = separator.join(tempClusterValues)
                currentCluster.add(key)
    clusters = currentCluster
    if len(clusters) == 1:
        print(f"Largest cluster of {i}:", clusters.pop())
        break
    print(f"Clusters of {i}: ", len(clusters))
    i+=1
