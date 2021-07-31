#Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

#To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

#For example:

#If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.

import hashlib
flag = False
input = "bgvyzdsv"

i = 0
while flag == False:

	string = str(i)
	value = (input+string)

	x = hashlib.md5((value).encode("utf-8"))
	hash = x.hexdigest()


	zero_char = (hash[:6])
	
	if zero_char == "000000":
		flag = True
		print(i)
	else:
		flag = False
	i = i + 1
