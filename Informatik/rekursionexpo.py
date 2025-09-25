def expo(n):
    if n == 0:  # base
        return 1
    else:       # rekursiv
        return expo(n - 1) * 2

print(expo(0))
