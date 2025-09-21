a = 0
b = 1
print(a)
print(b)
for _ in range(1, 100): # 100 ist für die Berechnung der ersten (100+2) Fibonacci-Zahlen
    a = a + b
    print(a)
    b = b + a
    print(b)
