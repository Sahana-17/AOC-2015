import os
import sys

count = 0
vowels = ['a', 'e', 'u', 'i', 'o']
nice = 0
char_list = []
value = 0

for line in sys.stdin:
	v = 0
	same = 0
	not_allowed = 0

	print(line)	
	string = str(line)
	length = len(string)
	same = 0
	value = 0
	for i in range(2,length):
		char = string[i]
		print("char")
		print(char)
		char2 = string[i-2]
		print("char2")
		print(char2)
		char1 = string[i-1]
		print("char1")
		print(char1)
		if char == char2:
			same = same + 1
		
		character = (char1+char)
		
		if (char1 == char2 and char1 == char):
			print(char)
		else:	
			if character in char_list:
				value = value + 1
			else:
				char_list.append(character)
	
	if same>=1 and value >=1:
		nice = nice + 1
		print("nice")

print("Nice : ", nice)
