# Ejercicio 1.6

billete_grosor = 0.11 * 0.001 # Metros (0.11 mm)
sears_altura = 442 # Altura (metros)
num_billetes = 1
dia = 1

while num_billetes * billete_grosor < sears_altura:
    print(dia, num_billetes, num_billetes * billete_grosor)
    dia = dia + 1
    num_billetes = num_billetes * 2

print ('Número de días', dia)
print ('Número de facturas', num_billetes)
print ('Altura final', num_billetes * billete_grosor)