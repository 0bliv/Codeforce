n = int(input())
s = input()
c = 0

for char in range(1,n):
    if s[char] == s[char-1]:
        c+=1


print(c)