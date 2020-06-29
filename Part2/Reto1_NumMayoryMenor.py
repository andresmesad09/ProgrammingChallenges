# -*- coding:utf-8 -*-

def main():
    print('¡B I E N V E N I D O!')
    num1 = float(input('Ingresa el primer número: '))
    num2 = float(input('Ingresa el segundo número: '))

    if num1 == num2:
        print(f'{num1} y {num2} son iguales.')
    elif num1 > num2:
        print(f'{num1} es mayor a {num2}. Y la diferencia es de {num1 - num2}')
    else:
        print(f'{num2} es mayor a {num1}. Y la diferencia es de {num2 - num1}')

if __name__ == "__main__":
    main()