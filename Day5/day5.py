#Santa needs help figuring out which strings in his text file are naughty or nice.

#A nice string is one with all of the following properties:

#It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
#For example:

#ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.

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
