#Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

#An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

#For example:

#(()) and ()() both result in floor 0.
#((( and (()(()( both result in floor 3.

order = input("Enter directions using parenthesis : ")

floor = 0
length = len(order)

for i in range(length):
    char = order[i]

    if floor == -1:
        print("Basement : ", i)
    if char == '(':
        floor = floor + 1
    elif char == ')':
        floor = floor -1

print("Floor Number : ", floor)
