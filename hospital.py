class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Patient(Person):
    def __init__(self, name, age, gender,patient_id,disease):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.disease = disease

class Doctor(Person):
    def __init__(self, name, age, gender,doctor_id,specialization):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialization = specialization


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self,patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added.")

    def add_doctor(self,doctor):
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} added.")

    def view_patient(self):
        for patient in self.patients:
            print(vars(patient))

    def view_doctors(self):
        for doctor in self.doctors:
            print(vars(doctor))