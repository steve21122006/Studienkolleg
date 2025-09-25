import math
n = 29
a = 2
for a in range(2, int(math.sqrt(n)), 1):
    if n % a == 0:
        print("a")
        break
    else:
        print("b")
        break
