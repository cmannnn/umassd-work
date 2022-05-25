# 03/14/2022
# author: Chris Murphy
# MTH 322 280 midterm exam practice

# You have one penny deposited in a very special bank. 
# Every 24 hours this bank doubles your money!
# Write a program which prints the amount of money you have in dollars 
# on each day until your money has
# exceeded 10 million dollars

loops = 0
total = .01
while total < 10000000:
	print(f'{loops}, {total}')
	loops = loops + 1
	total = total * 2
	
	
	