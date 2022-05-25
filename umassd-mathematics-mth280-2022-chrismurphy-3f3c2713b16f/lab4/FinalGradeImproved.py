# this program will compute my final MTH-280 grade
# by: Chris Murphy
# date: 02/01/2022

# homework = .4
# labs = .15
# mid_term = .2
# final_exam = .25

hw = [90.0, 97.0, 83.0]
lab   = [100.0, 100.0, 90.0, 80.0]
exam1 = 77.0
exam2 = 91.0

#print(round(sum(hw) / len(hw)))
grade = round(0.4 * (sum(hw) / len(hw)) + (0.15 * sum(lab) / len(hw)) + 0.2 * exam1 + 0.25 * exam2)

if grade <= 100 and grade >= 93:
 	letter_grade = 'A'
elif grade <= 92 and grade >= 90:
 	letter_grade = 'A-' 
elif grade <= 89 and grade >= 87:
 	letter_grade = 'B+'
elif grade <= 86 and grade >= 83 :
 	letter_grade = 'B'
elif grade <= 83 and grade >= 60:
	letter_grade = 'less than a B'
else:
 	letter_grade = 'failing'

print('My final (rounded) grade is: ' + str(grade))
print('Or a(n): ' + letter_grade)
