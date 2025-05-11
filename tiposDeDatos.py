#tipos de datos en phyton


""" ## listas ##

lista_de_numeros ={1,2,3,4,5,6,7,8,9}

frutas = ["manzana","uvas","peras",True,[1,2,3,[4,5,6]]]

frutas[4]

#modificar la lista
frutas[0] = "manzana"
frutas[3] = "uva"

#.append agrega un item al final de la lista
frutas.append("kiwi")

#insertar un elemento a un indice
frutas.insert(2, "banana")

#eliminar items
#.remove elimina por un valor
frutas.remove("banana")
#.pop para eliminar por indice
frutas.pop(4)


#ordenar
frutas.sort()
print(frutas) """


""" ##Diccionario

persona = {
    "nombre": "juan" , 
    "edad":35, 
    "ciudad":"talcahuano",
    "cursos":["html", "css","js"]
    }

#acceso al diccionario (dict)



print(persona["cursos"])

#modificar
persona["ciudad"] = "coronel"
print(persona)

#agregar nueva clave
persona["rut"] = "213343323-5"

del persona["rut"]

print(persona)

##sets

numeros = {1,2,3,4,5,6,7,8,9,4}

numeros.add(122) #se agrega 122

numeros.remove(122) #se quita el 122


print(numeros) """

## tuplas

colores = ("rojo", "verde", "azul")

#acceder a la tupla

print(colores[1])


