sentence=input("Enter a sentence: ")
UpperCase = 0
LowerCase = 0
Digits = 0
Punctuation = 0
for letter in sentence:
	if letter.isdigit():
		Digits+=1		
	else:
		if(letter!=" "):
			if letter.upper()==letter.lower():
				Punctuation+=1
			elif letter.lower()==letter:
				LowerCase+=1
			elif letter.upper()==letter:
				UpperCase+=1

print(" "*(15-len("Upper case"))+"Upper case"+" "*(6-len(str(UpperCase)))+str(UpperCase))
print(" "*(15-len("Lower case"))+"Lower case"+" "*(6-len(str(LowerCase)))+str(LowerCase))
print(" "*(15-len("Digits"))+"Digits"+" "*(5-len(str(Digits)))+str(Digits))
print(" "*(15-len("Punctuation"))+"Punctuation"+" "*(6-len(str(Punctuation)))+str(Punctuation))