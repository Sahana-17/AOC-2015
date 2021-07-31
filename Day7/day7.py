import sys

value = []
for line in sys.stdin:
	res = line.split()
	print(res)
	if '->' in res:
		#num = ord(res[2])
		res[2] = res[0]
		print(res[2])
	if 'AND' in res:
		var1 = res[0]
		print(var1)
		res[4] = res[0]&[2]	
		print(res[4])	
