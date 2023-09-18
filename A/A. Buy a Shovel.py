k,r = map(int,input().split())
x = 1

while (k * x)% 10 != 0 and (k * x) % 10 != r:
    x+=1

print(x)

