def fib(n):
    """returns the nth Fibonacci number"""
    sequence = [0, 1]
    for i in range(n + 1):
        value = sequence[-2] + sequence[-1]
        sequence.append(value)
    return sequence[n]
