file = open("input.txt", "r")
lines = file.readlines()
file.close()


maxX = 101
maxY = 103
robots = []
for line in lines:
    position = line.split("p=")[1].split(" v")[0].split(",")
    velocity = line.split("v=")[1].split(",")
    robots.append({"x": int(position[0]), "y": int(position[1]), "vx": int(velocity[0]), "vy": int(velocity[1])})


def robotPostionAfterSeconds(robot, seconds):
    posX = (robot["x"] + robot["vx"] * seconds) % maxX
    posY = (robot["y"] + robot["vy"] * seconds) % maxY
    return posX, posY

def robotsInQuadrants(robots, seconds):
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        x, y = robotPostionAfterSeconds(robot, seconds)
        midpositionX = (maxX  - 1) / 2
        midpositionY = (maxY  - 1) / 2
        if x < midpositionX and y < midpositionY:
            quadrants[0] += 1
        elif x > midpositionX and y < midpositionY:
            quadrants[1] += 1
        elif x < midpositionX and y > midpositionY:
            quadrants[2] += 1
        elif x > midpositionX and y > midpositionY:
            quadrants[3] += 1
    return quadrants


quadrants = robotsInQuadrants(robots, 100)

totalProduct = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print(totalProduct)


