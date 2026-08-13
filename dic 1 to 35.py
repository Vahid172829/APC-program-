# 1.
student = {
    "Roll Number": 101,
    "Name": "Rahul",
    "Department": "Computer Science",
    "Marks": 85
}

for key, value in student.items():
    print(key, ":", value)


# 2.
employee = {
    "ID": 101,
    "Name": "Amit",
    "Department": "IT",
    "Salary": 50000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found.")


# 3.
products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Pencil": 5,
    "Bottle": 100
}

products["Notebook"] = 80

print("Updated dictionary:", products)


# 4.
marks = {
    "Rahul": 85,
    "Priya": 90,
    "Amit": 78,
    "Sneha": 88
}

name = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))

if name in marks:
    marks[name] = new_marks
    print("Updated dictionary:", marks)
else:
    print("Student not found.")


# 5.
cities = {
    "Mumbai": 20,
    "Pune": 7,
    "Delhi": 19,
    "Chennai": 8
}

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print("Updated dictionary:", cities)
else:
    print("City not found.")


# 6.
employees = {
    101: "Rahul",
    102: "Priya",
    103: "Amit",
    104: "Sneha"
}

employee_id = int(input("Enter employee ID: "))

if employee_id in employees:
    print("Employee exists:", employees[employee_id])
else:
    print("Employee ID does not exist.")


# 7.
students = {
    "Rahul": 85,
    "Priya": 90,
    "Amit": 78,
    "Sneha": 88
}

print("Total number of key-value pairs:", len(students))


# 8.
student = {
    "Name": "Rahul",
    "Age": 20,
    "Department": "Computer Science",
    "Marks": 85
}

print("All keys:")
print(student.keys())

print("All values:")
print(student.values())

print("All key-value pairs:")
print(student.items())


# 9.
languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup"
}

for language, creator in languages.items():
    print(language, ":", creator)


# 10.
students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("Student dictionary:", students)


# 11.
marks = {
    "Rahul": 85,
    "Priya": 95,
    "Amit": 78,
    "Sneha": 88
}

highest_student = ""
highest_marks = -1

for name, mark in marks.items():
    if mark > highest_marks:
        highest_marks = mark
        highest_student = name

print("Student with highest marks:", highest_student)
print("Highest marks:", highest_marks)


# 12.
marks = {
    "Rahul": 85,
    "Priya": 95,
    "Amit": 78,
    "Sneha": 88
}

lowest_student = ""
lowest_marks = 101

for name, mark in marks.items():
    if mark < lowest_marks:
        lowest_marks = mark
        lowest_student = name

print("Student with lowest marks:", lowest_student)
print("Lowest marks:", lowest_marks)


# 13.
marks = {
    "Rahul": 85,
    "Priya": 95,
    "Amit": 78,
    "Sneha": 88
}

total = sum(marks.values())
average = total / len(marks)

print("Average marks:", average)


# 14.
text = input("Enter a string: ")

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print("Character frequency:", frequency)


# 15.
sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)


# 16.
dictionary1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dictionary2 = {
    "D": 40,
    "E": 50,
    "F": 60
}

merged = dictionary1.copy()
merged.update(dictionary2)

print("Merged dictionary:", merged)


# 17.
dictionary1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dictionary2 = {
    "B": 40,
    "C": 50,
    "D": 60
}

common_keys = dictionary1.keys() & dictionary2.keys()

print("Common keys:", common_keys)


# 18.
dictionary1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dictionary2 = {
    "D": 20,
    "E": 30,
    "F": 40
}

common_values = set(dictionary1.values()) & set(dictionary2.values())

print("Common values:", common_values)


# 19.
dictionary = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

new_dictionary = {}

for key, value in dictionary.items():
    if value not in new_dictionary.values():
        new_dictionary[key] = value

print("Original dictionary:", dictionary)
print("Dictionary without duplicate values:", new_dictionary)


# 20.
dictionary = {
    5: "E",
    2: "B",
    4: "D",
    1: "A",
    3: "C"
}

sorted_dictionary = dict(sorted(dictionary.items()))

print("Dictionary in ascending order of keys:", sorted_dictionary)


# 21.
squares = {}

for number in range(1, 11):
    squares[number] = number ** 2

print("Squares:", squares)


# 22.
squares = {}

for number in range(1, 21):
    if number % 2 == 0:
        squares[number] = number ** 2

print("Squares of even numbers:", squares)


# 23.
numbers = [10, 20, 10, 30, 20, 10, 40, 30, 50]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("Number frequency:", frequency)


# 24.
cubes = {}

for number in range(1, 11):
    cubes[number] = number ** 3

print("Cubes:", cubes)


# 25.
students = {
    "Rahul": 85,
    "Priya": 90,
    "Amit": 78,
    "Sneha": 88
}

