def add(a, b):           #function for addition
    return a + b

def subtract(a, b):       #function for subtraction
    return a - b

def multiply(a, b):       #function for multiplication
    return a * b

def divide(a, b):          #function for division
    if b == 0:
        return "Error: Division by zero"
    return a / b

def get_numbers():       #function for getting 2 numbers from user
    while True:          #the loop will continue to execute 
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            return a, b


def main():            #main function
    while True:        #the loop will continue to execute
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")             #input from user for arithmetic operation
        
        if choice == '1':                                        #function for addition operation will be called
            a, b = get_numbers()            
            result = add(a, b)
            print(f"The result of {a} + {b} is: {result}")
        
        elif choice == '2':                                      #function for subtraction operation will be called 
            a, b = get_numbers()
            result = subtract(a, b)
            print(f"The result of {a} - {b} is: {result}")
        
        elif choice == '3':                                     #function for multiplication operation will be called
            a, b = get_numbers()
            result = multiply(a, b)
            print(f"The result of {a} * {b} is: {result}")
        
        elif choice == '4':                                       #function for division operation will be called
            a, b = get_numbers()
            result = divide(a, b)
            print(f"The result of {a} / {b} is: {result}")
        
        elif choice == '5':                                       #exit statement
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":            #__name__ means if the module name is main then it will call main() automatically
    main()                            # main() function called
