n = 12

'''def fib(i):
    if(i!=1):
        arr=fib(i-1)
        newNum=arr[i-2]+arr[i-1]+arr[i]
        arr.append(newNum)
        print(str(newNum))
        return(arr)
    else:
        print("1")
        return[1,0,1]

fib(n)'''

num1=1
num2=0
num3=1
newNum=0
for x in range(n):
	print(num3)
	newNum=num3+num2+num1
	num1=num2
	num2=num3
	num3=newNum