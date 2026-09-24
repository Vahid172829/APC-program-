class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self, days):
        if not self.available:
            self.available = True
            charges = self.rental_rate * days
            print("Vehicle returned successfully.")
            print("Rental Charges: ₹", charges)
        else:
            print("Vehicle was not rented.")


vehicle = Vehicle("MH12AB1234", "Swift", 1500)

vehicle.rent()
vehicle.return_vehicle(3)
