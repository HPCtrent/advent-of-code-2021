with open('input.txt') as f:
	lines = f.readlines()


count = 0
lastline = None

for line in lines:
	if lastline != None:
		if int(line) > int(lastline):
			count += 1
	lastline = line

print("Part 1: " + str(count))


count = 0
lastsum = 0
currentsum = 0

for i in range(3, len(lines)):
	lastsum = int(lines[i-3]) + int(lines[i-2]) + int(lines[i-1])
	currentsum = int(lines[i-2]) + int(lines[i-1]) + int(lines[i])

	if currentsum > lastsum:
		count += 1

print("Part 2: " + str(count))
