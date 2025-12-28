#Fibonacci

a = 0 # n - 2
b = 1 # n - 1
c = 0 # n

for i in range(50):
    c = a + b
    a = b
    b = c
    print(i, "->", c)
