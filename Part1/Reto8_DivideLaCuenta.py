# -*- coding:utf-8 -*-


def main():
    print('¡B I E N V E N I D O!')
    total_bruto = float(input('Indicame el total a pagar sin propinas y sin impuestos: '))
    personas = int(input('¿Entre cuantas personas vas a dividr la cuenta?: '))
    propina = float(input('¿Qué porcentaje de propinas vas a dar? (Expresado de 0 a 100): '))
    impuestos = float(input('Indicame el procentaje de impuestos (Expresado de 0 a 100): '))

    total_a_pagar = round(total_bruto + (propina / 100) * total_bruto + (impuestos / 100) * total_bruto, 2)
    total_individual = round(total_a_pagar / personas, 2)

    print(f'El total a pagar es {total_a_pagar}. Y como son {personas}, a cada una le corresponde pagar {total_individual}')

if __name__ == "__main__":
    main()