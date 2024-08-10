#question 1 task 1

number = int(input("Enter a number: ")) #input needed to be designated as integer

if number > 0:
    print("The number is positive.")
elif number == 0: #comparison operator needed to be changed to "=="
    print("The number is zero.")
else: #"number < 0" throws syntax error. "Expected ':'"
    print("The number is negative.")