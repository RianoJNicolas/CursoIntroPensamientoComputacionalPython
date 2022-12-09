# Programa para imprimir los numeros impares (nones) 
# utilizando la funcion range

def nones(x):
    for i in range(1,x,2):
        print(i)


def run():
    limite = int(input('Ingresa el numero hasta donde quieras ver los numeros impares: '))
    nones(limite)


if __name__ == '__main__':
    run()
    
