# 03/14/2022
# author: Chris Murphy
# MTH 322 280 midterm exam practice

# Consider the Pythagorean theorem

# Part 1: There is only one combination of positive integers 0 < a < b < c that satisfy the Pythagorean theorem
# and such that a + b + c = 2000. Write a program to find the values of a, b, and c.

import math as m

def pythagore_triplets(n = 1000):
   maxn = int(n* (2 ** 0.5)) + 1 # max int whose square may be the sum of two squares
   squares = [x * x for x in range(maxn + 1)] # calculate all the squares once
   reverse_squares = dict([(squares[i], i) for i in range(maxn + 1)]) # x*x=>x
   for x in range(1, n):
     x2 = squares[x]
     for y in range(x, n + 1):
       y2 = squares[y]
       z = reverse_squares.get(x2 + y2)
       if z != None:
         yield x,y,z

pythagorean_list = list(pythagore_triplets(1000))

# for t in pythagorean_list:
# 	if sum(t) == 2000:
# 		print(t)

# Part 2: How many combinations of positive integers 0 < a < b < c are there such that a + b + c ≤ 2000 and a,
# b and c satisfy the Pythagorean theorem?
from collections import Counter

lt = []
for q in pythagorean_list:
	if sum(q) <= 2000:
		lt.append(q)

another = []
for th in lt:
	counter = 0
	th_len = len(th)
	th_len = th_len / 3
	another.append(th_len)
print(len(another))
# length = len(count)

# print(length)
