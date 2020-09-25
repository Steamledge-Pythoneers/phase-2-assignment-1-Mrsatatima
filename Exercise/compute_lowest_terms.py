## TODO: complete the function "lowest_terms" below
##rfraction function
def rfraction(num, den):
	""""Returns the lowest term of numerator and denominator of fraction.

    num (int) - numerator in integer
    dem(int)  - denominator  in integer
    """
	y = den
	x = num
	for i in range(2, den+1):
		if (num % i == 0) and (den % i == 0):
			x = num // i
			y = den // i
	return x, y
## created Lowest term Function
def lowest_terms(x):
	""""Returns the lowest term of a fraction.
		x (string) - x is a string
		it returns a string value
    """
	num = int(x.split("/")[0])
	den = int(x.split("/")[1])
	y = rfraction(num,den)						#rfraction call
	return str(y[0])+"/"+str(y[1])
		#except(ValueError):
		#	a = int(x.split("/")[0])
		#	b =int(x.split("/")[1])
		#	y= Fraction(a, b)
		#	return str(y.numerator)+"/"+str(y.denominator)
		#	if y.numerator == 0:
		#		return "0"
		#except ZeroDivisionError:
			#y= "Undefined"
			#return y
