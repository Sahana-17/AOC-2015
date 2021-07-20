#Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

#For example:

#A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.

#All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

file = open("/users/sahana/AOC-2015/Day2/day2.in", "r")
count = 0
wrapping = 0
total =0
ribbonlength = 0
ribbon = 0
while True:
	count = count +1
	wrapping = wrapping + total
	ribbon = ribbon + ribbonlength

	line = file.readline()
	if not line:
		break
	import re
	temp = re.findall(r'\d+', line)
	res = list(map(int, temp))
	res.sort()
	num1 = res[0]
	num2 = res[1]
	num3 = res[2]
	
	area1 = num1*num2
	area2 = num2*num3
	area3 = num1*num3
	
	surface_area = (2*(area1+area2+area3))
	cubic = (num1*num2*num3)	
	slack = area1
	smallest_perimeter = (2*(num1+num2))
	total = surface_area + slack
	ribbonlength = cubic + smallest_perimeter
file.close()

print("TOTAL WRAPPING : ", wrapping)
print("TOTAL RIBBON : ", ribbon)
