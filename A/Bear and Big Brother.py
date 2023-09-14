a,b = map(int,input().split())
c = 0
if a == b:
    print(1)
else:
    while a <= b:
        b *= 2
        a *= 3
        c+= 1
    print(c)