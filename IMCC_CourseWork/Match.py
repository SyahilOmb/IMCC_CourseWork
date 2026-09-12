day = int(input("enter a number :"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("holiday")