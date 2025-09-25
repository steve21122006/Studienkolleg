k = 2132134
a = len(str(k))
summe = 0
for i in range(a - 1, -1, -1):
    b = int(k / (10 ** i)) % 10
    summe += b
print(summe)
