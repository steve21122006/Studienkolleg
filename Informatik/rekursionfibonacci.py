def fib(n):
    if n == 1:  # base
        return 0
    elif n == 2:
        return 1
    else:       # rekursiv
        return fib(n - 1) + fib(n - 2)

print(fib(3))
