file = open("input.txt", "r")
lines = file.readlines()
file.close()



def doOperation(initialValue, multiplier, isDivision):
    if isDivision:
        multipliedValue =  initialValue // multiplier
    else:
        multipliedValue = initialValue * multiplier
    
    return (initialValue^multipliedValue)%16777216

def convertNumber(number):
    return doOperation(doOperation(doOperation(number, 64, False), 32, True), 2048, False)


totalSum = 0
k=0
for line in lines:
    number = int(line.strip())
    for i in range(2000):
        number = convertNumber(number)
    totalSum += number
    k+=1

print(totalSum)