import copy

file = open("input.txt", "r")
lines = file.readlines()
file.close()

workflows = {}

items = []

addingWorkflows = True
for line in lines:
    if line == "\n":
        addingWorkflows = False
    elif addingWorkflows:
        name = line.strip().split("{")[0]
        conditions = line.strip().split("{")[1].split("}")[0].split(",")
        workflowConditions = []
        for i in range(len(conditions)):
            if len(conditions[i].split(":")) > 1:
                destination = conditions[i].split(":")[1].strip()
                rest = conditions[i].split(":")[0]
                char_to_compare = rest[0]
                operator = rest[1]
                value = int(rest[2:])
            else :
                destination = conditions[i].strip()
                char_to_compare = None
                operator = None
                value = None
            workflowConditions.append({"destination": destination, "char_to_compare": char_to_compare, "operator": operator, "value": value})
        workflows[name] = workflowConditions
    else:
        lineItems = line.strip().split("{")[1].split("}")[0].split(",")
        items.append({"x": int(lineItems[0].split("=")[1]), "m": int(lineItems[1].split("=")[1]), "a": int(lineItems[2].split("=")[1]), "s": int(lineItems[3].split("=")[1])})

print(workflows)
print(items)

originItems = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]

charToIndex = {"x": 0, "m": 1, "a": 2, "s": 3}

def investigateList(initialDest, sumOfAcceptedItems, items):
    dest = initialDest
    while dest != "A" and dest != "R":
        workflow = workflows[dest]
        for workflowCondition in workflow:
            if workflowCondition["char_to_compare"] == None:
                dest = workflowCondition["destination"]
                break
            else:
                if workflowCondition["operator"] == ">":
                    if items[charToIndex[workflowCondition["char_to_compare"]]][0] > workflowCondition["value"]:
                        dest = workflowCondition["destination"]
                        break
                    elif items[charToIndex[workflowCondition["char_to_compare"]]][1] > workflowCondition["value"]:
                        newItems = copy.deepcopy(items)
                        newItems[charToIndex[workflowCondition["char_to_compare"]]][0] = workflowCondition["value"] + 1
                        items[charToIndex[workflowCondition["char_to_compare"]]][1] = workflowCondition["value"]
                        sumOfAcceptedItems = investigateList(workflowCondition["destination"], sumOfAcceptedItems, newItems)
                        
                elif workflowCondition["operator"] == "<":
                    if items[charToIndex[workflowCondition["char_to_compare"]]][1] < workflowCondition["value"]:
                        dest = workflowCondition["destination"]
                        break
                    elif items[charToIndex[workflowCondition["char_to_compare"]]][0] < workflowCondition["value"]:
                        newItems = copy.deepcopy(items)
                        newItems[charToIndex[workflowCondition["char_to_compare"]]][1] = workflowCondition["value"] - 1
                        items[charToIndex[workflowCondition["char_to_compare"]]][0] = workflowCondition["value"]
                        sumOfAcceptedItems = investigateList(workflowCondition["destination"], sumOfAcceptedItems, newItems)
    
    if dest == "A":
        sumOfAcceptedItems += (items[0][1] - items[0][0] + 1) * (items[1][1] - items[1][0] + 1) * (items[2][1] - items[2][0] + 1) * (items[3][1] - items[3][0] + 1)
    return sumOfAcceptedItems
    

print(investigateList("in", 0, originItems))



        

    