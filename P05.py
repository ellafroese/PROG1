import csv
from datetime import datetime

filename = 'patient_records.csv'


def read_patient_records(filename):
    records = []
    with open(filename, 'r', newline='') as file:
        csv_dict_reader = csv.DictReader(file)
        for row in csv_dict_reader:
            records.append(row)
    return records


def view_patient_records(records):
    for row in records:
        patient_id = row['Patient ID']
        name = row['Name']
        dob = row['Date of Birth']
        height = row['Height']
        weight = row['Weight']

        print(f"Patient ID: {patient_id}, Name: {name}, Date of Birth: {dob}, Height: {height}, Weight: {weight}")



def add_patient_record(records):
    # Implement adding a new patient record
    print("Adding a new patient record:")
    new_record = {}
    while True:
        try:
            new_record['Patient ID'] = int(input("Enter Patient ID (numbers only): "))
            # Check if the Patient ID already exists
            for record in records:
                if record['Patient ID'] == str(new_record['Patient ID']):
                    print("Patient ID already exists. Please enter a different Patient ID.")
                    return

            break
        except ValueError:
            print("Invalid input. Please enter a valid number for Patient ID.")

    new_record['Name'] = input("Enter Name (letters only): ")
    while not new_record['Name'].isalpha():
        print("Invalid input. Name should only contain letters.")
        new_record['Name'] = input("Enter Name (letters only): ")

    while True:
        try:
            new_record['Date of Birth'] = input("Enter Date of Birth (YYYY-MM-DD): ")
            datetime.strptime(new_record['Date of Birth'], "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")

    while True:
        try:
            new_record['Height'] = float(input("Enter Height (numbers only): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for Height.")

    while True:
        try:
            new_record['Weight'] = float(input("Enter Weight (numbers only): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for Weight.")

    records.append(new_record)
    print("Patient record added successfully.")


def update_patient_record(records):
    # Implement updating an existing patient record
    print("Updating a patient record:")
    patient_id = input("Enter Patient ID to update: ")
    for record in records:
        if record['Patient ID'] == patient_id:
            record['Name'] = input("Enter updated Name: ")
            record['Date of Birth'] = input("Enter updated Date of Birth: ")
            record['Height'] = input("Enter updated Height: ")
            record['Weight'] = input("Enter updated Weight: ")
            print("Patient record updated successfully.")
            return
    print("Patient ID not found.")


def delete_patient_record(records):
    # Implement deleting a patient record
    print("Deleting a patient record:")
    patient_id = input("Enter Patient ID to delete: ")
    for record in records:
        if record['Patient ID'] == patient_id:
            records.remove(record)
            print("Patient record deleted successfully.")
            return
    print("Patient ID not found.")


def write_patient_records(filename, records):
    # Implement writing records to CSV file
    with open(filename, 'w', newline='') as file:
        fieldnames = ['Patient ID', 'Name', 'Date of Birth', 'Height', 'Weight']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(records)


def main():
    records = read_patient_records("patient_records.csv")
    while True:
        print("\nPatient Records Management System")
        print("1. Add Patient Record")
        print("2. View Patient Records")
        print("3. Update Patient Record")
        print("4. Delete Patient Record")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '2':
            view_patient_records(records)
        elif choice == '3':
            update_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '4':
            delete_patient_record(records)
            write_patient_records("patient_records.csv", records)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
