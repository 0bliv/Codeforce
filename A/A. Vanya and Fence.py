n, h = map(int, input().split())
count = 0

heights = list(map(int, input().split()))

for a in heights:
    if a > h:
        count += 2
    else:
        count += 1

print(count)
