message = input("Enter message: ")
shift = int(input("Enter shift value: "))
result = ""
for ch in message:
    if ch.isalpha():
        if ch.isupper():
            result += chr((ord(ch)-65+shift)%26+65)
        else:
            result += chr((ord(ch)-97+shift)%26+97)
    else:
        result += ch
print("Encrypted Message:", result)