## TODO: complete the function "lowest_terms" below
from fractions import Fraction
def lowest_terms(x):
	y = Fraction(x)
	return str(y.numerator)+"/"+str(y.denominator)

	#x = x.split("/")
	#y= (Fraction(int(x[0]),int(x[1])))
	#print (lowest_terms("7/49"))

#
#x= input("enter Number: ")
#y=Fraction(x)
#y = y.split("/")
#print(y)
