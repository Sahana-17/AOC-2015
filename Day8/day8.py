#For example:

#"" is 2 characters of code (the two double quotes), but the string contains zero characters.
#"abc" is 5 characters of code, but 3 characters in the string data.
#"aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
#"\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
#Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

#Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

#For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.

import sys

total = 0
char = 0
sum = 0
total_char = 0
for sline in sys.stdin:
	print(sline)
	line = sline.strip()
	quotes=0
	slash = 0
	hex = 0
	nonhex = 0
	length = len(line)
	print("Length",length)
	i = 1
	while i < length-1:
		if line[i] == "\\":
			print(i,line[i])
			print(i+1,line[i+1])
			if line[i+1] == "\"":
				quotes = quotes+1
				i = i+1
			elif line[i+1] == "\\":
				slash = slash+1
				i = i+1
			elif line[i+1] == "x":
				print(line[i+2])
				print(line[i+3])
				if line[i+2]<= 'f' and line[i+3]<= 'f' :
					hex = hex +1
					i= i +3
				else:
					nonhex = nonhex+1
		i = i+1
	total_char = total_char + length
	char = length-(quotes + (hex*3) + slash)-2 - nonhex
	print("Length : ", length)
	print("Quotes : ", quotes)
	print("Hex : ", hex)
	print("Non Hex : ", nonhex)
	print("slash : ", slash)
	print("Char : ", char)	
	print("=====\n")

	total = total + char
	sum = total_char - total		
print(total)
print("Sum : ", sum)	
