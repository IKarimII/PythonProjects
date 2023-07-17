year = int(input("Enter the year to see if its a leap year "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a Leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a Leap Year")
else:
    print("It is not a leap year")