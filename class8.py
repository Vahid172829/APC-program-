class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee: ₹", self.consultation_fee)

    def total_bill(self, medicine_fee=0, test_fee=0):
        return self.consultation_fee + medicine_fee + test_fee


patient = Patient(101, "Sneha", 25, "Fever", 500)

patient.display()
print("Total Bill: ₹", patient.total_bill(300, 700))
