

totalAmountPoints = 104576
familyhomeAmountPoint = 400
bungalowAmountPoint = 546
mansionsPoint = 1122

amountFamilyhome = 12
amountBungalow = 5
amountMansions = 3

# amountFamilyhome = 24
# amountBungalow = 10
# amountMansions = 6

# amountFamilyhome = 36
# amountBungalow = 15
# amountMansions = 9

stateSpace: int = 1
cntr: int = 0
power = 0


while amountFamilyhome > 0:
	stateSpace = stateSpace * totalAmountPoints
	totalAmountPoints = totalAmountPoints - familyhomeAmountPoint
	cntr += 1
	amountFamilyhome -= 1
	print(cntr)

while amountBungalow > 0:
	stateSpace = stateSpace * totalAmountPoints
	totalAmountPoints = totalAmountPoints - amountBungalow
	cntr += 1
	amountBungalow -= 1
	print(cntr)

while amountMansions > 0:
	stateSpace = stateSpace * totalAmountPoints
	totalAmountPoints = totalAmountPoints - amountMansions
	cntr += 1
	amountMansions -= 1
	print(cntr)
	while stateSpace > 10:
		power += 1
		stateSpace /= 10

print(round(stateSpace, 2), power)
print ("statespace", stateSpace)
print ("cntr", cntr)