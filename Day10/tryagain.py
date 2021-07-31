input = 1321131112

input_str = str(input)
for x in range(50):
	length = len(input_str)
	i = 0
	out = ""
	while i < length:
		digit = input_str[i] 
		num = 1
		for j in range(i+1,length):
			if input_str[j] != digit:
				break
			else:
				num = num +1
				i = i +1
		out = out + str(num) + digit
		i = i+1
	input_str = out

print(out,len(out))
