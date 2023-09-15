n = int(input())
magnets = [input() for _ in range(n)]

g = 1 

for i in range(1,n):
    if magnets[i] != magnets[i - 1]:
        g+=1

print(g)