string = input("Enter a string: ")
max_char = string[0]
max_count = string.count(string[0])
for ch in string:
    if string.count(ch) > max_count:
        max_count = string.count(ch)
        max_char = ch
print("Most Frequent Character:", max_char)
print("Frequency:", max_count)