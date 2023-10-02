def max_dominoes(m, n):
    if m % 2 == 0 or n % 2 == 0:
        return m * n // 2
    else:
        return (m * n - 1) // 2

m, n = map(int, input().split())
result = max_dominoes(m, n)
print(result)
