import random
import psycopg2



# Establish connection parameters
hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'starwars_medical'

# Establish a connection
host=hostname,
user=username,
password=password,
dbname=database

def open_connection():
    return psycopg2.connect(
        host=hostname,
        user=username,
        password=password,
        dbname=database
    )


def close_connection(connection):
    connection.close()


def count_patients(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM blood_groups")
        return cursor.fetchone()[0]


def get_patients_by_blood_group(connection, blood_group):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM patients AS p JOIN blood_groups AS b ON p.blood_group_id = b.id WHERE b.type = %s", (blood_group,))
        return cursor.fetchall()

def insert_patient(connection, name, age, planet, blood_group):
    # Fetch the blood group ID based on the type
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM blood_groups WHERE type = %s", (blood_group,))
        result = cursor.fetchone()

        if result:
            blood_group_id = result[0]  # Extracting the blood group ID
            # Insert the patient with the fetched blood_group_id
            cursor.execute(
                "INSERT INTO patients (name, age, blood_group_id, planet) VALUES (%s, %s, %s, %s) RETURNING id",
                (name, age, blood_group_id, planet)
            )
            connection.commit()
            inserted_patient_id = cursor.fetchone()[0]  # Fetch the inserted patient ID
            print("Patient inserted successfully!")
            return inserted_patient_id  # Return the inserted patient ID
        else:
            print(f"Blood group '{blood_group}' not found.")
            return None




def verify_count(result):
    if isinstance(result, int):
        print("Success: Count is an integer, as expected.")
    else:
        print("Error: Count should be an integer.")


def verify_patient_list(result):
    if isinstance(result, list) and all(isinstance(item, dict) for item in result):
        print("Success: Patient list is a list of dictionaries, as expected.")
    else:
        print("Error: Patient list should be a list of dictionaries.")


def verify_insertion(result):
    if isinstance(result, int):
        print("Success: Inserted patient ID is an integer, as expected.")
    else:
        print("Error: Inserted patient ID should be an integer.")


def main():
    connection = open_connection()
    # !!! DO NOT MODIFY THIS FUNCTION !!!
    # ALL YOUR WORK SHOULD BE DONE IN THE 3 FUNCTIONS ABOVE

    # Possible new patients
    potential_new_patients = [
        {'name': 'Obi-Wan Kenobi', 'age': 57, 'planet': 'Stewjon', 'blood_group': 'A+'},
        {'name': 'Anakin Skywalker', 'age': 45, 'planet': 'Tatooine', 'blood_group': 'B+'},
        {'name': 'Padme Amidala', 'age': 46, 'planet': 'Naboo', 'blood_group': 'AB+'},
        {'name': 'Mace Windu', 'age': 64, 'planet': 'Haruun Kal', 'blood_group': 'O-'},
        {'name': 'Qui-Gon Jinn', 'age': 60, 'planet': 'Coruscant', 'blood_group': 'A-'}
    ]

    chosen_patient = random.choice(potential_new_patients)

    # Call and verify the functions
    count_result = count_patients(connection)
    verify_count(count_result)

    blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    chosen_blood_group = random.choice(blood_groups)
    patient_list_result = get_patients_by_blood_group(connection, chosen_blood_group)
    verify_patient_list(patient_list_result)

    insert_result = insert_patient(connection, **chosen_patient)
    verify_insertion(insert_result)

    # Close connection
    close_connection(connection)

if __name__ == '__main__':
    main()
