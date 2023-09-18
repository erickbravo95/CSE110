from fractions import Fraction

temp_fahrenheit = float(input("What is the temperature in Fahrenheit? "))
temp_Celsius = (temp_fahrenheit - 32) * Fraction(5,9)
print(f"The temperature in Celsius is {temp_Celsius:.1f} degrees.")
