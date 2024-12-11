file = open("input.txt", "r")
lines = file.readlines()
file.close()

import z3 as z3


twoDLines = []
for line in lines:
    positions = [int(x) for x in line.split(" @ ")[0].split(", ")]
    velocities = [int(x) for x in line.split(" @ ")[1].split(", ")]
    minValueX = positions[0] if velocities[0] > 0 else None
    maxValueX = positions[0] if velocities[0] < 0 else None
    minValueY = positions[1] if velocities[1] > 0 else None
    maxValueY = positions[1] if velocities[1] < 0 else None
    slope = velocities[1] / velocities[0]
    intercept = positions[1] - slope * positions[0]
    twoDLines.append([slope, intercept, minValueX, maxValueX, minValueY, maxValueY])

def findIntersection(line1, line2):
    if line1[0] == line2[0]:
        return None
    x = (line2[1] - line1[1]) / (line1[0] - line2[0])
    y = line1[0] * x + line1[1]
    return [x, y] 

lowRange = 200000000000000
highRange = 400000000000000
def inRange(value):
   return value >= lowRange and value <= highRange

def inFuture(values, intercection):
    if values[0] != None and intercection[0] < values[0]:
            return False
    if values[1] != None and intercection[0] > values[1]:
            return False
    if values[2] != None and intercection[1] < values[2]:
            return False
    if values[3] != None and intercection[1] > values[3]:
            return False
    return True

numberIntersectionsInRange = 0
numberIntersections = 0
for i in range(len(twoDLines)):
    twoDLine1 = twoDLines[i]
    for j in range(i + 1, len(twoDLines)):
        twoDLine2 = twoDLines[j]
        intersection = findIntersection(twoDLine1, twoDLine2)
        if intersection != None:
            numberIntersections += 1
            if inRange(intersection[0]) and inRange(intersection[1]) and inFuture(twoDLine1[2:], intersection) and inFuture(twoDLine2[2:], intersection):
                numberIntersectionsInRange += 1
print("Part 1", numberIntersectionsInRange)

threeDLines = []
for line in lines[:3]:
    positions = [int(x) for x in line.split(" @ ")[0].split(", ")]
    velocities = [int(x) for x in line.split(" @ ")[1].split(", ")]
    threeDLines.append(positions + velocities)

x, y, z, vx, vy, vz, t1, t2, t3 = z3.Reals('x y z vx vy vz t1 t2 t3')

s = z3.Solver()
equations = []

i = 1
for threeDLine in threeDLines:
    if i == 1:
        equations.append(x + vx * t1 == threeDLine[0] + t1 * threeDLine[3])
        equations.append(y + vy * t1 == threeDLine[1] + t1 * threeDLine[4])
        equations.append(z + vz * t1 == threeDLine[2] + t1 * threeDLine[5])
    elif i == 2:
        equations.append(x + vx * t2 == threeDLine[0] + t2 * threeDLine[3])
        equations.append(y + vy * t2 == threeDLine[1] + t2 * threeDLine[4])
        equations.append(z + vz * t2 == threeDLine[2] + t2 * threeDLine[5])
    elif i == 3:
        equations.append(x + vx * t3 == threeDLine[0] + t3 * threeDLine[3])
        equations.append(y + vy * t3 == threeDLine[1] + t3 * threeDLine[4])
        equations.append(z + vz * t3 == threeDLine[2] + t3 * threeDLine[5])
    i += 1

s.add(*equations)
s.check()
m = s.model()
print("Part 2", m[x].as_long() + m[y].as_long() + m[z].as_long())
