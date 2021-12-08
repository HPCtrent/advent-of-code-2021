with open('input.txt') as f:
	lines = f.readlines()


horizontal = 0
depth = 0

for line in lines:
	if line.split()[0] == "forward":
		horizontal += int(line.split()[1])
	if line.split()[0] == "up":
		depth -= int(line.split()[1])
	if line.split()[0] == "down":
		depth += int(line.split()[1])

answer = horizontal * depth

print("Part 1: " + str(answer))


horizontal = 0
depth = 0
aim = 0

for line in lines:
	if line.split()[0] == "forward":
		horizontal += int(line.split()[1])
		depth += int(line.split()[1]) * aim
	if line.split()[0] == "up":
		aim -= int(line.split()[1])
	if line.split()[0] == "down":
		aim += int(line.split()[1])

answer = horizontal * depth

print("Part 2: " + str(answer))
