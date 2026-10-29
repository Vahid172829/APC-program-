string=input("Enter string:")
old=input("Enter character to replace:")
new=input("Enter new character:")
result=""

for ch in string:
    if ch==old:
        result+=new
    else:
        result+=ch
print("Modified string:",result)        