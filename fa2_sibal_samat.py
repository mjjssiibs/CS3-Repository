class Patient:
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_bill_amount(self):
        return self._bill_amount

    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount

    def calculate_bill(self):
        return self._bill_amount


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self._bill_amount * 0.80


class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self._bill_amount * 0.85


regular_patient = Patient("Juan Dela Cruz", 15000.0)
senior_patient = SeniorPatient("Maria Santos", 15000.0)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000.0)

print("Hospital Billing System")
print("-----------------------")

print("Patient Name:", regular_patient.get_name())
print("Original Bill: ₱", regular_patient.get_bill_amount())
print("Final Bill: ₱", regular_patient.calculate_bill())
print()

print("Patient Name:", senior_patient.get_name())
print("Original Bill: ₱", senior_patient.get_bill_amount())
print("Final Bill: ₱", senior_patient.calculate_bill())
print()

print("Patient Name:", philhealth_patient.get_name())
print("Original Bill: ₱", philhealth_patient.get_bill_amount())
print("Final Bill: ₱", philhealth_patient.calculate_bill())