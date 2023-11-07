def mass_data_entry():
    patients_list = []

    patient_data = get_patient_data()
    patients_list.append(patient_data)

    return patients_list


def get_patient_data():
    ssn_numer = input("\nWhat is the patient's ssn: ")
    name = input("What is the patient's name: ")
    age = int(input("Age of patient: "))
    temperature = float(input("Temperature of patient: "))
    heart_rate = int(input("Heart rate of patient: "))
    sys_blood_pressure = int(input("Systolic blood pressure of patient: "))
    dys_blood_pressure = int(input("Dystolic blood pressure of patient: "))

    patient = {
        "Patient Name": name,
        "SSN Number": ssn_numer,
        "Age": age,
        "Temperature": temperature,
        "Heart Rate": heart_rate,
        "Systolic Blood Pressure": sys_blood_pressure,
        "Diastolic Blood Pressure": dys_blood_pressure
    }

    return patient


def index_patient_data(patient_data_list):
    indexed_data = {}

    for patient_data in patient_data_list:
        ssn_number = patient_data["SSN Number"]
        if ssn_number:
            indexed_data[ssn_number] = patient_data

    return indexed_data


def analyze_patient(ssn, indexed_data):
    for ssn, patient in indexed_data.items():
        name = patient['Patient Name']
        ssn_number = patient['SSN Number']
        age = patient['Age']
        temperature = patient['Temperature']
        heart_rate = patient['Heart Rate']
        sys_blood_pressure = patient['Systolic Blood Pressure']
        dys_blood_pressure = patient['Diastolic Blood Pressure']

    choice = input("Do you want to analyze temperature (t) or blood pressure (pb)? ")

    if choice == "t":
        analyze_temperature_age(age, temperature)
    elif choice == "bp":
        analyze_blood_pressure(sys_blood_pressure, dys_blood_pressure)


def analyze_temperature_age(age, body_temp):
    print("---------------------------------------------------")

    if age <= 10:
        if body_temp <= 35.5:
            print("The body temperature of your Patient is to low for their age.")
        elif body_temp <= 37.5:
            print("Your Patient has a normal body temperature for their age.")
        elif body_temp > 37.6:
            print("The body temperature of your Patient is to high for their age.")

    elif age <= 65:
        if body_temp <= 36.4:
            print("The body temperature of your Patient is to low for their age.")
        elif body_temp <= 37.6:
            print("Your Patient has a normal body temperature for their age.")
        elif body_temp > 37.6:
            print("The body temperature of your Patient is to high for their age.")

    elif age > 65:
        if body_temp <= 35.8:
            print("The body temperature of your Patient is to low for their age.")
        elif body_temp <= 36.9:
            print("Your Patient has a normal body temperature for their age.")
        elif body_temp > 36.9:
            print("The body temperature of your Patient is to high for their age.")


def analyze_blood_pressure(sys_blood_pressure, dys_blood_pressure):
    print("---------------------------------------------------")

    ideal_min_bp = (90, 60)
    ideal_max_bp = (120, 80)
    normal_max = (140, 90)

    if sys_blood_pressure < ideal_min_bp[0] or dys_blood_pressure < ideal_min_bp[1]:
        print("Low Blood Pressure")
    elif ideal_min_bp[0] <= sys_blood_pressure <= ideal_max_bp[0] and ideal_min_bp[1] <= dys_blood_pressure <= ideal_max_bp[1]:
        print("Optimal Blood Pressure")
    elif ideal_max_bp[0] <= sys_blood_pressure <= normal_max[0] and ideal_max_bp[1] <= dys_blood_pressure <= normal_max[1]:
        print("Normal Blood Pressure")
    elif sys_blood_pressure >= normal_max[0]:
        print("High Blood Pressure")
    else:
        print("Mild Hypertension")


def start_p4():
    patients_list = []

    quantity = int(input("How many patients do you want to add? "))

    for _ in range(quantity):
        patient_data = get_patient_data()
        patients_list.append(patient_data)

    indexed_data = index_patient_data(patients_list)

    while input("\nDo you want to analyze your patients' data? (y/n) ") == "y":
        ssn = input("\nPlease enter your patients SSN: ")
        if ssn in indexed_data:
            analyze_patient(ssn, indexed_data)
        else:
            print("Patient not found.")
    else:
        print("Goodbye :)")
