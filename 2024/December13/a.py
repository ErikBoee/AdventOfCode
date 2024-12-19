file = open("input.txt", "r")
lines = file.readlines()
file.close()

priceA = 3
priceB = 1

equations = []
equations.append({})
for line in lines:
    line = line.strip()
    if line == "":
        equations.append({})
        continue
    currentEquation = equations[-1]
    if line.startswith("Button A:"):
        currentEquation["AConstantX"] = int(line.split("X+")[1].split(",")[0])
        currentEquation["AConstantY"] = int(line.split("Y+")[1])
    elif line.startswith("Button B:"):
        currentEquation["BConstantX"] = int(line.split("X+")[1].split(",")[0])
        currentEquation["BConstantY"] = int(line.split("Y+")[1])
    else:
        currentEquation["XTarget"] = int(line.split("X=")[1].split(",")[0])
        currentEquation["YTarget"] = int(line.split("Y=")[1])

def isApproxInt(number):
    return abs(number - round(number)) < 0.001

def evaluateEquation(equation):
    nominatorB = equation["YTarget"] - equation["AConstantY"]*equation["XTarget"]/equation["AConstantX"]
    denominatorB = equation["BConstantY"]- equation["AConstantY"]*equation["BConstantX"]/equation["AConstantX"]
    if abs(denominatorB) < 0.00001:
        return "infiniteAmount"
    b = nominatorB/denominatorB
    if not isApproxInt(b):
        return "noSolution"
    a = (equation["XTarget"] - equation["BConstantX"]*b)/equation["AConstantX"]
    if not isApproxInt(a):
        return "noSolution"
    return int(round(a)),int(round(b))


def evaluateEquations(equations):
    results = []
    for equation in equations:
        result = evaluateEquation(equation)
        results.append(result)
    totalPrice = 0
    numberOfNoSolutions = 0
    for result in results:
        if result == "infiniteAmount":
            print("infiniteAmount")
            continue
        if result == "noSolution":
            numberOfNoSolutions += 1
            continue    
        a,b = result
        totalPrice += a*priceA + b*priceB
    print(numberOfNoSolutions)
    return totalPrice

print(len(equations))
print(evaluateEquations(equations))