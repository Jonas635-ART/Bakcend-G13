cadenaCaracteres = "Hola Mundo"

print(cadenaCaracteres[1])
# H

print(cadenaCaracteres[:4])
# Hola

print(cadenaCaracteres[5:])
# Mundo

print(cadenaCaracteres[2:7])
# la Mu

# Convertir a mayúsculas
print(cadenaCaracteres.upper())
# HOLA MUNDO

# Convertir a minúsculas
print(cadenaCaracteres.lower())
# hola mundo

# Remover espacios en blanco al inicio y al final
print(cadenaCaracteres.strip())

# Reemplazar caracteres
print(cadenaCaracteres.replace("o", "0"))

# Dividir una cadena de caracteres
cadenaCaracteres = "Eduardo De Rivero"
print(cadenaCaracteres.split(" "))
primerNombre = cadenaCaracteres.split(" ")

# Formatear cadenas de caracteres

print("Hola {} bienvenido a Código {}".format(primerNombre[0], "Python"))
print(f"Hola {primerNombre[0]} bienvenido a Código Python")
miNombre = "Eduardo_De_Rivero"

# Imprimir la primera letra de mi nombre convertido en mayúscula y el resto en minúsculas

# Output esperado: Hola soy: EDUARDO de rivero

miNombreLista = miNombre.split("_")
nombreUpper = miNombreLista[0].upper()
apellidoLower = miNombreLista[1].lower()
apellido2Lower = miNombreLista[2].lower()
resultado = f"Hola soy: {nombreUpper} {apellidoLower} {apellido2Lower}"
print(resultado)