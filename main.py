from tabulate import tabulate

def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number.")

def print_student_table(students):
    headers = ["Roll No", "Name", "Age", "CGPA"]
    table = tabulate(students, headers=headers, tablefmt="fancy_grid")
    print(table)

students_list = []

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Search Details")
    print("3. Update Name")
    print("4. Update Age")
    print("5. Update CGPA")
    print("6. Delete")
    print("7. Show All Students")
    print("8. Exit")

    action = get_valid_integer_input('Enter your Selection: ')

    if action == 1:
        student_info = []
        print()
        roll_no = input('Enter Student Roll No: ')
        student_info.append(roll_no)

        name = input('Enter Student Name: ')
        student_info.append(name)

        age = get_valid_integer_input('Enter Student Age: ')
        student_info.append(age)

        cgpa = get_valid_float_input('Enter Student CGPA: ')
        student_info.append(cgpa)

        students_list.append(student_info)

    elif action in [2, 3, 4, 5, 6]:
        action_roll_no = input('Enter The Roll No. for the Selected Action: ')
        record_found = False

        for student in students_list:
            if student[0] == action_roll_no:
                record_found = True
                if action == 2:
                    print_student_table([student])

                elif action == 3:
                    new_name = input('Enter New Name for Student: ')
                    student[1] = new_name
                    print_student_table([student])

                elif action == 4:
                    new_age = get_valid_integer_input('Enter New Age for Student: ')
                    student[2] = new_age
                    print_student_table([student])

                elif action == 5:
                    new_cgpa = get_valid_float_input('Enter New CGPA for Student: ')
                    student[3] = new_cgpa
                    print_student_table([student])

                elif action == 6:
                    students_list.remove(student)
                    print('Student Deleted.')
                    break

        if not record_found:
            print('No Record Found!')

    elif action == 7:
        if not students_list:
            print('No Records Found!')
        else:
            print_student_table(students_list)

    elif action == 8:
        print('Program going to end. Exiting...')
        break

    else:
        print('Invalid input. Please enter a valid option.')