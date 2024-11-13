
import math

def numeros_primos(n):
    primos = []
    
    def eh_primo(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    
    for num in range(2, n + 1):
        if eh_primo(num):
            primos.append(num)
    
    return primos

n = 20
resultado = numeros_primos(n)
print("Números primos até {n}: {resultado}")
