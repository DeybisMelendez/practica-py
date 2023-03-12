from math import dist
print("--- Ingrese los valores del punto A ---")
x1 = int(input("Ingrese el valor de x1: "))
y1 = int(input("Ingrese el valor de y1: "))
print("--- Ingrese los valores del punto B ---")
x2 = int(input("Ingrese el valor de x2: "))
y2 = int(input("Ingrese el valor de y2: "))
print("La distancia entre el punto A y B es:", dist((x1, y1), (x2, y2)))
