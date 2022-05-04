# Count the number of times a depth measurement increases from the previous measurement
# How many measurements are larger than the previous measurement?
import dayOneInput

increases = []
for i, measurement in enumerate(dayOneInput.nums):
	if i > 0:
		if measurement > dayOneInput.nums[i - 1]:
			increases.append(measurement)

print(len(increases))

