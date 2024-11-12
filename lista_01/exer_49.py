
def mdc_lista(lista):
    from functools import reduce
    return reduce(mdc,lista)

print(mdc_lista([48, 18, 30])) 