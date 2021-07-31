import sys
x = 0
y = 0
comb = 0
length = 0
value = []
for line in sys.stdin:

	for word in line.split():
		length = length + 1
		if word.isdigit():
			value.append(int(word))

value.sort()			
print(value)		
print("Length : ", length)
for i in range(0,length):
	print(i)
	x = value[i]
	for j in range(0,length):
		if i==j:
			print("hi")
		else:
			print("Start : ", x) 
			x = x + value[j] 
			print("Later : ", x)
			if x == 25:
				comb = comb + 1
				print("Value 1 : ", value[i])
				print("Value 2 : ", value[j])
				break

print("Combinations : ", comb)
		
