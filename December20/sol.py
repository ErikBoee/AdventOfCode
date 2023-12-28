file = open("input.txt", "r")
lines = file.readlines()
file.close()

broadCasterDests = []
flipFlopModules = {}
conjunctionModules = {}

# greatest common divisor (GCD) via Euclidean algorithm
def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

# lcm of a list
def LCM(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//GCD(lcm, i)
    return lcm

for line in lines:
    broadCasterAndReceiver = line.strip().split(" -> ")
    receiver = broadCasterAndReceiver[1]
    broadCaster = broadCasterAndReceiver[0]
    if broadCaster == "broadcaster":
        broadCasterDests = receiver.split(", ")
    elif broadCaster[0] == "%":
        name = broadCaster[1:]
        dests = receiver.split(", ")
        flipFlopModules[name] = {
            "dests": dests,
            "state": "off"
        }
    elif broadCaster[0] == "&":
        name = broadCaster[1:]
        dests = receiver.split(", ")
        conjunctionModules[name] = {
            "dests": dests,
            "inputsToLastPulse": {}
        }

for flipFlopModule in flipFlopModules:
    for dest in flipFlopModules[flipFlopModule]["dests"]:
        if conjunctionModules.get(dest) != None:
            conjunctionModules[dest]["inputsToLastPulse"][flipFlopModule] = "low"
for conjunctionModule in conjunctionModules:
    for dest in conjunctionModules[conjunctionModule]["dests"]:
        if dest != conjunctionModule:
            if conjunctionModules.get(dest) != None:
                conjunctionModules[dest]["inputsToLastPulse"][conjunctionModule] = "low"

numberOfLows = 0
numberOfHighs = 0
# Part 2, find third last inputs for LCM, after, second not working
inputs = [["rm"]]

for h in range(3):
    newInputs = []
    for input in inputs[h]:
        if conjunctionModules.get(input) != None:
            newInputs += conjunctionModules[input]["inputsToLastPulse"].keys()
    inputs.append(newInputs)

lcms = inputs[2]
lcmsToLoop = {}

i = 1
while len(lcmsToLoop.keys()) < len(lcms):
    pulses = [("broadcaster","low")]
    while len(pulses):
        pulse = pulses.pop(0)
        dest = pulse[0]
        ray = pulse[1]
        if ray == "low":
            numberOfLows += 1
        else:
            numberOfHighs += 1
        if dest == "broadcaster":

            for newdest in broadCasterDests:
                pulses.append((newdest, ray, dest))
        if flipFlopModules.get(dest):
            if ray == "high":
                continue
            if flipFlopModules[dest]["state"] == "off":
                flipFlopModules[dest]["state"] = "on"
                for newdest in flipFlopModules[dest]["dests"]:
                    pulses.append((newdest, "high", dest))
            else:
                flipFlopModules[dest]["state"] = "off"
                for newdest in flipFlopModules[dest]["dests"]:
                    pulses.append((newdest, "low", dest))
        elif conjunctionModules.get(dest):
            formerDest = pulse[2]
            conjunctionModules[dest]["inputsToLastPulse"][formerDest] = ray
            allHighInputs = True
            for input in conjunctionModules[dest]["inputsToLastPulse"]:
                if conjunctionModules[dest]["inputsToLastPulse"][input] == "low":
                    allHighInputs = False
                    break
            newRay = "low" if allHighInputs else "high"
            if newRay == "low" and dest in lcms:
                    lcmsToLoop[dest] = i

            for newdest in conjunctionModules[dest]["dests"]:
                pulses.append((newdest, newRay, dest))
    if i ==1000:
        print("Part 1", numberOfLows * numberOfHighs)
    i += 1
    
print("Part 2", LCM(list(lcmsToLoop.values())))

