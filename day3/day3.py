# --- Day 3: Binary Diagnostic ---

# Get data
with open('day3.in') as input:
	data = [str(i) for i in input.read().strip().split("\n")]

# Get power consumption
# Power consumption = gamma rate * epsilon rate
# Gamma rate is the most common value for each corresponding binary key
# epsilon rate is the least common value for each corresponding binary key

# Part 1
def part1():
	gamma = '' 
	epsilon = ''

	for digit in range(0, len(data[0])):
		zeros = 0
		ones = 0

		for number in data:
			if number[digit:digit + 1] == '0':
				zeros += 1
			else:
				ones += 1

		if int(zeros) > int(ones):
			gamma += '0'
			epsilon += '1'
		else:
			gamma += '1'
			epsilon += '0'

	return int(gamma, 2) * int(epsilon, 2)




print "Answer to part one:", part1()