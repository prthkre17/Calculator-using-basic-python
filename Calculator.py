#Making a calcuator with input function.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CALCULATOR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Taking integer input from user.
while True:
    while True:
        first_number = input("Enter your first number: ")
        #Checking if first_number is an integer.
        try:
            first_number = int(first_number)
            break
        except ValueError:
            print("Please try again with an integer/number!")

    while True:
        second_number = input("Enter your second number: ")
        #Checking if seconf_number is an integer.
        try:
            second_number = int(second_number)
            break
        except ValueError:
            print("Please try again with an integer/number!")

#Here user will choose from the available operations.
    while True:
        print('''CHOOSE AN AVAILABLE OPERATION: 
        For Addition  ----------------------->  (+)    
        For Subtraction  -------------------->  (-)
        For Multiplication  ----------------->  (*)
        For Division  ----------------------->  (/)
        For Exponential  -------------------->  (**)
        For only Quotient  ------------------>  (//)
        For only Remainder  ----------------->  (%)''')

#User input
        operation = input("Enter Operation code: ")

#if and else to make the calculator work accordingly with the user.
        if operation == "+" :
            print("The addition of your two number is", first_number,"+",second_number,"=", first_number + second_number)
            break
        elif operation == "-" :
            print("The subtraction of your two number is", first_number,"-",second_number,"=", first_number - second_number)
            break
        elif operation == "*" :
            print("The multiplication of your two number is", first_number,"*",second_number,"=", first_number * second_number)
            break
        elif operation == "/" :
            print("The division of your two number is", first_number,"/",second_number,"=", first_number / second_number)
            break
        elif operation == "**" :
            print("The exponential of your two number is", first_number,"**",second_number,"=", first_number ** second_number)
            break
        elif operation == "//" :
            print("The quotient of your two number is", first_number,"//",second_number,"=", first_number // second_number)
            break
        elif operation == "%" :
            print("The remainder of your two number is", first_number,"%",second_number,"=", first_number % second_number)
            break
        else:
            print("Invalid input!!!! Please try again with correct operation from below!")

    continue_choice = input("Do you want to continue using this calculator? (yes/no): ").strip().lower()
    if continue_choice != "yes":
        print('''Thank you for using my calculator ;)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BYEEEE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        break
