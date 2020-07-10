# -*- coding: utf-8 -*-

def main():
    num1 = int(input('Escribe el primer número: '))
    num2 = int(input('Escribe el segundo número: '))
    
    if num2 < num1:
        print(f'El número {num2} se encuentra en el rango')
    else:
        print(f'El número {num2} excede el límite permitido')
    


if __name__ == '__main__':
    main()