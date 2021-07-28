c_dist = 0
total = 0


i = 1
while total <= 2503:
	if i <= 1:
		i = i + 1
		total = total +1
		c_dist = c_dist + 37
		
	else:
		total = total + 36
		i = 1

print("Dist : ", c_dist)

