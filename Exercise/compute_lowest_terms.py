## TODO: complete the function "lowest_terms" below
##rfraction function
def rfraction(numerator, denominator):
	""""Returns the lowest term of numerator and denominator of fraction.

    numerator (int) - numerator in integer
    denominator(int)  - denominator  in integer
    """
	sign = +1											#created ro determine the sign of the fraction at the end
	if (denominator < 0):
		denominator = abs(denominator)
		sign = -1
	for i in range(2, denominator+1):
	    if (numerator % i == 0) and (denominator % i == 0):
	        x =  int(numerator / i)
	        y = int(denominator / i)
	return (sign * x), y

## created Lowest term Function
##this fuction will call the rfraction function
def lowest_terms(x):
	""""Returns the lowest term of a fraction.
		x (string) - x is a string
		it returns a string value
    """
	if x.split("/")[1] == "0":						#exception for ZeroDivisioError
		y= "Undefined"
		return y
	elif x.split("/")[0] == "0":					#fixing asserion Errror due to 0 numerator
		y = x.split("/")[0]
		return y
	else:
		num = int(x.split("/")[0])
		den = int(x.split("/")[1])
		y = rfraction(num,den)						#rfraction call
		return str(y[0])+"/"+str(y[1])
