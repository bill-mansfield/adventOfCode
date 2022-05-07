# --- Day 2: Dive! ---

# Get data
with open('dayTwo.in') as input:
	data = [str(i) for i in input.read().strip().split("\n")]

# Part 1
def part1():
	x = 0
	y = 0
	for command in data:
		if 'forward' in command:
			x += int(command[8:])
		elif 'up' in command:
			y -= int(command[3:])
		elif 'down' in command:
			y += int(command[5:])
	return x * y

# Part 2
# def part2():



print "Answer to part one:", part1()
# print "Answer to part two:", part2()