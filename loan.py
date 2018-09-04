sentence=input("Input the cost of the item in $: ")
UpperCase = 0
LowerCase = 0
Digits = 0
Punctuation = 0
for letter in sentence:
	if letter.isdigit():
		Digits+=1
	elif letter is Punctuation:
		Punctuation+=1
	else:
		if letter.istitle:
			UpperCase+=1
		else:
			LowerCase+=1