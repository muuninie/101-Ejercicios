#Anagrama

p1 = input("Ingrese primera palabra: ")
p2 = input("Ingrese segunda palabra: ")

p1.lower()
p2.lower()

if len(p1) == len(p2) and sorted(p1) == sorted(p2):
    print("Son anagramas!")
else:
    print("No son wajjj")

