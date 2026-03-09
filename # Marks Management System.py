# Marks Management System

stud = []

while True:
    print("\n--- Marks Management ---")
    print("1. Enter Student Marks")
    print("2. View Results")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter Student Name: ")

        m1 = int(input("Enter Marks for Subject 1: "))
        m2 = int(input("Enter Marks for Subject 2: "))
        m3 = int(input("Enter Marks for Subject 3: "))

        total = m1 + m2 + m3
        avg = total / 3

        if avg >= 90:
            gpa = 4.0
        elif avg >= 75:
            gpa = 3.5
        elif avg >= 60:
            gpa = 3.0
        elif avg >= 50:
            gpa = 2.5
        else:
            gpa = 0

        stud.append([name, m1, m2, m3, gpa])
        print("Result saved.")

    elif choice == 2:
        print("\n--- Student Results ---")
        for s in stud:
            print("Name:", s[0], "| Marks:", s[1], s[2], s[3], "| GPA:", s[4])

    elif choice == 3:
        print("Program Terminated")
        break

    else:
        print("Invalid choice")