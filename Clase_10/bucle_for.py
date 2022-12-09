# ciclo for con lista
myList = [1,2,3,4,5,6]
for item in myList:
    print(item)

# ciclo for con tupla
myTuple = (1,2,3,4,True,False,"hola","mundo")
for item in myTuple:
    print(item)

# ciclo for con diccionario
myDict = {"Colombia": 5000, "Ecuador": 1, "Peru": 6900, "Chile": 399}
for pais in myDict:
    print(pais)

for pais in myDict.keys():
    print(pais)

for moneda in myDict.values():
    print(moneda)

for pais, moneda in myDict.items():
    print(f"para el pais {pais}, 1 dolar equivale a {moneda} de su moneda local")

# Haciendo uso de break y continue
myList_2 = [1,2,3,4,5,6,7,8,9]
for item in myList_2:
    if item == 6:
        break
    elif item != 4:
        print(item)
        continue


