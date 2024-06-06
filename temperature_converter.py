def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Temperature Converter")
print("Celsius to Fahrenheit")
print("Fahrenheit to Celsius")

choice = input("Enter Choice (C/F) ")

if choice.upper() == "C":
    celsius = float(input("Enter temperature in Celsius "))
    print(celsius,"°C is", celsius_to_fahrenheit(celsius), "°F")
elif choice.upper() == "F":
    fahrenheit = float(input("Enter temperature in Fahrenheit "))
    print(fahrenheit,"°F is", fahrenheit_to_celsius(fahrenheit), "°C")
else:
    print("Invalid Input")
