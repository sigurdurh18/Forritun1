#dept=float(input("Input the cost of the item in $: "))
dept=500
Month=0
Interest=0.015
vxt=0
vxtTotal=0
while dept>0:
	Month+=1
	vxt=Interest*dept
	dept+=vxt
	vxtTotal+=vxt
	if(dept>50):
		dept-=50
		print("Month:",Month,"Payment: 50.0 Interest paid:",round(vxt*100)/100,"Remaining debt:",round(dept*100)/100)
	else:
		print("Month:",Month,"Payment:",round(dept*100)/100,"Interest paid:",round(vxt*100)/100,"Remaining debt: 0.0",end="\n\n")
		dept=0

print("Number of months:",Month)
print("Total interest paid:",round(vxtTotal*100)/100)

def f(numb):
	return round(numb*100)/100