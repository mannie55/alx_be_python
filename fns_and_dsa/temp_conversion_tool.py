FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    convert = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return convert

def convert_to_fahrenheit(celsius):
    convert = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return convert

temperature = float(input("Enter the temperature to convert: "))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temperature_type == "C":
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {fahrenheit}°F")
elif temperature_type == "F":
    celsius = convert_to_celsius(temperature)
    print(f"{temperature}°F is {celsius}°C")
else:
    raise ValueError("Invalid temperature. Please enter a numeric value.")