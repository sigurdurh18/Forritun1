def mass_int_check(txt,err,exp):
	while True:
		try:
			listi = input(txt).split(" ")
			new=[]
			for i in listi:
				new.append(int(i))
			if len(listi)==exp:
				return new
			else:
				raise error
		except Exception as e:# e is the error variable
			print(err)


while True:#do while loop100
	shares=mass_int_check("Enter number of shares: ","Invalid number!",1)[0]
	c,a,b=mass_int_check("Enter price (dollars, numerator, denominator): ", "Invalid price!",3)
	print(shares,"shares with market price",c,"{0}/{1} have value ${2:.2f}".format(a,b,shares*(c+a/b)))
	if input("Continue: ")=='n':
		break

