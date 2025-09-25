b = 11
summe = 0

if b % 2 == 0:  # even
    for a in range(2, b + 1, 2):
        summe += a
else:       # odd
    for a in range(2, b, 2):
        summe += a

print(summe)
