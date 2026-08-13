# 1.
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)


# 2.
cities = ("Mumbai", "Pune", "Delhi", "Chennai", "Kolkata")
print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])


# 3.
students = ("Rahul", "Amit", "Priya", "Sneha", "Riya")
print("Total number of students:", len(students))


# 4.
colors = ("Red", "Blue", "Green", "Yellow", "Black")
color = input("Enter a color: ")

if color in colors:
    print("Color exists in the tuple.")
else:
    print("Color does not exist in the tuple.")


# 5.
fruits = ("Apple", "Mango", "Banana", "Orange", "Grapes")

for fruit in fruits:
    print(fruit)


# 6.
numbers = (10, 20, 10, 30, 10, 40, 20, 10)
number = int(input("Enter a number: "))
print("Number of times it appears:", numbers.count(number))


# 7.
employee_ids = (101, 102, 103, 104, 105)
emp_id = int(input("Enter employee ID: "))

if emp_id in employee_ids:
    print("Index:", employee_ids.index(emp_id))
else:
    print("Employee ID not found.")


# 8.
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
result = tuple1 + tuple2

print("First tuple:", tuple1)
print("Second tuple:", tuple2)
print("Concatenated tuple:", result)


# 9.
numbers = (1, 2, 3)
result = numbers * 4

print("Original tuple:", numbers)
print("Repeated tuple:", result)


# 10.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Tuple:", numbers)
print("First five elements:", numbers[:5])
print("Last five elements:", numbers[5:])
print("Middle four elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])


# 11.
numbers = (10, 20, 30, 40)

print("Original tuple:", numbers)

my_list = list(numbers)
my_list.append(50)

print("List after adding new element:", my_list)


# 12.
numbers = []

for i in range(5):
    number = int(input("Enter number: "))
    numbers.append(number)

numbers_tuple = tuple(numbers)

print("List:", numbers)
print("Tuple:", numbers_tuple)


# 13.
numbers = (10, 20, 30, 40)

print("Original tuple:", numbers)

my_list = list(numbers)
my_list[1] = 200
my_list.append(50)

numbers = tuple(my_list)

print("Modified tuple:", numbers)


# 14.
numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)

del numbers

print("Tuple deleted successfully.")


# 15.
students = (
    (101, "Rahul", "Computer Science", 85),
    (102, "Priya", "Information Technology", 90),
    (103, "Amit", "Computer Science", 78)
)

for student in students:
    print("Roll Number:", student[0])
    print("Name:", student[1])
    print("Department:", student[2])
    print("Marks:", student[3])
    print()


# 16.
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
total = sum(numbers)

print("Tuple:", numbers)
print("Sum:", total)


# 17.
numbers = (25, 10, 45, 5, 30, 60, 15)

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Tuple:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)


# 18.
numbers = (10, 20, 30, 40, 50)

total = sum(numbers)
average = total / len(numbers)

print("Tuple:", numbers)
print("Average:", average)


# 19.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Tuple:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)


# 20.
numbers = (10, 20, 30, 40, 50)

number = int(input("Enter a number: "))

if number in numbers:
    print("Number exists in the tuple.")
else:
    print("Number does not exist in the tuple.")


# 21.
student = (101, "Rahul", "Computer Science", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])


# 22.
employees = (
    (101, "Rahul", 30000),
    (102, "Priya", 35000),
    (103, "Amit", 40000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()


# 23.
prices = (100, 250, 150, 300, 200)

total = sum(prices)
average = total / len(prices)

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price

    if price < lowest:
        lowest = price

print("Item prices:", prices)
print("Total bill:", total)
print("Average price:", average)
print("Highest-priced item:", highest)
print("Lowest-priced item:", lowest)


# 24.
temperatures = (32, 35, 31, 30, 36, 34, 33)

maximum = temperatures[0]
minimum = temperatures[0]

for temperature in temperatures:
    if temperature > maximum:
        maximum = temperature

    if temperature < minimum:
        minimum = temperature

average = sum(temperatures) / len(temperatures)

print("Temperatures:", temperatures)
print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)


# 25.
runs = (45, 78, 32, 90, 56, 67, 100, 34, 88, 76)

total = sum(runs)
average = total / len(runs)

highest = runs[0]
lowest = runs[0]

for run in runs:
    if run > highest:
        highest = run

    if run < lowest:
        lowest = run

print("Runs:", runs)
print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)


# 26.
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = ()

for number in tuple1:
    if number in tuple2:
        common = common + (number,)

print("First tuple:", tuple1)
print("Second tuple:", tuple2)
print("Common elements:", common)


# 27.
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple1 + tuple2
result = ()

for number in merged:
    if number not in result:
        result = result + (number,)

print("First tuple:", tuple1)
print("Second tuple:", tuple2)
print("Merged tuple:", result)


# 28.
numbers = (10, 20, 10, 30, 20, 10, 40, 30)

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("Tuple:", numbers)
print("Frequency of each element:")

for number, count in frequency.items():
    print(number, "appears", count, "time(s)")


# 29.
numbers = (50, 20, 40, 10, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Original tuple:", numbers)
print("Ascending order:", ascending)
print("Descending order:", descending)


# 30.
patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Priya", 30, "B+"),
    (103, "Amit", 28, "O+"),
    (104, "Sneha", 35, "A+"),
    (105, "Riya", 22, "O+")
)

print("All Patient Records:")

for patient in patients:
    print("Patient ID:", patient[0])
    print("Name:", patient[1])
    print("Age:", patient[2])
    print("Blood Group:", patient[3])
    print()

search_id = int(input("Enter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == search_id:
        print("\nPatient Found:")
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True
        break

if not found:
    print("Patient not found.")


print("\nTotal number of patients:", len(patients))


blood_group = input("\nEnter blood group to search: ")

print("\nPatients with blood group", blood_group + ":")

found = False

for patient in patients:
    if patient[3].upper() == blood_group.upper():
        print(
            "ID:", patient[0],
            "| Name:", patient[1],
            "| Age:", patient[2],
            "| Blood Group:", patient[3]
        )
        found = True

if not found:
    print("No patients found with this blood group.")
