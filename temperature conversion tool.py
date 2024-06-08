def celsius_to_fahrenheit(celsius):          #function for converting celcius to fahrenheit
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):       #function for converting celcius to fahrenheit
    return (fahrenheit - 32) * 5/9

def get_temperature():                       #function for getting temperature 
    while True:                              #the loop will continue to execute
            temperature = float(input("Enter the temperature: "))
            return temperature


def main():                          #main function
    while True:                     #the loop will continue to execute
        print("\nTemperature Conversion")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ")           #input from user for temperature conversion
        
        if choice == '1':                                  #function for converting celcius to fahrenheit will be called
            celsius = get_temperature()
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit}°F")
        
        elif choice == '2':                                #function for converting fahrenheit to celcius will be called
            fahrenheit = get_temperature()
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius}°C")
        
        elif choice == '3':                                #exit statement
            print("Exiting the temperature converter. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":                #__name__ means if the module name is main then it will call main() automatically
    main()                                # main() function called
