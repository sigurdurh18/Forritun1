def make_new_row(listinn,ls):
	if(ls):
		kek=[listinn.pop().upper()]
		if len(kek)>0:
			for x in range(len(ls)-1):
				kek.append(ls[x]+ls[x+1])
		kek.append(listinn.pop().upper())
		return kek
	else:
		return ['!']
def eu(txt):
    newStr=""
    car=txt[0]
    count=0
    for c in txt:
        if(c==car):
            count+=1
        else:
            newStr += '|'
            if count>1:
                newStr += str(count) + car.upper()
            else:
                newStr += car
            car=c
            count=1
            newStr += '|'
    newStr+=car
    return newStr


# Main program starts here - DO NOT CHANGE
height = int(12)
new_row = []
listinn= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
listinn.reverse()
for i in range(height):
    new_row = make_new_row(listinn,new_row)
    for x in new_row:
        print(eu(sorted(x)),end=" ")
    print()
    for x in new_row:
        print(len(x),end=" ")
    print()