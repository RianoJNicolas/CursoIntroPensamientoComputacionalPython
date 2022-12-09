# contador = 0

## Loop infinito
# while contador < 10:
#     print(contador)

# while True:
#     print(contador)

## Correccion
# while contador < 10:
#     print(contador)
#     contador += 1

# ## Iteraciones anidadas - Loops anidados
# contador_externo = 0
# contador_interno = 0

# while contador_externo < 5:
#     while contador_interno < 6:
#         print(contador_externo, contador_interno)
#         contador_interno += 1

#     contador_externo += 1
#     contador_interno = 0

# Iteraciones anidadas con "break"
contador_externo = 0
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1

        if contador_interno >= 3:
            break

    contador_externo += 1
    contador_interno = 0