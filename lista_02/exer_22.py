
def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
temperatura_fahrenheit = 77  
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)

print("{temperatura_fahrenheit}°F é igual a {temperatura_celsius:.2f}°C")
