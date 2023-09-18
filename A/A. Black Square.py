n = list(map(int,input().split()))
s = input()
total = 0

for char in s:
    values = int(char)
    total+= n[values - 1]

print(total)
