print(" ") #Espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #Datos del programador
print(" ") #Espacio

# Almacenar el número en una variable
numero = int(input("Introduce el número para ver su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar utilizando un bucle y rangos
for i in range(1, 11):  # El rango va de 1 a 10 (inclusive)
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
