n = int(input())
pi = list(map(int, input().split()))
gift_giver = [0] * n

for i in range(n):
    gift_giver[pi[i] - 1] = i + 1

print(*gift_giver)
