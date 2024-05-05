def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_num = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_num)
    return fib_series

n = 10
fib_series = fibonacci(n)
print(fib_series)
