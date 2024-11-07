print(" ") #Espacio
print("REYES MEZA ALAN EDUARDO 1207 : 3W") #Datos del programador
print(" ") #Espacio

# Definir la nota
nota = float(input("Introduce tu nota: "))

# Comprobar el rango de la nota y clasificar
if 0 <= nota < 5:
    print("SUSPENSO")
elif 5 <= nota < 6:
    print("SUFICIENTE")
elif 6 <= nota < 7:
    print("BIEN")
elif 7 <= nota < 9:
    print("NOTABLE")
elif 9 <= nota <= 10:
    print("SOBRESALIENTE")
else:
    print("NOTA NO VÁLIDA")
