# Parking Lot Management System

capacity = 5
parking = []
rate = 20

while True:
    print("\n--- Parking Lot Menu ---")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Show Available Spots")
    print("4. Exit Program")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(parking) < capacity:
            vehicle = input("Enter Vehicle Number: ")
            hours = int(input("Enter expected parking hours: "))
            parking.append([vehicle, hours])
            print("Vehicle parked successfully.")
        else:
            print("Parking Lot Full!")

    elif choice == 2:
        vehicle = input("Enter Vehicle Number to exit: ")
        found = False

        for v in parking:
            if v[0] == vehicle:
                fee = v[1] * rate
                print("Parking Fee:", fee)
                parking.remove(v)
                print("Vehicle exited.")
                found = True
                break

        if not found:
            print("Vehicle not found.")

    elif choice == 3:
        available = capacity - len(parking)
        print("Available Spots:", available)

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")