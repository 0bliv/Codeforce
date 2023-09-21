n, k = map(int, input().split())

distinct_letters = [chr(ord('a') + i) for i in range(k)]

password = ""

for i in range(n):
    password += distinct_letters[i % k]

print(password)
