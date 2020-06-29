# -*- coding:utf-8 -*-

def suma(a, b):
    total = round(a + b, 2)
    return total

def iniciateSum():
    print('¡B I E N V E N I D O!')
    n1 = float(input('Ingresa el primer número: '))
    n2 = float(input('Ingresa el segundo número: '))

    print(f'La suma de {n1} + {n2} es {suma(n1, n2)}')

if __name__ == '__main__':
    iniciateSum()