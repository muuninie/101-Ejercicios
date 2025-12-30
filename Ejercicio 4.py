#Es primo

n = 1

for i in range(1, 101):
    if n%i == 1:
        print(n)
    n += 1