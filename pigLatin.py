inputName=input("Enter a word: ")
tel = 0
while inputName !='.':
	tel=0
	for c in inputName.lower():
		if not (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
			tel+=1
		else:
			break

	if tel==0:
		inputName+='yay'
	elif tel==len(inputName):
		pass
	else:
		inputName=inputName[tel:]+inputName[:tel]+'ay'
		
	print(inputName)
	inputName=input("Enter a word: ")