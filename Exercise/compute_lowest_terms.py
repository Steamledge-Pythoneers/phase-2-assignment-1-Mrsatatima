## TODO: complete the function "lowest_terms" below
from fractions import Fraction
def lowest_terms(x):
	if x[0] == "0":
		return x[0]
	else:
		try:
			y = Fraction(x)
			return str(y.numerator)+"/"+str(y.denominator)
		except(ValueError):
			a = int(x.split("/")[0])
			b =int(x.split("/")[1])
			y= Fraction(a, b)
			return str(y.numerator)+"/"+str(y.denominator)
			if y.numerator == 0:
				return "0"
		except ZeroDivisionError:
			y= "Undefined"
			return y
