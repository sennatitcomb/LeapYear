year = input("Enter a year: ")
if (year.isnumeric()):
    if year % 4 == 0:
        if year % 100 != 0:
            print("This is a leap year")
        else:
            if year % 400 == 0:
                print("This is a leap year")
            else:
                print("This is not a leap year")
    else:
        print("This is not a leap year")
else:
     print("That is not a valid input")
   
