celcius = input("Enter the temperature in Celcius: ")

fahrenheit = (int(celcius) * 9//5) + 32

print("Temperature entered in Celcius: " + str(celcius) + "\N{DEGREE SIGN}C")
print("Temperature converted to Fahrenheit: " + str(fahrenheit) + "\N{DEGREE SIGN}F")