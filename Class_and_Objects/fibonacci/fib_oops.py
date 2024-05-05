class Fibonacci:
    def __init__(self, n):
        self.n = n

    def generate_series(self):
        fib_series = [0, 1]
        for i in range(2, self.n):
            next_num = fib_series[i-1] + fib_series[i-2]
            fib_series.append(next_num)
        return fib_series

n = 10
fib_obj = Fibonacci(n)
fib_series = fib_obj.generate_series()
print(fib_series)
