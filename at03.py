def p(y):
    if (y%2)==0:
        return True
    else:
        return False
while True:
    n=int(input("digite um valor:"))
    if p(n):#chamando a funçao e adicionando outra variavel
        print("o numero é PAR: " ,n)
    else:
        print("o numero é impar: ",n)