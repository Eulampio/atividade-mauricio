def maior(x,y):
    if x>y:
        return True
    elif y>x:
        return False
while True:
    x=int(input("digite um numero: "))
    y=int(input("digite um numero: "))
    if maior(x,y):
        print("o primeiro valor é maior")
    else:
        print("o segundo valor é menor ")