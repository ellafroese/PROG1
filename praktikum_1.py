import math
import random

# Im gesammten Programm wurden keine TryCatch statements gemacht,
#  da ich hier davon ausgehe, dass immer nur die korrenten Datentypen eingegeben werden :)

# Exercise 1
def age_calculator():
    age = int(input("How old are you? "))

    birthyear = 2023 - age
    hit_hundred = birthyear + 100

    print('you will turn 100 years old in the year: ', hit_hundred, 'you were born in ', birthyear)


# Exercise 2 and 4
def bmi_calculator():
    weight = int(input("What is your weight in kg? "))
    height = int(input("What is your height in cm? "))

    bmi = weight / (height / 100) ** 2
    bsa = math.sqrt((height * weight) / 3600)

    print("Your BMI is: ", bmi, " and your BSA is: ", bsa)

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("you are normal weight")
    elif bmi < 30:
        print("you are overweight")
    elif bmi > 30:
        print("you are obese")


# Exercise 3
def dosage_calculator():
    weight = float(input("What is your weight in kg? "))
    dosage_per_weight = float(input("How much can you take per kg (in mg)? "))

    dosage = float(weight * dosage_per_weight)
    print("The total dosage of the medicine the patient should take is: ", dosage, " mg.")
    intake = int(weight * dosage_per_weight) // 100
    print("you can take ", intake, " pills.")

    # Diese Aufgabe mit dem Defizit habe ich nicht ganz verstanden.
    # Daher stimmt wahrscheinlich diese Lösung nicht ganz
    deficit = 100 - dosage
    print("the deficit is the prescribed medicine is: ", deficit, " mg.")


# Exercise 5
def blood_pressure():
    systolic = int(input("what is your systolic blood pressure? "))
    diastolic = int(input("What is your diastolic blood pressure? "))

    if systolic == 0 and diastolic == 0:
        print("you are dead")
    elif (systolic > 180 and diastolic > 120) or (systolic > 180 or diastolic > 120):
        print("you have hypertension crisis blood pressure")
    elif systolic >= 140 or diastolic >= 90:
        print("you have hypertension stage 2 blood pressure")
    elif 130 <= systolic <= 139 or 80 <= diastolic < 89:
        print("you have hypertension stage 1 blood pressure")
    elif 120 <= systolic <= 129 and diastolic < 80:
        print("you have an elevated blood pressure.")
    elif systolic < 120 and diastolic < 80:
        print("You have a normal blood pressure.")


# Exercise 6
def rock_paper_scissors():
    print("Welcome to medical Rock, Paper; Scissors Game! \n"
          "Rules: Pill crushes, Scalpel, Scalpel cuts Prescription and Prescription covers Pill")

    choice = int(input("Choose between Pill (1), Scalpel (2) and Prescription(3): "))
    computer_choice = random.randint(1, 3)

    if choice == computer_choice:
        print("you both choose the same, no one wins.")
    elif choice == 1 and computer_choice == 2:
        print("Computer choose Scalpel, you win")
    elif choice == 1 and computer_choice == 3:
        print("Computer choose Prescription, you lose.")
    elif choice == 2 and computer_choice == 1:
        print("computer choose pill, you lose")
    elif choice == 2 and computer_choice == 3:
        print("computer choose Prescription, you win!")
    elif choice == 3 and computer_choice == 1:
        print("computer choose Pill, you win")
    elif choice == 3 and computer_choice == 2:
        print("computer choose Scalpel, you lose")


def execution_method():
    choice = int(input("What program do you want to execute? \n"
                       "Age calculator (1), bmi and bms calculator (2), blood pressure (3), dosage calculator (4) or play rock paper scissors (5)"))

    if choice == 1:
        age_calculator()
    elif choice == 2:
        bmi_calculator()
    elif choice == 3:
        blood_pressure()
    elif choice == 4:
        dosage_calculator()
    elif choice == 5:
        rock_paper_scissors()


def start_p1():
    while input("Do you want to calculate something (y/n)? ") == "y":
        execution_method()
    else:
        print("Goodbye :)")

