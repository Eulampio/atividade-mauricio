
def potencia_recursiva(base, exp):
    if exp == 0:
        return 1
    return base * potencia_recursiva(base, exp - 1)


print(potencia_recursiva(2, 3))  