def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

def fibo(i):
    results = {}
    fibo_dp(i, results)

def fibo_dp(i, results):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        try:
            return results[i]
        except KeyError:
            results[i] = fibo_dp(i - 1, results) + fibo_dp(i - 2, results)
            return results[i]

def fibo_up(i):
    if i == 0 or i == 1:
        return i

    a = 0
    b = 1
    c = 0
    for k in range(2, i + 1):
        c = a + b
        a = b
        b = c

    return c
