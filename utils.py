# utils.py

def save_patients_to_file(patient):
    with open('data/patients.txt','a') as file:
        file.write(f"{patient.patient_id},{patient.name},{patient.age},{patient.gender},{patient.disease}\n")


def load_patients_from_file():
    patients = []
    try:
        with open('data/patients.txt','r') as file:
            for line in file:
                patient_data = line.strip().split(',')
                patients.append({
                    'patient_id': int(patient_data[0]),
                    'name': patient_data[1],
                    'age': int(patient_data[2]),
                    'gender': patient_data[3],
                    'disease': patient_data[4],
                })
    except FileNotFoundError:
        print("No patient record found.")
    
    return patients


def save_doctors_to_file(doctor):
    with open('data/doctors.txt', 'a') as file:
        file.write(f"{doctor.doctor_id},{doctor.name},{doctor.age},{doctor.gender},{doctor.specialization}\n")




def load_doctors_from_file():
    doctors = []
    try:
        with open('data/doctors.txt', 'r') as file:
            for line in file:
                doctor_data = line.strip().split(',')
                doctors.append({
                    'doctor_id': int(doctor_data[0]),
                    'name': doctor_data[1],
                    'age': int(doctor_data[2]),
                    'gender': doctor_data[3],
                    'specialization': doctor_data[4],
                })
    except FileNotFoundError:
        print("No doctor record found.")
    return doctors
