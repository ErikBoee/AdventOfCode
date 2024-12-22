from a import *

separator = "&"

sequenceOfChangesToTotalValue = {}
for line in lines:
    number = int(line.strip())
    formerPrice = number % 10
    sequenceOfChangesAlreadySeen = {}
    sequenceOfChanges=""
    for i in range(2000):
        number = convertNumber(number)
        price = number % 10
        change = price - formerPrice
        formerPrice = price

        if sequenceOfChanges.count(separator) == 3:
            newSeqence = sequenceOfChanges[sequenceOfChanges.index(separator) + 1:] + separator + str(change)
        elif len(sequenceOfChanges) == 0:
            newSeqence = str(change)
        else: 
            newSeqence = sequenceOfChanges + separator + str(change)
        
        sequenceOfChanges = newSeqence
        if not sequenceOfChanges.count(separator) == 3 or sequenceOfChanges in sequenceOfChangesAlreadySeen:
            continue
        sequenceOfChangesAlreadySeen[sequenceOfChanges] = True

        if sequenceOfChanges in sequenceOfChangesToTotalValue:
            sequenceOfChangesToTotalValue[sequenceOfChanges] += price
        else:
            sequenceOfChangesToTotalValue[sequenceOfChanges] = price

print(max(sequenceOfChangesToTotalValue.values()))