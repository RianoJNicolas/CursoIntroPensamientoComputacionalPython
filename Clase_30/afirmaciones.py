def primera_letra(lista_de_palabras):
    primeras_letras = []
		
    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permite str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras


# CASO1
# listaPalabras = [1,2,3,4]
# print(primera_letra(listaPalabras))

# CASO2
listaPalabras = ['HOLA','MUNDO','QUE','TAL','ESTAS']
print(primera_letra(listaPalabras))

# CASO3
listaPalabras = ['','Hola']
print(primera_letra(listaPalabras))

