from hospital import Hospital, Patient, Doctor
import database
import utils

def main():
    hospital = Hospital()
    database.create_table()

    # Load existing patients from the file when the program starts
    saved_patients = utils.load_patients_from_file()
    for patient_data in saved_patients:
        patient = Patient(
            name = patient_data["name"],
            age = patient_data["age"],
            gender = patient_data["gender"],
            patient_id = patient_data["patient_id"],
            disease = patient_data["disease"]
        )
        hospital.add_patient(patient)

    # Load existing doctors from the file when the program starts
    saved_doctors = utils.load_doctors_from_file()
    for doctor_data in saved_doctors:
        doctor = Doctor(
            name = doctor_data["name"],
            age = doctor_data["age"],
            gender = doctor_data["gender"],
            doctor_id = doctor_data["doctor_id"],
            specialization = doctor_data["specialization"]
        )
        hospital.add_doctor(doctor)


    while True:
        print("\n Hospital Management System")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Display Patients")
        print("4. Display Doctors")
        print("5. Exit")

        choice = int(input("Enter your choice :"))

        if choice == 1:
            name = input("Enter patient name :")
            age = int(input("Enter age :"))
            gender = input("Enter gender :")
            disease = input("Enter disease :")
            patient = Patient(name,age,gender, len(hospital.patients)+1, disease)
            hospital.add_patient(patient)
            database.add_patient_to_db(name, age, gender, disease) # save  to database
            utils.save_patients_to_file(patient) # save to txt file

        elif choice == 2:
            name = input("Enter doctor name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            specialization = input("Enter specialization: ")
            doctor = Doctor(name, age, gender, len(hospital.doctors)+1, specialization)
            hospital.add_doctor(doctor)
            database.add_doctor_to_db(name, age, gender, specialization) # save  to database
            utils.save_doctors_to_file(doctor) # save to txt file

        elif choice == 3:
            print("Patients in system: ")
            patients = database.get_all_patients()
            for patient in patients:
                print(f"ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}, Gender: {patient[3]}, Disease: {patient[4]}")

        elif choice == 4:
            print("Doctors in system: ")
            doctors = database.get_all_doctors()
            for doctor in doctors:
                print(f"ID : {doctor[0]}, Name: {doctor[1]}, Age: {doctor[2]}, Gender: {doctor[3]}, Specialization: {doctor[4]}")
            #hospital.view_doctors()

        elif choice == 5:
            break

if __name__ == "__main__":
    main()