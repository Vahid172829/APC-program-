
# 1.
numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)

    
# 2.
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

numbers_set = set(numbers)

print("List:", numbers)
print("Set:", numbers_set)


# 3.
fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes"}

fruits.add("Pineapple")
fruits.add("Watermelon")

print("Updated set:", fruits)


# 4.
numbers = {10, 20, 30, 40, 50}

number = int(input("Enter number to remove: "))

if number in numbers:
    numbers.remove(number)
    print("Updated set:", numbers)
else:
    print("Number not found.")


# 5.
students = {"Rahul", "Priya", "Amit", "Sneha", "Riya"}

name = input("Enter student name: ")

if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist in the set.")


# 6.
cities = {"Mumbai", "Pune", "Delhi", "Chennai", "Kolkata"}

print("Total number of cities:", len(cities))


# 7.
languages = {"Python", "Java", "C", "C++", "JavaScript"}

for language in languages:
    print(language)


# 8.
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

numbers_set = set(numbers)

print("Original list:", numbers)
print("Set without duplicates:", numbers_set)


# 9.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

union = set1.union(set2)

print("Union:", union)


# 10.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

common = set1.intersection(set2)

print("Common elements:", common)


# 11.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

first_only = set1 - set2
second_only = set2 - set1

print("Elements only in first set:", first_only)
print("Elements only in second set:", second_only)


# 12.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.symmetric_difference(set2)

print("Elements present in either set but not both:", result)


# 13.
set1 = {10, 20}
set2 = {10, 20, 30, 40}

if set1.issubset(set2):
    print("First set is a subset of second set.")
else:
    print("First set is not a subset of second set.")


# 14.
set1 = {10, 20, 30, 40}
set2 = {10, 20}

if set1.issuperset(set2):
    print("First set is a superset of second set.")
else:
    print("First set is not a superset of second set.")


# 15.
set1 = {10, 20, 30}
set2 = {40, 50, 60}

if set1.isdisjoint(set2):
    print("The sets have no elements in common.")
else:
    print("The sets have common elements.")


# 16.
set1 = {10, 20, 30}
set2 = {10, 20, 30}

if set1 == set2:
    print("Both sets are equal.")
else:
    print("Both sets are not equal.")


# 17.
student1_subjects = {"Python", "Java", "Maths", "English"}
student2_subjects = {"Python", "C++", "Maths", "Science"}

common_subjects = student1_subjects.intersection(student2_subjects)

print("Subjects studied by both students:", common_subjects)


# 18.
sentence = input("Enter a sentence: ")

words = set(sentence.split())

print("Unique words:", words)


# 19.
morning_students = {"Rahul", "Priya", "Amit", "Sneha"}
afternoon_students = {"Amit", "Sneha", "Riya", "Karan"}

both_sessions = morning_students.intersection(afternoon_students)
morning_only = morning_students - afternoon_students
afternoon_only = afternoon_students - morning_students
at_least_one = morning_students.union(afternoon_students)

print("Students present in both sessions:", both_sessions)
print("Students present only in morning:", morning_only)
print("Students present only in afternoon:", afternoon_only)
print("Students present in at least one session:", at_least_one)


# 20.
python_students = {"Rahul", "Priya", "Amit", "Sneha", "Riya"}
java_students = {"Amit", "Sneha", "Karan", "Neha", "Rahul"}

print("Python students:", python_students)
print("Java students:", java_students)


# 21.
python_students = {"Rahul", "Priya", "Amit", "Sneha", "Riya"}
java_students = {"Amit", "Sneha", "Karan", "Neha", "Rahul"}

both_courses = python_students.intersection(java_students)
only_one_course = python_students.symmetric_difference(java_students)

print("Students enrolled in both courses:", both_courses)
print("Students enrolled in only one course:", only_one_course)


# 22.
employee1_skills = {"Python", "Java", "SQL", "HTML"}
employee2_skills = {"Python", "C++", "SQL", "JavaScript"}

common_skills = employee1_skills.intersection(employee2_skills)
unique_employee1 = employee1_skills - employee2_skills
unique_employee2 = employee2_skills - employee1_skills
all_skills = employee1_skills.union(employee2_skills)

print("Common skills:", common_skills)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All available skills:", all_skills)


# 23.
available_books = {
    "Python Basics",
    "Java Programming",
    "Data Science",
    "Web Development"
}

requested_books = {
    "Python Basics",
    "Data Science",
    "Machine Learning",
    "Java Programming"
}

available_requested = available_books.intersection(requested_books)

print("Requested books that are available:", available_requested)


# 24.
first_day_visitors = {101, 102, 103, 104, 105}
second_day_visitors = {103, 104, 105, 106, 107}

unique_visitors = first_day_visitors.union(second_day_visitors)
returning_visitors = first_day_visitors.intersection(second_day_visitors)
first_day_only = first_day_visitors - second_day_visitors
second_day_only = second_day_visitors - first_day_visitors

print("Unique visitors across both days:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on first day:", first_day_only)
print("Visitors only on second day:", second_day_only)


# 25.
user1_friends = {"Rahul", "Amit", "Priya", "Sneha", "Karan"}
user2_friends = {"Priya", "Sneha", "Riya", "Neha", "Amit"}

mutual_friends = user1_friends.intersection(user2_friends)
unique_user1 = user1_friends - user2_friends
unique_user2 = user2_friends - user1_friends
total_unique_friends = user1_friends.union(user2_friends)

print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_unique_friends)
```
