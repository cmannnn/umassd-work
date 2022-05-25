# inputs:
# -3
# -2.5
# -2.0

# outputs:
# 999.5
# 1000.0
# Done

inputs = (-3, -2.5, -2.0)
output = 999.5

while output <= 1000:
	print(output)
	output = output + 0.5
print('Done!')