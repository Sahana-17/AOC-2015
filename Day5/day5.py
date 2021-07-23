import os

file = open(os.path.join(os.path.dirname('__file__'),"day5.in"))
count = 0
vowels = ['a', 'e', 'u', 'i', 'o']
nice = 0
char_list = []
part = int(input("Part 1 or 2 : "))
value = 0

while True:
	v = 0
	same = 0
	not_allowed = 0

	line = file.readline()
	if not line:
		break
	print(line)	
	string = str(line)
	length = len(string)
	if part == 1:

		for i in range(length):
			char = string[i]
			char1 = string[i-1]
			if char in vowels:
				v = v + 1
			if char == char1:
				same = same + 1
			character = (char1+char)
	
			if character == "ab" or character == "cd" or character == "pq" or character == "xy":
				not_allowed = not_allowed + 1

		if v >=3 and same>=1 and not_allowed == 0:
			nice = nice + 1 

	if part == 2:		
		same = 0
		value = 0
	
		for i in range(2,length):
			for j in range(i-1):
				if string[i:i+2] == string[j:j+2]:
					value = value + 1		
					print(value)
		for x in range(2,length):
			if (string[x] == string[x-2]):
				same = same + 1
				print(same)
		if same>=1 and value >=1:
			nice = nice + 1
			print("nice")
file.close()

print("Nice : ", nice)
