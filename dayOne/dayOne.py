# Count the number of times a depth measurement increases from the previous measurement
# How many measurements are larger than the previous measurement?

# Get data
with open('dayOne.in') as input:
	data = [int(i) for i in input.read().strip().split("\n")]

print data


# Part 1
def part1():
	increases = []
	for firstN, secondN in zip(data, data[1:]):
		increases.append(secondN > firstN)

	return sum(increases)


print "Answer to part one:", part1()