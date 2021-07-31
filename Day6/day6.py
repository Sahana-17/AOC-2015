#Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

#To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

#For example:

#turn on 0,0 through 999,999 would turn on (or leave on) every light.
#toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
#turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

import sys
import re

lit = 0
bright = 0

lights = [[0 for i in range(1000)] for j in range(1000)]
brightness = [[0 for i in range(1000)] for j in range(1000)]

for line in sys.stdin:
	
	temp = re.findall(r'\d+', line)
	res = list(map(int, temp))
		
	num1 = res[0]
	num2 = res[1]
	num3 = res[2] 
	num4 = res[3] 

	if line[0:7] == "turn on":
	
		for i in range(num1, num3+1):
			for j in range(num2, num4+1):
				lights[i][j] = 1
				brightness[i][j] = brightness[i][j] + 1
	elif line[0:7] == "toggle ":
		for i in range(num1, num3+1):
			for j in range(num2, num4+1):
				brightness[i][j] = brightness[i][j] + 2
				if lights[i][j] == 1:
					lights[i][j] = 0
					
				else:
					lights[i][j] = 1
	else:
		for i in range(num1, num3+1):
			for j in range(num2, num4+1):
				lights[i][j] = 0
				if brightness[i][j] > 0:
					brightness[i][j] = brightness[i][j] - 1
				
for x in range(1000):
	for y in range(1000):
		bright = bright + brightness[x][y]	
		if lights[x][y] == 1:
			lit = lit + 1
print("Lit = ", lit)
print("Brightness = ", bright)	
