n = int(input())
resp = 0

for i in range(n):
    s = input()
    if s == "X++" or s == "++X":
        resp+=1
    if s =="--X" or s =="X--":
        resp-=1

print(resp)