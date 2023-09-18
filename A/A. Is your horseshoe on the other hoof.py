s = list(map(int,input().split()))
unique = set(s)
resp = len(s) - len(unique) 
print(resp)