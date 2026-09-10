seat_type = input("Enter the seat type (general/ac/sleeper/luxury)" ).lower()
match seat_type:
    case "general":
        print("You have selected General seat. only seat is available.")
    case "ac":
        print("You have selected AC seat. Seat and food are available.")
    case "sleeper":
        print("You have selected Sleeper seat. Seat and food are available.")
    case "luxury":
        print("You have selected Luxury seat. Seat, food, and amenities are available.")
    case _:
        print("Invalid seat type selected.")