# Temperature Converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


print("===== Temperature Converter =====")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

try:
    choice = int(input("Enter your choice (1-6): "))
    temperature = float(input("Enter temperature: "))

    if choice in [2, 4, 5, 6] and temperature < 0:
        if choice in [5, 6] or choice == 4:
            print("Invalid temperature! Kelvin cannot be below 0.")
        else:
            print("Invalid temperature!")
    elif choice == 1:
        print(f"Result: {celsius_to_fahrenheit(temperature):.2f} °F")
    elif choice == 2:
        if temperature < -273.15:
            print("Invalid Celsius temperature!")
        else:
            print(f"Result: {celsius_to_kelvin(temperature):.2f} K")
    elif choice == 3:
        if temperature < -459.67:
            print("Invalid Fahrenheit temperature!")
        else:
            print(f"Result: {fahrenheit_to_celsius(temperature):.2f} °C")
    elif choice == 4:
        if temperature < -459.67:
            print("Invalid Fahrenheit temperature!")
        else:
            print(f"Result: {fahrenheit_to_kelvin(temperature):.2f} K")
    elif choice == 5:
        print(f"Result: {kelvin_to_celsius(temperature):.2f} °C")
    elif choice == 6:
        print(f"Result: {kelvin_to_fahrenheit(temperature):.2f} °F")
    else:
        print("Invalid choice! Please select 1-6.")

except ValueError:
    print("Please enter a valid number.")
