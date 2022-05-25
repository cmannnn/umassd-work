# 03/13/2022
# author: Chris Murphy
# MTH 322 280 midterm exam practice

# Write a program to find which elements of a list are booleans. For each such element found your program should
# print “Im a bool” and the element’s index. Your program should work for any list, and should be structured as

myList = [1, True, 3.2, False, 34, True, True, 2.2]
is_bool = []
for idx, val in enumerate(myList):
	if type(val) == bool:
		print(f'I\'m a bool, element index {idx}')
