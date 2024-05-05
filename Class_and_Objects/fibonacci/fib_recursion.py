def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
fib_series = [fibonacci(i) for i in range(n)]
print(fib_series)
