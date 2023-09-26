n, k = map(int, input().split())
count = 0

for _ in range(n):
    ai = input().strip()
    digits = set(ai)

    is_k_good = all(str(digit) in digits for digit in range(k+1))

    if is_k_good:
        count += 1

print(count)
