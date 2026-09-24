class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage(), "%")
        print()


students = [
    Student(1, "Rahul", [85, 90, 78, 88, 92]),
    Student(2, "Priya", [90, 87, 95, 91, 89]),
    Student(3, "Amit", [75, 80, 72, 85, 79])
]

for student in students:
    student.display()
