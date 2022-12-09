def run():
    nombre = input("Ingresa tu nombre: ")
    saludo = f'Hola {nombre}, un gusto hablar contigo'
    len_saludo = str(len(saludo))
    print(f'la longitud del saludo es: {len_saludo}')


if __name__ == '__main__':
    run()