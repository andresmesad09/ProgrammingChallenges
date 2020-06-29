# -*- coding:utf-8 -*-

def main():
    print('¡B I E N V E N I D O!')
    dias = int(input('Ingresa la cantidad de días: '))

    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60

    if dias < 0:
        print('La cantidad de días no puede ser negativa')
    elif dias == 0:
        print('¿Qué es el tiempo? El fin es el principio y el principio es el fin\n NO PONGAS CERO DÍAS!!! ')
    elif dias == 1:
        print(f'{dias} día tiene {horas} horas, {minutos} minutos y {segundos} segundos.')
    else:
        print(f'{dias} días tienen {horas} horas , {minutos} minutos y {segundos} segundos.')


if __name__ == "__main__":
    main()