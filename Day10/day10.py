#Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

#To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

#For example:

#turn on 0,0 through 999,999 would turn on (or leave on) every light.
#toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
#turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

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
