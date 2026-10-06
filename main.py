#Patient Class
class Patient:
    def __init__(self, name, patient_id, age, gender, diagnosis):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print("\n***** Patient Information *****")
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Diagnosis: {self.diagnosis}")

#hospital Class
class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.patients =[]

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully") 

    def display_patients(self):
        print("\n ********All Patients ********") 
        print(f"\n ***** {self.hospital_name} ******") 

        #check if there are patients
        if len(self.patients) == 0:
            print("No Patient Records Found.")
        else:
            for patients in self.patients:
                patients.display_info()      

#Patient Objects
patient1 = Patient("Saidu", "101", 23, "Male", "Poverty")
patient2 = Patient("Abu Turay", "102", 30, "Male", "Malaria")
patient3 = Patient("Yabom Turay", "103", 21, "Female", "Headache")

# Hospital Object
hospital1 = Hospital("City Hospital")
#Add patient to the hospital using add_patient method
hospital1.add_patient(patient1)
hospital1.add_patient(patient2)
hospital1.add_patient(patient3)

#Displaying all patients records in the hospital
hospital1.display_patients()