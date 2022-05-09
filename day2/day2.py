# --- Day 2: Dive! ---

# Get data
with open('dayTwo.in') as input:
	data = [str(i) for i in input.read().strip().split("\n")]

# What do you get if you multiply your final horizontal position by your final depth?
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
# What do you get if you multiply your final horizontal position by your final depth? 
# Where depth is a product of your aim and forward value if aim is not equal to zero
def part2():
	aim = 0
	x = 0
	y = 0
	for command in data:
		if 'forward' in command:
			x += int(command[8:])
			if aim != 0:
				y += aim * int(command[8:])
		elif 'up' in command:
			aim -= int(command[3:])
		elif 'down' in command:
			aim += int(command[5:])
	return x * y



print "Answer to part one:", part1()
print "Answer to part two:", part2()