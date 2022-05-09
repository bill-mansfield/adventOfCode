# --- Day 1: Sonar Sweep ---

# Get data
with open('dayOne.in') as input:
	data = [int(i) for i in input.read().strip().split("\n")]

# Count the number of times a depth measurement increases from the previous measurement
# How many measurements are larger than the previous measurement?
# Part 1
def part1():
	increases = []
	for firstN, secondN in zip(data, data[1:]):
		increases.append(secondN > firstN)

	return sum(increases)

# Count the number of times the sum of measurements in this sliding window increases
# How many sums are larger than the previous sum?
# Part 2
def part2():
	# allSums = [sum(tuple) for tuple in zip(data, data[1:], data[2:])]
	allSums = []
	for tuple in zip(data, data[1:], data[2:]):
		allSums.append(sum(tuple))

	increases = []
	for firstSum, secondSum in zip(allSums, allSums[1:]):
		increases.append(firstSum < secondSum)
	
	return sum(increases)


print "Answer to part one:", part1()
print "Answer to part two:", part2()