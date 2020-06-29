# -*- coding:utf-8 -*-

def main():
    print('¡B I E N V E N I D O!')
    mayor_a_1000 = float(input('Ingresa un número mayor a 1000: '))
    while mayor_a_1000 <= 1000:
        mayor_a_1000 = float(input('Ingresa de nuevo el número. Debe ser mayor a 1000: '))

    menor_a_100 = float(input('Ingresa un número menor a 100: '))
    while menor_a_100 >= 100:
        menor_a_100 = float(input('Ingresa de nuevo el número. Debe ser menor a 100: '))

    cociente = mayor_a_1000 // menor_a_100
    residuo = mayor_a_1000 % menor_a_100

    print(f'El {menor_a_100} cabe {cociente} veces en {mayor_a_1000} y sobran {residuo}.')

if __name__ == '__main__':
    main()