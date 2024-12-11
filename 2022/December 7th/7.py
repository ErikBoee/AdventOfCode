import uuid
input = open('./Calendar/December 7th/input.txt', 'r')

lines = input.readlines()

directories = []

complete_total = 0
for line in lines:
    stripped_line = line.strip()
    if stripped_line[0] == "$":
        if stripped_line[2:4] == 'cd':
            if stripped_line[5:] == '..':
                for directory in directories:
                    if directory["active"]:
                        directory["depth"] -= 1
                        if directory["depth"] == 0:
                            directory["active"] = False
                        
            else:
                for directory in directories:
                    if directory["active"]:
                        directory["depth"] += 1
                directories.append({
                    "depth": 1,
                    "totalsize": 0,
                    "active": True,
                })

    elif stripped_line[0:3] != "dir":
        number = int(stripped_line.split(' ')[0])
        for directory in directories:
            if directory["active"]:
                directory["totalsize"] += number

print("directories", directories)
total = 70000000
needed = 30000000

totalSum = sum([directory["totalsize"] for directory in directories if directory["totalsize"] <= 100000])

max_total = directories[0]["totalsize"]
must_clear = max_total - (total - needed)
current_min = total
print("must_clear", must_clear)
print("max_total", max_total)
for directory in directories:
    if directory["totalsize"] >= must_clear:
        if directory["totalsize"] < current_min:
            current_min = directory["totalsize"]

print("totalSum", totalSum)
print("current_min", current_min)