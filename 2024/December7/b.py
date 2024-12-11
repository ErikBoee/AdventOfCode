
file = open("input.txt", "r")
lines = file.readlines()
file.close()

numberToPotentialFactors = {}

k=0
for line in lines:
    line = line.strip()
    resultAndFactors = line.split(": ")
    result = resultAndFactors[0]
    factors = resultAndFactors[1].split(" ")
    key = f"{result}-{k}"
    numberToPotentialFactors[key] = []
    for factor in factors:
        numberToPotentialFactors[key].append(int(factor))
    k+=1

def concatNumbers(number1, number2):
    return int(str(number1) + str(number2))

def canFactorsBeMultipliedToResult(factors, result):
    if len(factors) == 2:
        return (factors[0]*factors[1] == result) or (factors[1] + factors[0] == result) or (concatNumbers(factors[0], factors[1]) == result)
    
    additionResult = factors[0]+factors[1]
    multiplicationResult = factors[0]*factors[1]
    concatenationResult = concatNumbers(factors[0], factors[1])
    additionGivesTrue = canFactorsBeMultipliedToResult([additionResult] + factors[2:], result)
    multiplicationGivesTrue = canFactorsBeMultipliedToResult([multiplicationResult] + factors[2:], result)
    concatenationGivesTrue = canFactorsBeMultipliedToResult([concatenationResult] + factors[2:], result)
    return additionGivesTrue or multiplicationGivesTrue or concatenationGivesTrue

sumOfAcceptedNumbers = 0
numberOfOkay = 0
for key in numberToPotentialFactors:
    factors = numberToPotentialFactors[key]
    number = int(key.split("-")[0])
    if canFactorsBeMultipliedToResult(factors, number):
        sumOfAcceptedNumbers += number
        numberOfOkay += 1

print(sumOfAcceptedNumbers)