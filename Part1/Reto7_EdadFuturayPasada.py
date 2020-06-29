# -*- coding:utf-8 -*-

def main():
    print("!B I E N V E N I D O!")
    nombre = str(input('Ingresa tu nombre: '))
    edad =  int(input('Ingresa tu edad: '))

    print(f'{nombre} el año pasado tenías {edad - 1} años y el próximo año cumplirás {edad + 1} años')

if __name__ == "__main__":
    main()