key=input()
pos=1
while key == 'r' or key == 'q':
	if(key=='r' and pos<10):
		pos+=1
	elif(key=='q' and pos>1):
		pos-1

	print(pos)
	key=input()