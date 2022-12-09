# Programa que posee 3 opciones para realizar el calculo de una
# raiz cuadrada

def squareRoot_ExEn(objetivo):
    respuesta = 0
    mensaje = ' '

    while respuesta**2 < objetivo:
        respuesta += 1

        if respuesta**2 == objetivo:
            mensaje = f'La raiz cuadrada de {objetivo} es {respuesta}'
        else:
            mensaje = f'{objetivo} no tiene una raiz cuadrada exacta'

    return mensaje


def squareRoot_SolAprox(objetivo, epsilon):
    paso = epsilon**2   
    respuesta = 0.0
    mensaje = ' ' 

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

        if abs(respuesta**2 - objetivo) >= epsilon:
            mensaje = f'No se encontro la raiz cuadrada {objetivo}'
        else:
            mensaje = f'La raiz cuadrada de {objetivo} es {respuesta}'

    return mensaje


def squareRoot_BinarySearch(objetivo, epsilon):
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    mensaje = ' '

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    mensaje = f'La raiz cuadrada del numero {objetivo} es {respuesta}'
    return mensaje


def run():
    nombre = input('Hola, cual es tu nombre ? ')
    print(f'Hola de nuevo {nombre}, vas a seguir las siguientes instrucciones')
    print('Vamos a calcular la raiz cuadrada de un numero')
    print("""
        Tienes 3 opciones para calcularla:
        1) Calculamos por medio del algoritmo 'Enumeracion Exhaustiva'
        2) Calculamos una aproximacion al resultado real, utilizando el algoritmo 'Aproximacion de Soluciones'
        3) Calculamos una aproximacion al resultado real, utilizando el algoritmo 'Busqueda Binaria' 
    """)
    while(True):
        algoritmo = input('Elige una opcion: ')
        objetivo = 0
        if algoritmo == '1':
            objetivo = float(input('Escoge un numero entero: '))
            print(squareRoot_ExEn(objetivo))
            break
        elif algoritmo == '2':
            objetivo = float(input('Escoge un numero entero: '))
            epsilon = float(input('Ingresa la precision con la que deseas la respuesta: '))
            print(squareRoot_SolAprox(objetivo,epsilon))
            break
        elif algoritmo == '3':
            objetivo = float(input('Escoge un numero entero: '))
            epsilon = float(input('Ingresa la precision con la que deseas la respuesta: '))
            print(squareRoot_BinarySearch(objetivo,epsilon))
            break
        else:
            print('No ingresaste una opcion correcta')


if __name__ == '__main__':
    run()
