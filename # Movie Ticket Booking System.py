# Movie Ticket Booking System

movies = {
    "Interstellar": ["10:00 AM", "2:00 PM", "6:00 PM"],
    "Inception": ["11:00 AM", "3:00 PM", "7:00 PM"],
    "The Island": ["12:00 PM", "4:00 PM", "8:00 PM"]
}

seats = 25
booked = []

while True:
    print("\n--- Movie Ticket Booking ---")
    print("1. Check Movies and Showtimes")
    print("2. Book Ticket")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("\nAvailable Movies:")
        for m in movies:
            print(m, "Showtimes:", movies[m])

    elif choice == 2:
        select = input("Enter movie name: ")

        if select in movies:
            print("Available Showtimes:", movies[select])
            time = input("Select showtime: ")

            x = int(input("Select seat number (1-25): "))

            if x <= seats and x not in booked:
                name = input("Enter your name: ")
                booked.append(x)

                print("\n----- Booking Confirmation -----")
                print("Name:", name)
                print("Movie:", select)
                print("Showtime:", time)
                print("Seat Number:", x)
                print("Ticket Booked Successfully")
            else:
                print("Seat not available.")
        else:
            print("Movie not found.")

    elif choice == 3:
        print("Program Terminated")
        break

    else:
        print("Invalid choice")