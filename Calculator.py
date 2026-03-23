while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition  2. Subtraction  3. Multiplication 4. Divisible  5. Exist")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Goodbye!👋")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result: ", num1 + num2)
    
    elif choice == '2':
        print("Result: ", num1 - num2)

    elif choice == '3':
        print("Result: ", num1 * num2)

    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result: ", num1 / num2)
    else:
        print("Invalid choice! Please select a valid option.")



