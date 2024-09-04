# question 3 task 1 

leap_year = True
not_leap_year = False

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(leap_year)
        else:
            print(not_leap_year)
    else:
        print(leap_year)
else:
    print(not_leap_year)