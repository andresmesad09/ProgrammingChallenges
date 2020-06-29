#-*- coding:utf-8 -*-

def main():
    print('¡B I E N V E N I D O!')
    tasa = 1.609344 #km/mi
    millas = float(input('Ingrese la cantidad de millas: '))
    kilometros = round(millas * tasa, 2)

    print(f'{millas} millas son {kilometros} km. Recuerda que una milla es {tasa} km.')

if __name__ == "__main__":
    main()