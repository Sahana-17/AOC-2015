input = 11
p = ""
value = 0
input_str = str(input)
	
length = len(input_str)

for i in range(length):
	print(input_str[i])
	if i == length-1:
		print("bye")	
	else:
		value = 1
		if input_str[i] == input_str[i+1]:
			
			value = value + 1
		else:
			value = 1
	y = str(value)
	x = (y+input_str[i])
	print("TRY : ", x)
	print("", i, ": ", value)
	p = (p+x)
print("New : ", p)
