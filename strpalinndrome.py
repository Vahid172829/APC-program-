string=input("enter the string:")
reverse=""
for ch in string:
    reverse=ch+reverse
if string==reverse:
    print("Is Palindrome")
else:
    print("Not Palindrome")        