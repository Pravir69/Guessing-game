def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15
temp = float(input("Enter temperature value: "))
unit = input("Enter the unit (C/F/K): ").upper()

if unit == 'C':
    print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
elif unit == 'F':
    c = fahrenheit_to_celsius(temp)
    print(f"{temp}°F = {c:.2f}°C")
    print(f"{temp}°F = {celsius_to_kelvin(c):.2f}K")
elif unit == 'K':
    c = kelvin_to_celsius(temp)
    print(f"{temp}K = {c:.2f}°C")
    print(f"{temp}K = {celsius_to_fahrenheit(c):.2f}°F")
else:
    print("Invalid unit! Please enter C, F, or K.")
