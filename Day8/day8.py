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
