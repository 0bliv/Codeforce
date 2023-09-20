s = input()
s = s.replace('+','')
arr = []

for i in s:
    arr.append(int(i))

arr.sort()
result = '+'.join(map(str,arr))
print(result)