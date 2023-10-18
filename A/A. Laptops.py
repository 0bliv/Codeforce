n = int(input())
laptops = [tuple(map(int, input().split())) for _ in range(n)]
laptops.sort(key=lambda x: x[0])  # Sort laptops by price

happy_alex_found = False

for i in range(n - 1):
    if laptops[i][1] > laptops[i + 1][1]:
        happy_alex_found = True
        break

if happy_alex_found:
    print("Happy Alex")
else:
    print("Poor Alex")
