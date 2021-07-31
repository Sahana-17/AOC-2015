input = "ghijklmn"
input_str = str(input)
print(input_str)
flag = False
length = len(input_str)

error = ['i','o','l']
#while flag == False:

for j in range(0, length):
	if input_str[j] in error:
		x = input_str[j]
		val = ord(x)
		val = val + 1
		y = chr(val)
		print("VAL : ", y)
		print(input_str[0:j])
		break
		#new = input_str[0:j-1] & y
		#print("NEW : ", new)

print(input_str)
#for i in range(length-1, -1, -1):
#	print(input_str[i])
#	x = input_str[i]
#	val = ord(x)
#	print(val)	
