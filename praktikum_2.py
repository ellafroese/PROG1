def pulse_check():
    input_rates = input("Type all the heart rates you have messured (numbers only, without comma): ")

    heart_rates_list = list(map(int, input_rates.split()))
    normal_range = 0
    normal_rates_list = []
    abnormal_rates_list = []

    for r in heart_rates_list:
        if 60 <= r <= 100:
            normal_range = normal_range + 1
            normal_rates_list.append(r)
        else:
            abnormal_rates_list.append(r)

    print("These are all your messures heart rates: ", heart_rates_list, "\n"
            "These are all the normal heart rates: ", normal_rates_list, "\n"
            "These are all the not normal heart rates: ", abnormal_rates_list, "\n"
            "You have ", normal_range, " heart rates that are within the normal range.")


def dosage_reminder():

    for i in range(0,24):
        if i %4 == 0:
            print("Hour ", i, ": Take your medication")
        else:
            print("Hour ", i, ":")

def temperature_chart():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    body_temp = []
    above_average = {}

    for d in days:
        print("What was the body temperature on ", d, "?")
        temp = float(input("Temperature: "))
        body_temp.append(temp)

    average = sum(body_temp) / len(body_temp)

    for day, temp in zip(days, body_temp):
        if temp > average:
            above_average[day] = temp

    print("Days with above-average temperatures:")
    for day, temp in above_average.items():
        print(f"{day}: {temp}°C")

    print("The average temperature for the week is: ", average , "C")
    print(body_temp)


# -------------------------------------------------------------

def blood_vellesl_overlap():
    overlapping_counter = 0
    diagram = [[0 for _ in range(10)] for _ in range(10)]

    vessels = [
        [[0, 9], [5, 9]],
        [[8, 0], [0, 8]],
        [[9, 4], [3, 4]],
        [[2, 2], [2, 1]],
        [[7, 0], [7, 4]],
        [[6, 4], [2, 0]],
        [[0, 9], [2, 9]],
        [[3, 4], [1, 4]],
        [[0, 0], [8, 8]],
        [[5, 5], [8, 2]]
    ]

    for v in vessels:
        # Manhattan Distance
        distance = max(abs(v[0][0] - v[1][0]), abs(v[0][1] - v[1][1]))

        start_point_vessel = v[0]
        end_point_vessel = v[1]
        x = v[0][0]
        y = v[0][1]
        x_dir = 0
        y_dir = 0
        if start_point_vessel[0] < end_point_vessel[0]:
            x_dir = 1
        elif start_point_vessel[0] > end_point_vessel[0]:
            x_dir = -1
        if start_point_vessel[1] < end_point_vessel[1]:
            y_dir = 1
        elif start_point_vessel[1] > end_point_vessel[1]:
            y_dir = -1
        for i in range(distance):
            diagram[y][x] += 1
            x += x_dir
            y += y_dir

    print("Vessel representation:")
    for i in diagram:
        print("".join(str(x) for x in i))
        for j in i:
            if j > 1:
                overlapping_counter += 1
    print(f"There are {overlapping_counter} overlaps in this data.")
    print("To be healthy a tissue needs at least two vessels overlapping.")
    if overlapping_counter >= 2:
        print("This tissue is healthy.")
    else:
        print("This tissue is not healthy.")

# -------------------------------------------------------------

def execution_method():
    choice = int(input("What program do you want to execute? \n"
                       "Age pulse check (1), meds reminder (2), temperature calculator (3), vessel calculator (4) "))

    if choice == 1:
        pulse_check()
    elif choice == 2:
        dosage_reminder()
    elif choice == 3:
        temperature_chart()
    elif choice == 4:
        blood_vellesl_overlap()


def start_p2():
    while input("Do you want to calculate something (y/n)? ") == "y":
        execution_method()
    else:
        print("Goodbye :)")