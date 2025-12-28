p1 = input()
p2 = input()

p1.lower()
p2.lower()

if len(p1) == len(p2) and sorted(p1) == sorted(p2):
    print("Son anagramas!")
else:
    print("No son wajjj")

