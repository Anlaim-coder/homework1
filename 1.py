temp_in_Celsius = float(input())

temp_Fahrenheit = (temp_in_Celsius * 1.8) + 32
temp_in_kelvin = temp_in_Celsius + 273.15

print(str(temp_in_kelvin) + "°C = " + str(round(temp_Fahrenheit,2)) + "°F")
print(str(temp_in_kelvin) + "°C = " + str(round(temp_in_kelvin,2)) + "K")