while True:
    print("\n1. Add a student")
    print("2. Update marks")
    print("3. Delete a student")
    print("4. Search for a student")
    print("5. Display all students")
    print("6. Find highest marks")
    print("7. Calculate average")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added.")

    elif choice == 2:
        name = input("Enter student name: ")

        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated.")
        else:
            print("Student not found.")

    elif choice == 3:
        name = input("Enter student name: ")

        if name in students:
            del students[name]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == 4:
        name = input("Enter student name: ")

        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found.")

    elif choice == 5:
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == 6:
        highest = max(students.values())
        print("Highest marks:", highest)

    elif choice == 7:
        average = sum(students.values()) / len(students)
        print("Average marks:", average)

    elif choice == 8:
        break

    else:
        print("Invalid choice.")


# 26.
employees = {
    "Rahul": 45000,
    "Priya": 65000,
    "Amit": 55000,
    "Sneha": 48000,
    "Riya": 75000
}

highest_salary = max(employees.values())
lowest_salary = min(employees.values())
average_salary = sum(employees.values()) / len(employees)

print("Highest salary:", highest_salary)
print("Lowest salary:", lowest_salary)
print("Average salary:", average_salary)

print("Employees earning more than ₹50,000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)


# 27.
products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15,
    "Pencil": 8
}

while True:
    print("\n1. Add a product")
    print("2. Update quantity")
    print("3. Delete a product")
    print("4. Search for a product")
    print("5. Display products with quantity below 10")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        products[product] = quantity
        print("Product added.")

    elif choice == 2:
        product = input("Enter product name: ")

        if product in products:
            quantity = int(input("Enter new quantity: "))
            products[product] = quantity
            print("Quantity updated.")
        else:
            print("Product not found.")

    elif choice == 3:
        product = input("Enter product name: ")

        if product in products:
            del products[product]
            print("Product deleted.")
        else:
            print("Product not found.")

    elif choice == 4:
        product = input("Enter product name: ")

        if product in products:
            print("Quantity:", products[product])
        else:
            print("Product not found.")

    elif choice == 5:
        print("Products with quantity below 10:")

        for product, quantity in products.items():
            if quantity < 10:
                print(product, ":", quantity)

    elif choice == 6:
        break

    else:
        print("Invalid choice.")


# 28.
contacts = {
    "Rahul": "9876543210",
    "Priya": "9876543211",
    "Amit": "9876543212"
}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display all contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == 2:
        name = input("Enter name: ")

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter name: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == 5:
        print("All contacts:")

        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 6:
        break

    else:
        print("Invalid choice.")


# 29.
books = {
    101: "Python Basics",
    102: "Java Programming",
    103: "Data Science"
}

while True:
    print("\n1. Add a book")
    print("2. Search a book")
    print("3. Remove a book")
    print("4. Display all books")
    print("5. Count total books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        book_name = input("Enter book name: ")
        books[book_id] = book_name
        print("Book added.")

    elif choice == 2:
        book_id = int(input("Enter book ID: "))

        if book_id in books:
            print("Book name:", books[book_id])
        else:
            print("Book not found.")

    elif choice == 3:
        book_id = int(input("Enter book ID: "))

        if book_id in books:
            del books[book_id]
            print("Book removed.")
        else:
            print("Book not found.")

    elif choice == 4:
        print("All books:")

        for book_id, book_name in books.items():
            print(book_id, ":", book_name)

    elif choice == 5:
        print("Total books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid choice.")


# 30.
students = {
    "Rahul": "Computer Science",
    "Priya": "Information Technology",
    "Amit": "Computer Science",
    "Sneha": "Electronics",
    "Riya": "Information Technology"
}

departments = {}

for name, department in students.items():
    if department not in departments:
        departments[department] = []

    departments[department].append(name)

print("Students grouped by department:")

for department, names in departments.items():
    print(department, ":", names)


# 31.
words = ["cat", "dog", "apple", "bat", "banana", "car", "orange"]

word_lengths = {}

for word in words:
    length = len(word)

    if length not in word_lengths:
        word_lengths[length] = []

    word_lengths[length].append(word)

print("Words grouped by length:")

for length, word_list in word_lengths.items():
    print(length, ":", word_list)


# 32.
numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = {}
found = False

for number in numbers:
    complement = target - number

    if complement in seen:
        print("Two numbers:", complement, "and", number)
        print("Their sum:", target)
        found = True
        break

    seen[number] = True

if not found:
    print("No two numbers found.")


# 33.
text = input("Enter a string: ")

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

found = False

for character in text:
    if frequency[character] == 1:
        print("First non-repeating character:", character)
        found = True
        break

if not found:
    print("No unique character found.")


# 34.
text = input("Enter a string: ")

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

found = False

for character in text:
    if frequency[character] > 1:
        print("First repeating character:", character)
        found = True
        break

if not found:
    print("No repeating character found.")


# 35.
paragraph = input("Enter a paragraph: ")

words = paragraph.split()

word_length_count = {}

for word in words:
    length = len(word)

    if length in word_length_count:
        word_length_count[length] += 1
    else:
        word_length_count[length] = 1

print("Word length and number of words:")

for length, count in sorted(word_length_count.items()):
    print("Length", length, ":", count, "word(s)")
