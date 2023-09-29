# Read the input words
s = input().strip()
t = input().strip()

# Check if t is the reverse of s
if s == t[::-1]:
    print("YES")
else:
    print("NO")
