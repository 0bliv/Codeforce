n, k = map(int, input().split())

even_start = (n + 1) // 2
if k <= even_start:
    print(2 * k - 1)
else:
    k -= even_start
    print(2 * k)
