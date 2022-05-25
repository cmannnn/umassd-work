from integrate import riemann_sum # import from your module
def test_integrand(x):
	""" function to integrate"""
	return 3.0 * x**2

# integrand = test_integrand, xleft = 0.0, xright = 1.0, rectangles = 100
riemann_sum(test_integrand, 0.0, 1.0, 1000)