input = 111221
p = ""
value = 0
print("Input : ", input)
input_str = str(input)
	
length = len(input_str)
x = ""
y = ""
i= 0
while i < length:
	print("----i is ", i)
	print("----value is ", i)
	value = value + 1
	if i+1 < length:
		print("ith pos",input_str[i])
		print("i+1 pos",input_str[i+1])
		if input_str[i] == input_str[i+1]:
			value = value + 1
			i= i + 1		
		else:
			print("VAL : ", value)
			y = str(value)
			x = (y+input_str[i])
			print("TRY : ", x)
			print("", i, ": ", value)
			p = (p+x)
			value = 0
	else:
		i = i + 1
		break
	i = i +1
	
print("VAL : ", value)
y = str(value)
x = (y+input_str[i-1])
print("TRY : ", x)
print("", i, ": ", value)
p = (p+x)
print("New : ", p)
