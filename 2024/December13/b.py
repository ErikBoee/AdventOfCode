from a import *
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
        currentEquation["XTarget"] = int(line.split("X=")[1].split(",")[0]) + 10000000000000
        currentEquation["YTarget"] = int(line.split("Y=")[1]) + 10000000000000

print(evaluateEquations(equations))