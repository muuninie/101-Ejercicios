#Es primo

def es_primo(num):
    if num <= 2:
        return True
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

for i in range(1, 101):
    if es_primo(i):
        print(i, " -> Es primo")
    else:
        print(i, "-> No es primo")
    
    