class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        units = self.units

        if units <= 100:
            bill = units * 1.50
        elif units <= 200:
            bill = (100 * 1.50) + ((units - 100) * 2.50)
        elif units <= 500:
            bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
        else:
            bill = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.00)

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill: ₹", self.calculate_bill())


bill = ElectricityBill(1001, "Amit Kumar", 350)
bill.display()
