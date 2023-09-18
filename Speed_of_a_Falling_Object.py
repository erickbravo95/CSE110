import math 
print ("Welcome to the velocity calculator. Please enter the following: ")

Mass = float(input("\nMass (in kg): "))
Gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
Time = float(input("Time (in seconds): "))
Density_of_the_fluid = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
Cross_sectional_area = float(input("Cross sectional area (in m^2): "))
Drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c = (1 / 2) * Density_of_the_fluid * Cross_sectional_area * Drag_constant

velocity  = math.sqrt((Mass*Gravity)/c) * (1 - math.exp((-math.sqrt(Mass*Gravity*c)/Mass)*Time))

print (f"\nThe inner value of c is: {c:.3f}")
print (f"The velocity after {Time} seconds is: {velocity:.3f} m/s")
