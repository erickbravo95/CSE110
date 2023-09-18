
def convert_Cel_to_Fah(celsius):
    return (celsius * 1.8) + 32

def wind_chill (temperature,wind_speed):
    return 35.74 + (0.6215 * temperature) - (35.75 * wind_speed ** 0.16) + ((0.4275 * temperature)* wind_speed ** 0.16)

temp = int(input("What is the temperature? "))
degrees = input("Fahrenheit or Celsius (F/C)? ")
mph = 5
if degrees == "F":
    for i in range(0, 60, 5):
        print(f"At temperature {temp}F, and wind speed {mph} mph, the windchill is: {wind_chill(temp,mph):.2f}F")
        mph += 5
else:
    for i in range(0, 60, 5):
        print(f"At temperature {convert_Cel_to_Fah(temp)}F, and wind speed {mph} mph, the windchill is: {wind_chill(convert_Cel_to_Fah(temp),mph):.2f}F")
        mph += 5



