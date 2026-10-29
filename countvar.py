string=input("Enter your String:")
vowels=0
consonants=0
digits=0
space=0
special=0
for ch in string:
    if ch in "AEIOUaeiou":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        space+=1
    else:
        special+=1                

print("vowels:",vowels)  
print("Consonants:",consonants) 
print("Digits:",digits) 
print("Spaces:",space) 
print("Special:",special) 
      
      
      
      
      