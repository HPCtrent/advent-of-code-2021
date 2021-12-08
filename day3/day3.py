with open('input.txt') as f:
	lines = f.readlines()

def find_most_common(lines):
    ones = 0
    zeroes = 0

    for line in lines:
            if line[i] == "1":
                ones += 1
            if line[i] == "0":
                zeroes += 1
    
    if zeroes > ones:
        return "0"
    if ones > zeroes:
        return "1"
    if zeroes == ones:
        return "equal"


numlength = 12
mostcommon = ""


#Part 1
gamma = ""
epsilon = ""

for i in range(numlength):
    mostcommon = find_most_common(lines)

    gamma += mostcommon
    epsilon += str(int(not int(mostcommon)))

gammadecimal = int(gamma, 2)
epsilondecimal = int(epsilon, 2)

answer = gammadecimal * epsilondecimal
print("Part 1: " + str(answer))


#Part 2
decisionbit = 0

listcopy = lines
oxygen = 0
for i in range(numlength):
    mostcommon = find_most_common(listcopy)

    if mostcommon == "0":
        decisionbit = "0"
    else:
        decisionbit = "1"
    
    listcopy = [line for line in listcopy if line[i] == decisionbit]

    if len(listcopy) == 1:
        oxygen = int(listcopy[0], 2)
        break


listcopy = lines
carbon = 0
for i in range(numlength):
    mostcommon = find_most_common(listcopy)
    
    if mostcommon == "0":
        decisionbit = "1"
    else:
        decisionbit = "0"
    
    listcopy = [line for line in listcopy if line[i] == decisionbit]

    if len(listcopy) == 1:
        carbon = int(listcopy[0], 2)
        break


answer = oxygen * carbon

print("Part 2: " + str(answer))