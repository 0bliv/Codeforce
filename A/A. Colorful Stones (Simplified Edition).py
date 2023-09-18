s = input()
c = input()
lisa = 1
j = 0

for i in range(len(c)):
    if s[j] == c[i]:
        lisa+=1
        j+=1
print(lisa)