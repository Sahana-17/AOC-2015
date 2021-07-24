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
