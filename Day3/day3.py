#Santa is delivering presents to an infinite two-dimensional grid of houses.

#He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

#However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

#For example:

#> delivers presents to 2 houses: one at the starting location, and one to the east.
#^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
#^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

import os

file = open(os.path.join(os.path.dirname('__file__'),"day3.in"))
entire_file = file.read()
v = 0
h = 0
house = 1
v1 = 0
h1 = 0
house1 = 0

numlist = []
numlist.append([0,0])

length = len(entire_file)

for i in range(0,length-1,2):

	char = entire_file[i]
	if char == '^':
		h = h + 1
	elif char == 'v':
		h = h - 1
	elif char == '<':
		v = v + 1
	elif char == '>':
		v = v - 1
	
	house = house + 1
	
	if [h,v] in numlist:
		house = house -1
	else:
		numlist.append([h,v])

for j in range(1,length-1,2):

    char1 = entire_file[j]
    if char1 == '^':
        h1 = h1 + 1
    elif char1 == 'v':
        h1 = h1 - 1
    elif char1 == '<':
        v1 = v1 + 1
    elif char1 == '>':
        v1 = v1 - 1

    house1 = house1 + 1

    if [h1,v1] in numlist:
        house1 = house1 -1
    else:
        numlist.append([h1,v1])

total = house + house1   
print("Num : ", total)

file.close()
