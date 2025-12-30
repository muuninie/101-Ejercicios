#Área de un polígono

p = input("Ingrese el polígono: ")
p.lower()

if p != "triangulo":
    a = int(input("Ingrese la altura: "))
    l = int(input("Ingrese el largo: "))
    print("El área es: ", a*l)
else:
    b = int(input("Ingrese la base: "))
    h = int(input("Ingrese la altura: "))
    print("Él area es: ", (b*h)/2)