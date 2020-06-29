# -*- coding:utf-8 -*-

def iniciateProgram():
    print('!B I E N V E N I D O!')
    a = int(input('Ingresa el primer número: '))
    b = int(input('Ingresa el segundo número: '))
    c = int(input('Ingresa el tercer número: '))

    suma = a + b
    multiplicacion = suma * c

    print(f'la suma de {a} y {b} es: {suma}. Y este valor multiplicado por {c} es: {multiplicacion}')

if __name__ == '__main__':
    iniciateProgram()