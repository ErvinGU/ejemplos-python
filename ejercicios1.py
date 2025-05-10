import math as m




""" nombre = input("cual es tu nombre?")


edad = int(input("cual es tu edad?"))

print(f"el nombre de la persona es {nombre}\ny la edad es {edad}") """


""" #calculadora de IMC
#IMC = peso (en kg) / estatura² (en m²)
peso = float(input("cual es tu peso? : "))
altura = float(input("cual es tu altura? : "))

imc = peso / (altura ** 2)
print(f"el IMC es : {imc:.2f}") #.2f indica cantidad de decimales. """



#calculadora de descuento
#precio original × (porcentaje / 100) = descuento

""" precio_original = float(input("cual es el precio? : "))
descuento = float(input("cual es el porcentaje de descuento? : "))
precia_con_descuento = precio_original * (descuento / 100)
precio_final = precio_original - precia_con_descuento

print(f"precio con descuento es : {precio_final}") """


#calculadora promedio de notas
#x= n1 + n2 + n3 / n

""" nota1 = float(input("nota 1"))
nota2 = float(input("nota 2"))
nota3 = float(input("nota 3"))

promedio = (nota1 + nota2 + nota3) / 3 

print(f"el promedio de nota es : {promedio:.2f}") """


#area de un triangulo equilater0
#A = (√3 / 4) * L²

lado = float(input(f"longitud del lado del triangulo"))

area = (m.sqrt(3) / 4) * lado **2

print(f"Area del triangulo es : {area:.1f}")
