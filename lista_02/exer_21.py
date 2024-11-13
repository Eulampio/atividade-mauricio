
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = 25 
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

print("{temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F")
