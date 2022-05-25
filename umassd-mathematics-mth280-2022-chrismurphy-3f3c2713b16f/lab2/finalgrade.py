# this program will compute my final MTH-280 grade
# by: Chris Murphy
# date: 02/01/2022

# homework = .4
# labs = .15
# mid_term = .2
# final_exam = .25

def compute_grade(hw, lab, exam1, exam2):
	grade = hw * .4 + lab * .15 + exam1 * .2 + exam2 * .25
	print('My final grade is: %.2f' % grade)

compute_grade(90, 100, 77, 91)
