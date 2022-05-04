# Count the number of times a depth measurement increases from the previous measurement
# How many measurements are larger than the previous measurement?
import dayOneInput

increases = []

for firstN, secondN in zip(dayOneInput.nums, dayOneInput.nums[1:]):
	increases.append(secondN > firstN)

print(sum(increases))