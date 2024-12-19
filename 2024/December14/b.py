from a import *
import time


def eightConsecutiveRobots(map):
    for y in range(len(map)):
        line = map[y]
        numberOfConsecutive = 0
        for x in range(len(line)):
            if line[x] != ".":
                numberOfConsecutive += 1
            else:
                numberOfConsecutive = 0
            if numberOfConsecutive == 9:
                return True      
    return False
            

def printMap(robots, seconds):
    map = [["." for x in range(maxX)] for y in range(maxY)]
    for robot in robots:
        x, y = robotPostionAfterSeconds(robot, seconds)
        if map[y][x] == ".":
            map[y][x] = "1"
        else:
            map[y][x] = str()
    if eightConsecutiveRobots(map) or seconds % 100 == 0:
        print("Found it at", seconds)
    else:
        return
    for line in map:
        print("".join(line))

for i in range(10000):
    printMap(robots, i)

