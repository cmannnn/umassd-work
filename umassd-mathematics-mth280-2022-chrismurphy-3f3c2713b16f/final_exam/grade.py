# 05/05/2022
# author: Chris Murphy
# MTH 280 final exam

hw = 89
lab = 87
midterm = 90
# final = 0


def compute_grade(hw, lab, midterm):
	final = 0
	while final <= 100:
		grade = hw * .4 + lab * .15 + midterm * .2 + final * .25
		# print('My final grade is: %.2f' % grade)
		print(f'Final exam grade = {final}, My final grade is {grade}')
		final += 1

compute_grade(90, 100, 77)