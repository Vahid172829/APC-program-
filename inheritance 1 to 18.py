# 1. Employee and Manager

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def annual_salary(self):
        return self.salary * 12

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("Annual Salary:", self.annual_salary())


manager = Manager(101, "Yash", 50000, "IT")
manager.display_manager()


# 2. Vehicle and Car

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display_car(self):
        self.display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Discounted Price:", self.discounted_price(10))


car = Car("Toyota", "Fortuner", "Petrol", 3000000)
car.display_car()


# 3. Academic, Sports and Student
# Multiple Inheritance

class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)

    def overall_performance(self):
        return self.marks + self.sports_points

    def display(self):
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.sports_points)
        print("Overall Performance:", self.overall_performance())


student = Student(85, 10)
student.display()


# 4. PersonalDetails, ProfessionalDetails and Employee
# Multiple Inheritance

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(
            self, emp_id, designation, salary
        )

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


employee = Employee("Yash", 22, 101, "Developer", 50000)
employee.display()


# 5. Person, Student and ResearchStudent
# Multilevel Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


research_student = ResearchStudent(
    "Yash", 22, 101, "MCA",
    "Artificial Intelligence", "Dr. Sharma"
)

research_student.display()


# 6. BankAccount, SavingsAccount and PremiumSavingsAccount
# Multilevel Inheritance

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate)
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


premium = PremiumSavingsAccount(
    "AC101", 100000, 7, "Free Insurance"
)

premium.display()


# 7. Shape, Circle, Rectangle and Triangle
# Hierarchical Inheritance

class Shape:
    def display_name(self):
        print("Shape:", self.__class__.__name__)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(7)
rectangle = Rectangle(10, 5)
triangle = Triangle(10, 8)

circle.display_name()
print("Area:", circle.area())

rectangle.display_name()
print("Area:", rectangle.area())

triangle.display_name()
print("Area:", triangle.area())


# 8. Employee, Manager, Developer and Tester
# Hierarchical Inheritance

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.30

    def display(self):
        print("Manager:", self.name)
        print("Salary:", self.salary())


class Developer(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.20

    def display(self):
        print("Developer:", self.name)
        print("Salary:", self.salary())


class Tester(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.15

    def display(self):
        print("Tester:", self.name)
        print("Salary:", self.salary())


manager = Manager(101, "Rahul", 50000)
developer = Developer(102, "Amit", 40000)
tester = Tester(103, "Priya", 35000)

manager.display()
developer.display()
tester.display()


# 9. Person, Student, Faculty and TeachingAssistant
# Multiple + Hierarchical Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no


class Faculty(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, subject):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)


ta = TeachingAssistant("Yash", 22, 101, "Python")
ta.display()


# 10. Vehicle, Car, Bike, SportsCar and ElectricBike
# Combination of Inheritance

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors


class Bike(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine


class SportsCar(Car):
    def __init__(self, brand, model, doors, speed):
        super().__init__(brand, model, doors)
        self.speed = speed

    def display(self):
        super().display()
        print("Doors:", self.doors)
        print("Top Speed:", self.speed)


class ElectricBike(Bike):
    def __init__(self, brand, model, engine, battery):
        super().__init__(brand, model, engine)
        self.battery = battery

    def display(self):
        super().display()
        print("Engine:", self.engine)
        print("Battery:", self.battery)


sports_car = SportsCar("Ferrari", "F8", 2, "340 km/h")
electric_bike = ElectricBike("Ola", "S1", "Electric", "4 kWh")

sports_car.display()
electric_bike.display()


# 11. Student and Result
# Single Inheritance

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 3

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "F"

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())


result = Result(101, "Yash", "MCA", [85, 90, 88])
result.display()


# 12. Product and ElectronicProduct

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Final Price:", self.final_price(10))


electronic = ElectronicProduct(
    101, "Laptop", 60000, "Dell", "2 Years"
)

electronic.display()


# 13. Printer, Scanner and MultifunctionDevice
# Multiple Inheritance

class Printer:
    def print_document(self):
        print("Printing document")


class Scanner:
    def scan_document(self):
        print("Scanning document")


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        print("Multifunction Device")


device = MultifunctionDevice()

device.display()
device.print_document()
device.scan_document()


# 14. Camera, Phone and Smartphone
# Multiple Inheritance

class Camera:
    def take_photo(self):
        print("Taking photograph")


class Phone:
    def make_call(self):
        print("Making phone call")


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone")


smartphone = Smartphone()

smartphone.display()
smartphone.take_photo()
smartphone.make_call()


# 15. Animal, Dog, Cat and Cow
# Hierarchical Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal Name:", self.name)


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")


dog = Dog("Tommy")
cat = Cat("Kitty")
cow = Cow("Ganga")

dog.display()
dog.sound()

cat.display()
cat.sound()

cow.display()
cow.sound()


# 16. Person, Doctor, Patient, Surgeon and MedicalResearcher
# Multiple + Hierarchical Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease


class Surgeon(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Person.__init__(self, name, age)
        self.specialization = specialization
        self.disease = disease

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)


class MedicalResearcher(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Person.__init__(self, name, age)
        self.specialization = specialization
        self.disease = disease

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)


surgeon = Surgeon(
    "Dr. Rahul", 40, "General Surgery", "Appendicitis"
)

researcher = MedicalResearcher(
    "Dr. Priya", 38, "Medical Research", "Cancer"
)

surgeon.display()
researcher.display()




