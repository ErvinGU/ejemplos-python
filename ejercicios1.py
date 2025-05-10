




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

precio_original = int(input("cual es el precio? : "))
descuento = float(input("cual es el porcentaje de descuento? : "))
precia_con_descuento = precio_original * (descuento / 100)
precio_final = precio_original - precia_con_descuento

print(f"precio con descuento es : {precio_final}")