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
