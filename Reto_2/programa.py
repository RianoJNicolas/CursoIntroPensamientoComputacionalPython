def run():
    print('Vamos con los datos de la primera persona')
    nombre1 = input('Como es tu nombre: ')
    edad1 = int(input('¿Que edad tienes?: '))
    print('Vamos con los datos de la segunda persona')
    nombre2 = input('Como es tu nombre: ')
    edad2 = int(input('¿Que edad tienes?: '))

    if edad1 > edad2:
        print(f'{nombre1} es mayor que {nombre2}')
    elif edad2 > edad1:
        print(f'{nombre2} es mayor que {nombre1}')
    else:
        print(f'{nombre1} tiene la misma edad que {nombre2}')


if __name__ == '__main__':
    run()