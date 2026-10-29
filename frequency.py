string = input("Enter a string: ")
ch = input("Enter character to search: ")
count = 0
for i in string:
    if i == ch:
        count += 1
print("Frequency:", count)