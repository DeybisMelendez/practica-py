hash_fibonacci = {}


def fibonacci(n):
    if n in hash_fibonacci:
        return hash_fibonacci[n]
    if n == 1:
        return 1
    elif n == 0:
        return 0
    result = fibonacci(n-1) + fibonacci(n-2)
    hash_fibonacci[n] = result
    return result


for i in range(100):
    print(fibonacci(i))
