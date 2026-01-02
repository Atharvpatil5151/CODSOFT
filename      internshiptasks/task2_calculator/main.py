try:
    while True:
        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))
        op=input("Enter operation (+, -, *, /):")
        
        if op=='+':
            print(f"Addtion= {a+b}")
        elif op=='-':
            print(f"Subtraction = {a-b}")
        elif op=='*':
            print(f"Multiplication = {a*b}")
        elif op=='/':
            if b!=0:
                print(f"Division = {a/b}")
            else:
                print("Error: Division by zero")
        else:
            print("Invalid operation")  

        cont=input("Do you want to continue? (y/n): ").lower()
        if cont=='y':
            continue 
        elif cont=='n':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid input. Exiting the calculator. Goodbye!")
            break
except  ValueError:
    print("Invalid input. Please enter numeric values for numbers.")
except KeyboardInterrupt:
    print("\nCalculator interrupted. Goodbye!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
   
   