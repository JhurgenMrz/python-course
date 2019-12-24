def foreign_exchange_calculator(ammount):
    arg_to_col_rate = 0.0121
    return arg_to_col_rate*ammount

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos argentinos a dolares')
    print('')

    ammount = float(input('Ingresa la cantidad de pesos Argentinos: '))

    result = foreign_exchange_calculator(ammount)

    print('${} pesos argentinos son ${} dolares USD'.format(ammount, result))
    print('')

if __name__ == '__main__':
    run()